# Variance universality and signed logarithmic Weyl laws for periodic Hilbert commutators

## Finding

Let \(H=(1/(j+k+1))_{j,k\ge0}\) be the classical Hilbert operator on \(\ell^2(\mathbb N_0)\), let \(q\ge2\) be an integer, and let \(p_0,\ldots,p_{q-1}\) be real numbers, periodically extended to \(p_n=p_{n\bmod q}\). Put
\[
\mu=\frac1q\sum_{r=0}^{q-1}p_r,\qquad
\sigma=\left(\frac1q\sum_{r=0}^{q-1}(p_r-\mu)^2\right)^{1/2}.
\]
For a real bounded sequence \(d\) satisfying
\[
\sum_{n=0}^\infty \frac{|d_n-p_{n\bmod q}|}{\sqrt{n+1}}<\infty,
\]
let \(D_de_n=d_ne_n\) and \(K_d=i(D_dH-HD_d)\). Then:

1. \(K_d\) is bounded and selfadjoint, and
\[
\sigma_{\mathrm{ess}}(K_d)=[-\pi\sigma,\pi\sigma],\qquad
\|K_d\|_{\mathrm{ess}}=\pi\sigma.
\]
2. When \(\sigma>0\), the absolutely continuous part of \(K_d\) is unitarily equivalent to \(\sigma H\oplus(-\sigma H)\). Thus its absolutely continuous spectral multiplicity is one almost everywhere on each open half-band \((0,\pi\sigma)\) and \((-\pi\sigma,0)\). When \(\sigma=0\), the absolutely continuous part is absent.
3. For the orthogonal projection \(P_N\) onto \(\operatorname{span}\{e_0,\ldots,e_{N-1}\}\), let \(n_{+,N}(t)\) count eigenvalues of \(P_NK_dP_N\), acting on that \(N\)-dimensional space, strictly greater than \(t\), and let \(n_{-,N}(t)\) count eigenvalues strictly below \(-t\). For every fixed \(t>0\),
\[
\lim_{N\to\infty}\frac{n_{+,N}(t)}{\log N}
=\lim_{N\to\infty}\frac{n_{-,N}(t)}{\log N}
=\begin{cases}
\pi^{-2}\operatorname{arcosh}(\pi\sigma/t),&0<t<\pi\sigma,\\
0,&t\ge\pi\sigma\ \text{or}\ \sigma=0.
\end{cases}
\]
For every \(N\) and every \(t>0\), the two counts are actually equal (without normalization).
4. For the exactly periodic sequence, the residue-class form of \(K_p\) is \(B\otimes H\) plus a trace-class remainder, with \(B\) of rank two if \(\sigma>0\) and rank zero if \(\sigma=0\). When \(q=2\) the remainder vanishes identically and \(K_p\) is unitarily equivalent to \(\sigma H\oplus(-\sigma H)\). In this two-class case, if \(\sigma>0\) the spectrum is purely absolutely continuous, equals \([-\pi\sigma,\pi\sigma]\), and there are no eigenvalues. If \(\sigma=0\) then \(K_p=0\) and its spectrum consists of the eigenvalue zero with infinite multiplicity. In both cases the norm is \(\pi\sigma\).

In particular, the essential band, absolutely continuous spectral type and leading signed finite-section counting functions depend on the periodic pattern only through its standard deviation; all finite-order arrangements with equal variance share these invariants.

## Assumptions and scope

The Hilbert matrix is indexed from zero, with entries \(1/(j+k+1)\); its norm and spectrum are \(\pi\) and \([0,\pi]\), respectively. The diagonal sequence is real and bounded, and only the displayed weighted \(\ell^1\) tail condition is imposed. The essential spectrum is the Fredholm/Calkin essential spectrum. The absolutely continuous description concerns only the absolutely continuous part; the theorem does **not** exclude additional isolated eigenvalues or singular spectral components for periods above two or for asymptotically periodic perturbations. The coefficient applies to any fixed positive threshold, not thresholds varying with \(N\).

## Proof

**Residue-class decomposition.** For exactly periodic \(p\), conjugate by the unitary
\(Ue_{qj+r}=e_r\otimes e_j\), where \(0\le r<q\) and \(j\ge0\). Define \(H_a=(1/(j+k+a))_{j,k\ge0}\) for \(a>0\). Direct substitution gives the \((r,s)\) block
\[
(UK_pU^*)_{rs}=\frac{i(p_r-p_s)}q H_{(r+s+1)/q}.
\]
Set \(B_{rs}=i(p_r-p_s)/q\) and \(R=UK_pU^*-B\otimes H\). This yields the exact expression
\[
R_{rs}=\frac{i(p_r-p_s)}q\bigl(H_{(r+s+1)/q}-H\bigr).
\]

**Trace-class lemma.** Every \(H_a-H\), for \(a>0\), is trace class. Indeed, writing \(v_x=(1,x,x^2,\ldots)\in\ell^2\) for \(0<x<1\), the rank-one Bochner integral
\[
H_a-H=\int_0^1(x^{a-1}-1)\,v_x\otimes v_x\,dx
\]
converges in trace norm, since its trace-norm integrand equals \(|x^{a-1}-1|/(1-x^2)\), integrable on \((0,1)\). The integrand has constant sign; hence
\[
\|H_a-H\|_1=\sum_{j=0}^\infty
\left|\frac1{2j+a}-\frac1{2j+1}\right|
=\frac12\left|\psi(a/2)-\psi(1/2)\right|.
\]
Here \(\psi\) is the digamma function. In particular, a finite sum of blocks makes \(R\) trace class, with the explicit bound
\[
\|R\|_1\le\frac1q\sum_{0\le r<s<q}|p_r-p_s|
\left|\psi\left(\frac{r+s+1}{2q}\right)-\psi(1/2)\right|.
\]
The bound follows by pairing symmetric off-diagonal blocks, each of norm equal to its scalar factor times the trace norm of \(H_a-H\).

**Rank-two variance reduction.** If \(\sigma>0\), set \(u=q^{-1/2}(1,\ldots,1)\) and \(v=(p_r-\mu)_{r=0}^{q-1}/(\sqrt q\,\sigma)\). They are orthonormal, and the matrix \(B\) satisfies
\[
Bu=i\sigma v,\qquad Bv=-i\sigma u,\qquad B|_{\{u,v\}^\perp}=0.
\]
Thus the nonzero eigenvalues of \(B\) are exactly \(+\sigma\) and \(-\sigma\), regardless of period and ordering. When \(\sigma=0\), \(B=0\) and \(K_p=0\). Consequently \(K_p\) is a trace-class perturbation of \(\sigma H\oplus(-\sigma H)\oplus0\), with the zero direct summand of multiplicity \(q-2\). The classical Hilbert spectral theorem, the Weyl essential-spectrum theorem and the Kato–Rosenblum theorem prove assertions 1 and 2 for \(p\).

**Asymptotically periodic sequences.** Put \(\varepsilon_n=d_n-p_{n\bmod q}\). The identity
\[
[D_d,H]-[D_p,H]=\sum_{n\ge0}\varepsilon_n
\bigl(|e_n\rangle\langle He_n|-|He_n\rangle\langle e_n|\bigr)
\]
converges in nuclear norm, because
\(\|He_n\|_2^2=\sum_{k\ge0}(n+k+1)^{-2}\le2/(n+1)\). Hence
\[
\|K_d-K_p\|_1\le2\sqrt2\sum_{n\ge0}\frac{|\varepsilon_n|}{\sqrt{n+1}}.
\]
The essential and absolutely continuous assertions persist under this selfadjoint trace-class perturbation.

**Signed logarithmic finite-section law.** At cutoff \(N=qM\), the residue unitary takes \(P_NK_pP_N\) exactly to
\(B\otimes H_M+E_MRE_M\) on \(\operatorname{ran}E_M\), where \(E_M=I_{\mathbb C^q}\otimes P_M\) and \(H_M\) is the first \(M\)-by-\(M\) Hilbert section. The perturbation has uniformly bounded trace norm. The same holds for \(K_d\), by the previous estimate. For general \(N\), the difference from the preceding multiple of \(q\) amounts to fewer than \(q\) added rows and columns, changing the number of eigenvalues above any fixed threshold by at most \(q-1\) by interlacing. If \(\sigma=0\) the model vanishes and the count above \(t\) is bounded by \(\|K_d\|_1/t\). If \(\sigma>0\), the eigenvalues of \(B\otimes H_M\) consist of one copy of \(+\sigma\lambda_j(H_M)\), one copy of \(-\sigma\lambda_j(H_M)\), and \((q-2)M\) zeros. Widom's Hilbert-section result, with normalization made explicit in Fedele (2019, equations (1.8)–(1.10)), gives
\[
\lim_{M\to\infty}\frac{\#\{j:\lambda_j(H_M)>u\}}{\log M}
=\pi^{-2}\operatorname{arcosh}(\pi/u),\quad0<u<\pi,
\]
with limit zero for \(u\ge\pi\). To transfer the density under a uniformly trace-class perturbation \(Q_M\), use the eigenvalue-count inequalities at thresholds \(t\pm\delta\): at most \(\|Q_M\|_1/\delta\) eigenvalues can be displaced across a fixed gap \(\delta>0\) without charge to the unperturbed count. Divide by \(\log M\), pass to the limit and then let \(\delta\downarrow0\). The Hilbert density is continuous at positive thresholds, including \(\pi\). Since \(\log\lfloor N/q\rfloor/\log N\to1\), the asserted formula follows. Finally, the matrix of every finite section of \(K_d\) is purely imaginary Hermitian. Complex conjugation sends it to its negative, so eigenvalues occur in exact positive–negative pairs and the signed counts agree for every \(N\).

**Special two-class case.** For \(q=2\), the only potentially nonzero blocks have \((r,s)=(0,1)\) or \((1,0)\), and \((r+s+1)/q=1\), so \(R=0\). If \(p_0\ne p_1\), the two nonzero scalar multiples of the Hilbert matrix have purely absolutely continuous spectrum and no point spectrum. If \(p_0=p_1\), \(D_p=p_0I\) and \(K_p=0\) on all of \(\ell^2\), so zero is an eigenvalue of infinite multiplicity.

## Verification

The accompanying `verify.py` checks the exact rational residue-block decomposition for 1,750 entries across five periodic patterns (including a constant pattern), and confirms Hermiticity and conjugate-paired eigenvalues of 15 finite sections. These are diagnostics, not a substitute for the trace-class and asymptotic arguments above. The proof invokes two classical external inputs: the Hilbert matrix's simple purely absolutely continuous spectrum and the Hilbert finite-section logarithmic counting law; their precise normalizations are specified above. Standard Weyl and Kato–Rosenblum perturbation theorems are used in their selfadjoint trace-class form.

For example, \(p=(1,0,-1)\) has \(\sigma=\sqrt{2/3}\), so every permitted asymptotically periodic perturbation has essential band \([ -\pi\sqrt{2/3},\pi\sqrt{2/3}]\) and the stated counting law with that \(\sigma\).

## Relationship to prior work

The Hilbert spectral diagonalization is classical (Magnus and Hill), with an accessible modern proof by Montes-Rodríguez and Virtanen (2024). Widom's Hilbert-section counting formula is reproduced and normalized by Fedele (2019), who additionally proves Hankel spectral-density results for piecewise continuous symbols. Pushnitski and Yafaev (2014) develop a more general spectral/scattering theory for selfadjoint Hankel operators with discontinuous symbols. The result here concerns a different operator: the commutator with a periodic **diagonal** operator, which is not generally a scalar Hankel matrix. The additional step is an explicit residue-block rank-two/trace-class reduction to two oppositely signed Hilbert channels, together with the uniform finite-section transfer under weighted summable deviations. The published broad Hankel literature provides plausible alternative formulations and is a standing priority risk.

## Limitations

The formula gives neither the complete spectrum nor absence of singular continuous or point spectrum for periods \(q\ge3\) or perturbed sequences. It does not establish convergence of finite-section outlier eigenvalues or rates in the \(o(\log N)\) error. The scalar Hilbert spectral and counting inputs are cited, not reproved from first principles. A historically earlier formulation in operator-valued Hankel or multichannel scattering language has not been ruled out independently.

## References

- E. Fedele, *The spectral density of Hankel operators with piecewise continuous symbols*, arXiv:1903.11572v1 (first public 27 March 2019), especially equations (1.8)–(1.10). https://arxiv.org/abs/1903.11572
- A. Montes-Rodríguez and J. A. Virtanen, *The Hilbert matrix done right*, arXiv:2411.07324v1 (first public 11 November 2024). https://arxiv.org/abs/2411.07324
- A. Pushnitski and D. Yafaev, *Spectral and scattering theory of self-adjoint Hankel operators with piecewise continuous symbols*, arXiv:1408.2361v1 (2014). https://arxiv.org/abs/1408.2361
- H. Widom, *Hankel matrices*, Transactions of the American Mathematical Society **121** (1966), Theorem 4.3; see the normalization correction discussed in Fedele (2019).
