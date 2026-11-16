# Mathematical assessment

## Correctness — PASS

For every dyadic positive order \(n=2^k\) with \(k\ge1\), the rook expansion \(\operatorname{per}(J-2B)=\sum_j(-2)^j(n-j)!m_j(B)\) is exact. Rotation stabilizers of nonattacking rook placements of size \(j\) have order dividing \(j\); since the symmetry group is a two-group, the resulting uniform orbit divisibility supplies \(2^{k-\nu_2(j)}\mid m_j(B)\). Legendre's formula and the bound \(s_2(n-j)\le k-\nu_2(j)\) then force all nonconstant terms to vanish modulo \(2^n\). The constant term has valuation \(n-1\). The Fourier identity and full-group zero witness follow directly. A standalone exact-integer checker corroborates all normalized sign patterns through \(n=8\) and selected order-16 cases. Finite checks are not used as an infinite proof.

## Originality — PASS under bounded comparison

Minc's full 1972 circulant-permanent article treats classical and comparatively sparse circulant forms, not an all-sign dyadic valuation theorem. Tao–Vu's full 2008 preprint proves nonzero permanent with high probability for independent sign entries, not all deterministic circulants. Sburlati's 2008 parity paper concerns zero-one circulants and the parity of their permanents, not the high-power congruence for signed circulants. Sburlati's 2017 congruence article is a **substantive remaining historical-priority risk**: its abstract concerns a related family of congruences, but the full text could not be inspected, so noncoverage is not asserted. No equivalently covering result was identified in the accessible comparisons; this is not a guarantee of global historical novelty.

## Mathematical value — PASS

The invariant is the **exact** \(2\)-adic valuation, uniformly across all signed cyclic matching weights. The cyclic rotation orbit lemma shows a structural obstruction to cancellation and explains why an exponential family of Walsh multipliers remains nonzero. Passing from the unrestricted matching indicator (which has explicit zeros) to its displacement-parity quotient yields a genuine sharp invertibility dichotomy between two natural Fourier operators. The work is not a mere extraction of a computed small case; the proof covers all powers of two. It does not assert sharp endpoint inverse constants or an all-order classification.

## Residual limitations

General circulant congruence literature, particularly the inaccessible 2017 full article, presents an unresolved priority risk. The dyadic restriction is essential to this argument and extension beyond powers of two is unproved. Independent validation was not performed.

Self-review: passed. Independent audit: not yet performed.
