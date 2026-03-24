#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main(int argc, char* argv[])
{

    int nombreargument = argc;

    if (nombreargument != 4)
    {
        cout << "verifier les arguments" << endl;
        return 1;
    }

    ifstream fichieraverifier(argv[2]);

    char nom_sequenceav[100];
    char sequence_av[1000];

    fichieraverifier.getline(nom_sequenceav, 100);
    fichieraverifier.getline(sequence_av, 1000);

    // enlever >
    memmove(nom_sequenceav, nom_sequenceav + 1, strlen(nom_sequenceav));



    ifstream fichier_de_reference(argv[1]);

    char nom_de_reference[100];
    char sequence_de_reference[1000];

    fichier_de_reference.getline(nom_de_reference, 100);
    fichier_de_reference.getline(sequence_de_reference, 1000);

    // enlever >
    memmove(nom_de_reference, nom_de_reference + 1, strlen(nom_de_reference));



    if (strcmp(nom_sequenceav, nom_de_reference) != 0)
    {
        cout << "nom différent" << endl;
        return 1;
    }
    else
    {
        if (strlen(sequence_av) != strlen(sequence_de_reference))
        {
            cout << "longueur différente" << endl;
            return 1;
        }
        else
        {

            ofstream fichier_de_verification(argv[3]);

            for (int i = 0; i < strlen(sequence_de_reference); i++)
            {
                if (sequence_de_reference[i] != sequence_av[i])
                {

                    fichier_de_verification 
                        << nom_de_reference << ","
                        << i << ","
                        << sequence_de_reference[i] << ","
                        << sequence_av[i]
                        << endl;
                }
            }

            fichier_de_verification.close();
        }
    }

    fichieraverifier.close();
    fichier_de_reference.close();

    return 0;
}