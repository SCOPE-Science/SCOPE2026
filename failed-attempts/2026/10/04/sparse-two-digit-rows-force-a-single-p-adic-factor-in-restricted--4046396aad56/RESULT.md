# Sparse two-digit rows force a single \(p\)-adic factor in restricted binomial GCDs
## Finding
Let \(m\ge 3\), let \(p>m\) be prime, and let \(0\le s<t\) satisfy \(m\mid p^s+p^t\). Put
\[
N=p^s+p^t,
\qquad
G(N;m)=\gcd\left\{\binom Nk:0<k<N,\ m\mid k\right\}.
\]
Then
\[
v_p(G(N;m))=1.
\]

A concrete new residue-class consequence is obtained at modulus \(5\). If \(p\equiv2\) or \(3\pmod5\), then \(p\) has order \(4\) modulo \(5\), and
\[
5\mid p^s+p^t
\quad\Longleftrightarrow\quad
t-s\equiv2\pmod4.
\]
Hence every such sparse row has \(v_p(G(p^s+p^t;5))=1\).

## Assumptions and scope
The statement concerns the fixed-row arithmetic-progression gcd \(G(N;m)\). The assumptions are \(m\ge3\), \(p\) prime, \(p>m\), \(0\le s<t\), and \(m\mid p^s+p^t\). Since \(p>m\), one has \(\gcd(p,m)=1\); since \(t\ge1\), also \(m<N\).

The result is not a complete formula for arbitrary base-\(p\) rows. It isolates a natural two-nonzero-digit family in which the no-borrow obstruction and a one-borrow witness can both be determined exactly.

## Proof
Kummer's theorem identifies \(v_p\binom Nk\) with the number of borrows when subtracting \(k\) from \(N\) in base \(p\). Consequently
\[
v_p(G(N;m))=\min_{\substack{0<k<N\\m\mid k}} v_p\binom Nk.
\]

The base-\(p\) expansion of \(N=p^s+p^t\) has a digit \(1\) in positions \(s\) and \(t\), and zero elsewhere. A subtraction has no borrow exactly when the digits of \(k\) form a subdigit selection from these two occupied positions. Thus the only no-borrow lower indices are
\[
0,\quad p^s,\quad p^t,\quad N.
\]
The two proper nonzero choices \(p^s\) and \(p^t\) are not divisible by \(m\), because \(\gcd(p,m)=1\). The remaining two choices are excluded by \(0<k<N\). Therefore every admissible lower index has at least one borrow, and
\[
v_p(G(N;m))\ge1.
\]

For the opposite inequality take the explicit admissible index
\[
k=m p^{t-1}.
\]
Because \(m<p\), one has \(0<k<p^t<N\), and clearly \(m\mid k\). In base \(p\), subtracting \(m p^{t-1}\) from \(N\) forces a borrow from the occupied digit at position \(t\) into position \(t-1\). If \(s=t-1\), the digit there is initially \(1\); otherwise it is \(0\). In either case \(m<p\) makes the single borrowed unit sufficient, so the borrow chain stops immediately. Hence the subtraction has exactly one borrow. Kummer's theorem gives
\[
v_p\binom{N}{m p^{t-1}}=1,
\]
and therefore \(v_p(G(N;m))\le1\). Combining the two inequalities proves the theorem.

For the modulus-\(5\) corollary, primes \(p\equiv2,3\pmod5\) have multiplicative order \(4\), with \(p^2\equiv-1\pmod5\). Thus \(p^s+p^t\equiv0\pmod5\) exactly when \(p^{t-s}\equiv-1\pmod5\), equivalently \(t-s\equiv2\pmod4\).

## Verification
The standalone script `verify_sparse_two_digit.py` performs two layers of exact checks. First, over a deterministic grid of moduli, primes, and exponent pairs satisfying the hypotheses, it verifies the explicit witness and its exact one-borrow count. Second, for all test cases with manageable \(N\), it exhaustively minimizes the borrow count over every admissible lower index; for the smallest cases it also constructs the actual binomial coefficients, takes their integer gcd, and checks its \(p\)-adic valuation. A successful run prints `VERIFY_OK` with the numbers of structural, exhaustive, and direct-gcd cases.

These finite checks are corroborative. The infinite statement is established by the proof above.

## Relationship to prior work
McTague's Theorem Q treats primes \(p\equiv1\pmod m\), and the corrected remark in arXiv:1510.06696v5 allows a same-residue weakening when the occupied powers of \(p\) are congruent modulo \(m\). For the present two-digit rows with \(m\ge3\), the condition \(m\mid p^s+p^t\) makes the two occupied residues negatives of one another; they cannot be equal because they are units modulo \(m\) and \(m\nmid2\). Thus McTague's same-residue extension does not yield this family.

Fairfax-Ball, arXiv:2609.37754v1, gives a complete formula for \(p\equiv-1\pmod m\) and restates the known \(p\equiv1\pmod m\) branch. The theorem above overlaps those residue classes where applicable, but it is not restricted to \(p\equiv\pm1\pmod m\). Its modulus-\(5\) specialization produces exact infinite families for \(p\equiv2,3\pmod5\), the two invertible classes outside the \(\pm1\) cases.

Wu, arXiv:2606.20940v2, studies the same restricted gcd under different product-formula hypotheses. The recent Fairfax-Ball comparison records that Wu's principal product theorem forces the relevant non-modulus primes into the \(1\pmod m\) class, so it does not imply the non-\(\pm1\) modulus-\(5\) specialization above.

## Limitations
The theorem only treats rows with exactly two nonzero base-\(p\) digits, both equal to \(1\). It does not classify arbitrary residue classes for general rows, nor does it determine the full integer value of \(G(N;m)\). The originality check searched exact formulas, aliases, Kummer/borrow formulations, the recent restricted-gcd papers, and the current result database; no equivalent statement was located, but unindexed or differently phrased prior work remains a bibliographic risk.

## References
1. John Fairfax-Ball, *Restricted Binomial GCDs at Primes Congruent to -1*, arXiv:2609.37754v1, 2026.
2. Carl McTague, *On the Greatest Common Divisor of Binomial Coefficients \(\binom n q,\binom n{2q},\binom n{3q},\ldots\)*, Amer. Math. Monthly 124 (2017), 353--356; corrected preprint arXiv:1510.06696v5.
3. Chai Wah Wu, *Computing the Greatest Common Divisor of Binomial Coefficients \(\binom{mn}{mk}\)*, arXiv:2606.20940v2, 2026.
4. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, J. Reine Angew. Math. 44 (1852), 93--146.
