---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Reconstructed Gaussian projection from J=∫(1-u)dB_u, Var(J)=1/3 and c(v)=v-v²/2. The transformed reading B_s+Z and increment B_t−B_s are independent with variances s+η and t−s. If a variance is zero the corresponding constant datum contributes zero; this covers coincident times and (s,η)=(0,0). For fixed s<1 the increment gain d(1-s-d/2)² has its unique maximum at d=2(1-s)/3; s=t=1 gives gain at most 1/4<8/27. The reduced derivative has the product factors in RESULT.md; for η>0 each quadratic has one positive root below one, and at the first factor’s root r the second is 3r(r−2)<0. The signs −,+,− leave only s=0 and the second root s_+(η) as winners. For η=0 cancel the common factors and the only winner is s=2/5. For s>0 the gain relative to calibration has the sign of H(s)−η, where H=s(12−12s−5s²)/(32(s²−3s+3)). The differentiated envelope has exactly one maximum at (15−√105)/10 and its value is (7√105−69)/64=0.04263524002683107316…; the unique interior tie there must be the local maximum already identified. Risk is 1/75 noiseless, 1/27 at and above the threshold, and otherwise obtained by subtracting the winning gain from 1/3. The low-noise branch is continuous up to its positive tied first time; the high-noise branch starts at zero. Read all frozen supporting material, including the symbolic/matrix verifier and dependency list; the script was inspected, not executed. The foregoing projection, factorization and root ordering are the replay, not the sampled design checks. This conclusion is for two deterministic samples and perfectly common Gaussian error, not independent readings, drift, many samples or adaptivity.

## originality

PASS

The closest older two-measure Brownian primary text was accessible in this review and turns out to have both a different objective and independent sensor noise. The closest indexed shared-noise calibration record instead uses a Brownian bridge. Neither supplies the exact positive-noise common-offset transition for unpinned Brownian integral estimation. The noiseless calculation and Gaussian projection are not originality claims.

## value

PASS

A common zero-offset is a natural nuisance parameter. The result tells when to spend one of exactly two measurements entirely on calibration and gives the full risk and exact coexistence point, rather than just demonstrating that an offset can cancel. The jump and risk plateau are useful benchmark behavior for this rank-one error model; robustness to even small independent noise is not asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
