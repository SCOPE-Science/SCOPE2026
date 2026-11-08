# Exact two-band Hessian and isotropic weighting for minimal spherical two-designs

## Finding

For every integer \(d\ge3\), put \(N=d+1\). On the product of unit spheres \((S^{d-1})^N\), consider the unnormalized first-and-second-moment discrepancy
\[
\mathcal E_{a,b}(x_1,\ldots,x_N)
 =a\left\|\sum_{i=1}^N x_i\right\|^2
 +b\left\|\sum_{i=1}^N x_ix_i^{\mathsf T}-\frac Nd I_d\right\|_F^2,
 \qquad a,b>0.
\]
Every global minimum has value zero and is a regular simplex, up to orthogonal congruence. At any such minimum, the Riemannian Hessian, using the product of the standard round-sphere metrics, has **exactly** the following spectral bands, with multiplicities:
\[
\begin{array}{c|c}
\text{Hessian eigenvalue}&\text{multiplicity}\\\hline
0&d(d-1)/2\\
\lambda_{\mathrm{v}}=2a\frac{d^2-1}{d}+8b\frac{d+1}{d^2}&d\\
\lambda_{\mathrm{q}}=8b\frac{d+1}{d}&(d+1)(d-2)/2.
\end{array}
\]
The zero directions are precisely infinitesimal common rotations. Both positive bands exist for \(d\ge3\), so the condition number of the Hessian transverse to rotations is uniquely minimized, with optimal value \(1\), at the **dimension-dependent balancing ratio**
\[
\boxed{\frac ab=\frac4d.}
\]
At this ratio all positive eigenvalues coincide at \(8b(d+1)/d\): the moment-discrepancy landscape is exactly quadratically isotropic on the quotient by rotations. For equal weights \(a=b\), the least-curved sector is the \(d\)-dimensional vector sector in dimension \(3\), both sectors tie in dimension \(4\), and the quadratic sector is least-curved in every dimension \(d\ge5\).

## Assumptions and scope

All vectors and matrices are real. The number of equally weighted, ordered sample points is exactly \(d+1\), and each point lies on the unit sphere \(S^{d-1}\subset\mathbb R^d\). The weights \(a,b\) are strictly positive and multiply the **unnormalized** squared centroid and unnormalized squared covariance defect exactly as displayed. The matrix norm is Frobenius; the input metric is the unweighted product of unit-sphere metrics. The Hessian eigenvalues therefore change under a different normalization. The theorem concerns infinitesimal point displacements, not adjustments of the weights of individual quadrature nodes.

## Proof

**(1) Unique zero design.** A regular simplex \(u_1,\ldots,u_N\) obeys
\[
\sum_i u_i=0,\qquad \sum_i u_i u_i^{\mathsf T}=\frac Nd I_d,
\qquad u_i\cdot u_j=-\frac1d\quad(i\ne j).
\]
Hence it has zero discrepancy. Conversely, write \(X=[x_1\ \cdots\ x_N]\). If \(\mathcal E_{a,b}(X)=0\), then \(X\mathbf 1=0\) and \(XX^{\mathsf T}=(N/d)I_d\). Since \(\operatorname{rank}X=d\), the one-dimensional kernel is spanned by \(\mathbf1\); every nonzero eigenvalue of \(X^{\mathsf T}X\) is \(N/d\). Therefore
\[
X^{\mathsf T}X=\frac Nd\left(I_N-\frac1N\mathbf1\mathbf1^{\mathsf T}\right),
\]
which is the regular-simplex Gram matrix. Two such configurations differ by one orthogonal transformation.

**(2) Tangent-space coordinates.** Fix a regular simplex \(U=[u_1\ \cdots\ u_N]\). Let \(\operatorname{Sym}_0(d)\) denote real symmetric trace-zero matrices and \(\mathfrak{so}(d)\) skew-symmetric matrices. Every tangent family \(h_i\perp u_i\) has a unique representation
\[
h_i=\Omega u_i+A u_i-q_i u_i,
\qquad \Omega\in\mathfrak{so}(d),\quad A\in\operatorname{Sym}_0(d),\quad
q_i=u_i^{\mathsf T}A u_i.
\]
The map is injective: if all \(h_i\) vanish, then \((\Omega+A)u_i=q_i u_i\); summing over \(i\) gives \(\sum_iq_iu_i=0\), so all \(q_i\) are equal, because the only linear relation among the simplex columns is their sum. But \(\sum_iq_i=(N/d)\operatorname{tr}A=0\), whence all \(q_i=0\), and \(\Omega+A\) vanishes on a spanning set. Dimension counting then proves surjectivity. Rotational and symmetric tangent families are orthogonal for the product metric because \(\sum_i u_i u_i^{\mathsf T}=(N/d)I_d\).

Split \(\operatorname{Sym}_0(d)=V\oplus W\) orthogonally, where
\[
V=\left\{\sum_i\alpha_i u_i u_i^{\mathsf T}:\sum_i\alpha_i=0\right\},
\qquad
W=\left\{A\in\operatorname{Sym}_0(d):u_i^{\mathsf T}Au_i=0\text{ for every }i\right\}.
\]
The projector Gram matrix \(((u_i\cdot u_j)^2)_{ij}\) has eigenvalue \(1-1/d^2>0\) on \(\mathbf1^\perp\), so \(\dim V=d\). Its orthogonal complement has \(\dim W=(d+1)(d-2)/2\). Both are nonzero for \(d\ge3\).

**(3) Two differential norms.** The first derivatives of the two moment defects at \(U\) are
\[
Ds(h)=\sum_i h_i,
\qquad DQ(h)=\sum_i(h_i u_i^{\mathsf T}+u_i h_i^{\mathsf T}).
\]
Because both defects vanish at \(U\), the Riemannian Hessian quadratic form is exactly \(2a\|Ds(h)\|^2+2b\|DQ(h)\|_F^2\). The \(\Omega\) directions are its kernel.

For \(A\in W\) one has \(h_i=Au_i\), \(Ds(h)=0\), \(DQ(h)=2(N/d)A\), and \(\sum_i\|h_i\|^2=(N/d)\|A\|_F^2\). Thus the quadratic-form ratio on \(W\) is \(8bN/d\).

For \(A\in V\), express \(A=\sum_i\alpha_i u_i u_i^{\mathsf T}\) with \(\sum_i\alpha_i=0\), and set \(c=1-d^{-2}\). Then
\[
q_i=c\alpha_i,\quad \|A\|_F^2=c\sum_i\alpha_i^2,\quad
\sum_i\|h_i\|^2=\frac N{d^2}\|A\|_F^2.
\]
Furthermore,
\[
Ds(h)=-c\sum_i\alpha_i u_i,
\quad \|Ds(h)\|^2=\frac{cN}{d}\|A\|_F^2,
\quad DQ(h)=\frac{2N}{d^2}A.
\]
It follows that \(\|Ds(h)\|^2/\|h\|^2=(d^2-1)/d\) and \(\|DQ(h)\|_F^2/\|h\|^2=4N/d^2\), yielding \(\lambda_{\mathrm v}\). The differential images of \(V\) and \(W\) are mutually orthogonal in both measurement spaces, and the corresponding tangent spaces are orthogonal. Thus the quadratic-form ratios are actual eigenvalues, with exactly the asserted multiplicities. Positivity on \(V\oplus W\) excludes any additional zero modes.

**(4) Unique isotropic weighting.** The band difference factors as
\[
\lambda_{\mathrm v}-\lambda_{\mathrm q}
=\frac{2(d^2-1)}{d}\left(a-\frac{4b}{d}\right).
\]
Since both sectors occur, the ratio of largest to smallest positive eigenvalue equals one if and only if \(a/b=4/d\), proving uniqueness. Substitution gives the common eigenvalue. With \(a=b\), its sign changes precisely at \(d=4\). This finishes the proof.

## Verification

The accompanying standalone `check.py` verifies the symbolic band-difference identity, builds regular simplices in dimensions \(3\) through \(10\), computes the Hessian independently from the two moment Jacobians in orthonormal tangent coordinates, and compares all eigenvalues and multiplicities for five weighting pairs per dimension. It also checks two geodesic second-order expansions per dimension. Run with `python check.py` (requires NumPy and SymPy); the observed result is `SIMPLEX_MOMENT_CHECKS_PASS 130`. These finite checks corroborate the all-dimensional symbolic proof but are not a substitute for it.

## Relationship to prior work

The centroid and isotropic covariance criteria are standard characterizations of spherical two-designs; regular simplices are standard minimal examples. Sloan and Womersley (2009) developed variational characterizations of spherical designs. Xiao and Zhuang (first publicly posted March 9, 2023) developed general spherical-design objective, gradient, and Hessian machinery for numerical optimization and framelets. Their accessible abstract does not assert this particular two-band, all-dimension simplex spectrum or the balancing ratio; the complete text could not be checked and may contain relevant implicit calculations. Fu, Wang, and Yan (2022) study a different minimax energy based on absolute scalar products, not the squared centroid/covariance defect. The presently proved contribution is the **explicit transverse spectral decomposition and the unique perfectly conditioned relative weighting**, not the existence or uniqueness of the simplex two-design or generic Hessian differentiation.

## Limitations

This is a local quadratic stability and preconditioning result at the global minimizer, not a global convergence or iteration-complexity guarantee. It holds for exactly \(d+1\) equal-weight nodes and the displayed two-moment loss. It does not assert that arbitrary choices of the weights \(a,b\) preserve optimal conditioning for another loss, another input metric, or larger numbers of nodes. Although the proof is self-contained, historical priority of the exact Hessian calculation remains provisional because the most directly related 2023 paper's complete text was inaccessible. No independent mathematical validation has been performed.

## References

- Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365, first posted 2023-03-09; SIAM J. Imaging Sci. 16 (2023), 2072–2104; DOI: 10.1137/22M1542362.
- I. H. Sloan and R. S. Womersley, *A variational characterisation of spherical designs*, J. Approx. Theory 159 (2009), 308–318; DOI: 10.1016/j.jat.2009.02.014.
- W. Fu, G. Wang, and J. Yan, *On the minimax spherical designs*, Random Structures Algorithms 62 (2023), 131–154; first online 2022-04-19; DOI: 10.1002/rsa.21087.
