# Sharp cyclic Pascal-row correlations at every odd prime

## Finding
Fix an odd prime \(p\). For each \(n\ge0\), let
\[
F_p(n)=\#\{0\le j\le n:p\nmid\binom nj\}.
\]
For integers \(r\ge1\) and \(0\le h<p^r\), let \(\rho_{p,r}(h)\) be the ordinary Pearson correlation of the cyclic length-\(p^r\) arrays \(F_p(n)\) and \(F_p((n+h)\bmod p^r)\). For every fixed integer \(h\ge0\), the limit \(\rho_p(h)=\lim_{r\to\infty}\rho_{p,r}(h)\) exists and is rational. In particular,
\[
\boxed{\rho_p(0)=1,\qquad0<\rho_p(h)\le\frac{2(p+1)}{2p+5}\quad(h\ge1),}
\]
with equality in the upper bound **if and only if** \(h\) is an integral power of \(p\). Thus the exact largest positive-lag correlation is \(2(p+1)/(2p+5)\), giving \(8/11\) at \(p=3\) and \(4/5\) at \(p=5\).

Every positive-lag limit is determined by a finite rational recursion. Define
\[
S_p=\frac{p(p+1)(2p+1)}6,\quad \alpha_p=\frac{2(p+1)}{2p+5},
\]
\[
A_{p,d}=\frac{(p-d)(p-d+1)(2p+d+1)}6,\qquad
B_{p,d}=\frac{d(d+1)(3p-d+1)}6\quad(0\le d<p).
\]
Then \(\rho_p(0)=1\), \(\rho_p(1)=\alpha_p\), \(\rho_p(ph)=\rho_p(h)\), and, for \(h=pq+d\ge2\) with \(1\le d<p\),
\[
\boxed{\rho_p(h)=\frac{A_{p,d}\rho_p(q)+B_{p,d}\rho_p(q+1)}{S_p}.}
\]
Here both recursive arguments are strictly smaller than \(h\). The lag-one unnormalized cyclic cross-sum also has the exact finite-depth value
\[
\boxed{\sum_{n=0}^{p^r-1}F_p(n)F_p((n+1)\bmod p^r)=\alpha_p S_p^r+(1-\alpha_p)p^r.}
\]

## Assumptions and scope
The prime \(p\) is odd, not composite. Each shift \(h\) is fixed before \(r\to\infty\); cyclic rather than unwrapped shifts are used. The correlation uses uniform counting measure on all \(p^r\) indices. For finite \(r\), \(h\) is reduced modulo \(p^r\), and the variance is positive. No assertion is made about a shift that depends on \(r\), about higher prime-power nondivisibility, or about general digit weights.

## Proof
**Digit formula and normalization.** Let \(d_i\) be the base-\(p\) digits of \(n\). Lucas's theorem implies the classical Fine identity \(F_p(n)=\prod_i(d_i+1)\). Summing digitwise over all length-\(r\) words gives
\[
\sum_{n<p^r}F_p(n)=\left(\frac{p(p+1)}2\right)^r,
\qquad \sum_{n<p^r}F_p(n)^2=S_p^r.
\]
Put \(\mu_p=(p+1)/2\), \(\beta_p=S_p/p=(p+1)(2p+1)/6\), and \(\theta_p=\mu_p^2/\beta_p=3(p+1)/(2(2p+1))<1\). The uniform mean is \(\mu_p^r\), and the variance \(\beta_p^r-\mu_p^{2r}>0\).

**Exact cyclic carry decomposition.** Write
\[
H_r(h)=\sum_{n=0}^{p^r-1}F_p(n)F_p((n+h)\bmod p^r),\qquad H_0(h)=1.
\]
For any nonnegative \(h=pq+d\) with \(0\le d<p\), split \(n=pm+x\), \(0\le x<p\). If \(x+d<p\), the low output digit is \(x+d\), and the remaining index is shifted by \(q\). Otherwise the low output digit is \(x+d-p\), and the remaining index is shifted by \(q+1\). The digit weights multiply, giving the exact identity, for every \(r\ge1\),
\[
H_r(pq+d)=A_{p,d}H_{r-1}(q)+B_{p,d}H_{r-1}(q+1),
\]
where \(A_{p,d}=\sum_{x=0}^{p-d-1}(x+1)(x+d+1)\) and \(B_{p,d}=\sum_{x=p-d}^{p-1}(x+1)(x+d+1-p)\). Elementary summation gives the displayed closed forms. Note \(A_{p,0}=S_p\), \(B_{p,0}=0\), and \(H_r(0)=S_p^r\).

**Rational limiting correlation.** Define \(C_r(h)=H_r(h)/S_p^r\). For \(h=1\), \(A_{p,1}=p(p^2-1)/3\) and \(B_{p,1}=p\). Therefore
\[
C_r(1)=\frac{A_{p,1}}{S_p}+\frac{p}{S_p}C_{r-1}(1)
\longrightarrow\frac{A_{p,1}}{S_p-p}=\alpha_p,
\]
with the stated exact finite-depth cross-sum by solving the recurrence from \(H_0(1)=1\). For \(h=0\), \(C_r(0)=1\). Every positive multiple of \(p\) reduces to a smaller shift, since \(C_r(ph)=C_{r-1}(h)\). Every other \(h\ge2\) has recursive arguments \(q,q+1<h\). Strong induction on \(h\), using the exact carry recurrence and the solved \(h=1\) case, establishes convergence and the rational recursion for every fixed \(h\). The finite Pearson coefficient is exactly
\[
\rho_{p,r}(h)=\frac{C_r(h)-\theta_p^r}{1-\theta_p^r}.
\]
Since \(\theta_p<1\), its limit equals the recursive \(C\)-limit.

**Sharp upper bound and equality.** For \(1\le d<p\), direct polynomial simplification yields
\[
S_p-A_{p,d}-B_{p,d}=\frac{dp(p-d)}2>0,
\]
\[
6(2p+5)(\alpha_p S_p-A_{p,d}-\alpha_p B_{p,d})
=3(p-d)(d-1)(d+2p^2+3p+1)\ge0.
\]
For \(1\le h<p\), one has \(q=0\), \(C(0)=1\) and \(C(1)=\alpha_p\), so the second inequality proves \(C(h)\le\alpha_p\), with equality only at \(h=1\). For \(h=pq+d\) with \(q\ge1\) and \(d>0\), induction gives \(C(q),C(q+1)\le\alpha_p\), and the first strict inequality implies \(C(h)<\alpha_p\). For \(d=0\), \(C(ph)=C(h)\), so equality descends to \(1\) exactly for powers of \(p\). Every coefficient \(A_{p,d}\) and every \(B_{p,d}\) with \(d>0\) is positive; positivity of all limits follows by the same induction. This proves all strict and equality assertions for odd primes.

## Verification
The standalone standard-library checker `artifacts/verify.py` independently computes complete cyclic cross-sums at several odd primes and finite levels; it verifies the exact carry recurrence, the closed lag-one count, digit moments, the critical polynomial inequalities, and the rational all-shift bound and equality cases for one thousand positive shifts at each tested prime. Run `python3 artifacts/verify.py` from the package root. It reports `CHECK_OK 10456 exact assertions`. These finite tests corroborate algebra and boundaries; the induction and carry derivation, not enumeration, prove the unlimited claim.

## Relationship to prior work
Fine's 1947 identity is the input digit formula, not the finding. Rowland's 2010 preprint studies the individual Pascal-row counts and their prime-power refinements; its full primary text gives no shifted Pearson cross-sums or sharp all-shift extremum. Spiegelhofer and Wallner's 2016 preprint concerns subword polynomial formulas for exact divisibility, not these two-row normalized correlations. A published binary-only all-shift result establishes \(2/3\) and binary power-of-two extremizers. Its stated scope is exclusively \(p=2\); its binary digit matrices do not imply the odd-prime coefficient identities or the new prime-dependent sharp constant without an additional proof. The present finding specifically excludes that covered binary case. No claim is made that a general weighted digit-correlation theorem could not implicitly imply it.

## Limitations
This is a self-reviewed proof, not an independent mathematical certification. The correlations are cyclic and fixed-lag; changing either sampling convention or the order of limits may change the statement. Priority remains qualified because broader literature on weighted \(p\)-multiplicative correlations and historic digit-distribution work may contain an implicit equivalent. No assertion of newness is made for Fine's formula, the binary \(p=2\) specialization, or the carry technique alone.

## References
1. N. J. Fine, *Binomial coefficients modulo a prime*, American Mathematical Monthly 54 (1947), 589–592; the original digit-product theorem.
2. E. Rowland, *The number of nonzero binomial coefficients modulo \(p^\alpha\)*, arXiv:1001.1783, first public 2010-01-12. https://arxiv.org/abs/1001.1783
3. L. Spiegelhofer and M. Wallner, *An explicit generating function arising in counting binomial coefficients divisible by powers of primes*, arXiv:1604.07089, first public 2016-04-24. https://arxiv.org/abs/1604.07089
4. *Sharp shift correlations for the odd-entry counts in binary Pascal rows*, public result dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-shift-correlations-for-the-odd-entry-counts-in-binary-pasc--7be946ab1fa0
