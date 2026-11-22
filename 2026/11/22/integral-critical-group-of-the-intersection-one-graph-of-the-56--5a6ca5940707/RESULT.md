# Integral critical group of the intersection-one graph of the 56 degree-two del Pezzo exceptional curves

## Finding

Let \(S\) be any smooth degree-two del Pezzo surface over an algebraically closed field of characteristic zero. Define \(G(S)\) to have as vertices its \(56\) exceptional \((-1)\)-curves, with an unweighted edge between distinct curves \(D,E\) exactly when \(D\cdot E=1\). Then \(G(S)\) is connected and \(27\)-regular on \(56\) vertices, with \(756\) edges. Its integral graph critical group is

\[
K(G(S))\cong (\mathbb Z/2\mathbb Z)^{14}\oplus(\mathbb Z/4\mathbb Z)^7\oplus(\mathbb Z/28\mathbb Z)^5\oplus(\mathbb Z/336\mathbb Z)^{14}\oplus\mathbb Z/3024\mathbb Z\oplus(\mathbb Z/6048\mathbb Z)^6.
\]

The number of spanning trees is \(2^{128}3^{35}7^{26}\), and the exponent of the critical group is \(6048\). The graph is the distance-two graph of the \(56\)-vertex Gosset graph (whose edges represent *disjoint* exceptional curves), rather than the Gosset graph itself.

## Assumptions and scope

An exceptional curve means an irreducible \((-1)\)-curve on \(S\). By the classical classification, write \(S\) as the blowup of \(\mathbb P^2\) in seven general geometric points. Let \(H,E_1,\ldots,E_7\) denote the standard Picard basis, with \(H^2=1\), \(E_i^2=-1\), and all other basis pairings zero. The 56 exceptional classes are:

\[
\begin{array}{ll}
E_i &(7\text{ classes}),\\
H-E_i-E_j\quad(i<j)&(21\text{ classes}),\\
2H-\sum_{i\in I}E_i\quad(|I|=5)&(21\text{ classes}),\\
3H-2E_i-\sum_{j\ne i}E_j &(7\text{ classes}).
\end{array}
\]

These classes and their pairings are constant over the smooth geometric moduli family, hence the assertion applies to every such \(S\). The edges have multiplicity one even when intersection multiplicity is geometrically concentrated at a special point. The claim concerns the *combinatorial graph Jacobian*, not the algebraic Picard group of \(S\) or the Jacobian of its branch quartic.

## Proof

**1. Geometric adjacency.** Encode every divisor by \((d;m_1,\ldots,m_7)\) representing \(dH-\sum m_iE_i\). The intersection product is \(dd'-\sum m_im_i'\). Directly comparing the four complete families above gives, for each curve \(D\), exactly 27 curves of intersection zero, 27 of intersection one, and one of intersection two. The last is the Geiser mate \(\iota(D)=-K_S-D\), because \(-K_S=3H-\sum E_i\). This proves the vertex count, degree, and edge count, and identifies the distance-two relation in the usual Gosset graph. Connectedness also follows from the eigenvalues below.

**2. Spectral calculation independent of Smith reduction.** Let \(V\) be the \(56\times8\) integer matrix of the 56 divisor-coordinate row vectors in the signed Picard basis \((H,E_1,\ldots,E_7)\), let \(J=\mathrm{diag}(1,-1,\ldots,-1)\), and set \(M=VJV^{\mathsf T}\). Let \(P\) be the permutation matrix of the 28 Geiser swaps. The unweighted adjacency matrix satisfies the exact integer identity

\[A=M+I-2P.\]

The eight-by-eight matrix \(T=V^{\mathsf T}VJ\) has first row \((168,60,\ldots,60)\), and its lower seven rows have first entry \(-60\), diagonal entry \(-32\), and other entries \(-20\). Thus \(T\) has eigenvalue \(-12\) on the six-dimensional coordinate-sum-zero subspace; its remaining two-by-two block is \(\left(\begin{smallmatrix}168&420\\-60&-152\end{smallmatrix}\right)\), with eigenvalues \(28,-12\). Hence the nonzero spectrum of \(M\) is \(28\) once and \(-12\) seven times.

On the 28-dimensional \(+1\) eigenspace of \(P\), the matrix \(M\) has only the eigenvalue 28 on the constant vector and vanishes on the other 27 dimensions: pair-sums of divisor coordinates are all \(-K_S\). On the 28-dimensional \(-1\) eigenspace of \(P\), \(M\) has eigenvalues \(-12\) seven times and zero 21 times. Consequently

\[\operatorname{spec}(A)=\{27^{[1]},(-1)^{[27]},3^{[21]},(-9)^{[7]}\}.\]

In particular, 27 has multiplicity one, proving connectedness. The matrix-tree theorem then gives

\[\tau(G)=\frac{24^{21}28^{27}36^7}{56}=2^{128}3^{35}7^{26}.\]

**3. Integral primary factors.** Remove any one row and column from \(L=27I-A\), obtaining a \(55\times55\) integer reduced Laplacian \(R\). For each prime dividing the determinant, perform unit-pivot row and column eliminations over \(\mathbb Z/p^k\mathbb Z\), choosing at each stage a remaining entry with least \(p\)-adic valuation and normalizing its unit. The complete valuation multiplicities are:

| prime | \(p\)-adic valuation and multiplicity | modulus precision |
|---|---|---|
| \(2\) | \(0:8,\ 1:14,\ 2:12,\ 4:15,\ 5:6\) | \(2^{12}\) |
| \(3\) | \(0:34,\ 1:14,\ 3:7\) | \(3^{10}\) |
| \(7\) | \(0:29,\ 1:26\) | \(7^8\) |

At each stage the chosen least-valuation element divides every element of the remaining block in the principal ideal ring, so the recorded row and column operations diagonalize that block without changing its cokernel. Every recorded valuation is strictly below the modulus precision. Their weighted sums equal respectively \(128,35,26\), the exact valuations of \(\det R\); hence none is omitted or underdetermined. All other primary components vanish by the exact determinant formula. Sorting each prime's 55 exponents and combining corresponding entries yields eight unit invariant factors and the displayed nonunit factors, which form a divisibility chain. This establishes the full integral critical group, not just its order.

## Verification

Run `python3 verify.py` using Python 3, without third-party dependencies. The program independently enumerates the four geometric curve families, checks all 56 intersection-neighborhood distributions and the Geiser-pair identity, derives the eight-by-eight Gram identity, calculates a full exact integer reduced-Laplacian determinant using fraction-free Bareiss elimination, and computes the local Smith valuations. It repeats all local calculations with three different deleted vertices. It also checks the invariant-factor divisibility chain and product against the spanning-tree count. Its success line is `DEGREE_TWO_DEL_PEZZO_INTERSECTION_ONE_CRITICAL_GROUP_VERIFIED_OK`.

## Relationship to prior work

Lee's 2009 analysis of Gosset polytopes in del Pezzo Picard groups describes the 56 curves, the Geiser involution, and the intersection-zero and intersection-one neighbor classes (notably Lemmas 6 and 7). Lee's 2010 paper studies configurations of fixed-intersection simplexes, while Knecht and Reyes (2015) give the complete four-family exceptional-curve enumeration. Lee and Shin (2016) study the geometry and Weyl-equivariant polytope correspondences. These supply the geometric ingredients but do not establish the displayed integral reduced-Laplacian Smith invariants. The distinction between intersection-one edges and ordinary Gosset edges is essential: the latter encode *zero* intersection and have a different adjacency spectrum. General critical-group methods do not determine this particular integral decomposition without a local Smith calculation.

## Limitations

The theorem is restricted to characteristic zero, although the integer graph itself makes sense independently of a field. It does not establish a canonical isomorphism with any algebraic divisor-class or Jacobian group, nor an equivariant representation of \(W(E_7)\) on the critical group. Scientific priority remains provisional: mathematically equivalent calculations could occur in unindexed graph tables or under the name of a Gosset distance graph. No independent mathematical review is claimed.

## References

1. J.-H. Lee, *Gosset Polytopes in Picard groups of del Pezzo Surfaces*, first public arXiv version 19 May 2009, https://arxiv.org/abs/0905.3025 ; later Canadian Journal of Mathematics 64 (2012), 123–150.
2. J.-H. Lee, *Configuration of lines in del Pezzo surfaces with Gosset Polytopes*, arXiv 1001.4174, first public 23 January 2010, https://arxiv.org/abs/1001.4174 .
3. A. Knecht and K. Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields*, arXiv 1510.04621, first public 15 October 2015, https://arxiv.org/abs/1510.04621 .
4. J.-H. Lee and Y. Shin, *E-Polytopes in Picard Groups of Smooth Rational Surfaces*, Symmetry 8 (2016), article 27, 20 April 2016, https://doi.org/10.3390/sym8040027 .
