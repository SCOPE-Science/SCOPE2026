---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In the wrap segment j<k the inner-product numerator has factor gamma_N^N=2i relative to j≥k, after pulling out gamma_N^(−k). With u=e^(2a/N)e^(2πiℓ/N) and u^N=4, the resulting geometric numerator is (1−2i)u^k+2i−4, and the squared norm before normalization is 3/(e^(2a/N)−1). This gives the exact absolute-value formula. Choosing h=k−N/2 equal to 1/2 for odd N or 1 for even N and rounding the corresponding resonant frequency to the nearest index of the required parity proves an O(N^(−2)) upper bound for all sufficiently large N. Conversely that bound and the exact formula force the radial mismatch to be O(1/N) at minima, hence h is bounded. Take a subsequence with fixed h, fixed frequency parity and ℓ/N→s. Necessarily (−1)^ℓ exp(2πihs)=exp(iϑ); neither endpoint s is possible since 2h is integer and exp(iϑ)≠±1. Radial mismatch alone gives scaled lower bound B·4a|h|/|1−exp(2πis)|, B=2a√(5/2)/3. For odd N, |h|≥3/2 is strictly worse even with denominator 2; |h|=1/2 forces the two stated mirror resonances with denominator 2sinϑ=6/5. For even N, h=0 cannot resonate and |h|≥2 is strictly worse; |h|=1 gives maximum denominator 2cos(ϑ/2)=6/√10 with odd ℓ. These give the stated distinct constants. Irrationality follows because rational ϑ/π would make 2cosϑ=8/5 an algebraic integer. Irrational rotation on odd N and on N divisible by 4 makes ℓ−Ns=o(1) with the respective parity, so the phase mismatch is o(1/N) and the radial lower bounds are attained as subsequential limits. Thus these are true liminfs, not claims of parity-wide convergence. Independent `python3 /workspace/reproduce_reviews.py` compared exact-index phases with direct normalized cyclic sums in dimensions 2–12 and obtained near-resonant scaled margins about 0.8440699078 at N=36625 and 1.0676733731 at N=30376. These finite observations do not prove the asymptotic, which follows from the radial lower bound and the exact density argument for irrational rotations.

## originality

PASS

The contribution is the two sharp dimension-asymptotic constants and their particular arithmetic attainability for the dimension-dependent principal root of 2i. Credit the existing seed, N^(−2) order, finite ambiguity identity, and fixed-dimension phase resonance. Those comparisons motivate the calculation but do not themselves optimize the discrete phase with N and parity changing. Priority is conditional on available statements, especially given limited direct access to the preprint and two related records.

## value

PASS

The ambiguity margin is a natural conditioning statistic of an existing explicit cyclic Gabor design. The exact subsequential lower envelopes give a sharp benchmark missed by two-sided order bounds and show that rescaling by N² does not give one asymptotic constant. The arithmetic obstruction and attainability mechanism are part of the exact result; it does not optimize other windows or classify all accumulation points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
