# Sharp eventual periods for prime-square rational floor monomials

## Finding

Let \(p\) be any prime, \(a\ge1\) an integer with \(p\nmid a\), and \(k\ge2\) an integer. For positive integers \(n\), set
\[
F(n)=\mathbf 1_{\gcd(n,\lfloor an^k/p^2\rfloor)=1}.
\]
For each \(1\le r<p^2\) satisfying \(p\nmid r\), let \(t_r\) denote the unique integer in \(\{1,\ldots,p^2-1\}\) congruent to \(ar^k\pmod{p^2}\). Put
\[
Q=\operatorname{rad}\!\left(\operatorname{lcm}_{\substack{1\le r<p^2\\p\nmid r}}t_r\right),\qquad \operatorname{rad}(1)=1,
\qquad P=p^{1+\mathbf 1_{p\nmid k}}Q.
\]
Then the **least eventual period** of \(F\) is exactly \(P\). More precisely, define the periodic model
\[
H(n)=\begin{cases}
\mathbf1_{\gcd(n,t_{n\bmod p^2})=1},&p\nmid n,\\
0,&p\mid n.
\end{cases}
\]
Its least period from the first index is \(P\), and **the only discrepancy at all positive indices** is
\[
\boxed{F(n)=H(n)+\mathbf1_{\{k=2,\ n=p\}}.}
\]
Thus when \(k\ge3\), the original sequence is periodic from its first index. When \(k=2\), it becomes periodic at the **sharp starting index** \(p+1\) and not earlier. In particular, the factor \(p^2\) in its basic residue-period collapses to \(p\) if and only if \(p\mid k\).

The exact natural density is
\[
\boxed{\delta=\frac1{p^2}\sum_{\substack{1\le r<p^2\\p\nmid r}}\frac{\varphi(t_r)}{t_r},\qquad
\#\{1\le n\le X:F(n)=1\}=\delta X+O(P).}
\]
For example, \((p,a,k)=(3,1,2)\) gives \(Q=14\) and least eventual period \(126\), with the isolated exception at \(n=3\). For \((p,a,k)=(3,1,3)\), the least period is \(6\), with no exception.

## Assumptions and scope

All parameters and residues lie in the stated integer ranges. In particular the denominator is exactly a prime square, the numerator is nonzero modulo that prime, and the polynomial is the monomial \(an^k\) with exponent at least two. We use \(\varphi(1)=1\). A period means a positive integer \(T\) with \(F(n+T)=F(n)\) for all sufficiently large positive \(n\). The least starting index is the smallest positive \(n_0\) such that the sequence is periodic for all \(n\ge n_0\) with its least eventual period. The model is defined even at the finitely many indices where the original sequence may differ. The \(O(P)\) constant is absolute for each fixed parameter choice.

## Proof

**1. Exact floor reduction and the single exceptional index.** If \(p\nmid n\), Euclidean division gives \(p^2\lfloor an^k/p^2\rfloor=an^k-t_r\), where \(r\equiv n\pmod{p^2}\). As \(p^2\) is invertible modulo \(n\),
\[
\gcd\!\left(n,\left\lfloor\frac{an^k}{p^2}\right\rfloor\right)=\gcd(n,an^k-t_r)=\gcd(n,t_r).
\tag{1}
\]
For \(n=pm\) with \(m\ge1\), the floor is the integer \(ap^{k-2}m^k\), and
\[
\gcd(pm,ap^{k-2}m^k)=m\gcd(p,ap^{k-2}m^{k-1}).
\tag{2}
\]
For \(k\ge3\), this equals \(pm\), so no multiple of \(p\) is admitted. For \(k=2\), it equals one exactly when \(m=1\), since \(p\nmid a\). This proves the displayed exact identity for \(F\) and \(H\).

**2. Existence of the proposed period.** Each \(t_r\) is a unit modulo \(p\). Formula (1) shows that \(H\) depends only on the residue of \(n\) modulo \(p^2Q\), because only divisibility by primes dividing the \(t_r\) matters. If \(p\mid k\), the binomial theorem yields \(a(r+p)^k\equiv ar^k\pmod{p^2}\); hence \(t_r\) depends only on \(r\bmod p\), and \(pQ\) is already a period. Thus \(P\) is a period.

**3. All periods contain the factor \(pQ\).** Let \(T\) be any positive period of \(H\); the following contradiction constructions can use arbitrarily large positive \(n\), so they also apply to any eventual period. If \(p\nmid T\), choose a unit class \(r\pmod{p^2}\) with \(r\equiv-T\pmod p\). By the Chinese remainder theorem, select \(n\equiv r\pmod{p^2}\) that avoids every prime dividing \(t_r\). Then \(H(n)=1\), while \(H(n+T)=0\), a contradiction. Therefore \(p\mid T\).

For any prime \(\ell\mid Q\), select a unit class \(r\pmod{p^2}\) with \(\ell\mid t_r\). Suppose \(\ell\nmid T\). Choose \(n\equiv r\pmod{p^2}\) and \(n\equiv0\pmod\ell\). For every other prime \(u\mid t_{(r+T)\bmod p^2}\), choose \(n\not\equiv-T\pmod u\), which is always possible. The conditions are compatible by CRT, since all these primes differ from \(p\); at \(\ell\), the required avoidance for \(n+T\) follows from \(\ell\nmid T\). Now \(H(n)=0\) but \(H(n+T)=1\), a contradiction. Consequently \(\ell\mid T\) for each \(\ell\mid Q\), and \(pQ\mid T\).

**4. The sharp prime-square obstruction.** Assume \(p\nmid k\), and suppose, for contradiction, that some period \(T\) is not divisible by \(p^2\). The preceding step gives \(pQ\mid T\), so \(T=ph\) with \(p\nmid h\). For every unit residue \(r\pmod{p^2}\), the values \(H(n)\) at \(n\equiv r\pmod{p^2}\) depend solely on coprimality to \(t_r\). Because \(Q\mid T\) and \(p\nmid Q\), varying \(n\) modulo \(Q\) by CRT shows that invariance under \(n\mapsto n+T\) forces \(t_r\) and \(t_{r+T}\) to have exactly the same sets of prime divisors. Repeating the translation gives this for all \(p\) lifts \(r+jp\) of a fixed nonzero residue modulo \(p\).

Yet
\[
a(r+jp)^k\equiv ar^k+ak r^{k-1}jp\pmod{p^2}.
\tag{3}
\]
The coefficient \(ak r^{k-1}\) is nonzero modulo \(p\). Thus the corresponding \(p\) representatives \(t_{r+jp}\) form the complete set of integers
\[
\{u,u+p,\ldots,u+(p-1)p\},\qquad 1\le u<p.
\]
In particular \(u\) and \(u+p\) are coprime, while \(u+p>1\); they cannot have equal sets of prime divisors. This contradiction proves \(p^2\mid T\) when \(p\nmid k\). Together with step 3 and the established upper period, the least period of \(H\) is exactly \(P\).

**5. Exact onset and density.** The model \(H\) and \(F\) agree except possibly at \(n=p\). If \(k\ge3\), they agree everywhere. If \(k=2\), then \(F(p)=1\), whereas \(F(p+P)=H(p+P)=0\), so no periodicity can start at or before \(p\). Periodicity does start at \(p+1\), proving sharpness. Finally, \(p\nmid Q\); on each unit residue class modulo \(p^2\), CRT gives exactly the fraction \(\varphi(t_r)/t_r\) of indices coprime to \(t_r\), and the nonunit classes contribute zero to \(H\). A single exceptional point does not affect density. Counting complete periods and one remainder proves the formula with \(O(P)\) error.

## Verification

The accompanying standalone `verify.py` uses only Python standard-library exact integer and rational arithmetic. It checks the original floor-based GCD predicate against the formula at the first 219 indices across 693 choices of parameters, then verifies the proposed periodic shift at further indices; in 95 tractable instances it directly enumerates a complete predicted period and independently confirms its least period and exact rational density. Run `python3 verify.py` in the directory containing this file. The expected output is `PRIME_SQUARE_FLOOR_COPRIMALITY_OK 693 FULL_PERIOD_DENSITIES 95`. The finite checks are supplementary; the infinite quantifiers follow only from the proof above.

## Relationship to prior work

A. Chatterjee (arXiv:2611.04345v1, first posted November 3, 2026) proves an asymptotic coprimality density for irrational quadratic coefficients; it does not give rational prime-square periodicity. J. Champagne (arXiv:2607.27533v1, July 30, 2026) studies multivariate integer parts under irrational coefficient assumptions. An earlier exact-period theorem for rational monomials with **prime denominator** appears in *Exact periods and a prime-denominator transition law for rational floor-polynomial coprimality* (published-finding corpus, November 8, 2026); its hypotheses explicitly exclude composite denominators. More general rational-polynomial results provide finite-state descriptions or nonminimal periods, but they do not imply the precise exponent-dependent loss of one prime factor in the least period or the unique early exception. The derivative calculation (3) and the special multiple-of-prime calculation (2) are the additional steps here.

## Limitations

The theorem addresses only denominator \(p^2\) and a monomial with numerator coprime to \(p\). It does not assert least periods for arbitrary prime powers or composite denominators, or any joint uniform estimate in growing parameters. The literature comparison cannot eliminate an equivalent unindexed result. Source-access restrictions on some broader irrational-coefficient treatments do not affect the independently stated proof but leave limited bibliographic uncertainty.

## References

1. A. Chatterjee, *On integers n relatively prime to \(\lfloor\alpha n^2\rfloor\)*, arXiv:2611.04345v1, first public November 3, 2026, https://arxiv.org/abs/2611.04345.
2. J. Champagne, *On the greatest common divisor of \(n,\lfloor\alpha_1n\rfloor,\ldots,\lfloor\alpha_kn^k\rfloor\)*, arXiv:2607.27533v1, first public July 30, 2026, https://arxiv.org/abs/2607.27533.
3. *Exact periods and a prime-denominator transition law for rational floor-polynomial coprimality*, first public November 8, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-periods-and-a-prime-denominator-transition-law-for-rationa--b7932551eaf2/RESULT.md.
4. W. Banks and I. E. Shparlinski, *On the greatest common divisor of integer parts of polynomials*, arXiv:2205.00253v1, https://arxiv.org/abs/2205.00253.
