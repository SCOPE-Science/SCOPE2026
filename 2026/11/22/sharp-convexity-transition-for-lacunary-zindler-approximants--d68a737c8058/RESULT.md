# Sharp convexity transition for lacunary Zindler approximants

## Finding

For the finite Fourier approximants to the fractal Zindler curves introduced by Martinez-Maure and Rochera, there is an exact threshold for convexity at every truncation order. Let \(\beta\ge7\) be odd and choose \(\alpha>\beta\) with \(\beta^2>\alpha(1+3\pi/2)\). For every integer \(n\ge1\), put
\[
h_n(t)=\sum_{k=1}^{n}\alpha^{-k}\sin(\beta^k t),\qquad R_n=\sum_{k=1}^{n}\frac{\beta^{3k}-\beta^k}{\alpha^k}.
\]
With \(u(t)=(\cos t,\sin t)\) and \(r>0\), form
\[
z_{n,r}(t)=h_n(t)u(t)+(h_n'(t)+r)u'(t),\qquad t\in\mathbb R/(2\pi\mathbb Z).
\]
Then the image of \(z_{n,r}\) is the boundary of a convex planar body **if and only if** \(r\ge R_n\). It is a smooth, strictly convex Jordan curve throughout this regime. Its Euclidean curvature is positive at every parameter value if \(r>R_n\); at equality it vanishes at exactly the \(\beta\) parameter values
\[
t_j=(2j+1)\pi/\beta\pmod{2\pi},\qquad j=0,\dots,\beta-1,
\]
and those zeros are quadratic in the parameter. Thus the minimum halving-chord length compatible with convexity is exactly \(2R_n\).

More precisely, writing \(c_k=(\beta^{3k}-\beta^k)/\alpha^k\) and \(S_n=\sum_{k=1}^{n}c_k\beta^{2k}\), the signed curvature at the critical radius has the local expansion
\[
\kappa_{n,R_n}(t_j+s)=\frac{R_n+S_n/2}{R_n^2}s^2+O(s^4),\qquad s\to0.
\]
Set \(q=\beta^3/\alpha>1\). The sharp radius has the growth law
\[
R_n=\frac{q^{n+1}}{q-1}+O(1),\qquad \frac{R_{n+1}}{R_n}\longrightarrow q.
\]
Consequently no fixed positive chord length can make all the smooth approximants convex. For the paper's concrete parameters \((\alpha,\beta)=(8,7)\), the first two critical radii are exactly \(R_1=42\) and \(R_2=3759/2\).

## Assumptions and scope

The assumptions on \(\alpha,\beta\) are those in the cited fractal construction. The proof of the finite-order convexity classification uses only that \(\alpha>0\) and \(\beta\ge3\) is an odd integer; the narrower source regime is retained to describe its actual approximants. The parameter \(r\) is the half-length of the chord joining the two points with arguments separated by \(\pi\), not a curvature radius. The claim concerns **finite, smooth approximants**, not convexity of the nowhere-differentiable limiting fractal curve.

For this construction, \(h_n(t+\pi)=-h_n(t)\), and the same holds for \(h_n'\). It follows directly that
\[
z_{n,r}(t)-z_{n,r}(t+\pi)=2r\,u'(t).
\]
Thus every such paired chord has length \(2r\), whether or not the curve is embedded or convex. In the convex regime these are genuine halving chords of the resulting convex body.

## Proof

Write \(H=h_n+h_n''\). Since \(u'=(-\sin t,\cos t)\), \(u''=-u\), differentiation of the prescribed parameterization gives
\[
z_{n,r}'=-r u+H u',\qquad z_{n,r}''=-H u+(H'-r)u'.
\]
In particular \(|z_{n,r}'|^2=r^2+H^2>0\), so this is always a regular immersion. Its signed curvature numerator is
\[
K_{n,r}(t):=\det(z_{n,r}',z_{n,r}'')=r^2-rH'(t)+H(t)^2.
\]
Directly from the finite series,
\[
H(t)=-\sum_{k=1}^n\frac{\beta^{2k}-1}{\alpha^k}\sin(\beta^k t),\qquad H'(t)=-\sum_{k=1}^n c_k\cos(\beta^k t).
\]
Since every \(c_k>0\),
\[
R_n-H'(t)=\sum_{k=1}^n c_k[1+\cos(\beta^k t)]\ge0.
\]
If \(r\ge R_n\), then \(K_{n,r}=r(r-H')+H^2\ge0\); the inequality is everywhere strict for \(r>R_n\). At \(r=R_n\), equality is possible exactly when every cosine in the last displayed sum equals \(-1\). Because \(\beta\) is odd, that is equivalent to \(t=(2j+1)\pi/\beta\), giving exactly \(\beta\) distinct values modulo \(2\pi\). At each such value all sine terms vanish, so \(H=0\), as required.

To pass from curvature sign to global convexity without assuming injectivity, note that the tangent vector is the rotation by \(t\) of \((-r,H(t))\). This latter vector lies strictly in the left open half-plane, so it has winding number zero. Thus the tangent vector \(z_{n,r}'\) has winding number one for every \(r>0\). Whenever \(K_{n,r}\ge0\), its tangent direction turns monotonically through exactly \(2\pi\). In the present family the zeros of \(K_{n,r}\) are isolated. Consequently every normal direction has a unique global supporting point on the parametrized curve: the scalar projection of the curve onto that direction increases to its unique maximum and then decreases, as follows from the monotonically rotating tangent. The curve is therefore a simple strictly convex closed boundary. Positive curvature holds at every point if \(r>R_n\).

Conversely, at \(t_0=\pi/\beta\), oddness of \(\beta\) gives \(\cos(\beta^k t_0)=-1\) and \(\sin(\beta^k t_0)=0\). Hence \(H(t_0)=0\), \(H'(t_0)=R_n\), and
\[
K_{n,r}(t_0)=r(r-R_n)<0\quad\text{when }0<r<R_n.
\]
A regular parametrization of a convex Jordan boundary with tangent winding number one must have nonnegative signed curvature; therefore this negative value rules out convexity even if other parameter values exhibit positive curvature.

For the quadratic critical zeros, set \(s=t-t_j\). Taylor expansion at any critical parameter gives \(H(t_j+s)=R_n s-(S_n/6)s^3+O(s^5)\) and \(H'(t_j+s)=R_n-(S_n/2)s^2+O(s^4)\). Thus \(K_{n,R_n}(t_j+s)=R_n(R_n+S_n/2)s^2+O(s^4)\). Dividing by \(|z_{n,R_n}'|^3=(R_n^2+H^2)^{3/2}\) yields the claimed curvature coefficient.

Finally, with \(q=\beta^3/\alpha>1\) and \(p=\beta/\alpha<1\), the exact geometric-series identity
\[
R_n=\frac{q(q^n-1)}{q-1}-\frac{p(1-p^n)}{1-p}
\]
implies the asymptotics and strict growth. The two exact sample values follow by direct rational substitution.

## Verification

The complete symbolic argument above is the infinite-order proof. The companion standalone `checker.py`, requiring only Python's standard library, independently constructs the differentiated tangent and curvature vectors, compares the determinant with the closed formula, checks positive coefficients and odd-parity phase alignment, verifies rational identities for several truncations, and samples the curvature inequality on three admissible parameter pairs. It does not establish the universal statements through sampling. Run `python3 checker.py` in the same directory as this file.

## Relationship to prior work

Martinez-Maure and Rochera (2026) introduce precisely these lacunary support-function truncations and Zindler offset parametrizations; they prove the properties of the fractal limit, including the fixed-length halving-chord geometry and an explicit sufficient condition for embeddedness. Their theorem does not state an exact convexity threshold for the finite truncations. Ansgar Grüne's dissertation on halving distance recounts Zindler's classical general curvature criterion and derives an exact convexity threshold for a different rolling-circle example. We therefore do not claim the general curvature criterion or the method of testing a Zindler curve for convexity as new. The contribution here is the exact all-order threshold, its attained phase structure, and its exponential asymptotics for the source's particular lacunary approximants.

## Limitations

No claim is made that general Zindler-curve convexity criteria are new or that the resulting body is unique among curves of a given chord length. The sharp law addresses a specific family of finite-frequency curves. It does not determine the embedding threshold below convexity, the exact global geometry of nonconvex examples, or the convex hull of the fractal limit. Pre-2026 publications on projective hedgehog offsets and Zindler curves may contain related criteria; two plausible 2022 journal texts were not retrievable in the available session. This is a self-review, not independent validation.

## References

- Y. Martinez-Maure and D. Rochera, *Fractal solutions to the two-dimensional floating body problem*, arXiv:2611.11309v1 (publicly submitted 8 November 2026), especially Sections 1–3 and formula (2): https://arxiv.org/html/2611.11309v1
- A. Grüne, *Geometric Dilation and Halving Distance*, University of Bonn dissertation (2006/2007), Section 3.2.3 on the classical convexity criterion: https://www.academia.edu/64402939/Geometric_dilation_and_halving_distance
- D. Rochera, *Offsets and front tire tracks to projective hedgehogs*, Computer Aided Geometric Design 97 (2022), 102135, DOI: 10.1016/j.cagd.2022.102135. Related title and abstract reviewed; full text not available here.
- D. Rochera, *Algebraic equations for constant width curves and Zindler curves*, Journal of Symbolic Computation 113 (2022), 139–147, DOI: 10.1016/j.jsc.2022.03.001. Related title and abstract reviewed; full text not available here.
