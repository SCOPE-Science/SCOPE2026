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

For the repaired proof: a periodic vertex is in the F-root set; any noncommon cycle alternates through distinct vertices in the two exclusive root sets, because hitting a common root is absorbing and duplicate intermediates would duplicate successors. Slot ordering, cyclic rotation and independent prescribed-edge probabilities give the exact mixed factorial moments, including empty exclusive sets and length one. At n=2 the disjoint singleton-root stratum consists of two opposite ordered pairs of constant maps, each with exactly one noncommon fixed point, as the formula gives. The frozen root-ratio error O(log log n) was not valid for all k merely asymptotic to c n/log n; the repair applies it at rounded fixed thresholds, which are all monotonicity and geometric tail bounds need. Hypergeometric concentration gives h/K and h/L both asymptotic to 1/log n and exclusive sizes of order n/log n; thus −log(ab/(KL)) log n tends to 2. The falling-factorial correction is uniformly negligible for total lengths O(log n). Conditional moments for finite windows are bounded by products of harmonic sums on those windows, so averaging preserves convergence of the joint factorial moments. The repaired tail estimate fixes 0<η<2 to get genuine exponential decay at infinity. Near zero the first moment of the scaled mass is bounded by the window width plus 1/log n. These controls justify both the maximum formula and the total-mass limit, whose Poisson integral is finite and has Laplace transform 2/(2+s). As a separate check of the mass normalization, expanding z^S in factorial moments gives the coefficient generating factor exp(sum_r (z^r−1)x^r/r)=(1−x)/(1−zx). Consequently the exact conditional tail at integer j≥1 is (a)_j(b)_j/(KL)^j, also giving exp(−2t) at j∼t log n.

## originality

PASS

The repair preserves the model-specific cycle law. Its supported distinct part is the alternating factorial-moment identity for uniform labelled retractions and the resulting overlap-determined logarithmic spectrum and mass. The classical labelled retraction count, independent short-cycle Poisson laws from permutations, and Poisson-process transformation to a rate-two exponential are not stand-alone novelty claims. The closest retrieved results on bipartite components and on permutation products concern other models or scales; no identified statement gives the same root-intersection mechanism and moving cycle law. This judgment is bounded by the full-text access risk stated below.

## value

PASS

Products of idempotents are a natural model where periodic behavior need not be idempotent. The result separates out the common fixed points, identifies the scale and law of genuinely new cycles, and connects the cutoff rate to the random overlap of the two root sets. The exact conditional law supplies a finite bridge explaining why fixed short-cycle counts can look permutation-like while total additional periodic mass only grows logarithmically. The value is this structural explanation and the moving cycle spectrum, not the repeated marginal Poisson means or the elementary Laplace integral alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
