dna = "GATATATGCATATACTT"
motif = "ATAT"

for dna in range(1, len(dna), 4):
    if dna == motif:
        print("yay")

