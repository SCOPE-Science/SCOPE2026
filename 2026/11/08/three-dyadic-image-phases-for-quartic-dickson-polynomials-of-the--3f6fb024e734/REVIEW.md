# Review of the quartic Dickson value-image theorem

## Correctness — PASS

All quantifiers are explicit: odd \(a\), any \(2\)-adic argument, all image counts for \(k\ge1\), and fibers for \(k\ge5\). A factorization of \(h_a(y)-h_a(z)\) gives two regular branches. A canonical square root defines a third-branch isometry. The three images, their overlaps, measures and representation multiplicities follow exactly. The verifier reproduces every target fiber across \(261632\) modular target cases without assuming the claimed answer as input to its brute-force enumeration. Finite computations are supporting checks, not substitutes for the proof.

## Originality — PASS (historically qualified)

Qu–Ding (2014), especially their accessible Theorem 3.2 and concluding section, determine permutation cases but do not classify values of the nonpermuting quartic. Fan–Liao (2015) address dynamics of first-kind Chebyshev polynomials, not these second-kind parameter-dependent fibers. Distinct first-kind dyadic image classifications concern different maps, and a permutation criterion cannot imply three numerical image measures and all multiplicities. Searches for equivalent quartic image formulas returned no controlling source. A more general unpublished or differently phrased \(p\)-adic polynomial-value theorem could still cover the case; no blanket novelty certification is asserted.

## Mathematical value — PASS

The lowest genuinely quartic, nonpermuting second-kind Dickson family is a natural next case after permutation criteria. The complete all-unit-parameter phase diagram has three different positive image densities (depending on \(a\bmod8\)) and exact target-fiber data at every stated modulus. This reveals arithmetic information concealed by a yes/no permutation classification. It is a self-contained classification, not an arbitrary numerical slice.

## Evidence and limitations

Direct primary-material comparisons used Qu–Ding, DOI `10.1137/130942589`, and Fan–Liao, arXiv:`1511.03529`. The full proof is in `RESULT.md`; the independent finite-level checker is `verify_e4.py`. The result covers degree four and unit parameters only. Historical priority remains qualified; independent review has not occurred.

Self-review: passed. Independent audit: not yet performed.
