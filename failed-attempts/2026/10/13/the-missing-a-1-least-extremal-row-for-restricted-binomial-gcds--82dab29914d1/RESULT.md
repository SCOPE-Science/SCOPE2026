# The missing \(a=1\) least extremal row for restricted binomial GCDs
## Finding
Let \(p\) be any prime and put \(m=p+1\). For an admissible row \(N=mq\) with \(q\ge2\), define
\[
G(N;m)=\gcd\left\{\binom{N}{k}:0<k<N,\ m\mid k\right\}.
\]
Then the complete profile through the first extremal row is
\[
v_p(G((p+1)q;p+1))=0\quad(2\le q<p),
\]
and
\[
v_p(G(p(p+1);p+1))=2.
\]
In fact, at \(q=p\) every selected coefficient \(\binom{p(p+1)}{(p+1)d}\), \(1\le d<p\), has \(p\)-adic valuation exactly \(2\). Since \(p<p+1<p^2\), the extremal value in the notation of arXiv:2610.01328v1 is \(r_p(p+1)=2\). Consequently
\[
T_p(p+1)=p(p+1).
\]
Thus the boundary case \(a=1\), explicitly excluded from the published formula for \(m=p^a+1\) with \(a\ge2\), has a different and much smaller least extremal row.
## Assumptions and scope
The prime \(p\) is arbitrary, including \(p=2\). The restriction parameter is exactly \(m=p+1\). An admissible row is an integer \(N>m\) divisible by \(m\), hence uniquely \(N=mq\) with \(q\ge2\). The least extremal row \(T_p(m)\) is the least admissible \(N\) satisfying
\[
v_p(G(N;m))=r_p(m),\qquad r_p(m)=\min\{r\ge1:m<p^r\}.
\]
No statement is made here about \(T_p(m)\) for restriction parameters outside this boundary family.
## Proof
Because \(p<p+1<p^2\), one has \(r_p(p+1)=2\).

First let \(2\le q<p\), put \(N=(p+1)q\), and choose any selected multiplier \(d\) with \(1\le d<q\). Then
\[
N=qp+q,\qquad (p+1)d=dp+d,
\]
and
\[
N-(p+1)d=(q-d)p+(q-d).
\]
All displayed coefficients \(q,d,q-d\) lie in \(\{0,1,\ldots,p-1\}\). In base \(p\), adding the last two quantities produces no carry in the units column because
\[
d+(q-d)=q<p,
\]
and no carry in the \(p\)-column for the same reason. Kummer's theorem therefore gives
\[
v_p\binom{(p+1)q}{(p+1)d}=0
\]
for every \(1\le d<q\). Hence
\[
v_p(G((p+1)q;p+1))=0
\]
for every \(2\le q<p\).

Now take \(q=p\), so
\[
N=p(p+1)=p^2+p.
\]
For \(1\le d<p\), write
\[
k=(p+1)d=dp+d,
\]
and
\[
N-k=(p-d)p+(p-d).
\]
In base \(p\), the units digits add to \(p\), producing one carry. In the next column the two digits again sum to \(p\), and the incoming carry makes the column sum \(p+1\), producing a second carry. The resulting carry enters the \(p^2\)-column and terminates there. Thus there are exactly two carries, and Kummer's theorem gives
\[
v_p\binom{p(p+1)}{(p+1)d}=2
\]
for every \(1\le d<p\). Therefore
\[
v_p(G(p(p+1);p+1))=2=r_p(p+1).
\]
Every admissible row smaller than \(p(p+1)\) has multiplier \(2\le q<p\) and was shown nonextremal, so \(p(p+1)\) is the least extremal row.
## Verification
The proof is purely symbolic and uses only the carry form of Kummer's theorem. The accompanying `verify.py` independently replays the carry count for every prime \(p\le97\), checks all smaller multipliers \(2\le q<p\), and directly compares with exact integer binomial valuations for every prime \(p\le43\). It returns

`VERIFY_OK primes=25 max_prime=97 smaller_multipliers_zero=1 target_multiplier_two_carries=1 direct_binomial_checks_through=43`

The finite replay is a consistency check, not the infinite proof; the universal quantifiers are discharged by the two base-\(p\) digit calculations above.
## Relationship to prior work
arXiv:2610.01328v1 defines the same restricted GCD and proves the sharp maximum \(r_p(m)\) for general \(m\) with \(p\nmid m\). For the special family \(m=p^a+1\), it proves
\[
T_p(p^a+1)=p^{3a}+1\qquad(a\ge2),
\]
but Remark 8.3 explicitly excludes \(a=1\), and Remark 8.4 records only the already known instance \(T_2(3)=6\). The result above supplies the omitted boundary uniformly for every prime \(p\).

McTague's theorem for the same multiple-index GCD gives a \(0/1\)-valuation criterion when the valuation prime is congruent to \(1\) modulo the restriction parameter; that hypothesis does not apply here because the valuation prime is \(p<p+1\). McTague also records the exceptional valuation-two example \((p,m,N)=(2,3,6)\), which is exactly the \(p=2\) member of the present formula. Wu's 2026 paper studies the same family and gives formulas under other structural hypotheses; the recent extremal paper identifies the \(a=1\) least-row regime as outside its proved special-family theorem.
## Limitations
The theorem resolves only the natural boundary \(m=p+1\). It does not classify least extremal rows for arbitrary \(m\), nor does it extend the \(a\ge2\) formula beyond the family \(m=p^a+1\). Historical uniqueness cannot be proved by search; the originality assessment is limited to the inspected literature and semantic/database searches described in `AUDIT.json`.
## References
1. J. Fairfax-Ball, *Sharp \(p\)-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs*, arXiv:2610.01328v1, 2026.
2. C. McTague, *On the Greatest Common Divisor of Binomial Coefficients \(\binom{n}{q},\binom{n}{2q},\binom{n}{3q},\ldots\)*, arXiv:1510.06696v5; *Amer. Math. Monthly* 124 (2017), 353--356.
3. C. W. Wu, *Computing the Greatest Common Divisor of Binomial Coefficients \(\binom{mn}{mk}\)*, arXiv:2606.20940v2, 2026.
4. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, *J. Reine Angew. Math.* 44 (1852), 93--146.
