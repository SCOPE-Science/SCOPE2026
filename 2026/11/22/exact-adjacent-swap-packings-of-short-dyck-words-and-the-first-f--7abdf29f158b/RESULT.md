# Exact adjacent-swap packings of short Dyck words and the first fractional gap

## Finding

Let \(\mathcal D_m\) denote the Dyck words of semilength \(m\), encoded with `0` as an opening parenthesis and `1` as a closing parenthesis. Let \(B(w)\) consist of \(w\) and all words obtained from \(w\) by swapping one pair of unequal adjacent letters. A one-adjacent-swap-correcting Dyck code is a subset \(C\subseteq\mathcal D_m\) with \(B(u)\cap B(v)=\varnothing\) for distinct \(u,v\in C\).

For \(m=1,2,3,4,5\), the exact maximum code sizes are respectively
\[
(A_m)_{m=1}^5=(1,1,2,4,9).
\]
The natural output-shadow fractional packing relaxation has the exact respective optima
\[
(P_m)_{m=1}^5=\left(1,1,2,4,\frac{19}{2}\right).
\]
Thus semilength \(5\), corresponding to length-ten words, is the **first** semilength with a strict gap between the fractional and integral optima for the code-size objective. The gap is \(\frac12\). The first semilength at which the relaxation has a fractional vertex is instead \(3\). There are **exactly eleven** labeled maximum nine-word codebooks at semilength five, of which **nine** are invariant under reversal followed by bit-complementation; the other two are exchanged by that involution.

| Semilength \(m\) | Dyck source words | Distinct possible channel outputs | Maximum code size \(A_m\) | Fractional optimum \(P_m\) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 1 | 1 |
| 2 | 2 | 4 | 1 | 1 |
| 3 | 5 | 10 | 2 | 2 |
| 4 | 14 | 28 | 4 | 4 |
| 5 | 42 | 84 | 9 | \(19/2\) |

## Assumptions and scope

The alphabet is precisely \(\{0,1\}\). A Dyck word has \(m\) zeroes and \(m\) ones and in every prefix the number of zeroes is at least the number of ones. A channel error is at most one swap of *adjacent* letters in the source word, with a no-error outcome included. Non-Dyck words are permitted and counted as channel outputs, though their constraints in the packing problem are redundant, as shown below. Swapping equal adjacent letters leaves the word unchanged and introduces no additional outcome. Codebooks are sets of distinct, indexed binary strings, not rotation classes. Symmetry is reversal with simultaneous exchange of zero and one, which preserves the Dyck condition.

## Proof

For each semilength \(m\), index the \(C_m\) source words in \(\mathcal D_m\) and the possible outputs in \(U_m=\bigcup_{w\in\mathcal D_m}B(w)\). Define the binary incidence matrix \(H_m\) with \((H_m)_{z,w}=1\) precisely when \(z\in B(w)\). Any one-swap-correcting code is an integral feasible packing
\[
\max\sum_w x_w\quad\text{such that}\quad H_mx\le\mathbf1,\quad x_w\in\{0,1\}.
\]
Relax to nonnegative rational \(x_w\) with no integrality condition. The weak-duality certificate is any nonnegative rational \(y_z\) such that \(H_m^{\mathsf T}y\ge\mathbf1\): then \(\sum_wx_w\le\sum_zy_z\). Each of the five instances in `certificates.json` supplies an explicit sparse primal vector \(x\), an explicit sparse dual vector \(y\), and a feasible integral codebook. All omitted coordinates equal zero. Exact rational verification of the incidence inequalities, objective equality, and disjoint output shadows is performed by `verify_rational.py` without relying on a numerical optimizer. Its source-word and output generation also establishes the displayed source and output counts.

For \(m\le4\), primal-dual equality and a codebook meeting that value imply the exact integer optimum. For \(m=5\), both rational objectives equal \(19/2\), hence an integer code contains at most \(\lfloor19/2\rfloor=9\) words. The nine-word witness in the data file attains this upper bound, while a fractional packing attaining \(19/2\) proves a strict code-size objective gap.

**Non-Dyck outputs.** A swap can change the height of only one prefix. The only way it creates a negative height is to swap a `01` at height zero to `10`. Thus every non-Dyck output has the form \(A\,10\,B\), where \(A,B\) are Dyck words (possibly empty), and the location of `10` is determined by the unique negative prefix. Its unique Dyck preimage is \(A\,01\,B\). The output constraint merely bounds this preimage's variable by one, which the no-error output constraint already implies. The number of non-Dyck outputs at semilength \(m\) is \(\sum_{i=0}^{m-1}C_i C_{m-1-i}=C_m\), so the total number of outputs is \(2C_m\).

**First fractional vertex.** For semilengths one and two, some output is shared by all source words, so the relaxation is the simplex \(x\ge0,\ \sum_w x_w\le1\). At semilength three, in lexicographic source order \((000111,001011,001101,010011,010101)\), take \(x=(0,1/3,1/3,1/3,1/3)\). The five Dyck output constraints, in that same order, have left sides
\[
 x_1+x_2,\quad x_1+x_2+x_3+x_4,\quad x_2+x_3+x_5,\quad
 x_2+x_4+x_5,\quad x_3+x_4+x_5.
\]
All are at most one. Non-Dyck outputs give no new constraints. The last four output constraints are tight and, together with \(x_1=0\), uniquely determine \(x\): they set each three-element sum of \(x_2,x_3,x_4,x_5\) equal to one. Thus \(x\) is a vertex. Its value \(4/3<2\) explains why this fractional vertex does not force a code-size objective gap.

To classify equality cases, let two distinct Dyck words be adjacent in the *compatibility graph* when their output shadows are disjoint. Correcting codes are exactly its cliques. The script `verify_classification.py` independently generates all 42 length-ten Dyck words and their output shadows, builds every compatibility edge by direct set intersection, and enumerates **every maximal clique** by a Bron–Kerbosch search with a pivot. The recursion maintains disjoint sets of eligible and excluded vertices; every maximal clique is reached once, since each branch selects one eligible vertex and excludes it from later branches. It finds 3,582 maximal cliques, of which exactly eleven have maximum size nine, and compares their full word lists with `certificates.json`. Applying the reversal-complement involution to each of those eleven lists shows that nine are fixed and two are exchanged. The exhaustive count is exact and finite, without extrapolation to larger semilength.

## Verification

The package contains `certificates.json`, `verify_rational.py`, and `verify_classification.py`. From the directory containing these files run:

```sh
python verify_rational.py
python verify_classification.py
```

Both use only Python's standard library and check the supplied embedded data. The first validates, using exact fractions, all ten families of primal and dual inequalities, matching objectives, source and output counts, and integral witnesses at semilengths one through five. The second uses a separate Dyck generator and shadow map to reproduce the eleven optimal codebooks and their symmetry counts. The proof of optimality depends on the exact rational inequalities and complete finite enumeration, not on floating-point optimization logs. The earlier fractional vertex is verified directly by the tight constraints displayed above.

## Relationship to prior work

Adjacent-transposition correction and Kendall-type coding are established topics. Buzaglo and Etzion (first publicly posted August 21, 2014) treat permutation codes in the Kendall metric rather than the present Catalan-restricted binary codebooks. Gabrys, Yaakobi and Milenkovic (first publicly posted January 26, 2016) study binary deletion/transposition code constructions, but not the exact five-semilength Dyck shadow-packing relaxation. Gómez Soto, Leaños, Ríos-Castro and Rivera study the two-one constant-weight layer through a path-token-graph packing formulation; the length-ten Dyck layer has five ones and a prefix restriction. Mütze's Gray-code survey documents adjacent-transposition Gray codes on Dyck words, which concern traversing the word graph, not disjoint radius-one balls. These results supply the mathematical context but do not state the eleven optimal ten-bit codebooks or the fractional value \(19/2\).

The enumerated deletion-shadow packing for the same Dyck source family is a **different channel**: a deletion shortens the output whereas an adjacent swap preserves length and weight. Indeed, among the 42 length-ten Dyck words, the two confusability graphs have 77 swap-only edges and 88 deletion-only edges, as checked by `verify_classification.py`; neither graph includes the other. Neither code size nor linear packing certificate transfers just by implication between the two incidence matrices. This result therefore does not claim a new general one-deletion code theorem, nor does it infer novelty merely from a changed name or presentation.

## Limitations

The result concerns exactly semilengths one through five. It does not establish a formula for arbitrary semilength, optimal algorithms for large instances, or a general relaxation gap. Codebook counts refer to labeled, indexed source words; quotienting by any additional symmetry would yield a different enumeration. Prior work may contain unindexed finite computations or supplementary tables that were not available in the inspected research sources. A finite computational proof only certifies the stated finite domain, not its extension.

## References

1. S. Buzaglo and T. Etzion, *Bounds on the Size of Permutation Codes with the Kendall \(\tau\)-Metric*. arXiv:1408.4963, initial public submission August 21, 2014. https://arxiv.org/abs/1408.4963
2. R. Gabrys, E. Yaakobi and O. Milenkovic, *Codes in the Damerau Distance for Deletion and Adjacent Transposition Correction*. arXiv:1601.06885, initial public submission January 26, 2016. https://arxiv.org/abs/1601.06885
3. J. M. Gómez Soto, J. Leaños, L. M. Ríos-Castro and L. M. Rivera, *The packing number of the double vertex graph of the path graph*, arXiv:1711.03682, first posted November 10, 2017. https://arxiv.org/abs/1711.03682
4. T. Mütze, *Combinatorial Gray codes—an updated survey*. Electronic Journal of Combinatorics 30(3), 2023, #DS26, §4.4. https://doi.org/10.37236/11023
