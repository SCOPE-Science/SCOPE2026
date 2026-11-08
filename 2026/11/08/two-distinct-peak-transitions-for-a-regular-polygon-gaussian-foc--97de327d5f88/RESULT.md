# Two distinct peak transitions for a regular-polygon Gaussian Fock intensity

## Finding
For each integer \(n\ge3\), the Gaussian-weighted polynomial intensity
\[
H_{n,a}(z)=\exp(-|z|^2)|z^n-a|^2,\qquad z\in\mathbb C,\quad a>0,
\]
exhibits **two different sharp transitions**: a switch in the global maximizing locations, followed at a larger parameter by annihilation of a ring of local maxima with a ring of saddles. We classify every critical point, including the non-Morse transition points, for every \(n\ge3\) and every \(a>0\).

Put
\[
A_n=2(n-2)^{(n-2)/2}.
\]
For the uniquely defined \(s_n\in(n-2,n)\) satisfying
\[
n\exp(-s_n/2)=n-s_n,
\]
put \(G_n=(n-s_n)s_n^{(n-2)/2}\). Then \(0<G_n<A_n\). When \(0<a<G_n\), the \(n\) points on the outer negative-power critical ring are the only global maxima. At \(a=G_n\), they tie with the origin. For \(a>G_n\), only the origin is a global maximum. The outer ring ceases to be a local maximum ring only at \(a=A_n\), through an \(n\)-fold simultaneous saddle-node collision.

## Assumptions and scope
The polynomial is \(f(z)=z^n-a\) with real \(a>0\), and the Gaussian normalization is exactly \(e^{-|z|^2}\). Rotating or multiplying \(f\) by a nonzero complex scalar only rotates the portrait or rescales its values, so real positive \(a\) fixes these symmetries. Critical points mean real stationary points of the smooth function \(H_{n,a}:\mathbb R^2\to\mathbb R\). A nondegenerate maximum/minimum/saddle is classified by the real Hessian. Critical points where the Hessian is singular are stated separately. All maxima referred to as global are over the whole complex plane.

For \(a>0\), exactly \(n\) simple polynomial zeros \(a^{1/n}e^{2\pi ik/n}\), \(0\le k<n\), are nondegenerate global minima. The origin is an additional nondegenerate local maximum. On each positive-power ray \(\arg z=2\pi k/n\) there is exactly one further critical point at the unique \(r>\sqrt n\) satisfying
\[
a=(r^2-n)r^{n-2},
\]
and it is a nondegenerate saddle. On each negative-power ray \(\arg z=(2k+1)\pi/n\), there are exactly two nonzero critical radii if \(0<a<A_n\): one \(0<r_-<\sqrt{n-2}\), a nondegenerate saddle, and another \(\sqrt{n-2}<r_+<\sqrt n\), a nondegenerate local maximum. For \(a=A_n\), each negative ray has exactly one degenerate stationary point at \(r=\sqrt{n-2}\), not a nondegenerate maximum. For \(a>A_n\), none exist. No off-ray critical points occur.

## Proof
**Exact stationary-point constraint.** Outside polynomial zeros and the origin, the stationarity condition for \(\log H\) is
\[
\frac{n z^{n-1}}{z^n-a}=\overline z.
\]
Multiplying by \(z(z^n-a)\) gives
\[
(r^2-n)z^n=ar^2,\qquad r=|z|>0.
\]
Thus \(z^n\) is real and nonzero: every nonzero non-minimum stationary point is on one of the \(2n\) stated rays. At a zero of \(f\), its simple complex derivative gives \(H(z)=e^{-|z_0|^2}|f'(z_0)|^2|z-z_0|^2+O(|z-z_0|^3)\), so the zero is a nondegenerate minimum. As \(n\ge3\), near zero \(H(z)=a^2-a^2|z|^2+O(|z|^3)\), so the origin is a nondegenerate local maximum.

**Radial equations and Hessian signs.** In polar coordinates,
\[
H(r,\theta)=e^{-r^2}[r^{2n}+a^2-2ar^n\cos(n\theta)].
\]
At each ray, the mixed radial-angular second derivative vanishes and the angular curvature is \(2an^2r^ne^{-r^2}\cos(n\theta)\). On positive-power rays the angular curvature is positive, and away from the zeros the radial profile is \(e^{-r^2}(r^n-a)^2\). Its only non-minimum positive stationary radius solves \(a=(r^2-n)r^{n-2}\), which is strictly increasing in \(r>\sqrt n\) and therefore has exactly one solution. The radial profile has a strict local maximum there, so the point is a saddle.

On negative-power rays the angular curvature is negative; the radial profile is \(e^{-r^2}(r^n+a)^2\). Its stationary radii satisfy \(a=g_n(r):=(n-r^2)r^{n-2}\) with \(0<r<\sqrt n\). Its derivative has the sign of \(n-2-r^2\); therefore the unique maximum of \(g_n\) is \(g_n(\sqrt{n-2})=A_n\). Below this level are two roots, at the level one double root, above it no roots. The radial derivative of the profile changes negative-to-positive at the smaller root (radial minimum and angular maximum: saddle) and positive-to-negative at the larger root (maximum in both directions). At equality the radial derivative has a double zero while the angular second derivative stays negative: the critical point is degenerate. This proves the full local portrait.

**Sharp global switch.** As \(r\to\infty\), \(H(r,\theta)\to0\); thus its global maxima occur among the local maxima just listed. At the outer negative-ray root, set \(s=r_+^2\in(n-2,n)\). The radial equation gives \(a=(n-s)s^{(n-2)/2}\) and hence
\[
H(r_+,(2k+1)\pi/n)=n^2s^{n-2}e^{-s},\qquad H(0)=a^2=(n-s)^2s^{n-2}.
\]
Their values agree if and only if \(ne^{-s/2}=n-s\). The ratio \(ne^{-s/2}/(n-s)\) has logarithmic derivative \(-1/2+1/(n-s)>0\) on \((n-2,n)\), tends to infinity at the right endpoint, and is strictly below one at the left endpoint: \(ne^{-(n-2)/2}<2\) for \(n>2\), since \(\log(n/2)<(n-2)/2\). Hence a unique \(s_n\in(n-2,n)\) exists. Since \(g_n(r)\) decreases strictly on the outer branch, its corresponding parameter \(G_n\) lies strictly between \(0\) and \(A_n\). The outer ring is globally maximizing below \(G_n\); at equality it ties; above it the origin dominates. At \(a\ge A_n\) the only local maximum is the origin, completing the classification.

## Verification
All identities are elementary and can be checked by differentiating the displayed polar expression. As illustrative numerical evaluations only, \(n=3\) gives \(A_3=2\) and \(G_3\approx1.65492444358\); \(n=4\) gives \(A_4=4\) and \(G_4\approx2.59044095157\). These values do not establish the all-order result, which follows from the monotonicity and Hessian arguments above. No random-model averaging or limiting statement is used.

## Relationship to prior work
The 2022 work of Abreu on critical points of Gaussian spectrograms develops general stationary-point and saddle/maximum methods, primarily for random Gaussian entire functions. The 2019 stellar representation of Chabaud, Markham and Grosshans relates polynomial Bargmann functions and their Husimi zeros to non-Gaussian states. The exact two-threshold portrait here concerns one deterministic, symmetry-constrained entire polynomial and is not claimed to follow from those statistical or zero-representation statements. It is distinct from phase portraits for two oppositely displaced coherent-state superpositions, whose entire functions involve hyperbolic cosine rather than a binomial polynomial.

## Limitations
This is a finite-degree deterministic result for \(n\ge3\) and \(a>0\); the boundary cases \(n=1,2\) and \(a=0\) exhibit different degeneracies and are not included. The result does not characterize arbitrary Fock polynomials, perturbations away from regular polygon zeros, or random-Gaussian ensemble averages. While comparison with selected published literature found no direct equivalent, a specialized earlier phase-portrait computation cannot be ruled out; historical priority has not been independently certified.

## References
1. L. D. Abreu, *Local maxima of white noise spectrograms and Gaussian entire functions*, arXiv:2210.06721v1 (first posted 2022-10-13); Journal of Fourier Analysis and Applications (2022/2023), DOI 10.1007/s00041-022-09979-7. https://arxiv.org/abs/2210.06721
2. U. Chabaud, D. Markham, F. Grosshans, *Stellar representation of non-Gaussian quantum states*, arXiv:1907.11009v1 (first posted 2019-07-25), subsequently Phys. Rev. Lett. 124 (2020), 063605. https://arxiv.org/abs/1907.11009
