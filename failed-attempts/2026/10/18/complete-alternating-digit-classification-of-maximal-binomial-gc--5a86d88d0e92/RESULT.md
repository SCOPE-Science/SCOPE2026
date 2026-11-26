# Complete alternating-digit classification of maximal binomial-GCD rows

## Finding
For every prime \(p\), put \(m=p+1\). For every integer \(N>m\) satisfying \(m\mid N\), let
\[
G_p(N)=\gcd\left\{\binom Nk:0<k<N,\ m\mid k\right\}.
\]
The following **complete equality-locus classification** holds:
\[
\boxed{\nu_p(G_p(N))=2\ \Longleftrightarrow\ N=p^a+p^b\text{ for integers }0\le a<b,\ b-a\text{ odd}.}
\]
In the right-hand condition the standing restriction \(N>p+1\) applies. In every other admissible row \(\nu_p(G_p(N))\le1\). Consequently \(2\) is the maximal valuation, and its least attaining row is \(N=p(p+1)\). In particular every extremal row has precisely two base-\(p\) digits, each equal to one, at positions of opposite parity.

## Assumptions and scope
All integers and prime powers are ordinary positive integers; \(\nu_p(u)\) is the exponent of \(p\) in nonzero integer \(u\). The gcd is over a nonempty set because \(N\ge2m\). The assertion is about the entire family of rows, not only the least row or the maximum valuation. The base-\(p\) representation is \(N=\sum_i n_i p^i\) with \(0\le n_i<p\).

## Proof
Set \(A_p(u)=\sum_i(-1)^i u_i\) and \(s_p(u)=\sum_i u_i\). Since \(p\equiv-1\pmod m\), we have \(A_p(u)\equiv u\pmod m\), while \(|A_p(u)|\le s_p(u)\). Kummer's theorem states that \(\nu_p\binom Nk\) counts carries when adding \(k\) and \(N-k\) in base \(p\), equivalently borrows on subtracting \(k\) from \(N\). Moreover, if there are \(c\) carries, then
\[
s_p(k)+s_p(N-k)=s_p(N)+(p-1)c.
\]

**Necessity, mixed parity.** Suppose the support of the nonzero digits of \(N\) meets both parity classes. Select nonzero positions \(i,j\) of opposite parity and put \(k=p^i+p^j\). Then \(m\mid k\), and its digits are bounded by the digits of \(N\). If \(N\ne k\), this gives \(0<k<N\) with zero carries, hence \(\nu_p(G_p(N))=0\). If \(N=k\), the stated two-unit pattern holds.

**Necessity, one parity.** Suppose every nonzero digit position of \(N\) has the same parity. There must be at least two such positions: a single nonzero digit \(n_i p^i\) with \(1\le n_i<p\) cannot be divisible by \(m\). Choose two nonzero positions \(i<j\); then \(j-i\ge2\). Put \(k=p^i+p^{j-1}\), which is divisible by \(m\). The subtraction of \(k\) from \(N\) borrows exactly once: all residues modulo \(p^h\) up to \(h=j-1\) are at least those of \(k\), the digit at \(j-1\) of \(N\) vanishes while the digit at \(j\) is nonzero, and the unique borrow at the \(j-1\) position is extinguished at the \(j\) position. Thus \(0<k<N\) and \(\nu_p(G_p(N))\le1\).

**Sufficiency, excluding fewer than two carries.** Now \(N=p^a+p^b\) with \(a<b\) of opposite parity, and \(N>m\). No proper multiple of \(m\) in \((0,N)\) is a digitwise subnumber of \(N\): the only nonzero proper digitwise subnumbers are \(p^a\) and \(p^b\), neither divisible by \(m\). Therefore no selected binomial has zero carries. If a selected \(k\) gave exactly one carry, write \(\ell=N-k\). Both \(k\) and \(\ell\) are positive multiples of \(m\), so \(A_p(k)\) and \(A_p(\ell)\) are multiples of \(m\). The digit-sum identity gives \(s_p(k)+s_p(\ell)=p+1\), so both positive digit sums are at most \(p\); hence \(A_p(k)=A_p(\ell)=0\). But one carry from position \(t\) into \(t+1\) changes the sum of alternating digit sums by \((p+1)(-1)^t\) relative to \(A_p(N)=0\). This is nonzero, a contradiction. Thus every selected binomial has valuation at least two.

**Sharp two-carry witnesses.** If \(b-a\ge3\), take \(k=p^a+p^{b-2}\); this is a proper positive multiple of \(m\) and subtraction gives exactly two consecutive borrows at positions \(b-2,b-1\). If \(b=a+1\), the condition \(N>m\) implies \(a\ge1\), and \(k=p^{a-1}+p^a\) is a proper multiple of \(m\) giving exactly two consecutive borrows at positions \(a-1,a\). In both cases \(\nu_p\binom Nk=2\). This proves the equivalence.

The least admissible two-unit opposite-parity number is \(p+p^2=p(p+1)\), since \(1+p\) is excluded. This concludes the proof.

## Verification
Execute `python verify.py` with Python standard library. The program enumerates eight small prime bases, compares valuations of all selected coefficients in \(1372\) eligible rows against the asserted characterization, tests \(174040\) selected coefficients, and independently compares \(3515\) valuation calculations against Legendre's factorial formula. Expected output: `VERIFY_OK prime_fields 8 rows 1372 selected_indices 174040 independent_legendre_checks 3515`. These finite checks are consistency tests, not a substitute for the preceding proof.

## Relationship to prior work
Fairfax-Ball (2026), *Sharp p-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs* (arXiv:2610.01328), proves the universal maximum valuation and establishes least extremal rows for the separate family \(m=p^a+1\) when \(a\ge2\). Its discussion distinguishes the omitted first exponent \(a=1\). The present result does not re-claim the universal upper bound; it characterizes **all** attaining rows at \(m=p+1\), an infinite equality locus. McTague (2015), *On the Greatest Common Divisor of Binomial Coefficients* (arXiv:1510.06696), gives criteria in different congruence regimes; its cited example at \((p,m)=(2,3)\) is compatible with this classification. Wu (2026), *Computing the Greatest Common Divisor of Binomial Coefficients* (arXiv:2606.20940), addresses various additional restriction families; the located statements do not establish this complete two-digit locus. The first prime case overlaps earlier known least-row calculations but does not supply the global equivalence.

## Limitations
This classifies only \(p\)-adic valuations at the specific restriction modulus \(p+1\). Values at non-extremal rows (zero versus one) are not distinguished. It does not assert independent verification or establish priority over every potentially inaccessible general result; implicit coverage by broader carry-based binomial-GCD theory remains a residual literature risk.

## References
- J. Fairfax-Ball, *Sharp p-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs* (2026), arXiv:2610.01328, https://arxiv.org/abs/2610.01328.
- C. McTague, *On the Greatest Common Divisor of Binomial Coefficients* (2015), arXiv:1510.06696, https://arxiv.org/abs/1510.06696.
- C. W. Wu, *Computing the Greatest Common Divisor of Binomial Coefficients* (2026), arXiv:2606.20940, https://arxiv.org/abs/2606.20940.
