# All fifty first-jet discriminant critical points can be real for ternary cubics

## Finding

For all sufficiently small positive real \(\varepsilon\), define the homogeneous ternary cubic
\[
F_{\varepsilon}(x,y,z)=x^3-3xy^2-\varepsilon z(x^2+y^2)+2z^3.
\]
On the real unit sphere \(S^2\), let the first-jet Bombieri–Weyl discriminant-distance function be
\[
\delta_F(X)=-2F(X)^2+\frac13\|\nabla F(X)\|^2.
\]
Then \(\delta_{F_\varepsilon}\) has at least **fifty distinct nondegenerate real critical points** for every sufficiently small \(\varepsilon>0\). Consequently, a nonempty Euclidean-open set of *generic real ternary cubics* has **exactly fifty real nondegenerate critical points**, attaining the complete complex count in Kozhasov–Mourrain–Parusiński, Theorem 1.2. This answers their Problem 6.2 affirmatively for three variables and degree three; it does not settle other pairs of variables and degrees. The construction is explicit in one positive parameter, although no numerical upper endpoint for that parameter is asserted.

## Assumptions and scope

All functions and critical points are over \(\mathbb R\), and complex critical-point counts refer to the complex quadric \(\{x^2+y^2+z^2=1\}\). The gradient in \(\delta_F\) is the ambient Euclidean gradient, not the spherical gradient. The restriction of \(\delta_F\) to the sphere is the function defined by formula (1.2) of the motivating paper for cubic forms. “Generic” means outside the proper algebraic exceptional set to which its complex critical-point theorem applies. Critical points and nondegeneracy on the sphere are understood with respect to its smooth two-dimensional manifold structure. A simple real critical point persists under a sufficiently small real perturbation of the coefficients.

## Proof

**Step 1: rational meridian coordinates.** More generally put
\[
F_{b,\lambda}=x^3-3xy^2+bz(x^2+y^2)+\lambda z^3,
\qquad b\in\mathbb R,\ \lambda=2.
\]
Off the two poles write
\[
(x,y,z)=\frac{(\cos\theta,\sin\theta,u)}{\sqrt{1+u^2}},
\qquad c=\cos(3\theta).
\]
Direct substitution, using homogeneity of the cubic and its first derivatives, yields the exact rational identity
\[
\delta_{F_{b,\lambda}}(u,\theta)=\frac{N_{b,\lambda}(u,c)}{(1+u^2)^3},
\]
where
\[
N_{b,\lambda}=(c+bu+\lambda u^3)^2
+\frac13\bigl[b+(3\lambda-2b)u^2-3uc\bigr]^2
+3(1-c^2)(1+u^2).
\]
Define the polynomial meridian derivative numerator
\[
P_{b,\lambda}=(1+u^2)\partial_uN_{b,\lambda}-6uN_{b,\lambda}.
\]
Thus a finite critical point satisfies \(P_{b,\lambda}=0\) and either \(\sin(3\theta)=0\) or \(\partial_cN_{b,\lambda}=0\). The latter derivative is simply
\[
\partial_cN_{b,\lambda}=4\bigl((b-\lambda)u^3-c\bigr).
\]

**Step 2: thirty simple finite critical points at \(b=0\).** At \(b=0\), \(\lambda=2\), the exact identities are
\[
P_{0,2}=12u\bigl(c^2+2cu^3-2cu+3u^2-1\bigr),\qquad
\partial_cN_{0,2}=-4(c+2u^3).
\]
The complete list of finite critical configurations *apart from six degenerate equatorial points* is as follows; each pair \((u,c)\) has the indicated number of angular lifts \(\theta\):

| \(u\) | \(c\) | angular lifts | determinant of the \((u,\theta)\)-Hessian |
|:--:|:--:|--:|--:|
| \(0\) | \(0\) | 6 | \(432\) |
| \(-2\) | \(1\) | 3 | \(5184/3125\) |
| \(1/2\) | \(1\) | 3 | \(442368/3125\) |
| \(2\) | \(-1\) | 3 | \(5184/3125\) |
| \(-1/2\) | \(-1\) | 3 | \(442368/3125\) |
| \(1/2\) | \(-1/4\) | 6 | \(-663552/3125\) |
| \(-1/2\) | \(1/4\) | 6 | \(-663552/3125\) |

The signed determinants are obtained by differentiating the displayed rational function; all are nonzero. They represent \(6+12+12=30\) distinct points, which persist as real nondegenerate critical points for small \(b\).

**Step 3: twelve points from the six equatorial degeneracies.** For \(c=s\in\{1,-1\}\), there are three corresponding angles. The remaining finite critical points at \(b=0\) have \(u=0,c=s\) and are degenerate in the meridian direction. For each fixed \(c=s\), exact polynomial division gives
\[
P_{b,2}(u,s)=u\,Q_s(u,b),
\quad Q_s(0,b)=8b-\frac83b^2,
\quad \partial_uQ_s(0,0)=-24s.
\]
The analytic implicit-function theorem therefore supplies a second real root
\[
u_s(b)=\frac{b}{3s}+O(b^2)
\]
of \(P_{b,2}(\cdot,s)=0\) alongside the exact root \(u=0\). For all sufficiently small nonzero \(b\), they are distinct and simple in the meridian direction. At these points \(\sin3\theta=0\), the angular mixed Hessian entry vanishes, while the angular second derivative tends to \(36\). Thus each of six degenerate points splits into **two distinct nondegenerate real critical points**: twelve in total, rather than six.

**Step 4: eight points near the two poles.** Put \(b=-\varepsilon\), \(\lambda=2\), and in a chart near the north/south pole use
\[
x=\varepsilon X,\quad y=\varepsilon Y,\quad
z=\sigma\sqrt{1-\varepsilon^2(X^2+Y^2)},\qquad \sigma\in\{1,-1\}.
\]
On every bounded \((X,Y)\)-set, the *exact Taylor expansion* gives convergence in \(C^2\):
\[
\varepsilon^{-3}\left(\delta_{F_{-\varepsilon,2}}-4\right)
\longrightarrow Q_{\sigma}(X,Y)
=4(X^2+Y^2)-8\sigma(X^3-3XY^2).
\]
The polynomial \(Q_\sigma\) has exactly four distinct real nondegenerate critical points: the origin (Hessian determinant \(64\)) and the three points
\[
(\sigma/3,0),\quad(-\sigma/6,\sqrt3/6),\quad
(-\sigma/6,-\sqrt3/6),
\]
whose Hessian determinants are all \(-192\). The implicit-function theorem applied to the rescaled family preserves these four points near each pole, giving **eight further real nondegenerate critical points** for sufficiently small \(\varepsilon>0\). Their neighborhoods are disjoint from those in Steps 2–3 because the pole chart has radial size \(O(\varepsilon)\), whereas the finite meridian points stay away from the poles.

**Step 5: sharpness and genericity.** Steps 2–4 exhibit \(30+12+8=50\) pairwise distinct real nondegenerate critical points of \(\delta_{F_\varepsilon}\). A finite collection of nondegenerate real critical points persists simultaneously under small real perturbations of \(F_\varepsilon\); hence a nonempty Euclidean-open neighborhood in the ten-dimensional coefficient space has at least fifty real critical points. The generic algebraic locus from Kozhasov–Mourrain–Parusiński, Theorem 1.2, is Zariski open and dense. Its intersection with the constructed Euclidean-open neighborhood is nonempty. At any such generic form, the cited theorem gives exactly
\[
\frac{3(2\cdot3-3)^3-4(3-1)^3-3+4}{(3-2)^2}=50
\]
complex critical points, counted on the complex unit sphere. Therefore all fifty are the real simple points already obtained. Since the generic locus can be chosen Euclidean open near such a form, a nonempty Euclidean-open set of generic forms attains the count.

## Verification

Run the included `verify_ternary_jet.py` with Python 3 and SymPy. It checks the spherical rational reduction modulo \(\cos^2\theta+\sin^2\theta=1\), the meridian and angular derivative identities, all seven finite critical-point classes and Hessian determinants, the two-branch meridian splitting derivatives, and the \(C^2\)-limit polynomials and nondegenerate critical points at both poles. It reports `VERIFY_OK`. These symbolic checks are exact; the passage to every sufficiently small positive parameter and to a generic open neighborhood is proved by the implicit-function theorem, not finite numerical sampling.

## Relationship to prior work

Kozhasov, Mourrain and Parusiński (2026) determine the full complex critical-point count for \(\delta_F^1\) (Theorem 1.2) and explicitly ask whether all these points can be real (Problem 6.2). Their general count and the first-jet distance formula are premises, not claimed as new. The present theorem answers the all-real question in the previously unresolved non-binary cubic case \(n=d=3\), via an explicit perturbative construction. Kozhasov (2018) constructs fully real *eigenconfigurations*, i.e., critical points of \(F|_{S^{n-1}}\); that is a distinct function and count and does not imply this result. Literature and research-record searches identified no statement establishing fifty real first-jet discriminant-distance critical points for ternary cubics. Priority is subject to later specialist review; no claim is made for arbitrary \(n,d\).

## Limitations

The theorem concerns real ternary cubics only and establishes existence for sufficiently small positive parameter; it does not furnish an explicit rational upper bound on \(\varepsilon\), classify all real cubics with the property, identify the global distance minimizer, or prove the all-real property for higher degrees or dimensions. The displayed special family is used to exhibit persistent critical points, while genericity is achieved by a further arbitrarily small coefficient perturbation. No independent mathematical audit has been performed.

## References

1. K. Kozhasov, B. Mourrain, A. Parusiński, *On the distance to discriminants and osculating varieties*, arXiv:2610.06538v1, first publicly submitted 2026-10-05. Theorem 1.2; equation (1.2); Problem 6.2. https://arxiv.org/abs/2610.06538
2. K. Kozhasov, *On fully real eigenconfigurations of tensors*, SIAM Journal on Applied Algebra and Geometry 2 (2018), 339–347, DOI:10.1137/17M1145902; arXiv:1707.04005 (earlier eigenconfiguration problem).
