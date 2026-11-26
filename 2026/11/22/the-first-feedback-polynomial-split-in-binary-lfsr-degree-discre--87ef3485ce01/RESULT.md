# The first feedback-polynomial split in binary LFSR degree discrepancy

## Finding

Let \(k\ge 2\) and let \(p(X)\in\mathbb F_2[X]\) be a monic primitive polynomial of degree \(k\), with constant coefficient one. Represent successive powers of \(X\) modulo \(p(X)\) by nonzero integers \(s_t\in\{1,\ldots,2^k-1\}\), starting at \(s_0=1\). Put \(M=2^k-1\) and \(d_t=\lfloor\log_2 s_t\rfloor\), with indices modulo \(M\). For every integer \(1\le r\le M\), let
\[
c_j(t,r)=\#\{0\le h<r:d_{t+h}=j\},\qquad
D_p(t,r)=\frac12\sum_{j=0}^{k-1}\left|c_j(t,r)-\frac{r2^j}{M}\right|,
\]
\[
\Delta_p(r)=\max_{0\le t<M}D_p(t,r)-\min_{0\le t<M}D_p(t,r),\qquad
H_k(p)=\max_{1\le r\le M}\Delta_p(r).
\]

**Theorem (first feedback sensitivity and exact degree-five spectrum).** For degrees \(2\le k\le4\), the peak \(H_k(p)\) is independent of the primitive polynomial and equals \(1/3,6/7,8/5\), respectively. Degree \(k=5\) is the first degree with different peaks. Its complete, exact feedback-polynomial table is:

| Primitive polynomial as hexadecimal coefficient bit mask | \(H_5(p)\) | Smallest maximizing \(r\le15\) |
|---|---:|---:|
| `0x25` | \(70/31\) | 15 |
| `0x29` | \(68/31\) | 14 |
| `0x2f` | \(80/31\) | 9 |
| `0x37` | \(86/31\) | 15 |
| `0x3b` | \(86/31\) | 15 |
| `0x3d` | \(80/31\) | 9 |

Thus the exact degree-five peak spectrum, counting distinct primitive polynomials, is \(68/31:1,70/31:1,80/31:2,86/31:2\). In particular, the reciprocal primitive pair `0x25` and `0x29` has **different** peaks when each cycle is measured in its own natural power basis. Reciprocity replaces a generator by its inverse and changes the basis used to measure degree. Inverting the generator alone with the basis held fixed preserves the peak.

## Assumptions and scope

A bit mask `0x25` encodes \(X^5+X^2+1\), and `0x29` encodes \(X^5+X^3+1\). All maxima include **every** cyclic start \(0\le t<M\) and **every** length \(1\le r\le M\), not only sampled lengths. Each primitive polynomial is considered separately, in its natural power basis. There is no coordinate-basis invariance assertion. The source's highest-set-bit convention is used, and the ideal frequency of degree \(j\) is \(2^j/M\).

## Proof

**1. Primitive list is exhaustive.** A monic binary polynomial of degree \(k\) and nonzero constant coefficient has a unique integer mask \(p\) among the \(2^{k-1}\) odd masks with highest bit \(2^k\). Multiplication by \(X\) modulo \(p\) acts on positive state masks by \(s\mapsto 2s\), followed by XOR with \(p\) if bit \(k\) is set. Since the constant coefficient of \(p\) is one, this map permutes the nonzero residue classes. Such a polynomial is primitive **if and only if** the orbit of state one has length \(M\). Thus checking every eligible mask's orbit length is a complete test for primitivity, and the resulting degree list visits the \(M\) nonzero states once each.

**2. Exact score and complement reduction.** Define the integer score
\[
G_p(t,r)=\sum_{j=0}^{k-1}\left|M c_j(t,r)-r2^j\right|=2M D_p(t,r).
\]
The sum of the window and complementary-window degree histograms is \((1,2,4,\ldots,2^{k-1})\), so \(G_p(t,r)=G_p(t+r,M-r)\). Consequently
\[
H_k(p)=\frac1{2M}\max_{1\le r\le\lfloor M/2\rfloor}
\left(\max_{0\le t<M}G_p(t,r)-\min_{0\le t<M}G_p(t,r)\right).
\]
This is a maximum over a finite, explicitly complete set of integer computations.

**3. Exact exhaustive certificate.** The accompanying `verify_peak.py` enumerates all \(2^{k-1}\) possible masks for each \(k=2,3,4,5\), retains **only** full-length orbits, and computes the score range for every admissible window length and start. It also implements a second sliding-histogram evaluation and asserts agreement with direct independent recounts at all \(111\) primitive-polynomial/horizon pairs. The checked primitive-mask sets are \(\{\texttt{0x7}\}\), \(\{\texttt{0xb},\texttt{0xd}\}\), \(\{\texttt{0x13},\texttt{0x19}\}\), and \(\{\texttt{0x25},\texttt{0x29},\texttt{0x2f},\texttt{0x37},\texttt{0x3b},\texttt{0x3d}\}\). Their maximum score ranges are respectively \(2,12,48\) for degrees two through four, and \(140,136,160,172,172,160\) for the six degree-five masks. Division by \(2M\) yields all fractions in the theorem.

For concrete boundary witnesses at \(k=5\), at the extremal length \(r=15\) for `0x25`, the smallest and largest integer scores are \(30\) (at starting state index \(t=6\)) and \(170\) (at \(t=29\)), giving \((170-30)/62=70/31\). For its reciprocal `0x29`, \(r=14\) gives scores \(42\) (\(t=2\)) and \(178\) (\(t=8\)), giving \((178-42)/62=68/31\). The exhaustive loops exclude any larger score range at other lengths. Bit reversal of six coefficient bits sends `0x25` to `0x29`, confirming reciprocity.

**4. Fixed-basis inversion.** For a primitive generator \(\alpha\) and a fixed basis, write \(d^+_t\) for the degree label of \(\alpha^t\) and \(d^-_t\) for that of \(\alpha^{-t}\) in the same basis. Then \(d^-_t=d^+_{-t}\). A window of length \(r\) starting at \(t\) in the inverse cycle has the same histogram as the forward window starting at \(-t-r+1\) modulo \(M\). This start transformation is a bijection, so every score range and hence the peak are unchanged. By contrast, representing \(\alpha^{-1}\) as the residue of \(X\) modulo the reciprocal polynomial measures its powers in the basis \(1,\alpha^{-1},\ldots,\alpha^{-(k-1)}\), rather than \(1,\alpha,\ldots,\alpha^{k-1}\).

## Verification

Run `python3 verify_peak.py` using Python's standard library. The final line is `LFSR_EXHAUSTIVE_DEGREE_FIVE_OK: 111 primitive-polynomial/horizon pairs; direct + sliding independently agree`. Exact rational fractions (`fractions.Fraction`), integer histograms and complete loops are used; no random sampling or floating-point comparisons occur. The script explicitly asserts the entire theorem table and checks complementary windows at both boundary lengths for every primitive polynomial. The argument in Proof 2 establishes the complement identity for **all** lengths.

## Relationship to prior work

Joonas Pääkkönen, *An Empirical Square-Root Law for the Degree Discrepancy of Binary m-Sequences*, arXiv:2611.15635v1 (first public November 11, 2026), Sections 3–5, studies the same exact degree-discrepancy statistic but chooses one primitive polynomial for each degree and reports a sampled-grid maximum for degrees at least five. The exhaustive all-polynomial spectrum and the reciprocal-pair distinction above are not contained in its reported table. Its earlier cited study on finite-horizon invariance loss addresses fixed-horizon minimal discrepancy; a complete full text was not located during this comparison. Ordinary de Bruijn discrepancy and autocorrelation spectra concern other observables. This theorem makes **no** claim of priority over any as-yet-unindexed source.

## Limitations

This is an exhaustive finite theorem through degree five, **not** a bound uniform over large \(k\), a proof of a square-root asymptotic, or an assertion that the feedback variation persists in a prescribed manner at every higher degree. The statistic depends on the chosen polynomial-basis coordinate representation. The finite enumerations prove exactly the finite classification asserted here because every candidate, primitive orbit, starting phase, and relevant horizon is exhausted.

## References

- J. Pääkkönen, *An Empirical Square-Root Law for the Degree Discrepancy of Binary m-Sequences*, arXiv:2611.15635v1 (2026), https://arxiv.org/abs/2611.15635 .
- J. Pääkkönen, *Finite-horizon invariance loss in cyclic discrete designs over binary finite fields*, submitted to *Discrete Applied Mathematics* (2026), cited as reference [17] in arXiv:2611.15635v1; public full text not located.
- `verify_peak.py`, accompanying exact finite certificate.
