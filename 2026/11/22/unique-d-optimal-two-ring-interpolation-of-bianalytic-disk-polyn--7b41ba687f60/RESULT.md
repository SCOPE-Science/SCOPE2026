# Unique D-optimal two-ring interpolation of bianalytic disk polynomials

## Finding

For each integer \(N\ge 1\), let
\[
\mathcal B_N=\{p(z)+\overline z\,q(z):\deg p,\deg q\le N\},\qquad \dim_{\mathbb C}\mathcal B_N=2(N+1).
\]
Consider the minimal-size, two-orbit point-evaluation design formed by two regular \((N+1)\)-gons,
\[
Z_{r,s,\phi}=\{r\omega^j:0\le j\le N\}\cup
 \{s e^{i\phi}\omega^j:0\le j\le N\},
\qquad \omega=e^{2\pi i/(N+1)},\quad 0<r<s\le1.
\]
With the fixed coefficient basis \((1,z,\ldots,z^N,\overline z,\overline z z,\ldots,\overline z z^N)\), write \(A_N(r,s,\phi)\) for the square evaluation matrix. Its exact Gram determinant is
\[
\det(A_N^*A_N)=(N+1)^{2(N+1)}(rs)^{N(N-1)+2}
(s^2-r^2)^{2N}\left|s^{N-1}e^{i(N+1)\phi}-r^{N-1}\right|^2.
\tag{1}
\]
Consequently the global maximum **within this two-regular-polygon design class in the closed unit disk** is attained precisely at \(s=1\), \(e^{i(N+1)\phi}=-1\), and \(r=\sqrt{t_N}\), where \(t_N\in(0,1)\) is the unique root of
\[
\frac{N(N-1)+2}{2}-\frac{2Nt}{1-t}
 +\frac{(N-1)t^{(N-1)/2}}{1+t^{(N-1)/2}}=0.
\tag{2}
\]
Uniqueness is understood modulo common rotation and relabeling points on each polygon. The inner squared radius satisfies \(t_1=1/3\) and
\[
t_N=1-\frac4N+O(N^{-2})\quad\text{as }N\to\infty.
\tag{3}
\]
For \(N\ge2\), every design with \(0<r<s\) is unisolvent, irrespective of relative angle. For \(N=1\), unisolvency additionally requires \(e^{2i\phi}\ne1\).

## Assumptions and scope

The objective is the raw squared modulus of the determinant of the point-evaluation matrix. Any other fixed basis changes this by a positive factor independent of the design; thus the maximizing nodes are basis invariant. All nodes are on two **regular**, centered, equally populated polygons, with the two rings of positive distinct radii and arbitrary relative angular shift. No claim is made about unrestricted configurations of \(2(N+1)\) points. Boundary evaluation is well defined because all functions are polynomials. If all nodes must lie in the *open* disk, the same supremum is approached as \(s\uparrow1\), but is not attained.

## Proof

Set \(M=N+1\). Take a unitary discrete Fourier transform separately in the row samples of each polygon. Frequencies of \(z^j\) and \(\overline z z^{j+1}\) agree modulo \(M\) for \(0\le j<N\). Each such residue yields a two-by-two block with inner row \((r^j,r^{j+2})\) and outer row \(e^{ij\phi}(s^j,s^{j+2})\). Its determinant is \(r^j s^j e^{ij\phi}(s^2-r^2)\).

The remaining residue comprises \(z^N\) and \(\overline z\), with block
\[
\begin{pmatrix}r^N&r\\s^Ne^{iN\phi}&se^{-i\phi}\end{pmatrix},
\]
whose determinant has modulus \(rs\,|s^{N-1}e^{iM\phi}-r^{N-1}|\). Every residue block inherits a factor \(M\) in its two-row determinant from the unitary Fourier transforms. Squaring the product proves (1), including its exact normalization. Positivity of its factors gives the stated rank criterion; in the final residue, cancellation requires \(e^{iM\phi}=(r/s)^{N-1}\), which is impossible for \(N>1\) and is equivalent to \(e^{2i\phi}=1\) for \(N=1\).

Write \(r=s\sqrt t\). The determinant in (1) equals \(s^{2M^2}\) times a strictly positive function of \((t,\phi)\), so its maximum has \(s=1\). For fixed positive \(r<s\), the last factor in (1) is strictly maximized exactly when \(e^{iM\phi}=-1\). The exact angular squared-distance loss is
\[
(s^{N-1}+r^{N-1})^2-
|s^{N-1}e^{iM\phi}-r^{N-1}|^2
=2(rs)^{N-1}[1+\cos(M\phi)].
\]

It remains to maximize on \(0<t<1\) the function
\[
F_N(t)=t^{a}(1-t)^{2N}(1+t^b)^2,\quad
 a=\frac{N(N-1)+2}{2},\quad b=\frac{N-1}{2}.
\]
The logarithmic derivative multiplied by \(t\) is precisely the left side of (2). To prove strict concavity, differentiate twice:
\[
(\log F_N)''(t)=-\frac a{t^2}-\frac{2N}{(1-t)^2}
 +\frac{2b t^{b-2}(b-1-t^b)}{(1+t^b)^2}.
\]
For \(b\le1\) the final term is nonpositive. For \(b>1\), since \(0<t<1\), the final term is at most \(2b(b-1)/t^2<a/t^2\); indeed \(a-2b(b-1)=(3N-1)/2>0\). Thus \(\log F_N\) is strictly concave on \((0,1)\). Since \(F_N\to0\) at both endpoints, it has precisely one maximizer, characterized by (2). For \(N=1\), the equation reduces to \(1-2t/(1-t)=0\), giving \(t_1=1/3\).

Finally, (2) can be written
\[
\frac{2Nt_N}{1-t_N}
=\frac{N(N-1)+2}{2}+
\frac{(N-1)t_N^{(N-1)/2}}{1+t_N^{(N-1)/2}}.
\]
The final term lies between zero and \(N-1\), uniformly in \(N\). Solving for \(1-t_N\), using the leading term \(N^2/2\) on the right, proves (3). All claims hold for every integer \(N\ge1\).

## Verification

A standalone Python 3 checker (`CHECK.py`) computes the complex determinant directly by Gaussian elimination and compares it against (1) for degrees one through eight and 12 independent parameter triples at each degree. It also solves (2) by bisection, checks local optimality and the expected large-degree scaling. The saved checker completed 141 diagnostic assertions. These finite diagnostics are not substitutes for the all-degree factorization and concavity proof above.

Representative optimal inner squared radii are \(t_2\approx0.372957494237\), \(t_3\approx0.434258545911\), \(t_4\approx0.492739039179\), and \(t_8\approx0.654379245913\).

## Relationship to prior work

The construction is motivated by the explicit disk polyanalytic spaces and polynomial bases of El Harti–ElKachkouri–Ghanmi (2020). Speckbacher (2022) considers uniqueness and sampling on infinitely many concentric trajectories for polyanalytic short-time Fourier transforms; his setting does not determine this finite-dimensional bianalytic determinant or its optimal radius. Dell'Accio–Sommariva–Vianello (2023) treats generic random unisolvency, rather than exact symmetry-constrained determinant optimization. Borodin–Fedorovskiy (2026) use two concentric circles as pole sets for bianalytic rational approximation, a different problem from polynomial evaluation at two polygon orbits. The novelty asserted here is **the joint exact two-ring determinant, exceptional low-degree unisolvency, uniquely optimal radius for each degree, and its asymptotic boundary layer**, not the general principles of Fourier aliasing or determinant-based interpolation.

## Limitations

Optimization is restricted to two regular concentric \((N+1)\)-gons with equal point weights. D-optimality is a volume/determinant criterion, not a claim of best spectral condition number or of pointwise noise minimax optimality. The boundary optimum does not belong to the open disk if strict interior sampling is required. The historical-priority comparison is best-knowledge and does not establish absolute novelty; related general Fekete and weighted sampling results may contain an implicit equivalent formulation. An independent audit has not been performed.

## References

1. R. El Harti, A. ElKachkouri and A. Ghanmi, *A note on weighted poly-Bergman spaces*, first public 28 August 2020, arXiv:2008.12764v1, https://arxiv.org/abs/2008.12764.
2. M. Speckbacher, *Sampling Trajectories for the Short-Time Fourier Transform*, *Journal of Fourier Analysis and Applications* **28** (2022), article 82, https://doi.org/10.1007/s00041-022-09977-9.
3. F. Dell'Accio, A. Sommariva and M. Vianello, *Random sampling and unisolvent interpolation by almost everywhere analytic functions*, first public 24 March 2023, arXiv:2303.14074v1, https://arxiv.org/abs/2303.14074.
4. P. A. Borodin and K. Yu. Fedorovskiy, *Approximation by sums of shifts of the function conjugate(z)/z*, *Sbornik: Mathematics* **217** (2026), 129–144, https://doi.org/10.4213/sm10298e.
