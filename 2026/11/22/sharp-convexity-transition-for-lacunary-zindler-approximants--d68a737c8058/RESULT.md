# Sharp convexity transition for lacunary Zindler approximants

## Finding

For the finite Fourier approximants to the fractal Zindler curves introduced by Martinez-Maure and Rochera, there is an exact threshold for convexity at every truncation order. Let \(\beta\ge7\) be an odd integer and choose \(\alpha>\beta\) with \(\beta^2>\alpha(1+3\pi/2)\). For every integer \(n\ge1\), put
\[
h_n(t)=\sum_{k=1}^{n}\alpha^{-k}\sin(\beta^k t),\qquad R_n=\sum_{k=1}^{n}\frac{\beta^{3k}-\beta^k}{\alpha^k}.
\]
With \(u(t)=(\cos t,\sin t)\) and \(r>0\), form
\[
z_{n,r}(t)=h_n(t)u(t)+(h_n'(t)+r)u'(t),\qquad t\in\mathbb R/(2\pi\mathbb Z).
\]
The image of \(z_{n,r}\) is the boundary of a convex planar body **if and only if** \(r\ge R_n\), including equality. It is a smooth, strictly convex Jordan curve throughout this regime. Its Euclidean curvature is positive at every parameter value if \(r>R_n\); at equality it vanishes at exactly the \(\beta\) parameter values
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
Consequently no fixed positive chord length can make all the smooth approximants convex. For \((\alpha,\beta)=(8,7)\), the first two critical radii are exactly \(R_1=42\) and \(R_2=3759/2\).

## Assumptions and scope

The assumptions on \(\alpha,\beta\) are those of the cited fractal construction. The finite-order convexity and flat-point classifications use only \(\alpha>0\) and odd integer \(\beta\ge3\); the growth law above uses the narrower source regime. The parameter \(r\) is the half-length of the chord joining the points with arguments separated by \(\pi\), not a curvature radius. The result concerns finite, smooth approximants, not convexity of the nowhere-differentiable limiting fractal curve.

## Proof

Write \(z=z_{n,r}\) and \(H=h_n+h_n''\). Since \(u''=-u\),
\[
z'=-r u+H u',\qquad z''=-H u+(H'-r)u'.
\]
In particular \(|z'|^2=r^2+H^2>0\), so this is always a regular immersion. Its signed curvature numerator is
\[
K_{n,r}(t):=\det(z',z'')=r^2-rH'(t)+H(t)^2.
\]
Directly from the finite series,
\[
H(t)=-\sum_{k=1}^n\frac{\beta^{2k}-1}{\alpha^k}\sin(\beta^k t),\qquad H'(t)=-\sum_{k=1}^n c_k\cos(\beta^k t).
\]
All \(c_k>0\), and
\[
R_n-H'(t)=\sum_{k=1}^n c_k[1+\cos(\beta^k t)]\ge0.
\]
For \(r\ge R_n\), \(K_{n,r}=r(r-H')+H^2\ge0\), with strict inequality if \(r>R_n\). At \(r=R_n\), a zero requires that every cosine equal \(-1\). The first cosine forces \(t=t_j\), and at each such \(t_j\) every higher cosine equals \(-1\) by oddness of \(\beta\), while all sine terms vanish. These are exactly the \(\beta\) zeros.

To pass from curvature sign to global convexity, note that \(z'\) is the rotation by \(t\) of \((-r,H(t))\). This latter vector stays in the left open half-plane, so the tangent has winding number one. When \(r\ge R_n\), the tangent angle has derivative \(K_{n,r}/|z'|^2\ge0\), positive except at isolated parameters, and strictly increases by \(2\pi\) in one period. Thus, for every unit vector \(v\), the derivative of \(v\cdot z(t)\) changes sign once from positive to negative and once from negative to positive per period. It follows that each supporting direction has exactly one maximizing parameter. Moreover, each parameter is such a maximizer for the clockwise unit normal to its tangent. In particular, distinct parameters cannot give the same point. The convex hull has nonempty interior because the tangent turns through a full revolution. Every boundary point of the hull has a supporting direction, whose maximizing face is the singleton on the curve, and every curve point is a support point. Hence the image is exactly the strictly convex boundary of that hull.

Conversely, at \(t_0=\pi/\beta\), oddness gives \(H(t_0)=0\) and \(H'(t_0)=R_n\). At \(t=0\), \(H(0)=0\) and \(H'(0)=-R_n\). For \(0<r<R_n\) the two curvature numerators have opposite signs:
\[
K_{n,r}(t_0)=r(r-R_n)<0,\qquad K_{n,r}(0)=r(r+R_n)>0.
\]
These signs exclude a convex boundary image without presuming injectivity. Indeed, if the image were a convex boundary, a supporting line at any \(z(t)\) would have to be its tangent line, since the regular curve lies on one side of that line for parameters on both sides of \(t\). Fix an interior point \(b\) of the hypothesized body. The continuous function \(\det(z'(t),b-z(t))\) is never zero and so has constant sign. It follows that the body stays on the same oriented side of the tangent at every parameter. The function \(s\mapsto\det(z'(t),z(t+s)-z(t))\) has constant weak sign in \(s\) matching that side and is zero at \(s=0\). Its second derivative at zero is \(K_{n,r}(t)\), so \(K_{n,r}\) must have one weak sign everywhere, a contradiction.

For the quadratic critical zeros, set \(s=t-t_j\). Taylor expansion gives \(H(t_j+s)=R_n s-(S_n/6)s^3+O(s^5)\) and \(H'(t_j+s)=R_n-(S_n/2)s^2+O(s^4)\). Thus \(K_{n,R_n}(t_j+s)=R_n(R_n+S_n/2)s^2+O(s^4)\). Dividing by \((R_n^2+H^2)^{3/2}\) gives the asserted curvature coefficient.

To see that the paired chords halve area in the convex regime, oddness implies \(H(t+\pi)=-H(t)\), and likewise \(h_n\) and \(h_n'\) change sign. Consequently
\[
z(t)-z(t+\pi)=2r u'(t),\qquad z'(t)+z'(t+\pi)=2H(t)u'(t).
\]
The first identity gives length \(2r\) for all \(r>0\), with or without convexity. In the convex regime let \(A(t)\) be the signed area bounded by the arc from \(z(t)\) to \(z(t+\pi)\) and the closing chord. By the oriented area formula and differentiation,
\[
2A'(t)=\det\!\big(z(t+\pi)-z(t),\,z'(t+\pi)+z'(t)\big)=0.
\]
The complementary arc and chord give \(A(t+\pi)\); their two areas add to the area of the body. Since \(A\) is constant, each chord bisects area.

Finally, with \(q=\beta^3/\alpha>1\) and \(p=\beta/\alpha<1\), the exact identity
\[
R_n=\frac{q(q^n-1)}{q-1}-\frac{p(1-p^n)}{1-p}
\]
gives the asymptotics. The radius is strictly increasing because each successive coefficient is positive. The two example values follow by direct rational substitution.

## Verification

The analytic proof addresses every truncation and all parameters in scope. The companion `checker.py` in the source package compares independently formed tangent and acceleration determinants, checks arithmetic and phase identities, and samples the curvature inequality. It requires only Python's standard library. These finite diagnostics are supplementary; they do not establish the global classification.

## Relationship to prior work

The lacunary functions and Zindler offset construction are due to Martinez-Maure and Rochera. The question addressed here is the exact convexity threshold of their finite truncations, distinct from embedding or halving-chord geometry of the limiting construction. Grüne discusses the general Zindler convexity criterion and a rolling-circle example. The general curvature criterion and the method of testing convexity are not claimed as new. The particular features used here are simultaneous attainment of the sharp curvature bound across the retained modes, the exact orders of the critical flat points, and the growth of the least convexity-preserving chord length.

## Limitations

The result does not characterize embedding below the convexity threshold, the shape of nonconvex examples, or the convex hull of the limit. The comparison is not a historical-priority certification. In particular, full-text overlap with the related Rochera works below was not resolved.

## References

- Y. Martinez-Maure and D. Rochera, *Fractal solutions to the two-dimensional floating body problem*, arXiv:2611.11309v1, §§1–3 and formula (2): https://arxiv.org/html/2611.11309v1
- A. Grüne, *Geometric Dilation and Halving Distance*, University of Bonn dissertation (2006/2007), §3.2.3: https://www.academia.edu/64402939/Geometric_dilation_and_halving_distance
- D. Rochera, *Offsets and front tire tracks to projective hedgehogs*, Computer Aided Geometric Design 97 (2022), 102135, DOI: 10.1016/j.cagd.2022.102135.
- D. Rochera, *Algebraic equations for constant width curves and Zindler curves*, Journal of Symbolic Computation 113 (2022), 139–147, DOI: 10.1016/j.jsc.2022.03.001.
