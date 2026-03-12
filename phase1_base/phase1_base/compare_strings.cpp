#include <cstdio>
#include <cstdlib>

#include "utils_fasta.h"
#include "utils_csv.h"


// Hypothèses de la phase 1 (voir énoncé)
static const size_t MAX_SEQ_NAME_LEN = 101; // 100 caractères + '\0'
static const size_t MAX_SEQ_LEN = 1000;     // max 1000 caractères


int main(int argc, char* argv[]) {
    
    // TODO: vérifier que 3 arguments soient donnés à l'exécutable et gérer correctement le cas contraire
    if (argc != 4) {
        return -1;
    }
    const char* path_ref = argv[1];
    const char* path_seq = argv[2];
    const char* path_out = argv[3];

    // --- Ouverture des fichiers FASTA ---
    FILE* fp_ref = nullptr;
    FILE* fp_seq = nullptr;

    char name_ref[MAX_SEQ_NAME_LEN];
    char name_seq[MAX_SEQ_NAME_LEN];

    FastaStatus fs;

    fs = fasta_open_and_read_header(path_ref, &fp_ref, name_ref, MAX_SEQ_NAME_LEN);
    
    // TODO: si fs n'est pas FASTA_OK, imprimer un message d'erreur explicite, fermer les fichiers ouverts et arrêter le programe
    if (fs != FASTA_OK) {
        return -1;
    }

    fs = fasta_open_and_read_header(path_seq, &fp_seq, name_seq, MAX_SEQ_NAME_LEN);
    // TODO: si fs n'est pas FASTA_OK, imprimer un message d'erreur explicite, fermer les fichiers ouverts et arrêter le programe
    if (fs != FASTA_OK) {
        return -1;
    }

    // TODO: vérifier que name_ref et name_seq sont identiques

    // --- Ouverture du fichier CSV ---
    FILE* fp_out = nullptr;

    CsvStatus cs;
    cs = csv_open(path_out, &fp_out);

    // TODO: si cs n'est pas CSV_OK, imprimer un message d'erreur, fermer les fichiers ouverts et arrêter le programe
    if (cs != CSV_OK) {
        return -1;
    }

    // --- Lecture des séquences en mémoire (phase 1 autorise le chargement complet) ---
    char seq_ref[MAX_SEQ_LEN];
    char seq[MAX_SEQ_LEN];

    size_t n_ref = 0;
    size_t n_seq = 0;

    fs = fasta_read_bases(fp_ref, seq_ref, MAX_SEQ_LEN, &n_ref);
    // TODO: si fs n'est pas FASTA_OK, imprimer un message d'erreur explicite, fermer les fichiers ouverts et arrêter le programe
    if (fs != FASTA_OK) {
        return -1;
    }

    fs = fasta_read_bases(fp_seq, seq, MAX_SEQ_LEN, &n_seq);
    // TODO: si fs n'est pas FASTA_OK, imprimer un message d'erreur explicite, fermer les fichiers ouverts et arrêter le programe
    if (fs != FASTA_OK) {
        return -1;
    }


    // TODO:
    //  - vérifier que n_ref == n_seq
    //  - vérifier que seq_ref[i] et seq[i] soient dans ALPHABET autorisé
    //  - comparer seq_ref[i] et seq[i]
    //  - appeler csv_write_mutation(...) si nécessaire avec  csv_write_mutation(fp_out, name_ref, i, seq_ref[i], seq[i])

    // --- Fermeture des fichiers de sortie ---
    csv_close(fp_out);
    fasta_close(fp_ref);
    fasta_close(fp_seq);

    return 0;
}
