# Permutation-symmetric identification in binary hypercubes: a four-state criterion and one-third density

## Finding

For every integer \(n\ge3\), let \(Q_n\) have vertex set \(\{0,1\}^n\), with edges between words at Hamming distance one. A radius-one identifying code \(C\) has the property that \(I_C(x)=C\cap N[x]\) is nonempty for every vertex \(x\), and \(I_C(x)\ne I_C(y)\) whenever \(x\ne y\). Call \(C\) **coordinate-permutation-invariant** if it is fixed setwise by every permutation of the \(n\) coordinate positions.

Put \(L_k=\{x:|x|=k\}\). Every invariant code is a union \(C_W=\bigcup_{k\in W}L_k\), for a unique \(W\subseteq\{0,\dots,n\}\). The following three conditions are **necessary and sufficient** for \(C_W\) to identify all vertices:

1. For each \(0\le k\le n\), \(W\cap(\{k-1,k,k+1\}\cap\{0,\dots,n\})\ne\varnothing\).
2. \(W\cap\{1,2\}\ne\varnothing\).
3. \(W\cap\{n-2,n-1\}\ne\varnothing\).

In particular the exact minimum number \(B_n\) of sensors among coordinate-permutation-invariant identifying codes is the minimum of \(\sum_{k=0}^{n}\binom nk x_k\) over binary variables \(x_k\) satisfying those three conditions. A four-state exact dynamic program below evaluates \(B_n\) with \(O(n)\) big-integer operations, for **every** \(n\ge3\). Its principal asymptotic consequence is

\[
\lim_{n\to\infty}\frac{B_n}{2^n}=\frac13.
\]

This is a positive-density obstruction imposed purely by coordinate indistinguishability; general identifying codes are not required to contain whole Hamming layers. For dimensions three through twenty, exact values and counts of attaining layer profiles are:

| \(n\) | \(B_n\) | Optimal layer profiles | \(n\) | \(B_n\) | Optimal layer profiles |
|---:|---:|---:|---:|---:|---:|
| 3 | 4 | 2 | 12 | 1366 | 2 |
| 4 | 8 | 2 | 13 | 2732 | 1 |
| 5 | 10 | 1 | 14 | 5462 | 1 |
| 6 | 22 | 2 | 15 | 10924 | 2 |
| 7 | 44 | 1 | 16 | 21848 | 1 |
| 8 | 86 | 1 | 17 | 43690 | 1 |
| 9 | 172 | 2 | 18 | 87382 | 2 |
| 10 | 344 | 1 | 19 | 174764 | 1 |
| 11 | 682 | 1 | 20 | 349526 | 1 |

These numerical values are consequences of the exact recurrence, not an extrapolation to uncomputed dimensions. The earlier ten-sensor code made from the weight-one and weight-four layers at dimension five is already given in the 1998 foundational paper; that isolated example is **not claimed as new**.

## Assumptions and scope

All balls are **closed radius-one Hamming balls**; the fault-location requirement concerns single vertices, not simultaneous sets of faulty vertices. Coordinate permutations act on positions only, without flipping symbols. Thus invariance means full Hamming-weight layers, not arbitrary group codes, invariance under translations, or invariance under the entire automorphism group of \(Q_n\). The dimension is any integer \(n\ge3\). No claim is made for a radius other than one or for a nonbinary alphabet.

## Proof

**Orbit reduction.** The coordinate-permutation group is transitive on words of each fixed Hamming weight. Hence its invariant subsets are exactly the unions of whole layers \(L_k\). Such a layer contains \(\binom nk\) vertices.

**Domination and necessity of the extra tests.** A word of weight \(k\) has its closed neighborhood in weight levels \(k-1,k,k+1\), with each existing level represented. Consequently nonempty signatures are equivalent to condition 1. For two different unit vectors \(e_i,e_j\), the symmetric difference \(N[e_i]\triangle N[e_j]\) has weights only one and two, and has vertices of both weights when \(n\ge3\). Identifying the two forces condition 2. Complementing every bit gives condition 3 from the analogous pair at weight \(n-1\).

**Sufficiency, by Hamming distance.** If \(d(x,y)\ge3\), the closed neighborhoods are disjoint, so domination separates their nonempty signatures. If \(d(x,y)=1\), write their weights as \(k\) and \(k+1\). For \(1\le k\le n-2\), the symmetric difference of their neighborhoods contains vertices at each of weights \(k-1,k,k+1,k+2\); condition 1 at weight \(k\) supplies a selected level among the first three. At \(k=0\) its distinguishing levels are one and two, so condition 2 applies; at \(k=n-1\) they are \(n-2,n-1\), so condition 3 applies.

For \(d(x,y)=2\), either they have equal weight \(k\), or their weights are \(k,k+2\). In the first case, their own vertices are separating witnesses at weight \(k\). If \(2\le k\le n-2\), each also has distinct neighboring vertices at both levels \(k-1,k+1\), so condition 1 at weight \(k\) suffices. At \(k=1\) the weight-two neighbors differ (there is an extra upper neighbor because \(n\ge3\)), and the witnesses have weights one and two, so condition 2 suffices. Weight \(n-1\) is complementary. In the unequal-weight case, their own vertices distinguish at weights \(k,k+2\), and there is at least one distinguishing neighbor of intermediate weight \(k+1\): the number of nonshared intermediate neighbors is \((n-k-2)+k=n-2>0\). Thus condition 1 at weight \(k+1\) suffices. This exhausts all pairs and proves necessity and sufficiency.

**Exact finite-state minimization.** Let \(w_k=\binom nk\) and \(x_k=1\) precisely when \(k\in W\). Initialize \(F_1(a,b)=aw_0+bw_1\) for \(a,b\in\{0,1\}\) satisfying \(a\vee b\), and set other entries to infinity. For \(2\le k\le n\), compute

\[
F_k(b,c)=cw_k+\min_{a\in\{0,1\}} F_{k-1}(a,b),
\]

where the minimum ranges only over \(a\vee b\vee c=1\), with the additional restrictions \(b\vee c=1\) if \(k=2\), and \(a\vee b=1\) if \(k=n\). The final answer is \(B_n=\min_{a\vee b=1}F_n(a,b)\). To count minimizing layer profiles, carry the number of attaining histories in parallel, adding counts on cost ties. Each extension verifies the domination triple centered at \(k-1\), while the first and last transitions enforce the two extra distinguishing pairs. Thus every legal profile is represented once and every illegal profile is excluded. There are at most four states per stage, giving the claimed exact \(O(n)\)-operation algorithm.

**Upper density bound.** Write \(R_r(n)=\sum_{0\le k\le n,\ k\equiv r\pmod3}\binom nk\). By the roots-of-unity filter,

\[
R_r(n)=\frac{2^n+2\cos((n-2r)\pi/3)}3.
\]

If \(n\equiv0\pmod3\), select all levels congruent to two modulo three, together with level zero. If \(n\equiv1\pmod3\), select those levels together with levels zero and \(n\). If \(n\equiv2\pmod3\), select just the levels congruent to one modulo three. In every case the three exact identification criteria hold, and at most two singleton endpoint layers were added. Therefore \(B_n\le2^n/3+8/3\).

**Lower density bound.** Let \(H_n=\{k:|k-n/2|\le n^{2/3}\}\). Among any three consecutive indices, at least one must be selected by condition 1 at their central index. Partition the central window into consecutive triples, leaving at most two endpoints. Uniformly inside this window, the ratio between successive binomial coefficients is \(1+O(n^{-1/3})\), so a selected coefficient in each triple weighs at least \((1-O(n^{-1/3}))/3\) times the total weight of the triple. The omitted at-most-two boundary coefficients contribute \(O(2^n/\sqrt n)=o(2^n)\), and the binomial mass outside the window is \(o(2^n)\) by the standard binomial concentration bound. Hence \(B_n\ge(1/3-o(1))2^n\), completing the density limit.

## Verification

Run `python3 verify.py` from a directory containing the accompanying file. It recomputes the exact four-state minima and multiplicities at every dimension from three through twenty, verifies the exhibited residue constructions, and checks the identification criterion directly by constructing **all** neighborhood signatures of **every** possible weight-layer selection for dimensions three through seven. It also exercises the recurrence and explicit feasible constructions through dimension one hundred; that finite exercise is not the proof of the asymptotic statement.

Separately compile `g++ -std=c++17 -O2 independent.cpp -o independent` and run `./independent`. This verifier builds distinguishing constraints directly from representatives of all coordinate-permutation orbits of vertex pairs, not from the proved three-condition characterization. It searches every weight-layer choice at dimensions three through fourteen and checks both optimal counts and sizes. Both independent paths agree on their common dimensions. Their success markers are `VERIFY_OK` and `ALTERNATE_OK`.

## Relationship to prior work

Karpovsky, Chakrabarty and Levitin (1998) introduced identifying codes and analyzed binary hypercubes, including the particular ten-codeword choice of full weight-one and weight-four layers at dimension five (Section II and Table I). This example is prior coverage, not evidence of an all-dimensional, exact layer-profile characterization. Janson and Laihonen (2008 preprint; 2009 journal) study general identifying codes and parameter-dependent asymptotics without imposing fixedness under all coordinate permutations. Cohen and colleagues (1999) study general identifying-code bounds, focused on square lattices. The new assertion is the iff characterization for **all** dimensions, its exact four-state reduction, and its sharp one-third symmetry-constrained density, rather than a new general identifying-code bound or the previously known five-cube example.

## Limitations

The displayed finite minima were established with exact arithmetic, while the infinite-dimensional density conclusion rests on the preceding analytic proof. A compact elementary closed formula for every \(B_n\), or a general classification of equality profiles beyond the computed dimensions, is **not** asserted. The comparison against relevant indexed research records and accessible primary-source sections did not identify the same all-dimensional symmetric theorem, but literature databases are incomplete and a later construction paper with only partial text access remains a historical-priority risk. The manuscript does not claim independent mathematical validation.

## References

1. M. G. Karpovsky, K. Chakrabarty and L. B. Levitin, *On a New Class of Codes for Identifying Vertices in Graphs*, IEEE Transactions on Information Theory **44** (1998), 599–611, DOI 10.1109/18.661507. Author-hosted full text: https://sites.bu.edu/mark/files/2018/02/132.pdf
2. S. Janson and T. Laihonen, *On the Size of Identifying Codes in Binary Hypercubes*, preprint dated April 18, 2008; Journal of Combinatorial Theory A **116** (2009), 1087–1096. Author-hosted text: https://www2.math.uu.se/~svantejs/papers/sj216.pdf
3. G. Cohen, I. Honkala, A. Lobstein and G. Zémor, *New Bounds for Codes Identifying Vertices in Graphs*, Electronic Journal of Combinatorics **6** (1999), R19; published March 15, 1999. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v6i1r19
4. I. Honkala, T. Laihonen and S. Ranto, *New Identifying Codes in the Binary Hamming Space*, European Journal of Combinatorics **31** (2010), 491–501, DOI 10.1016/j.ejc.2009.03.032. Only abstract/introductory text was accessible in the present comparison.
