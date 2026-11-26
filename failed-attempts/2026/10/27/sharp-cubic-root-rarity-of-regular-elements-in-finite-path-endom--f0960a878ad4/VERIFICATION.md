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

A regular path endomorphism has a section on its image, necessarily an injective nearest-neighbor walk, hence a contiguous monotone full-image run; inverses of such runs extend by alternating at each endpoint. For a fixed width h, marking the run bounds the free prefix and suffix by the path spectral radius 2 cos(π/(h+2)); fixing a leading run and applying the positive sine eigenvector supplies the uniform lower bound. The all-walk count is between a constant times 2^(n−1) and n·2^(n−1) for large n, e.g. by maximal inequality for a walk started in the central half. Thus log of the ratio differs by O(log n) from the negative minimum of h log 2−(n−1−h) log cos(π/(h+2)). Widths on smaller and larger scales than (n−1)^(1/3) cannot minimize, by −log cos x≥x²/2 and the linear run cost, respectively. Compact rescaling gives u log 2+π²/(2u²), minimized at u=(π²/log 2)^(1/3), with the stated constant and negative sign. Independent finite replay checked inverse-witness equivalence through n=7 and spectral bounds through n=10; the uploaded checker was inspected, not executed. The retrieved version of the criterion labels it Proposition 1.7 rather than the frozen citation's 1.9; the criterion itself matches.

## originality

FAIL

The exact exponent and constant are a direct corollary of the distinct indexed retraction-rank result plus the standard regularity criterion. For image width h, the total number of regular maps with a marked full run is exactly 2(n−h) times the count of idempotents of rank h+1: transport the whole output by the isomorphism from the image interval to the marked source interval, producing an idempotent there; the original image interval and orientation recover the marked map. Between 1 and n−h marks per regular map give 2 I_{n,h+1}≤R_{n,h+1}≤2(n−h)I_{n,h+1}; in particular log R_n=log I_n+O(log n). The published retraction asymptotic for I_n therefore gives the entire finding, not just one inequality. The distinct record's later indexed date establishes no earlier priority; the failure is coverage by mathematical implication in the inspected corpus.

## value

FAIL

The rarity rate is a natural invariant, but at exactly this logarithmic resolution the known retraction law already determines it by marking and relabeling a full run. The frozen result has no independent unmarked counting formula, prefactor, or fluctuation law that survives the coverage comparison. The alternate spectral proof alone does not supply a distinct scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
