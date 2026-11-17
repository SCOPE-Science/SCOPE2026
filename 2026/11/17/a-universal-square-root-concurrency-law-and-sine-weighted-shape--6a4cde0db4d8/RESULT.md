# A universal square-root concurrency law and sine-weighted shape distribution for random cevians

## Finding
Let \(ABC\) be any nondegenerate Euclidean triangle. Independently choose \(D\in BC\), \(E\in CA\), and \(F\in AB\), each uniformly in arclength on its specified side. The cevians \(AD,BE,CF\) bound the (possibly degenerate) Routh triangle \(PQR\), with \(P=AD\cap BE\), \(Q=BE\cap CF\), and \(R=CF\cap AD\). Write its normalized area as \(Z=[PQR]/[ABC]\). Then
\[
\Pr\{0<Z<\varepsilon\}=\frac{3\pi}{4}\sqrt{\varepsilon}+o(\sqrt{\varepsilon})\quad (\varepsilon\downarrow0).
\]
The constant is independent of the Euclidean shape of \(ABC\). Moreover, the following explicitly marked conditional law holds jointly in **total variation**, not just weak convergence.

Let \((a,b,c)\), \(a,b,c>0\), \(a+b+c=1\), be the barycentric coordinates of \(P\) relative to \(ABC\). The three positive numbers \(a+b,b+c,c+a\) form the side lengths of an auxiliary triangle with opposite angles \((\alpha,\beta,\gamma)\), where \(\gamma=\pi-\alpha-\beta\). Orient the Ceva defect by
\[
T=2uvw-uv-uw+u-vw+v+w-1,
\]
where \(u=CD/BC\), \(v=AE/AC\), and \(w=BF/AB\) are independent uniforms in \((0,1)\). Under the condition \(0<Z<\varepsilon\), the joint law of
\[
\left(\alpha,\beta,\operatorname{sgn}(T)\sqrt{Z/\varepsilon}\right)
\]
converges in total variation to the probability measure on \(\{\alpha,\beta>0,\alpha+\beta<\pi\}\times(-1,1)\) having density
\[
\frac{\sin\alpha+\sin\beta+\sin(\alpha+\beta)}{6\pi}.
\]
In particular, the angle pair has density \(g(\alpha,\beta)=(\sin\alpha+\sin\beta+\sin(\alpha+\beta))/(3\pi)\); the third coordinate is an independent uniform variable on \((-1,1)\); \(Z/\varepsilon\) has limiting \(\operatorname{Beta}(1/2,1)\) law; and the limiting auxiliary triangle is acute with probability exactly \(1/\pi\).

## Assumptions and scope
The point on each original side is sampled independently from normalized arclength on that side, not from the whole three-side perimeter. Areas are unsigned Euclidean areas. All three intersection points are well defined for interior side parameters; the concurrency event \(Z=0\) has probability zero. Barycentric coordinates refer to \(P=AD\cap BE\) regardless of \(F\). The angle-conversion triangle is an auxiliary triangle defined from those coordinates, not the original triangle or the small Routh triangle. All limits fix the sampling scheme while \(\varepsilon\to0\).

## Proof
**1. Affine reduction and exact factorization.** An invertible affine map sends any triangle to \(A=(0,0)\), \(B=(1,0)\), \(C=(0,1)\). Its restriction to each side has constant arclength dilation, preserving the three independent *side-uniform* fractions and normalized area. Thus it suffices to study these vertices with \(D=(u,1-u)\), \(E=(0,v)\), and \(F=(1-w,0)\).

Computing the three pairwise line intersections (equivalently applying the classical Routh formula) yields
\[
Z=\frac{T^2}{Q},\quad T=2uvw-uv-uw+u-vw+v+w-1,
\quad Q=(1-u+uv)(1-w+uw)(1-v+vw).
\]
Every factor in \(Q\) is positive and at most one for \(u,v,w\in(0,1)\). Put
\[
H=uv+(1-u)(1-v)>0,\qquad
w_0=\frac{(1-u)(1-v)}{H}\in(0,1).
\]
Then the crucial exact identity is \(T=H(w-w_0)\), so the Ceva/concurrency set is the smooth graph \(w=w_0(u,v)\) in the open unit cube.

**2. Square-root tube and domination.** Write \(Q_0=Q(u,v,w_0)\). At every fixed interior \((u,v)\), smoothness and \(Q_0>0\) give
\[
\lim_{\varepsilon\downarrow0}\frac{1}{\sqrt\varepsilon}
\operatorname{Leb}\{w\in(0,1):Z(u,v,w)<\varepsilon\}
=\frac{2\sqrt{Q_0}}{H}.
\]
Because \(Q\le1\), this length is at most \(2\sqrt\varepsilon/H\) for every \(\varepsilon>0\). The function \(1/H\) is integrable on the unit square: its only problematic corners are \((0,1)\) and \((1,0)\), where \(H\) is comparable to a sum of two nonnegative coordinate distances. Dominated convergence proves
\[
\Pr(Z<\varepsilon)=2\sqrt\varepsilon\int_0^1\int_0^1\frac{\sqrt{Q_0}}{H}\,du\,dv+o(\sqrt\varepsilon).
\]

**3. Barycentric and angular Jacobians.** Write \((a,b,c)\) for the positive barycentric coordinates of \(P\), with \(c=1-a-b\). The intersection relations \(P\in AD\cap BE\) imply
\[
u=\frac{b}{b+c},\qquad v=\frac{c}{a+c}.
\]
Direct substitution and differentiation give
\[
\frac{\sqrt{Q_0}}{H}\,du\,dv
=\frac{\sqrt{abc}}{(a+b)^2(b+c)^2(c+a)^2}\,da\,db.
\]
The numbers \(A'=a+b=1-c\), \(B'=b+c=1-a\), \(C'=c+a=1-b\) form a triangle with semiperimeter one and area \(\Delta'=\sqrt{abc}\) by Heron's formula. Let its opposite angles be \(\alpha,\beta,\gamma\). Differentiating the cosine law, or the equivalent sine-law inverse \(A'=2\sin\alpha/S\), \(B'=2\sin\beta/S\), \(C'=2\sin\gamma/S\), with \(S=\sin\alpha+\sin\beta+\sin\gamma\), gives
\[
\left|\frac{\partial(a,b)}{\partial(\alpha,\beta)}\right|
=\frac{A'B'C'}{2}.
\]
The circumradius of this auxiliary triangle is \(\rho=1/S\) since its semiperimeter is one; the ordinary circumradius-area identity \(\Delta'=A'B'C'/(4\rho)\) therefore yields
\[
\frac{\sqrt{abc}}{(a+b)^2(b+c)^2(c+a)^2}\,da\,db
=\frac{\sin\alpha+\sin\beta+\sin\gamma}{8}\,d\alpha\,d\beta.
\]
Each of the three sine terms integrates to \(\pi\) on the open angle simplex, so the original double integral equals \(3\pi/8\). Substitution in Step 2 gives the leading coefficient \(3\pi/4\).

**4. Marked total-variation limit.** On any compact subset of the open \((u,v)\)-square, each branch \(w>w_0\) and \(w<w_0\) admits the exact signed square-root-deficit coordinate \(s=\operatorname{sgn}(T)\sqrt{Z/\varepsilon}\). The change-of-variables density in \((u,v,s)\), restricted to \(|s|<1\), divided by \(\sqrt\varepsilon\), converges locally uniformly to \(\sqrt{Q_0}/H\) for each sign. The normalizing probability divided by \(\sqrt\varepsilon\) converges to \(3\pi/4\). Outside a compact subset the contribution is uniformly dominated by \(2/H\), whose integral can be made arbitrarily small. Therefore the full joint densities converge in \(L^1\), establishing total-variation convergence. The angular change of variables from Step 3 gives the displayed product density and independence of the signed uniform mark.

For the acute-triangle conclusion, the acute region is \(0<\alpha<\pi/2\) and \(\pi/2-\alpha<\beta<\pi/2\). Its integral of \(\sin\alpha\) is \(\int_0^{\pi/2}\alpha\sin\alpha\,d\alpha=1\). Symmetry gives the same integral for the other two sine terms, hence total mass \(3/(3\pi)=1/\pi\). Finally the square of a uniform \((-1,1)\) variable has the \(\operatorname{Beta}(1/2,1)\) law.

## Verification
The standalone script `verify_random_routh_cevians.py` requires Python 3, NumPy, and SciPy. It checks the polynomial area identity independently from direct Euclidean line intersections, integrates the coefficient by adaptive quadrature, tests the rare-event square-root prediction by Monte Carlo at three thresholds, and checks the limiting auxiliary acute-angle probability. Replay via `python verify_random_routh_cevians.py`; successful output ends `ROUTH_CEVA_SQRT_AND_ANGLES_CHECK_OK`. The simulations use 1,800,000 independently drawn triples per threshold. The proof of the infinite limiting statements is the change-of-variables and domination argument above, not numerical enumeration.

## Relationship to prior work
Routh's exact cevian-triangle area formula and the Ceva concurrency criterion are classical; neither is claimed as new. Bényi–Ćurgus (2011 preprint, revised 2012) gives a comprehensive generalized area identity. McConnell (2014) extends Ceva–Menelaus and Routh for six marked side points. Abboud (2014) develops barycentric area patterns and parallelogram generalizations. Their accessible full texts treat deterministic ratios, not independent side-uniform sampling, the sharp random near-concurrency coefficient, or the sine-weighted conditional auxiliary-angle density.

The closest meaning-search record, *Sharp Routh-area profile at fixed Ceva product* (2026), gives a deterministic area bound conditional on a fixed product of positive cevian ratios and identifies an extremizer. Its full result states neither a distribution for random triples nor the marked law established here. Pointwise envelopes at fixed product do not determine the law of a random product or the angular weighting along the Ceva surface. Likewise, results on the area of triangles spanned by independent boundary points address a different object, with a different degeneracy exponent.

## Limitations
The random points are chosen one per side with independent uniform arclength, not with a joint correlated law or from the entire perimeter without stratification. The asymptotic does not claim finite-threshold equality or a rate in the \(o(\sqrt\varepsilon)\) remainder. The auxiliary angle distribution describes the Ceva intersection point and not the shape of the small Routh triangle. An equivalent stochastic Ceva theorem in older or non-indexed sources cannot be excluded by finite literature searches; independent verification of historical priority remains necessary.

## References
1. Á. Bényi and B. Ćurgus, *A generalization of Routh's triangle theorem*, arXiv:1112.4813v1 (first public 2011-12-20), https://arxiv.org/abs/1112.4813 ; full HTML https://arxiv.org/html/1112.4813v2 .
2. B. D. S. McConnell, *A Six-Point Ceva-Menelaus Theorem*, arXiv:1403.0478v1 (first public 2014-03-03), https://arxiv.org/html/1403.0478v1 .
3. E. Abboud, *On Routh-Steiner Theorem and Generalizations*, arXiv:1403.5652v1 (first public 2014-03-22), https://arxiv.org/html/1403.5652v1 .
4. *Sharp Routh-area profile at fixed Ceva product*, public research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-sharp-routh-area-profile-at-fixed-ceva-product--9339fa8c11cd/RESULT.md (deterministic comparison only).
