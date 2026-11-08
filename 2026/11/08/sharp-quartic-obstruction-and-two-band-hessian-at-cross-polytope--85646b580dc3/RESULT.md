# Sharp quartic obstruction and two-band Hessian at cross-polytope spherical two-designs

## Finding

Consider the unnormalized real spherical two-moment discrepancy
\[
\mathcal E_{a,b}(X)=a\left\|\sum_{i=1}^d(x_{i,+}+x_{i,-})\right\|^2+b\left\|\sum_{i=1}^d(x_{i,+}x_{i,+}^{\mathsf T}+x_{i,-}x_{i,-}^{\mathsf T})-2I_d\right\|_F^2
\]
on \( (S^{d-1})^{2d}\), where \(d\ge3\) is an integer and \(a,b>0\). At the labelled cross-polytope \(X_0=(x_{i,\pm}=\pm e_i)_{i=1}^d\), the complete product-sphere Riemannian Hessian has spectrum
\[
\boxed{0\ (\text{multiplicity }d(3d-5)/2),\quad 4a(d-1)\ (\text{multiplicity }d),\quad 16b\ (\text{multiplicity }d(d-1)/2).}
\]
The positive-spectrum condition number is minimized uniquely, with value \(1\), at \(a/b=4/(d-1)\). This does **not** remove the Hessian's nonrotational zero modes.

The new fourth-order statement gives the precise obstruction hidden in those zero modes. Write an infinitesimal symmetric-pair variation as
\[
\dot x_{i,+}(0)=\dot x_{i,-}(0)=p_i/\sqrt2,\qquad p_i\perp e_i,\qquad\sum_i p_i=0.
\]
Define the squared-flow imbalance
\[
D_j(p)=\sum_{i\ne j}p_{i,j}^2-\sum_{k\ne j}p_{j,k}^2,\qquad j=1,\ldots,d,
\]
where \(p_{i,j}\) denotes the \(j\)-th coordinate of \(p_i\). For **every** \(C^2\) curve of unit-vector configurations with initial value \(X_0\) and precisely these first derivatives,
\[
\boxed{\liminf_{t\to0,\ t\ne0}\frac{\mathcal E_{a,b}(X(t))}{t^4}\ge b\sum_{j=1}^d D_j(p)^2.}
\]
The bound is sharp for every allowed \(p\): an explicit real-analytic curve with these first derivatives attains the corresponding limit. Consequently, \(D(p)=0\) if and only if some analytic curve with this initial velocity satisfies \(\mathcal E_{a,b}(X(t))=O(t^6)\). This last statement concerns second-order feasibility of the moment constraints, **not** existence of an exact design curve for every balanced \(p\).

For each \(d\ge3\), a concrete flat Hessian velocity has \(p_1=e_3\), \(p_2=-e_3\), and every other \(p_i=0\). Its imbalance is \(D=(-1,-1,2,0,\ldots,0)\). One analytic curve with this velocity has the exact positive energy
\[
\boxed{\mathcal E_{a,b}(X(t))=\frac{6b\,t^4}{(1+t^2/2)^2}.}
\]
In contrast, for every nonzero real skew-symmetric \(K\) with \(K\mathbf1=0\), the curves \(x_{i,+}(t)=e^{tK/2}e_i\), \(x_{i,-}(t)=-e^{-tK/2}e_i\) are nonrotational exact two-design deformations through \(X_0\), showing that some nonrotational Hessian-zero directions really are integrable.

## Assumptions and scope

All vectors and matrices are **real**. The ambient metric is the product of round-sphere metrics, so tangent coordinates have the ordinary summed Euclidean norm; the discrepancy uses **unnormalized sums**, with no factor of \(1/(2d)\). The first-moment term is essential to the stated spectrum. We use the Frobenius norm on real \(d\)-by-\(d\) matrices. Only the degree-at-most-two moment discrepancy is analyzed, although the cross-polytope also gives a spherical three-design. The fourth-order result fixes the first derivative of every labelled point; it does not allow a different first-order rotation or re-labelling.

## Proof

**1. Spectral splitting.** For tangent vectors \(u_{i,\pm}\in e_i^\perp\), set
\[
p_i=(u_{i,+}+u_{i,-})/\sqrt2,\qquad q_i=(u_{i,+}-u_{i,-})/\sqrt2.
\]
This is an isometry of tangent coordinate spaces. Put \(s(X)=\sum_{i,\pm}x_{i,\pm}\) and \(M(X)=\sum_{i,\pm}x_{i,\pm}x_{i,\pm}^{\mathsf T}-2I_d\). At \(X_0\), both vanish, and their differentials are
\[
\dot s=\sqrt2\sum_i p_i,\qquad \dot M=\sqrt2\sum_i(e_iq_i^{\mathsf T}+q_ie_i^{\mathsf T}).
\]
Because \(\mathcal E=a\|s\|^2+b\|M\|_F^2\) has zero residual at \(X_0\), its Riemannian Hessian quadratic form is exactly \(2a\|\dot s\|^2+2b\|\dot M\|_F^2\). On the \(p\)-space, \(A(p)=\sum_i p_i\) satisfies \(AA^*=(d-1)I_d\): for a vector \(y\), the \(i\)-th block of \(A^*y\) is \(y-y_ie_i\). Hence one positive Hessian eigenvalue is \(4a(d-1)\) with multiplicity \(d\), while its kernel has dimension \(d(d-2)\).

On the \(q\)-space, the diagonal of \(\dot M\) is zero and for \(i<j\), its \((i,j)\)-entry is \(\sqrt2(q_{i,j}+q_{j,i})\). Therefore
\[
2b\|\dot M\|_F^2=8b\sum_{i<j}(q_{i,j}+q_{j,i})^2.
\]
Each independent two-coordinate block has eigenvalues \(16b,0\). Thus \(16b\) occurs \(d(d-1)/2\) times, with another \(d(d-1)/2\) zero modes (exactly the infinitesimal common rotations). Adding the kernels proves the stated spectrum. Positive-spectrum conditioning is \(\max\{4a(d-1),16b\}/\min\{4a(d-1),16b\}\), which equals one exactly at the displayed ratio.

**2. Universal fourth-order lower bound.** Fix \(p_i\perp e_i\) with \(\sum_i p_i=0\), and let a \(C^2\) sphere-valued curve have \(\dot x_{i,\pm}(0)=p_i/\sqrt2\). Taylor expand as
\[
x_{i,\sigma}(t)=\sigma e_i+t p_i/\sqrt2+t^2(\sigma[-\|p_i\|^2/4]e_i+w_{i,\sigma})+o(t^2),\quad\sigma\in\{+1,-1\},\quad w_{i,\sigma}\perp e_i.
\]
The radial coefficient follows from \(\|x_{i,\sigma}(t)\|=1\). The second-order covariance residual is
\[
M(X(t))=t^2\left(T(p)+\sum_i[e_i v_i^{\mathsf T}+v_ie_i^{\mathsf T}]\right)+o(t^2),\quad v_i=w_{i,+}-w_{i,-},
\]
where \(T(p)=\sum_i(p_ip_i^{\mathsf T}-\|p_i\|^2 e_ie_i^{\mathsf T})\). Because every \(v_i\perp e_i\), the correction matrix has zero diagonal, while \(T(p)_{jj}=D_j(p)\). Hence the squared Frobenius norm of the covariance error is at least \(t^4\sum_jD_j(p)^2+o(t^4)\); the nonnegative centroid error only increases the objective. This proves the bound.

**3. Attainment and two-jet classification.** Define tangent correction vectors \(v_i\) by \(v_{i,i}=0\) and \(v_{i,j}=-T(p)_{ij}/2\) for \(i\ne j\), noting that \(T(p)\) is symmetric. Take the explicit normalized analytic curves
\[
x_{i,\sigma}(t)=\frac{\sigma e_i+t p_i/\sqrt2+\sigma t^2v_i/2}{\|\sigma e_i+t p_i/\sqrt2+\sigma t^2v_i/2\|}.
\]
Their centroid has no terms of order zero, one, or two. Their second-order covariance residual equals precisely \(\operatorname{diag}D(p)\), since the selected corrections cancel every off-diagonal entry of \(T(p)\). It follows that \(\mathcal E(X(t))=b t^4\|D(p)\|_2^2+O(t^5)\). If \(D=0\), both residuals begin at order three, so \(\mathcal E=O(t^6)\). Conversely, \(\mathcal E=o(t^4)\) for a \(C^2\) curve forces \(D=0\) by the lower bound. This establishes the claimed equivalence without claiming that every balanced jet integrates to an exact spherical design.

**4. Exact quartic example and integrable comparison.** With \(p_1=e_3\) and \(p_2=-e_3\), the vector sum is zero, the covariance second-order tensor is \(T=\operatorname{diag}(-1,-1,2,0,\ldots,0)\), and the off-diagonal corrections are unnecessary. Set
\[
x_{1,\sigma}(t)=\frac{\sigma e_1+t e_3/\sqrt2}{\sqrt{1+t^2/2}},\quad x_{2,\sigma}(t)=\frac{\sigma e_2-t e_3/\sqrt2}{\sqrt{1+t^2/2}},\quad x_{i,\sigma}(t)=\sigma e_i\quad(i\ge3).
\]
The centroid is identically zero; the covariance residual is diagonal with entries \(-t^2/(1+t^2/2)\), \(-t^2/(1+t^2/2)\), \(2t^2/(1+t^2/2)\), and zeros, proving the exact energy. Separately, if \(K^{\mathsf T}=-K\) and \(K\mathbf1=0\), the two sets \(\{e^{tK/2}e_i\}_i\) and \(\{-e^{-tK/2}e_i\}_i\) are orthonormal bases with equal sums and combined second moment \(2I_d\). The initial velocities agree within each antipodal pair and yield nontrivial zero-Hessian directions whenever \(K\ne0\), as asserted.

## Verification

Run `python3 checker.py` in an ordinary Python environment with `numpy` and `sympy` installed. The checker constructs integer moment Jacobians from the stated unnormalized functional, compares all Hessian eigenvalues numerically to the exact formulas for dimensions \(3\) through \(10\), independently verifies exact Jacobian ranks in dimensions \(3\) through \(6\), checks the complete second-order cancellation over rational velocity families, and verifies the nonintegrable example, including an independent symbolic check of its exact energy. Its expected terminal message is `CROSSPOLYTOPE_EXACT_CHECKS_PASS 1110`. The proof above establishes all dimensions analytically; finite tests are corroboration only.

## Relationship to prior work

Xiao and Zhuang (first publicly posted March 9, 2023, arXiv:2303.05365; published 2023) derive general spherical-design discrepancy, gradient and Hessian machinery and numerically construct the octahedron as a spherical **three-design**. That established framework motivates the exact local study here, but its inspected sections do not give this real, dimension-uniform, **two-moment** cross-polytope spectrum, the balancing weight, or the sharp coefficient of residual fourth-order error.

Needham and Shonkwiler (arXiv:2110.11295, first posted October 21, 2021) establish a general quadratic-cone description of singular **complex** tight-frame varieties at orthodecomposable configurations. Accordingly, the qualitative possibility of nonintegrable first-order directions is **not** asserted to be new here. Their result does not supply the explicit centered-real cross-polytope Hessian bands or the sharp \(b\|D\|^2\) energy coefficient for this specific unnormalized two-moment functional. The general Hessian/optimization perspective of Mixon, Needham, Shonkwiler and Villar is also acknowledged. 

## Limitations

The classification is for labelled configurations and fixed first-order velocities of the symmetric-pair form only. It does not classify all global minimizers, prove convergence rates of a numerical solver, or provide a full analytic description of all exact design curves through the cross-polytope. The sharp quartic barrier is not coercive along every zero-Hessian direction: some admit exact design deformations. Earlier real moment-map geometry might contain a reformulation of the concrete diagonal-balance criterion; historical originality requires further expert review. The result has no independent mathematical audit.

## References

1. Y. Xiao and X. Zhuang, *Spherical Framelets from Spherical Designs*, arXiv:2303.05365 (version 1, 2023-03-09), https://arxiv.org/abs/2303.05365; SIAM Journal on Imaging Sciences 16 (2023), 2072–2104, https://doi.org/10.1137/22M1542362.
2. T. Needham and C. Shonkwiler, *Toric Symplectic Geometry and Full Spark Frames*, arXiv:2110.11295 (version 1, 2021-10-21), https://arxiv.org/abs/2110.11295; freely available author text: https://www.math.colostate.edu/~clayton/research/papers/fullspark.pdf.
3. D. G. Mixon, T. Needham, C. Shonkwiler and S. Villar, *Three Proofs of the Benedetto–Fickus Theorem*, freely available author text: https://www.math.colostate.edu/~clayton/research/papers/BenedettoFickus.pdf.
