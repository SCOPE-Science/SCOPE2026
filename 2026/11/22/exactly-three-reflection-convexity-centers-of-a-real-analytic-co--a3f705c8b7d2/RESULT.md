# Exactly three reflection-convexity centers of a real-analytic constant-width oval

## Finding
Let \(R>8\varepsilon>0\). There is a unique strictly positively curved planar convex body \(K_{R,\varepsilon}\) whose support function, in the normal-angle parameter, is
\[
h(\theta)=R+\varepsilon\cos(3\theta).
\]
It is real analytic and has constant width \(2R\). Call \(z\in\mathbb R^2\) a **reflection-convexity center** if \(K_{R,\varepsilon}\cup(2z-K_{R,\varepsilon})\) is convex. Its complete set of such centers consists of **exactly three points**:
\[
\boxed{z_k=-3\varepsilon\bigl(\cos(2\pi k/3),\sin(2\pi k/3)\bigr),\quad k=0,1,2.}
\]
They are the vertices of an equilateral triangle. At every one of them, the union is a centrally symmetric, strictly convex body whose support function measured relative to its symmetry center \(z_k\), after rotating the normal angle by \(2\pi k/3\), is
\[
\boxed{H(\theta)=R+4\varepsilon|\cos\theta|^3.}
\]
The union has the **exact** perimeter and area
\[
\boxed{P_{\cup}=2\pi R+\frac{32}{3}\varepsilon,\qquad
 A_{\cup}=\pi R^2+\frac{32}{3}R\varepsilon-4\pi\varepsilon^2.}
\]
In particular, the area gained over the original oval is exactly \(32R\varepsilon/3\). The boundary of each convex union is \(C^2\) but not \(C^3\) at its two reflection-joining normals, whereas the original oval is real analytic.

## Assumptions and scope
All convex bodies are compact subsets of the Euclidean plane with nonempty interior. The support function of a convex body is \(h(\theta)=\max_{x\in K}\langle x,n(\theta)\rangle\), where
\[
n(\theta)=(\cos\theta,\sin\theta),\qquad t(\theta)=(-\sin\theta,\cos\theta).
\]
For a smooth, strictly positively curved support function the unique support point is \(x(\theta)=h(\theta)n(\theta)+h'(\theta)t(\theta)\). Since \(h+h''=R-8\varepsilon\cos3\theta>0\), the stated support function indeed defines such a body. The identity \(h(\theta)+h(\theta+\pi)=2R\) proves constant width. Moreover \(h\ge R-\varepsilon\), so \(K_{R,\varepsilon}\) contains the disk of radius \(R-\varepsilon\) centered at the origin.

The strict conditions \(\varepsilon>0\) and \(R>8\varepsilon\) are part of the claim. In particular the circular degeneration \(\varepsilon=0\) is excluded, because it has a different reflection-center set. A phase-shifted or translated oval gives the rigid-motion image of the same three centers.

## Proof
**1. The common-support obstruction.** Put \(L_z=2z-K_{R,\varepsilon}\). Its normal-angle support function is
\[
h_{L_z}(\theta)=2\langle z,n(\theta)\rangle+h(\theta+\pi)
=R+2\langle z,n(\theta)\rangle-\varepsilon\cos3\theta.
\]
Define the half-difference
\[
f_z(\theta)=\tfrac12\bigl(h(\theta)-h_{L_z}(\theta)\bigr)
=\varepsilon\cos3\theta-\langle z,n(\theta)\rangle.
\]
At any zero of \(f_z\), the bodies share a supporting line. Each has a single support point there. If their union is convex, those support points must coincide: otherwise the supporting segment joining them belongs to the union's convex hull but not to the union of its two singleton support faces. The support-point formula therefore forces equality of the tangential support coordinates, namely \(f_z'(\theta)=0\). Thus
\[
K_{R,\varepsilon}\cup L_z\text{ convex}
\quad\Longrightarrow\quad
f_z(\theta)=0\implies f_z'(\theta)=0.
\tag{1}
\]

**2. Necessity of one of three centers.** The function \(f_z\) is real analytic, is not identically zero (its third Fourier harmonic is nonzero), and obeys \(f_z(\theta+\pi)=-f_z(\theta)\). It therefore has a sign-changing zero \(\theta_0\). If the union is convex, (1) gives \(f_z'(\theta_0)=0\). An analytic sign-changing zero with vanishing first derivative has odd multiplicity at least three, so also \(f_z''(\theta_0)=0\). The three equations are
\[
\begin{aligned}
\langle z,n(\theta_0)\rangle&=\varepsilon\cos3\theta_0,\\
\langle z,t(\theta_0)\rangle&=-3\varepsilon\sin3\theta_0,\\
0=f_z''(\theta_0)&=-9\varepsilon\cos3\theta_0+\langle z,n(\theta_0)\rangle
=-8\varepsilon\cos3\theta_0.
\end{aligned}
\]
Hence \(\cos3\theta_0=0\) and \(z=-3\varepsilon\sin3\theta_0\,t(\theta_0)\). The six possible angles modulo \(2\pi\) produce precisely the three listed points, since opposite angles produce the same \(z\). No other reflection-convexity center is possible.

**3. Sufficiency and the exact symmetric hull.** It suffices by threefold rotational symmetry to examine \(z_0=(-3\varepsilon,0)\). The elementary identity \(\cos3\theta+3\cos\theta=4\cos^3\theta\) gives
\[
f_{z_0}(\theta)=4\varepsilon\cos^3\theta.
\]
Consequently the common-support angles are exactly \(\theta=\pi/2,3\pi/2\), and the support functions agree there to first derivative order. At all other directions one body has a strictly larger support value, so the convex hull of the two bodies has a singleton support face belonging to that body. At the two common-support directions the singleton faces coincide, since \(f_{z_0}=f_{z_0}'=0\). Therefore every point on the boundary of the convex hull lies in \(K_{R,\varepsilon}\cup L_{z_0}\).

Also \(z_0\) lies in both bodies: indeed \(|z_0|=3\varepsilon<R-\varepsilon\), and the disk inclusion from the assumptions gives \(z_0\in K_{R,\varepsilon}\); reflection in \(z_0\) fixes that point. Any point of the convex hull lies on a segment from \(z_0\) to a boundary point; that segment is contained in whichever of the two convex bodies contains the boundary point. Thus the whole convex hull is the union. This proves convexity.

The support function of the union relative to \(z_0\) is its maximal support value minus \(\langle z_0,n(\theta)\rangle\):
\[
\begin{aligned}
H(\theta)
&=\max\{R+\varepsilon\cos3\theta,\ R-6\varepsilon\cos\theta-\varepsilon\cos3\theta\}
  +3\varepsilon\cos\theta\\
&=R+\left|\varepsilon\cos3\theta+3\varepsilon\cos\theta\right|
=R+4\varepsilon|\cos\theta|^3.
\end{aligned}
\]
This is \(\pi\)-periodic and therefore is the support function of a centrally symmetric body. Its curvature radius is
\[
H+H''=R-8\varepsilon\operatorname{sgn}(\cos\theta)\cos3\theta
\quad(\cos\theta\ne0),
\]
with continuous extension \(R\) at the two joining normals. It is strictly positive because \(R>8\varepsilon\). The term \(|\cos\theta|^3\) is \(C^2\) but not \(C^3\) at these normals. More explicitly, the curvature radius \(\rho=H+H\x27\x27\) is continuous, positive, and has a nonzero jump in one-sided derivatives. Thus curvature \(1/\rho\) is continuous but not differentiable as a function of arclength, so the geometric boundary is \(C^2\) but not \(C^3\). Rotation supplies the other two cases.

**4. Exact perimeter and area.** For a \(C^2\) strictly convex support function \(H\), the planar support formulas are
\[
P=\int_0^{2\pi}H(\theta)\,d\theta,
\qquad A=\frac12\int_0^{2\pi}\bigl(H(\theta)^2-H'(\theta)^2\bigr)\,d\theta.
\]
Using \(g(\theta)=|\cos\theta|^3\), the elementary integrals are
\[
\int_0^{2\pi}g\,d\theta=\frac83,\quad
\int_0^{2\pi}g^2\,d\theta=\frac{5\pi}{8},\quad
\int_0^{2\pi}(g')^2\,d\theta=\frac{9\pi}{8}.
\]
Inserting \(H=R+4\varepsilon g\) gives
\[
P_{\cup}=2\pi R+\frac{32}{3}\varepsilon,
\qquad
A_{\cup}=\pi R^2+\frac{32}{3}R\varepsilon-4\pi\varepsilon^2.
\]
For the original oval, the same area identity and Fourier orthogonality yield \(A(K_{R,\varepsilon})=\pi R^2-4\pi\varepsilon^2\). Subtraction gives the asserted exact area increment.

## Verification
The proof is exact for every pair \(R>8\varepsilon>0\), with no inference from a finite sample. The included `check_reflection_convexity.py` requires only the Python standard library. It checks three admissible parameter pairs, the three reflection-center formulas, the triple-zero support identities, positivity of curvature, numerical support integrals against the exact perimeter/area expressions, and transversal common supports at representative excluded points. Execution returns `ANALYTIC_THREE_REFLECTION_CENTERS_CHECKS_OK`. These finite checks are independent transcription sanity checks, not substitutes for the sign-changing-zero argument or the global convexity proof.

## Relationship to prior work
Schneider's 2015 *Reflections of planar convex bodies* introduced convexity points, proved that every noncentrally symmetric planar convex body has at least three affinely independent ones, and established the general middle-line criterion for convex reflection unions. Schneider's 2016 *The middle hedgehog of a planar convex body* describes midpoint support loci, gives a typical-infinite-multiplicity theorem, and names triangles and Reuleaux triangles as examples with precisely three centers. Neither inspected paper states the present real-analytic, positive-curvature, constant-width example with exactly three centers or the support, area, and perimeter of its reflection unions.

Other published finite-count examples classify convexity points of quadrilaterals without parallel sides and of regular odd polygons. They do not imply exactness for a smooth oval. A separate two-harmonic Wigner-caustic classification includes the pure third harmonic and determines its three cusps; cusp count alone is not an exact reflection-convexity-center classification, since the exposed-point implication is one-way. The present necessity argument excludes all other centers and the explicit support formula supplies additional quantitative information. Full bibliographic priority is not claimed.

## Limitations
The theorem concerns the pure third support harmonic and its translates and rotations, not arbitrary analytic ovals or mixtures of odd modes. The strict positivity condition \(R>8\varepsilon\) is used throughout; no endpoint claim is made at \(R=8\varepsilon\). The circle case \(\varepsilon=0\) is excluded. The results do not establish that every analytic oval has finitely many centers, and they do not settle historical priority beyond the inspected sources.

## References
1. R. Schneider, *Reflections of planar convex bodies*, arXiv:1504.00541v1, first public 2015-04-02. In particular Section 2, Lemmas 1--2, and the proof of Theorem 1. https://arxiv.org/abs/1504.00541
2. R. Schneider, *The middle hedgehog of a planar convex body*, arXiv:1607.03014v1, first public 2016-07-11. In particular Section 1 and the middle-hedgehog parametrization in Section 2. https://arxiv.org/abs/1607.03014
3. *Exactly three convexity points for quadrilaterals without parallel sides*, published mathematical record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exactly-three-convexity-points-for-quadrilaterals-without-parall--3019eafaeb1d
4. *Regular odd polygons have exactly as many convexity points as vertices*, published mathematical record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-regular-odd-polygons-have-exactly-as-many-convexity-points-as-ve--fbe5b682b936
5. *Sharp phase locking of Wigner-caustic cusps in the first two odd support harmonics*, published mathematical record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-phase-locking-of-wigner-caustic-cusps-in-the-first-two-odd--1b55f2f7ba5a
