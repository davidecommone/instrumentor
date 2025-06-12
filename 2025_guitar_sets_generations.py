from instrumentor import FretboardExplorer

nkpb = FretboardExplorer()


nkpb.liutaio(6, 22, [64, 59, 55, 50, 45, 40])

#set1 = nkpb.all_voicings(["La","Re","Sol","Si","Mi"]) #1
#set7 = nkpb.all_voicings(["Sol#","Do#","Fa#","La#","Re#"]) #7
set4 = nkpb.all_voicings(["Fa#","Si","Mi","Sol#","Do#"]) #4
#set10 = nkpb.all_voicings(["Do","Fa","La#","Re","Sol"]) #10 
#set3 = nkpb.all_voicings(["Si","Mi","La","Do#","Fa#"]) #3
#set9 = nkpb.all_voicings(["Fa","La#","Re#","Sol","Do"]) #9
#set5 = nkpb.all_voicings(["Do#","Fa#","Si","Re#","Sol#"]) #5
#set11 = nkpb.all_voicings(["Sol","Do","Fa","La","Re"]) #11
#set6 = nkpb.all_voicings(["Re#","Sol#","Do#","Fa","La#"]) #6
#set12 = nkpb.all_voicings(["Re","Sol","Do","Mi","La"]) #12
#set2 = nkpb.all_voicings(["Mi","La","Re","Fa#","Si"]) #2
#set8 = nkpb.all_voicings(["La#","Re#","Sol#","Do","Fa"]) #8
#
#
#########################################################  SCENA 1
#
subset4 = nkpb.voicings_filter(set4,7)
for item in subset4:
    print(item)

nkpb.plot_voicings_heatmap(6,22,subset4,1,["La, Re, Sol, Si, Mi"])

#subset6 = nkpb.voicings_filter(set6, 9)
#for item in subset6:
#    print(item)
#
#subset11 = nkpb.voicings_filter(set11, 12)
#for item in subset11:
#    print(item)
#
#subset10 = nkpb.voicings_filter(set10, 17)
#for item in subset10:
#    print(item)
#
#subset7 = nkpb.voicings_filter(set7,15)
#for item in subset7:
#    print(item)
#
#subset9 = nkpb.voicings_filter(set9,8)
#for item in subset9:
#    print(item)
#
#subset12 = nkpb.voicings_filter(set12,7)
#for item in subset12:
#    print(item)
#
#nkpb.chord_plotter(subset4, "set4; posizioni con il tasto 7")
#nkpb.chord_plotter(subset6, "set6; posizioni con il tasto 9")
#nkpb.chord_plotter(subset11, "set11; posizioni con il tasto 12")
#nkpb.chord_plotter(subset10, "set10; posizioni con il tasto 17")
#nkpb.chord_plotter(subset7, "set7; posizioni con il tasto 15")
#nkpb.chord_plotter(subset9, "set9; posizioni con il tasto 8")
#nkpb.chord_plotter(subset12, "set12; posizioni con il tasto 7")
#
#
#######################################################   SCENA 2
#subset1 = nkpb.voicings_filter(set1,7)
#for item in subset1:
#    print(item)
#
#subset9 = nkpb.voicings_filter(set9, 10) 
#for item in subset9:
#    print(item)
#
#subset11 = nkpb.voicings_filter(set11, 12) 
#for item in subset11:
#    print(item)
#
#subset6 = nkpb.voicings_filter(set6, 18) 
#for item in subset6:
#    print(item)
#
#subset3 = nkpb.voicings_filter(set3,14) 
#for item in subset3:
#    print(item)
#
#subset10 = nkpb.voicings_filter(set10,10)
#for item in subset10:
#    print(item)
#
#subset2 = nkpb.voicings_filter(set2,7)
#for item in subset2:
#    print(item)
#
#
#
#nkpb.chord_plotter(subset1, "set1; posizioni con il tasto 7")
#nkpb.chord_plotter(subset9, "set9; posizioni con il tasto 10")
#nkpb.chord_plotter(subset11, "set11; posizioni con il tasto 12")
#nkpb.chord_plotter(subset6, "set6; posizioni con il tasto 18")
#nkpb.chord_plotter(subset3, "set3; posizioni con il tasto 14")
#nkpb.chord_plotter(subset10, "set10; posizioni con il tasto 10")
#nkpb.chord_plotter(subset2, "set2; posizioni con il tasto 7")
#
#
######################################################   SCENA 3
#
#subset2 = nkpb.voicings_filter(set2,7)
#for item in subset2:
#    print(item)
#
#subset7 = nkpb.voicings_filter(set7, 9)
#for item in subset7:
#    print(item)
#
#subset3 = nkpb.voicings_filter(set3, 12)
#for item in subset3:
#    print(item)
#
#subset6 = nkpb.voicings_filter(set6, 17)
#for item in subset6:
#    print(item)
#
#subset11 = nkpb.voicings_filter(set11,15)
#for item in subset11:
#    print(item)
#
#subset8 = nkpb.voicings_filter(set8,8)
#for item in subset8:
#    print(item)
#
#subset12 = nkpb.voicings_filter(set12,7)
#for item in subset12:
#    print(item)
#
#nkpb.chord_plotter(subset2, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset7, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset3, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset6, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset11, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset8, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset12, "set; posizioni con il tasto ")
#
#
#######################################################   SCENA 4
#
#subset3 = nkpb.voicings_filter(set3,18)
#for item in subset3:
#    print(item)
#
#subset6 = nkpb.voicings_filter(set6,13)
#for item in subset6:
#    print(item)
#
#subset11 = nkpb.voicings_filter(set11,7)
#for item in subset11:
#    print(item)
#
#subset8 = nkpb.voicings_filter(set8, 5)
#for item in subset8:
#    print(item)
#
#subset12 = nkpb.voicings_filter(set12,7)
#for item in subset12:
#    print(item)
#
#subset4 = nkpb.voicings_filter(set4,12)
#for item in subset4:
#    print(item)
#
#subset1 = nkpb.voicings_filter(set1,17)
#for item in subset1:
#    print(item)
#
#nkpb.chord_plotter(subset3, "set3; posizioni con il tasto 18")
#nkpb.chord_plotter(subset6, "set6; posizioni con il tasto 13")
#nkpb.chord_plotter(subset11, "set11; posizioni con il tasto 7")
#nkpb.chord_plotter(subset8, "set8; posizioni con il tasto 5")
#nkpb.chord_plotter(subset12, "set12; posizioni con il tasto 7")
#nkpb.chord_plotter(subset4, "set4; posizioni con il tasto 12")
#nkpb.chord_plotter(subset1, "set1; posizioni con il tasto 17")
#
#######################################################   SCENA 5
#
#subset1 = nkpb.voicings_filter(set1,7)
#for item in subset1:
#    print(item)
#
#subset3 = nkpb.voicings_filter(set3, 9)
#for item in subset3:
#    print(item)
#
#subset4 = nkpb.voicings_filter(set4, 12)
#for item in subset4:
#    print(item)
#
#subset12 = nkpb.voicings_filter(set12, 17)
#for item in subset12:
#    print(item)
#
#subset2 = nkpb.voicings_filter(set2,15)
#for item in subset2:
#    print(item)
#
#subset11 = nkpb.voicings_filter(set11,8)
#for item in subset11:
#    print(item)
#
#subset1 = nkpb.voicings_filter(set1,7)
#for item in subset1:
#    print(item)
#
#nkpb.chord_plotter(subset1, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset3, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset4, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset12, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset2, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset11, "set; posizioni con il tasto ")
#nkpb.chord_plotter(subset1, "set; posizioni con il tasto ")
#
#
#######################################################   SCENA 6
#
#subset5 = nkpb.voicings_filter(set5,9)
#for item in subset5:
#    print(item)
#
#subset6 = nkpb.voicings_filter(set6,9)
#for item in subset6:
#    print(item)
#
#subset4 = nkpb.voicings_filter(set4,9)
#for item in subset4:
#    print(item)
#
#subset1 = nkpb.voicings_filter(set1,9)
#for item in subset1:
#    print(item)
#
#subset2 = nkpb.voicings_filter(set2, 9)
#for item in subset2:
#    print(item)
#
#subset11 = nkpb.voicings_filter(set11,8)
#for item in subset11:
#    print(item)
#
#subset3 = nkpb.voicings_filter(set3,9)
#for item in subset3:
#    print(item)
#
#nkpb.chord_plotter(subset5, "set5; posizioni con il tasto 9")
#nkpb.chord_plotter(subset6, "set6; posizioni con il tasto 9")
#nkpb.chord_plotter(subset4, "set4; posizioni con il tasto 9")
#nkpb.chord_plotter(subset1, "set1; posizioni con il tasto 9")
#nkpb.chord_plotter(subset2, "set2; posizioni con il tasto 9")
#nkpb.chord_plotter(subset11, "set11; posizioni con il tasto 9 ")
#nkpb.chord_plotter(subset3, "set3; posizioni con il tasto 9")



# Clemens gadenstatter . STUDIES FOR A PORTRAIT , FOR SOLO ELECTRIC GUITAR: pagina 2 barrè damping.
# PHILIPPE Hurel Loops fo electric guitar
# Clara Iannotta - Fur & Bone
# Yaron Deutsche - chitarrista elettrico
# Pierluigi Billone - Sgorgo Y, Sgorgo Oo
# Sparking Orbit (2013) for solo electric guitar and live Electronics 





#utilizzare variazioni tra il numero di risonatori usati in modo percepibile es: 1/2 a 20/30


# Lachemann - Dal Niente - Clarinetto Bb

#idee per un brano per chitarra
# composizione: far stare bene insieme due cose che non c'entrano niente.
#Percorsi: chiusi, aperti
#Giustapposizioni: è possibile percepire un senso di struttura geometrica quando gli esemmlpari appartengono tutti alla stessa specie e differiscono per posizione, sfumature o dimensioni; se fossero tutti diversi .
