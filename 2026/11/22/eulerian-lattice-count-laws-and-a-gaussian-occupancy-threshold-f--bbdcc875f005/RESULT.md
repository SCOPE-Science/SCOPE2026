# Eulerian lattice-count laws and a Gaussian occupancy threshold for smooth simplex frusta

## Finding
For integers \(r\ge 2\) and \(c\ge 1\), consider the full-dimensional smooth lattice polytope
\[
Q_{r,c}=\{(x,z)\in\mathbb R^r\times\mathbb R:\ 0\le z\le1,\ x_i\ge0,\ \sum_{i=1}^r x_i\le1+cz\}.
\]
Choose \(U\) uniformly on the \((r+1)\)-dimensional unit torus and count \(N_{r,c}=\#((Q_{r,c}+U)\cap\mathbb Z^{r+1})\). Set \(A(n,j)\) to be the number of permutations of \(n\) elements with exactly \(j\) descents, for \(0\le j<n\). Let \(K\) be uniform on \(\{1,\ldots,c\}\), independently of \(J\), where
\[
 \Pr(J=j)=\frac{A(r+1,j)}{(r+1)!},\qquad 0\le j\le r.
\]
Then the **complete exact distribution** is
\[
 N_{r,c}\ \stackrel{\rm d}=\ B_r(K-J),\qquad
 B_r(t)=\begin{cases}\binom{t+r}{r},&t\ge0,\\0,&t<0.\end{cases}
\tag{1}
\]
Its support is exactly \(\{0\}\cup\{\binom{m+r}{r}:0\le m\le c\}\), with all atoms present. In particular, for \(0\le m\le c\),
\[
 \Pr\left(N_{r,c}=\binom{m+r}{r}\right)
 =\frac{1}{c(r+1)!}\sum_{j=\max(0,1-m)}^{\min(r,c-m)} A(r+1,j),
\tag{2}
\]
with an empty sum equal to zero, and
\[
 \Pr(N_{r,c}=0)=\frac1{c(r+1)!}\sum_{j=2}^{r} A(r+1,j)\min(c,j-1).
\tag{3}
\]
For \(c>r\) the interior atoms satisfy the exact plateau law \(\Pr(N_{r,c}=\binom{m+r}{r})=1/c\) whenever \(1\le m\le c-r\). The expectation is
\[
 \mathbb E N_{r,c}=\frac{(c+1)^{r+1}-1}{c(r+1)!}.
\tag{4}
\]
For any integer sequence \(c_r\ge1\) with \(c_r/r\to\alpha\in(0,\infty)\), the **nonempty-translate probability** has the sharp phase transition
\[
\lim_{r\to\infty}\Pr(N_{r,c_r}>0)=
\begin{cases}0,&\alpha\le\tfrac12,\\1-\dfrac1{2\alpha},&\alpha>\tfrac12.\end{cases}
\tag{5}
\]
In the critical window \(c_r=r/2+\lambda\sqrt r+o(\sqrt r)\), \(\lambda\in\mathbb R\), one has
\[
\lim_{r\to\infty}\sqrt r\,\Pr(N_{r,c_r}>0)
 =2\left[\lambda\Phi(\sqrt{12}\lambda)+\frac{\phi(\sqrt{12}\lambda)}{\sqrt{12}}\right],
\tag{6}
\]
where \(\Phi\) and \(\phi\) denote the standard Gaussian cumulative distribution and density. At fixed \(r\), as \(c\to\infty\), \(N_{r,c}/c^r\) converges in distribution to \(V^r/r!\), where \(V\) is uniform on \([0,1]\); its coefficient of variation approaches \(r/\sqrt{2r+1}\).

## Assumptions and scope
The lattice is the standard \(\mathbb Z^{r+1}\) with torus translation in the displayed coordinates, without random rotations or independent resampling at separate heights. The boundary-equality events have translation probability zero. The claim is for integers \(r\ge2\), \(c\ge1\); the arguments also specialize to \(r=1\), with the zero atom absent. The body has \(r+3\) facets and dimension \(r+1\); its smoothness and its integer-dilation Ehrhart polynomial are established in Liu–Tang–Tao–Zhang, Proposition 5.1 (2026), and are not claimed as new.

## Proof
**Step 1 (one random integer section).** Write the translation as \(U=(u_1,\ldots,u_r,u_z)\in[0,1)^{r+1}\). Almost surely \(Q_{r,c}+U\) meets only the integer-height plane \(z=1\). Undoing the translation gives section height \(h=1-u_z\), uniform on \((0,1)\). Every integer point in that section has horizontal coordinates \((1+k_1,\ldots,1+k_r)\) with \(k_i\ge0\) integers. Set \(v_i=1-u_i\). The simplex constraint becomes
\[
 k_1+\cdots+k_r\le 1+ch-(v_1+\cdots+v_r).
\tag{7}
\]
The horizontal \(v_i\) and \(h\) are mutually independent uniform variables.

**Step 2 (a uniform integer, plus a uniform fractional phase).** Since \(c\) is a positive integer, the random variable \(1+ch\) decomposes as \(K+T\), where \(K\) is uniform on \(\{1,\ldots,c\}\), \(T\) is uniform on \((0,1)\), and \(K,T,v_1,\ldots,v_r\) are jointly independent. Put \(W=v_1+\cdots+v_r+(1-T)\) and \(J=\lfloor W\rfloor\). Off the null set of integer \(W\), inequality (7) reduces to \(\sum k_i\le K-J\). The weak-composition count is \(\binom{K-J+r}{r}\) for \(K\ge J\), and zero otherwise. This proves (1), once the law of \(J\) is identified.

**Step 3 (Eulerian cubical slices).** The variable \(W\) is a sum of \(n=r+1\) independent uniform \((0,1)\) variables. By inclusion–exclusion in the unit cube, for integers \(0\le j\le n-1\),
\[
\Pr(j<W<j+1)
=\frac1{n!}\sum_{k=0}^{j+1}(-1)^k\binom{n+1}{k}(j+1-k)^n
=\frac{A(n,j)}{n!}.
\tag{8}
\]
The final identity is the classical Eulerian inclusion–exclusion formula, independently available from the cube-slice enumeration in Schmidt–Simion (1997, §2). Thus (1) holds. Summing over \(K=m+j\in\{1,\ldots,c\}\) gives (2), and counting \(K<J\) gives (3). Since \(A(n,j)>0\) for all its legitimate indices, every asserted atom occurs, including zero because \(r\ge2\) permits \(J=2,K=1\). For \(1\le m\le c-r\), all \(j=0,\ldots,r\) contribute; the Eulerian numbers sum to \((r+1)!\), proving the plateau.

**Step 4 (mean).** Integrating over the unit translation torus and partitioning into integer cells shows that \(\mathbb E N_{r,c}\) equals the Euclidean volume of \(Q_{r,c}\). Its sections are \((1+cz)\Delta_r\), so
\[
\operatorname{vol}_{r+1}(Q_{r,c})
=\frac1{r!}\int_0^1(1+cz)^r\,dz
=\frac{(c+1)^{r+1}-1}{c(r+1)!}.
\]
This proves (4), independently corroborating the finite formula.

**Step 5 (occupancy threshold).** Write \(J_r\) as the integer part of the sum of \(r+1\) independent uniform variables. Its mean is \(r/2\): by symmetry \(J_r\) has the same distribution as \(r-J_r\). Moreover,
\[
\frac{J_r-r/2}{\sqrt r}\Rightarrow\mathcal N(0,1/12)
\tag{9}
\]
by the classical central limit theorem; taking an integer part changes the normalized sum by at most \(1/\sqrt r\). Conditional on \(J_r=j\), the nonempty event is \(K\ge j\), so
\[
\Pr(N_{r,c}>0)=\frac1c\,\mathbb E\left[\min\{c,(c-J_r+1)_+\}\right].
\tag{10}
\]
Here \((t)_+=\max(t,0)\). Since \(J_r/r\to 1/2\) in probability and \(K/r\) converges to a uniform \([0,\alpha]\) variable independently, (10) yields (5). For the window in (6), the clipped term in (10) differs from \((c-J_r+1)_+\) only on \(J_r=0\), whose probability is \(1/(r+1)!\). The family \((J_r-r/2)/\sqrt r\) has uniformly bounded second moments (from the independent-uniform representation), so its positive-part expectations are uniformly integrable. Put \(\sigma=1/\sqrt{12}\). Multiplying (10) by \(\sqrt r\), applying (9) and the critical expansion of \(c_r\), yields \(2\mathbb E(\lambda-\sigma Z)_+\), with \(Z\) standard normal. Integration gives \(\mathbb E(\lambda-\sigma Z)_+=\lambda\Phi(\lambda/\sigma)+\sigma\phi(\lambda/\sigma)\), completing (6).

**Step 6 (fixed-dimensional large shear).** For fixed \(r\), \(J_r\) is bounded by \(r\); moreover \(K/c\Rightarrow V\) uniform \([0,1]\). Since \(B_r(k)=k^r/r!+O_r(k^{r-1})\) for positive \(k\), (1) gives \(N_{r,c}/c^r\Rightarrow V^r/r!\), with convergence of both initial moments by uniform boundedness. The limiting first and second moments are \(1/((r+1)r!)\) and \(1/((2r+1)(r!)^2)\), yielding the asserted coefficient of variation.

## Verification
The accompanying `verify_eulerian.py` checks that each exact mass is a nonnegative rational number and totals one, its support and mean agree with (1)–(4) for a finite parameter grid, and direct integer-point enumeration in translated frusta matches (7) for pseudorandom test translations. It also computes the two sides of (6) at increasing dimensions as a numerical cross-check. These are finite checks: infinite validity depends on the preceding analytic argument. Section geometry and smoothness were separately verified against Proposition 5.1 of the motivating paper.

## Relationship to prior work
Liu, Tang, Tao, and Zhang (2026, Proposition 5.1) define the same smooth family and determine its **integer-dilation Ehrhart polynomial**, but not the distribution under random torus translation. Schlie (2026) surveys randomized lattice-point counts and variance questions; its discussed theorems concern general discrepancy, smooth-body estimates, and annular counts, rather than this explicit distribution. Schmidt and Simion (1997, §2) give the classical Eulerian law for unit-cube slabs (equivalently the integer part of a sum of independent uniforms), which is explicitly used here as an input. The additional result is the independent uniform layer decomposition, exact distribution of **all** count atoms of the smooth frusta and their sharp dimension–shear occupancy transition. Neither the same body's previously available Ehrhart-numerator classification nor its Ehrhart polynomial alone determines these random-translate probabilities.

## Limitations
No novelty is asserted for Eulerian numbers, cube-slice probabilities, weak compositions, or the smoothness and Ehrhart polynomial of these frusta. Priority is conditional on accessible indexed literature; unindexed or otherwise inaccessible work could contain equivalent random-translate laws. The Gaussian window (6) governs the probability of **at least one** lattice point, not the whole count's centered distribution. There is no assertion for arbitrary sheared prisms, arbitrary convex bodies, random orientations, or all parameter trajectories beyond the stated asymptotic regimes. The verification program's finite checks are not certificates for the infinite claims.

## References
1. F. Liu, J. Tang, S. Tao, and Z. Zhang, *Ehrhart positivity of smooth polytopes with few facets*, arXiv:2610.27819v1 (first public 20 October 2026), especially §5, Proposition 5.1. https://arxiv.org/abs/2610.27819v1
2. S. Schlie, *On the randomized lattice-point count problem*, arXiv:2611.16769v1 (first public 12 November 2026), especially §§1, 4, 7. https://arxiv.org/abs/2611.16769v1
3. F. Schmidt and R. Simion, *Some geometric probability problems involving the Eulerian numbers*, Electronic Journal of Combinatorics 4(2), R18 (1997), especially §2. https://doi.org/10.37236/1333
