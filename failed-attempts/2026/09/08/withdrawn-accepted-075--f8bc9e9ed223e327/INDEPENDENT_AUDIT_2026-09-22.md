# Independent audit — 2026-09-22

**Assigned source:** `2026/09/08/075`  
**Disposition:** **FAIL**

## Correctness — PASS

I independently recomputed the row-, column-, and symbol-pair permutations directly from the committed raw Latin-square lists, using separately written code rather than the record's verifier.

For the 147 order-7 main-class representatives, all 147 inputs are Latin squares and the replay gives row-Hamiltonian index 37 only, column-Hamiltonian indices 37 and 39, symbol-Hamiltonian index 37 only, and atomic index 37 only; index 39 has counts `(15,21,15)`. For the 564 order-7 isotopy representatives, all 564 inputs are Latin and the replay gives row-Hamiltonian indices 67 and 300, column-Hamiltonian indices 67 and 294, symbol-Hamiltonian indices 67 and 365, and atomic index 67 only. For the committed first 300 order-8 main-class representatives, all 300 are Latin, none is Hamiltonian in any aspect, and each per-aspect maximum is 16. Thus the finite calculations reported by the record are correct for the committed lists.

## Originality — FAIL

The central complete-order-7 classification is already established in substance by Ian M. Wanless, *Perfect Factorisations of Bipartite Graphs and Latin Squares Without Proper Subrectangles*, Electronic Journal of Combinatorics 6 (1999), R9, DOI 10.37236/1441.

Wanless defines `nu(L)` as the number of row-Hamiltonian conjugates and states that it is a main-class invariant. He records `nu(C_p)=6` for the cyclic prime square. In the small-orders classification, he states that at order 7 there are precisely two relevant main classes, both containing pan-Hamiltonian squares, and identifies the noncyclic class `A_7` with `nu(A_7)=2`. Together with the cyclic class `C_7` with `nu=6`, this gives the same substantive order-7 main-class picture underlying this record: one class with `nu=6`, one with `nu=2`, and the remaining main classes with `nu=0`.

The record's exact McKay line numbers, orientation labels (row/column/symbol), and per-pair cycle counts annotate a particular representative ordering, but do not constitute a new main-class classification. The explicit atomic witness certifies a phenomenon already present in the prior classification.

## Scientific value — FAIL

After removing the already-known order-7 classification, the residual contribution is primarily a mapping from a fixed database ordering to aspect labels and cycle counts. That can be useful as a reproducibility annotation, but it is not a nontrivial new regime, classification, criterion, or meaningful improvement over the prior scientific result.

The order-8 component does not rescue the record: it examines only the first 300 of 283,657 main-class representatives and reports an arbitrary-prefix negative sample, with no inference about the unexamined classes. It therefore does not establish an order-8 classification or a new structural result.

No bounded correction of the existing claim leaves a result that is simultaneously original and of sufficient scientific value under this audit standard.

## Prior literature checked

- I. M. Wanless, *Perfect Factorisations of Bipartite Graphs and Latin Squares Without Proper Subrectangles*, Electronic Journal of Combinatorics 6 (1999), R9. DOI: https://doi.org/10.37236/1441.
- B. D. McKay, Latin-square combinatorial data: https://users.cecs.anu.edu.au/~bdm/data/latin.html.
- D. Allsop and I. M. Wanless, *Row-Hamiltonian Latin squares and Falconer varieties*, Proc. London Math. Soc. (2024), arXiv:2211.13826.

## Archive rationale

The mathematics in the finite replay is retained as evidence, but the record fails the originality and scientific-value axes. The complete original package is preserved in this failed-attempt archive together with this audit and the failure note.
