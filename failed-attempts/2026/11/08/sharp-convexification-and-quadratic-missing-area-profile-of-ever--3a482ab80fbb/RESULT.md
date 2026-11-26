# Sharp convexification and quadratic missing-area profile of every trapezoid vertex set

## Finding
Let \(Q\subset\mathbb R^2\) be a nondegenerate convex trapezoid, including a parallelogram, with four distinct vertices, parallel base lengths \(L\ge \ell>0\), and \(t=\ell/L\in(0,1]\). Let \(V=V(Q)\) denote its four-vertex set. For \(\lambda\ge0\), put
\[
S_\lambda(Q)=\frac{V+\lambda Q}{1+\lambda},\qquad
D_Q(\lambda)=\frac{\operatorname{area}(Q\setminus S_\lambda(Q))}{\operatorname{area}(Q)}.
\]
Then the exact Schneider nonconvexity index is
\[
\boxed{c(V)=\inf\{\lambda\ge0:V+\lambda Q=(1+\lambda)Q\}=2-t.}
\]
For every genuine non-parallelogram trapezoid \(0<t<1\), the complete near-convexification area deficit is
\[
\boxed{D_Q(\lambda)=\frac{(2-t-\lambda)^2}{(1-t^2)(1+\lambda)^2}\quad(1\le\lambda\le2-t),}
\]
and \(D_Q(\lambda)=0\) for all \(\lambda\ge2-t\). For parallelograms \(t=1\), \(c(V)=1\) and \(D_Q(\lambda)=0\) whenever \(\lambda\ge1\).

In particular \(D_Q(1)=(1-t)/(4(1+t))\) for \(0<t<1\). For each fixed \(0<t<1\), as \(\varepsilon\downarrow0\),
\[
D_Q(2-t-\varepsilon)=\frac{\varepsilon^2}{(1-t^2)(3-t-\varepsilon)^2}
\sim \frac{\varepsilon^2}{(1-t^2)(3-t)^2}.
\]
Thus the uncovered area vanishes with the exactly quadratic critical exponent, with an explicit affine-invariant coefficient.

## Assumptions and scope
A trapezoid has two opposite parallel edges of positive lengths; the parallelogram case is permitted. Four distinct extreme points and nonzero planar area are assumed. The shorter-to-longer base ratio \(t\) is invariant under invertible affine maps. The sets \(S_\lambda\) are subsets of \(Q\); the area is ordinary two-dimensional Lebesgue area. The stated area formula covers the complete interval \(1\le\lambda\le2-t\), not the range \(0\le\lambda<1\). The index statement covers every \(\lambda\ge0\).

## Proof
**Affine reduction.** Translation, a shear parallel to the bases, and independent nonzero horizontal and vertical scaling send \(Q\) to
\[
T_t=\operatorname{conv}\{(-1,0),(1,0),(-t,1),(t,1)\}.
\]
The base-length ratio remains \(t\); Minkowski sums and the equality \(V+\lambda Q=(1+\lambda)Q\) commute with invertible affine maps (translations cancel under normalization), and area fractions are preserved. It therefore suffices to prove the assertions for \(T_t\), whose horizontal section at height \(y\in[0,1]\) is \([-w(y),w(y)]\), with \(w(y)=1-(1-t)y\) and \(\operatorname{area}(T_t)=1+t\).

Set \(\beta=\lambda/(1+\lambda)\). Then \(S_\lambda(T_t)\) is the union of four closed copies \((1-\beta)v+\beta T_t\) indexed by the vertices \(v\). If \(\beta<1/2\), the two copies attached to the bottom base cover only two disjoint intervals at height \(y=0\), while the top-attached copies miss \(y=0\). Hence \(S_\lambda(T_t)\ne T_t\). This proves nonconvexification for every \(\lambda<1\), including \(t=1\).

Assume now \(\beta\ge1/2\). At every height \(0\le y\le\beta\), the two copies attached to the bottom vertices have interval centers \(\pm(1-\beta)\), common halfwidth
\[
r_{\mathrm b}(y)=\beta-(1-t)y.
\]
Their outermost endpoints are \(\pm w(y)\). Both intervals together cover the entire \(T_t\) section exactly when
\[
r_{\mathrm b}(y)\ge1-\beta\quad\Longleftrightarrow\quad
1-2\beta+(1-t)y\le0.
\]
Similarly, at each height \(1-\beta\le y\le1\), the two copies attached to the top vertices have centers \(\pm t(1-\beta)\) and common halfwidth
\[
r_{\mathrm t}(y)=\beta-(1-t)(y-1+\beta).
\]
Their outermost endpoints are again \(\pm w(y)\). As \(r_{\mathrm t}(y)\ge t\beta\ge t(1-\beta)\), these top copies cover the *whole* section whenever \(y\ge1-\beta\). Consequently all potential missing points occur below \(y_1=1-\beta\), where only bottom copies are available.

For \(0<t<1\), the two bottom intervals first separate around the horizontal centerline above the critical height
\[
y_0=\frac{2\beta-1}{1-t}.
\]
When \(\beta\ge1/2\), the uncovered set is therefore *exactly*
\[
T_t\setminus S_\lambda(T_t)=
\{(x,y): y_0<y<y_1,\ |x|<(1-t)(y-y_0)\}
\]
if \(y_0<y_1\), and is empty otherwise. The strict inequalities are necessary: the top copies fill the entire section at \(y=y_1\), and the boundary edges of the bottom intervals remain covered.

The gap is nonempty exactly when
\[
\frac{2\beta-1}{1-t}<1-\beta
\quad\Longleftrightarrow\quad
\beta<\frac{2-t}{3-t}
\quad\Longleftrightarrow\quad
\lambda<2-t.
\]
This is the claimed sharp index in the genuine trapezoid case. The gap is a triangle with height \(y_1-y_0\) and top width \(2(1-t)(y_1-y_0)\), with its top side excluded. Its area is
\[
(1-t)(y_1-y_0)^2
=\frac{(2-t-\lambda)^2}{(1-t)(1+\lambda)^2}.
\]
Dividing by \(\operatorname{area}(T_t)=1+t\) proves the exact relative deficit and quadratic onset. If \(t=1\), each section of \(T_1\) is the interval \([-1,1]\); when \(\beta\ge1/2\), the bottom copies alone cover the interval for \(y\le\beta\) and the top copies alone cover it for \(y\ge1-\beta\). Hence \(c(V(T_1))=1\). Affine invariance completes the proof. \(\square\)

## Verification
The standalone `trapezoid_convexification_verify.py` uses only Python 3's standard-library `fractions.Fraction`. Its point-in-homothet function independently enumerates all four vertex translates and tests the normalized remaining point against the trapezoid's exact inequalities. It checks the predicted uncovered triangular region against **39,919 exact-rational assertions** across five strict base ratios, the parallelogram endpoint, and parameters below, at, and above the threshold. It additionally verifies strict subcritical witnesses and the integrated missing-area identity. Run `python3 trapezoid_convexification_verify.py` and expect `EXACT_RATIONAL_OK 39919`. The proof above, not finite sampling, establishes the universal theorem for arbitrary real parameters and affine trapezoids.

## Relationship to prior work
Schneider introduced the affine nonconvexity index; Artstein-Avidan, Falah and Slomka introduced the equivalent vertex-generation weight \(\eta(Q)=1/(1+c(V(Q)))\). Their general planar bounds and the fact that every zonotope is vertex-generated imply, in particular, the known parallelogram endpoint \(c=1\), but do not supply the sharp continuous base-ratio formula or a missing-area profile for non-parallelogram trapezoids. Meyer's 2026 work characterizes the existence of finite Minkowski convexification and develops exposed-face criteria in the planar case; its results do not explicitly evaluate the trapezoid vertex threshold or the quadratic area deficit. The new claim is the exact *all-trapezoid, all-near-critical-parameters* classification; no novelty is claimed for the definition, general finite-convexification theorem, or parallelogram endpoint.

## Limitations
The explicit deficit profile is established for \(\lambda\ge1\); no formula is asserted for the more complicated subunit regime. The statement concerns vertex sets of planar trapezoids and does not classify all nontrapezoidal quadrilaterals or higher-dimensional prismatoids. Independent expert review and definitive historical priority checks have not been performed. Search absence is not proof that the formula was never previously published.

## References
- Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1 (first posted 2026-10-19), https://arxiv.org/abs/2610.26744 . In particular the index definition, main finiteness theorems and Section 2.3 on planar exposed faces.
- Shiri Artstein-Avidan, Tomer Falah and Boaz A. Slomka, *Vertex generated polytopes*, arXiv:2407.20604v1 (2024-07-30), https://arxiv.org/abs/2407.20604 . In particular Definition 1.1, the relation to Schneider's index and the theorem that zonotopes are vertex-generated.
