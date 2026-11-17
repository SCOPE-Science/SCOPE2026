# Sharp three-rotation area rigidity for regular Reuleaux odd-gons

## Finding
Fix an odd integer \(n\ge3\) and width \(w>0\). Let \(R_n(w)\) be the centered **regular Reuleaux \(n\)-gon**, and for arbitrary angles \(\alpha_1,\alpha_2,\alpha_3\in\mathbb R\) form their equally weighted Minkowski mean
\[
K_{\boldsymbol\alpha}=\tfrac13\bigl(R_{\alpha_1}R_n(w)+R_{\alpha_2}R_n(w)+R_{\alpha_3}R_n(w)\bigr).
\]
Here \(R_\alpha\) means rotation by \(\alpha\) about the regular body's symmetry center, and \(n\)-fold rotational symmetry makes each angle periodic modulo \(2\pi/n\). Put \(c=\pi/(2n)\).

**Sharp minimum and rigidity.** Over all triples of rotations, the minimum area is
\[
\boxed{A_{\min}=\frac{w^2}{2}\bigl(\pi-n\tan c\bigr).}
\]
Equality holds if and only if all three rotations agree modulo \(2\pi/n\). This is the classical area of the original regular Reuleaux body, included to make the three-rotation range complete.

**Sharp maximum and rigidity.** The maximum area is \(\pi w^2/4-D_{n,3}\), with strictly positive residual disk deficit
\[
\boxed{D_{n,3}=w^2\left[\frac{n}{6\cos c}\left(\sin c-2\sin\frac c3\right)-\frac\pi{36}\right]>0.}
\]
Equality holds precisely when, modulo a common rotation, the three angles form the set
\[
\boxed{\left\{\alpha_0,\;\alpha_0+\frac{2\pi}{3n},\;\alpha_0+\frac{4\pi}{3n}\right\}\pmod{2\pi/n};}
\]
permutations do not alter the mean. Thus optimal three-copy averaging is achieved by *equal phase gaps*, yet is never the disk (in contrast to suitable two-copy averaging). Its sharp residual deficit obeys
\[
D_{n,3}=\frac{\pi^3w^2}{3888n^2}+O\!\left(\frac{w^2}{n^4}\right)\quad(n\to\infty\text{ through odd integers}).
\]

**Local phase stability.** Let \(t_i=n\alpha_i\pmod{2\pi}\), cyclically ordered, and write their three circular gaps as \(x,y,z\), so \(x+y+z=2\pi\). In a neighborhood of the maximizing configuration, set \(\eta=(x,y,z)-(2\pi/3,2\pi/3,2\pi/3)\). Then
\[
\boxed{A_{\max}-\operatorname{area}(K_{\boldsymbol\alpha})
=\frac{w^2\sin(\pi/(6n))}{18n\cos(\pi/(2n))}\,\|\eta\|_2^2+O_{n,w}(\|\eta\|_2^3).}
\]
The positive quadratic coefficient gives a strict nondegenerate optimizer modulo common rotation and permutation.

## Assumptions and scope
The regular Reuleaux odd-\(n\)-gon is the planar constant-width \(w\) convex body with \(n\)-fold rotational and reflection symmetry and alternating straight-normal curvature-radius values \(0,w\). More precisely, after an appropriate choice of normal-angle origin, its curvature radius, interpreted almost everywhere as \(h+h''\), is
\[
\rho_n(\theta)=\frac w2\left(1+\operatorname{sgn}(\cos n\theta)\right).
\]
This is consistent for odd \(n\) with constant width, since opposite normals have complementary curvature radius. The support function is continuously differentiable and piecewise twice differentiable, and the standard area identity for support functions applies by approximation or weak derivatives. All areas are ordinary planar Lebesgue areas. The rotations have equal weights \(1/3\); there is no claim for arbitrary weights, arbitrary constant-width bodies, or a general number of summands. The integer \(n\) counts the curved corners of the regular Reuleaux polygon, not the number of Minkowski summands.

## Proof
**1. Fourier energy formula.** The Fourier expansion of the curvature radius is
\[
\rho_n(\theta)=\frac w2+\frac{2w}{\pi}\sum_{\substack{j\ge1\\j\text{ odd}}}
\frac{(-1)^{(j-1)/2}}j\cos(nj\theta).
\]
Because \(n\ge3\), integration of \(h+h''=\rho_n\) gives the centered support function, with the nonconstant harmonic \(nj\) having coefficient
\[
a_{nj}=\frac{2w(-1)^{(j-1)/2}}{\pi j(1-n^2j^2)}.
\]
The support coefficients decay cubically. For any planar convex body with support Fourier coefficients \(a_k,b_k\) and mean support \(w/2\), Green's formula and Parseval give
\[
\frac{\pi w^2}{4}-\operatorname{area}(K)
=\frac\pi2\sum_{k\ge2}(k^2-1)(a_k^2+b_k^2).
\]
The normalized phase factors are \(e^{ij t_i}\), where \(t_i=n\alpha_i\) modulo \(2\pi\). Therefore
\[
\boxed{\frac{\pi w^2}{4}-\operatorname{area}(K_{\boldsymbol\alpha})
=\frac{2w^2}{9\pi}\sum_{\substack{j\ge1\\j\text{ odd}}}\frac{\left|e^{ijt_1}+e^{ijt_2}+e^{ijt_3}\right|^2}{j^2(n^2j^2-1)}.}\tag{1}
\]
All terms are nonnegative, and the series converges absolutely. In particular the area is at most the disk area, and an equal-step triple leaves nonzero harmonics \(j\equiv3\pmod6\).

**2. Exact pair kernel.** Define the even, \(2\pi\)-periodic kernel
\[
F_n(t)=\sum_{\substack{j\ge1\\j\text{ odd}}}\frac{\cos(jt)}{j^2(n^2j^2-1)}.
\]
Elementary partial fractions give
\[
\frac1{j^2(n^2j^2-1)}=-\frac1{j^2}+\frac{n^2}{n^2j^2-1}.
\]
For \(0\le t\le\pi\), the odd cosine sums are
\[
\sum_{j\text{ odd}}\frac{\cos jt}{j^2}=\frac{\pi^2}{8}-\frac{\pi t}{4},\qquad
\sum_{j\text{ odd}}\frac{\cos jt}{n^2j^2-1}
=\frac\pi{4n\cos c}\sin\frac{\pi/2-t}{n}.
\]
(The second identity follows, for example, by integrating against all cosine basis functions on \([0,\pi]\), or by the elementary partial-fraction expansion of the resolvent; it also appears in the motivating symmetric-area analysis.) Hence
\[
\boxed{F_n(t)=-\frac{\pi^2}{8}+\frac{\pi t}{4}
+\frac{\pi n}{4\cos c}\sin\frac{\pi/2-t}{n},\quad0\le t\le\pi.}\tag{2}
\]
In particular, \(F_n(\pi)=-F_n(0)\). Differentiation gives, on \((0,\pi)\),
\[
F_n'(t)=\frac\pi4\left(1-\frac{\cos((\pi/2-t)/n)}{\cos c}\right)<0,
\qquad
F_n'(t)=0\Longleftrightarrow t\in\{0,\pi\}
\quad\text{on }[0,\pi].\tag{3}
\]
Both the derivative and the kernel extend continuously across the endpoints under even periodic continuation.

Let \(x,y,z\in[0,2\pi]\) be the successive circular gaps of the sorted phases, with \(x+y+z=2\pi\). Expanding the squared modulus in (1) yields
\[
\frac{\pi w^2}{4}-\operatorname{area}(K_{\boldsymbol\alpha})
=\frac{2w^2}{9\pi}\left(3F_n(0)+2[F_n(x)+F_n(y)+F_n(z)]\right).\tag{4}
\]
Thus maximizing area is the genuine three-point energy problem of minimizing \(F_n(x)+F_n(y)+F_n(z)\) over the closed triangular simplex.

**3. Unique optimal circular gaps.** On \((0,\pi)\), \(F_n'<0\); on \((\pi,2\pi)\), \(F_n'>0\). If all gaps are strictly positive and one exceeds or equals \(\pi\), transferring a small amount from that gap to a smaller gap strictly decreases the sum in (4), so such a configuration cannot minimize it. Any interior minimizer must therefore have all three gaps in \((0,\pi)\). The Lagrange multiplier condition is
\[
F_n'(x)=F_n'(y)=F_n'(z).
\]
By (3) and strict monotonicity of cosine with respect to the absolute angle in this range, equality of derivatives for two gaps in \((0,\pi)\) implies either that the gaps agree or that they sum to \(\pi\). The second possibility would make the third gap exactly \(\pi\), impossible here. Thus \(x=y=z=2\pi/3\).

On the boundary of the simplex, at least one gap is zero, say \(x=0\), and \(z=2\pi-y\). Even periodicity and the strict decrease of \(F_n\) on \([0,\pi]\) give
\[
F_n(0)+F_n(y)+F_n(z)\ge F_n(0)+2F_n(\pi)=-F_n(0).
\]
From (2), however,
\[
3F_n(2\pi/3)+F_n(0)=\frac{\pi n}{4\cos c}\left(\sin c-3\sin\frac c3\right)<0,
\]
since \(\sin(3s)<3\sin s\) for \(s=c/3>0\). Therefore the equispaced interior triple is strictly better than every boundary triple. By compactness, it is the unique global minimizer of the energy, up to circular permutation, hence the unique global maximizer of area up to common rotation and permutation.

**4. Exact extremal areas and residual deficit.** Substituting the equal gaps in (4) and then using (2) gives
\[
D_{n,3}=\frac{2w^2}{9\pi}\bigl(3F_n(0)+6F_n(2\pi/3)\bigr)
=w^2\left[\frac{n}{6\cos c}\left(\sin c-2\sin\frac c3\right)-\frac\pi{36}\right].
\]
This is strictly positive: at equal gaps, the \(j=3\) term of the positive series (1) is nonzero. Equivalently,
\[
D_{n,3}=\frac{2w^2}{\pi}\sum_{\substack{j\ge1\\j\equiv3\;(\mathrm{mod}\;6)}}\frac1{j^2(n^2j^2-1)}.
\]
The maximum of \(F_n\) is achieved only at multiples of \(2\pi\) by (3). Hence the deficit in (4) is largest only when every pairwise phase difference vanishes modulo \(2\pi\). Substituting \(F_n(0)=-\pi^2/8+(\pi n/4)\tan c\) yields the stated area minimum.

For the high-order asymptotic, expanding the displayed closed form at \(c=0\) gives
\[
\frac{D_{n,3}}{w^2}=\frac{\pi c^2}{972}+O(c^4)
=\frac{\pi^3}{3888n^2}+O(n^{-4}).
\]
For stability, two derivatives of (2) at \(t=2\pi/3\) give
\[
F_n''(2\pi/3)=\frac{\pi}{4n\cos c}\sin\frac{\pi}{6n}>0.
\]
Taylor's theorem in (4) with \(\eta_1+\eta_2+\eta_3=0\) gives the claimed local quadratic area deficit.

## Verification
Run the bundled `verify.py` with Python 3 and no third-party dependencies. In the included verification run, all **10,692 finite checks passed**. Tests compare the closed kernel against independently summed Fourier series at 31 angles for each of six odd values of \(n\), verify disk deficit and classical-area endpoints, exhaust all pairs of points on a 41-by-41 phase mesh for each chosen \(n\), and independently reconstruct the mean's polygonal boundary using exact piecewise curvature-radius integration before checking area via the shoelace formula. The numerical tests are consistency checks; they do not prove the all-odd-\(n\), all-phase assertion. The latter follows from the derivations (1)–(4) and the strict gap argument above.

## Relationship to prior work
Falcó and Myroshnychenko (2026) classify the least-area constant-width bodies under prescribed odd cyclic or dihedral symmetry, establishing the canonical regular Reuleaux odd-gon and useful Fourier curvature formulas. Their shape minimization is **not** a classification of the area of a Minkowski mean of three independently rotated copies of that shape. Bogosel (2023) develops mixed-area formulas for a Reuleaux body and its *opposite*; that concerns a single special pair of rotations, not a constrained triple.

A published exact rotation-area profile of the Reuleaux **triangle with two summands** evaluates the two-phase kernel and proves monotonicity up to the opposite-body angle. A published Fourier study of randomly rotated Minkowski sums proves expected area, variance, and limit laws for **independent random angles**, not the unique deterministic three-angle optimum. A separate example of two-frequency smooth constant-width ovals shows that monotonicity for two rotations is not universal. These results supply context or standard tools, but their statements do not imply the complete three-phase extremal classification or its nonzero residual disk deficit. Existing regular-polygon union/convex-hull rotation results concern different set operations. Historical priority against older unindexed work on three-point circle energy remains provisional.

## Limitations
The theorem is restricted to three *equally weighted* rotated copies of a single regular odd-\(n\) Reuleaux body. It does not characterize area extrema for four or more copies, arbitrary constant-width ovals, or unequal weights. The local stability expansion is asymptotic near optimizers, not a global quadratic stability inequality. The primary novelty is the triple-phase geometric optimization and exact positive disk deficit; the Fourier area identity, classical Reuleaux area, and two-copy opposite-body disk identity are background results.

## References
1. J. Falcó and S. Myroshnychenko, *Area Minimization Among Group-Invariant Planar Convex Bodies of Constant Width*, arXiv:2608.05125v1, first publicly submitted 2026-08-05. https://arxiv.org/abs/2608.05125.
2. B. Bogosel, *Mixed volumes and the Blaschke–Lebesgue theorem*, arXiv:2311.14618v1, first publicly submitted 2023-11-24. https://arxiv.org/abs/2311.14618.
3. *Exact rotational Minkowski-average area profile of the Reuleaux triangle*, published mathematical finding, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-rotational-minkowski-average-area-profile-of-the-reuleaux--53c190e0340e.
4. *One-sided non-Gaussian area fluctuations of randomly rotated Minkowski sums*, published mathematical finding, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-one-sided-non-gaussian-area-fluctuations-of-randomly-rotated-min--b78353b61adf.
5. *A sharp rotational-area monotonicity threshold for threefold constant-width ovals*, published mathematical finding, 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-sharp-rotational-area-monotonicity-threshold-for-threefold-con--ffbd498fa460.
