# Integral critical group of the cubic-surface line–double-six incidence graph

## Finding
Let \(S\) be any smooth cubic surface over an algebraically closed field of characteristic zero. Define the bipartite graph \(\Gamma(S)\) whose two parts are its \(27\) geometric lines and its \(36\) unordered Schläfli double-sixes, with a line adjacent to a double-six exactly when it is one of that double-six's \(12\) lines. The graph has \(63\) vertices and \(432\) edges, and its integral critical group is
\[
\boxed{K(\Gamma(S))\cong
(\mathbb Z/2\mathbb Z)^{28}\oplus
(\mathbb Z/4\mathbb Z)^2\oplus
\mathbb Z/60\mathbb Z\oplus
(\mathbb Z/180\mathbb Z)^5\oplus
(\mathbb Z/540\mathbb Z)^2\oplus
(\mathbb Z/1080\mathbb Z)^6\oplus
(\mathbb Z/4320\mathbb Z)^6.}
\]
Equivalently, its reduced Laplacian has Smith invariant factors
\[
1^{12},\quad 2^{28},\quad 4^2,\quad60,\quad180^5,\quad540^2,\quad1080^6,\quad4320^6,
\]
with the powers in this display denoting multiplicities. The number of spanning trees is \(2^{96}3^{53}5^{20}\), the exponent of the critical group is \(4320\), and the minimal number of generators is \(50\).

## Assumptions and scope
For a fixed blow-up presentation \(S\simeq\operatorname{Bl}_{p_1,\ldots,p_6}\mathbb P^2\) at six points in general position, write \(H\) for the pullback of a line and \(E_i\) for the exceptional divisors. The \(27\) line classes, in the order used for the certificate, are \(E_1,\ldots,E_6\), then \(L_{ij}=H-E_i-E_j\) for \(1\le i<j\le6\) in lexicographic order, then \(Q_i=2H-\sum_{j\ne i}E_j\) for \(1\le i\le6\). The intersection form on coefficient vectors \((d,m_1,\ldots,m_6)\) is \(dd'-\sum_i m_i m'_i\). The surface-dependent geometric realization has the same line-incidence structure on every smooth cubic surface; the graph and its invariant therefore depend only on the classical configuration, not on coefficients of a chosen cubic equation.

A Schläfli double-six is an *unordered* pair of sixers \(\{a_1,\ldots,a_6\}\), \(\{b_1,\ldots,b_6\}\): each row consists of six pairwise skew lines, and \(a_i\) meets \(b_j\) precisely when \(i\ne j\). A finite connected graph's critical group is the torsion subgroup of the cokernel of its integer Laplacian, equivalently the cokernel of any one-vertex deleted Laplacian.

## Proof
**1. Complete geometric incidence.** Enumerate all six-element subsets of the \(27\) classes having pairwise intersection zero. Exactly \(72\) occur. For each such sixer \(A\), the set of lines that meet exactly five of its six lines is another sixer \(B\) of size six, with an opposite perfect nonintersection matching. Its union with \(A\) is a double-six, and every double-six occurs this way twice, so there are exactly \(36\) distinct \(12\)-line supports. An independent construction uses the \(36\) root directions in \(E_6\), represented by the \(15\) classes \(E_i-E_j\), the \(20\) classes \(H-E_i-E_j-E_k\), and \(2H-\sum_iE_i\). The lines pairing nontrivially with a root are exactly its twelve double-six lines. Exact enumeration verifies that the two support families coincide, and proves their completeness via the classical classification. Let \(B\) denote the resulting \(27\)-by-\(36\) zero-one incidence matrix.

**2. Rational spectral calculation.** Each line lies in sixteen double-sixes; each double-six contains twelve lines. For distinct line classes, a skew pair shares six double-sixes and an intersecting pair shares eight. Thus
\[
BB^{\mathsf T}=10I_{27}+2G+6J_{27},
\]
where \(G\) is adjacency for meeting of distinct lines. Its spectrum is \(10^1,1^{20},(-5)^6\), so the Gram matrix has eigenvalues \(192^1,12^{20},0^6\). The exact identity \((BB^{\mathsf T})(BB^{\mathsf T}-12I)(BB^{\mathsf T}-192I)=0\), together with its trace and constant row sum, is independently verified in the certificate. The graph Laplacian is
\[
\mathcal L=\begin{pmatrix}16I_{27}&-B\\-B^{\mathsf T}&12I_{36}\end{pmatrix}.
\]
Its spectrum, with multiplicities, is \(0^1,28^1,10^{20},18^{20},16^6,12^{15}\). In particular the graph is connected. The matrix-tree theorem gives
\[
\tau(\Gamma)=\frac{28\,10^{20}\,18^{20}\,16^6\,12^{15}}{63}=2^{96}3^{53}5^{20}.
\]

**3. Integral classification.** Delete one vertex to obtain a nonsingular \(62\)-by-\(62\) integer Laplacian \(M\). At each prime dividing its determinant, apply exact unit-pivot elimination in \(\mathbb Z/p^{22}\mathbb Z\): a unit pivot splits off a local Smith factor of the current valuation; when the remaining block has no unit, divide that whole block by \(p\) and raise its common valuation by one. This is the usual valuation-preserving local Smith algorithm, not merely a modular rank estimate. The multiplicities for valuations \(0,1,2,3,5\) at \(p=2\) are respectively \(12,28,10,6,6\); at \(p=3\), valuations \(0,1,2,3\) have multiplicities \(42,1,5,14\); and at \(p=5\), valuations \(0,1\) have multiplicities \(42,20\). The three valuation sums are \(96,53,20\), equal to the exponents in the **independently calculated** tree determinant. No other primes can occur. Sorting each prime's valuations and multiplying them positionwise gives the displayed integral invariant factors. The calculations were repeated for two different deleted vertices and yielded identical ordered valuation vectors; sufficient \(p\)-adic precision was maintained throughout (the largest observed valuation is five).

## Verification
The standalone `verify_double_six_graph.py` requires only Python's standard library. Run `python3 verify_double_six_graph.py` from the containing directory. It computes both sixer-based and root-based double-six families, checks their agreement and all \(432\) incidences, verifies the Gram-matrix polynomial and the matrix-tree number, and performs independent local Smith eliminations on two different deleted Laplacians. It terminates with `DOUBLE_SIX_GRAPH_CRITICAL_GROUP_OK`. These are exhaustive *finite* integer calculations; the extension to every smooth characteristic-zero cubic surface follows from the standard blow-up classification, not from checking a sample of surface equations.

## Relationship to prior work
The \(27\) lines and \(36\) double-sixes and their Weyl-group action are classical. Hunt (1995, pp. 4–5) explicitly lists the \(36\) double-sixes, and Alexeev–Donagi–Farkas–Izadi–Ortega (2015, §2) identify them with pairs of opposite \(E_6\)-roots. A previously published result on the *same* \(27\)-by-\(36\) incidence matrix determines the integral cokernel of the matrix \(B\) and its sharp order-four saturation obstruction, including its rational Gram spectrum; it does **not** determine the graph critical group, which is the torsion cokernel of the different \(63\)-by-\(63\) matrix \(\mathcal L\). The novelty asserted here is the full critical group and its prime-local decomposition, not the line configuration, the double-six enumeration, the incidence matrix's original Smith form, or its known rational spectrum. Searches of the graph-Jacobian, root-weight incidence, double-six, and Smith-normal-form literature did not reveal this exact Laplacian decomposition. Such search cannot rule out an older unindexed equivalent computation.

## Limitations
This critical group is the graph's chip-firing/degree-zero divisor-class invariant; it is **not** the Picard group, Néron–Severi lattice, or a torsion subgroup of the cubic surface itself. No result on arithmetic Galois descent, special positive-characteristic geometry, or uniqueness of the graph from its spectrum is claimed. Historical priority remains provisional pending independent specialist review.

## References
1. B. Hunt, *A Gem of the Modular Universe*, arXiv:alg-geom/9503018v1 (first posted 1995-03-27), especially pp. 4–5; https://www.mathcurve.com/surfaces.gb/clebsch/hunt%202.pdf.
2. V. Alexeev, R. Donagi, G. Farkas, E. Izadi and A. Ortega, *The uniformization of the moduli space of principally polarized abelian 6-folds*, arXiv:1507.05710 (first posted 2015-07-21), especially §2; https://arxiv.org/abs/1507.05710.
3. *The order-four integral reconstruction obstruction for Schläfli double-sixes*, publicly accessible research record, 2026; https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-order-four-integral-reconstruction-obstruction-for-schl-fli--0aac314408f8.
