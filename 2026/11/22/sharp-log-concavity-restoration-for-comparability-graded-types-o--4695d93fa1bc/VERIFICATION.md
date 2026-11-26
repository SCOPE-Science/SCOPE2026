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

Pointwise naming and homogeneity make each admissible atomic relation pattern one complete type: the lower set is an ideal, the upper set a filter, and every lower element precedes every upper element. If both sets are nonempty they lie on the same chain, with j−1 prefix/suffix splits at grade j per chain. The one-sided patterns give 2U_a^k−1. For a,k≥2, the untruncated binomial expansion with the correction proves the interior inequalities, except that grade 1 uses c0=1 and c1²−c2=k(3k−2). At grade a the actual next coefficient is smaller than the fully untruncated corrected one. At grades ≥a+2 the three relevant coefficients are all uncorrected and log-concavity follows from convolution. Inclusion–exclusion (no two coordinates can exceed a at degrees a+1,a+2) gives the sole candidate defect at a+1. For k=2,3,4 the three displayed polynomials give the exact sign transitions and Δ(4,4)=−336. For k≥5 the base quartic is positive after a=2+y, and the induction certificate is nonnegative termwise except possibly at (2,5), where it equals 576. The a=1 binomial case and k=1 coefficients 1,…,a+1 cover the boundaries, including singleton supports with no internal grade. Independently expanded the decisive identities symbolically and checked 209 exact inclusion–exclusion profiles, including localization of every negative defect. Replay: python3 /workspace/branches/frozen_math_reproductions.py 1 (SymPy). These checks verify algebra and sampled profiles, not the infinite theorem, which follows from the sign and induction arguments. The frozen verification code was inspected, not run.

## originality

PASS

Pass only the contribution the record itself identifies in RESULT.md line 91: the full equal-chain coefficient-shape classification, including uniform restoration at five and the four-by-three exception. The counting polynomial is an exact specialization of a distinct same-date catalog result, and the two-chain slice is covered by that result as well. Its statement does not give the all-k threshold. No priority order is inferred from the shared date.

## value

PASS

The exact length-uniform cutoff is meaningful for a natural graded logical-type enumerator: ordinary convolution would predict no obstruction, yet two through four copies can fail for arbitrarily long chains. Identifying the sole boundary grade and the isolated surviving (3,4) case is a useful complete classification, not a finite table or a novelty claim about the polynomial itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
