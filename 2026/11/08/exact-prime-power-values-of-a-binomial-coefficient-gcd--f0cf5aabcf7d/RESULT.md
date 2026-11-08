# Exact prime-power values of a binomial-coefficient gcd

## Finding

For each integer \(k\ge 2\), define the positive integer
\[
D(k)=\gcd_{2\le q\le k+1}\binom{qk}{k}.
\]
Put \(n=k+1\). For each prime \(p\mid n\), write \(n=p^a b\), where \(a\ge1\) and \(p\nmid b\), and put \(t=\lfloor\log_p b\rfloor\) (so \(p^t\le b<p^{t+1}\)). Then the exact prime factorization is
\[
\boxed{D(k)=\prod_{p^a\parallel k+1}p^{\max\{0,a-\lfloor\log_p((k+1)/p^a)\rfloor\}}.}
\]
In particular, \(D(k)\) is always either \(1\) or a power of a **single** prime. If \(D(k)>1\), its supporting prime \(p\) is characterized by the unique prime-power component \(p^a\parallel k+1\) satisfying \(p^a>(k+1)/p^a\); the exponent equals \(a-\lfloor\log_p((k+1)/p^a)\rfloor\). Explicit examples are \(D(11)=2\), \(D(23)=4\), \(D(35)=3\), \(D(71)=3\), and \(D(99)=25\).

## Assumptions and scope

The gcd is over the nonempty finite range of integers \(2\le q\le k+1\). The symbol \(p^a\parallel n\) means that \(p^a\mid n\) but \(p^{a+1}\nmid n\). All logarithmic floors are integer comparisons, not floating-point operations. The theorem holds for every integer \(k\ge2\), without primality or squarefreeness assumptions. Standard inputs are Kummer's carry theorem for binomial valuations and the prime-support and zero-versus-positive criteria proved by Guo, Qiu, Cao, Feng and Gao in their 2026 paper cited below.

## Proof

Fix \(n=k+1\) and a prime \(p\mid n\), with \(n=p^a b\), \(p\nmid b\), and \(t=\lfloor\log_p b\rfloor\). We shall prove
\[
\min_{2\le q\le n}\nu_p\binom{q(n-1)}{n-1}=\max\{0,a-t\}.
\]

**Prime support and the zero branch.** Guo et al., Lemma 4, show that every prime divisor of \(D(k)\) divides \(n\). Their Lemma 9 further shows that for \(p^a\parallel n\), \(p\nmid D(k)\) if and only if \(b>p^a\). This establishes the asserted zero exponent whenever \(a\le t\): since \(p\nmid b\), equality \(b=p^a\) cannot occur, so \(a\le t\) entails \(b>p^a\). These two prior results are used as proven inputs; their novelty is not claimed here.

**A carry lower bound when \(a>t\).** Write \(K=n-1\). For an arbitrary \(q\in[2,n]\), let \(r=q-1\) and \(j=\nu_p(r)\). Kummer's theorem says that \(\nu_p\binom{qK}{K}\) is the total number of carries when adding \(K\) and \(rK\) in base \(p\). A carry across the \(p^h\) place occurs precisely when the least nonnegative residues of \(K\) and \(rK\) modulo \(p^h\) sum to at least \(p^h\).

For every \(j<h\le a\), we have \(K\equiv-1\pmod{p^h}\) and \(rK\equiv-r\pmod{p^h}\), while \(p^h\nmid r\). Their residues are therefore \(p^h-1\) and a strictly positive integer, so a carry occurs. This supplies \(a-j\) carries if \(j<a\).

If \(j\le t\), that already gives at least \(a-t\) carries. If \(j>t\), consider instead every integer \(h\) satisfying \(a+t<h\le a+j\). Since \(b<p^{t+1}\), we have \(K=n-1<p^{a+t+1}\le p^h\); moreover \(r\le K<p^h\). Because \(p^{a+j}\mid rn\), the residue of \(rK=r(n-1)\) modulo \(p^h\) equals \(p^h-r\). Therefore \(K+(p^h-r)\ge p^h\), giving an additional \(j-t\) carries, all at levels strictly above \(a\). Combining the disjoint ranges gives at least
\[
\max\{0,a-j\}+(j-t)\ge a-t.
\]
This proves the universal lower bound for all \(q\).

**An explicit upper-bound witness.** If \(b=1\), take \(q=2\): the number \(K=p^a-1\) has exactly \(a\) base-\(p\) digits all equal to \(p-1\), and adding \(K+K\) produces exactly \(a\) carries. Here \(t=0\), as required.

Suppose \(b>1\), and set \(m=b-1\). Because \(a>t\), we have \(m<b<p^a\). For any integer \(s\in[1,m]\), put \(q=1+p^a s\), which satisfies \(2\le q\le n\). The base-\(p\) trailing \(a\) digits in both \(qK=p^a(m+sK)+(p^a-1)\) and \(K=p^a m+(p^a-1)\) contribute no valuation to the factorial formula. Consequently,
\[
\nu_p\binom{qK}{K}=\nu_p\binom{m+sK}{m}.
\]
Using \(sK=sn-s\), the numerator factors in the latter binomial coefficient are \(sn+(i-s)\), for \(1\le i\le m\). Their \(p\)-valuations equal \(\nu_p(i-s)\) for \(i\ne s\), since \(0<|i-s|<p^a\), \(p^a\mid sn\), and therefore \(\nu_p(i-s)<a\); the factor with \(i=s\) is \(sn\), of valuation \(a+\nu_p(s)\). Cancelling \(m!\) gives the exact identity
\[
\boxed{\nu_p\binom{qK}{K}=a-\nu_p\binom m s.}
\]
If \(t=0\), take \(s=1\), since \(1\le m<p\) and \(\nu_p\binom m1=0\). If \(t\ge1\), write \(b=up^t+v\), with \(1\le u<p\) and \(1\le v<p^t\); the latter lower bound holds since \(p\nmid b\). Choose \(s=v\). In base \(p\), adding \(s=v\) to \(m-s=up^t-1\) causes exactly \(t\) carries: the lowest \(t\) digits of \(up^t-1\) are all \(p-1\), the units digit of \(v\) is nonzero, and the carry stops at the \(p^t\) digit because \(u<p\). Kummer thus gives \(\nu_p\binom m s=t\), proving the upper bound \(a-t\).

**Prime-power support.** If two distinct prime-power components \(p^a\parallel n\) and \(r^c\parallel n\) gave positive exponents, both would strictly exceed their complementary cofactors and hence both exceed \(\sqrt n\). Their product divides \(n\), an impossibility. This completes the proof of the formula and the single-prime-power corollary.

## Verification

Run the embedded standalone script with Python 3.10 or newer: `python verify_binomial_gcd.py`. No packages beyond the Python standard library are required. The script independently checks exact gcds computed from integer binomial coefficients for \(3\le n\le100\), all individual prime-adic minima using base-\(p\) carries for \(3\le n\le700\), selected valuations by an independent factorial method, and the explicit witnesses for all positive prime-power components with \(3\le n\le5000\). Observed output is recorded in `VERIFICATION.md`.

## Relationship to prior work

Guo, Qiu, Cao, Feng and Gao (2026) introduced exactly this finite binomial-coefficient gcd and proved the criterion for it to equal one, together with the prime-support lemma and the local criterion for the presence of a prime. Their full publicly available paper, including the proofs and stated results, does not give the **exact exponent** of a prime in the gcd or an explicit valuation-attaining index. Those form the principal new contribution; the single-prime-power consequence can already be deduced from their prime-support criterion and is included only for completeness. The source lemmas are acknowledged dependencies. OEIS A080170 records the unity-index set, not these values. Wu (2026) studies gcds of coefficients in a *fixed binomial row*, a different parameter pattern. Other fixed-row gcd literature may overlap via an unrecognized reduction, so independent historical-priority verification remains appropriate.

## Limitations

The proof uses two published lemmas for the prime support and the zero-exponent branch; it does not independently reprove these cited results. The exact arithmetic experiments are finite checks, not proofs for all \(k\). Absence of an equivalent published historical theorem is not mathematically certified. No independent mathematical audit was performed.

## References

- Guo, Qiu, Cao, Feng, and Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1 (first public posting June 22, 2026), https://arxiv.org/abs/2606.22997 .
- N. J. A. Sloane et al., OEIS A080170, https://oeis.org/A080170 (sequence of parameters yielding gcd one).
- Chai Wah Wu, *Computing the Greatest Common Divisor of Binomial Coefficients*, arXiv:2606.20940 (June 2026), https://arxiv.org/abs/2606.20940 .
- Kummer's theorem on prime-adic valuations of binomial coefficients, classical standard result.
