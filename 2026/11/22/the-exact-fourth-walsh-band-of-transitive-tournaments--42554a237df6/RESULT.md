# The exact fourth Walsh band of transitive tournaments

## Finding
Let \(n\ge3\), let \(E_n=\binom{[n]}2\), and let \(A_n\subseteq\mathbb F_2^{E_n}\) be the set of inversion-vector representations of all total orders of \([n]\). Relative to the natural order, the bit at \(\{u,v\}\), \(u<v\), is one exactly when \(v\) occurs before \(u\). Define the unnormalized Walsh multiplier
\[
W_n(S)=\sum_{x\in A_n}(-1)^{\sum_{e\in S}x_e},\qquad S\subseteq E_n.
\]
For frequencies with \(|S|\le4\), the following list gives **all** nonzero possibilities, classified by the simple graph \(([n],S)\) after discarding isolated vertices. The displayed multiplier magnitudes are exact.

| Edges | Frequency graph after deleting isolates | \(|W_n(S)|/n!\) |
| --- | --- | --- |
| 0 | Empty graph | \(1\) |
| 2 | Two-edge path \(P_3\) | \(1/3\) |
| 4 | Four-cycle \(C_4\) | \(1/3\) |
| 4 | Five-vertex star \(K_{1,4}\) | \(1/5\) |
| 4 | Five-vertex tree of degrees \((3,2,1,1,1)\) | \(1/15\) |
| 4 | Five-vertex path \(P_5\) | \(2/15\) |
| 4 | Disjoint union \(P_3\sqcup P_3\) | \(1/9\) |

Every other \(S\) of size at most four has \(W_n(S)=0\), including all odd-size frequencies, every disjoint pair of edges, and the four-edge triangle with a pendant edge. Consequently, for unnormalized XOR counting convolution by \(\mathbf1_{A_n}\), the exact rank of its restriction to the span of Walsh characters of degree at most four is
\[
\boxed{R_{\le4}(n)=1+3\binom n3+3\binom n4+125\binom n5+90\binom n6.}
\]
Here \(\binom nk=0\) when \(k>n\). This is a statement about the restricted operator, not its full Fourier rank.

## Assumptions and scope
All graphs are simple and labelled; the listed graph is the *frequency support graph*, not a graph required to appear inside a ranking. The group is \(\mathbb F_2^{\binom n2}\), with convolution \((Tf)(x)=\sum_y\mathbf1_{A_n}(y)f(x\oplus y)\). Each permutation of \([n]\) determines a distinct transitive tournament, so \(|A_n|=n!\). A graph isomorphism may reverse some reference directions, changing the sign of a multiplier but never its magnitude or zero status.

## Proof
**Permutation reduction.** If \(S\) has \(k\) nonisolated vertices, its multiplier equals \(n!/k!\) times the same signed permutation sum on the induced frequency graph with these \(k\) vertices. This follows because the relative order of the marked vertices is uniform, with exactly \(n!/k!\) completions per relative order. For disjoint nontrivial support components, their relative internal orders are independent, so the normalized multiplier is the product of the normalized component multipliers. Reversing an entire relative order flips the parity of all its support edges; hence every component with an odd number of edges forces a zero. In particular every odd total support size vanishes.

**Exact connected small motifs.** For an arbitrary support graph on \(k\) vertices, put \(D(\varnothing)=1\) and recursively define, for \(U\subseteq[k]\),
\[
D(U)=\sum_{v\in U}(-1)^{\#\{u\in U\setminus\{v\}:u>v,\ \{u,v\}\in S\}}D(U\setminus\{v\}).
\]
Appending \(v\) last in a total order creates precisely the displayed inversions, so induction proves \(D([k])=W_k(S)\). There are exactly two connected four-edge simple graphs on four vertices: \(C_4\) and a triangle with a pendant edge. Their respective absolute sums are \(8\) and \(0\). Every connected four-edge graph on five vertices is a tree, and there are exactly three unlabelled shapes: \(K_{1,4}\), degree sequence \((3,2,1,1,1)\), and \(P_5\). Their respective absolute sums are \(24\), \(8\), and \(16\). For two edges on three vertices the absolute sum is \(2\). All of these integers follow from the finite exact recurrence above; the complete direct-permutation and subset-recursion checks are in `verify.py`.

**Disconnected shapes and exhaustiveness.** Any disconnected four-edge graph with a component containing an odd number of edges has zero multiplier. The only remaining disconnected possibility is two disjoint copies of \(P_3\), whose normalized coefficient magnitude is \((1/3)^2=1/9\). A connected four-edge graph uses at most five vertices, and a disconnected four-edge graph uses at most eight; the edge partition cases already listed therefore exhaust every graph, regardless of the ambient \(n\).

**Counting surviving modes.** There are \(3\binom n3\) two-edge paths and \(3\binom n4\) four-cycles. By Cayley's tree count on five labelled vertices, there are \(5^{3}=125\) four-edge trees on every five-vertex subset. On each six-vertex subset there are \(\binom63/2\cdot3^2=90\) disjoint pairs of two-edge paths. These supports are disjoint by edge count or component structure. Adding the empty support proves the rank expression, since Walsh characters diagonalize XOR convolution and each nonzero multiplier contributes exactly one rank dimension.

## Verification
Run `python3 verify.py` with Python 3.8 or later. The program directly enumerates all permutations and frequency supports with at most four edges for ambient orders four, five and six, compares every resulting signed multiplier with the claimed isomorphism-type magnitude, and checks the rank polynomial. A separate subset dynamic program checks the independent small-motif evaluations, including their zeros. The outputs are respectively \((1,0,12,0,3)\), \((1,0,30,0,140)\), and \((1,0,60,0,885)\), indexed by Fourier degrees zero through four. The proof of the universal statement is the preceding finite-shape classification; computations alone are not an extrapolation to larger \(n\).

## Relationship to prior work
Boolean-character diagonalization and normalized Fourier conventions are classical (de Wolf, 2008). Transitive tournaments are classical representations of total rankings (Yuster, 2002). Chebikin and Postnikov (2008) study a different inversion polynomial on trees and generalized parking functions; their evaluation at \(-1\) does not imply the present sparse-frequency graph classification. Other archived work establishes a universal two-adic divisor of the entire transitive-tournament Fourier spectrum and the odd-weight zero phenomenon, but does not give these degree-two/four motif values or the rank polynomial. The distinction is between divisibility or reversal symmetry and an exact graph-by-graph low-degree spectrum.

## Limitations
No full Fourier spectrum is claimed for frequencies of five or more edges; zero/nonzero at such frequencies can involve additional motifs. The low-degree rank is a restriction rank, and no noise-stability or conditioning bound for the surviving modes is asserted. The literature comparison is bounded and an undiscovered equivalent formula remains a priority risk. The finite recurrence table can be verified without external computer algebra.

## References
- R. Yuster, *Tiling transitive tournaments and their blow-ups*, arXiv:math/0210338v1, first public 2002-10-22, https://arxiv.org/pdf/math/0210338v1.
- R. de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Library, 2008, first published 2008-09-25, https://cims.nyu.edu/~regev/toc/articles/gs001/gs001.pdf.
- D. Chebikin and A. Postnikov, *Generalized Parking Functions, Descent Numbers, and Chain Polytopes of Ribbon Posets*, arXiv:0806.0440v1, first public 2008-06-03, https://math.mit.edu/~apost/papers/GeneralizedParking.pdf.
