import sys
ALPHABET = {'A', 'C', 'G', 'N', 'T'}
MAX_SEQ_LEN = 1000

# ---------------------------------------------------------------------
# Helpers FASTA 
# ---------------------------------------------------------------------

def fasta_open_and_read_header(path: str) -> Tuple[Optional[TextIO], Optional[str]]:

    """
    Ouvre un fichier FASTA et lit l'en-tête.
    Retourne (fp, name) où :
      - fp est un fichier ouvert en lecture, positionné juste après l'en-tête
      - name est le nom de séquence sans le '>'
    En cas d'erreur : retourne (None, None).

    TODO : imprimer message d'erreur en cas d'erreur ou de problème de format 
    """
    try:
        fp = open(path, "r")
    except OSError:
        return None, None

    header = fp.readline()
    if header == "":
        fp.close()
        return None, None

    header = header.strip()
    if not header.startswith(">"):
        fp.close()
        return None, None

    name = header[1:]

    return fp, name


def fasta_read_bases(fp: Optional[TextIO], n: int) -> Optional[str]:

    """
    Lit au maximum n bases depuis le fichier fp.
    Ignore les caractères '\n' et '\r'.

    Retourne une chaîne contenant au plus n caractères.
    Retourne "" si fin de séquence.
    Retourne None en cas d'erreur de format (ex: second '>').

    TODO : imprimer message d'erreur en cas d'erreur ou de problème de format 
    """

    if fp is None:
        return None

    bases = []
    
    while len(bases) < n:
        c = fp.read(1)

        if c == "":
            # EOF
            break

        if c == "\n" or c == "\r":
            continue

        if c == ">":
            # deuxième en-tête inattendu
            return None

        bases.append(c)

    return "".join(bases)



# ---------------------------------------------------------------------
# Helpers CSV 
# ---------------------------------------------------------------------

def csv_open(path: str) -> Optional[TextIO]:

    """
    Ouvre le fichier CSV de sortie en écriture.
    Retourne fp ou None si erreur.

    TODO : imprimer message d'erreur en cas d'erreur
    """
    try:
        return open(path, "w")
    except OSError:
        return None


def csv_write_mutation(fp: TextIO, name: str, pos: int, ref: str, alt: str) -> None:

    """
    Écrit une substitution sur une ligne CSV.
    """

    fp.write(f"{name},{pos},{ref},{alt}\n")


def csv_close(fp: Optional[TextIO]) -> None:
    if fp is not None:
        fp.close()


# ---------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------

def main():
    # TODO: vérifier le nombre d'arguments et afficher un message si nécessaire

    path_ref = sys.argv[1]
    path_seq = sys.argv[2]
    path_out = sys.argv[3]

    # --- Ouverture des fichiers FASTA ---
    fp_ref, name_ref = fasta_open_and_read_header(path_ref)
    if fp_ref is None:
        return 1

    fp_seq, name_seq = fasta_open_and_read_header(path_seq)
    if fp_seq is None:
        fp_ref.close()
        return 1

    # TODO: vérifier que name_ref == name_seq (sinon erreur)
    # TODO: si erreur, fermer fp_ref et fp_seq et retourner un code != 0

    # --- Ouverture du CSV ---
    fp_out = csv_open(path_out)
    if fp_out is None:
        fp_ref.close()
        fp_seq.close()
        return 1

    # --- Lecture des séquences (phase 1: chargement complet autorisé) ---
    seq_ref = fasta_read_bases(fp_ref,MAX_SEQ_LEN)
    seq = fasta_read_bases(fp_seq,MAX_SEQ_LEN)

    # TODO: vérifier que seq_ref et seq ne sont pas None
    # TODO: si erreur, fermer tous les fichiers et retourner un code != 0

    # TODO:
    #  - vérifier que len(seq_ref) == len(seq)
    #  - vérifier que tous les caractères sont dans ALPHABET
    #  - comparer caractère par caractère
    #  - si substitution: appeler csv_write_mutation(fp_out, name_ref, i, seq_ref[i], seq[i])

    # --- Fermeture des fichiers ---
    csv_close(fp_out)
    fp_ref.close()
    fp_seq.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
