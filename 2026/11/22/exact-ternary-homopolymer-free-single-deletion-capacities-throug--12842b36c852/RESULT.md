# Exact ternary homopolymer-free single-deletion capacities through length seven

## Finding

Let \(\Sigma=\{0,1,2\}\). For \(n\geq1\), let \(H_n\) be all length-\(n\) words \(w=w_1\cdots w_n\) with \(w_i\ne w_{i+1}\) for every \(1\leq i<n\). Let \(D(w)\) be the **set of distinct** words obtained by deleting exactly one coordinate from \(w\). A code \(C\subseteq H_n\) corrects one unknown-position deletion precisely when \(D(u)\cap D(v)=\varnothing\) for all distinct \(u,v\in C\). Define \(M_n\) as its maximum possible cardinality.

The exact capacities are

\[
(M_1,M_2,M_3,M_4,M_5,M_6,M_7)=(1,1,3,4,8,12,22).
\]

The corresponding optimum \(P_n\) of the ordinary fractional *deletion-shadow packing* relaxation, defined below, is

\[
(P_1,P_2,P_3,P_4,P_5,P_6,P_7)=\left(1,\frac32,3,\frac92,\frac{42}{5},\frac{27}{2},\frac{99}{4}\right).
\]

In particular, \(n=7\) is the shortest blocklength that permits at least \(16\) messages while forbidding every repeated neighboring symbol and correcting an arbitrary single deletion. At this length the integrality gap is \(P_7-M_7=11/4\). The explicit optimal \(22\)-word code is in `optimal_codebooks.json`.

## Assumptions and scope

The alphabet is **labeled and ternary**. Input symbols must differ at neighboring positions; received words are **not** assumed to satisfy that constraint. A deletion can occur at any one position, is not marked, and its exact position is unknown to the decoder. All codewords have equal length. Claims of exact optimum concern only \(1\leq n\leq7\), and there is no assertion about the optimal number of codebooks or about longer lengths.

For \(n\geq2\), let \(R_n=\bigcup_{w\in H_n}D(w)\). The primal fractional relaxation is

\[
P_n=\max\left\{\sum_{w\in H_n}x_w:\ x_w\geq0,\ \sum_{w:y\in D(w)}x_w\leq1\quad(y\in R_n)\right\}.
\]

Its dual minimizes \(\sum_{y\in R_n}z_y\) subject to \(z_y\geq0\) and \(\sum_{y\in D(w)}z_y\geq1\) for every \(w\in H_n\). At \(n=1\), all three possible source letters produce the same empty word, giving \(M_1=P_1=1\).

## Proof

**Deletion shadows.** For a word with unequal neighboring symbols, deleting two different indices cannot produce the same descendant: equality of the two length-\((n-1)\) results would require all symbols between the two positions to be identical. Therefore \(|D(w)|=n\), and the receiver constraint is exactly pairwise disjointness of these shadows. All \(|H_n|=3\cdot2^{n-1}\) words are generated without duplication by choosing the first symbol freely and each following symbol from the other two.

**Reduction to clique optimization.** Form the compatibility graph \(G_n\) on \(H_n\); join two distinct vertices if their deletion shadows are disjoint. Any correcting code is precisely a clique. The file `verify_exact.cpp` constructs this graph independently from the definitions, then computes its maximum clique exactly for every \(2\leq n\leq7\). The computed maximum values, and their upper-bound certification, are reproduced in `VERIFICATION.md`. Each associated codeword set is supplied in `optimal_codebooks.json` and its shadows can be checked directly.

**Why the finite algorithm proves an upper bound.** At a recursion node, the maintained clique \(K\) is adjacent to every vertex in the remaining candidate set \(S\). Greedy proper coloring of the compatibility graph induced by \(S\) partitions its vertices into independent color classes. Any clique in \(S\) contains at most one vertex from each class, so a prefix carrying \(c\) colors cannot extend \(K\) by more than \(c\) vertices. The recursion examines candidates in reverse order of this color ordering. When processing one vertex \(v\), its extension candidates are exactly \(S\cap N(v)\); afterward \(v\) is removed. The pruned branches have certified upper bound no greater than the largest clique already found, so no larger clique can be lost. Every other branch is visited. Thus the returned maxima are exhaustive finite proofs rather than inference from a time limit. An independent incidence-matrix mixed-integer optimization, `alternate_milp.py`, returns the same proven optima.

**Fractional values.** The file `fractional_certificate.json` records explicit nonnegative rational primal input weights and dual output weights for \(2\leq n\leq7\), indexed by their literal words. The pure-Python exact checker `verify_fractions.py` regenerates the entire input/output incidence relation, verifies every primal constraint, every dual constraint and equality of the two objectives in rational arithmetic. Weak duality then proves all listed \(P_n\) without floating-point assumptions. For example \(P_7=99/4\) while the exact integer optimum is \(22\).

## Verification

The artifacts `verify_exact.cpp`, `optimal_codebooks.json`, `fractional_certificate.json`, `verify_fractions.py`, and `alternate_milp.py` suffice to reproduce every finite assertion. Compile with `g++ -O3 -std=c++17 verify_exact.cpp -o verify_exact` and invoke `./verify_exact n` separately for each integer \(2\leq n\leq7\). Run `python3 verify_fractions.py` for the independently reconstructed exact rational certificates. If SciPy and NumPy are installed, run `python3 alternate_milp.py` as a second implementation of the integer optimization. No external dataset is required. A compiler and Python standard library suffice for the principal exact proof and rational certificates; the alternative solver is optional.

## Relationship to prior work

Kulkarni and Kiyavash (2012, arXiv:1211.3128v1) introduced hypergraph matching and fractional bounds for deletion-correcting codes, including binary \((d,\infty)\) run-length-limited source families. Their Section V and numerical tables do not evaluate the exact ternary, maximum-run-one, single-deletion capacities here. Nguyen, Cai, Immink and Kiah (2020, arXiv:2001.02839v1) give capacity-approaching constructions for constrained DNA codes correcting edits, with a quaternary setting and additional biochemical constraints; those constructions do not prove these finite ternary optima. Benerjee and Banerjee (2023, arXiv:2305.10741v1) treat homopolymer-free codes under Hamming-distance constraints rather than this unknown-position deletion channel. The exactness is not inferred from the general matching formulation itself.

## Limitations

The integer upper bounds rest on an explicitly supplied finite exhaustive branch-and-bound algorithm, not a short closed-form inequality. Its correctness requires the stated coloring bound and exact graph generation; these have been inspected and cross-checked, but no independent external audit has been performed. The results have no claimed extension to quaternary alphabets, multiple deletions, GC-content constraints or arbitrary \(n\). Full bibliographic priority is subject to unindexed prior computations or equivalent results using different terminology.

## References

1. Ankur A. Kulkarni and Negar Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, initial public arXiv posting 2012-11-13, https://arxiv.org/abs/1211.3128 .
2. Tuan Thanh Nguyen, Kui Cai, Kees A. Schouhamer Immink and Han Mao Kiah, *Capacity-Approaching Constrained Codes with Error Correction for DNA-Based Data Storage*, initial public posting 2020-01-09, https://arxiv.org/abs/2001.02839 .
3. Krishna Gopal Benerjee and Adrish Banerjee, *Bounds on Size of Homopolymer Free Codes*, initial public posting 2023-05-18, https://arxiv.org/abs/2305.10741 .
