'''
Een gen is een sub-string van het genoom die begint na een triplet ATG 
en eindigt voor een triplet TAG, TAA of TGA.
Bovendien is de lengte van een gen-string een veelvoud van 3 en
het gen zelf bevat niet een van de triplets ATG, TAG, TAA of TGA.
Schrijf een programma dat alle genen uit onderstaande sequence toont. 
Controleer je antwoord met: assert (len(gene) == 42 or len(gene) == 12)
'''

genoom = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

sequenceStarted = False
sequenceStartIndex = 0
currentGene = ""

def processGene(gene):
        if(gene != "" and len(gene) % 3 == 0):
                print(f'Gene found: {gene}')
        else:
                print('Gene not multiple of 3')

for index, char in enumerate(genoom):
        if(char == 'A' and genoom[index : index + 3] == 'ATG'):
                sequenceStartIndex = index
                sequenceStarted = True

        if(sequenceStarted == True):
                if(char == 'T' and (genoom[index : index + 3] == 'TAG'
                        or genoom[index : index + 3] == 'TAA'
                        or genoom[index : index + 3] == 'TGA')):
                        sequenceStarted = False
                        processGene(currentGene)
                        currentGene = ""
                        continue
        
                if(index > sequenceStartIndex + 2):
                        currentGene += char