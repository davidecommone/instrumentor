from instrumentor import FretboardExplorer

guitar = FretboardExplorer()

guitar.liutaio(6,22,[40, 45, 50, 55, 59, 64])

######

guitar.all_positions("Do#",0,1)
guitar.all_positions("Do#3",1,1)

#######

chord = guitar.all_voicings(["Do#","Mi","Sol#","La#"])

for voicing in chord[0]:
    print(voicing)

guitar.chord_plotter(chord,"")

######

chord_filtered = guitar.voicings_filter(chord,7)

for voicing in chord_filtered:
    print(voicing)

guitar.chord_plotter(chord_filtered,"")

######

guitar.plot_voicings_heatmap(6,22,chord,0,["Do#","Mi","Sol#","La#"])

guitar.plot_voicings_heatmap(6,22,chord_filtered,1,["Do#","Mi","Sol#","La#"])
