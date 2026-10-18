# Binary-weight trichotomy for the ternary-step binomial GCD

## Finding

For every integer \(n\ge2\), define the restricted Pascal-row greatest common divisor
\[
G_3(n)=\gcd\left\{\binom{3n}{3k}:1\le k<n\right\}.
\]
Write \(s_2(u)\) for the number of ones in the binary expansion of a positive integer \(u\). Then
\[
\boxed{\nu_2(G_3(n))=
\begin{cases}
2,&s_2(3n)=2,\\
1,&s_2(3n)=3,\\
0,&s_2(3n)\ge4.
\end{cases}}
\]
The missing case \(s_2(3n)=1\) is impossible because \(3\mid3n\). Thus this is an exact formula for every admissible row, not just a large-row approximation.

## Assumptions and scope

The selected indices are precisely the **positive proper multiples of three** in row \(3n\), and \(n\ge2\). The valuation \(\nu_2\) is the exponent of the prime \(2\). The result determines only the two-adic component of the GCD; it does not claim a formula for the other prime factors. The case \(n=1\) is excluded because its selected set is empty.

## Proof

Set \(N=3n\). For \(1\le k<n\), put \(t=3k\). By Legendre's digit-sum identity, equivalently Kummer's binary carry theorem,
\[
\nu_2\binom Nt=s_2(t)+s_2(N-t)-s_2(N).
\]
The valuation of a GCD is the minimum of the valuations of its entries. We therefore minimize this integer over \(0<t<N\) with \(3\mid t\). Because \(3\mid N\), both \(t\) and \(N-t\) are positive multiples of three.

**Binary subset criterion.** A binomial valuation is zero precisely when \(t\) is represented by a nonempty proper subset of the one-bit positions of \(N\). Since \(2^j\equiv(-1)^j\pmod3\), a subset of positions represents a multiple of three exactly when its number of even positions minus its number of odd positions is divisible by three.

Let \(E\) and \(O\) be the respective counts of even and odd one-bit positions of \(N\). Then \(E-O\equiv0\pmod3\). If both counts are positive and \(s_2(N)>2\), choose one bit of each parity: their sum is divisible by three and is a proper binary subset of \(N\). If one count vanishes, the total weight is a positive multiple of three; when the weight exceeds three, any three one-bits form a proper subset whose sum is divisible by three. Hence \(s_2(N)\ge4\) always admits a zero-valuation selected coefficient. Conversely, if \(s_2(N)=2\), the two bits must have opposite parities and neither singleton is divisible by three. If \(s_2(N)=3\), all three bits must have the same parity, and no nonempty proper subset is divisible by three. Thus positive valuation is forced precisely at binary weights two and three.

**Weight three.** Write
\[
N=2^i+2^j+2^\ell,\qquad i<j<\ell.
\]
The exponents have the same parity, hence \(j-i\ge2\). Set
\[
t=2^i+2^{j-1},\qquad N-t=2^{j-1}+2^\ell.
\]
Each displayed summand has exactly two one-bits in positions of opposite parity, so both are divisible by three and are positive. Their combined binary weight is four. The digit-sum identity gives valuation \(4-3=1\), which is minimal because valuation zero has already been excluded.

**Weight two.** Write
\[
N=2^i+2^j,\qquad i<j.
\]
The exponents have opposite parity, so their difference is odd. Every positive multiple of three has binary weight at least two. Consequently any admissible decomposition \(N=t+(N-t)\) has combined binary weight at least four and therefore valuation at least \(4-2=2\). To attain this lower bound, consider two cases. If \(j=i+1\), then \(i\ge1\), since \(N>3\); choose
\[
t=N-t=3\cdot2^{i-1}.
\]
Both halves are positive multiples of three with binary weight two. If \(j-i\ge3\), set
\[
t=2^i+2^{j-2},\qquad N-t=3\cdot2^{j-2}.
\]
The two exponents in \(t\) have opposite parity, so \(3\mid t\). The other term is visibly divisible by three. Both terms have binary weight two, giving valuation exactly \(2\).

The cases exhaust every \(N=3n\) with \(n\ge2\), which proves the formula.

## Verification

The accompanying `artifacts/verify.py` is a standard-library-only, integer-arithmetic transcription check. It independently computes \(G_3(n)\) from exact big-integer binomial coefficients for every \(2\le n\le200\), independently minimizes the binary digit-sum identity over every \(1\le k<n\) for \(2\le n\le1000\), and constructs the explicit proof witnesses for each of those \(999\) inputs. Its outcome is stored in `artifacts/replay.txt`. The finite tests are **not** used as an infinite proof; the symbolic parity and digit-sum argument above supplies that proof.

For illustration, \(n=2\) has binary \(3n=6\) of weight two and valuation two; \(n=7\) has \(3n=21\) of weight three and valuation one; \(n=5\) has \(3n=15\) of weight four and valuation zero.

## Relationship to prior work

McTague (arXiv:1510.06696v5) proves a selected-binomial GCD theorem when the valuation prime is congruent to one modulo the index step, and specifically notes that the unrestricted congruence hypothesis fails for the \(p=2\), step-three instance: \(\nu_2\binom63=2\). That isolated example is covered, not new. Wu (arXiv:2606.20940v2) determines the prime-local valuation when the step itself is a power of the valuation prime and gives full GCD formulas under additional congruence restrictions; neither determines the two-adic valuation for every step-three row. Fairfax-Ball (arXiv:2610.01328v1, Theorem 4.3) establishes the sharp universal bound \(\nu_2(G_3(n))\le2\) and attainment, and explicitly identifies the known \(G_3(2)\) example, but does not classify which rows attain zero, one, or two. The present result gives precisely that row-by-row classification, including the first-prime-exception case excluded by the congruence-based formulas.

## Limitations

No formula for the complete integer \(G_3(n)\) or for its odd prime divisors is asserted. The claim concerns exactly the two-adic valuation and all \(n\ge2\); it does not extend without proof to other index steps or other primes. The closest accessible primary papers were inspected in full, but a negative literature search is not a guarantee that no unindexed equivalent statement exists.

## References

1. Chai Wah Wu, *Computing the Greatest Common Divisor of Binomial Coefficients* \(\binom{mn}{mk}\), arXiv:2606.20940v1 (2026-06-18), inspected v2 (2026-08-04), §§1–3. https://arxiv.org/html/2606.20940v2
2. Carl McTague, *On the Greatest Common Divisor of Binomial Coefficients*, arXiv:1510.06696v5, Theorem Q and the non-congruence remark. https://arxiv.org/html/1510.06696v5
3. John Fairfax-Ball, *Sharp p-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs*, arXiv:2610.01328v1, Theorem 4.3, Remark 8.4, and §9. https://arxiv.org/html/2610.01328v1
4. Ernst Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, J. Reine Angew. Math. 44 (1852), 93–146.
