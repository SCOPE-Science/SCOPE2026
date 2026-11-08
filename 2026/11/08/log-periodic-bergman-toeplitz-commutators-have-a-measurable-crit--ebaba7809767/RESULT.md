# Log-periodic Bergman Toeplitz commutators have a measurable critical singular trace

## Finding

Fix an integer \(d\ge1\), a Bergman weight \(\tau>-1\), and a nonconstant real trigonometric polynomial
\[
P(u)=\sum_{k=-K}^{K}c_ke^{ik\omega u},\qquad
\omega>0,\quad c_{-k}=\overline{c_k},\quad c_k\ne0\text{ for at least one }k\ne0.
\]
On the complex ball \(\mathbb B_d\), define the bounded radial symbol
\[
f(z)=P\!\left(\log\frac1{1-|z|^2}\right)
\]
and let \(C=[T_f,M_{z_1}]\) be the commutator of its Bergman Toeplitz operator and multiplication by the first coordinate. Set
\[
G(u)=\sum_{k=-K}^{K}c_k
\frac{\Gamma(\tau+1-ik\omega)}{\Gamma(\tau+1)}e^{ik\omega u},
\quad L=\frac{2\pi}{\omega},\quad
\mathsf R=\frac{\Gamma(1+d/2)}{\Gamma(3d/2)}
\frac1L\int_0^L|G'(u)|^d\,du.
\]
Then \(\mathsf R>0\); \(C\) is compact and belongs to the Schatten class \(\mathcal S_p\) **exactly for \(p>d\)**. At the critical dimension \(p=d\), \(C\) belongs to the weak class \(\mathcal S_{d,\infty}\) but not \(\mathcal S_d\), and the complete finite-degree cutoff trace satisfies
\[
\operatorname{Tr}\left(|C P_{\le M}|^d\right)=\mathsf R\log M+O_{d,\tau,P}(1)
\qquad(M\to\infty).
\]
Here \(P_{\le M}\) denotes orthogonal projection onto polynomials of total degree at most \(M\). More strongly, if \(s_1(C)\ge s_2(C)\ge\cdots\) are the ordered singular values, then
\[
\sum_{j=1}^{N}s_j(C)^d
=\frac{\mathsf R}{d}\log N+O_{d,\tau,P}(1).
\]
Thus \(|C|^d\) is **Dixmier measurable**: every normalized Dixmier trace of \(|C|^d\) equals \(\mathsf R/d\). The symbol has no radial boundary limit whenever \(P\) is nonconstant; the residue is nonetheless explicit.

For the particularly natural single oscillation \(P(u)=c+\cos u\), the value simplifies to
\[
\boxed{\mathsf R=\left|\frac{\Gamma(\tau+1-i)}{\Gamma(\tau+1)}\right|^d
\frac{\Gamma((d+1)/2)}{\sqrt\pi\,\Gamma(3d/2)}.}
\]
For the ordinary unweighted disk (\(d=1\), \(\tau=0\)) this gives \(\mathsf R=2\sqrt{\pi/\sinh\pi}/\pi\), and for the ordinary unweighted two-dimensional complex ball, \(\mathsf R=\pi/(4\sinh\pi)\). The additive constant \(c\) has no effect on the commutator.

## Assumptions and scope

The Hilbert space \(A^2_\tau(\mathbb B_d)\) comprises holomorphic functions square-integrable for the probability measure
\[
d\nu_{d,\tau}(z)=\frac{\Gamma(d+\tau+1)}{\pi^d\Gamma(\tau+1)}(1-|z|^2)^\tau\,dV(z).
\]
The bounded Toeplitz operator is \(T_fh=\Pi_\tau(fh)\), and \(M_{z_1}h=z_1h\). Both are bounded. The phase function \(P\) is a **finite** real Fourier sum; no assertion here extends to arbitrary measurable periodic profiles. The commutator is bounded and subsequently shown compact. The weak ideal uses \(\sup_{j\ge1}j^{1/d}s_j(C)<\infty\). A normalized Dixmier trace on positive \(\mathcal L^{1,\infty}\) agrees with the ordinary limit of the logarithmic Cesàro sums when that limit exists.

For \(\alpha=(\alpha_1,\ldots,\alpha_d)\in\mathbb N_0^d\), write \(m=|\alpha|\) and denote its normalized monomial by \(e_\alpha\). The following formulas fix the normalization and provide exact, not merely asymptotic, singular-value data.

## Proof

**Step 1: exact moment and weighted-shift formulas.** Unitary invariance of the measure makes the monomials an orthogonal basis. Their norms satisfy
\[
\|z^\alpha\|_{A^2_\tau}^2
=\frac{\alpha!\,\Gamma(d+\tau+1)}{\Gamma(m+d+\tau+1)}.
\]
Radiality makes \(T_f\) diagonal: \(T_fe_\alpha=\lambda_m e_\alpha\), where the beta integral gives
\[
\begin{aligned}
\lambda_m&=\frac{\int_0^1 t^{m+d-1}(1-t)^\tau
P(\log\frac1{1-t})\,dt}{B(m+d,\tau+1)}\\
&=\sum_{k=-K}^{K}c_k\frac{\Gamma(\tau+1-ik\omega)}{\Gamma(\tau+1)}
\frac{\Gamma(m+d+\tau+1)}{\Gamma(m+d+\tau+1-ik\omega)}.
\end{aligned}
\]
Also,
\[
M_{z_1}e_\alpha=\sqrt{\frac{\alpha_1+1}{m+d+\tau+1}}\,e_{\alpha+e_1}.
\]
Consequently
\[
Ce_\alpha=(\lambda_{m+1}-\lambda_m)
\sqrt{\frac{\alpha_1+1}{m+d+\tau+1}}\,e_{\alpha+e_1}.
\]
All output monomials are different, so these coefficients give **every** singular value, including multiplicity, without diagonalization approximations.

**Step 2: uniformly accurate oscillatory increment.** For each integer \(k\), let \(\zeta_k=ik\omega\) and
\[
U_k(m)=\frac{\Gamma(\tau+1-\zeta_k)}{\Gamma(\tau+1)}
\frac{\Gamma(m+d+\tau+1)}{\Gamma(m+d+\tau+1-\zeta_k)}.
\]
The gamma recurrence yields the exact difference
\[
U_k(m+1)-U_k(m)
=\frac{\zeta_k\,U_k(m)}{m+d+\tau+1-\zeta_k}.
\]
For each fixed \(k\), the gamma-ratio expansion gives \(U_k(m)=\Gamma(\tau+1-\zeta_k)m^{\zeta_k}/\Gamma(\tau+1)+O(m^{-1})\), with the usual bounded oscillatory factor implicit in the \(O\)-notation. Since the number of modes is finite,
\[
\Delta_m:=\lambda_{m+1}-\lambda_m
=\frac{G'(\log m)}m+O(m^{-2})\quad(m\ge1).
\]
In particular \(|\Delta_m|\le C/(m+1)\). This proves compactness, because the monomial-weighted-shift singular values converge to zero outside every finite-degree subspace. The function \(G\) is real and nonconstant: complex gamma has no zeros and the nonconstant Fourier coefficients of \(P\) survive the filter. Consequently \(\frac1L\int_0^L|G'|^p>0\) for every \(p>0\).

**Step 3: degree multiplicity and the sharp cutoff law.** For \(d\ge2\), group degree-\(m\) monomials by \(\alpha_1=j\): there are exactly \(\binom{m-j+d-2}{d-2}\) such monomials. Therefore, for every fixed \(p>0\),
\[
W_{m,p}:=\sum_{|\alpha|=m}
\left(\frac{\alpha_1+1}{m+d+\tau+1}\right)^{p/2}
=m^{d-1}\frac{\Gamma(1+p/2)}{\Gamma(d+p/2)}+O_{d,\tau,p}(m^{d-2}).
\]
Indeed this is a Riemann sum for \(x^{p/2}(1-x)^{d-2}/(d-2)!\) over \([0,1]\); the endpoint errors are \(O(m^{d-2})\). When \(d=1\), \(W_{m,p}=((m+1)/(m+\tau+2))^{p/2}=1+O(1/m)\), exactly matching the stated leading gamma quotient. Combining this with the increment formula and the estimate \(|\,|a+b|^d-|a|^d\,|\le C_d|b|\) for bounded \(a,b\), we obtain
\[
\sum_{|\alpha|=m}|\langle Ce_\alpha,e_{\alpha+e_1}\rangle|^d
=\frac{\Gamma(1+d/2)}{\Gamma(3d/2)}
\frac{|G'(\log m)|^d}{m}+O(m^{-2}).
\]
The \(O(m^{-2})\) is summable. The positive \(L\)-periodic function \(h(u)=|G'(u)|^d\) is Lipschitz (for \(d\ge1\)); comparison of \(\sum_{m\le M}h(\log m)/m\) with \(\int_1^M h(\log x)\,dx/x\) has uniformly bounded error. Substitution \(u=\log x\) gives \(\sum_{m\le M}h(\log m)/m=(L^{-1}\int_0^Lh)\log M+O(1)\). This yields the asserted cutoff trace. Similarly \(W_{m,p}\asymp m^{d-1}\) and the positive periodic phase average show that \(\sum_mW_{m,p}|\Delta_m|^p\) converges if and only if \(p>d\): for \(p=d\) divergence is logarithmic, whereas \(p<d\) each logarithmic-period block contributes a positive amount growing geometrically. The bound \(s_\alpha\le C/(m+1)\) and the \(O(m^d)\) count of degrees at most \(m\) prove the critical weak-ideal estimate.

**Step 4: sorted singular values and Dixmier measurability.** Write \(a_\alpha=|\langle Ce_\alpha,e_{\alpha+e_1}\rangle|^d\), \(N(M)=\binom{M+d}{d}\), \(S_M=\sum_{|\alpha|\le M}a_\alpha\), and let \(A_N\) be the sum of the \(N\) largest numbers \(a_\alpha\). Trivially \(A_{N(M)}\ge S_M\). We prove that a fixed number \(B>1\), independent of \(M\), satisfies \(A_{N(M)}\le S_{BM}\) for all sufficiently large \(M\).

Choose a closed phase interval where \(|G'|>2\eta>0\). For every large \(X\), the logarithmic period of degrees \([Xe^{-L},X]\) contains at least \(cX\) integers with \(|G'(\log m)|>\eta\). For each such \(m\), at least \(c'm^{d-1}\) multiindices have \(\alpha_1\ge m/2\) (for \(d=1\), there is one). By Step 2 and the shift coefficient, each corresponding \(a_\alpha\ge c''X^{-d}\). Hence, for some fixed sufficiently large \(A>1\), degrees at most \(AM\) supply at least \(N(M)\) numbers \(a_\alpha\ge c''(AM)^{-d}\). On the other hand the universal upper bound makes every \(a_\alpha\) of degree \(m>BM\) strictly smaller than this threshold as soon as the fixed \(B\) is chosen sufficiently larger than \(A\). The \(N(M)\) largest therefore all come from degrees at most \(BM\), as asserted. It follows from Step 3 that
\[
S_M\le A_{N(M)}\le S_{BM},\quad
S_{BM}-S_M=\mathsf R\log B+O(1),
\]
so \(A_{N(M)}=\mathsf R\log M+O(1)\). Since \(N(M)\asymp M^d\), monotonicity interpolates between adjacent \(N(M)\), with a bounded error: the difference \(A_{N(M+1)}-A_{N(M)}\) is bounded above by the corresponding cutoff difference up to the preceding comparison (or directly by the global \(O(1/M)\) bounds for the \(O(M^{d-1})\) newly indexed values). Therefore
\[
A_N=\frac{\mathsf R}{d}\log N+O(1),
\]
which is exactly the claimed sorted singular-value law. Dividing by \(\log N\) proves ordinary convergence of the normalized logarithmic partial sums for \(|C|^d\), hence every normalized Dixmier trace has the same value \(\mathsf R/d\).

**Step 5: the cosine formula.** For \(P(u)=c+\cos u\), \(G'(u)=-R_{\tau}\sin(u+\vartheta)\), where \(R_{\tau}=|\Gamma(\tau+1-i)|/\Gamma(\tau+1)\). The elementary beta integral yields \((2\pi)^{-1}\int_0^{2\pi}|\sin u|^ddu=\Gamma((d+1)/2)/(\sqrt\pi\,\Gamma(1+d/2))\), giving the displayed special constant. All parameters have remained fixed throughout the asymptotics.

## Verification

The accompanying standalone `CHECK.py` uses `mpmath` high-precision arithmetic to compare the exact beta-moment integrals against their gamma-ratio representations at several dimensions, weights, frequencies, and degrees; checks the exact gamma recurrence; tests the predicted large-degree increment and beta-multiplicity leading coefficient; and independently verifies the single-cosine residue simplification. Run `python -m pip install -r requirements.txt` followed by `python CHECK.py` in the directory containing those two files. Finite checks do not prove the infinite spectral classification, logarithmic cutoff law, or Dixmier measurability; these follow from the analytic arguments above.

## Relationship to prior work

Looi's 2026 radial Toeplitz counterexample computes the log-periodic eigenvalue profile and contrasts it with Berezin averages; this supplies the motivated symbol and its elementary beta-moment structure. The present claim concerns instead the critical weak-Schatten decay and **sorted singular trace of its commutator with a coordinate multiplier**, across every dimension and power Bergman weight. In their 2007/2009 account, Engliš, Guo and Zhang calculate Dixmier traces of products of Toeplitz commutators for **symbols smooth up to the boundary** by a boundary Poisson bracket. These hypotheses do not cover the symbol here, whose radial limit oscillates indefinitely. Bendaoud, Kupin, Toumache, Touré and Zarouf (2020) develop Schatten tests for **radial Toeplitz operators themselves**, rather than the coordinate commutator considered here. Classical beta integrals, gamma ratios and counting arguments are not claimed as new mathematical ingredients.

## Limitations

The theorem is restricted to a bounded, nonconstant **finite trigonometric log-radial profile**, a fixed coordinate multiplier, the standard positive power weights on the complex ball, and total-degree cutoffs. A general periodic or nonperiodic bounded profile might have a different singular-trace behavior. The assertion of originality is limited to the inspected sources and search comparisons; equivalent formulations in older operator-ideal literature cannot be excluded. No independent mathematical audit has been performed.

## References

1. S. Looi, *Positive Berezin liminf does not imply essential positivity for radial Toeplitz operators on Bergman and Fock spaces*, arXiv:2603.10879 (first public posting 2026-03-11), https://arxiv.org/html/2603.10879.
2. M. Engliš, K. Guo and G. Zhang, *Toeplitz and Hankel operators and Dixmier traces on the unit ball of \(\mathbb C^n\)*, arXiv:0707.2025, https://arxiv.org/pdf/0707.2025.
3. Z. Bendaoud, S. Kupin, K. Toumache, B. Touré and R. Zarouf, *Toeplitz Operators with Radial Symbols on Bergman Space and Schatten-von Neumann Classes*, Journal of Mathematical Physics, Analysis, Geometry **16** (2020), 3–26, doi:10.15407/mag16.01.003.
