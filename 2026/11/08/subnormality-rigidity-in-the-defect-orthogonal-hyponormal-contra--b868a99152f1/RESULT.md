# Subnormality rigidity in the defect-orthogonal hyponormal contraction class

## Finding
Let \(T\) be a hyponormal contraction on a separable complex Hilbert space \(H\), and write \(\mathcal D_T=\overline{\operatorname{ran}}(I-T^*T)^{1/2}\), with \(\mathcal D_{T^*}\) defined analogously. Suppose
\[
\operatorname{ran}(T^*T-TT^*)\subseteq \mathcal D_{T^*}\ominus\mathcal D_T.
\]
Then the following conditions are equivalent:

1. \(T\) is subnormal (it has a normal extension on a larger Hilbert space).
2. The self-commutator \(T^*T-TT^*\) is an orthogonal projection.
3. \(T\) is unitarily equivalent to \((M_z\otimes I_{\mathcal E})\oplus N\), where \(\mathcal E\) is a Hilbert space (possibly zero) and \(N\) is a normal contraction.

The obstruction is local and quantitative: any nonunitary positive, injective step coupling produces a vector whose first five squared orbit norms have a strictly negative order-three Hankel determinant. No finite-rank assumption is made on the commutator or defect spaces.

## Assumptions and scope
All Hilbert spaces are complex; separability is assumed for application of the cited functional model. Hyponormal means \(T^*T\ge TT^*\); subnormal means \(T=N|_H\) for some normal operator on a larger space that leaves \(H\) invariant. The condition involves the **range** of the self-commutator, not merely its closure. The zero space and zero-multiplicity shift are allowed.

Write \(S=M_z\) for the Hardy-space unilateral shift. The functional model of Maji and Paramanik represents \(T\) as a normal summand and an operator on \(H^2_{\mathcal E_1}\oplus H^2_{\mathcal E_2}\) of the form
\[
\begin{pmatrix}S\otimes I_{\mathcal E_1}&P_0\otimes\widetilde D\\0&S^*\otimes D\end{pmatrix},
\]
where \(\mathcal E_2\) is isometrically embedded in \(\mathcal E_1\), \(D\) is a positive injective contraction on \(\mathcal E_2\), and the coupling identifies an isometric image of \(D\) inside \(\mathcal E_1\). The model's canonical coupled part has no positive spectral mass at \(D=I\); any unitary component can equivalently be put into the normal summand.

## Proof
**1. Split the coupled block.** Conjugate by a fixed unitary on the first multiplicity space so that \(\widetilde D\) has the form \(D\oplus0\). Splitting \(\mathcal E_1=\mathcal E_2\oplus(\mathcal E_1\ominus\mathcal E_2)\) decomposes the block into an uncoupled unilateral shift and
\[
B_D=\begin{pmatrix}S\otimes I_{\mathcal E_2}&P_0\otimes D\\0&S^*\otimes D\end{pmatrix}.
\]
Identify the first Hardy space with nonnegative indices and the second with negative indices in reverse order. Then \(B_D\) becomes the bilateral step shift \(W_D\) on \(\ell^2(\mathbb Z;\mathcal E_2)\):
\[
W_D(e_k\otimes v)=\begin{cases} e_{k+1}\otimes Dv,&k<0,\\e_{k+1}\otimes v,&k\ge0.\end{cases}
\]
The unitary conjugacy follows on each orthonormal coordinate, not just formally on matrices.

**2. A five-moment obstruction.** Suppose \(D\) is a positive injective contraction distinct from the identity. Then \(D^2-D^4\) is positive and nonzero. Choose a unit vector \(v\) for which \(a=\langle D^2v,v\rangle> b=\langle D^4v,v\rangle>0\). For \(x=e_{-2}\otimes v\), direct application of the two negative-side steps and then the unit steps gives
\[
(\|W_D^jx\|^2)_{j=0}^{4}=(1,a,b,b,b).
\]
The first three by three Hankel moment matrix has determinant
\[
\det\begin{pmatrix}1&a&b\\a&b&b\\b&b&b\end{pmatrix}=-b(a-b)^2<0.
\]
If \(W_D\) were subnormal, the normal extension would give \(\|W_D^jx\|^2=\int |z|^{2j}\,d\mu_x(z)\) for a finite positive measure \(\mu_x\); the displayed Hankel matrix would then be positive semidefinite, a contradiction. Subnormality passes to reducing summands, hence no nontrivial canonical coupled block can occur for subnormal \(T\). (If an identity summand of \(D\) is retained in a noncanonical representation, it yields a bilateral unitary, hence belongs to the normal part.) Thus (1) implies (3).

**3. Positive direction.** A unilateral shift is subnormal, since it extends to multiplication by the coordinate on a circle \(L^2\) space; a normal contraction is subnormal. Their orthogonal sum is subnormal. Thus (3) implies (1).

**4. Self-commutator test.** On \(W_D\), the self-commutator vanishes at all coordinates except \(k=0\), where it equals \(I-D^2\). On the uncoupled unilateral shift it is the projection onto the constants, and on a normal summand it is zero. Since \(D\) is positive and injective, \(I-D^2\) can be a projection only if \(D=I\): indeed \(D^2\) would be a projection with trivial kernel. The canonical model excludes an identity-coupled nonnormal sector, so (2) forces absence of any nontrivial coupled block, giving (3). Conversely the commutator of a shift plus a normal operator is the projection onto the shift's wandering subspace. This proves (2) equivalent to (3) and completes the theorem.

## Verification
The determinant identity can be checked by direct expansion. For the example \(D=\frac12 I\), \(a=1/4\), \(b=1/16\), and the determinant is \(-9/4096\). The analytic argument uses the full normal spectral measure rather than any finite truncation. All inequalities hold for general positive injective contractions, including operators with continuous spectrum and nonclosed range.

## Relationship to prior work
Maji–Paramanik's 2026 Theorem 3.1 supplies the infinite-dimensional model and is an essential input; that model theorem is **not** claimed as new here. Sneha B., Bala, and Sarkar's 2026 Theorem 5.2 gives a finite-rank version and identifies the projection-commutator shift-plus-normal case; this is also prior work. The finding classifies *subnormality* for the full defect-orthogonal hyponormal class, with a precise non-subnormal Hankel witness for every nontrivial coupled sector. The positive moment criterion is classical. The classification is a consequence of the cited model coupled with the additional moment obstruction, rather than a new representation theorem.

## Limitations
The range-containment hypothesis is essential to the scope; no classification of arbitrary hyponormal contractions is asserted. Normal-extension moment positivity is necessary, not sufficient in general, but one negative determinant suffices for the exclusion. The argument has not received independent mathematical validation or a comprehensive publication-priority assessment. Earlier equivalent formulations under the theory of weighted shifts or subnormal operators remain possible.

## References
1. A. Maji and S. Paramanik, *A functional model for hyponormal contractions*, arXiv:2610.35880v1, first publicly dated 27 August 2026, especially Theorem 3.1, https://arxiv.org/html/2610.35880v1.
2. Sneha B., N. Bala and J. Sarkar, *Hyponormal contractions and analytic shifts*, arXiv:2602.22636v1, first publicly dated 26 February 2026, especially Theorem 5.2, https://arxiv.org/html/2602.22636v1.
