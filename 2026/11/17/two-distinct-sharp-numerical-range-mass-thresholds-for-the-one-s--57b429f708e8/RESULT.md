# Two distinct sharp numerical-range mass thresholds for the one-sided discrete Dirac operator

## Finding

Let \(S\) denote the bilateral right shift on \(\ell^2(\mathbb Z)\). For \(c>0\) and \(m\geq0\), consider the bounded complex-Hilbert-space operator
\[
D_{m,c}=-ic\,\sigma_1(I-S)+mc^2\sigma_3
\]
on \(\ell^2(\mathbb Z;\mathbb C^2)\), where \(\sigma_1=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\) and \(\sigma_3=\begin{psmallmatrix}1&0\\0&-1\end{psmallmatrix}\). Write \(M=mc^2\) and \(W(D)=\{\langle Df,f\rangle:\|f\|=1\}\). For every real \(\theta\), the support function of its **closed** numerical range is exactly
\[
h(\theta)=\max_{z\in\overline{W(D_{m,c})}}\operatorname{Re}(e^{-i\theta}z)
=\sqrt{M^2\cos^2\theta+c^2(1+|\sin\theta|)^2}.
\]
Thus \(\overline{W(D_{m,c})}=\bigcap_{\theta\in[0,2\pi)}\{z:\operatorname{Re}(e^{-i\theta}z)\leq h(\theta)\}\). The (uncentered) numerical radius \(w(D)=\sup_{z\in W(D)}|z|\) and the largest centered closed-disk radius \(r_0\) of \(\overline{W(D)}\) have **different sharp mass transitions**:
\[
w(D_{m,c})=\begin{cases}2c,&M\leq\sqrt2\,c,\\M^2/\sqrt{M^2-c^2},&M>\sqrt2\,c,\end{cases}
\qquad
r_0(D_{m,c})=\begin{cases}\sqrt{M^2+c^2},&M\leq\sqrt3\,c,\\2c,&M\geq\sqrt3\,c.\end{cases}
\]
The boundary of \(\overline{W(D)}\) has exactly two nondegenerate straight faces. They are vertical segments at
\[
\operatorname{Re}z=\pm\sqrt{M^2+c^2},\qquad
|\operatorname{Im}z|\leq\frac{c^2}{\sqrt{M^2+c^2}}.
\]
No boundary point is in \(W(D)\); in fact \(W(D)=\operatorname{int}\overline{W(D)}\).

## Assumptions and scope

The Hilbert space is complex; \(S\) is the **bilateral**, not unilateral, shift with \((Sf)_n=f_{n-1}\). Every statement holds simultaneously for all \(m\geq0\), \(c>0\), and all \(\theta\in\mathbb R\). The inradius \(r_0\) is centered at zero, which is natural because the numerical range is centrally symmetric; no statement is made about the radius of a disk with freely chosen center. The central disk of radius \(r_0\) lies in the closed numerical range; only its open interior is guaranteed inside the ordinary numerical range.

## Proof

Under the bilateral Fourier transform \(S\) becomes multiplication by \(e^{-ik}\), for \(k\in[-\pi,\pi)\). The operator is therefore unitarily equivalent to multiplication by the continuous matrix symbol
\[
F(k)=M\sigma_3+z(k)\sigma_1,\quad z(k)=-ic(1-e^{-ik})=c\sin k-ic(1-\cos k).
\]
The Hermitian part in any supporting direction has the exact form
\[
H_\theta(k)=\operatorname{Re}(e^{-i\theta}F(k))
=M\cos\theta\,\sigma_3+c(\sin(k+\theta)-\sin\theta)\sigma_1.
\]
The two real Pauli matrices anticommute and square to the identity, so the eigenvalues of \(H_\theta(k)\) are
\[
\pm\sqrt{M^2\cos^2\theta+c^2(\sin(k+\theta)-\sin\theta)^2}.
\]
For every fixed \(\theta\), the essential supremum over \(k\) of the positive eigenvalue is its maximum; the identity
\[
\max_k|\sin(k+\theta)-\sin\theta|=1+|\sin\theta|
\]
proves the asserted exact support function. Since the numerical range is convex (Toeplitz–Hausdorff), its closure is recovered as the intersection of those supporting half-planes.

To optimize the supporting function, put \(s=|\sin\theta|\in[0,1]\). Its square is
\[
Q(s)=M^2+c^2+2c^2s+(c^2-M^2)s^2.
\]
If \(M^2\leq2c^2\), \(Q\) is nondecreasing on \([0,1]\) and \(\max Q=4c^2\). If \(M^2>2c^2\), it is strictly concave with unique maximizing point \(s_*=c^2/(M^2-c^2)\in(0,1)\), and
\[
Q(s_*)=\frac{M^4}{M^2-c^2}.
\]
Taking square roots gives the numerical radius. For the minimum, when \(M^2\leq c^2\) the polynomial is increasing, and otherwise it is concave, so the minimum is always the smaller of \(Q(0)=M^2+c^2\) and \(Q(1)=4c^2\). Comparing them yields the second transition at \(M=\sqrt3\,c\), and \(r_0=\min_\theta h(\theta)\).

The only angles at which \(h\) is not differentiable are \(\theta=0\) and \(\theta=\pi\) modulo \(2\pi\), since \(|\sin\theta|\) is nonsmooth exactly there. At \(0\), the one-sided derivatives are \(h'_+(0)=c^2/\sqrt{M^2+c^2}\) and \(h'_-(0)=-c^2/\sqrt{M^2+c^2}\). The general subgradient description of support functions identifies the exposed face as the stated vertical segment at positive real coordinate. Central symmetry gives the other face. Differentiability elsewhere excludes any other nontrivial straight face.

Finally, for each \(\theta\), equality of the positive fiber eigenvalue with \(h(\theta)\) requires the sinusoid \(\sin(k+\theta)\) to take one of at most two prescribed extremal values. This occurs on a measure-zero set of Fourier frequencies. Hence the global positive operator \(h(\theta)I-\operatorname{Re}(e^{-i\theta}D)\) has trivial kernel, and no unit vector realizes a supporting-line equality. No point of \(\partial\overline{W(D)}\) therefore belongs to \(W(D)\). The support is strictly positive in every direction (indeed \(h(\theta)\geq c\)); consequently \(\overline{W(D)}\) has nonempty interior. The interior of the closure of a convex set with nonempty interior belongs to that convex set. Therefore \(W(D)=\operatorname{int}\overline{W(D)}\), as claimed.

## Verification

All identities follow from the exact Fourier symbol, the eigenvalue calculation, and elementary optimization of the single quadratic \(Q\). The independent finite checker `check_numerical_range.py` evaluates sampled Hermitian fiber eigenvalues against the proposed support function, checks the two extremal radius formulas on angular grids, and checks the one-sided support derivatives. Its successful output is `DIRAC_NUMERICAL_RANGE_DIAGNOSTICS_OK 2206`. Those finite tests corroborate formulas but are not proofs of the continuum statements, the absence of boundary eigenvectors, or the optimality of the thresholds.

## Relationship to prior work

Niwiński (2026) introduces this precise one-sided discrete Dirac operator and computes its operator norm, spectral radius, complex spectral curve, and resolvent convergence. The Fourier–Laurent matrix symbol is taken directly from that source; these existing results are not claimed as new. The present result supplies an **explicit complete numerical-range support function**, both sharp numerical-range radii and their distinct critical masses, a complete description of the two flat faces, and absence of numerical-range boundary attainment. This is a numerical-range calculation, not a replacement proof of the cited spectral results.

The general matrix-symbol approach to Toeplitz numerical ranges in Bebiano–Spitkovsky (2012), and subsequent banded biperiodic work of Bebiano–da Providência–Nata (2013), supplies a methodological antecedent: the numerical range of a matrix-symbol operator is controlled by the family of finite-dimensional symbol ranges. The present proof applies that established structural idea, performs the specific global optimization and determines the previously unreported paired mass thresholds for this Dirac family. Older exact treatments under a different operator or variable convention remain a possible priority risk.

## Limitations

The statement is restricted to the homogeneous one-dimensional bilateral one-sided Dirac operator. It does not cover a unilateral edge, variable mass, electric potentials, higher-dimensional lattice Dirac systems, or numerical pseudospectra. The result determines centered-disk geometry only; it gives no claim about optimal off-center disk embeddings. The finite checker is diagnostic rather than an infinite-dimensional certificate. Publication priority, including possible specialization of earlier general matrix-symbol formulas, has not been independently certified.

## References

1. M. Niwiński, *Spectral Theory and Continuum Norm Resolvent Convergence of a One-Sided Discrete Dirac-Type Operator* (2026), arXiv:2611.00820, first submitted October 31, 2026. https://arxiv.org/abs/2611.00820
2. N. Bebiano and I. M. Spitkovsky, *Numerical ranges of Toeplitz operators with matrix symbols*, Linear Algebra and its Applications 436 (2012), 1721–1726, doi:10.1016/j.laa.2011.06.019.
3. N. Bebiano, J. da Providência, and A. Nata, *The numerical range of banded biperiodic Toeplitz operators*, Journal of Mathematical Analysis and Applications 398 (2013), 189–197, doi:10.1016/j.jmaa.2012.08.029.
4. B. Randell, *Exploring the Numerical Range of Block Toeplitz Operators*, California Polytechnic State University master's thesis (2022), doi:10.15368/theses.2022.34.
