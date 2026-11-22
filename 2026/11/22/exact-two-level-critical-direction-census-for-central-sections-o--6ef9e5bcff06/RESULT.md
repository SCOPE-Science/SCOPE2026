# Exact two-level critical-direction census for central sections of the five-cube

## Finding

Let \(Q=[-\tfrac12,\tfrac12]^5\) and let
\[
\sigma(v)=\mathcal H^4(Q\cap v^\perp),\qquad v\in\mathbb R^5\setminus\{0\}.
\]
Call a unit normal *two-level with full support* when its five absolute coordinates are positive and take exactly two distinct values. Then **all** stationary points of \(\sigma\) on the unit sphere among these normals are, up to coordinate permutations and sign changes, the unique direction
\[
\boxed{v_*=\frac{(1,1,\tau,\tau,\tau)}{\sqrt{2+3\tau^2}},\qquad
\tau=\frac{24-\sqrt{69}}{39}=0.402394259925177568\ldots.}
\]
There are exactly \(\binom52\,2^4=160\) distinct *unoriented* stationary hyperplanes of this two-level full-support kind, constituting one hyperoctahedral-symmetry orbit. Their common section volume is exactly
\[
\boxed{\sigma(v_*)=\sqrt{2+3\tau^2}\left(1-\frac{13\tau}{32}\right)
=1.31889442272420290\ldots.}
\]
Along the one-dimensional two-level path \((1,1,t,t,t)\), \(0<t<1\), this point is its unique strict minimum. This is **not** a claim of a local minimum among all normal vectors: the prior work proves the constructed non-diagonal critical point is a saddle in the full sphere.

## Assumptions and scope

The cube has unit edge length and is centered at the origin; \(\mathcal H^4\) means intrinsic Euclidean four-volume, not coordinate-parametrized volume. Normals \(v\) and \(-v\) define the same hyperplane. The classification is *only* for normals with **five nonzero coordinates and exactly two positive absolute-coordinate levels**. It excludes normals with zero coordinates, all-equal absolute coordinates, and vectors with three or more distinct absolute-coordinate values. All positive real ratios are covered, including ratios where the combinatorial type of the section changes. Stationarity always refers to the full four-dimensional unit sphere of normal directions, not merely to a restricted symmetric path.

By signs, permutations, and positive rescaling, every normal in scope has a unique representation \((\underbrace{1,\ldots,1}_{p},\underbrace{t,\ldots,t}_{q})\) with \(p+q=5\), \(p,q\ge1\), and \(0<t<1\). The four exhaustive cases are \((p,q)=(1,4),(2,3),(3,2),(4,1)\).

## Proof

**1. Symmetry reduces full stationarity to a single derivative.** Let \(V_{p,q}(t)=\sigma(1^p,t^q)\) for \(0<t<1\). The volume function is continuously differentiable wherever all normal coordinates are nonzero, as follows either from convolution of five uniform densities or the piecewise fourth-power formula below. At a two-level point, its Euclidean gradient is constant on each of the two equal-coordinate blocks, by permutation invariance. Hence its tangential gradient on the unit sphere belongs to the one-dimensional space of block-constant tangent vectors. The normalized path \((1^p,t^q)/\sqrt{p+qt^2}\) spans this space tangentially, since \(p,q>0\) and \(t>0\). Therefore a full-sphere stationary normal occurs if and only if \(V'_{p,q}(t)=0\).

**2. An exact convolution formula.** Let \(X_1,\dots,X_5\) be independent uniform variables on \([-\tfrac12,\tfrac12]\), and let \(f_{p,q}(t)\) be the density at zero of \(\sum_{i\le p} X_i+t\sum_{i>p}X_i\). The coarea formula gives
\[
V_{p,q}(t)=\sqrt{p+qt^2}\,f_{p,q}(t).
\]
Repeated convolution of uniform interval densities, or finite-difference inclusion–exclusion, gives the exact piecewise-rational identity
\[
f_{p,q}(t)=\frac{1}{24t^q}\sum_{j=0}^p\sum_{k=0}^q(-1)^{j+k}
\binom pj\binom qk\left(\frac p2-j+\left(\frac q2-k\right)t\right)_+^4,
\qquad (x)_+=\max\{x,0\}.
\tag{1}
\]
The fourth power makes all the transition knots continuously differentiable. Set
\[
D_{p,q}(t)=(p+qt^2)f'_{p,q}(t)+qt f_{p,q}(t),
\quad V'_{p,q}(t)=\frac{D_{p,q}(t)}{\sqrt{p+qt^2}}.
\tag{2}
\]
Thus the signs and zeros of \(D_{p,q}\) give the complete stationarity census.

**3. Exact formulas on every interval.** Expanding (1) and reducing rational functions yields the following exhaustive list, where rows are separated at every positive-part knot. In the displayed table \(f=f_{p,q}(t)\) and \(D=D_{p,q}(t)\):

| \((p,q)\) | Range | \(f\) | \(D\) |
|---|---|---|---|
| \((2,3)\) | \(0<t<2/3\) | \(1-13t/32\) | \(-(39t^2-48t+13)/16\) |
| \((2,3)\) | \(2/3<t<1\) | \((3t^4-24t^3+216t^2-96t+16)/(192t^3)\) | \((t-1)P_{23}(t)/(32t^4)\) |
| \((3,2)\) | \(0<t<1/2\) | \((9-2t^2)/12\) | \(-t(2t^2-1)/2\) |
| \((3,2)\) | \(1/2<t<1\) | \((16t^4-96t^3+216t^2-24t+3)/(192t^2)\) | \((t-1)P_{32}(t)/(32t^3)\) |
| \((1,4)\) | \(0<t<1/4\) | \(1\) | \(4t\) |
| \((1,4)\) | \(1/4<t<1/2\) | \(-(64t^4-256t^3+96t^2-16t+1)/(192t^4)\) | \(-P_{14}(t)/(48t^5)\) |
| \((1,4)\) | \(1/2<t<1\) | \((128t^3-16t+3)/(192t^4)\) | \(-(t-1)(3t-1)/(16t^5)\) |
| \((4,1)\) | \(0<t<1\) | \((3t^3-16t^2+128)/192\) | \(t^2(t-3)(t-1)/16\) |

The three polynomial abbreviations are
\[
\begin{aligned}
P_{23}(t)&=3t^5-9t^4-8t^3+40t^2-48t+16,\\
P_{32}(t)&=16t^5-48t^4+40t^3-8t^2-9t+3,\\
P_{14}(t)&=64t^6-96t^4+96t^3-51t^2+12t-1.
\end{aligned}
\tag{3}
\]
Both \(f\) and \(f'\) agree at adjacent transition points, as follows from (1) and is also checked directly from the rational expressions.

**4. Sign certificates and uniqueness.** For \((2,3)\) on \(0<t<2/3\), the derivative numerator vanishes exactly at
\[
t=\frac{24\pm\sqrt{69}}{39}.
\]
The smaller root \(\tau\) lies in \((2/5,1/2)\), while the larger is greater than \(2/3\). Therefore \(D_{2,3}\) is strictly negative before \(\tau\) and strictly positive from \(\tau\) to \(2/3\). To verify that the sign remains positive on \([2/3,1)\), put \(u=3t-2\in[0,1]\). The polynomial \(-P_{23}((u+2)/3)\) has degree-five Bernstein coefficients
\[
\left(\frac{160}{81},\frac{128}{45},\frac{488}{135},\frac{196}{45},\frac{77}{15},6\right),
\]
all strictly positive. Since every Bernstein basis function is nonnegative on \([0,1]\) and the basis sums to one, \(P_{23}(t)<0\) throughout this branch. Together with \(t-1<0\), this yields \(D_{2,3}(t)>0\). Therefore \(\tau\) is the sole interior stationary ratio and the unique restricted-path strict minimum.

For \((3,2)\), the first branch has \(D=-t(2t^2-1)/2>0\) since \(t<1/2\). On the second, \(u=2t-1\in[0,1]\) yields
\[
P_{32}((u+1)/2)=\frac{u^5-u^4-4u^3-6u-2}{2}<0.
\]
As \(t-1<0\), also \(D_{3,2}(t)>0\).

For \((1,4)\), the first branch has \(D=4t>0\). On the middle branch, \(u=4t-1\in[0,1]\), the polynomial \(-P_{14}((u+1)/4)\) has degree-six Bernstein coefficients
\[
\left(\frac3{64},\frac3{32},\frac3{16},\frac5{16},\frac{37}{80},\frac58,\frac34\right),
\]
so again \(D>0\). On the last branch, \(-(t-1)(3t-1)/(16t^5)>0\). For \((4,1)\), \(t^2(t-3)(t-1)/16>0\) on \((0,1)\). Thus **all three other block multiplicities are strictly increasing**, and neither transition knot introduces a stationary point. The list is complete by Step 1.

**5. Volume and orbit count.** Because \(\tau<2/3\), the first \((2,3)\) density branch gives the exact displayed volume. The two large-coordinate positions can be chosen in \(\binom52=10\) ways. Each choice has \(2^5\) independent sign patterns, modulo the simultaneous overall sign, giving \(10\cdot2^4=160\) unoriented hyperplanes, all distinct since \(0<\tau<1\). This exhausts the stated class. \(\square\)

## Verification

The standalone `verify.py` is executable with Python 3, SymPy, NumPy and SciPy by running `python3 verify.py`. It independently constructs the section vertices from intersections with five-cube edges, projects them into an orthonormal hyperplane basis, computes Euclidean four-volume via `scipy.spatial.ConvexHull`, and compares with the convolution formula at 20 parameter values across every knot interval. It also exactly expands all eight density and derivative branches, checks differentiability at the four branch knots, verifies both Bernstein-coefficient positivity certificates, checks the \((3,2)\) substitution identity, and verifies the critical quadratic root. Its observed output is `PASS 75 exact symbolic identities/positivity conditions and independent geometric volume comparisons` and prints the critical ratio, normalized coordinate, and critical volume recorded above.

The finite convex-hull comparisons are **not** a proof for all real parameters; Steps 1–5 give the analytic universal proof. The symbolic checks use exact rational arithmetic for the certificate identities.

## Relationship to prior work

Ambrus and Gárgyán's *Non-diagonal critical central sections of the cube* (arXiv:2307.03792, first public 2023-07-07) proves existence of a non-diagonal full-support stationary normal with two large coordinates in **every** dimension at least four. Their Section 5 explicitly reports only a numerical value for the dimension-five ratio and states that their proof does **not** establish uniqueness, which they conjecture. Their Section 6 already proves the constructed critical direction is a full-sphere saddle. The present result does **not** claim discovery of that saddle or of a general cube-section formula; it resolves the exact algebraic value, uniqueness on the natural \((2,3)\) arc, the absence of all other full-support two-level critical directions in dimension five, and the exact orbit count. See https://arxiv.org/html/2307.03792v4, Sections 5–6.

Ambrus, *Critical central sections of the cube* (arXiv:2107.14778, first public 2021-07-30) characterizes critical central sections in dimensions three and four, including a dimension-four two-level direction; it does not classify the dimension-five full-support case. Brandenburg, De Loera and Meroni, *The Best Ways to Slice a Polytope* (arXiv:2304.14239, first public 2023-04-27), provide general algorithms for polytope-section optimization; the abstract and source metadata do not establish this explicit stationarity census.

Three independently inspected published geometric findings also concern sections of cubes, but establish respectively the **ridge area** for five-cube sections with normal \((1,1,1,1,s)\), the **covariance eigenspaces** of a four-cube section, and a **zonotopality criterion** for arbitrary cube sections. None of these published statements implies the critical normal classification for the five-cube volume functional. Their separate mathematical objects and parameters are not being conflated with volume stationarity.

## Limitations

The theorem does not classify normals with three or more distinct nonzero absolute values, nor does it extend its uniqueness conclusion to higher dimensions. It does not replace the global stationary classification, and its unique symmetric-path minimum remains a saddle on the full sphere by prior work. Finding an explicit quadratic ratio for one dimension does not establish the conjectured uniqueness for every dimension. The novelty assessment is a best-knowledge literature comparison, not a guarantee against unindexed earlier exact calculations or unrelated equivalent characterizations. No independent mathematical audit has been performed.

## References

1. G. Ambrus and B. Gárgyán, *Non-diagonal critical central sections of the cube*, arXiv:2307.03792 (first posted 2023-07-07); full text at https://arxiv.org/html/2307.03792v4; Advances in Mathematics 441 (2024), 109524.
2. G. Ambrus, *Critical central sections of the cube*, arXiv:2107.14778 (first posted 2021-07-30), https://arxiv.org/abs/2107.14778.
3. M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239 (first posted 2023-04-27), https://arxiv.org/abs/2304.14239.
4. *Exact ridge-area profile for symmetric four-dimensional sections of the five-cube*, mathematical research record: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-ridge-area-profile-for-symmetric-four-dimensional-sections--bd1b77b94571.
5. *A three-halves covariance-axis transition inside a fixed four-cube section type*, mathematical research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-three-halves-covariance-axis-transition-inside-a-fixed-four-cu--e8262b256ed3.
6. *A dominance criterion for zonotopal central sections of cubes*, mathematical research record: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-dominance-criterion-for-zonotopal-central-sections-of-cubes--fd7b9cd5f90d.
