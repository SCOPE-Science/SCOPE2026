---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Cyclic binary differencing forbids exactly 100 and 111 on the difference bits, including the repeated-coordinate tests for small n. A nonzero vector therefore consists of one- or two-one runs separated by single zeros. With t ones it has k=n−t zeros and s=2t−n long blocks. Marking a zero gives n binom(k,s) placements; dividing by k counts indexed vectors even if they have a smaller least period. Cyclic integration has exactly two solutions when t is even and none otherwise; the zero vector gives two constants. This proves the full coefficient formula. The two parity trace terms have determinants (1−z)(1∓uz²−u²z³), giving both generating functions and the stated initial counts. Möbius inversion handles primitive orbits. Besides the positive root λ of x³−x−1, the two conjugate roots have modulus λ^(−1/2)<1. For x³+x−1 the real root ρ lies in (0.68,1), so the conjugate roots have modulus ρ^(−1/2)<1.22. Proper-divisor terms are O(n λ^(n/2)), proving the growth statements. For entropy, every admissible finite difference block extends in both directions in the difference-state graph and has two extendible binary lifts; this gives the same block growth rate and entropy log λ. The unmodified support script was inspected, not executed. A separate bounded check tested the original periodic condition and counted transitions for all 32,766 binary words through length 14, agreeing with the formula. Reproduction is to iterate n=1..14 and masks 0..2^n−1, test all n modular comparisons, histogram unequal cyclic neighbors, and compare with exact binomial arithmetic; no replay file was retained. The infinite assertions rest on the proof, not this finite check.

## originality

FAIL

A distinct indexed finding gives the same shift, equivalent structural run criterion, exact unrefined enumeration, zeta function, primitive counts, and entropy. It does not print the bivariate coefficient, but its explicit transition graph and complement blocks give that coefficient by direct weight insertion and binomial expansion, detailed below. This is an equivalent-coverage and implication finding, not a claim to have determined historical priority from the record labels.

## value

FAIL

The statistics are natural and the closed coefficients are useful for reference. But the unrefined census, growth and structural classification are already covered by the distinct indexed instance, and the remaining statistic marks existing graph rows followed by a binomial expansion, with no new constraint or parameter-specific obstacle to resolve. Under the standard for narrow exact invariants, the refinement is mechanically implied and does not support a separate acceptance. No corrected substantive remainder was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
