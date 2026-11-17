# Exact deep-hole radial tail of the \(D_4\) Voronoi 24-cell

## Finding
Let \(D_4=\{a\in\mathbb Z^4:\sum_i a_i\in2\mathbb Z\}\), let \(V\) be its Euclidean Voronoi cell at the origin, and let \(X\) be volume-uniform on \(V\). The cell has volume \(2\), covering radius \(1\), and exactly \(24\) maximizing (deep-hole) vertices.

For every real \(0<\varepsilon<1/4\), the complete upper tail of the **squared** nearest-lattice-point error is
\[
\Pr(\|X\|_2^2>1-\varepsilon)
=3\int_{[-1,1]^3}\left(\frac{\varepsilon}{1+\sqrt{1-\varepsilon(1+u_1^2+u_2^2+u_3^2)}}\right)^4du_1\,du_2\,du_3.
\]
It admits the absolutely convergent, strictly positive rational-coefficient expansion
\[
\Pr(\|X\|_2^2>1-\varepsilon)=\frac32\varepsilon^4\sum_{m=0}^\infty b_m\varepsilon^m,
\quad b_m=\frac{4}{(2m+4)4^m}\binom{2m+4}{m}\mathbb E[(1+U_1^2+U_2^2+U_3^2)^m],
\]
where the independent \(U_i\) are uniform on \([-1,1]\). In particular,
\[
\Pr(\|X\|_2^2>1-\varepsilon)
=\frac32\varepsilon^4+3\varepsilon^5+\frac{28}{5}\varepsilon^6+\frac{76}{7}\varepsilon^7+O(\varepsilon^8).
\]
The first four normalized coefficients are \(b_0=1\), \(b_1=2\), \(b_2=56/15\), and \(b_3=152/21\).

## Assumptions and scope
All norms and volumes are ordinary Euclidean ones in \(\mathbb R^4\). The lattice is the **unrescaled**, covolume-two root lattice. The probability concerns the uniform point in a single closed Voronoi cell (boundaries have zero measure). The exact integral and convergent series hold for the indicated open range, not for arbitrary radii. The upper-tail variable is the deficit from **squared** covering radius, not the deficit from covering radius itself.

## Proof
**Cell geometry and volume.** The \(24\) shortest nonzero \(D_4\) vectors are \(\pm e_i\pm e_j\) for distinct indices, with squared length \(2\). Their perpendicular-bisector inequalities are \(|x_i|+|x_j|\le1\). Let \(P\) be their intersection. In each orthant, \(P\) decomposes into the central coordinate cube \([0,1/2]^4\) and four disjoint pyramid-like regions, indexed by the unique coordinate \(x_i>1/2\), with \(x_i=1-t\), \(0\le t<1/2\), and remaining coordinates between zero and \(t\). This decomposition shows that \(P\) is the convex hull of
\[
S=\{\pm e_i:1\le i\le4\}\ \cup\ \{(s_1/2,s_2/2,s_3/2,s_4/2):s_i\in\{-1,1\}\}.
\]
Indeed, central-cube corners with fewer than four nonzero coordinates are convex combinations of the indicated unit vectors and half-coordinate vertices; the spike regions have exactly those corners and their axial tips. All \(24\) displayed vertices have norm \(1\), so \(P\) lies in the closed unit ball. Any other nonzero lattice vector has Euclidean length at least \(2\), hence for \(x\in P\) the Cauchy–Schwarz inequality gives \(x\cdot a\le\|a\|\le\|a\|^2/2\). Its Voronoi inequality follows automatically. Thus \(P=V\), and these are precisely its vertices. The orthant decomposition yields
\[
\operatorname{vol}_4(V)=16\left((1/2)^4+4\int_0^{1/2}t^3\,dt\right)=2.
\]
In particular, the maximal squared norm is \(1\), attained exactly at \(S\).

**Disjoint deep-hole caps.** Distinct elements \(v,w\in S\) satisfy \(v\cdot w\le1/2\). For any \(x\in V=\operatorname{conv}S\),
\[
(v+w)\cdot x\le\max_{z\in S}(v+w)\cdot z\le3/2,
\]
because for \(z=v\) or \(w\) the value is at most \(3/2\), and otherwise both dot products are at most \(1/2\). Therefore the \(24\) open vertex caps \(C_v=\{x\in V:v\cdot x>3/4\}\) are pairwise disjoint. Moreover, if \(\|x\|^2>3/4\) then, expressing \(x\) as a convex combination of \(S\),
\[
\|x\|^2=x\cdot x\le\max_{v\in S}v\cdot x,
\]
so \(x\) belongs to one of the caps. Signed coordinate permutations act transitively on the eight axial vertices. The orthogonal matrix
\[
H=\frac12\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{pmatrix}
\]
permutes \(S\) and takes \(e_1\) to the all-positive half-coordinate vertex. Signed permutations and \(H\) therefore act transitively on all \(24\) vertices, so their cap volumes agree.

**Exact cap integration.** For the cap at \(v=e_1\), write \(x_1=1-t\), \(0\le t<1/4\). The bisector inequalities reduce exactly to \(|x_j|\le t\) for \(j=2,3,4\); all other pairwise inequalities follow since \(2t<1/2\). Put \(x_j=tu_{j-1}\) with \(u\in[-1,1]^3\) and \(A(u)=1+\sum_{j=1}^3u_j^2\). The Jacobian is \(t^3\), and
\[
1-\|x\|^2=2t-A(u)t^2.
\]
For \(0<\varepsilon<1/4\), \(1\le A\le4\) and the quadratic deficit is increasing on \([0,1/4]\). Its crossing of level \(\varepsilon\) occurs at
\[
t_\varepsilon(u)=\frac{1-\sqrt{1-A(u)\varepsilon}}{A(u)}=\frac{\varepsilon}{1+\sqrt{1-A(u)\varepsilon}}<\frac14.
\]
Thus one cap contributes \(\frac14\int_{[-1,1]^3}t_\varepsilon(u)^4du\). Since all \(24\) caps are disjoint, cover the superlevel set, and \(\operatorname{vol}(V)=2\), the exact probability is \((24/2)(1/4)\int t_\varepsilon^4=3\int t_\varepsilon^4\), as asserted.

**All-order convergent expansion.** The Catalan generating function \(C(z)=(1-\sqrt{1-4z})/(2z)\) satisfies \(t_\varepsilon=(\varepsilon/2)C(A\varepsilon/4)\). The identity
\[
[z^m]C(z)^4=\frac4{2m+4}\binom{2m+4}{m}
\]
follows from Lagrange inversion applied to \(C=1+zC^2\). Since \(A\le4\), its power series is uniformly absolutely convergent on the cube for each \(\varepsilon<1/4\). Term-by-term integration gives the stated coefficients. Every coefficient is a strictly positive rational, because each odd uniform moment vanishes and each even moment \(\mathbb E U^{2k}=1/(2k+1)\) is rational. Explicitly,
\[
\mathbb E A^m=\sum_{j_0+\cdots+j_3=m}\frac{m!}{j_0!j_1!j_2!j_3!}\prod_{r=1}^3\frac1{2j_r+1}.
\]
Using the first four values establishes the displayed expansion. This completes the proof.

## Verification
Running `python verify.py` with Python 3 and NumPy reconstructs the \(24\) vertices, checks the transitive Hadamard action and pairwise inner-product bound, verifies exact rational Catalan/moment coefficients, checks the volume normalization, independently samples \(1{,}200{,}000\) volume-uniform points using the central-cube/spike mixture, and compares four numerical tail probabilities against tensor Gauss–Legendre quadrature. All assertions passed. These finite checks corroborate, but do not replace, the exact geometric and analytic proof above.

## Relationship to prior work
Conway and Sloane (1982) computed Voronoi geometry and second moments of root lattices, including the \(24\)-cell, but the inspected geometry and mean-square calculations do not supply this endpoint tail law. Ordentlich (2025) studies the Voronoi spherical CDF and random-lattice bounds; its related-work section acknowledges pre-existing plotted/evaluated radial functions for \(D_4\). Liu (2026), the recent motivating source, proves global optimality of the \(D_4\) lattice for normalized second moment, not a fixed-\(D_4\) endpoint distribution. A prior exact tail law for nearest-vertex quantization of regular simplices concerns a different quantization object and is not an implication for this lattice Voronoi cell. The result here is the explicit all-order upper endpoint distribution for the \(D_4\) squared-error radial statistic, within the stated interval.

## Limitations
No claim is made about the radial CDF below squared radius \(3/4\), optimality of the upper-tail probability among different lattices, or independence of any verification. Historical priority is provisional because older \(D_4\) radial-distribution plots may conceal additional unindexed endpoint calculations. The series and the integral are exact on \(0<\varepsilon<1/4\); their stated validity outside this range is neither proved nor asserted.

## References
- T. Liu, *The optimal four-dimensional lattice quantizer and bounds from Voronoi facets*, arXiv:2611.00100, first publicly posted 2026-10-26; https://arxiv.org/abs/2611.00100.
- O. Ordentlich, *The Voronoi Spherical CDF for Lattices and Linear Codes: New Bounds for Quantization and Coding*, arXiv:2506.19791, first publicly posted 2025-06-24; https://arxiv.org/html/2506.19791.
- J. H. Conway and N. J. A. Sloane, *Voronoi Regions of Lattices, Second Moments of Polytopes, and Quantization*, IEEE Trans. Inform. Theory 28 (1982), 211–226; https://neilsloane.com/doc/Me82.pdf.
