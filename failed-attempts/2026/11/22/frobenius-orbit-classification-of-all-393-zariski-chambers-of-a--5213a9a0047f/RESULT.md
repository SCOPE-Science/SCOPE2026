# Frobenius orbit classification of all 393 Zariski chambers of a quartic del Pezzo surface

## Finding
Let \(S/\mathbb F_q\) be any smooth degree-four del Pezzo surface, over a finite field of arbitrary characteristic. Its geometric exceptional curves form a set \(V\) of sixteen curves; write \(g\in W(D_5)\) for geometric Frobenius on that configuration. The \(393\) geometric Zariski chambers of the big cone form a canonical finite Frobenius set \(\mathscr Z(S)\). This result gives its **complete orbit-length classification for each of the eighteen signed cycle types** in \(W(D_5)\), including the number of chambers realized by ground-field divisors and the chamber count over every extension field.

A signed cycle has a length and either positive or negative sign; the number of negative cycles is even. In the table, \(d^{m}\) in the last column denotes \(m\) distinct orbits of length \(d\), not a numerical exponentiation. The class size counts elements of the order-\(1920\) Weyl group.

| Signed cycle type | Weyl class size | Rational chambers | Complete chamber orbit profile |
|:--|--:|--:|:--|
| \(5^{+}\) | 384 | 3 | \(1^{3}\, 5^{78}\) |
| \(4^{-}, 1^{-}\) | 240 | 1 | \(1^{1}\, 8^{49}\) |
| \(4^{+}, 1^{+}\) | 240 | 7 | \(1^{7}\, 2^{13}\, 4^{90}\) |
| \(3^{-}, 2^{-}\) | 160 | 1 | \(1^{1}\, 2^{1}\, 4^{6}\, 6^{3}\, 12^{29}\) |
| \(3^{-}, 1^{-}, 1^{+}\) | 160 | 1 | \(1^{1}\, 2^{13}\, 6^{61}\) |
| \(3^{+}, 2^{+}\) | 160 | 11 | \(1^{11}\, 2^{8}\, 3^{32}\, 6^{45}\) |
| \(3^{+}, 1^{-}, 1^{-}\) | 80 | 3 | \(1^{3}\, 2^{12}\, 3^{6}\, 6^{58}\) |
| \(3^{+}, 1^{+}, 1^{+}\) | 80 | 27 | \(1^{27}\, 3^{122}\) |
| \(2^{-}, 2^{-}, 1^{+}\) | 60 | 1 | \(1^{1}\, 4^{98}\) |
| \(2^{-}, 2^{+}, 1^{-}\) | 120 | 3 | \(1^{3}\, 2^{9}\, 4^{93}\) |
| \(2^{-}, 1^{-}, 1^{-}, 1^{-}\) | 20 | 1 | \(1^{1}\, 2^{10}\, 4^{93}\) |
| \(2^{-}, 1^{-}, 1^{+}, 1^{+}\) | 60 | 5 | \(1^{5}\, 2^{8}\, 4^{93}\) |
| \(2^{+}, 2^{+}, 1^{+}\) | 60 | 33 | \(1^{33}\, 2^{180}\) |
| \(2^{+}, 1^{-}, 1^{-}, 1^{+}\) | 60 | 7 | \(1^{7}\, 2^{193}\) |
| \(2^{+}, 1^{+}, 1^{+}, 1^{+}\) | 20 | 107 | \(1^{107}\, 2^{143}\) |
| \(1^{-}, 1^{-}, 1^{-}, 1^{-}, 1^{+}\) | 5 | 1 | \(1^{1}\, 2^{196}\) |
| \(1^{-}, 1^{-}, 1^{+}, 1^{+}, 1^{+}\) | 10 | 21 | \(1^{21}\, 2^{186}\) |
| \(1^{+}, 1^{+}, 1^{+}, 1^{+}, 1^{+}\) | 1 | 393 | \(1^{393}\) |

The corresponding refined fixed-chamber polynomial records the number of rational chamber supports of each cardinality: \(F_g(t)=\sum_{j=0}^{5}f_j(g)t^j\), with \(f_j(g)\) counting \(g\)-invariant subsets of \(j\) pairwise disjoint geometric exceptional curves.

| Signed cycle type | Fixed-chamber polynomial \(F_g(t)\) |
|:--|:--|
| \(5^{+}\) | \(1+t+t^{5}\) |
| \(4^{-}, 1^{-}\) | \(1\) |
| \(4^{+}, 1^{+}\) | \(1+2t+2t^{4}+2t^{5}\) |
| \(3^{-}, 2^{-}\) | \(1\) |
| \(3^{-}, 1^{-}, 1^{+}\) | \(1\) |
| \(3^{+}, 2^{+}\) | \(1+2t+2t^{2}+2t^{3}+2t^{4}+2t^{5}\) |
| \(3^{+}, 1^{-}, 1^{-}\) | \(1+2t^{2}\) |
| \(3^{+}, 1^{+}, 1^{+}\) | \(1+4t+2t^{2}+4t^{3}+12t^{4}+4t^{5}\) |
| \(2^{-}, 2^{-}, 1^{+}\) | \(1\) |
| \(2^{-}, 2^{+}, 1^{-}\) | \(1+2t^{4}\) |
| \(2^{-}, 1^{-}, 1^{-}, 1^{-}\) | \(1\) |
| \(2^{-}, 1^{-}, 1^{+}, 1^{+}\) | \(1+4t^{4}\) |
| \(2^{+}, 2^{+}, 1^{+}\) | \(1+4t+8t^{2}+8t^{3}+8t^{4}+4t^{5}\) |
| \(2^{+}, 1^{-}, 1^{-}, 1^{+}\) | \(1+4t^{2}+2t^{4}\) |
| \(2^{+}, 1^{+}, 1^{+}, 1^{+}\) | \(1+8t+20t^{2}+32t^{3}+38t^{4}+8t^{5}\) |
| \(1^{-}, 1^{-}, 1^{-}, 1^{-}, 1^{+}\) | \(1\) |
| \(1^{-}, 1^{-}, 1^{+}, 1^{+}, 1^{+}\) | \(1+8t^{2}+12t^{4}\) |
| \(1^{+}, 1^{+}, 1^{+}, 1^{+}, 1^{+}\) | \(1+16t+80t^{2}+160t^{3}+120t^{4}+16t^{5}\) |

In particular, for a surface with signed type \((3^{+},1^{-},1^{-})\), no exceptional curve is individually rational, but the nef chamber and two distinct non-nef chambers are rational; their negative supports are pairs of conjugate disjoint curves. This is a conditional statement for every surface of that arithmetic type, not a claim that the type is realizable over every particular small finite field. In contrast, for signed type \((4^{-},1^{-})\) only the nef chamber is rational.

The distribution of all geometric supports by cardinality is exactly
\[
1+16t+80t^2+160t^3+120t^4+16t^5.
\]
For any \(g\) in a table row with orbit profile \(\{d^{m_d}\}\), the finite étale chamber scheme has formal zeta function
\[
Z(\mathscr Z(S),T)=\prod_{d\ge1}(1-T^d)^{-m_d},\qquad
\#\mathscr Z(S)(\mathbb F_{q^n})=\sum_{d\mid n}d\,m_d.
\]
This is the zeta function of the finite chamber set, **not** the Hasse--Weil zeta function of the surface.

## Assumptions and scope
Here \(S\) is smooth, projective and geometrically integral, its anticanonical class \(-K_S\) is ample, and \(K_S^2=4\). The Zariski chambers are chambers in the geometric big cone indexed by the support of the negative part in the unique Zariski decomposition. A *rational chamber* means a geometric chamber whose relative interior contains a class of a big divisor defined over \(\mathbb F_q\). Equivalently, its set of exceptional-curve components is invariant under Frobenius; a rational chamber need not be supported on individually rational curves. A Weyl type is conditional on its realization by a surface; this classification does not assert that all eighteen types occur over every finite field.

Over an algebraic closure the surface is the blow-up of five points in general position in \(\mathbf P^2\). The negative curves are the five exceptional divisors \(E_i\), the ten strict transforms \(L_{ij}=H-E_i-E_j\), and the conic transform \(Q=2H-\sum_iE_i\). Intersections of distinct exceptional curves are either zero or one. Their forty intersection pairs are \(E_i\cdot Q=1\), \(E_i\cdot L_{ij}=1\), and \(L_{ij}\cdot L_{kl}=1\) for disjoint index pairs; all other pairwise intersections vanish. No negative curves are omitted.

## Proof
**1. Negative supports are exactly independent sets.** Bauer--Funke--Neumann's chamber-support criterion identifies non-nef chambers with negative-definite subsets of negative curves. If two distinct exceptional curves intersect, their intersection submatrix is \(\left(\begin{smallmatrix}-1&1\\1&-1\end{smallmatrix}\right)\), with a zero eigenvalue. Thus a negative-definite support contains only disjoint curves. Conversely, every pairwise disjoint subset has diagonal intersection matrix \(-I\) and is negative definite. The empty support is the nef chamber. Therefore the chambers are exactly independent sets of the sixteen-vertex, forty-edge exceptional-curve intersection graph.

**2. Every invariant support really descends as a rational chamber.** Let \(B\) be a Frobenius-invariant set of \(r\) pairwise disjoint exceptional curves, write again \(B\) for their sum as a divisor, and consider the ground-field divisor \(D_B=-K_S+2B\). Its Zariski decomposition is
\[
D_B=P_B+N_B,\qquad P_B=-K_S+B,\quad N_B=B.
\]
For each component \(E\) of \(B\), one has \(P_B\cdot E=1-1=0\); for any other exceptional curve \(F\), \(P_B\cdot F=1+B\cdot F\ge1\). The Mori cone of a smooth del Pezzo surface is generated by the exceptional curves, hence \(P_B\) is nef, and \(P_B^2=4+r>0\) proves bigness. The negative part has disjoint negative-definite components, so this is the unique Zariski decomposition, and \(D_B\) lies in the interior of exactly the chamber with support \(B\). Galois invariance of the effective divisor sum \(B\) gives descent to \(\mathbb F_q\). Conversely uniqueness of the negative part forces the support of every ground-field big divisor to be Frobenius-stable. This proves the arithmetic-chamber bijection.

**3. Spin-bit configuration and the full Weyl group.** Index the sixteen exceptional curves by the even-weight bit strings \(v\in\mathbb F_2^5\): the zero word is \(Q\); the weight-two word supported on \(\{i,j\}\) is \(L_{ij}\); the weight-four word missing \(i\) is \(E_i\). Two vertices intersect precisely when their Hamming distance is four. The full Picard-lattice Weyl action is
\[
v\longmapsto \pi(v)+\varepsilon,
\qquad \pi\in S_5,\quad \varepsilon\in\mathbb F_2^5,
\quad \sum_i\varepsilon_i=0\pmod2.
\]
There are exactly \(5!\,2^4=1920\) group elements. Each conjugacy class is determined by the partition into cycles of \(\pi\), marked negative whenever the sum of \(\varepsilon_i\) on the cycle is odd. Since the total parity is even, there are eighteen signed types.

**4. Exact finite enumeration, with no extrapolation.** A subset of the sixteen vertices is represented by a sixteen-bit integer. Enumerate all \(2^{16}\) masks and retain those with no intersecting pair. This produces exactly \(393\) masks with size generating polynomial displayed above. For every one of the \(1920\) signed permutations, its action on the sixteen vertices induces a permutation of these \(393\) masks. Enumerate its disjoint cycles and count lengths. Independently, the accompanying lattice-reflection program constructs the sixteen divisor classes directly from their intersection form, generates \(W(D_5)\) by the four adjacent exceptional-divisor swaps and the Cremona reflection in \(H-E_1-E_2-E_3\), and computes the same signed types via the ten complementary conic pencils. This gives all eighteen rows, with identical results for every element in each signed type. The two approaches do not share an incidence matrix or group generator implementation. The invariant-support generating functions follow by counting the fixed masks according to their sizes.

**5. Extension degrees.** A Frobenius orbit of geometric chambers of length \(d\) contributes \(d\) fixed chambers to the \(n\)-th iterate precisely when \(d\mid n\). The displayed zeta product and extension counts follow immediately. This is a consequence of the computed complete cycle types, not an assumption about point counts.

## Verification
Run `python3 verify_signed.py` and `python3 verify_geometry.py`, each using only the Python standard library. Both have been executed successfully on their saved source files. The first exhaustively enumerates the even-bit affine model and checks equality within every signed class. The second reconstructs the Picard intersection lattice, all sixteen divisor classes, ten conic-pencil classes and five Weyl reflection generators; it enumerates a group of order \(1920\), checks its eighteen signed types and verifies the independently recorded exact orbit table. The finite enumeration is exhaustive in the finite Weyl group; it is the geometric identification of Frobenius and chambers in Steps 1--3 that makes this valid for *every* smooth quartic del Pezzo surface over a finite field. No surface-by-surface finite-field enumeration is claimed.

## Relationship to prior work
Bauer--Funke--Neumann (arXiv:0912.0958, first public version 2009-12-04), Proposition 1.1, Theorem 3.1 and their counting algorithm, give the geometric chamber-support criterion and the unrefined counts. They do not tabulate Frobenius actions on chambers. Bright--Bruin--Flynn--Logan (2007) describe the same sixteen-line incidence configuration and Weyl action for Brauer--Manin calculations, but their target invariant is distinct from Frobenius-stable Zariski chambers. Blache--Hallouin (arXiv:2301.13582, 2023) enumerate the eighteen signed Weyl types in the context of arithmetic del Pezzo surfaces and their conic pencils, without a corresponding chamber-orbit table.

Two relevant publicly available computations on quartic del Pezzo surfaces determine Frobenius-dependent zeta functions of the complement of the sixteen exceptional curves. Their complete even-sign bit model and eighteen-type classification of **curve, node, and branch incidence** are explicitly taken as prior information, not new. The present table instead concerns all \(393\) negative-definite exceptional-curve supports and their full Frobenius orbit distribution; this is not a claim about rational points of the curve complement. Similarity of the Weyl-action input does not make the two finite sets or their permutation characters identical. Exact priority over other unindexed computations of chamber permutation characters remains a residual risk.

## Limitations
No all-field realization theorem for the eighteen Weyl types is claimed; the table states what happens whenever a given type occurs. Nor is a chamber invariant being identified with a Picard, Brauer, or graph critical group. The geometric chamber number and general support algorithm are prior knowledge. The new contribution is the explicit eighteen-type arithmetic refinement, not a newly discovered Weyl action. Historical priority over other independent-set permutation-character calculations remains provisional.

## References
1. T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958v1, 2009-12-04. https://arxiv.org/abs/0912.0958
2. M. Bright, N. Bruin, E. V. Flynn, A. Logan, *The Brauer--Manin obstruction and Sha[2]*, LMS J. Comput. Math. 10 (2007), 354--377. https://doi.org/10.1112/S1461157000001455
3. R. Blache, E. Hallouin, *Classification of singular del Pezzo surfaces over finite fields*, arXiv:2301.13582 (2023), especially Section 4.3 on signed cycle types. https://arxiv.org/abs/2301.13582
