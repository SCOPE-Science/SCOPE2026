# Sharp consistent-mass stability of nodal spectral clipping on simplicial meshes

## Finding

For every nondegenerate \(d\)-simplex, \(d\ge1\), and every conforming mesh of such simplices, consider nodewise Frobenius-nearest spectral clipping of symmetric \(m\times m\) tensors to a common interval \([a,b]\), followed by continuous affine reinterpolation. When \(m\ge2\) and \(a<b\), its optimal *universal* \(L^2\) Frobenius-norm Lipschitz constant over all such meshes is
\[
C_d=\frac{d+3}{2\sqrt{d+2}}.
\]
The bound is exactly attained by two distinct tensor fields on one simplex, for each dimension. The scalar analogue instead has the sharp universal constant
\[
C_d^{\rm scalar}=\sqrt{\frac{(\lfloor n/2\rfloor+1)(\lceil n/2\rceil+1)}{n+1}},\qquad n=d+1.
\]
These constants coincide when \(d\) is odd; tensor clipping is strictly more amplifying when \(d\) is even. In particular, on triangles \(C_2=5/4\) while \(C_2^{\rm scalar}=\sqrt{3/2}\). In contrast, clipping in the nodal mass-lumped \(L^2\) Frobenius norm has sharp modulus one.

## Assumptions and scope

Let \(\Omega\) be a domain with a conforming simplicial mesh \(\mathcal T\) of nondegenerate simplices in \(\mathbb R^d\). All mesh vertices are free nodal degrees of freedom, and \(V_h\) is the vector space of continuous, elementwise affine real symmetric \(m\times m\) tensor fields. The physical norm is \(\|U\|^2=\int_\Omega\|U(x)\|_F^2\,dx\). The Frobenius-nearest projection \(\pi_{[a,b]}\) onto \(\{X=X^\top:aI\preceq X\preceq bI\}\) acts by clipping eigenvalues. Define \(\mathcal C_h U=\sum_i \phi_i\pi_{[a,b]}(U(x_i))\), where \(\phi_i\) are nodal hat functions. The universal constant means the supremum over every such mesh, two distinct inputs, and the stated fixed matrix size \(m\); it is not a claim that each particular mesh attains the same constant.

## Proof

**1. Element mass matrix.** On a simplex \(K\) with \(n=d+1\) vertices, the consistent \(P_1\) mass matrix is
\[
M_K=\frac{|K|}{n(n+1)}(I_n+\mathbf1\mathbf1^\top).
\]
The irrelevant positive prefactor cancels in Lipschitz ratios. In coefficient space \(H^n\), \(H={\rm Sym}(m)\) with Frobenius inner product, set \(G=(I_n+\mathbf1\mathbf1^\top)\otimes I_H\). Its smallest and largest eigenvalues are \(1\) and \(\kappa=n+1\).

**2. An arbitrary pair of clipped fields reduces to a Euclidean positive contraction.** Metric projection onto a closed convex set in a Hilbert space is firmly nonexpansive. Hence, with input node difference \(u_i\) and output difference \(v_i\),
\[
\|v_i\|_F^2\le\langle u_i,v_i\rangle_F.
\]
If \(v_i\ne0\), define \(T_i=(v_i\otimes v_i)/\langle u_i,v_i\rangle_F\); otherwise take \(T_i=0\). Then \(T_i u_i=v_i\) and \(0\preceq T_i\preceq I_H\). Thus the output difference is \(Tu\) for a block-diagonal self-adjoint contraction \(0\preceq T\preceq I\). Its spectral-layer decomposition expresses it as an average of orthogonal projections, \(T=\int_0^1\mathbf1_{[t,1]}(T)\,dt\).

**3. Sharp universal metric change.** For any Euclidean orthogonal projection \(P\), the standard Kantorovich/Wielandt two-subspace estimate for a positive-definite metric whose spectral ratio is \(\kappa\) gives
\[
\|P\|_{G\to G}\le\frac{\kappa+1}{2\sqrt\kappa}.
\]
Indeed, if \(y\in\operatorname{ran}P\) and \(z\in\ker P\) are Euclidean-orthogonal, their metric correlation is at most \((\kappa-1)/(\kappa+1)\) in absolute value. Minimizing \(\|y+z\|_G\) over \(z\) therefore bounds the metric norm of the oblique decomposition by the reciprocal square root of \(1-((\kappa-1)/(\kappa+1))^2\). Integrate the projection bound in the spectral-layer decomposition and use the triangle inequality. This yields the single-element Lipschitz factor \((n+2)/(2\sqrt{n+1})\); summation over all elements yields the global inequality, without mesh regularity assumptions.

**4. Exact tensor sharpness by finite input pairs.** On a single simplex take the unit Frobenius tensor \(h=I_2/\sqrt2\), embedded into a leading \(2\times2\) block when \(m>2\). Let \(D_i\) be orthogonal projections of the tensor coefficient at node \(i\) such that \(\sum_iD_ih=(n/2)h\). If \(n\) is even, use \(n/2\) identity blocks and \(n/2\) zero blocks. If \(n=2k+1\) is odd, use \(k-1\) identities, \(k-1\) zero blocks, and three rank-one tensor projections \(D_jX=\langle X,q_j\rangle_Fq_j\), with \(q_j=u_ju_j^\top\) and
\[
u_1=(1,0),\quad u_2=(1/2,\sqrt3/2),\quad u_3=(-1/2,\sqrt3/2).
\]
The elementary frame identity \(\sum_jq_j=3I_2/2\) proves the required balancing. Put \(D=\operatorname{diag}(D_i)\), \(e=(h,\ldots,h)/\sqrt n\), \(z=2De-e\), and \(\delta=e/(n+1)+z\). The vectors \(e,z\) are Euclidean orthonormal, \(e\) belongs to the constant spatial eigenspace of \(G\), \(z\) to its orthogonal complement, and \(Dz=De\). Directly,
\[
\frac{\|D\delta\|_G^2}{\|\delta\|_G^2}=\frac{(n+2)^2}{4(n+1)}.
\]
Each selected block action is realized **exactly along the perturbation direction \(\delta\)** by spectral clipping between two finite nodal configurations: an interior scalar base for identity blocks, a strictly below-interval scalar base for zero blocks, and for the three rank-one blocks the base matrix \(((a+b)/2)q_j+(a-1)(I_2-q_j)\). Here the perturbation \(\delta_j\) commutes with \(q_j\), so clipping is exactly affine along that direction for every sufficiently small positive finite perturbation, not merely in a formal derivative. On the extra matrix coordinates, hold both fields fixed. Taking those two fields on a single simplex attains the claimed ratio.

**5. Scalar comparison and lumping.** Scalar clipping differences are multiplication by independent slopes in \([0,1]\) at each node. Convexity of the induced operator norm makes its maximum occur for slopes in \(\{0,1\}\). A selector with \(k\) active and \(n-k\) clipped nodes has exact squared consistent-mass operator norm \((k+1)(n-k+1)/(n+1)\). Maximization over integers \(0\le k\le n\) gives the scalar formula and exact finite clipping witnesses. For odd \(n\), the tensor squared factor exceeds the scalar squared factor by \(1/[4(n+1)]\), and otherwise they coincide. In the lumped mass norm, positive vertex weights and the nodewise Frobenius nonexpansivity prove modulus one; two fields whose eigenvalues stay inside \([a,b]\) attain one.

## Verification

The accompanying standalone `verify.py` checks the two-dimensional rank-one tensor frame identity and the required matrix mass-norm equality in exact symbolic arithmetic for spatial dimensions one through eight. It also evaluates actual two-by-two eigenvalue-clipping pairs at small, finite perturbations in dimension two. The analytic proof, not this finite set of checks, establishes all dimensions and all meshes. Run with `python verify.py` using Python, SymPy, and NumPy.

## Relationship to prior work

Amiri, Barrenechea, and Pryer (2026, arXiv:2601.04839) develop nodal eigenvalue-range-preserving finite elements for symmetric tensor fields; their variational and stability estimates motivate examining the exact consistent-mass sensitivity of a simpler projected-nodal operator. Barrenechea, Georgoulis, Pryer, and Veeser (2023, arXiv:2304.01067) study scalar nodal bound-preserving finite elements; their stability arguments and mass-lumping framework do not imply the present sharp tensor-versus-scalar constant. Lohmann (2019) considers tensor positivity mechanisms in algebraic flux correction, rather than the above nodewise Frobenius projection map. The Hilbert-space projection inequality and Kantorovich/Wielandt metric estimate used in the upper bound are established mathematics, not claimed as new. The new claim concerns exact attainability by spectral clipping under the restricted nodal structure and the strict scalar–tensor separation in even spatial dimensions.

## Limitations

The theorem assumes affine nodal interpolation, one common convex spectral interval, unconstrained vertices, exact symmetric eigenvalue clipping, and the physical consistent-mass \(L^2\) norm. It does not cover high-order elements, nonlinear tensor interpolation, arbitrary boundary constraints, or simultaneous energy-seminorm stability. It is a universal worst-case result; particular meshes or input ranges can have a smaller modulus. Historical priority is based on the specified searched sources and records, not an exhaustive global literature certificate.

## References

- Amiri, Barrenechea, and Pryer, *A finite element method preserving the eigenvalue range of symmetric tensor fields*, arXiv:2601.04839, initial public release 2026-01-08, https://arxiv.org/abs/2601.04839.
- Barrenechea, Georgoulis, Pryer, and Veeser, *A nodally bound-preserving finite element method*, arXiv:2304.01067, https://arxiv.org/abs/2304.01067.
- Lohmann, *On positivity preservation in finite element discretizations of systems of conservation laws*, ESAIM: M2AN (2019), https://www.numdam.org/item/10.1051/m2an/2019006.pdf.
- Kantorovich/Wielandt inequality for bounded positive-definite metrics (classical); only the specific metric-projection inequality is used.
