from dna_features_viewer.biotools import (extract_translation,
                                          reverse_complement)

def test_extract_translation():
    seq = 'ATGGACAGAACAATATAA'
    seq1 = "ATGC" + seq + "GTTC"
    seq2 = "ATGC" + reverse_complement(seq) + "GTTC"

    assert extract_translation(seq1, (4, 22)) == 'MDRTI*'
    assert extract_translation(seq2, (4, 22, -1)) == 'MDRTI*'[::-1]
