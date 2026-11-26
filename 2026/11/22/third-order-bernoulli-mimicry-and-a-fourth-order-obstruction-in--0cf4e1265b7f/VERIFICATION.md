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

Conditioning on the input, the spin response is u X_i times the indicator of unequal neighbors plus v X_{i-1} times the indicator of equal neighbors. Global spin flip kills odd moments. Pairing the equal Walsh monomials gives uv/2 at separation one and v²/4 at separation two for n≥5 and on Z; other pairs vanish. On the four-ring the distance-two term has two common singletons, hence v²/2. On the three-ring a pair has common cubic and common singletons, giving (u+v)²/4; on one and two sites the neighbors necessarily coincide, and in the two-site case each response uses only the other input. At v=0 and n≥4 all proper nonempty moments of a four-block vanish, as do all moments on any selection of at most three sites. Independently of the written Walsh counting argument, the four-block product is nonzero only when all four pairs (i−1,i+1) are unequal. The inner constraints force X_0 X_2=X_1 X_3=−1, so the block product is +u⁴ on that event. The constraint graph has rank four for n≥5 and on Z (two disjoint paths, glued at one endpoint on n=5), and rank two on n=4 where two pairs are repeated. This gives the stated quartic coefficients and the complete law by Walsh inversion. The pair and four-block obstructions prove necessity for fair stationarity; all sufficiency and small rings follow from the moment calculations. Independently enumerated exact coefficient maps in u and v from local cases for 210 subsets through order four on rings n=1..7 (replay: /workspace/branches/independent-replays/audit_pca_coefficients.py); this tests all parameter coefficients for the sampled sizes, not the arbitrary-size quantifier. Frozen checker read, not executed. The three-wise claim excludes the three-ring away from the fair point, as specified in the record.

## originality

PASS

Credit the known update and small-ring computations. The supported distinct claim is the all-size and infinite-lattice one-step vanishing of all spin correlations through order three on the nontrivial line together with the exact fourth-order obstruction and resulting size-uniform classification. Neither the same-model antecedents nor the closest broader comparisons checked establish it.

## value

PASS

On a naturally defined one-parameter slice of an existing noisy majority model, every marginal test involving at most three sites misses a departure from fair-product stationarity. The explicit parity law supplies the first witness, at any size where the phenomenon occurs, and a complete stationarity obstruction rather than a single small-ring computation. It makes no claim about arbitrary initial measures or asymptotic mixing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
