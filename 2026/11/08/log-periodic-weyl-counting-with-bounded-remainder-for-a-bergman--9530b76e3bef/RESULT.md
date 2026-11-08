# Log-periodic Weyl counting with bounded remainder for a Bergman Toeplitz commutator

## Finding

Fix \(\alpha>-1\), \(\tau>0\), and \(0<b<(1+\tau)^{-1}\). On the standard weighted analytic Bergman Hilbert space \(A^2_\alpha(\mathbb D)\), define
\[
\gamma_\alpha(v)=\frac{\Gamma(\alpha+1+iv)}{\Gamma(\alpha+1)},\qquad
f_{\alpha,\tau,b}(z)=\frac{(1-|z|^2)^{i\tau}}{\gamma_\alpha(\tau)}+
\frac{b(1-|z|^2)^{2i\tau}}{2\gamma_\alpha(2\tau)}.
\]
The powers use the real logarithm on \((0,1)\); boundary values on the unit circle are immaterial. Let \(P_\alpha\) be the Bergman projection, \(T_f=P_\alpha M_f|_{A^2_\alpha}\), \(S=M_z\), and \(K=[T_f,S]=T_fS-ST_f\). Write \(N_K(s)=\#\{j:s_j(K)>s\}\) for \(s>0\), where singular values are counted with multiplicity.

For each \(\theta\in\mathbb R\), there is a **unique** positive solution \(H_{\tau,b}(\theta)\) of
\[
H_{\tau,b}(\theta)=\tau\left|1+b\exp\bigl(-i[\theta+\tau\log H_{\tau,b}(\theta)]\bigr)\right|.
\]
The function \(H_{\tau,b}\) is continuous and \(2\pi\)-periodic, takes every value in \([\tau(1-b),\tau(1+b)]\), and is not constant. The singular-value counting function satisfies the **uniform bounded-remainder law**
\[
\boxed{\displaystyle N_K(s)=\frac{H_{\tau,b}(\tau\log(1/s))}{s}+O_{\alpha,\tau,b}(1)}
\qquad(s\downarrow0).
\]
Consequently,
\[
\boxed{\displaystyle\liminf_{s\downarrow0}sN_K(s)=\tau(1-b),\qquad
\limsup_{s\downarrow0}sN_K(s)=\tau(1+b).}
\]
Thus \(sN_K(s)\) has no limit despite the compactness of \(K\). Nevertheless \(K\in\mathcal S_p\) exactly for \(p>1\), and \(K\in\mathcal S_{1,\infty}\setminus\mathcal S_1\). The positive operator \(|K|\) is Dixmier-measurable: every normalized Dixmier trace gives the same value
\[
\boxed{\displaystyle\operatorname{Tr}_{\omega}(|K|)
=\lim_{J\to\infty}\frac{1}{\log J}\sum_{j=1}^{J}s_j(K)
=\frac{\tau}{2\pi}\int_0^{2\pi}\!|1+b e^{i\theta}|\,d\theta.}
\]
Equivalently, the final constant is \(2\tau(1+b)E(4b/(1+b)^2)/\pi\), where \(E(m)=\int_0^{\pi/2}\sqrt{1-m\sin^2 u}\,du\) is the complete elliptic integral of the second kind (parameter convention). The sharp counting envelopes and the logarithmic trace are independent of \(\alpha\) because the chosen Mellin normalization fixes the two asymptotic spectral amplitudes.

## Assumptions and scope

The measure defining \(A^2_\alpha\) is \((\alpha+1)(1-|z|^2)^\alpha dA(z)\), with normalized area \(dA=dx\,dy/\pi\). Its normalized monomial basis is
\[
e_n(z)=\sqrt{\frac{\Gamma(n+\alpha+2)}{\Gamma(\alpha+2)\,\Gamma(n+1)}}z^n,\qquad n=0,1,2,\ldots .
\]
The radial symbol \(f_{\alpha,\tau,b}\) is bounded but generally has no pointwise radial limit at the boundary. The parameter restriction \(b<(1+\tau)^{-1}\) ensures a strict radial monotonicity in the limiting counting threshold. The theorem concerns a *two-frequency* symbol and the commutator with coordinate multiplication, not arbitrary radial Toeplitz commutators. \(\operatorname{Tr}_\omega\) denotes any usual normalized Dixmier trace on the weak trace ideal; only positive \(|K|\) is traced.

## Proof

**1. Exact diagonal moment calculation.** Radiality makes \(T_f\) diagonal on the monomial basis. Put \(q_n=n+\alpha+2\) and \(R_v(n)=\Gamma(q_n)/\Gamma(q_n+iv)\). The Euler beta integral gives, for every \(n\ge0\),
\[
T_fe_n=\lambda_ne_n,\qquad
\lambda_n=R_\tau(n)+\tfrac b2R_{2\tau}(n).
\]
Indeed, for the symbol \((1-|z|^2)^{iv}\), the normalized moment is exactly \(\gamma_\alpha(v)R_v(n)\). The multiplication operator is a weighted unilateral shift:
\[
Se_n=w_ne_{n+1},\qquad w_n=\sqrt{\frac{n+1}{n+\alpha+2}}.
\]
The gamma recurrence yields the *exact* identity
\[
R_v(n+1)-R_v(n)=-\frac{iv}{q_n+iv}R_v(n).
\]
Thus \(Ke_n=d_ne_{n+1}\), where
\[
d_n=-i\tau w_n\left(\frac{R_\tau(n)}{q_n+i\tau}
+b\frac{R_{2\tau}(n)}{q_n+2i\tau}\right).
\]
Because the ranges of the different columns of this shift are orthogonal, \(K^*Ke_n=|d_n|^2e_n\), and its singular values are precisely the nonincreasing rearrangement of \(a_n=|d_n|\), \(n\ge0\). There is no unproved spectral decomposition here.

**2. Sharp model and uniform remainder.** The classical fixed-parameter gamma-ratio expansion is
\[
R_v(n)=n^{-iv}\bigl(1+O_{\alpha,v}(n^{-1})\bigr),\qquad
w_n=1+O_\alpha(n^{-1}).
\]
It follows that, uniformly for integers \(n\ge1\),
\[
\boxed{\displaystyle a_n=\frac{\tau}{n}|1+b e^{-i\tau\log n}|+O_{\alpha,\tau,b}(n^{-2}).}
\]
Here and below the finitely many small indices may be absorbed into constants. In particular \(a_n\to0\), proving compactness, and for sufficiently large \(n\),
\[
\frac{\tau(1-b)}{2n}\le a_n\le\frac{2\tau(1+b)}n.
\]
The latter inequalities already prove the exact Schatten cutoff and weak trace-class membership.

**3. Unique threshold root.** Set \(A=\tau(1-b)\), \(B=\tau(1+b)\) and \(g_\theta(t)=\tau|1+b e^{-i(\theta+\tau\log t)}|\) for \(t>0\). Then \(A\le g_\theta(t)\le B\). The Lipschitz constant of \(u\mapsto|1+b e^{iu}|\) does not exceed \(b\), so on \([A,B]\) the derivative of \(g_\theta\), wherever evaluated, satisfies
\[
|g_\theta'(t)|\le\frac{\tau^2b}{t}\le\frac{\tau b}{1-b}<1.
\]
The function \(t-g_\theta(t)\) changes sign between \(A\) and \(B\) and is strictly increasing there, hence has exactly one zero \(H_{\tau,b}(\theta)\). For all \(t>0\), the sign of \(t-g_\theta(t)\) agrees with the sign of \(t-H_{\tau,b}(\theta)\). Moreover, with \(c=1-\tau b/(1-b)>0\), the mean-value theorem yields
\[
|t-g_\theta(t)|\ge c|t-H_{\tau,b}(\theta)|
\]
**for \(t\in[A,B]\)**. Outside that interval the elementary inequalities \(g_\theta(t)\ge A\) and \(g_\theta(t)\le B\) control the sign and possible errors near the endpoints. Continuity and periodicity follow from the strict root estimate. Taking \(\theta=-\tau\log B\pmod{2\pi}\) and \(\theta=\pi-\tau\log A\pmod{2\pi}\) gives respectively the exact roots \(B\) and \(A\). Thus the stated envelopes are achieved and all intermediate values follow by continuity.

**4. Uniform counting with bounded remainder.** Fix small \(s>0\), put \(\theta_s=\tau\log(1/s)\), and set \(t=sn\). The expansion in Step 2 rewrites the condition \(a_n>s\), for \(n\ge1\), as the comparison
\[
 t<g_{\theta_s}(t)+O(n^{-1}).
\]
For \(n\) with \(t\in[A/2,2B]\), \(n^{-1}=O_{\tau,b}(s)\). On \([A,B]\), the root estimate in Step 3 shows that disagreement with the unperturbed test \(t<H_{\tau,b}(\theta_s)\) is possible only if
\[
|sn-H_{\tau,b}(\theta_s)|\le C_{\alpha,\tau,b}s.
\]
On \([A/2,A)\) a disagreement requires \(sn\ge A-Cs\), since \(g_{\theta_s}(sn)\ge A\); on \((B,2B]\) it requires \(sn\le B+Cs\), since \(g_{\theta_s}(sn)\le B\). Each exceptional set contains only \(O_{\alpha,\tau,b}(1)\) lattice indices. For sufficiently large \(n\) with \(sn<A/2\), the test always holds, and for \(sn>2B\) it always fails; any remaining exceptional small indices contribute only a fixed constant. The unperturbed test has \(H_{\tau,b}(\theta_s)/s+O(1)\) positive integer solutions. Therefore
\[
N_K(s)=H_{\tau,b}(\theta_s)/s+O_{\alpha,\tau,b}(1).
\]
As \(s\downarrow0\), the phase \(\theta_s\) visits every residue class modulo \(2\pi\) infinitely often; the liminf and limsup conclusions follow from Step 3.

**5. Exact logarithmic singular trace.** Put \(h(u)=|1+b e^{iu}|\). By Step 2,
\[
\sum_{n=1}^{N}a_n=\tau\sum_{n=1}^{N}\frac{h(\tau\log n)}{n}+O_{\alpha,\tau,b}(1).
\]
Since \(h\) and \(h'\) are bounded, Euler summation compares this harmonic sum to \(\int_1^N h(\tau\log t)dt/t\) with bounded error. By periodicity, the integral equals
\[
\frac{\log N}{2\pi}\int_0^{2\pi}h(u)du+O_{\tau,b}(1).
\]
Although the \(a_n\) are not assumed sorted, write \(\sigma_j=s_j(K)\). The largest \(N\) entries dominate the sum of the first \(N\), while for \(M> N\),
\[
\sum_{n=1}^{N}a_n\le\sum_{j=1}^{N}\sigma_j
\le\sum_{n=1}^{M}a_n+N\sup_{n>M}a_n.
\]
Taking \(M=\lceil N\log N\rceil\) and using \(a_n\le C/n\), the upper and lower expressions differ by \(O(\log\log N)\). Dividing by \(\log N\) proves the displayed limit and consequently Dixmier measurability of \(|K|\). The elliptic-integral expression follows from the substitution \(u=2v\) and the identity \(|1+be^{iu}|=(1+b)\sqrt{1-[4b/(1+b)^2]\sin^2(u/2)}\).

## Verification

The included standalone script `check.py` evaluates the exact gamma-ratio matrix coefficients (without discretizing the Bergman projection), compares them to the model, checks uniqueness and prescribed extrema of the threshold roots, and tests the bounded counting discrepancy for several parameter triples and several decreasing thresholds. Its finite diagnostics are reproducible with Python, NumPy and SciPy. The argument for every parameter and arbitrarily small threshold is Steps 1–5, not the finite checks. For implementation, \(R_v(n)\) should be evaluated by logarithmic gamma functions to avoid overflow.

## Relationship to prior work

Li and Wang's 2026 compactness/Berezin-transform characterization for bounded-symbol Toeplitz operators on radial weighted Bergman spaces motivates examining quantitative operator-ideal behavior in concrete radial families. This theorem is about a **commutator with multiplication**, rather than compactness of an individual radial Toeplitz operator. Looi's 2026 Bergman counterexamples already exploit imaginary powers of the boundary distance and the resulting gamma/Mellin asymptotics; the use of these scalar modes is credited as prior mathematical machinery. Maximenko and Pacheco prove logarithmic-Lipschitz regularity for radial Toeplitz eigenvalue sequences; that regularity predicts first-order decay but does not specify the two-frequency counting threshold or its exact phase modulation. Earlier Dixmier-trace formulas of Engliš, Guo and Zhang concern smooth-symbol Toeplitz commutators and products, while the present symbols oscillate without boundary limits. The particular bounded-remainder counting law and its simultaneous nonconvergent Weyl coefficient and convergent logarithmic trace were not identified in the examined primary statements. A general theory of slowly varying/oscillatory weighted shifts could conceivably imply the phase-profile mechanism; originality is consequently qualified and independent priority verification remains appropriate.

## Limitations

The small-modulation inequality \(0<b<(1+\tau)^{-1}\) is a proved sufficient condition for a one-root counting profile, not a claimed sharp boundary for all possible modulation amplitudes. No result is asserted for larger \(b\), multiple incommensurable Mellin frequencies, nonradial symbols, arbitrary doubling weights, or commutators with arbitrary analytic multipliers. The result is an explicit one-variable model; it does not provide a general operator-ideal characterization. The source comparison is literature screening, not independent publication-priority certification.

## References

1. Y. Li and Z. Wang, *Compact Toeplitz operators on radial weighted Bergman spaces*, arXiv:2608.23733 (first public version August 24, 2026), especially Theorem 1.1 and the introduction. https://arxiv.org/abs/2608.23733
2. S. Looi, *The Berezin liminf criterion fails for radial Toeplitz operators*, arXiv:2603.10879 (2026), especially Section 3 and Proposition 3.3. https://arxiv.org/abs/2603.10879
3. E. A. Maximenko and C. G. Pacheco, *Toeplitz operators in Bergman space induced by radial measures*, arXiv:2503.23649 (2025), especially Sections 7–8. https://arxiv.org/abs/2503.23649
4. M. Engliš, K. Guo and G. Zhang, *Toeplitz and Hankel operators and Dixmier traces on the unit ball of \(\mathbb C^n\)*, arXiv:0707.2025 (2007). https://arxiv.org/abs/0707.2025
5. D. Suárez, *The eigenvalues of limits of radial Toeplitz operators*, arXiv:0710.0797 (2007). https://arxiv.org/abs/0710.0797
