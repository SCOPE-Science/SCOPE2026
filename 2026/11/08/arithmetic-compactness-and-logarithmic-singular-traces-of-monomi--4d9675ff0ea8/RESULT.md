# Arithmetic compactness and logarithmic singular traces of monomial Bergman composition commutators

## Finding
For every real \(\alpha>-1\) and integers \(m,n\ge2\), let \(C_m f(z)=f(z^m)\) and \(C_n f(z)=f(z^n)\) act on the weighted analytic Bergman Hilbert space \(A^2_\alpha(\mathbb D)\). Define the cross-adjoint commutator
\[
K_{m,n}=C_m C_n^*-C_n^*C_m.
\]
Write \(g=\gcd(m,n)\), \(a=m/g\), \(b=n/g\), and \(\delta=\alpha+1\). The operator is compact **if and only if** \(g=1\).

If \(g>1\), its essential norm is exactly
\[
\|K_{m,n}\|_{\mathrm e}=(mn)^{-\delta/2},
\]
and the essential spectrum of its modulus is \(\sigma_{\mathrm e}(|K_{m,n}|)=\{0,(mn)^{-\delta/2}\}\). In particular it lies in no finite Schatten class.

If \(g=1\), it is compact but not trace class. Its singular values, arranged in nonincreasing order with multiplicity, obey
\[
\lim_{N\to\infty}N s_N(K_{m,n})=c_{\alpha;m,n}
=\frac{\delta(\delta+1)}2(mn)^{-\delta/2}
\left(1-\frac1m\right)\left(1-\frac1n\right)>0.
\]
Consequently \(K_{m,n}\in\mathcal S_p\) precisely for \(p>1\) (all real \(p>0\)), it belongs to weak trace class \(\mathcal S_{1,\infty}\), and
\[
\lim_{N\to\infty}\frac{\sum_{j=1}^N s_j(K_{m,n})}{\log N}=c_{\alpha;m,n}.
\]
The coefficient is an exact, nonzero logarithmic singular trace. In the unweighted Bergman case \(\alpha=0\), the nonzero singular-value multiset is **exactly**
\[
\left\{\frac{(m-1)(n-1)q}{(mnq+1)\sqrt{(mq+1)(nq+1)}}:q=1,2,\ldots\right\}
\qquad(\gcd(m,n)=1).
\]

## Assumptions and scope
The Hilbert norm is normalized by
\[
\|f\|_{A^2_\alpha}^2=\frac{\alpha+1}{\pi}\int_{\mathbb D}|f(z)|^2(1-|z|^2)^\alpha\,dA(z).
\]
Let \(h_k=\|z^k\|=[\Gamma(\alpha+2)\Gamma(k+1)/\Gamma(k+\alpha+2)]^{1/2}\) and \(e_k=z^k/h_k\). Here \(C_r f=f\circ(z\mapsto z^r)\), \(r\ge2\), is a bounded composition operator: it acts as the contraction \(C_r e_k=w_r(k)e_{rk}\), where \(w_r(k)=h_{rk}/h_k\le1\). The operator \(K_{m,n}\) is defined on the *whole* Hilbert space; no unbounded-operator domain issue occurs. The essential spectrum is the spectrum in the Calkin algebra. Singular-value claims refer to nonzero singular values of compact operators; the essential-spectrum assertion applies to the noncompact case.

## Proof
**1. Arithmetic reduction and full singular-value description.** For any \(r\), \(C_r^*e_{rq}=w_r(q)e_q\) and \(C_r^*e_k=0\) if \(r\nmid k\). Since \(g=\gcd(m,n)\), the support of \(C_n^*C_m\) consists exactly of columns indexed by \(bq\), while that of \(C_mC_n^*\) consists of columns indexed by \(nq=bgq\). Both products send the column \(e_{bq}\), whenever defined, to the *same* target \(e_{aq}\). Therefore, for every integer \(q\ge0\),
\[
K_{m,n}e_{bq}=\kappa_q e_{aq},\qquad
\kappa_q=\mathbf1_{g\mid q}\,w_n(q/g)w_m(q/g)-w_m(bq)w_n(aq),
\]
and \(K_{m,n}e_k=0\) whenever \(b\nmid k\). Both the input indices \(bq\) and output indices \(aq\) are pairwise distinct as \(q\) varies. Thus \(K_{m,n}^*K_{m,n}\) is diagonal in this basis, with entries \(|\kappa_q|^2\) on \(e_{bq}\) and zero elsewhere. In particular, the exact nonzero singular-value multiset is \(\{|\kappa_q|:q\ge1,\ \kappa_q\ne0\}\) (counting multiplicity); \(\kappa_0=0\).

**2. Noncoprime case.** Stirling's gamma-ratio asymptotic yields, for fixed \(r\ge2\),
\[
w_r(k)=r^{-\delta/2}+O(k^{-1})\quad(k\to\infty).
\]
Hence \(w_m(bq)w_n(aq)\to(mn)^{-\delta/2}\), while \(w_n(q/g)w_m(q/g)\to(mn)^{-\delta/2}\) along \(g\mid q\). If \(g>1\), the infinite subsequence \(g\nmid q\) therefore has \(|\kappa_q|\to(mn)^{-\delta/2}\), whereas \(\kappa_q\to0\) along \(g\mid q\). The diagonal formula for \(|K_{m,n}|\) gives precisely two essential spectral values, \(0\) and \((mn)^{-\delta/2}\), and the asserted essential norm. In particular the commutator is noncompact.

**3. Coprime case and sharp coefficient.** If \(g=1\), every \(q\ge1\) has
\[
\kappa_q=A_q-B_q,\qquad
A_q=\frac{h_{nq}h_{mq}}{h_q^2},\quad
B_q=\frac{h_{mnq}^2}{h_{nq}h_{mq}}.
\]
For fixed \(\delta>0\), the two-term gamma-ratio expansion is
\[
\log h_k=\mathrm{const}-\frac\delta2\log k-\frac{\delta(\delta+1)}{4k}+O(k^{-2}).
\]
Substituting it into the two products (at the four indices \(q,mq,nq,mnq\)) gives
\[
A_q-B_q=\frac{\delta(\delta+1)}{2q}(mn)^{-\delta/2}
\left(1-\frac1m\right)\left(1-\frac1n\right)+O(q^{-2})
=\frac{c_{\alpha;m,n}}q+O(q^{-2}).
\]
Thus \(\kappa_q\to0\), proving compactness, and \(q|\kappa_q|\to c_{\alpha;m,n}>0\). The counting function of the exact singular multiset satisfies \(\#\{q:|\kappa_q|>t\}\sim c_{\alpha;m,n}/t\) as \(t\downarrow0\), by two-sided comparison with \((c_{\alpha;m,n}\pm\varepsilon)/q\) for large \(q\). Inverting this counting relation yields \(Ns_N\to c_{\alpha;m,n}\). The Schatten threshold and logarithmic-sum identity follow by the \(p\)-series and harmonic-series tests, respectively. No finite enumeration is used to prove these infinite conclusions.

**4. Closed form for standard Bergman space.** At \(\alpha=0\), \(h_k=(k+1)^{-1/2}\). Therefore
\[
A_q=\frac{q+1}{\sqrt{(nq+1)(mq+1)}},\qquad
B_q=\frac{\sqrt{(nq+1)(mq+1)}}{mnq+1}.
\]
Subtracting and using \((q+1)(mnq+1)-(mq+1)(nq+1)=q(m-1)(n-1)\) gives the exact displayed singular spectrum.

## Verification
The standalone file `check_monomial_commutators.py` performs 6,966 finite assertions using only the Python standard library. It checks arithmetic support, exact integer-factorization identities, exact rational squared-weight comparisons for the standard Bergman case, and asymptotic scale checks for five sample weights and several coprime and noncoprime integer pairs. Run it using `python check_monomial_commutators.py`; the expected terminal line is `MONOMIAL_BERGMAN_CHECK_OK 6966 finite assertions`. The checks do not establish the infinite theorem; all limiting steps are justified above by Stirling expansion and diagonal spectral counting.

## Relationship to prior work
Leng and Zhao (2026), arXiv:2610.15472, investigate Schatten membership of the two *individual* products \(C_\varphi C_\psi^*\) and \(C_\psi^*C_\varphi\) on Hardy and Bergman spaces. Their Sections 3–4 do not state the arithmetic *difference* formula above, whose compactness depends on cancellation between noncompact products. Clifford, Levi and Narayan (2012), and MacCluer, Narayan and Weir (2013), investigate compactness of commutators induced by **linear-fractional** maps; degree-at-least-two monomials are outside that class. Clifford, Dabkowski, Wiggins and Zeytuncu (published 2025) consider products with finite Blaschke factors on **Hardy** space, not the weighted Bergman singular trace of the cross-adjoint commutator. The simple diagonalization of orthogonal columns and Stirling's formula are classical tools, not new theorems. This result claims only the resulting complete arithmetic phase diagram and its logarithmic coefficient for the specified monomial family.

## Limitations
The theorem concerns exactly monomial maps of degree at least two on classical power-weighted analytic Bergman Hilbert spaces; it does not classify general finite Blaschke symbols or arbitrary radial weights. Inaccessible full texts of some earlier commutator papers leave a residual priority risk, despite their publicly stated restriction to linear-fractional maps. Neither numerical tests nor unsuccessful literature searches certify publication novelty. There has been no independent mathematical audit.

## References
1. Q. Leng and X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472 (first submitted 11 October 2026), https://arxiv.org/abs/2610.15472 .
2. J. H. Clifford, D. Levi and S. K. Narayan, *Commutator of composition operators with adjoints of composition operators*, Complex Variables and Elliptic Equations 57 (2012), 677–686, https://doi.org/10.1080/17476933.2010.534142 .
3. B. D. MacCluer, S. K. Narayan and R. J. Weir, *Commutators of composition operators with adjoints of composition operators on weighted Bergman spaces*, Complex Variables and Elliptic Equations 58 (2013), 35–54, https://doi.org/10.1080/17476933.2010.551202 .
4. J. H. Clifford, M. Dabkowski, A. Wiggins and Y. Zeytuncu, *The operator \(C_\phi^*C_\psi\) when \(\phi\) is a Blaschke product*, Advances in Operator Theory 11, article 3 (2026), first published 24 October 2025, https://doi.org/10.1007/s43036-025-00476-4 .
5. C. Duna, M. Gagne, C. Gu and J. E. Shapiro, *Toeplitzness of products of composition operators and their adjoints*, Journal of Mathematical Analysis and Applications 410 (2014), 577–584, https://doi.org/10.1016/j.jmaa.2013.08.029 .
