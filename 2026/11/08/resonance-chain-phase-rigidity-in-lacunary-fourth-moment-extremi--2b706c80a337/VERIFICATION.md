---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Parseval on P² counts ordered pair sums; distinct unordered sums give 2S²−Σ|c_j|⁴. For q>=3, base-q digits never carry in two-term sums, so this is the whole expression and equality is precisely equal magnitudes with arbitrary phases. In binary the sole carry collisions within the set are 0+2^j=2^(j−1)+2^(j−1), each contributing 4 Re(c0 c_(j+1) conj(c_j)^2). Replacing coefficients by magnitudes maximizes these real parts simultaneously. If c0 is present, compressing the positive support in order preserves every existing resonant adjacency, adds only nonnegative ones, and preserves the baseline. The singleton c0 case has value 1 directly (the source's compression expression would otherwise use undefined K_(2,0)). If c0 is absent, all positive power sums are distinct as unordered sums, so the ratio is strictly below 2. At m=2, put s=a0²+a2², p=a0a2, S=1; the terms involving p are 2p²+4p(1−s), increasing with p. Its maximum p=s/2 gives 1+4s−(7/2)s², attaining 15/7 at s=4/7. The m=1 maximizer has full support; appending ε to any full-support nonnegative maximizer gains a strictly positive linear resonance while normalization costs only O(ε²). Strict growth excludes any proper support containing c0 by compression and the inductive inequalities, and 15/7>2 excludes supports without c0 from m=2 onward. Equality in every resonant term forces 2 arg(c_j)=arg(c0)+arg(c_(j+1)) mod 2π; subtracting arg(c0) iterates doubling, giving exactly global phase and circle rotation for each maximizing magnitude profile. No uniqueness of those profiles is claimed. The independently written test verified 36 Fourier-difference moment identities and recovers 15/7 from the correlations of (sqrt(2),sqrt(3),sqrt(2)). Replay: python3 /workspace/review-evidence/replay.py 5. This is separate from the frozen recorded 1297 finite checks.

## originality

PASS

The exact linked-midpoint four-character phase and support result covers m=3 and is expressly credited to the prior record. The higher-base formula is the routine collision-free Parseval result and is not the novelty basis. The supported distinct content is the all-length dyadic theorem: full support and character phase fibers at arbitrary length, together with strict growth across lengths. The needed compression and strict extension argument is not a consequence of the isolated four-character equality classification, or of the real three-harmonic result at the same indexed date.

## value

PASS

The theorem explains a qualitative sharp-equality transition between dyadic carrying and carry-free sums: at every dyadic length no maximizing spectrum can omit any available character, and phases are forced into a character orbit. The strict gain across lengths and exact structural equality are information that a generic fourth-moment bound or any one fixed small spectrum does not give.

The dated certificate retains the supplied scientific assessment, sources and limitations.
