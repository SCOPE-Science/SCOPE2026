# A sharp dipole–quadrupole saddle in extreme spherical-triangle perimeter probabilities

## Finding

Let three points be sampled independently on the round unit sphere \(S^2\). Let \(P\) be the sum of their three shorter geodesic side lengths and let \(E_\varepsilon=\{P>2\pi-\varepsilon\}\). Fix either a vector \(d\in\mathbb R^3\) with \(\|d\|<1\), or a real symmetric trace-zero \(3\times3\) matrix \(A\) with \(I+A\) positive definite. Consider the normalized positive probability densities
\[
 f_d(p)=\frac{1+d\cdot p}{4\pi},\qquad
 f_A(p)=\frac{1+p^\mathsf T A p}{4\pi} \quad (p\in S^2).
\]
The **entire leading near-maximal-perimeter coefficient** is given exactly, without requiring the anisotropy to tend to zero:
\[
 \boxed{\lim_{\varepsilon\downarrow0}\frac{\mathbb P_d(E_\varepsilon)}{C_*\sqrt\varepsilon}=1-m\|d\|^2,\qquad
 \lim_{\varepsilon\downarrow0}\frac{\mathbb P_A(E_\varepsilon)}{C_*\sqrt\varepsilon}
 =1+\frac{\operatorname{tr}(A^2)}{20}-\frac{\operatorname{tr}(A^3)}{42}.}
\]
Here \(C_*=\pi\Gamma(7/4)/(16\Gamma(5/4)^3)=0.242332519572411\ldots\) is the previously known isotropic constant. The new strictly positive universal constant is the natural weighted-angle mean
\[
 m=\frac1I\int_0^\pi\int_0^\kappa
 \cos x\,\sqrt{\sin\kappa\sin x\sin(\kappa-x)}\,dx\,d\kappa
 =0.4296991136262733\ldots,
 \quad I=\int_0^\pi\int_0^\kappa\sqrt{\sin\kappa\sin x\sin(\kappa-x)}\,dx\,d\kappa.
\]
Thus every nonzero admissible dipole strictly **suppresses** extreme perimeters; every nonzero admissible quadrupole strictly **enhances** them. In the second family the following stability inequality is sharp over all admissible matrices:
\[
 \boxed{\lim_{\varepsilon\downarrow0}\frac{\mathbb P_A(E_\varepsilon)}{C_*\sqrt\varepsilon}
 \ge 1+\frac{11}{420}\operatorname{tr}(A^2),}
\]
with strict inequality for every nonzero admissible \(A\), and best possible coefficient \(11/420\), approached when the eigenvalues of \(A\) tend to \((2,-1,-1)\). Uniform sampling is therefore a strict **saddle** of this rare-event coefficient within the first two nonconstant spherical-harmonic sectors, not a local extremizer.

## Assumptions and scope

The sphere has radius one; shortest geodesic distances are in \([0,\pi]\). The sampling density is with respect to ordinary spherical area, independently for all three points. Positivity is strict, equivalently \(\|d\|<1\) or \(\lambda_{\min}(A)>-1\); trace zero ensures normalization. The limit is at a fixed density, not a joint anisotropy–threshold limit. The scalar probability limit and the sharp stability constant are the sole claimed results. The known isotropic perimeter density and the known circular-ensemble conditional shape law are prerequisites, not newly asserted findings.

## Proof

**1. A geometric probability limit.** Choose the first point at \((1,0,0)\) and, after a global random rotation, the second at \((\cos\kappa,\sin\kappa,0)\), where \(0<\kappa<\pi\) has density \(\sin\kappa/2\). Write the third point in longitude \(\theta\) and signed latitude \(z\); its conditional area measure is \(\cos z\,d\theta\,dz/(4\pi)\). For the maximum-perimeter boundary, \(\theta=\pi+x\) with \(0<x<\kappa\) and \(z=0\). A direct expansion of the two distances gives, locally uniformly on the strict angular simplex,
\[
2\pi-P=\frac{\sin\kappa}{2\sin x\sin(\kappa-x)}z^2+O(z^4).
\]
Consequently, putting \(z=\sqrt\varepsilon h\), the normalized uniform rare-event measure tends to \(\sin\kappa\,d\kappa\,dx\,dh/(8\pi)\) on
\[
0<x<\kappa<\pi,\qquad |h|<\sqrt{\frac{2\sin x\sin(\kappa-x)}{\sin\kappa}}.
\]
To justify global integration, the Gram determinant identity
\[
\sin^2\kappa\sin^2z
=4\sin s\sin(s-a)\sin(s-b)\sin(s-c),\quad s=P/2,
\]
for the three side lengths \(a,b,c\), gives \(|\sin z|\le\min(1,\sqrt{2\varepsilon}/\sin\kappa)\) on the rare event. Splitting the \(\kappa\)-integral into a compact interior and two arbitrarily small endpoint strips and then shrinking the longitude endpoint strips proves tightness at scale \(\sqrt\varepsilon\). It also proves convergence of bounded continuous orientation-weighted observables, not merely the total mass. This is the core localization argument underlying the known uniform marked limit. Integrating \(h\), the limiting angular probability weight is
\[
 W(x,y,w)=\sqrt{\sin x\sin y\sin w},\quad
 x,y,w>0,\quad x+y+w=\pi,
\]
where \(y=\kappa-x\), \(w=\pi-\kappa\). Its integral is \(I\), and Dyson's circular integral yields \(C_*\) as displayed. The overall spatial orientation remains independently Haar-uniform in \(SO(3)\).

**2. Change of sampling density and rotational moments.** Under the base uniform law, the likelihood for three i.i.d. observations from \(f_d\) or \(f_A\) is respectively \(\prod_{i=1}^3(1+d\cdot p_i)\) or \(\prod_{i=1}^3(1+p_i^\mathsf T A p_i)\). These products are bounded at fixed admissible parameters, so Step 1 permits taking the boundary limit inside their conditional expectations. The limiting coplanar locations have pairwise dot products, in some order,
\[
 c_{12}=-\cos x,\qquad c_{23}=-\cos y,\qquad c_{31}=-\cos w.
\]
For a Haar-random global rotation, each one-point linear or trace-free quadratic term has mean zero. For two points \(p,q\),
\[
\mathbb E_R[(d\cdot Rp)(d\cdot Rq)]=\frac{\|d\|^2}{3}(p\cdot q),
\quad
\mathbb E_R[(p^\mathsf TR^\mathsf T A Rp)(q^\mathsf TR^\mathsf T A Rq)]
=\frac{2\operatorname{tr}(A^2)}{15}P_2(p\cdot q),
\]
where \(P_2(t)=(3t^2-1)/2\). The triple linear term vanishes: a half-turn about the common plane's normal reverses all three coplanar points. Thus the dipole factor is exactly \(1+\|d\|^2\mathbb E(c_{12}+c_{23}+c_{31})/3=1-m\|d\|^2\), by the symmetry of \(W\).

**3. The exact two- and three-body angular moments.** The three angular variables are symmetric under permutations with density \(W/I\). Their half-angle circular phases \(0,2x,2(x+y)\) form a three-particle Dyson circular ensemble with repulsion exponent \(\beta=1/2\). A direct integration by parts for the circular density \(\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^\beta\) gives
\[
\mathbb E\left|\sum_{j=1}^3e^{i\theta_j}\right|^2
=\frac{3}{1+\beta}=2.
\]
Indeed, integrate \(\sum_j\partial_{\theta_j}[e^{i\theta_j}\overline{\sum_ke^{i\theta_k}}\,W_{\rm circ}]\) on the torus, and pair terms with \((e^{i\theta_j}-e^{i\theta_k})\cot((\theta_j-\theta_k)/2)=i(e^{i\theta_j}+e^{i\theta_k})\) (with the missing \(i\) arising from the derivative of each complex exponential). The resulting identity is \([1+\beta]\mathbb E|\sum_je^{i\theta_j}|^2=3\). Thus symmetry gives \(\mathbb E\cos(2x)=-1/6\), so
\[
\mathbb E\cos^2x=5/12,\qquad
\mathbb E P_2(-\cos x)=1/8.
\]
As \(x+y+w=\pi\), elementary trigonometry yields \(\cos^2x+\cos^2y+\cos^2w+2\cos x\cos y\cos w=1\). Taking expectations yields
\[
\mathbb E\sum\cos^2x=5/4,\qquad
\mathbb E[\cos x\cos y\cos w]=-1/8.
\]
It follows that the total pairwise quadratic contribution is \(3(2/15)(1/8)\operatorname{tr}(A^2)=\operatorname{tr}(A^2)/20\).

**4. Cubic rotation average and invariant identification.** For the axisymmetric trace-zero matrix \(A_\eta=\eta\operatorname{diag}(-1/2,-1/2,1)\), its pointwise quadratic term is \(\eta P_2(p_z)\). For three fixed unit vectors with pairwise dot products \(c_{ij}\), the ordinary uniform spherical second-, fourth-, and sixth-moment identities imply
\[
\mathbb E_R\prod_{i=1}^3P_2((Rp_i)_z)
=\frac{2-3(c_{12}^2+c_{23}^2+c_{31}^2)+9c_{12}c_{23}c_{31}}{35}.
\]
The angular averages from Step 3 give \(\mathbb E\sum c_{ij}^2=5/4\) and \(\mathbb E(c_{12}c_{23}c_{31})=1/8\), hence the cubic coefficient is exactly \(-1/56\) for \(A_\eta\). Since the full cubic expectation is an \(SO(3)\)-invariant homogeneous cubic polynomial in a trace-zero real symmetric matrix, diagonalization and symmetry in its three eigenvalues show it must be proportional to \(\operatorname{tr}(A^3)\). As \(\operatorname{tr}(A_\eta^3)=3\eta^3/4\), the proportionality constant is \(-1/42\). There are no terms of degree greater than three because only three independent samples occur. This completes both exact formulas.

**5. Strict signs and optimal stability.** Since \(x+y+w=\pi\), the pointwise identity \(\cos x+\cos y+\cos w=1+4\sin(x/2)\sin(y/2)\sin(w/2)>0\) proves \(m>0\). For any admissible nonzero matrix \(A\), all three eigenvalues are greater than \(-1\), have sum zero, and their squared sum is strictly below six. For the sharp trace inequality, fix \(q=\operatorname{tr}(A^2)\) and maximize the cubic power sum over three real eigenvalues of sum zero and square sum \(q\). Lagrange multipliers imply that at a nontrivial extremum the eigenvalues take at most two values; they therefore have proportions \((2,-1,-1)\) up to sign and permutation. Substitution proves the sharp inequality
\[
|\operatorname{tr}(A^3)|\le\frac{\operatorname{tr}(A^2)^{3/2}}{\sqrt6},
\]
therefore yields \(\operatorname{tr}(A^3)<\operatorname{tr}(A^2)\). Substituting in the exact polynomial gives
\[
\frac{\operatorname{tr}(A^2)}{20}-\frac{\operatorname{tr}(A^3)}{42}
>\left(\frac1{20}-\frac1{42}\right)\operatorname{tr}(A^2)
=\frac{11}{420}\operatorname{tr}(A^2).
\]
The family \(A_t=t\operatorname{diag}(2,-1,-1)\), \(t\uparrow1\), is strictly admissible and attains the last coefficient in the limit, showing its sharpness. The two density families provide directions of both signs around uniform sampling, proving the asserted saddle.

## Verification

The standalone `verify.py` performs independent deterministic two-dimensional quadrature of the angular normalization \(I\), the cosine moment \(m\), the quadratic moment \(\mathbb E P_2(-\cos x)\), and the triple contraction \(\mathbb E[\cos x\cos y\cos w]\). It checks the gamma-constant relation and the algebraic cubic coefficient \(-1/56\) and then performs seeded sampling of global orientations of limiting coplanar triples to test the predicted dipole and quadrupole likelihood ratios. The checker is diagnostic only; the continuum statements follow from the proof and exact spherical moment formulas. Execute `python verify.py` with Python's standard library.

## Relationship to prior work

The three-uniform-vertex maximal-perimeter square-root tail, its exact \(C_*\), and its circular-ensemble conditional gap law have previously been derived. They are **reused as input**, rather than claimed here. Finch and Jones (2010) review a classical exact integral for the uniform triangle-perimeter density. Le (1989) concerns shape densities for uniform sampling on a spherical cap; its accessible abstract does not describe anisotropic harmonic perturbations, although the full text could not be inspected. The new result determines the *nonuniform sampling response*: a finite exact trace polynomial on the entire admissible quadrupole cone, the strictly opposite dipole sign, and a **sharp, globally valid quadrupole stability inequality**. This exact sign dichotomy and sharp coefficient are not stated in the inspected uniform-model statements, nor are they an evaluation of an existing table entry. Their derivation requires additional tensor averaging, a circular-ensemble Fourier moment, and the invariant cubic classification.

## Limitations

The law concerns only three independent samples, the round two-sphere, the near-\(2\pi\) perimeter tail, and the specified degree-one or degree-two positive sampling densities. For general smooth densities the coefficient can be represented as a weighted conditional expectation, but this result does not provide a closed polynomial beyond the stated families or higher-order small-threshold corrections. The scalar isotropic coefficient and circular ensemble shape limit were previously known; no independent mathematical audit has been performed. A published general anisotropic full-shape theorem could potentially subsume the specialized response, though none was located in the inspected sources.

## References

1. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, first posted 2010-09-27, https://arxiv.org/abs/1009.5329. Full accessible text, especially sections 2 and 3.
2. *A circular-ensemble boundary law for nearly maximal spherical triangle perimeters*, publicly accessible mathematical research record, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-circular-ensemble-boundary-law-for-nearly-maximal-spherical-tr--b0aaedddabf0. Complete result and proof examined.
3. *Dyson circular shape laws at the maximal perimeter of random spherical triangles*, publicly accessible mathematical research record, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-dyson-circular-shape-laws-at-the-maximal-perimeter-of-random-sph--4e61cd3549f1. Complete result and proof examined.
4. H. Le, *Random Spherical Triangles II: Shape Densities*, Advances in Applied Probability 21 (1989), 581–594, DOI:10.2307/1427637. Accessible abstract; full text not available for inspection.
5. F. J. Dyson, *Statistical theory of the energy levels of complex systems I*, Journal of Mathematical Physics 3 (1962), 140–156; circular ensemble integration by parts background.
