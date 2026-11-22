# Arithmetic collision residue for Schatten-four norms of radially damped Bergman composition differences

## Finding

Let \(\alpha>-1\), let \(p,q\) be distinct positive integers, and let \(a,b>0\). For \(0<r<1\) and phases \(\theta,\phi\in\mathbb R\), consider the difference of two composition operators on the standard analytic weighted Bergman Hilbert space:
\[
D_r=C_{r^a e^{i\theta}z^p}-C_{r^b e^{i\phi}z^q}.
\]
Put \(\gamma=\alpha+1\), \(g=\gcd(p,q)\), \(p_0=p/g\), \(q_0=q/g\), \(A=p^{-\gamma}\), and \(B=q^{-\gamma}\). Define
\[
h_n=\frac{\Gamma(\alpha+2)\Gamma(n+1)}{\Gamma(n+\alpha+2)},\qquad w_k(n)=\frac{h_{kn}}{h_n}\quad(n\ge1).
\]
Then \(D_r\) belongs to every Schatten class, and its **exact** Schatten-four moment is
\[
\boxed{\|D_r\|_{\mathcal S_4}^4
=\sum_{n=1}^\infty\bigl(r^{2an}w_p(n)+r^{2bn}w_q(n)\bigr)^2
+2\sum_{k=1}^\infty r^{2(aq_0+bp_0)k}w_p(q_0k)w_q(p_0k).}
\tag{1}
\]
In particular, the entire singular-value sequence is independent of both phases. As \(r\uparrow1\),
\[
\boxed{\|D_r\|_{\mathcal S_4}^4
=\frac{\Lambda_{\alpha;p,q}(a,b)}{1-r}
+O_{\alpha,p,q,a,b}\!\left(\log\frac{e}{1-r}\right),}
\tag{2}
\]
where the **sharp coefficient** is
\[
\boxed{\Lambda_{\alpha;p,q}(a,b)
=\frac{A^2}{4a}+\frac{B^2}{4b}
+\frac{AB}{a+b}
+\frac{AB}{a q_0+b p_0}.}
\tag{3}
\]
The final, strictly positive term is a monomial-frequency collision residue and does not arise from the diagonal Gram entries. By comparison,
\[
\boxed{\lim_{r\uparrow1}(1-r)\|D_r\|_{\mathcal S_2}^2
=\frac{A}{2a}+\frac{B}{2b}.}
\tag{4}
\]
The normalized collision coefficient \(\frac{1}{AB}\bigl(\Lambda-\frac{A^2}{4a}-\frac{B^2}{4b}-\frac{AB}{a+b}\bigr)=1/(aq_0+bp_0)\) is independent of the Bergman weight parameter \(\alpha\). For equal damping speeds \(a=b=1\), equation (3) reads \(\Lambda=(A+B)^2/4+ABg/(p+q)\). At \(\alpha=0\), \(p=2\), and \(q=3\), it is exactly \(149/720\).

## Assumptions and scope

Write \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and
\[
\|f\|_\alpha^2=\frac{\alpha+1}{\pi}\int_{\mathbb D}|f(z)|^2(1-|z|^2)^\alpha\,dA(z).
\]
Its normalized monomial basis is \(e_n(z)=z^n/\sqrt{h_n}\), \(n\ge0\). The composition-operator convention is \(C_\varphi f=f\circ\varphi\). All Schatten norms count singular values with multiplicity. The exponents \(p,q\) must be distinct, and both damping speeds strictly positive. Constants lie in the kernel of \(D_r\). Equations (1)–(4) do not extend by the same argument to boundary symbols \(r=1\), to arbitrary analytic symbols, or to unweighted Hardy-space moment asymptotics.

## Proof

**1. Monomial action and compactness.** Direct substitution into the orthonormal basis gives, for \(n\ge1\),
\[
D_re_n=r^{an}e^{in\theta}\sqrt{w_p(n)}\,e_{pn}
-r^{bn}e^{in\phi}\sqrt{w_q(n)}\,e_{qn},\qquad D_re_0=0.
\tag{5}
\]
Because the monomial norms decrease with degree, \(0<w_j(n)\le1\) for \(j\ge1\). Each summand in (5) is an exponentially damped partial monomial permutation. Its singular values are \(r^{an}\sqrt{w_p(n)}\) or \(r^{bn}\sqrt{w_q(n)}\), respectively. Thus each composition operator, and hence their difference, lies in \(\mathcal S_s\) for every \(s>0\), including the quasi-ideals \(0<s<1\). All traces below converge absolutely.

**2. Exact Gram-square identity.** For a Hilbert–Schmidt operator \(T\), positivity and trace cyclicity imply
\[
\|T\|_{\mathcal S_4}^4=\operatorname{Tr}((T^*T)^2)
=\sum_{n,m\ge0}|\langle Te_n,Te_m\rangle|^2.
\tag{6}
\]
For \(n=m\ge1\), the two output degrees \(pn\) and \(qn\) differ. Therefore the Gram diagonal is exactly \(r^{2an}w_p(n)+r^{2bn}w_q(n)\), giving the first sum in (1). For \(n\ne m\), a nonzero overlap can occur only when \(pn=qm\) or \(qn=pm\). Writing \(g=\gcd(p,q)\), all positive solutions to the first equation are uniquely \(n=q_0k\), \(m=p_0k\), with \(k\ge1\). The two conditions cannot simultaneously hold unless \(p=q\), which is excluded. The modulus squared of this Gram entry is
\[
r^{2(aq_0+bp_0)k}w_p(q_0k)w_q(p_0k).
\]
The Hermitian-conjugate Gram entry contributes the same quantity, giving precisely the factor two in the second sum of (1). This accounts for every pair of indices; no other terms remain.

**3. Exact phase independence.** Let \(R_\xi e_n=e^{in\xi}e_n\), a unitary for real \(\xi\). Set \(\lambda=(\theta-\phi)/(p-q)\) and \(\mu=\theta-p\lambda\). Then \(\mu+p\lambda=\theta\) and \(\mu+q\lambda=\phi\), and equation (5) gives \(D_r(\theta,\phi)=R_\lambda D_r(0,0)R_\mu\). Left and right unitary multiplication preserves every singular value. Thus phase independence holds for the full singular spectrum, not only for (1).

**4. Precise boundary coefficient.** The fixed-integer gamma-ratio formula yields
\[
w_j(n)=j^{-\gamma}+O_{\alpha,j}(n^{-1})\qquad(n\to\infty),
\tag{7}
\]
for every fixed \(j\ge1\); the estimate is uniform over positive integers \(n\) after adjusting its constant for finitely many small indices. For each fixed \(c>0\), a geometric series and a logarithmic series give
\[
\sum_{n=1}^\infty r^{cn}=
\frac{1}{c(1-r)}+O_c(1),\qquad
\sum_{n=1}^\infty\frac{r^{cn}}{n}
=O_c\!\left(\log\frac{e}{1-r}\right).
\tag{8}
\]
Expanding the first square in (1) and applying (7)–(8) gives, respectively, leading coefficients \(A^2/(4a)\), \(B^2/(4b)\), and \(2AB/[2(a+b)]=AB/(a+b)\). The collision sum has \(w_p(q_0k)w_q(p_0k)=AB+O(k^{-1})\); the same geometric calculation gives coefficient \(2AB/[2(aq_0+bp_0)]=AB/(aq_0+bp_0)\). Each error is at most logarithmic. Summing proves (2)–(3), with all dependence on fixed parameters explicit in the error subscript. Finally, equation (5) gives the exact Hilbert–Schmidt trace \(\sum_{n\ge1}(r^{2an}w_p(n)+r^{2bn}w_q(n))\), which proves (4) by the same estimate. The collision coefficient is positive for every admissible parameter, so it cannot be absorbed into the diagonal terms.

## Verification

The accompanying `verify.py` is a supplementary finite diagnostic using NumPy and SciPy, with declared dependencies in `requirements.txt`. Running `python verify.py` yielded `RADIAL_MONOMIAL_S4_MOMENT_DIAGNOSTIC_OK 403`. It compares finite monomial matrices with the exact truncated series (384 tests), checks phase independence of finite-section singular values (9 tests), and samples near-boundary limits (10 tests). The infinite-dimensional identities and error bound are established by the analytic proof above, not by finite truncation. The standard Gamma-function formula for the monomial norm follows from a beta integral, and the asymptotic is the classical fixed-shift Gamma-ratio expansion; neither requires an external numerical certificate.

## Relationship to prior work

Choe–Choi–Koo–Park (2026) characterize Schatten membership of differences of Bergman composition operators for indices at least two, using local pseudohyperbolic averages. Such membership information does not directly determine the trace of the **fourth power of the Gram operator**, its exact monomial collision sum, or its sharp radial blow-up coefficient. Its public abstract and references were inspected, but the full publisher article was not accessible, so this implication comparison remains incomplete. Ai–Yang (2026; first posted November 18) extend membership and weak-Schatten characterizations and two-sided estimates, but their accessible full text does not state equation (1) or its arithmetic coefficient (3). The later publication is only a comparison source and is not used to assign the direction's public date. Bayart–Gilmore–Şahin (2025) study approximation numbers of differences mainly in the Hardy composition setting rather than this exact radial Bergman moment.

A publicly available earlier result, *Hardy–Bergman spectral gap for differences of power-map composition operators* (2026), proves the Fredholm essential singular interval for the **undamped** monomial difference. That theorem is compatible with the new radial Schatten explosion, but its essential spectral bounds do not supply an exact fourth Schatten trace or reduced-degree collision residue. The current calculation uses familiar monomial basis and arithmetic lattice tools; no claim is made that those tools are new. The asserted contribution is the explicit moment and universal reduced-degree boundary coefficient, together with a quantitative comparison against the Hilbert–Schmidt blow-up.

## Limitations

The result concerns fixed \(p,q,a,b,\alpha\) as \(r\uparrow1\); there is no claim of an estimate uniform in increasing monomial degrees or varying Bergman weights. It does not characterize the full singular-value distribution at the boundary, nor general nonmonomial symbols. The leading coefficient is exact, but no constant-order term in the asymptotic expansion is claimed. The primary publisher paper's complete text was unavailable; abstract-based comparison cannot exclude an equivalent formula inside it. Searches cannot rule out unindexed or differently named earlier statements. Independent mathematical verification and definitive bibliographic priority have not been performed.

## References

1. B. R. Choe, K. Choi, H. Koo, I. Park, *Schatten Class Difference of Composition Operators on the Bergman Space*, Complex Analysis and Operator Theory 20, Article 109 (first published May 20, 2026), https://doi.org/10.1007/s11785-026-01962-0.
2. Q. Ai, R. Yang, *Schatten and weak Schatten classes of composition operator differences on Bergman spaces*, arXiv:2611.23733 (posted November 18, 2026), https://arxiv.org/abs/2611.23733.
3. F. Bayart, T. Gilmore, H. Şahin, *Approximation numbers of differences of composition operators*, arXiv:2509.19797 (2025), https://arxiv.org/abs/2509.19797.
4. *Hardy–Bergman spectral gap for differences of power-map composition operators*, publicly available 2026 research record, https://github.com/published-finding corpus/2026.
5. B. R. Choe, T. Hosokawa, H. Koo, *Hilbert-Schmidt differences of composition operators on the Bergman space*, Mathematische Zeitschrift 269 (2011), 751–775.
