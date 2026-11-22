# Exact dyadic squared-distance law for odd harmonic sums

## Finding
For each integer \(n\ge 0\), define the rational odd-denominator harmonic sum
\[
O_n=\sum_{j=1}^{n}\frac1{2j-1},\qquad O_0=0.
\]
**Theorem.** For all integers \(0\le a<b\),
\[
\boxed{\nu_2(O_b-O_a)=\nu_2(b^2-a^2).}
\]
Here \(\nu_2\) denotes the exponent of \(2\) in a nonzero rational number. Equivalently, for every integer \(r\ge1\) and all \(a,b\ge0\),
\[
O_a\equiv O_b\pmod{2^r}\quad\Longleftrightarrow\quad
 a^2\equiv b^2\pmod{2^r}.
\]
The congruence is in \(\mathbb Z_2\); every \(O_n\) belongs to \(\mathbb Z_2\). With \(n=b-a\ge1\), this also determines the valuation of every shifted odd-reciprocal interval:
\[
\boxed{\nu_2\!\left(\sum_{j=0}^{n-1}\frac1{2a+2j+1}\right)=\nu_2\bigl(n(2a+n)\bigr).}
\]

## Assumptions and scope
All indices are nonnegative integers, all interval lengths are positive integers, and no analytic continuation of harmonic sums is assumed. The conclusion is an exact identity for all indices; it is not a finite-range observation. The previously known fixed-start case \(a=0\) is not claimed as new.

## Proof
Write \(n=b-a\) and \(c=a+b=2a+n\). If \(n\) is odd, the difference \(O_b-O_a\) is a sum of an odd number of odd rational \(2\)-adic units, so it is odd in \(\mathbb Z_2\). The integers \(n\) and \(c\) are both odd; hence both valuations are zero.

Now let \(n=2m\), where \(m\ge1\). The midpoint \(c=2(a+m)\) is even. Pair the first and last, second and penultimate, and so on. Writing \(d_i=2i-1\) for \(1\le i\le m\), the paired denominators are precisely \(c-d_i\) and \(c+d_i\). Therefore
\[
O_b-O_a=\sum_{i=1}^{m}\left(\frac1{c-d_i}+\frac1{c+d_i}\right)
=2cT,\qquad T=\sum_{i=1}^{m}\frac1{c^2-d_i^2}.
\]
Put \(s=\nu_2(m)\). For every integer \(k\ge1\), define \(W_k=\sum_{i=1}^{m}d_i^{-2k}\in\mathbb Z_2\). The \(d_i\) run through exactly \(m/2^s\) complete sets of odd residues modulo \(2^{s+1}\). Inversion permutes those residue classes. Thus
\[
 W_k\equiv\frac{m}{2^s}\sum_{\substack{x\bmod 2^{s+1}\\x\text{ odd}}}x^{2k}\pmod{2^{s+1}}.
\]
The inner sum is congruent to \(2^s\) modulo \(2^{s+1}\), for **every** positive integer \(k\). For \(s=0\) this is immediate. Inductively, when \(s\ge1\), pair \(x\) with \(x+2^s\) over odd residues modulo \(2^{s+1}\). The binomial theorem gives \((x+2^s)^{2k}\equiv x^{2k}\pmod{2^{s+1}}\): its linear binomial term contains \(2k\cdot2^s\), and all higher terms are multiples of \(2^{2s}\), which is divisible by \(2^{s+1}\) for \(s\ge1\). Therefore the new sum is twice the previous-level sum modulo \(2^{s+1}\). By induction
\[
W_k\equiv m\pmod{2^{s+1}},\quad\text{so in particular}\quad\nu_2(W_k)=s.
\]
Since \(c\) is even, each geometric series \((c^2-d_i^2)^{-1}=-\sum_{j\ge0}c^{2j}d_i^{-2j-2}\) converges in \(\mathbb Z_2\). Summing over finitely many \(i\) yields
\[
T=-\sum_{j\ge0}c^{2j}W_{j+1}=-W_1-\sum_{j\ge1}c^{2j}W_{j+1}.
\]
Each term in the tail has valuation at least \(2j+s\ge s+2\), and \(W_1\equiv m\pmod{2^{s+1}}\). Consequently
\[
T\equiv-m\pmod{2^{s+1}},\qquad \nu_2(T)=s.
\]
It follows exactly that
\[
\nu_2(O_b-O_a)=1+\nu_2(c)+s
=\nu_2(2m c)=\nu_2\bigl((b-a)(b+a)\bigr)
=\nu_2(b^2-a^2).
\]
This proves the theorem. If \(a=b\), both differences vanish, so the stated congruence equivalence holds trivially as well.

## Verification
`check.py` uses exact rational arithmetic to compare all index pairs up to a stated cutoff; it also checks the modular equivalence at successive moduli. Run `python3 check.py` from the same directory. The infinite theorem follows from the preceding proof, not from this finite verification.

## Relationship to prior work
A July 15, 2016 Mathematics Stack Exchange question records the single-index identity \(\nu_2(O_n)=2\nu_2(n)\). The July 16–20, 2016 MathOverflow discussion includes Will Sawin's proof using aligned dyadic blocks and Dongryul Kim's proof using power sums. These are acknowledged as prior results. Their stated conclusions concern \(a=0\), or power-of-two intervals aligned with the block length. The theorem here compares **every pair** \(a,b\), including intervals of arbitrary length and arbitrary starting point. Its symmetric-midpoint factor \(b+a\), complete square-residue collision condition, and general exact valuation do not follow just from the one-point valuations; the two known valuations can be equal without determining their difference. The proof uses a related elementary technique but produces a new two-variable law. Prior sources are linked below.

## Limitations
No claim of priority against every unindexed or implicit earlier derivation is made. The result concerns odd-denominator sums in \(\mathbb Q_2\), not ordinary harmonic numbers with all denominators, nor valuations at odd primes. Scientific verification is same-model only; independent audit has not been performed.

## References
1. *2-adic valuation of odd harmonic sums*, Mathematics Stack Exchange, question and discussion begun July 15, 2016. https://math.stackexchange.com/questions/1860105/2-adic-valuation-of-odd-harmonic-sums
2. *2-adic valuation of odd harmonic sums*, MathOverflow, question July 16, 2016; responses by Will Sawin and Dongryul Kim dated July 17, 2016. https://mathoverflow.net/questions/244430/2-adic-valuation-of-odd-harmonic-sums/244501
