# Exact binomial greatest common divisors on one-digit prime-power cofactors

## Finding
For every prime \(p\), integer \(a\ge1\), and integer \(1\le m<p\) satisfying \(mp^a\ge3\), set \(k=mp^a-1\) and
\[
D(k)=\gcd_{2\le q\le k+1}\binom{qk}{k}.
\]
Then
\[
\boxed{D(mp^a-1)=p^a.}
\]
In particular, every coefficient in this gcd is divisible by \(p^a\), and no greater power of \(p\) and no different prime can divide them all. Examples include \(D(7)=8\), \(D(17)=9\), and \(D(99)=25\).

## Assumptions and scope
The gcd is the positive greatest common divisor of exactly the \(k\) positive integers \(\binom{qk}{k}\), for the full integer range \(2\le q\le k+1\). The prime \(p\) is unrestricted, including \(p=2\). The cofactor \(m\) occupies a single nonzero base-\(p\) digit: \(1\le m<p\). The restriction \(mp^a\ge3\) aligns with the standard domain \(k\ge2\); the omitted case \(k=1\) is straightforward and also satisfies the displayed equality. No assertion about a general composite cofactor \(m\ge p\) is made.

## Proof
Write \(P=p^a\), \(n=mP\), and \(k=n-1\). Three steps suffice.

**1. Upper bound \(D(k)\mid n\).** Define the polynomial
\[
F(X)=\binom{kX}{k}=\frac{(kX)(kX-1)\cdots(kX-k+1)}{k!}
\]
of degree \(k\). Its \((k+1)\)-st forward difference vanishes:
\[
0=\sum_{q=0}^{k+1}(-1)^{k+1-q}\binom{k+1}{q}F(q).
\]
Here \(F(0)=0\) and \(F(1)=1\). Every term indexed by \(2\le q\le k+1\) is divisible by \(D(k)\), whereas the term indexed by \(q=1\) is \((-1)^k(k+1)\). Therefore \(D(k)\mid k+1=n\). This is a strengthened elementary version of the prime-support consequence of the finite-difference argument in Guo et al. [2].

**2. Full \(p\)-adic lower bound.** Fix an arbitrary \(2\le q\le n\) and let \(t=q-1\). By Kummer's theorem, \(\nu_p\binom{qk}{k}\) equals the number of carries when \(k\) and \(tk\) are added in base \(p\). We prove there are at least \(a\) carries. Write
\[
t=uP+r,\qquad0\le u\le m-1,\quad0\le r<P.
\]
The low \(a\) digits of \(k=(m-1)P+(P-1)\) are all \(p-1\).

If \(r>0\), write \(v=\nu_p(r)\), so \(0\le v<a\). The exact quotient-and-remainder identity
\[
tk=(mt-u-1)P+(P-r)
\]
shows that adding \(P-1\) to \(P-r\) produces carries at positions \(v,v+1,\ldots,a-1\), a total of \(a-v\) low-block carries. For \(v=0\), this already proves the required bound. For \(v\ge1\), the carry into the next block adds to the high digit \(m-1\), so the high-block addition begins by adding \(m\) to \(H=mt-u-1\). Since \(p^v\mid t\),
\[
H\equiv-u-1\pmod{p^v}.
\]
Because \(1\le u+1\le m<p\), the last \(v\) base-\(p\) digits of \(H\) are exactly those of \(p^v-u-1\): its units digit is \(p-u-1\) and each of the remaining \(v-1\) digits is \(p-1\). Adding \(m\) to this block produces a carry in its units digit (as \(m\ge u+1\)), which then propagates through all \(v\) digits. There are at least \(v\) additional carries, for a total of \(a\).

If \(r=0\), then \(1\le u\le m-1\), and the exact identity is
\[
tk=(mt-u)P.
\]
There are no low-block carries. In the high blocks one adds \(m-1\) to \(H=mt-u\equiv-u\pmod P\). The first \(a\) digits of \(H\) form \(P-u\). Their units digit is \(p-u\), and all higher digits are \(p-1\), since \(1\le u<m<p\). As \((p-u)+(m-1)\ge p\), a carry starts and propagates across all \(a\) positions. Thus this case also has at least \(a\) carries.

Kummer's theorem proves \(p^a\mid\binom{qk}{k}\) for every eligible \(q\), hence \(p^a\mid D(k)\).

**3. Exclude other primes.** We use the proven local prime-support criterion of Guo, Qiu, Cao, Feng and Gao [2, Lemma 9]: for any prime \(\ell\) and any \(n\ge3\), if \(\ell^b\parallel n\) then
\[
\ell\mid D(n-1)\quad\Longleftrightarrow\quad n/\ell^b\le\ell^b.
\]
This criterion concerns divisibility by \(\ell\), not its exact valuation. For any prime \(\ell\mid m\), let \(\ell^b\parallel m\). Since \(m<p\), we have \(\ell\ne p\) and
\[
\frac{n}{\ell^b}=\frac m{\ell^b}P\ge P\ge p>m\ge\ell^b.
\]
The criterion therefore gives \(\ell\nmid D(k)\). Step 1 shows that no prime outside \(mp^a\) divides \(D(k)\). Step 2 gives \(p^a\mid D(k)\), and Step 1 gives \(D(k)\mid mp^a\); excluding primes of \(m\) forces \(D(k)=p^a\), as claimed.

## Verification
Run `python3 verify.py` with the Python standard library. The script computes exact Legendre-factorial valuations for a bounded collection of all allowable triples, compares selected valuations with independently implemented base-\(p\) carry counts, checks that the minimum valuation over every multiplier is exactly \(a\), and computes the complete integer gcd directly for every tested \(n\le135\). Its successful replay reports `VERIFY_OK valuation_pairs= 78683 carry_checks= 2779 direct_gcd_cases= 80`. These are finite checks, not an infinite proof; the unrestricted argument is above.

## Relationship to prior work
OEIS A080170, created by Benoit Cloitre on 2003-01-31, asks when the same fixed-lower-index binomial gcd equals one [1]. Guo et al. [2, Theorem 1 and Lemma 9] proved its exact criterion for being \(1\) and established a local first-power divisibility criterion for every prime. Their result decides whether a prime occurs in the gcd, but does not give the full positive integer gcd or the \(p\)-adic exponent on the one-digit cofactor family. The present finding determines that exact exponent and shows the gcd saturates the complete prime-power factor \(p^a\). The earlier paper's finite-difference and local prime-support arguments are credited and used as indicated; the uniform \(a\)-carry proof in Step 2 is the new component.

Earlier research by Joris, Oestreicher and Steinig [3] treats gcds in regions of Pascal's triangle; [2, Introduction] distinguishes those selected sets from the present varying-upper-index, fixed-lower-index family. The full 1985 paper was not accessible for source-level comparison, leaving a historical-priority risk. This finding does not claim to resolve the full exact-gcd problem for arbitrary \(k\).

## Limitations
The statement is restricted to \(1\le m<p\); an exact formula for arbitrary cofactors is not established. The proof invokes the independently published prime-support criterion [2] and Kummer's classical theorem [4], both stated with their applicable hypotheses. Bounded computation does not certify all cases. Historical-priority uncertainty remains because not every earlier paper was fully accessible.

## References
[1] Benoit Cloitre, OEIS A080170, *Numbers \(k\) such that gcd of \(\binom{2k}{k},\ldots,\binom{(k+1)k}{k}\) is one*, created 2003-01-31. https://oeis.org/A080170

[2] D. Guo, R. Qiu, Y. Cao, R. Feng and X.-S. Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997 (first submitted 2026-06-22), especially §2.2, Lemma 9, and §2.6. https://arxiv.org/abs/2606.22997

[3] H. Joris, C. Oestreicher and J. Steinig, *The greatest common divisor of certain sets of binomial coefficients*, *J. Number Theory* 21 (1985), 101–119. https://doi.org/10.1016/0022-314X(85)90013-7

[4] E. E. Kummer, 1852, classical theorem counting prime valuations of binomial coefficients by base-prime addition carries.
