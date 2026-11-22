# A neutral spoke abolishes the real-spectrum threshold of a gain–loss quantum trimer

## Finding

A pair of balanced imaginary site potentials on opposite leaves of a weighted quantum star has an unexpectedly singular response to adding a passive spoke. When no passive spoke is coupled, the active trimer has an all-real spectrum for \(0\leq\gamma\leq\sqrt{2}t\) and a third-order exceptional point at \(\gamma=\sqrt{2}t\). Coupling even one neutral leaf with arbitrarily small **nonzero** hopping instead makes the spectrum nonreal at **every** \(\gamma>0\); the whole enlarged finite-dimensional Hamiltonian is diagonalizable at all such parameters and has no exceptional point.

More precisely, let the two active spoke hoppings equal \(t>0\), and let the passive spoke hoppings be real \(w_1,\dots,w_m\), with \(m\geq1\) and \(W=\sum_{j=1}^m w_j^2>0\). The entire spectrum consists of \(m-1\) zeros and four simple eigenvalues \(\pm\alpha,\pm i\beta\), where

\[
\alpha^2=\frac{S-\gamma^2+\sqrt{(S-\gamma^2)^2+4W\gamma^2}}2,\quad
\beta^2=\frac{-S+\gamma^2+\sqrt{(S-\gamma^2)^2+4W\gamma^2}}2,\quad S=2t^2+W.
\]

For every \(W,\gamma,t>0\) these numbers satisfy \(\alpha>0\) and \(0<\beta<\gamma\); for fixed \(t,\gamma>0\), \(\beta\) increases strictly from its uncoupled limit toward \(\gamma\) as \(W\) increases. At the uncoupled exceptional-point parameter \(\gamma=\sqrt{2}t\), the emerging four eigenvalues obey the *quarter-power-in-squared-hopping* law

\[
\alpha\sim\beta\sim(2t^2W)^{1/4}\qquad(W\downarrow0).
\]

Here \(W\) is the squared \(\ell^2\)-norm of the passive coupling vector: the same law is a square-root law in the passive hopping amplitude \(\sqrt W\). It does **not** describe a fourth-order exceptional point; the decoupled critical Hamiltonian has a size-three Jordan block and an additional independent zero mode.

## Assumptions and scope

The one-particle Hilbert space is \(\mathbb C^{m+3}\), with leaf basis \(e_+,e_-,f_1,\ldots,f_m\) and central basis \(c\). The finite matrix \(H=H(t,\gamma,w_1,\ldots,w_m)\) is defined by

\[
He_+=i\gamma e_++tc,\quad He_-=-i\gamma e_-+tc,\quad
Hf_j=w_jc,\quad Hc=t(e_++e_-)+\sum_{j=1}^m w_j f_j.
\]

All couplings are real, \(t>0\), \(\gamma\geq0\), and \(m\geq1\). For the uncoupled comparison, set \(m=0\), or equivalently split off the neutral zero modes when \(W=0\). The parity involution exchanges \(e_+\) and \(e_-\) and fixes all other basis vectors; combined with complex conjugation, it commutes with \(H\). Thus the spectrum is conjugation-symmetric, but parity-time invariance itself does not guarantee its reality. "All-real threshold" means the supremum of \(\gamma\geq0\) for which every eigenvalue is real; it does not assert diagonalizability at an endpoint.

## Proof

**1. Exact block decomposition.** Assume \(W>0\) and put \(f=W^{-1/2}\sum_j w_jf_j\). The \(m-1\)-dimensional passive-leaf subspace orthogonal to \(f\) is annihilated by \(H\). On \(\operatorname{span}\{e_+,e_-,f,c\}\), the matrix is

\[
B=\begin{pmatrix}
i\gamma&0&0&t\\
0&-i\gamma&0&t\\
0&0&0&\sqrt W\\
t&t&\sqrt W&0
\end{pmatrix}.
\]

A direct determinant expansion (or a polynomial Schur-complement identity) gives

\[
\det(\lambda I-B)=\lambda^4+(\gamma^2-2t^2-W)\lambda^2-W\gamma^2.
\]

**2. Exact spectrum, diagonalizability, and zero threshold.** When \(\gamma>0\), regard the quartic as a quadratic in \(y=\lambda^2\). Its constant term is \(-W\gamma^2<0\), so its two roots are strictly real, nonzero, and of opposite signs. They are respectively \(\alpha^2\) and \(-\beta^2\) as displayed in the finding. The four nonzero eigenvalues are pairwise distinct; every remaining zero belongs to the explicitly annihilated passive-leaf subspace. Hence the matrix is diagonalizable, and the spectral reality threshold is exactly zero. At \(\gamma=0\) the matrix is Hermitian and therefore also diagonalizable.

To prove the bound on imaginary growth, evaluate the quadratic \(p(y)=y^2+(\gamma^2-S)y-W\gamma^2\) at \(y=-\gamma^2\) and \(y=0\): \(p(-\gamma^2)=2t^2\gamma^2>0\), whereas \(p(0)=-W\gamma^2<0\). Its unique negative root therefore lies strictly between \(-\gamma^2\) and zero. For fixed \(t,\gamma\), the positive quantity \(x=\beta^2\) solves \(x^2+(S-\gamma^2)x-W\gamma^2=0\), and implicit differentiation gives

\[
\frac{dx}{dW}=\frac{\gamma^2-x}{2x+S-\gamma^2}>0.
\]

The denominator equals the strictly positive quadratic discriminant square root. Taking \(W\to\infty\) in the defining equation yields \(x\to\gamma^2\), while the lower endpoint \(W\downarrow0\) equals \(\max\{\gamma^2-2t^2,0\}\).

**3. Contrast with the uncoupled trimer.** On just \(e_+,e_-,c\), the uncoupled characteristic polynomial is

\[
\lambda(\lambda^2+\gamma^2-2t^2).
\]

Its eigenvalues are all real exactly for \(0\le\gamma\le\sqrt{2}t\). At \(\gamma=\sqrt{2}t\), the characteristic polynomial is \(\lambda^3\), and direct multiplication gives \(H_3^3=0\), \(\operatorname{rank}H_3=2\), \(\operatorname{rank}H_3^2=1\). Thus its only Jordan block has size three. Adding an uncoupled passive leaf contributes a one-dimensional, independent zero block. Any nonzero passive coupling, however small, produces the nonreal pair from Step 2 and removes every exceptional point of this real-parameter family.

**4. Singular weak-passive-coupling laws.** Put \(D=2t^2-\gamma^2\) and let \(W\downarrow0\) with \(t,\gamma>0\) fixed. If \(D>0\), the nonreal pair emerges from the semisimple zero eigenspace with

\[
\beta=\frac{\gamma}{\sqrt D}\sqrt W+O(W^{3/2}),\qquad \alpha=\sqrt D+O(W).
\]

If \(D<0\), it is instead the real pair that emerges from zero, while the old trimer's imaginary pair persists:

\[
\alpha=\frac{\gamma}{\sqrt{-D}}\sqrt W+O(W^{3/2}),\qquad \beta=\sqrt{-D}+O(W).
\]

At \(D=0\), the quartic is \(\lambda^4-W\lambda^2-2t^2W\). Substituting \(\lambda=(2t^2W)^{1/4}u\) yields \(u^4-1=O(\sqrt W)\), and the four roots tend to \(\{1,-1,i,-i\}\) on this rescaled level. This proves the displayed quarter-power law with the stated physical normalization. All remainder estimates here are at fixed positive \(t,\gamma\) away from the indicated critical alternative.

## Verification

The standalone `verify_star.py` reconstructs the three-site and four-site matrices independently, compares their symbolic characteristic polynomials, verifies the rank and nilpotency identities at the uncoupled exceptional point, and compares numerical eigenvalues of 108 independently assembled weighted-star matrices with the derived eigenvalue list. Tests range from three to eleven total leaves and include positive gain/loss strengths on both sides of the old trimer threshold. The program prints `PT_STAR_CHECKS_PASSED 108 symbolic_charpoly_and_Jordan_passed` on success. The infinite-family assertion is proved above; finite numerical checks provide supplementary diagnostics rather than an exhaustive proof.

## Relationship to prior work

Jin and Song (arXiv:0904.1513, first posted 2009-04-09) solve the end-gain/end-loss non-Hermitian **path** and establish an ordinary positive real-spectrum threshold and exceptional-point transition. The active three-site subsystem here is that familiar trimer; the claim made here is the discontinuity induced by a passive spoke and its complete weighted-star spectral classification.

Znojil (arXiv:1205.5211, first posted 2012-05-23; and arXiv:1411.3828, first posted 2014-11-14) studies **metric** stars with differential edge Hamiltonians and complex rotating Robin boundary conditions. Its degrees of freedom and boundary conditions differ from this finite adjacency matrix and its pair of on-site gain/loss leaves.

Agarwal, Pathak and Joglekar (arXiv:1802.00854, first posted 2018-02-02) show that coupling whole neutral chains to gain/loss chains can **raise** or suppress the threshold, including special plaquettes. Their fully specified models use extended coupled paths/plaquettes; the present theorem isolates the contrary threshold-collapse mechanism of neutral star spokes, with an explicit formula for every positive passive coupling norm and its singular weak-coupling laws.

Ge and Stone (arXiv:1402.0428, 2014, Sections II–III) already explain the general mechanism by which a gain–loss perturbation can split degenerate Hermitian modes into nonreal pairs at arbitrarily small strength, without a spectral exceptional point. Their results concern symmetry-class perturbation theory and wave-equation examples rather than this exact discrete weighted-star family; the general principle motivates, and qualitatively anticipates, the threshold collapse, so the thresholdless *mechanism itself is not claimed as new*. The claim here is instead a uniform all-gain/loss star classification, absence of nonzero-coupling exceptional points, exact amplitudes and the singular weak-spoke unfolding. Published index and primary-literature searches did not identify a broader theorem explicitly implying all these statements, but this is not a certification of historical priority.

## Limitations

Only a finite-dimensional one-particle tight-binding Hamiltonian with equal active hopping magnitudes and real passive hoppings is treated. The theorem does not extend without proof to arbitrary onsite real detunings, unequal active spokes (which generally break the stated parity symmetry), quantum many-body dynamics, scattering states, Lindblad evolution, or metric-graph boundary operators. The asymptotic formulas hold at fixed \(t,\gamma>0\) with passive squared-hopping strength \(W\downarrow0\). The eigensystem is not a normalized physical quantum probability evolution when non-Hermitian gain/loss is present. Published-priority research is bounded and independent external validation remains outstanding.

## References

1. L. Jin and Z. Song, *Solutions of PT symmetric tight-binding chain and its equivalent Hermitian counterpart*, arXiv:0904.1513 (first posted 2009-04-09), https://arxiv.org/abs/0904.1513.
2. M. Znojil, *Quantum star-graph analogues of PT-symmetric square wells*, arXiv:1205.5211 (first posted 2012-05-23), https://arxiv.org/html/1205.5211v3.
3. M. Znojil, *Quantum star-graph analogues of PT-symmetric square wells. II: Spectra*, arXiv:1411.3828 (first posted 2014-11-14), https://arxiv.org/html/1411.3828v1.
4. L. Ge and A. D. Stone, *Parity-Time Symmetry Breaking beyond One Dimension: The Role of Degeneracy*, arXiv:1402.0428 (first posted 2014-02-03), https://arxiv.org/abs/1402.0428.
5. K. S. Agarwal, R. K. Pathak and Y. N. Joglekar, *Raising the PT transition threshold by strong coupling to neutral chains*, arXiv:1802.00854 (first posted 2018-02-02), https://arxiv.org/abs/1802.00854.
