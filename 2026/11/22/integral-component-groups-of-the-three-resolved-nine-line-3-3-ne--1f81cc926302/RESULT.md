# Integral component groups of the three resolved nine-line \((3,3)\)-net boundaries

## Finding

Let \(\mathcal A\) be any complex projective nine-line arrangement that is a \((3,3)\)-net. Blow up **every triple intersection** of \(\mathcal A\) and let \(D\) be the reduced curve consisting of the nine strict line transforms and all exceptional curves. The remaining ordinary double intersections are not blown up. The curve \(D\) is connected, reduced, nodal and stable. Write \(K(\Gamma_D)\) for the critical group of its dual graph, equivalently the cokernel of any reduced integer graph Laplacian.

There are precisely three possibilities, classified by the total numbers of triple and double points of \(\mathcal A\):

| Nine-line net | Triple / double points | Components / nodes / genus | Exact integral critical group |
| --- | --- | --- | --- |
| Hesse-pencil nine-line net | \(9/9\) | \(18/36/19\) | \(C_5\oplus C_{15}^{2}\oplus C_{45}^{2}\oplus C_{135}\) |
| Pappus ten-triple net | \(10/6\) | \(19/36/18\) | \(C_3\oplus C_{45}^{2}\oplus C_{135}\oplus C_{405}\) |
| Ceva nine-line net | \(12/0\) | \(21/36/16\) | \(C_3\oplus C_9^{4}\oplus C_{27}^{3}\) |

Here \(C_m=\mathbb Z/m\mathbb Z\), and a superscript denotes the direct-sum multiplicity. In particular, the five-primary part is nonzero in the first two cases but **vanishes altogether** in the Ceva case; the exponent is, respectively, \(135\), \(405\), and \(27\). These groups are determined by the intersection-lattice type, not by a selected realization of that type.

For every proper regular split semistable one-parameter smoothing having the indicated special curve with unit node thicknesses, the geometric component group of the generic Jacobian's Néron model is the group in the corresponding row.

## Assumptions and scope

All three nets are considered over \(\mathbb C\), with nine distinct lines and only ordinary double and triple intersection points. A \((3,3)\)-net is a partition into three classes of three lines, in which the nine pairwise intersections between two distinct classes are triple points shared with exactly one line of the third class. A line in a fixed class meets the two other lines in that class either in two distinct ordinary double points or at one concurrent triple point.

The classification of complex \((3,3)\)-nets, including the exclusion of exactly two concurrent classes, is Theorem 2.2 of Dimca–Ibadula–Măcinic [1]. Their classification distinguishes the nine-triple Hesse-pencil *subarrangement* from the full Hesse arrangement of twelve lines; they are not the same divisor. Their ten-triple Pappus arrangement is likewise distinct from the classical nine-triple \((9_3)\) Pappus realization. The results below apply to these three arrangements and their stated resolution construction, not to arbitrary graph modifications or distinct models of a line arrangement.

## Proof

**Step 1: uniform incidence construction.** Index the nine lines as \(A_i,B_j,C_k\) with \(i,j,k\in\{0,1,2\}\), indices modulo three. After relabelling the net, the nine mixed triple points are indexed \(T_{ij}\), and \(T_{ij}\) lies on exactly \(A_i,B_j,C_{i+j}\). Let \(t\) be the number of line classes whose own three members are concurrent. Theorem 2.2 of [1] says that exactly \(t\in\{0,1,3\}\) occurs; the three cases are Hesse-pencil, Pappus, and Ceva respectively.

At every mixed triple point, its exceptional curve meets those three strict line transforms transversely, giving \(27\) distinct nodes. A concurrent class contributes one exceptional component and three additional nodes. A nonconcurrent class contributes three ordinary double nodes and no exceptional component. Thus

\[
\#V=9+9+t=18+t,\qquad
\#E=27+3t+3(3-t)=36,\qquad
p_a(D)=\#E-\#V+1=19-t.
\]

The nine line components each have at least four distinct nodes; each exceptional component has three. Therefore every genus-zero component is stable. Distinct line tangent directions ensure the exceptional intersections are ordinary nodes, so this is exactly the graph specified below.

**Step 2: integer Laplacian.** Give the vertices the order \(A_0,A_1,A_2,B_0,B_1,B_2,C_0,C_1,C_2,T_{00},\ldots,T_{22}\), followed by exceptional vertices for concurrent classes. Add the three edges \(T_{ij}A_i\), \(T_{ij}B_j\), \(T_{ij}C_{i+j}\). For each nonconcurrent class add its three within-class line–line edges; for each concurrent class instead add a three-edge star from a fresh exceptional vertex to the lines in that class. The first \(t\) classes may be taken concurrent without changing the graph up to isomorphism. This yields an explicit symmetric integral Laplacian \(L_t\), with diagonal entries equal to vertex degrees and off-diagonal entries equal to minus edge multiplicities. The executable `verify_net3.py` constructs these matrices directly from this rule.

Their exact characteristic polynomials, with \(z\) an indeterminate, are

\[
\begin{aligned}
\det(zI-L_0)&=z(z-6)(z-3)^4(z^2-9z+15)^6,\\
\det(zI-L_1)&=z(z-3)^3(z^2-9z+15)^4(z^2-7z+9)^2
 (z^3-13z^2+51z-57),\\
\det(zI-L_3)&=z(z-7)(z-3)^3(z^2-7z+9)^8.
\end{aligned}
\]

The matrix–tree theorem (or the nonzero eigenvalue products divided by the vertex counts) gives the exact orders

\[
\tau_0=3^9 5^6=307546875,\qquad
\tau_1=3^{12}5^4=332150625,\qquad
\tau_3=3^{18}=387420489.
\]

**Step 3: integral rather than spectral determination.** Delete any one vertex from \(L_t\) and denote the resulting full-rank matrix by \(R_t\). Independent exact prime-local row and column reductions modulo \(p^9\), using only unit operations over the ring \(\mathbb Z/p^9\mathbb Z\), give the following complete multisets of Smith exponents. The notation \(e^r\) means that exponent \(e\) occurs \(r\) times, **including zero exponents**.

| Case | Smith exponents at \(p=3\) | Smith exponents at \(p=5\) |
| --- | --- | --- |
| \(t=0\) | \(0^{12},1^2,2^2,3\) | \(0^{11},1^6\) |
| \(t=1\) | \(0^{13},1,2^2,3,4\) | \(0^{14},1^4\) |
| \(t=3\) | \(0^{12},1,2^4,3^3\) | \(0^{20}\) |

All computed exponents are below nine, so the finite precision does not lose a pivot. Combining the increasing prime-local exponents gives exactly the invariant factors in the finding table. The determinant factorizations exclude every other torsion prime. The Smith forms are independently reproduced by exact integer-domain elimination, with two different deleted vertices for each case. This proves the complete integral statement rather than only the group order.

**Step 4: geometric interpretation.** For a regular split semistable model with reduced nodal special fiber \(D\) and all local equations of thickness one, its integral intersection graph is precisely \(\Gamma_D\). Raynaud's component-group theorem, as stated in [2, Theorem 8.2], identifies the Néron component group with the regularized graph Jacobian, equal here to \(K(\Gamma_D)\). This implication is conditional on the specified smoothing assumptions.

## Verification

The standalone Python 3/SymPy script `verify_net3.py` reconstructs all three integer Laplacians from the nine mixed triples and the possible concurrent classes. It checks all vertex/node/genus counts, stability valences, characteristic polynomials, spanning-tree determinants and complete Smith lists for two distinct roots. As a separate computation, it performs prime-local elimination modulo \(3^9\) and \(5^9\) and matches the resulting exponents against the exact integer Smith form. It also independently enumerates all \(36\) line pairs in rational coordinate examples of the nine-triple and ten-triple nets from [1]: specializations \((b,c)=(2,3)\) and \((b,c)=(2,2)\) respectively. The Ceva line factors are those of \((x^3-y^3)(y^3-z^3)(z^3-x^3)\), as in [1]; a separate exact enumeration over \(\mathbb Q(\omega)\), with \(\omega^2+\omega+1=0\), verifies precisely twelve triple points and no double points.

Reproduction: `python verify_net3.py` in an environment with SymPy installed; a successful run prints `THREE_NINE_LINE_NET_INTEGRAL_BOUNDARIES_OK`. All required data and algorithms are contained in this package. No numerical approximation or probabilistic search is needed.

## Relationship to prior work

The three-way *incidence-lattice* classification, line equations, nine mixed base points and distinction of the two Pappus usages are from [1]; none of those facts is claimed new. The component-group interpretation is from the general theorem of Raynaud [2], not a new principle. The new calculation is the complete integral critical-group classification for the **three resolved nine-line net boundaries**, including the five-primary disappearance. Published calculations of the three \((9_3)\) Levi graphs concern bipartite graphs with 18 vertices and 27 edges, unlike the present graphs with 36 edges and 18, 19 or 21 vertices; those calculations do not give the current decompositions. A published computation for the full twelve-line Hesse arrangement likewise has a different divisor and incidence graph. A general graph-Smith algorithm is not an already evaluated table for these three geometrically selected integer matrices.

## Limitations

The three nodal boundaries have different arithmetic genera and are **not asserted** to be fibers of a single flat genus-preserving family. The line configurations can degenerate by within-class concurrence, but passing to their selected resolved reduced divisors changes the number of components and genus. The classification is over characteristic zero; no assertion is made about small-characteristic specializations, extra incidences, or nonunit node thicknesses. The exact integral decomposition has been checked computationally and reconstructed mathematically, but has not received independent external mathematical validation. Historical priority may be affected by unindexed older sandpile computations under different names.

## References

[1] A. Dimca, D. Ibadula and D. A. Măcinic, *Pencil type line arrangements of low degree: classification and monodromy*, arXiv:1305.5092, first public 22 May 2013, Theorem 2.2 and Example 2.3. https://arxiv.org/abs/1305.5092

[2] O. Amini, M. Baker, E. Brugallé and J. Rabinoff, *Lifting harmonic morphisms I: metrized complexes and Berkovich skeleta*, Section 8, Theorem 8.2 (Raynaud's theorem). https://www.math.ens.psl.eu/~amini/Publications/hmmcI.pdf

[3] B. Grünbaum, *Configurations of Points and Lines*, American Mathematical Society, 2009. Classical arrangement context and terminology; the group decompositions displayed here are not attributed to this book.
