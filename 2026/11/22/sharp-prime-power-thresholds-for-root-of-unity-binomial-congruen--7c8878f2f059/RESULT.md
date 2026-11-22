# Sharp prime-power thresholds for root-of-unity binomial congruences in the first near-prime band

## Finding
For every prime \(p\ge5\) and integer \(p+1\le t\le2p-1\), write \(d=p^r\) for any integer \(r\ge1\). The root-of-unity-averaged binomial congruence introduced by Miska holds for **all** integer inputs if and only if
\[
1\le r\le 2t-p+1.
\]
Equivalently, the prime-power exponents in this entire two-parameter band form an exact initial segment, with a constructive failure beyond its endpoint.

## Assumptions and scope
For \(m\ge0\) define the generalized binomial polynomial \(\binom zm=z(z-1)\cdots(z-m+1)/m!\), with \(\binom z0=1\). Put \(\zeta_t=\exp(2\pi i/t)\) and
\[
G_{t,d,m}(n)=\frac1t\sum_{s=0}^{t-1}\binom{n+d\zeta_t^s}{m}-\binom nm.
\]
The root-of-unity filter makes this a rational number for every integer \(n\), and congruence modulo \(p^r\) means \(p\)-adic valuation at least \(r\). The claim concerns \(G_{t,p^r,p^r-1}(n)\) for all \(n\in\mathbb Z\). Its proof also gives a sharper explicit valuation for an intermediate degree used as a witness, without asserting the same valuation at degree \(p^r-1\).

## Proof
Set \(L=2t-p+1\). For any \(0\le m<d=p^r\), evaluation at \(n=-1\) and root-of-unity filtering give the exact identity
\[
G_{t,d,m}(-1)=(-1)^m\sum_{k\ge1,\,kt\le m}(-1)^{kt}e_{kt}(d,\,d/2,\,\ldots,\,d/m),
\]
where \(e_h\) is the elementary symmetric function of degree \(h\). Each \(d/i\) for \(1\le i<d\) has valuation \(r-\nu_p(i)\ge1\). There are at most \(p-1\) indices with valuation exactly one, namely \(i=up^{r-1}\) with \(1\le u\le p-1\). In any product containing \(kt\ge t>p-1\) distinct factors, at least \(kt-(p-1)\) factors have valuation at least two; the product valuation is at least \(2kt-(p-1)\ge L\). Consequently every filtered coefficient above has valuation at least \(L\), and \(G_{t,d,m}(-1)\equiv0\pmod{p^r}\) for every \(m<d\) whenever \(r\le L\).

The generalized Pascal identity gives
\[
G_{t,d,m}(n+1)-G_{t,d,m}(n)=G_{t,d,m-1}(n).
\]
Since the initial row \(m=0\) vanishes, induction on \(m\) and then forward/backward integer differences propagate all congruences from \(n=-1\) to every integer \(n\). In particular they hold for \(m=d-1\). This proves sufficiency for \(1\le r\le L\).

To prove necessity, suppose \(r>L\); then \(r\ge2\). Define
\[
j=t-p+1\in\{2,\ldots,p\},\qquad
q=\begin{cases}j,&j\le p-2,\\0,&j=p-1,\\1,&j=p,\end{cases}\qquad
K=p(p-1)+q,\qquad c=Kp^{r-2}.
\]
Here \(t\le c<d\). The list \(d/i\), for \(1\le i\le c\), has exactly \(p-1\) factors of valuation one (at \(i=up^{r-1}\)), exactly \((p-1)^2+q\) of valuation two (at \(i=up^{r-2}\) with \(1\le u\le K\) and \(p\nmid u\)), and all remaining factors have valuation at least three. Because \(t=(p-1)+j\), the coefficient of \(p^L\) in \(e_t(d,\ldots,d/c)\) modulo \(p\) is the product of all normalized valuation-one factors times the degree-\(j\) symmetric polynomial of normalized valuation-two factors:
\[
\frac{e_t(d,d/2,\ldots,d/c)}{p^L}\equiv
\left(\prod_{u=1}^{p-1}u^{-1}\right)[X^j]
\prod_{\substack{1\le u\le K\\p\nmid u}}(1+u^{-1}X)\pmod p.
\]
All inverses and products in this displayed congruence are in \(\mathbb F_p\). Each nonzero residue appears \(p-1\) times among \(1\le u\le p(p-1)\), so
\[
\prod_{\substack{1\le u\le K\\p\nmid u}}(1+u^{-1}X)
\equiv (1-X^{p-1})^{p-1}\prod_{u=1}^{q}(1+u^{-1}X)
\equiv (1+X^{p-1})\prod_{u=1}^{q}(1+u^{-1}X)
\pmod{(p,\,X^{p+1})}.
\]
The degree-\(j\) coefficient is \(1/j!\not\equiv0\pmod p\) when \(2\le j\le p-2\) (since \(q=j\)), and is \(1\pmod p\) when \(j=p-1\) or \(j=p\) (since \(q=0\) or \(q=1\)). Thus \(\nu_p(e_t)=L\). Terms of degree \(kt\) for \(k\ge2\) have valuation at least \(2kt-(p-1)>L\), so no cancellation at valuation \(L\) is possible. Therefore
\[
\nu_p(G_{t,p^r,c}(-1))=L<r.
\]
If the congruence at degree \(d-1\) held for every integer input, repeated use of the Pascal finite-difference identity would imply that it held at every degree \(c<d\), contradicting this witness. Necessity follows.

## Verification
A standalone exact-integer/finite-field checker is supplied as `check_miska_band.py`. It checks the nonzero leading residue in 72 \((p,t)\) cases for primes \(p\in\{5,7,11,13,17,19\}\), including 66 in the theorem's domain and six boundary controls at \(t=p\). It also computes the filtered discrepancy from the whole product for six feasible \((p,t,r)\) test cases, rather than using the abbreviated leading-coefficient expression. All tests passed. The infinite theorem rests on the symbolic proof, not on finite enumeration.

## Relationship to prior work
Piotr Miska, *Binomial coefficients, roots of unity and powers of prime numbers*, arXiv:2203.03281v1 (first publicly posted 2022-03-07), Bulletin of the Malaysian Mathematical Sciences Society, DOI 10.1007/s40840-022-01266-4, introduced the condition and obtained partial exponent ranges. His Corollary 3.11 proves the sufficient bound \(r\le2t-p+1\) in the present band; Proposition 3.7 proves failure for \(r>2t-1\). The intervening exponents were not resolved by those implications; the present result proves failure throughout that intervening range by a deliberately selected finite-difference witness. Miska's extra prime-power result for \(t=p^u\) does not cover \(p+1\le t\le2p-1\). The first half of the proof above is included for self-containment; the new boundary is the exact converse.

## Limitations
The theorem is restricted to odd primes \(p\ge5\) and the indicated first near-prime band of \(t\), not all composite moduli or higher bands. It establishes exact existence and failure of a rational congruence, not primality, independent certification, or any unconditional claim about all possible equivalent uncatalogued literature. Its finite checker is supplementary.

## References
- P. Miska, *Binomial coefficients, roots of unity and powers of prime numbers*, arXiv:2203.03281v1 (2022-03-07), https://arxiv.org/pdf/2203.03281 .
- P. Miska, *Binomial Coefficients, Roots of Unity and Powers of Prime Numbers*, Bulletin of the Malaysian Mathematical Sciences Society (2022), https://doi.org/10.1007/s40840-022-01266-4 .
