# Enter your Nucleotide seuence when prompted
test_01 = input("Please enter the string: \n").upper()
test_01 = test_01.strip().replace(" ", "")
valid_bases = ['A', 'C', 'T', 'G']
for base in test_01:
    if base not in valid_bases:
        print("Invalid base!")
        break
else:
    print("Valid string!")
    a = test_01.count('A')
    c = test_01.count('C')
    g = test_01.count('G')
    t = test_01.count('T')
    print("A: ",a)
    print("G: ",g)
    print("T: ",t)
    print("C: ",c)

  # Printing the output
