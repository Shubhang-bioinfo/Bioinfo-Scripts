# Input the DNA sequence when prompted 
input_01 = input("Enter the DNA Sequence for Transcription\n").upper()
input_02 = input_01.strip().replace(" ", "" )
for bases in input_02:
    if bases not in input_02:
        print("Invalid DNA Sequence")
else:
    var1 = input_02.replace("T", "U")
## Printing the Transcribed DNA Sequence
print(len(input_02))
print("Transcribed DNA Sequence: ", var1)
