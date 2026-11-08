# First Fourier-magnitude ambiguities for six-symbol quadrature phase sequences

## Finding
Let \(\mathcal Q=\{1,i,-1,-i\}\). For each integer \(1\le n\le6\), consider every sequence \(a=(a_0,\ldots,a_{n-1})\in\mathcal Q^n\) on the consecutive integer support \(\{0,\ldots,n-1\}\), and its Fourier polynomial
\[
P_a(z)=\sum_{j=0}^{n-1}a_jz^j.
\]
Two sequences are called trivially equivalent if one is obtained from the other by multiplication by a common fourth root of unity and, optionally, conjugating and reversing the order of the coefficients. For a sequence whose first nonzero index is anchored at zero, this also accounts for the usual translation symmetry of finite-support signals.

**Theorem.** For every \(n\le5\), equality \(|P_a(e^{it})|=|P_b(e^{it})|\) for all real \(t\) implies trivial equivalence. At \(n=6\), exactly four distinct Fourier-intensity functions have more than one trivial equivalence class of QPSK preimages. Each of those four fibers contains exactly two such classes; all other fibers contain one. The four exceptional fibers form a single orbit under the coefficient modulations \(a_j\mapsto i^{tj}a_j\), \(t\in\{0,1,2,3\}\).

One complete exceptional pair is
\[
a=(1,1,-1,-1,1,-1),\qquad b=(1,i,-1,1,-i,-1).
\]
They have the same exact positive-lag autocorrelation vector
\[
(C(1),C(2),C(3),C(4),C(5))=(-1,-2,1,0,-1),
\]
but are not trivially equivalent. Every other exceptional fiber arises by multiplying **both** sequences at position \(j\) by \(i^{tj}\) for one \(t\in\{1,2,3\}\), and then applying trivial symmetries. In particular, a binary phase sequence and a genuinely four-phase sequence can have exactly the same Fourier intensities at six consecutive sites, although no nontrivial QPSK ambiguity occurs at any shorter full-support length.

Equivalently, the statement holds for the complete set of \(2n-1\) equally spaced DFT-intensity samples of the zero-padded length-\(n\) sequence; these samples determine the aperiodic autocorrelation by discrete Fourier inversion.

## Assumptions and scope
All sequence entries lie in the four-element alphabet \(\mathcal Q\) and are nonzero. The support is **all** \(n\) consecutive integer sites, not an arbitrary sparse support inside an interval. Fourier magnitude is continuous over the full circle, or equivalently sampled on any equally spaced grid with at least \(2n-1\) nodes. Reflection means reversal **together with complex conjugation**; plain reversal is not generally an intensity symmetry for complex sequences. No additional symmetry, such as frequency shifting, is quotiented out when counting the four exceptional intensity functions.

For \(1\le k<n\), set
\[
C_a(k)=\sum_{j=0}^{n-1-k}a_{j+k}\overline{a_j}.
\]
The constant autocorrelation is \(C_a(0)=n\), and the negative lags satisfy \(C_a(-k)=\overline{C_a(k)}\).

## Proof
**Reduction to an exact finite classification.** The Laurent expansion
\[
|P_a(e^{it})|^2=\sum_{k=-(n-1)}^{n-1} C_a(k)e^{ikt}
\]
shows that two full-circle intensity functions agree precisely when their complete autocorrelation vectors agree. Since all entries lie in \(\mathcal Q\), multiplication by the inverse of the first entry uniquely normalizes the initial entry to \(1\); every global-phase class has exactly one such normalized representative. There are therefore exactly \(4^{n-1}\) normalized representatives of length \(n\).

Write normalized symbols as powers \(a_j=i^{e_j}\) with \(e_0=0\) and \(e_j\in\{0,1,2,3\}\). The normalized conjugate reverse has exponent tuple
\[
T(e)_j\equiv e_{n-1}-e_{n-1-j}\pmod4.
\]
Thus each trivial equivalence class is represented by the lexicographically smaller of \(e\) and \(T(e)\). Every autocorrelation coefficient is a Gaussian integer, calculated using only integer additions and Gaussian-integer multiplications. This produces an exhaustive, exact, and finite classification with no floating-point comparison.

The fully explicit independent-loop verifier in `CHECK.py` enumerates every \((e_1,\ldots,e_{n-1})\in\{0,1,2,3\}^{n-1}\) for each \(1\le n\le6\). For each tuple it computes all \(C_a(k)\) by the defining finite sum, places the canonical representative in the corresponding autocorrelation bucket, and counts distinct canonical representatives per bucket. It verifies all counts in the following table:

| \(n\) | Normalized sequences | Distinct autocorrelation vectors | Trivial equivalence classes | Ambiguous autocorrelation vectors |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 |
| 2 | 4 | 4 | 4 | 0 |
| 3 | 16 | 10 | 10 | 0 |
| 4 | 64 | 40 | 40 | 0 |
| 5 | 256 | 136 | 136 | 0 |
| 6 | 1024 | 540 | 544 | 4 |

The length-six bucket sizes, counted in trivial equivalence classes, are exactly \(536\) singleton buckets and \(4\) doubleton buckets; there are no larger buckets. In particular, the five shorter lengths have no ambiguity, and the sixth length has exactly four exceptional intensity functions.

**Explicit partner identity.** Set
\[
F(z)=1-z,\quad G(z)=z^2+iz+i,\quad H(z)=z^2-iz-i,
\]
and \(H^{\#}(z)=z^2\overline{H(1/\overline z)}=1+iz+iz^2\). Direct multiplication gives
\[
P_a(z)=F(z)H(z)G(z),\qquad
P_b(z)=F(z)(-iH^{\#}(z))G(z).
\]
The two polynomials have the stated coefficient sequences. On \(|z|=1\), the reciprocal-conjugate operation preserves polynomial magnitude, \(|H^{\#}(z)|=|H(z)|\); the scalar \(-i\) also has unit modulus. Hence \(|P_a(z)|=|P_b(z)|\) throughout the unit circle. They cannot be related by a global phase and conjugate reversal: after normalizing the first entry, the binary sequence's trivial orbit contains only binary sequences, whereas \(b\) has imaginary entries.

**Exhaustion of the four exceptional fibers.** For each \(t\in\{0,1,2,3\}\), modulate both sequences via \(a^{(t)}_j=i^{tj}a_j\), \(b^{(t)}_j=i^{tj}b_j\). Then
\[
C_{a^{(t)}}(k)=i^{tk}C_a(k)=C_{b^{(t)}}(k).
\]
Since \(C_a(1)=-1\), these four autocorrelation vectors are pairwise distinct. `CHECK.py` verifies that their two canonical orbit representatives exhaust exactly the four doubleton buckets, proving the claimed single modulation orbit and fiber sizes.

## Verification
Run `python3 CHECK.py` using Python 3.8 or later; no third-party libraries are required. The program recomputes all Gaussian-integer autocorrelations directly from the sequences, normalizes every global phase, checks reflection-conjugation equivalence, and tests the complete census and exceptional orbit. Independently, it multiplies the three Gaussian-integer polynomials in the explicit factorization and compares all coefficients with the two witness sequences. Its expected terminal message begins `CHECK_OK table=` and includes `ambiguous_spectra=4 orbit_sizes=(2,2,2,2)`.

Each of the \(4^{n-1}\) normalized sequences is visited once. The finite certificate proves the exact length-at-most-six claim because its domain is exhausted; it does not purport to classify longer sequences. No analytic approximation or numerical tolerance is used. An equally spaced grid of size at least \(2n-1\) also determines the full intensity Laurent polynomial by Fourier inversion, so the same classification holds for that oversampled-DFT observation scheme.

## Relationship to prior work
Novikov and Xu (arXiv:2604.25662, first posted 2026-04-28) construct classes of Fourier phase-retrieval ambiguities and Pauli partners by finite differences, including in the discrete setting; their theorems do not count or characterize the first QPSK alphabet-restricted full-support fibers. The present result is a finite-alphabet classification, rather than another general existence construction.

Katz, Rahman and Ward (arXiv:2308.07467, first posted 2023-08-14) prove a broad factorization theorem for equicorrelational sequences over self-conjugate fields and tabulate **binary** ambiguities through length 44; notably, their binary table has no nontrivial length-six fiber. Their general factor-flipping framework explains the identity in this result, but their binary table and factorization criteria do not state the four QPSK fiber counts or establish the sharp QPSK first onset. The factorization and the general phase retrieval symmetry theory are not claimed as new.

The short-length QPSK census differs from published QPSK constructions aimed at small **periodic** autocorrelation and from prior work on scalar fourth-moment optima. The present invariant is the *full aperiodic autocorrelation vector*, which is finer than a scalar energy, and the classification is up to only the universal phase-retrieval trivialities.

## Limitations
This is a small finite-length exact classification for full consecutive support and a fixed four-phase alphabet; it does not extend to arbitrary nonzero complex coefficients, incomplete supports, lengths seven and above, or noisy intensity data. The implementation is a transparent finite exhaustion, not a formula for all lengths. Publication priority beyond inspected papers, their stated results, and searched databases may require additional archival verification. Independent validation has not been performed.

## References
- R. Novikov and T. Xu, *On phase retrieval for continuous and discrete Fourier transforms*, arXiv:2604.25662, first public version 2026-04-28. https://arxiv.org/abs/2604.25662
- D. J. Katz, A. Rahman, M. J. Ward, *Sequences with identical autocorrelation functions*, arXiv:2308.07467, first public version 2023-08-14. https://arxiv.org/abs/2308.07467
- J. R. Fienup et al., classical one-dimensional zero-flipping framework, as referenced and discussed in Katz–Rahman–Ward, Section 1.
