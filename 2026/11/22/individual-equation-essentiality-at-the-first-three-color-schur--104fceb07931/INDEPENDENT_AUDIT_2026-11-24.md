# Independent mathematical audit

## correctness

PASS

The sum over z=2,...,14 of floor(z/2) is 49, with one test for a=b. I independently represented the 3^13 normalized ternary words as bits of a single integer. For each equation its violation mask is the union over hues of the intersection of the three position masks. Updating the zero- and one-defect masks by Z'=Z\B and O'=(O\B)∪(Z∩B) after each equation counts exhaustively, including when a=b. Final popcounts are 0 and 1350; intersecting O with each violation mask reproduced every one of the 49 CSV rows, with 29 positive rows and seven zeros ending at 14. Counts for 5+5=10 and 6+7=13 are 222 and 4 before normalization is undone. Cyclic relabeling gives exactly one representative with c(1)=0 per orbit of size three, hence 4050 named. The surviving [1,13] prefix mask independently gives six named-normalized classes, with the blocks in the result and 2,2,3 violations for the three possible hues of 14 up to permutation. Thus no one right-hand-side-14 deletion can suffice. Replay: python3 /workspace/branches/schur_bitset_reproduction.py <frozen directory>/critical_triples.csv. The frozen programs were inspected, not executed.

## originality

PASS

The threshold and the [1,13] rigidity are prior, and the seven endpoint zeros follow directly from that rigidity, so they are not counted as independent originality. The full 49-equation individual-deletion spectrum and the finite one-defect census are the distinct contribution on the sources inspected.

## value

PASS

The first unsatisfiable three-color Schur interval is canonical, not a chosen arbitrary cutoff. Single-equation sensitivity is an exact way to distinguish indispensable constraints from redundant constraints in that benchmark. The exact survivor multiplicities for all equations quantify how deletion changes the solution set, which a threshold, one UNSAT certificate, or one minimal core does not provide. The full census, not the already implied endpoint fact in isolation, supplies the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
