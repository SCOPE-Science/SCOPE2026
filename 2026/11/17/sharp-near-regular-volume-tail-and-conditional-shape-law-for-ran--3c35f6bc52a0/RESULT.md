# Sharp near-regular volume tail and conditional shape law for random inscribed tetrahedra

## Finding
Let \(P_1,P_2,P_3,P_4\) be independent surface-area-uniform points on the Euclidean unit sphere \(S^2\), and let \(V\) be the ordinary three-dimensional volume of their convex hull. The sharp maximum is \(V_*=8/(9\sqrt3)\). Put \(\Delta=1-V/V_*\). Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-5/2}\Pr(\Delta<\varepsilon)=\frac{128\sqrt3}{405}.}
\]
The asymptotic concerns the positive relative volume deficiency, not a small-volume event. Equivalently, for absolute deficiencies \(t\downarrow0\),
\[
\Pr(V>V_*-t)\sim\frac{9\sqrt2\,3^{3/4}}{10}t^{5/2}.
\]
There is also a complete rotation-reduced conditional shape limit. Rotate the sample so that \(P_1=(0,0,1)\) and \(P_2\) lies in the half-plane of azimuth zero. Write the other three polar heights as \(x,y,z\in(-1,1)\) and the azimuths of \(P_3,P_4\) as \(\phi,\psi\in\mathbb R/(2\pi\mathbb Z)\). Define
\[
q_+=(-1/3,-1/3,-1/3,2\pi/3,4\pi/3),\qquad
q_-=(-1/3,-1/3,-1/3,4\pi/3,2\pi/3).
\]
For sufficiently small \(\Delta\), each sample is close to one of these two points. If it is close to \(q_-\), first interchange the labels \(P_3,P_4\); if it is close to \(q_+\), leave them fixed. Let \(q\) denote the resulting five coordinates, taken in a local real angle chart around \(q_+\), and let \(\sigma\in\{+,-\}\) record whether the interchange was made. Conditional on \(\Delta<\varepsilon\), the pair
\[
\left(\sigma,\frac{q-q_+}{\sqrt\varepsilon}\right)
\]
converges in distribution to an independent fair sign and the uniform probability measure on the five-dimensional ellipsoid \(\mathcal E=\{h\in\mathbb R^5:h^{\mathsf T}Hh<2\}\), where
\[
H=\begin{pmatrix}
27/32&9/64&9/64&\sqrt3/8&-\sqrt3/8\\
9/64&27/32&9/64&0&\sqrt3/8\\
9/64&9/64&27/32&-\sqrt3/8&0\\
\sqrt3/8&0&-\sqrt3/8&2/3&-1/3\\
-\sqrt3/8&\sqrt3/8&0&-1/3&2/3
\end{pmatrix}.
\]
The conditional limiting law describes the full five-dimensional unlabeled-up-to-chirality local shape deformation, not independent edge perturbations.

## Assumptions and scope
All four points have independent normalized spherical surface measure, not volume measure in the ball. Volumes are Euclidean, with no orientation sign. The coordinate reduction uses rotations and fixes the azimuth of the second vertex, which is valid almost surely. The two coordinates \(q_\pm\) are separated, and the local chart is used only when the relative deficiency is sufficiently small. The theorem is for exactly four points on \(S^2\); no claim is made for arbitrary sample counts or higher dimensions.

## Proof
**1. Global maximum and its equality locus.** Let \(m=(P_1+\cdots+P_4)/4\) and \(S=\sum_{i=1}^4(P_i-m)(P_i-m)^{\mathsf T}\). For the difference matrix \(B=[P_2-P_1\;P_3-P_1\;P_4-P_1]\), direct centering yields \(\det(B)^2=4\det(S)\). Moreover,
\[
\operatorname{tr}S=4-4\|m\|^2\le4,
\quad
\det S\le (\operatorname{tr}S/3)^3\le(4/3)^3.
\]
It follows that \(6V=|\det B|\le16\sqrt3/9\), hence \(V\le V_*\). Equality requires \(m=0\) and \(S=(4/3)I_3\). For the \(3\)-by-\(4\) column matrix \(A=[P_1\;\cdots\;P_4]\), this gives \(A\mathbf1=0\), \(AA^{\mathsf T}=(4/3)I_3\), so \(A^{\mathsf T}A=(4/3)(I_4-\mathbf1\mathbf1^{\mathsf T}/4)\). Thus every distinct pair of maximizing vertices has dot product \(-1/3\): the maxima are precisely the labelled regular tetrahedra, in two orientation classes modulo rotations. Compactness excludes any other near-maximal regions for sufficiently small deficiency.

**2. Exact reduced coordinates and density.** By rotation invariance, set \(P_1=(0,0,1)\) and \(P_2=(\sqrt{1-x^2},0,x)\). Set
\[
P_3=(\sqrt{1-y^2}\cos\phi,\sqrt{1-y^2}\sin\phi,y),\quad
P_4=(\sqrt{1-z^2}\cos\psi,\sqrt{1-z^2}\sin\psi,z).
\]
Then \(q=(x,y,z,\phi,\psi)\) has constant probability density \(1/(32\pi^2)\) relative to \(dx\,dy\,dz\,d\phi\,d\psi\) on \((-1,1)^3\times[0,2\pi)^2\). This density is exact because the polar height of each point is uniform on \((-1,1)\) and its azimuth is uniform independently. Define
\[
\begin{aligned}
D(q)={}&(x-1)\sqrt{(1-y^2)(1-z^2)}\sin(\psi-\phi)\\
&-(y-1)\sqrt{(1-x^2)(1-z^2)}\sin\psi\\
&+(z-1)\sqrt{(1-x^2)(1-y^2)}\sin\phi.
\end{aligned}
\]
This is exactly \(\det(P_2-P_1,P_3-P_1,P_4-P_1)\), and \(V=|D|/6\). The only global maxima of \(|D|\) in these reduced coordinates are \(q_+\) and \(q_-\), at which \(|D|=16\sqrt3/9\).

**3. Exact transverse second variation.** Around \(q_+\), \(D\) has negative sign, so \(\Delta=1+D/(16\sqrt3/9)\). Direct differentiation of the displayed elementary determinant gives a vanishing gradient and
\[
\Delta(q_++h)=\tfrac12 h^{\mathsf T}Hh+O(\|h\|^3),
\]
with the explicit matrix \(H\) in the finding. Its five leading principal minors are
\[
27/32,\quad 2835/4096,\quad18225/32768,\quad1215/4096,\quad243/2048,
\]
all strictly positive. Thus \(H\) is positive definite, \(\det H=243/2048\), and \(\sqrt{\det H}=9\sqrt6/64\). Interchanging \(P_3,P_4\) carries \(q_-\) to \(q_+\), preserving the coordinate density and absolute volume, so both local maxima contribute the same amount.

**4. Tube integration and conditional shape.** By compactness and the strictly positive Hessian, for any fixed bounded rescaled set of \(h\), the inequality \(\Delta(q_++\sqrt\varepsilon h)<\varepsilon\) converges away from a null boundary to \(h^{\mathsf T}Hh<2\). Local positive quadratic bounds confine all contributing rescaled coordinates to a fixed ball for small \(\varepsilon\). Dominated convergence applies, also with any bounded continuous test function of \(h\), proving the asserted ellipsoid-uniform conditional law and fair independent chirality sign. The volume of the five-dimensional Euclidean unit ball is \(8\pi^2/15\), whence
\[
\begin{aligned}
\lim_{\varepsilon\downarrow0}\varepsilon^{-5/2}\Pr(\Delta<\varepsilon)
&=2\cdot\frac1{32\pi^2}\cdot\frac{8\pi^2}{15}
\cdot\frac{2^{5/2}}{\sqrt{243/2048}}\\
&=\frac{128\sqrt3}{405}.
\end{aligned}
\]
The statement for absolute deficiency follows by substituting \(\Delta=t/V_*\). The same local argument handles strict or non-strict inequalities because the normalized limiting ellipsoid boundary has zero volume. This completes the proof.

## Verification
The included independent-coordinate geometry script `check_tetra_endpoint.py` (Python 3 with `numpy` and `sympy`) differentiates the determinant expression symbolically, checks the exact Hessian, computes its determinant and leading principal minors, and compares the determinant against Cartesian scalar triple products at generic configurations. It then simulates nine million independent reduced-coordinate configurations to check the probability tail at four small thresholds, and checks the quadratic approximation in random local directions. The analytic proof, not these finite experiments, establishes the full theorem. Run `python check_tetra_endpoint.py` from a directory containing the script after installing the dependencies in `requirements.txt`.

## Relationship to prior work
The regular tetrahedron is the classical maximum-volume tetrahedron inscribed in the sphere. Horváth and Lángi (2014) study maximum-volume inscribed polytopes with greater vertex counts; their paper does not give a near-maximum probability law for four random vertices. Miles (1971) computes moment formulae for isotropic random simplex volumes and already covers substantial scalar-volume information. The new statement emphasizes the sharp endpoint constant **and the full conditional local shape distribution**; a formula for scalar moments alone does not determine the conditional distribution of the five labelled shape coordinates given a rare near-maximum volume event. Akopyan, Edelsbrunner and Nikitenko (2020) derive expected intrinsic volumes and mean deficiencies from the ball for random spherical polytopes, including a section on deficiencies, but not this fixed-four-vertex conditional near-regular law. The published upper-tail theorem for eight points on \(S^3\) concerns a different four-dimensional polytope and has an explicit exclusion of other vertex counts; its generic tube integration method does not supply this five-dimensional tetrahedral Hessian, constant, or conditional law. MathWorld's sphere-tetrahedron entry gives the sampling parametrization and several moments but not the near-maximum conditional shape law.

## Limitations
Historical priority is provisional. The full text of Miles's 1971 paper was not accessible during the comparison, so it is not claimed to have been exhaustively ruled out; its abstract and the indexed moment formulas were inspected. The theorem does not provide a finite-deficiency distribution, a remainder rate, statistical stability of shape inference, or an extension to tetrahedra sampled from the solid ball. The five local coordinates depend on the stated rotation/azimuth gauge, and the assertion concerns that gauge only, not independence of individual edges. No independent mathematical review is claimed.

## References
1. Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, first posted 2014-02-26, arXiv:1402.6496v1. https://arxiv.org/abs/1402.6496
2. R. E. Miles, *Isotropic random simplices*, Advances in Applied Probability **3** (1971), 353–382, DOI:10.2307/1426176. https://doi.org/10.2307/1426176
3. A. Akopyan, H. Edelsbrunner, and A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-Sphere*, arXiv:2007.07783v1, especially Sections 5 and 7. https://arxiv.org/abs/2007.07783
4. E. W. Weisstein, *Sphere Tetrahedron Picking*, MathWorld, https://mathworld.wolfram.com/SphereTetrahedronPicking.html
5. *Sharp ninth-power upper-volume tail for eight random points on the three-sphere*, published repository result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-ninth-power-upper-volume-tail-for-eight-random-points-on-t--32bb10986e8d
