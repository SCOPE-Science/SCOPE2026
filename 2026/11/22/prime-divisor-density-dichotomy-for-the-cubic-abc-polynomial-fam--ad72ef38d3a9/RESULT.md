# Prime-divisor density dichotomy for the cubic ABC polynomial family

## Finding

For each integer \(u\), put
\[
F_u(X)=X(X-1)(X-u)+1=X^3-(u+1)X^2+uX+1.
\]
For a rational prime \(p\), let \(R_u(p)\) be the number of distinct solutions \(x\in\mathbb F_p\) to \(F_u(x)=0\). Fix \(u\) and let \(p\) range over rational primes. The complete natural densities of the three possible root counts away from finitely many discriminant primes are

| Integer parameter | \(R_u(p)=0\) | \(R_u(p)=1\) | \(R_u(p)=3\) |
|---|---:|---:|---:|
| \(u\in\{-4,3\}\) | \(2/3\) | \(0\) | \(1/3\) |
| \(u\notin\{-4,3\}\) | \(1/3\) | \(1/2\) | \(1/6\) |

In particular, the set of primes dividing at least one integer value \(F_u(n)\), for \(n\in\mathbb Z\), has natural density exactly \(1/3\) for \(u=-4,3\), and exactly \(2/3\) for every other integer \(u\). These are the only exceptional integer parameters.

For \(u=-4\) and \(u=3\), the two irreducible cubic fields are both isomorphic to the real cubic subfield of the seventh cyclotomic field. Consequently, for **every** \(p\ne7\),
\[
R_{-4}(p)=R_3(p)=\begin{cases}3,&p\equiv1\text{ or }-1\pmod7,\\0,&\text{otherwise}.\end{cases}
\]
For every fixed \(u\), all primes \(p\) not dividing the discriminant satisfy \(R_u(p)\in\{0,1,3\}\), and for each integer \(k\ge1\) the number of solutions modulo \(p^k\) is exactly \(R_u(p)\). Thus the table also describes the prime-by-prime density spectrum at every fixed prime-power depth, with the discriminant primes excluded.

## Assumptions and scope

The parameter \(u\) is any **fixed** integer, including negative integers and zero. The variable \(p\) ranges over positive rational primes. Density is relative to all primes: \(\lim_{X\to\infty}\#\{p\le X:\mathcal P(p)\}/\pi(X)\). The number \(R_u(p)\) counts distinct residue roots rather than roots with multiplicity. The polynomial discriminant is
\[
\Delta_u=(u^2+u-3)^2-32.
\]
All polynomial-discriminant primes form a finite excluded set for each fixed \(u\). The density statements are not claimed uniformly as \(u\) varies with \(X\). No assertion about the divisibility of terms of an arbitrary recurrence with characteristic polynomial \(F_u\) is implied.

## Proof

**1. Irreducibility and discriminant.** Since \(F_u\) is monic with constant term \(1\), every rational root must be \(1\) or \(-1\). Direct substitution gives \(F_u(1)=1\) and \(F_u(-1)=-2u-1\), neither of which is zero for integral \(u\). Thus \(F_u\) is irreducible over \(\mathbb Q\) for every integer \(u\). The standard monic cubic discriminant identity, applied to the coefficients \(-(u+1),u,1\), gives
\[
\operatorname{disc}(F_u)=u^4+2u^3-5u^2-6u-23=(u^2+u-3)^2-32.
\]
In particular it never vanishes at an integer parameter.

**2. Exhaustive cyclic-field exceptions.** An irreducible cubic over \(\mathbb Q\) has Galois group \(C_3\) exactly when its discriminant is a square in \(\mathbb Q\); otherwise the group is \(S_3\). Since \(\Delta_u\) is integral, a rational square \(\Delta_u\) is an integer square. Write \(m=u^2+u-3\), an odd integer at least \(-3\). If \(m^2-k^2=32\) with \(k\in\mathbb Z\), then \(m\) and \(k\) have the same parity, so
\[
a=(m-k)/2,\qquad b=(m+k)/2,\qquad ab=8,\qquad m=a+b.
\]
Because \(m\) is odd, the integer factor pairs of \(8\) require \(m=9\) or \(m=-9\). The bound \(m\ge-3\) leaves \(m=9\). Hence \(u^2+u=12\), or \((u-3)(u+4)=0\). Both cases have \(\Delta_u=49\). This proves that \(C_3\) occurs exactly at \(u=3,-4\), and \(S_3\) elsewhere, without an unbounded search.

**3. Explicit common exceptional field.** Put \(\zeta=\exp(2\pi i/7)\) and \(z=\zeta+\zeta^{-1}\). Its minimal polynomial is \(m_7(Z)=Z^3+Z^2-2Z-1\). Polynomial reduction modulo \(m_7(Z)\) yields the exact identities
\[
F_3(1-z)=0,\qquad F_{-4}(-4+z+2z^2)=0.
\]
Each root has degree three by Step 1; therefore both fields equal \(\mathbb Q(z)\), the unique real cubic subfield of \(\mathbb Q(\zeta_7)\). At each \(p\ne7\), Frobenius acts trivially on this subfield exactly when its residue modulo seven belongs to \(\{1,-1\}\). Consequently \(F_3\) and \(F_{-4}\) have three distinct roots precisely in those two residue classes, and no roots otherwise. Dirichlet's theorem gives densities \(2/6=1/3\) and \(4/6=2/3\).

**4. General prime-root distributions.** Let \(u\notin\{-4,3\}\). By Step 2 its splitting field has Galois group \(S_3\), acting on the three roots. For primes \(p\nmid\Delta_u\), the factor-degree partition of the reduction \(F_u\pmod p\) equals the cycle type of Frobenius. In \(S_3\), the two 3-cycles have no fixed root, the three transpositions have exactly one fixed root, and the identity has three fixed roots. Chebotarev's density theorem therefore gives respective proportions \(2/6\), \(3/6\), and \(1/6\). Step 3 gives the analogous \(C_3\) proportions. A prime divides some integer \(F_u(n)\) exactly when \(F_u\) has a residue root modulo that prime. Adding the one- and three-root densities proves the stated \(1/3\) versus \(2/3\) dichotomy.

**5. Good prime powers.** For \(p\nmid\Delta_u\), the reduction has no repeated root. Every root modulo \(p\) is simple and lifts uniquely modulo \(p^k\) for each \(k\ge1\) by Hensel's lemma. Reduction of any solution modulo \(p^k\) gives a root modulo \(p\), so these lifts are exhaustive. This proves the prime-power assertion.

## Verification

The accompanying executable `check_prime_spectrum.py` uses the standard Python library only. Run `python3 check_prime_spectrum.py`. It checks the symbolic cubic discriminant against its expanded coefficient formula and exhaustively tests the proposed square-discriminant classification on \(-1000\le u\le1000\). Integer polynomial reduction verifies both explicit cyclotomic field identities. It then checks \(4153\) good-prime parameter pairs, all within \(-30\le u\le30\) and primes at most \(347\), including the exceptional congruence criterion and unique root lifts modulo \(p^3\). All tests passed. Such finite computations do **not** prove the infinitely quantified theorem; Steps 1–5 give the proof.

## Relationship to prior work

Pethő's 2026 treatment of linear recurrences with characteristic polynomial \(XQ(X)(X-u)+1\) includes this cubic specialization at \(Q(X)=X-1\), but addresses common recurrence values, not the exact classification of exceptional cubic splitting fields or prime-divisor densities. Halter-Koch, Lettl, Pethő, and Tichy (1999), Section 3, establish generic full symmetric Galois groups in much broader ABC families using thin-set methods; that almost-everywhere result does not determine the complete integer exceptional set in this fixed cubic specialization. The current theorem makes that exceptional set explicit and identifies its arithmetic prime-divisor consequence. Earlier finite-field counts across the variable parameter \(u\) address a different quantifier than the present fixed-integer-parameter prime-density limit.

## Limitations

The main theorem applies to cubic specializations with \(Q(X)=X-1\), not arbitrary higher-degree ABC polynomials. It determines densities, not uniform effective error estimates in \(u\). The exact root-count assertions at prime powers exclude the finite set of discriminant primes, where multiple residue roots can occur. Neither exact counts of recurrence-term prime divisors nor a distribution for varying parameters are claimed. The result uses established Chebotarev and Hensel theorems, and an unindexed earlier explicit classification for this specialization remains a literature risk.

## References

1. A. Pethő, *Common values of linear recurrences related to Ankeny-Brauer-Chowla polynomials*, arXiv:2611.17962v1, first posted 13 November 2026, https://arxiv.org/abs/2611.17962.
2. F. Halter-Koch, G. Lettl, A. Pethő, R. F. Tichy, *Thue equations associated with Ankeny–Brauer–Chowla number fields*, J. London Math. Soc. **60** (1999), 1–20, https://doi.org/10.1112/S0024610799007474.
3. A. Noubissie, R. F. Tichy, *Large common values of generalized Ankeny-Brauer-Chowla recurrences*, arXiv:2606.27885v1 (2026), https://arxiv.org/abs/2606.27885.
4. K. Conrad, *Galois Theory at Work*, discussion of the cubic discriminant and the alternating subgroup criterion, https://kconrad.math.uconn.edu/blurbs/galoistheory/galoisapp.pdf.
