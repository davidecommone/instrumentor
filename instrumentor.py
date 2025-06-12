from pyswip import Prolog
import itertools, abjad, re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm, LinearSegmentedColormap



prolog = Prolog()



def mtoname(midi_note,outputmode): #converte un valore MIDI in una stringa con il nome della nota con o senza l'ottava
    note_names = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
    octave = (midi_note // 12) - 2  
    names_index = midi_note % 12
    
    name_octave = f"{note_names[names_index]}{octave}"
    cname = str(note_names[names_index])
    if outputmode == 1:
        return name_octave
    else:
        return cname
    
    
    
def nametom(nota):  # converte il nome di una nota + l'ottava in un valore MIDI
    note_base = {'Do': 0,'Do#': 1,'Re': 2,'Re#': 3,'Mi': 4,'Fa': 5,'Fa#': 6,'Sol': 7,'Sol#': 8,'La': 9,'La#': 10,'Si': 11}

    # Separare il nome della nota dall'ottava
    match = re.match(r"([A-Za-z#b]+)(-?\d+)", nota)
    if not match:
        raise ValueError(f"Formato nota non valido: {nota}")

    nome_nota = match.group(1)
    ottava = int(match.group(2))

    if nome_nota not in note_base:
        raise ValueError(f"Nota sconosciuta: {nome_nota}")

    semitono = note_base[nome_nota]
    midi_number = 12 * (ottava + 2) + semitono 

    return midi_number
    


def miditoabjad(midivalue): # converte i valori MIDI (0-127) in valori relativi al Do3 (il do centrale è l'asse), quindi 60 == 0
    converted = midivalue - 60
    #if midivalue > 60:
    #    converted = midivalue - 60
    #elif midivalue < 60 or midivalue == 60:
    #    converted = 60 - midivalue
    return int(converted)



class FretboardExplorer: 


    """ 
    """
 

    def liutaio(self,n_strings, n_frets, tunings=[]): #costruisce il manico dello strumento dato un numero di tasti, corde e relative accordature
        if n_strings != len(tunings):
            print("Error, size of tunings list doesn't match strings number")
            return
        
        for s in range(n_strings):
            for f in range(n_frets + 1):
                if f == 0:
                    cordavuota = "CV" #il tasto 0 equivale ad una corda vuota
                else:
                    cordavuota = "CT" #tutte le altre sono tastate
                nextfret = int(tunings[s]) + f
                pitch_name = mtoname(nextfret,1)
                note_name = mtoname(nextfret,0)
                neck_pos = f"position({s+1},{f},'{pitch_name}','{note_name}','{cordavuota}')"  # position(corda, tasto, pitch, nota, cordavuota) PITCH=nome nota+ottava, NOTA=solo nome della nota,come classe di altezze
                prolog.assertz(neck_pos)
        
    
        
    def all_positions(self,n_tofind,mode=0,printout=0): #restituisce tutte le posizioni sul manico di un pitch all_positions("Do4",1) o di una nota in tutte le ottave possibili allpositions("Do")
        positions = []
    
        if mode == 1:
            query = f"position(S, F, '{n_tofind}', C, CS)"  
            for solution in prolog.query(query): 
                retrieved_pos = f"Corda: {solution['S']}, Tasto: {solution['F']}, Tipo: {solution['CS']}"
                positions.append(retrieved_pos)
        else:
            query = f"position(S, F, N, '{n_tofind}', CS)"  
            for solution in prolog.query(query): 
                retrieved_pos = f"Corda: {solution['S']}, Tasto: {solution['F']}, Pitch: {solution['N']}, Tipo: {solution['CS']}"
                positions.append(retrieved_pos)
        
        if printout == 1:
            print(f"{n_tofind}; {len(positions)} posizioni trovate:")
            for item in positions:
                print(item)
        else:
            pass
                    
        return positions
    
    
    
    def all_voicings(self,chordnotes=[]):  # trova tutte le posizioni di tutti i rovolti possobili sul manico della lista di note inserita su chordnotes
        if not chordnotes or len(chordnotes) < 2:
            print("all_voicings() ERROR: Chord notes list is not valid")
            return []
    
        all_pos_dict = {note: self.all_positions(note) for note in chordnotes} #dizionario con i nomi delle note (come chiavi) e la lista restituita da all_positions (come valori)
    
        all_combinations = list(itertools.product(*all_pos_dict.values())) #permutazioni, costruzione dei rivolti
        
        valid_voicings = []
        id_counter = 1 
    
        for combination in all_combinations: 
            positions = []
            for pos in combination:
                parts = pos.split(", ")
                string = int(parts[0].split(": ")[1])
                fret = int(parts[1].split(": ")[1])
                tipo = str(parts[3].split(": ")[1])
                positions.append((string, fret, tipo))
    
            strings = [pos[0] for pos in positions] # una corda == una nota 
            if len(strings) != len(set(strings)): 
                continue
    
            frets = [pos[1] for pos in positions] # regola dei 3 tasti
            tipi = [pos[2] for pos in positions]
            if "CV" in tipi:
                frets_no_open = [f for f, t in zip(frets, tipi) if t != "CV"]
                if not frets_no_open:
                    valid_voicings.append((combination,id_counter))
                    id_counter += 1
                    continue
                delta = max(frets_no_open)-min(frets_no_open)
                if delta <= 3:
                    valid_voicings.append((combination,id_counter))
                    id_counter += 1
                    continue
            else:
                delta = max(frets) - min(frets)
                if delta <= 3:
                    valid_voicings.append((combination,id_counter))
                    id_counter += 1
                else:
                    continue
                
        out_buffer = []
        print(f"{len(valid_voicings)} rivolti trovati per le note {chordnotes}:")
        for voicing, voicing_id in valid_voicings:
            #print(voicing)
            out_buffer.append((voicing, voicing_id))
    
        return valid_voicings,out_buffer
    
    
    
    def voicings_filter(self, allvoicings, tasto_scelto): # filtra l'output in uscita da all_voicings cercando solo i rivolti che hanno il tasta_scelto come posizione di almeno una nota dell'accordo
        valid_voicings_out = allvoicings[0]  # Lista dei voicing validi con ID
        filtered_voicings = []
        seen_voicings = set() 
    
        for voicing, voicing_id in valid_voicings_out: 
            frets = []
            for pos in voicing:
                fret = int(pos.split(", ")[1].split(": ")[1])
                frets.append(fret)
            prolog.assertz(f"voicing({frets})")
            
        query = f"voicing(Frets), member(Tasto, Frets), (Tasto = {tasto_scelto})" #query
        for solution in prolog.query(query):
            frets_filtered = solution["Frets"]
            
            for voicing, voicing_id in valid_voicings_out:
                voicing_frets = [int(pos.split(", ")[1].split(": ")[1]) for pos in voicing]
                if voicing_frets == frets_filtered:
                    if voicing_id not in seen_voicings: # Controllo della ridondanza
                        filtered_voicings.append((voicing, voicing_id))
                        seen_voicings.add(voicing_id)  # Aggiungi l'ID al set
    
        print(f"{len(filtered_voicings)} rivolti trovati che includono il tasto {tasto_scelto}:")
        return filtered_voicings
    
    
    
    def chord_extractor(self, voicing_buffer):  # prende l'output di voicing_filter ed elimina le informazioni inutili, creando solo una lista di note+ottava e ID del voicing
        chord =[]
        
        for data in voicing_buffer:
            voicing_infos, id_finale = data
            note_estratte = []
            for info in voicing_infos:
                match = re.search(r"Pitch: ([A-Za-z#b]+[0-9\-]*)", info)
                if match:
                    nota = match.group(1)
                    note_estratte.append(nota)
    
            chord.append((note_estratte, id_finale))
        
        return chord
    
    
    
    def chord_plotter(self, voicing_buffer,subtitle): # stampa in notazione musicale i tutti i rivolti passati da voicing_buffer
    
        notes_coll = self.chord_extractor(voicing_buffer)
        container = abjad.Container()
        main_score = abjad.Score()
    
        header = r""" #(set-global-staff-size 14)
        \header {
        composer = \markup {} 
        title = \markup {NeckProbe - Chords Plotting}
        subtitle = \markup {"""+subtitle+"""}
        }
        """
    
        preamble = r"""
        \layout {
            \context {
                \Staff
                \override VerticalAxisGroup.staff-staff-spacing.minimum-distance = 11
            }       
            \context {
                \Score
                \override SpacingSpanner.strict-spacing = ##t
                \override SystemStartBar.stencil = ##f
                \override Stem.stencil = ##f
                \override TextScript.staff-padding = 5
                \override TimeSignature.transparent = ##t
                proportionalNotationDuration = #(ly:make-moment 1 16)
            }
        }
        """
        plotting_index = 0
        for item in notes_coll:
            midinote_list = []
            name_list, id_num = item
            
            for item in name_list:
                midinote = nametom(item)
                midinote_list.append(midinote)
            
            voicing_chord = abjad.Chord()
            voicing_chord.note_heads = [miditoabjad(item) for item in midinote_list]
            container.append(voicing_chord)
            mark = r"\markup \with-color #blue"
            mark = mark + r" { ID: \sub" + str(id_num) + "}" #\hspace #-0.55
            iteration_mark = abjad.Markup(mark)
            abjad.attach(iteration_mark, container[plotting_index] , direction=abjad.UP)
        
            abjad.attach(abjad.BarLine("||"), container[-1])
    
            main_score.append(container)
            plotting_index += 1
        
        abjad.attach(abjad.Clef("treble_8"), container[0])
        abjad.attach(abjad.TimeSignature((1, 4)),container[1]) 
    
        lilypond_file = abjad.LilyPondFile([header,preamble,container])
        abjad.show(lilypond_file)
    


    def plot_voicings_heatmap(self, n_strings, n_frets, voicings, set_or_subset, chordnoteslist=[]):   # crea un grafico di tipo heatmap delle posizioni trovate sul manico dei rivolti

        heatmap = np.zeros((n_strings, n_frets + 1))

        if set_or_subset == 0:
            voicings = voicings[0]
        else:
            pass

        for voicing_tuple in voicings:
            if isinstance(voicing_tuple, tuple):
                voicing = voicing_tuple[0]
            else:
                voicing = voicing_tuple
            for position in voicing:
                parts = position.split(", ")
                string = int(parts[0].split(": ")[1]) - 1
                fret = int(parts[1].split(": ")[1])
                heatmap[string, fret] += 1

        base_colors = ['#080037', '#00bfff', '#00ff00', '#ff0000'] 
        n_bins = int(np.max(heatmap)) + 1
        cmap = LinearSegmentedColormap.from_list("custom_meteo", base_colors, N=n_bins)

        plt.figure(figsize=(20, 4))
        img = plt.imshow(
            heatmap,
            cmap=cmap,
            aspect='auto',
            extent=[0, n_frets + 1, 0, n_strings],
            interpolation='nearest'
        )

        for i in range(n_frets + 2):
            plt.axvline(x=i, color='gray', linestyle='-', alpha=0.7, linewidth=1)

        for i in range(n_strings):
            plt.axhline(y=i + 0.5, color='gray', linestyle=':', alpha=0.7, linewidth=1)

        plt.xticks(
            ticks=np.arange(n_frets + 1),
            labels=[str(i) for i in range(n_frets + 1)],
            fontsize=10,
            fontweight='bold'
        )

        plt.yticks(np.arange(n_strings) + 0.5, ['Mi', 'La', 'Re', 'Sol', 'Si', 'Mi'])

        cbar = plt.colorbar(img, ticks=[0, np.max(heatmap)])
        cbar.ax.set_yticklabels(['0', str(int(np.max(heatmap)))])
        cbar.set_label('Frequenza di utilizzo', fontsize=12, fontweight='bold')

        plt.xlabel('Tasti', fontsize=12, fontweight='bold')
        plt.ylabel('Corde', fontsize=12, fontweight='bold')
        plt.title(
            f"Distribuzione delle posizioni per l'accordo: {', '.join(chordnoteslist)}",
            fontsize=14, fontweight='bold', pad=20
        )
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.tight_layout()
        plt.show()


# Prompt:
# crea una documentazione in stile readMe di Github di questo modulo, soffermandoti sui dettagli sulla siintassi e la guida all'uso.
# crea inoltre un breve testo di assistenza alla sintassi da inserire tra le """""" sotto la classe e tutte le sue funzioni, in modo l'editor di testo e il compilatore possano visualizzarlo durante l'attività di programmazione