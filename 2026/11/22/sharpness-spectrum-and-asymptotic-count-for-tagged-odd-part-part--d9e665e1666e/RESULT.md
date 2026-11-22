# Sharpness spectrum and asymptotic count for tagged odd-part partitions

## Finding

For every positive integer \(n\) and every integer \(m\ge0\), let \(T(N)=\mathrm{PDO}_{\mathrm t}(N)\) be the total number of tagged (designated) parts among all partitions of \(N\) into odd parts with one occurrence of each distinct part size designated. Define
\[
S_m=\{n\ge1:\nu_3(T(12\cdot3^m n))=m+2\}.
\]
Then **all** sets \(S_m\) equal the same set \(S\), characterized exactly by the prime factorization of \(n\):

1. \(\gcd(n,6)=1\);
2. for every prime \(p\equiv2\pmod3\), the exponent \(\nu_p(n)\) is even;
3. for every prime \(p\equiv1\pmod3\), \(\nu_p(n)\not\equiv2\pmod3\).

In particular, the published infinite divisibility bound \(3^{m+2}\mid T(12\cdot3^m n)\) is attained *exactly* on this set, simultaneously at every level \(m\). The set has an asymptotically sharp counting law:
\[
\#\{n\le X:n\in S\}\sim C\frac{X}{\sqrt{\log X}}\qquad(X\to\infty),
\]
with the absolutely convergent positive Euler product
\[
C=\frac1{\sqrt{6\sqrt3}}\prod_{p\equiv1\pmod3}\frac{1-p^{-2}}{1-p^{-3}}
\prod_{\substack{p\equiv2\pmod3\\p>2}}(1-p^{-2})^{-1/2}
\approx0.31006165.
\]
Consequently, the sharpness set has natural density zero but infinitely many elements, with a precise square-root logarithmic rarity law.

## Assumptions and scope

All prime factorizations and valuations are for ordinary positive integers. Set \(\nu_3(0)=+\infty\). The empty-product condition includes \(n=1\). The variable \(m\) is fixed or arbitrary nonnegative, and the stated characterization is uniform in \(m\). The asymptotic variable is \(X\to\infty\), counting positive integers \(n\), not values of the partition statistic. The theorem neither classifies valuations larger than \(m+2\) nor claims uniform error terms as \(m\) varies.

Write \(E_r(q)=\prod_{j\ge1}(1-q^{rj})\). The tagged-part generating series is
\[
\sum_{N\ge0}T(N)q^N=q\,\frac{E_2(q)E_3(q)^2E_{12}(q)^2}{E_1(q)^2E_6(q)}.
\]
Let \(f(q)=\eta(6\tau)^4=qE_6(q)^4=\sum_{n\ge1}a(n)q^n\), where \(q=e^{2\pi i\tau}\).

## Proof

**1. Uniform leading-residue identity.** Li and Tang (2026), Theorems 1.1 and 1.2(ii), prove divisibility \(3^{m+2}\mid T(12\cdot3^m n)\) and the internal congruence
\[
T(12\cdot3^{m+1}n)\equiv3\mu_m T(12\cdot3^m n)\pmod{3^{m+5}},
\]
where \(\mu_m\in\{5,8\}\) and hence \(\mu_m\equiv-1\pmod3\). Dividing by \(3^{m+3}\) shows that the normalized leading residues at successive levels differ by a factor \(-1\pmod3\). Thus it suffices to determine the normalized generating series at level zero.

Their equation (3.8) and the definitions of its auxiliary functions give
\[
\sum_{n\ge0}T(12n)q^n=\vartheta(144\xi+1728\xi^2),
\quad \vartheta=\frac{E_2^8E_3^5}{E_1^7E_6^4},\quad
\xi=q\frac{E_2E_6^5}{E_1^5E_3}.
\]
Dividing coefficientwise by \(9\), then reducing modulo \(3\), yields
\[
\sum_{n\ge0}\frac{T(12n)}9q^n\equiv\vartheta\xi
=q\frac{E_2^9E_3^4E_6}{E_1^{12}}\equiv qE_6^4=f(q)\pmod3.
\]
The last equality follows from the formal characteristic-three identity \(E_r(q)^3\equiv E_{3r}(q)\pmod3\): specifically \(E_2^9\equiv E_{18}\equiv E_6^3\), and \(E_1^{12}\equiv E_3^4\), cancelling the other factors. Therefore, for all \(m,n\ge0\),
\[
\boxed{\frac{T(12\cdot3^m n)}{3^{m+2}}\equiv(-1)^m a(n)\pmod3.}
\]
This equality is in ordinary integers after the established divisibility, so exactness of the bound is equivalent to \(a(n)\not\equiv0\pmod3\).

**2. Local classification of the CM coefficient.** The normalized weight-two level-\(36\) newform \(f=\eta(6\tau)^4\) has complex multiplication by \(\mathbb Q(\sqrt{-3})\); its Fourier coefficients are multiplicative on coprime arguments, vanish for arguments divisible by \(2\) or \(3\), and obey the weight-two Hecke recursion at primes \(p\ge5\):
\[
a(p^{e+1})=a(p)a(p^e)-p\,a(p^{e-1}),\qquad a(1)=1.
\]
For inert primes \(p\equiv2\pmod3\), \(a(p)=0\). The recurrence then gives \(a(p^{2j+1})=0\) and \(a(p^{2j})=(-p)^j\), nonzero modulo \(3\). For split primes \(p\equiv1\pmod3\), the CM trace is \(a(p)=\pm2u\) with \(p=u^2+3v^2\); necessarily \(3\nmid u\). Thus modulo \(3\), the characteristic polynomial \(t^2-a(p)t+p\) has the repeated, nonzero root \(\lambda\equiv a(p)/2\pmod3\). The recursion gives the exact congruence
\[
a(p^e)\equiv(e+1)\lambda^e\pmod3.
\]
It vanishes precisely when \(e\equiv2\pmod3\). Multiplicativity and the bad-prime support now prove the three prime-factor conditions stated above. They also show that \(S_m=S\) for every \(m\ge0\).

**3. Counting law.** Let \(b(n)\) be the indicator of \(n\in S\). The local exponent rules yield, for \(\Re(s)>1\),
\[
D(s)=\sum_{n\ge1}\frac{b(n)}{n^s}=
\prod_{p\equiv1\ (3)}\frac{1+p^{-s}}{1-p^{-3s}}
\prod_{\substack{p\equiv2\ (3)\\p>2}}\frac1{1-p^{-2s}}.
\]
Let \(\chi=\chi_{-3}\) be the nonprincipal real character modulo \(3\). Comparing Euler factors gives
\[
D(s)=\zeta(s)^{1/2}L(s,\chi)^{1/2}H(s),
\]
where
\[
H(s)=\sqrt{(1-3^{-s})(1-2^{-2s})}
\prod_{p\equiv1\ (3)}\frac{1-p^{-2s}}{1-p^{-3s}}
\prod_{\substack{p\equiv2\ (3)\\p>2}}(1-p^{-2s})^{-1/2}.
\]
The products defining \(H\) converge normally near \(s=1\) (indeed in \(\Re(s)>1/2\)), with \(H(1)>0\). By the standard Selberg–Delange theorem for nonnegative multiplicative coefficients, or its elementary analytic Tauberian specialization to a zeta power of \(1/2\),
\[
\sum_{n\le X}b(n)\sim\frac{L(1,\chi)^{1/2}H(1)}{\Gamma(1/2)}\frac{X}{\sqrt{\log X}}.
\]
Using \(L(1,\chi)=\pi/(3\sqrt3)\), \(\Gamma(1/2)=\sqrt\pi\), and \(\sqrt{(1-1/3)(1-1/4)}=1/\sqrt2\) gives exactly the product for \(C\) above. The absolute convergence proves \(0<C<\infty\), completing the proof.

## Verification

The accompanying standalone Python checker works entirely in exact integer arithmetic, constructs \(T(N)\) from its Euler product modulo \(3^{12}\), computes the coefficients of \(qE_6(q)^4\) modulo \(3\) separately, and factors each index to evaluate the prime-exponent criterion. At degree cutoff \(3600\), it confirms **433** normalized-residue and exact-valuation identities across the levels \(m=0,1,2\), plus **300** CM support comparisons. Expected output: `TAGGED_3ADIC_SHARPNESS_OK: 433 exact coefficient checks, 300 CM support checks, up to 3600 input degree`. These computations are finite checks, not proofs of uniformity or asymptotics. The analytic and modular-form steps above are the proof of the infinite assertions.

## Relationship to prior work

Li and Tang, *Congruence properties modulo powers of 3 for designated summands in partitions into odd parts* (2026), prove the infinite lower bounds and internal congruences used in step 1, but do not state which indices attain the bound, describe a prime-factor sharpness spectrum, or count such indices asymptotically. Thus the intermediate leading-residue congruence is derived from their results and is not claimed as an independent new theorem. Huber, Liu, McLaughlin, Ye, Yuan, and Zhang (2023), *On the vanishing of the coefficients of CM eta quotients*, classify exact zeros of the relevant CM form; **integral nonvanishing is weaker than nonvanishing modulo three**. Their full manuscript also supplies the Hecke and CM framework used in step 2. The new conclusion combines those inputs with a mod-three prime-power analysis and a separate multiplicative counting argument, producing the exact uniform sharpness set and its constant. No earlier proof of this combined statement was identified among the inspected sources. Existing general Tauberian theory is invoked, not claimed as new.

## Limitations

The result concerns the first nonzero ternary digit of the specified progression and its counting function. It does not determine higher valuations on the complement, nor a power-saving asymptotic remainder. Unindexed work on these CM coefficients or a broader theorem specializing to the same Euler factors could contain an equivalent asymptotic. No independent mathematical validation is represented.

## References

- X. Li and D. Tang, *Congruence properties modulo powers of 3 for designated summands in partitions into odd parts*, arXiv:2611.15164v1 (first posted 11 November 2026), Theorems 1.1, 1.2(ii), Eq. (3.8). https://arxiv.org/html/2611.15164v1
- T. Huber, C. Liu, J. McLaughlin, D. Ye, M. Yuan, S. Zhang, *On the vanishing of the coefficients of CM eta quotients*, Proceedings of the Edinburgh Mathematical Society 66 (2023), 1202–1216. https://doi.org/10.1017/S0013091523000627
- P. Delange, standard mean-value/asymptotic theorem for Dirichlet series with zeta singularities (Selberg–Delange method); no claim of a new analytic theorem.
