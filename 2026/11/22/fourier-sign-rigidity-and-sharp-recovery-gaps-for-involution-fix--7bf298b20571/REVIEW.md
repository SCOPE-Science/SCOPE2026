# Review: Fourier sign rigidity of involution fixed-point profiles

## Correctness — PASS
The counting kernel is explicitly the distribution of exact fixed-point masks for all involutions. Signed inclusion–exclusion gives the binomial formula, and the two-type exponential formula agrees with Wick pairing for one standard Gaussian. The adjacent-frequency identity and complement symmetry follow algebraically. Gaussian integration by parts proves the positive central-moment recurrence from initial values \(1,0\); induction proves the strict even/odd sign laws and the exact central spectral minimum for every \(n\ge4\). Direct independent involution enumeration and an integer Hadamard transform agree on 4094 characters through size 11; separate exact coefficient checks extend through size 60. The low-order exceptions are checked explicitly. No finite experiment substitutes for the all-order proof.

## Originality — PASS, with bounded literature priority risk
Lugo's 2009 full text (Sections 1, 4, 6) and Chow–Mansour's 2010 Section 4/Proposition 7 establish classical involution/partial-matching enumeration and scalar fixed-point refinements, not positionwise all-character Walsh signs or the sharp spectral gap. A related exact Walsh theorem for fixed positions of unrestricted permutations has analogous adjacency methods but uses \((n-j)!\), not involution counts, and does not imply the odd-order indefinite signs here. An involution permutation-matrix edge-coordinate spectrum and complete-graph matching edge-coordinate results likewise concern different Fourier domains. The central moment sequence itself is already OEIS A053871, and no novelty is claimed for that table or recurrence. Dedicated searches for aliases, multivariate and signed enumerators, sharper coverage, and exact tables yielded no established implication; unindexed work remains a priority risk, not proof of uniqueness.

## Value — PASS
Fixed-point positions are the canonical local statistic of an involution; preserving multiplicities rather than replacing the kernel by support makes the recovery question intrinsically linked to the classical telephone-number law. The theorem settles *all dimensions*: exactly two singular orders, a sharp parity sign phase, and the least nonzero multiplier as a known central moment with a previously unestablished Fourier role. It therefore supplies exact stability constants for recovering arbitrary signals from XOR convolution by these fixed-point profiles, not merely a restated scalar enumeration or an isolated finite case.

## Limits and close comparisons
Only the \(\ell^2\) operator condition number is sharp here. No claim is made about independent checking, broad wreath-product extensions, or endpoint inverse norms. External searches cannot rule out unindexed equivalent signed-profile identities. The known centered chi-square moment sequence is explicitly credited.

Self-review: passed. Independent audit: not yet performed.
