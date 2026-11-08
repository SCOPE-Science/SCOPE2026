# Prime-index congruence for central odd-nomial coefficients

## Finding
For every integer \(d\ge0\) and odd prime \(p\), put
\[
C_d(p)=[x^{dp}](1+x+\cdots+x^{2d})^p.
\]
Then the **complete prime-square congruence** is
\[
C_d(p)\equiv
\begin{cases}
1\pmod{p^2},&p\nmid(2d+1),\\
2^p-1\pmod{p^2},&p\mid(2d+1).
\end{cases}
\]
In particular, the correction at the exceptional primes is \(p\) times twice the Fermat quotient \((2^{p-1}-1)/p\), and is independent of the quotient \((2d+1)/p\). This congruence is valid without restrictions on the size of \(d\) relative to \(p\).

## Assumptions and scope
All coefficients and powers above are taken in the ordinary integer polynomial ring. A central \((2d+1)\)-nomial coefficient is the coefficient of degree \(dn\) in the \(n\)-th power of \(1+x+\cdots+x^{2d}\). The case \(d=0\) gives \(C_0(p)=1\). The prime \(2\) is excluded: for example, \(C_d(2)=2d+1\), which need not be \(1\pmod4\). No claim is made at composite exponents or modulo \(p^3\).

## Proof
Put \(N=2d+1\) and \(P(x)=1+x+\cdots+x^{N-1}=(1-x^N)/(1-x)\). Work in \(\mathbb Z_{(p)}[[x]]\), reducing coefficients modulo \(p^2\). Let
\[
F(x)=-\sum_{j=1}^{p-1}\frac{x^j}{j}.
\]
The binomial identity \(\binom pj\equiv p(-1)^{j-1}/j\pmod{p^2}\) for \(1\le j<p\) yields
\[
(1-x)^p\equiv 1-x^p+pF(x)\pmod{p^2}.
\]
Substitute \(x^N\) for \(x\), divide the two expansions using the invertible series \(1-x^p\), and retain terms through first order in \(p\):
\[
P(x)^p\equiv \frac{1-x^{Np}}{1-x^p}
+p\left(\frac{F(x^N)}{1-x^p}
-\frac{(1-x^{Np})F(x)}{(1-x^p)^2}\right)\pmod{p^2}.
\]
The coefficient of \(x^{dp}\) in the first term is exactly \(1\), since it is \(1+x^p+\cdots+x^{(N-1)p}\). The last term contributes zero: \(F(x)\) contains only powers \(x^j\), \(1\le j<p\), while its other factor has only powers divisible by \(p\). Therefore
\[
\frac{C_d(p)-1}{p}\equiv
-\sum_{\substack{1\le j<p\\ Nj\le dp\\p\mid Nj}}j^{-1}\pmod p.
\]
If \(p\nmid N\), then \(p\mid Nj\) requires \(p\mid j\), impossible for \(1\le j<p\), so the sum is empty.

If \(p\mid N\), write \(N=pt\), where \(t\) is odd. Because \(d=(pt-1)/2\), the condition \(Nj\le dp\) is equivalent to \(j\le\lfloor d/t\rfloor=(p-1)/2\). Thus the exceptional correction is \(-H_{(p-1)/2}\pmod p\), with \(H_m=\sum_{j=1}^m j^{-1}\) calculated in \(\mathbb F_p\).

Finally, from \(2^p=2+\sum_{j=1}^{p-1}\binom pj\) we obtain
\[
\frac{2^p-2}{p}\equiv\sum_{j=1}^{p-1}\frac{(-1)^{j-1}}{j}
\equiv-H_{(p-1)/2}\pmod p.
\]
The final equality uses \(H_{p-1}\equiv0\pmod p\) and the identity \(\sum_{j\text{ even}}j^{-1}=\tfrac12 H_{(p-1)/2}\). Multiplication by \(p\) now gives \(C_d(p)\equiv 1+(2^p-2)=2^p-1\pmod{p^2}\), as required.

## Verification
A standalone Python 3 standard-library checker `verify.py` computes central coefficients by repeated sliding-window polynomial multiplication. Independently, it computes the exact coefficient by inclusion-exclusion from \(((1-x^N)/(1-x))^p\). It compares both integer values and the theorem's residue modulo \(p^2\). Running the supplied checker gives:

```
VERIFY_OK exact_cases=319 exceptional_cases=33 primes=[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] d=0..28
```
These finite tests are not used as proof for unbounded \(p,d\); the formal-power-series argument above proves the unrestricted assertion.

## Relationship to prior work
Sun's 2010 work develops central-trinomial congruences and proves a prime-index congruence modulo \(p\) (Lemma 2.5), a weaker and narrower statement. Rudolph-Lilith and Muller (2014) give trigonometric trace formulas for the entire central odd-nomial family without the prime-square dichotomy. Mellit and Vlasenko (2013) prove higher-power Dwork congruences under a Newton-polytope hypothesis; for \(d\ge2\) the Laurent polynomial \(x^{-d}+\cdots+x^d\) has interior lattice points other than zero, so their stated theorem does not apply to this full family. Even for \(d=1\), the particular exceptional prime-square value does not follow from their displayed general theorem. The present result is a two-parameter, exact prime-index classification separating the primes dividing the alphabet size from all other primes. Literature priority is not independently certified.

## Limitations
The theorem is modulo \(p^2\), only for odd primes and prime exponent \(n=p\). At an exceptional prime satisfying \(2^{p-1}\equiv1\pmod{p^2}\) (a Wieferich prime to base \(2\)), the two displayed residues coincide; the statement is a congruence classification, not an assertion that their numerical residues are always distinct. No higher-power or composite-index generalization is proved. Older literature could express this elementary congruence under a different name; no independent mathematical review has been performed.

## References
- Zhi-Wei Sun, *Congruences involving generalized central trinomial coefficients*, arXiv:1008.3887 (first public 2010-08-23), especially Lemma 2.5.
- Anton Mellit and Masha Vlasenko, *Dwork's congruences for the constant terms of powers of a Laurent polynomial*, arXiv:1306.5811 (first public 2013-06-24), Theorem 1.
- Michelle Rudolph-Lilith and Lyle E. Muller, *On an explicit representation of central \((2k+1)\)-nomial coefficients*, arXiv:1403.5942 (first public 2014-03-24), Sections II-III.
- OEIS A005191, central pentanomial coefficients, definition and bibliography (inspected 2026-11-06 UTC).
