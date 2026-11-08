# Exact spectral staircases for periodic narrow-arc Fourier observation

## Finding

Fix an integer \(q\geq1\) and a finite nonempty set \(\Lambda\subset\mathbb Z\). On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let
\[
E_{q,\alpha}=\bigcup_{h=0}^{q-1}\{t:|t-2\pi h/q|_{\mathbb T}<\alpha\},\qquad 0<\alpha<\pi/q,
\]
and let \(C_{\Lambda,q,\alpha}\) be the concentration operator on \(V_\Lambda=\operatorname{span}\{e^{ikt}:k\in\Lambda\}\), with the ambient norm \(\|f\|^2=(2\pi)^{-1}\int_{\mathbb T}|f|^2dt\). Precisely, \(\langle Cf,g\rangle=(2\pi)^{-1}\int_{E_{q,\alpha}}f\overline g\,dt\).

For every occupied residue class \(r\pmod q\), write its frequencies uniquely as \(r+q n\), with distinct integers \(n\) forming a set \(N_r\) of size \(L_r\). For \(0\le j\le L_r\), define the real moment matrix
\[
H_{r,j}=\left(\sum_{n\in N_r}n^{a+b}\right)_{0\le a,b<j},\qquad \det H_{r,0}=1,
\]
and for \(0\le j<L_r\) put
\[
W_{r,j}=\frac{\det H_{r,j+1}}{\det H_{r,j}}>0,\qquad
c_{r,j}=\frac{2^{2j}W_{r,j}}{\pi(2j+1)(j!)^2\binom{2j}{j}^2}.
\]
**Complete spectral staircase:** The entire multiset of eigenvalues of \(C_{\Lambda,q,\alpha}\) is the union, over occupied \(r\), of \(L_r\) positive eigenvalues \(\lambda_{r,0}\ge\cdots\ge\lambda_{r,L_r-1}\) satisfying, for fixed \(q,\Lambda\) as \(\alpha\downarrow0\),
\[
\boxed{\lambda_{r,j}(\alpha)\sim c_{r,j}(q\alpha)^{2j+1},\quad 0\le j<L_r.}
\]
Thus exactly \(\#\{r:L_r>j\}\) eigenvalues have decay order \((q\alpha)^{2j+1}\), with every individual coefficient explicitly determined by integer-frequency moment determinants. The matching restriction singular values are the positive square roots.

Let \(L=\max_rL_r\). If \(L\ge2\), set \(c_*=\min_{r:L_r=L}c_{r,L-1}\). Then
\[
\boxed{\kappa(C_{\Lambda,q,\alpha})\sim\frac{L}{\pi c_*}(q\alpha)^{-2(L-1)}.}
\]
Here \(\kappa\) is the spectral eigenvalue ratio, whereas the restriction operator has singular-value condition number \(\sqrt{\kappa}\). If \(L=1\), one has the exact identity \(C_{\Lambda,q,\alpha}=(q\alpha/\pi)I\) for **every** \(0<\alpha<\pi/q\). Conversely, such an identity for every admissible \(\alpha\) requires all frequencies to be distinct modulo \(q\).

For example, with \(q=3\) and \(\Lambda=\{0,1,2,3,4,6\}\), the occupied residue multiplicities are \((3,2,1)\), and the sharp loss is
\[
\lambda_{\min}\sim\frac{2}{135\pi}(3\alpha)^5,\qquad
\lambda_{\max}\sim\frac{3}{\pi}(3\alpha),\qquad
\boxed{\kappa(C_{\Lambda,3,\alpha})\sim\frac52\alpha^{-4}.}
\]

## Assumptions and scope

The result holds for **every** fixed positive integer \(q\), every fixed finite nonempty subset \(\Lambda\subset\mathbb Z\) without repeated frequencies, and every sufficiently small positive arc half-width \(\alpha<\pi/q\). The classes \(r\) are occupied residues only. All determinants are finite and strictly positive for the stated \(j\), by the rank of the real Vandermonde matrix of distinct integers \(N_r\). The implicit \(o(1)\) errors may depend on the fixed frequency set and \(q\); no bound uniform in growing frequency apertures is claimed. No special choice of the center phase is needed because a common rotation unitarily conjugates the operator.

## Proof

**1. Exact cyclic reduction.** In the ambient orthonormal Fourier basis, for \(k,\ell\in\Lambda\) the Gram entry equals
\[
\frac1{2\pi}\sum_{h=0}^{q-1}e^{i(\ell-k)2\pi h/q}\int_{-\alpha}^{\alpha}e^{i(\ell-k)u}\,du.
\]
The finite root-of-unity sum is zero unless \(k\equiv\ell\pmod q\). In a fixed residue class write \(k=r+qn\), \(\ell=r+qm\), and change variables \(v=qu\). The corresponding block is **exactly** the Gram matrix of the functions \(e^{inv}\), \(n\in N_r\), on the single interval \([-\beta,\beta]\), with \(\beta=q\alpha\) and measure \(dv/(2\pi)\). There is no approximation in this step. Distinct exponentials are linearly independent on every nonempty interval, proving positivity.

**2. Exterior-power small-window lemma.** Fix any \(L\) distinct real numbers \(n_1,\ldots,n_L\) and put \(T_\beta:\mathbb C^L\to L^2([-1,1],ds)\),
\[
T_\beta c(s)=\sqrt{\frac\beta{2\pi}}\sum_{h=1}^L c_h e^{i\beta n_hs}.
\]
Let \(v_a=(n_1^a,\ldots,n_L^a)\) in coefficient space and \(p_a(s)=s^a\). Its convergent rank-one expansion is
\[
T_\beta=\sqrt{\frac\beta{2\pi}}\sum_{a=0}^\infty\frac{(i\beta)^a}{a!}\,p_a\otimes v_a^*.
\]
For each \(0\le j<L\), the first nonzero coefficient of the exterior-power map \(\bigwedge^{j+1}T_\beta\) uses the **distinct** Taylor degrees \(0,1,\ldots,j\). Indeed, a repeated degree makes an output exterior product vanish, and any different set of distinct nonnegative degrees has strictly larger total degree. This leading term is a nonzero rank-one exterior operator, and hence its operator norm is asymptotic to
\[
\left(\frac\beta{2\pi}\right)^{(j+1)/2}\frac{\beta^{j(j+1)/2}}{\prod_{a=0}^j a!}\,
\left\|v_0\wedge\cdots\wedge v_j\right\|
\left\|p_0\wedge\cdots\wedge p_j\right\|.
\]
This follows in operator norm because the rank-one power series converges for fixed nodes. The norm of an exterior power is the product of the corresponding largest singular values; division by the expression at \(j-1\) gives the sharp individual singular-value coefficient. The squared norm ratio of the coefficient wedges is \(\det H_{j+1}/\det H_j\). The squared norm ratio of the output wedges is the minimum squared \(L^2([-1,1])\)-norm of a **monic** degree-\(j\) polynomial.

**3. Legendre normalization and exact coefficient.** The normalized Legendre polynomial \(P_j\) has leading coefficient \(2^{-j}\binom{2j}{j}\) and squared norm \(2/(2j+1)\). Thus the monic orthogonal polynomial has squared norm
\[
\frac{2}{2j+1}\left(\frac{2^j}{\binom{2j}{j}}\right)^2.
\]
Combining this with the \(1/j!\) from the Taylor coefficient and the \(1/(2\pi)\) measure yields precisely \(c_{r,j}\). This proves all eigenvalue asymptotics, not just an extremal bound.

**4. Condition number and rigidity.** The leading eigenvalue in a block of size \(L_r\) is \((L_r/\pi)\beta\), while its smallest is order \(\beta^{2L_r-1}\). The largest residue-class size therefore determines both global extremes; among equally large classes the smallest \(c_{r,L-1}\) determines the global minimum. If every class has size one, each diagonal block is the scalar \(\beta/\pi\). If some class has at least two frequencies \(n\ne m\), its off-diagonal entry \(\sin((n-m)\beta)/[\pi(n-m)]\) is not identically zero as \(\beta\) varies. The condition-number and exact-tightness statements follow. Finally, for the displayed example, the three-size block has \(c_2=2/(135\pi)\), giving the stated constant \(5/2\) after substituting \(\beta=3\alpha\).

## Verification

Run \(\texttt{python3 repro/check_periodic_windows.py}\) with Python 3 and the \(\texttt{mpmath}\) package. The supplied script independently constructs concentration Gram matrices, numerically integrates representative Fourier matrix entries over all the arcs, computes moment-determinant constants and spectra at high precision, tests the exact cyclic block reduction, tests the barycentric identity at the last spectral level, and checks the limiting example. It reports \(\texttt{PERIODIC_FOURIER_STAIRCASE_CHECKS_PASS 134}\) when all assertions pass. These finite computations corroborate, but do not substitute for, the exterior-power proof covering all fixed finite frequency sets.

## Relationship to prior work

Classical Slepian concentration theory treats single-band/single-interval Fourier restriction and its prolate spectrum. The work of Batenkov, Demanet, Goldman, and Yomdin (arXiv:1809.00658, Sections 2–4) establishes optimal **scaling bounds** in clustered Fourier Vandermonde problems, rather than exact constants for the present periodic-arc operator. Batenkov, Diederichs, Goldman, and Yomdin (arXiv:1909.01927, Theorems 2.2–2.3, proof in Section 4) identify the **orders** of an entire clustered singular spectrum by Taylor/moment arguments, but do not state the explicit monic-Legendre determinant coefficients and exact root-of-unity decomposition for arbitrary sparse frequency sets. Batenkov and Goldman (arXiv:2107.09326, Theorems 2.3 and 7.1–7.3) further supply lower bounds and clustered-spectral order estimates, not this exact arithmetic staircase. Karnik, Romberg, and Davenport (arXiv:2006.00427) give nonasymptotic prolate transition-region bounds in a different asymptotic regime. The full-text comparisons make these papers close in method and motivation but do not establish implication of the stated exact formula.

For two arcs and a consecutive symmetric frequency band, the theorem specializes to the leading coefficient of the least eigenvalue, but that narrow subcase alone does not determine the new theorem. The statement treats **every** sparse frequency mask, **any** cyclic observation multiplicity, all spectral levels, and their exact arithmetic constants. Divided differences and Legendre orthogonality are standard tools, and their separate ingredients are not claimed to be new.

## Limitations

The problem is a continuous, noiseless restriction problem with fixed finite Fourier support and exact periodic arc geometry. There is no theorem for jittered centers, unequal arc widths, growing \(q\) or frequency supports, or nonlinear phaseless measurements. The result does not optimize the frequency selection itself. Algebraically equivalent results may be implicit in classical confluent-Vandermonde singular-perturbation literature; mathematical originality and priority remain subject to independent historical checking.

## References

1. D. Batenkov, L. Demanet, G. Goldman, and Y. Yomdin, *Conditioning of partial nonuniform Fourier matrices with clustered nodes* (2018 preprint), arXiv:1809.00658, https://arxiv.org/abs/1809.00658.
2. D. Batenkov, B. Diederichs, G. Goldman, and Y. Yomdin, *The spectral properties of Vandermonde matrices with clustered nodes* (2019 preprint), arXiv:1909.01927, https://arxiv.org/abs/1909.01927.
3. D. Batenkov and G. Goldman, *Single-exponential bounds for the smallest singular value of Vandermonde matrices in the sub-Rayleigh regime* (2021 preprint), arXiv:2107.09326, https://arxiv.org/abs/2107.09326.
4. S. Karnik, J. Romberg, and M. A. Davenport, *Improved bounds for the eigenvalues of prolate spheroidal wave functions and discrete prolate spheroidal sequences* (2020 preprint), arXiv:2006.00427, https://arxiv.org/abs/2006.00427.
