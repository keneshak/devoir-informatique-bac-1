
import sys 

nombreargument= sys.argv
if len(nombreargument) !=4 :
    
    print ("verifier les arguments")

    sys.exit()


fichieraverifier=open(sys.argv[2],'r')
nom_sequenceav = fichieraverifier.readline()
sequence_av= fichieraverifier.readline()
sequence_av=sequence_av.strip()
nom_sequenceav = nom_sequenceav [1:]
a = nom_sequenceav.strip() 
nom_sequenceav=a                        

fichier_de_reference=open(sys.argv[1],'r')
nom_de_reference= fichier_de_reference.readline()
nom_de_reference=nom_de_reference[1:]
nom_de_reference=nom_de_reference.strip()
sequence_de_reference =fichier_de_reference.readline()
sequence_de_reference=sequence_de_reference.strip()



if nom_sequenceav!= nom_de_reference:
    print("nom différent")
   
    sys.exit()
else:
    if len(sequence_av) != len(sequence_de_reference):
        print("longueur différente")
        
        sys.exit()
    else:

        fichier_de_verification = open (sys.argv [3],'w')
        for i in range (0,len(sequence_de_reference)):
            if sequence_de_reference[i]!= sequence_av [i]:
                
                fichier_de_verification. write( f"{nom_de_reference},{i},{sequence_de_reference[i]},{sequence_av[i]}\n")
                
        fichier_de_verification.close()  
fichier_de_reference.close()
fichieraverifier.close() 





