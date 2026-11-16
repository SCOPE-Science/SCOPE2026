# Five-circle bifurcation and conserved zero charge for two-mode first-Hermite spectrograms

## Finding

Let \(m>k\ge 1\) be integers, \(d=m-k\), and \(c>0\). Take normalized Hermite functions \(h_j\), with the standard Bargmann convention \(\mathcal B h_j(z)=\pi^{j/2}z^j/\sqrt{j!}\), and the finite-energy signal
\[
f_{m,k,c}=\sqrt{m!}\,h_m+c\sqrt{k!}\,h_k.
\]
For the first-Hermite analysis window, the zero set of the short-time Fourier transform (STFT), in the dimensionless Bargmann coordinate \(w=\sqrt\pi z\), is exactly the zero set of
\[
G_{m,k,c}(w)=(\partial_w-\overline w)(w^m+cw^k)
=w^{k-1}\bigl[(m-|w|^2)w^d+c(k-|w|^2)\bigr].
\]
The nonzero zeros lie on three or five concentric regular \(d\)-gons, depending sharply on \(m,k,c\). All nonzero circles and all charges are completely classified below.

Define, for real \(s>0\), \(s\ne k,m\),
\[
R_{m,k}(s)=s^{d/2}\frac{|m-s|}{|k-s|}.
\]
For each positive solution of \(R_{m,k}(s)=c\), there are exactly \(d\) zeros at \(|w|=\sqrt s\), with phases \(\arg w=(2j+1)\pi/d\) if \(s<k\) or \(s>m\), and \(\arg w=2\pi j/d\) if \(k<s<m\), where \(j=0,\ldots,d-1\). There are no other nonzero zeros. The origin is a zero precisely when \(k\ge2\), with local index \(k-1\).

Always, exactly one nonzero zero-circle parameter lies in \((0,k)\), and exactly one lies in \((m,\infty)\). The interval \((k,m)\) has one, two, or three distinct zero-circle parameters as follows. If
\[
d\le 2+\sqrt{8k},
\]
then it has exactly one for every \(c>0\). At strict inequality all nonzero zeros are simple; at equality there is one special amplitude with \(d\) isolated zero points having zero Jacobian (but no change in zero count), detailed below. If \(d>2+\sqrt{8k}\), let
\[
s_\pm=\frac{m+k-2\pm\sqrt{(d-2)^2-8k}}{2},\qquad
c_-=R_{m,k}(s_-),\qquad c_+=R_{m,k}(s_+).
\]
Then \(k<s_-<s_+<m\), \(0<c_-<c_+\), and the full nonzero-zero count is
\[
\#\{G_{m,k,c}=0,\ w\ne0\}=\begin{cases}
3d,&0<c<c_-\text{ or }c>c_+,\\
4d,&c=c_-\text{ or }c=c_+,\\
5d,&c_-<c<c_+.
\end{cases}
\]
At either endpoint there are exactly \(d\) nonzero degenerate zeros, one on each of the rays of the colliding regular polygons. They are nondegenerate saddle-node folds. Thus the total number of **distinct** complex zeros, including the origin if \(k\ge2\), is the displayed number plus \(\mathbf 1_{\{k\ge2\}}\).

At a simple nonzero zero with squared radius \(s\), the local mapping index (Jacobian charge) is \(+1\) if \(R'_{m,k}(s)>0\) and \(-1\) if \(R'_{m,k}(s)<0\). The inner and outer polygons have positive charges; the sole intermediate polygon has negative charges in the three-circle phase. In the five-circle phase, the successive charges, from the smallest radius outward, are
\[
(+1,-1,+1,-1,+1).
\]
Every fold creates or annihilates one positive and one negative regular \(d\)-gon. For all noncritical parameters the sum of the local indices of all zeros, counting the origin with index \(k-1\), equals **exactly** \(m-1\).

A separate **cubic-contact resonance** occurs at equality \(d=2+\sqrt{8k}\), which is possible for integers exactly when
\[
(k,m)=(2t^2,2(t+1)^2),\qquad t=1,2,\ldots .
\]
Put \(s_*=2t(t+1)\) and \(c_*=[2t(t+1)]^{2t+1}(t+1)/t\). At \(c=c_*\), the unique middle polygon consists of \(d\) isolated **Jacobian-degenerate** zeros. The radial crossing has cubic (rather than quadratic) contact, and no polygon pair is created or destroyed: there are still precisely \(3d\) nonzero distinct zeros. Each degenerate middle point has local index \(-1\), so the total signed-index law remains \(m-1\). For \(c\ne c_*\) all nonzero zeros in this equality regime are simple.

The first possible five-circle phase occurs at \((m,k)=(6,1)\), with \(s_-=2\), \(s_+=3\), and explicit endpoints
\[
c_-=2^{9/2},\qquad c_+=3^{7/2}/2.
\]
Thus this smallest example has 15, 20, or 25 distinct nonzero zeros according as the amplitude is outside, on, or inside the two critical endpoints.

## Assumptions and scope

All quantifiers apply to **every** integer pair \(m>k\ge1\) and **every** real \(c>0\). No large-degree approximation or genericity assumption is made. The STFT convention is
\[
V_gf(u,v)=\int_{\mathbb R}f(t)\overline{g(t-u)}e^{-2\pi i vt}\,dt,
\]
with normalized Gaussian and Hermite functions; replacing the STFT by its standard phase-conjugate Bargmann form does not change its zeros or charge signs under the stated orientation-preserving coordinate. The first-Hermite transform is, up to a nonvanishing scalar-Gaussian factor, the true polyanalytic Bargmann transform \((\partial_w-\overline w)F(w)\). The normalization of the physical superposition is chosen to give \(F(w)=w^m+cw^k\) exactly. The charge is \(\operatorname{sgn}(|\partial_wG|^2-|\partial_{\overline w}G|^2)\) at a simple zero, and the local index at an isolated multiple zero is its topological winding number.

The exceptional parameter \(c=0\) is **excluded**: the polynomial then has a whole circle of zeros, so neither finite-zero count nor the fold description extends to that endpoint. The charge statement at folds asserts only the behavior of nearby simple zeros; it does not assign a \(\pm1\) charge to the degenerate zero itself. At \(k\ge3\) the origin is an isolated higher-order zero (not a simple zero), with local index \(k-1\); for \(k=2\) it is simple and positively charged. At the resonant parameter \(c=c_*\) on the equality surface, the \(d\) intermediate zeros are also Jacobian-degenerate but isolated and have index \(-1\), not a simple-zero charge.

## Proof

**1. Reduction to one radial equation.** Under the Bargmann normalization, \(\mathcal Bf_{m,k,c}(w/\sqrt\pi)=w^m+cw^k\). The first Hermite raising operator yields \(G=(\partial_w-\overline w)F\). Writing \(s=|w|^2\), for \(w\ne0\) the equation is
\[
(m-s)w^d+c(k-s)=0.
\]
In particular neither \(s=k\) nor \(s=m\) is possible. Absolute values give \(R_{m,k}(s)=c\). Conversely, for each such \(s\), the argument of \(w^d\) must equal \(\pi\) on \((0,k)\) and \((m,\infty)\), and zero on \((k,m)\); the displayed regular polygons follow. The leading term at the origin is \(ckw^{k-1}\), which gives the stated origin index.

**2. Exact monotonicity and the bifurcation discriminant.** For \(0<s<k\), differentiation gives
\[
\frac{d}{ds}\log R_{m,k}(s)=\frac d{2s}+\frac d{(k-s)(m-s)}>0.
\]
Here \(R\) increases from zero to infinity. For \(s>m\),
\[
\frac{d}{ds}\log R_{m,k}(s)=\frac d{2s}+\frac d{(s-m)(s-k)}>0,
\]
and \(R\) again increases from zero to infinity. Hence each outside interval contains exactly one radius for each \(c>0\).

For \(k<s<m\),
\[
\frac{d}{ds}\log R_{m,k}(s)
=\frac{d\bigl[(m-s)(s-k)-2s\bigr]}{2s(m-s)(s-k)}.
\]
The numerator is \(dP(s)\) with
\[
P(s)=-s^2+(m+k-2)s-mk.
\]
Since \(P(k)=-2k<0\) and \(P(m)=-2m<0\), positive derivative occurs inside \((k,m)\) precisely when \(P\) has two interior real roots. Its discriminant equals \((d-2)^2-8k\). Since \(d\ge1\), both interior roots exist exactly when \(d>2+\sqrt{8k}\). In that case they are \(s_-<s_+\): the function \(R\) decreases from infinity to its strict minimum \(c_-\), rises to its strict maximum \(c_+\), and then decreases to zero. Horizontal lines therefore have respectively one, two (with a tangency), or three distinct intersections in \((k,m)\), as claimed. At equality of the discriminant the derivative has one double root but never changes sign; \(R\) is strictly decreasing, so the zero-circle number remains three. The integer solutions of \((d-2)^2=8k\) with \(d\ge1,k\ge1\) are precisely \(d=4t+2,k=2t^2,m=2(t+1)^2\), with \(t\ge1\). At \(s_*=2t(t+1)\), one has \(R(s_*)=c_*\) as above, and
\[
\frac{d}{ds}\log R(s)=-\frac{d(s-s_*)^2}{2s(m-s)(s-k)}.
\]
Consequently \(R(s)-c_*=-c_*d(s-s_*)^3/[6s_*(m-s_*)(s_*-k)]+O((s-s_*)^4)\). This is an isolated cubic crossing, with the same orientation reversal on both sides, not a fold. Its local topological index is \(-1\), established by the monotone cubic normal form and nonzero angular derivative.

**3. Jacobian and topological charge.** The nonzero factor \(w^{k-1}\) does not alter the sign of the Jacobian at a zero. Put \(w=re^{i\phi}\), \(a(r)=(m-r^2)r^d\) and \(b(r)=c(k-r^2)\); the residual factor is \(U=a(r)e^{id\phi}+b(r)\). At a zero, the angular factor is \(\pm1\), and the polar Jacobian identity gives
\[
J_U=\frac1r\operatorname{Im}\bigl(\overline{U_r}U_\phi\bigr)
=\frac d{2r}\frac{d}{dr}(a(r)^2-b(r)^2).
\]
Since \(a^2-b^2=(s-k)^2(R_{m,k}(s)^2-c^2)\), evaluation at \(R(s)=c\) yields the exact nonzero-zero Jacobian
\[
J_G=2dc\,s^{k-1}(s-k)^2 R'_{m,k}(s).
\]
Thus its sign is the sign of \(R'\). The three-circle signs are \((+,-,+)\), and the five-circle signs are \((+,-,+,-,+)\). In the cubic resonance the middle polygon is degenerate only at \(c=c_*\), with local index \(-1\) rather than a nonzero Jacobian charge. On any noncritical amplitude the signed sum of the polygons is \(d\); adding the origin's index \(k-1\) gives \(m-1\), which also agrees with the leading angular winding of \(G\) on sufficiently large circles.

**4. Fold nondegeneracy and separation scale.** At \(c=c_-\) or \(c=c_+\), the colliding radius is a strict extremum of \(R\), so \(R'=0\) and \(R''\ne0\); the latter follows from the simple roots of \(P\). At the corresponding zero \(U_\phi\ne0\), while the radial first derivative vanishes and the radial second derivative is nonzero. Thus the rank-one zero is a transverse saddle-node fold. The nearby squared radii satisfy
\[
s=s_*\pm\sqrt{\frac{2|c-c_*|}{|R''_{m,k}(s_*)|}}+O(|c-c_*|)
\]
on the side where two branches exist. The two branches have opposite charges, as proved above.

**5. Sharp first occurrence.** The condition \(d>2+\sqrt{8k}\) implies \(d\ge5\) for \(k\ge1\); the minimal possible \(m=k+d\) is therefore 6, attained only for \(k=1,d=5\). In that case direct substitution in the formulas gives \(s_-=2\), \(s_+=3\) and the displayed exact thresholds.

## Verification

The standalone program `CHECK.py` uses only the Python standard library. Run `python CHECK.py` after extracting this package. It brackets the radial solutions on all monotonicity intervals, constructs all regular-polygon roots, directly evaluates the polyanalytic expression and real Jacobian, verifies charge patterns and total index, and tests the exact first exceptional pair. Its saved-package replay passed 4,126 finite assertions. These checks are **not** an exhaustive or infinite-domain certificate; the proof of the infinite family is the analytical argument above. In particular, numerical checks are not used to prove the no-other-zeros assertion or the unique-fold classification.

## Relationship to prior work

The first-Hermite/true-polyanalytic Bargmann representation and the definition of positive/negative charged zeros are classical and are used explicitly by Bellourak, Meignen, Polisano and Nahon (2026, Sections 2–4). Their principal theorems concern Gaussian white-noise spectrogram-zero intensities and pair correlations; they do not provide a deterministic global root census for arbitrary two-Hermite input-mode superpositions.

Gröchenig, Jaming and Malinnikova (2018 preprint, Section 6, especially Proposition 6.4) prove that mismatched finite Hermite modes force the existence of an STFT zero. Their result does not count all zeros, classify charge signs, or determine the five-ring threshold. Abreu and Shirai (2026) study randomized Landau-level zero correlations and averaged fields, not a finite deterministic two-mode bifurcation. Known formulas for complex Hermite polynomials imply the starting expression, but the complete all-index fold/charge diagram requires the radial discriminant analysis above.

The comparison includes relevant indexed results for a first-Hermite **two-tone Fourier signal**, whose spatial periodic cylinder and exponential Bargmann input differ from the present **two Hermite-input modes**; one count does not imply the other. Indexed results for **Gaussian-window** vacuum–Hermite spectrogram intensity maxima concern a holomorphic analysis window and maxima, rather than charged zeros of the first-Hermite transform. This result claims no novelty for the basic Bargmann transform formula, polyanalytic Jacobian formula, or general topological-degree principle.

## Limitations

The classification applies to exactly two **positive-index Hermite input modes** and the first-Hermite analysis window, with a real positive relative coefficient. The phase of an arbitrary nonzero complex relative coefficient can be removed by a rotation and does not change zero counts; it rotates the zero polygons. It does not address three or more input modes, higher-order Hermite analysis windows, random-input laws, stability under generic nonsymmetric perturbations, or zeros as \(c\to0\). The fold statement is local and does not imply all spectrogram intensity critical points are classified. Older special-function or signal-processing literature may contain an equivalent two-mode phase diagram under different terminology; independent priority review is not performed.

## References

1. C. Bellourak, S. Meignen, K. Polisano and M. Nahon, *Zeros of the Spectrogram of White Noise with Hermite Windows*, arXiv:2610.13531 (first public 2026-10-09), Sections 2–4 and 6. https://arxiv.org/abs/2610.13531
2. K. Gröchenig, P. Jaming and E. Malinnikova, *Zeros of the Wigner Distribution and the Short-Time Fourier Transform*, arXiv:1811.03937 (2018), Section 6. https://arxiv.org/html/1811.03937v1
3. L. D. Abreu and T. Shirai, *Zero correlations and averaged fields of orthonormal Gaussian functions*, arXiv:2605.17296 (first public 2026-05-17), Sections 1 and 8. https://arxiv.org/abs/2605.17296
4. M. E. H. Ismail, *Analytic properties of complex Hermite polynomials*, Trans. Amer. Math. Soc. **368** (2016), 1189–1210, DOI:10.1090/tran/6358. (Background complex-Hermite formulas; only abstract available in this review.)
