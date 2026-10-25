# Exact primitive periods for prime-power Diophantine solvability words

## Finding
For coprime integers \(a,c\ge2\), let \(\Gamma(a,c)=0\) if
\[
ax+cy=\frac{(a-1)(c-1)}2
\]
has a solution in nonnegative integers \(x,y\), and let \(\Gamma(a,c)=1\) if instead
\[
1+ax+cy=\frac{(a-1)(c-1)}2
\]
has such a solution. Exactly one alternative holds for these parameters.

**Theorem.** Let \(p\) be an odd prime, \(e\ge2\), \(m=p^e\), and let \(b\ge2\) be any integer that is a primitive root modulo \(m\). Set \(N=\varphi(m)=p^{e-1}(p-1)\), and \(G_i=\Gamma(m,b^i)\) for each integer \(i\ge1\). The least positive period of the infinite binary word \((G_i)_{i\ge1}\) is **exactly \(N\)**. In fact,
\[
G_{i+N/2}=1-G_i\qquad(i\ge1).
\]
In every full period there are exactly \(N/2\) zeros and \(N/2\) ones. Thus a primitive generator of the full unit group yields a balanced word of maximal possible period, rather than merely a word of period dividing the generator's order.

## Assumptions and scope
The inverse \(u^{-1}\bmod m\) always means the unique least positive representative in \(\{1,\ldots,m-1\}\); all coprimality statements concern integers. Primitive root means multiplicative order \(\varphi(m)\) modulo \(m\). The theorem applies to every odd prime and every exponent \(e\ge2\), with no condition on the parity of \(b\). Periods refer to **the output word**, not merely to the modular state sequence. The case \(e=1\) also satisfies the argument, but is not asserted as a new result: full-period parity words modulo primes already occur in the older literature on binary \(d\)-sequences. Likewise the primitive-base-\(2\) prime-power cases are covered by known binary reciprocal periods, and are included in the theorem only as part of a uniform all-generator classification.

## Proof
**Step 1: connect the Diophantine predicate to inverse parity.** Fix an odd \(m\ge3\) and \(c\ge2\) coprime to \(m\). Put \(u=(c^{-1}\bmod m)\), and write \(cu-1=mv\), so \(0\le v\le c-1\). If \(u\) is odd, then \(v\equiv c-1\pmod2\), and the nonnegative integers
\[
x=\frac{c-1-v}{2},\qquad y=\frac{u-1}{2}
\]
satisfy \(mx+cy=(m-1)(c-1)/2\). If \(u\) is even, then \(v\) is odd and the nonnegative integers
\[
x=\frac{v-1}{2},\qquad y=\frac{m-u-1}{2}
\]
satisfy \(1+mx+cy=(m-1)(c-1)/2\). To check exclusivity, note that for either right-hand side, the congruence modulo \(m\) specifies a unique \(y\in\{0,\ldots,m-1\}\); replacing \(y\) by a larger nonnegative congruent representative strictly decreases \(x\). In the opposite equation the least such \(y\) already gives negative \(x\): if \(u\) is even, the first equation has \(x=-(v+1)/2\); if \(u\) is odd, the second has \(x=(v-c-1)/2<0\). Hence
\[
\Gamma(m,c)=1\quad\Longleftrightarrow\quad(c^{-1}\bmod m)\text{ is even}.
\]
This independently reconstructs the inverse-parity characterization used in the source literature.

**Step 2: the even-unit moment.** With \(m=p^e\), let
\[
E=\{u:1\le u<m,\ u\equiv0\pmod2,\ p\nmid u\},\qquad S=\sum_{u\in E}u.
\]
Writing \(h=(m-1)/2\) and \(k=(p^{e-1}-1)/2\), sum all even integers below \(m\) and subtract the even multiples of \(p\):
\[
S=h(h+1)-p k(k+1)=\frac{(p-1)(p^{2e-1}+1)}4.
\]
Consequently \(4S\equiv p-1\pmod{p^e}\), so \(S\) is invertible modulo \(m\). This is the decisive obstruction to nontrivial multiplicative stabilization of the output partition.

**Step 3: rule out every shorter output period.** Since \(b\) is a primitive root, the states \(b^{-i}\bmod m\) for \(1\le i\le N\) run through the entire unit group. Step 1 says \(G_i=1\) precisely when \(b^{-i}\bmod m\in E\). Suppose \(t\ge1\) is any period of the output. Multiplication by \(h=b^{-t}\bmod m\) then carries \(E\) bijectively onto itself. Summing its elements modulo \(m\) gives \(hS\equiv S\pmod m\). Because \(S\) is a unit, \(h\equiv1\pmod m\). The order of \(b\) therefore divides \(t\), so \(N\mid t\). Conversely the modular state sequence, and hence \(G\), has period \(N\). The least output period is \(N\).

**Step 4: complement and balance.** The unit group modulo an odd prime power is cyclic, with unique element of order two equal to \(-1\). Therefore \(b^{N/2}\equiv-1\pmod m\). Multiplication by \(-1\) replaces a least positive representative \(u\) by \(m-u\), reversing its parity because \(m\) is odd. Thus \(G_{i+N/2}=1-G_i\). This pairs each zero with a one in every period, proving the exact balance.

## Verification
The standalone Python 3 program `verify.py` implements independent modular inversion, exact integer checks of the even-unit moment, detection of a least output period by checking all divisor periods, the complement identity, and direct bounded searches for solutions to the two Diophantine equations. It uses only the Python standard library. Run `python3 verify.py` from the directory containing this document. The exact output supplied is `verification_output.json`. It checks 33 prime-power moduli (including prime levels as boundary controls), 272 primitive-root parameter choices, 75,882 binary positions, 355 direct Diophantine predicates, and a nonprimitive counterexample. These finite tests corroborate, but do not establish, the universal theorem; the proof above supplies the infinite argument.

## Relationship to prior work
Chu, Kim, Koch, Miller, and Nguyen, *Generalizing a Pair of Diophantine Equations*, arXiv:2609.08728v1 (first public September 8, 2026), Theorem 1.2 gives the inverse-parity characterization and Theorem 4.1 establishes **only** that the output period divides the multiplicative order. The present theorem is a sharp determination for every primitive root of every odd prime-power modulus with exponent at least two. Kak's \(d\)-sequence work (1981, 1985; see also his short *A New Random Number Generator*) already discusses prime-modulus full periods and complementary half periods, so the prime-modulus assertion is not treated here as new. OEIS A167791 additionally covers maximal binary-reciprocal periods for prime-power moduli where \(2\) is primitive, and the parity word for inverse powers of base \(2\) is a reversal (up to cyclic reindexing) of the reciprocal digit word, with bits possibly complemented by the solvability convention. The new scope is **every primitive base**, including prime-power moduli where \(2\) is not primitive; for example, modulo \(49\), base \(2\) has order \(21\), but base \(3\) has order \(42\) and the output has least period \(42\). The even-unit moment gives the uniform argument without assuming the base is \(2\). Searches for prime-power analogues under both Diophantine-\(\Gamma\) and \(d\)-sequence/least-significant-bit terminology did not locate a theorem subsuming the asserted lift; absence from searches is not proof of novelty.

## Limitations
Primitive-root status is essential to the stated scope; for example, the base \(3\) modulo \(121\) has order \(5\), whereas its output is the constant zero word of least period \(1\). The theorem does not classify periods of nonprimitive bases or moduli with more than one distinct odd prime factor. Classical \(d\)-sequence and reciprocal-expansion literature already covers the base-\(2\) subfamily for prime powers; a more general result for all primitive bases might be implicit elsewhere not found in the inspected sources; independent literature review remains necessary. No claim of independent audit or external certification is made.

## References
1. H. V. Chu, D. Kim, T. Koch, S. J. Miller, A. V. Nguyen, *Generalizing a Pair of Diophantine Equations*, arXiv:2609.08728v1 (2026), especially Theorems 1.2 and 4.1, https://arxiv.org/abs/2609.08728.
2. S. Kak and A. Chatterjee, *On Decimal Sequences*, IEEE Transactions on Information Theory 27 (1981), 647–652.
3. S. Kak, *Encryption and Error-Correction Coding Using D Sequences*, IEEE Transactions on Computers C-34 (1985), 803–809, DOI:10.1109/TC.1985.1676636.
4. S. Kak, *A New Random Number Generator*, short note (dated February 5, 2006), https://www.ece.lsu.edu/kak/RNG.pdf (prime-modulus maximum periods and half-period complements).
5. OEIS Foundation, *A167791: Numbers with primitive root 2*, https://oeis.org/A167791 (periods of binary reciprocals, including odd prime powers).
6. S. Thippireddy and S. Chalasani, *Period of the d-Sequence Based Random Number Generator* (2008), abstract at https://www.researchgate.net/publication/1901599_Period_of_the_d-Sequence_Based_Random_Number_Generator (full text not obtained; remaining comparison risk).
