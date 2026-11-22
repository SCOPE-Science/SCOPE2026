# Exact adjacent trinomial quotient spectra and a sharp extremal reversal

## Finding
For every odd prime \(p\) and every positive integer \(r\), form the trinomial (three-part multinomial) coefficient
\[
M(a,b,c)=\frac{(a+b+c)!}{a!b!c!}.
\]
Consider ordered triples of nonnegative integers with \(a\ge1\) and \(a+b+c<p^r\). Retain only triples for which \(M(a,b,c)\) and \(M(a-1,b+1,c)\) are both units modulo \(p\), and record their quotient \(u=M(a-1,b+1,c)/M(a,b,c)\pmod p\).

Write \(H_{p,r}(u)\) for the number of retained triples with quotient \(u\in\mathbb F_p^\times\), and let \(\langle t\rangle_p\) denote the unique integer in \(\{1,\ldots,p-1\}\) congruent to the nonzero residue \(t\pmod p\). Put
\[
Q_p=\binom{p+2}{3},\quad S_r=\sum_{j=0}^{r-1}Q_p^j,\quad
N_p(u)=\sum_{y=1}^{p-1}\max\{0,p+1-y-\langle uy\rangle_p\}.
\]
Then the **complete quotient spectrum** is
\[
\boxed{H_{p,r}(u)=S_rN_p(u)\quad(u\in\mathbb F_p^\times).}
\]
In particular, the conditional quotient law is independent of \(r\), because
\[
\sum_{u\in\mathbb F_p^\times}H_{p,r}(u)=\binom{p+1}{3}S_r.
\]
For every prime \(p\ge5\), it has **unique and reversed extrema**:
\[
\boxed{N_p(-1)=p-1<N_p(u)<\frac{p^2-1}{4}=N_p(1)
\quad\text{for }u\notin\{-1,1\}.}
\]
For \(p=3\), both values occur with \(N_3(1)=N_3(-1)=2\). In the corresponding binomial-neighbor problem, the quotient \(-1\) is instead the most frequent: the third multinomial coordinate reverses its extremal role.

## Assumptions and scope
The prime \(p\) is odd, \(r\) is a positive integer, \(a,b,c\) are nonnegative, \(a\ge1\), and \(a+b+c<p^r\). Divisions modulo \(p\) are taken only after both actual integer trinomial coefficients are known to be units. The closed finite sum \(N_p(u)\) describes **every** nonzero quotient, not only its extrema. No assertion is made about the quotient when either coefficient is divisible by \(p\).

## Proof

**1. Lucas admissibility and a unique decisive digit.** Write all coordinates in base \(p\) using exactly \(r\) digit positions. The multinomial form of Lucas's theorem says that \(M(a,b,c)\) is a unit precisely when the three digits sum to at most \(p-1\) at every position; the same applies to \((a-1,b+1,c)\). Since the exact integer quotient is
\[
\frac{M(a-1,b+1,c)}{M(a,b,c)}=\frac{a}{b+1},
\]
unitness of both coefficients forces \(\nu_p(a)=\nu_p(b+1)=j\) for some \(0\le j<r\). At each position below \(j\), the three original digits are necessarily \((0,p-1,0)\), and the neighboring digits are \((p-1,0,0)\); both have sum \(p-1\). At position \(j\), write the original first digit as \(x\in\{1,\ldots,p-1\}\), and the original second digit plus one as \(y\in\{1,\ldots,p-1\}\). The third digit \(z\) may be any integer satisfying \(0\le z\le p-x-y\). In higher positions the two triples have identical, unconstrained (except for no-carry) digit triples. Finally \(u\equiv x/y\pmod p\), because the common \(p^j\) cancels.

**2. Exact count.** At any higher digit there are \(Q_p=\binom{p+2}{3}\) triples of digits with sum at most \(p-1\). For a specified positive residue \(u\), each \(y\in\{1,\ldots,p-1\}\) forces \(x=\langle uy\rangle_p\), leaving \(\max\{0,p+1-x-y\}\) choices of \(z\). Thus a decisive position \(j\) contributes \(N_p(u)Q_p^{r-j-1}\), and summing positions gives \(H_{p,r}(u)=N_p(u)S_r\). Summing over quotients is equivalent to counting positive \(x,y\), nonnegative \(z\), and a slack variable with \(x+y+z\le p\); the number is \(\binom{p+1}{3}\). This proves the total-count and depth-independence statements.

**3. Lower extreme.** For \(u\ne0\) let \(\pi_u(t)=\langle-ut\rangle_p\) for \(1\le t<p\), a permutation of \(\{1,\ldots,p-1\}\). Replacing \(y\) by \(p-t\) yields
\[
N_p(u)=\sum_{t=1}^{p-1}(t+1-\pi_u(t))_+
=(p-1)+\sum_{t=1}^{p-1}(\pi_u(t)-t-1)_+,
\]
where \((v)_+=\max\{v,0\}\); the second equality follows from \(\sum_t(\pi_u(t)-t)=0\). For \(u=-1\) the permutation is the identity, giving \(p-1\). If \(p\ge5\) and \(u\ne-1\), set \(d=\langle-u\rangle_p\in\{2,\ldots,p-1\}\). If \(d\ge3\), the summand at \(t=1\) is positive; if \(d=2\), the summand at \(t=2\) is positive. Hence every other quotient is strictly more frequent.

**4. Upper extreme.** Put \(m=(p-1)/2\). When \(u\ne-1\), the permutation \(\pi_u\) has no fixed point and \(\pi_u(p-t)=p-\pi_u(t)\). Consequently exactly \(m\) of its displacements are positive and exactly \(m\) are negative. The previous identity becomes
\[
N_p(u)=m+\tfrac12 F(\pi_u),\qquad
F(\pi)=\sum_{t=1}^{2m}|\pi(t)-t|.
\]
For any permutation of \(\{1,\ldots,2m\}\), its footrule \(F\) equals twice the total number of left-to-right crossings over all cuts \(k=1,\ldots,2m-1\). At cut \(k\), at most \(\min(k,2m-k)\) elements cross. Therefore \(F\le2m^2\), with equality if and only if the lower half \(A=\{1,\ldots,m\}\) is mapped exactly onto the upper half \(B=\{m+1,\ldots,2m\}\). This implies \(N_p(u)\le m+m^2=(p^2-1)/4\). If equality holds for \(\pi_u\), multiplying its image by \(-1\pmod p\) shows \(uA=A\). Summing the elements of \(A\) modulo \(p\) gives
\[
(u-1)\frac{m(m+1)}2\equiv0\pmod p,\qquad
\frac{m(m+1)}2\equiv-8^{-1}\not\equiv0\pmod p.
\]
Hence \(u=1\). Conversely \(u=1\) gives the reversal \(\pi_u(t)=p-t\), which exchanges the two halves and attains the bound. For \(p=3\), direct evaluation yields the asserted tie. This proves all claims.

## Verification
The standalone script `checker.py` directly evaluates both actual integer trinomial coefficients for every eligible triple, computes their quotient as a ratio of nonzero residues, and compares the complete frequencies with the formula for primes \(2,3,5,7,11\) at the available depths. The odd-prime theorem is checked at depths up to three for prime five. Further exact arithmetic independently checked the permutation identity and both sharp extrema for 25 odd primes through 101. These checks are finite corroboration; the proof above establishes all prime and depth quantifiers.

For example, the one-digit frequency vectors for the ordered quotients \(1,2,3,4\) at \(p=5\) are \((6,5,5,4)\), with \(Q_5=35\), so at depth two they become \((216,180,180,144)\).

## Relationship to prior work
Lucas's theorem and its multinomial extension give the zero/nonzero digit criterion. Deutsch and Sagan apply the multinomial extension to central-trinomial and Motzkin sequence congruences, rather than to joint adjacent coefficients or their quotient histogram. The Garfield–Wilf binomial residue distribution treats coefficients individually, not their adjacent ternary quotients. A two-coordinate neighboring-binomial quotient law has a distinguished most-frequent quotient \(-1\); the third coordinate produces a weighted simplex count and a strictly opposite extremum for \(p\ge5\). Meštrović surveys Lucas congruences and related applications, but the examined material supplies no evaluated three-coordinate quotient spectrum. The claimed novelty is the complete ternary quotient law and its sharp phase reversal, not the underlying Lucas theorem or the standard permutation-crossing bound.

## Limitations
This is a statement about adjacent transfers between the first two coordinates of a three-part multinomial coefficient, at prime modulus, and only where both coefficients are units. The real-number ratio is not reduced modulo \(p\) before cancellation of its common prime-power factor. The finite-sum formula is exact but can require \(O(p)\) operations to evaluate one quotient. A prior implicit equivalent in unindexed joint-distribution literature remains possible; a targeted literature comparison does not establish universal novelty. Independent mathematical audit has not been performed.

## References
- E. Deutsch and B. E. Sagan, “Congruences for Catalan and Motzkin numbers and related sequences,” *Journal of Number Theory* **117** (2006), 191–215; available online 22 August 2005, DOI: 10.1016/j.jnt.2005.06.005. Author's full text: https://users.math.msu.edu/users/bsagan/papers/old/ccm.pdf.
- R. Meštrović, “Lucas' theorem: its generalizations, extensions and applications (1878–2014),” arXiv:1409.3820, first posted 6 September 2014. https://arxiv.org/abs/1409.3820.
- R. Garfield and H. S. Wilf, “The distribution of the binomial coefficients modulo \(p\),” *Journal of Number Theory* **41** (1992), 1–5, DOI: 10.1016/0022-314X(92)90078-4.
