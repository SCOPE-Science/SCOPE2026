---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS: Directly reconstructed all 81 one-digit quadruples and the signed-carry matrix [[8,10,2],[3,15,3],[2,10,8]], which keeps carries in {-1,0,1}. Its reflection-even 2x2 block has polynomial x²-25x+90 and central entry E_n. Independently enumerated digit-set additive energies 15,285,5775,118725 at depths 1..4. The continuous tail has support [0,2] and each grid-cell probability is q0 w_k+q1 w_{k-1}; nonnegative cross terms and Young yield (1/2) E_n/81^n <= sum cell masses² <= E_n/81^n for every n. This proves the exact all-scale dimension; Cauchy–Schwarz makes L² impossible because 4 lambda+/81>1. Strict separation of the basic IFS cylinders justifies dimension log3/log4 for each factor; no singularity or smaller-p density claimed.

## originality

PASS

Best-of-knowledge original evaluated digit-set invariant and near-threshold L² counterexample; generic finite-type and Lq convolution theory does not state its evaluated base-4 {0,1,3} self-convolution dimension or 25±sqrt265 growth constants. Possible old tables of overlap-IFS energies remain a real priority risk.

## value

PASS

PASS: Each factor has Hausdorff dimension log_4(3)>1/2, yet the natural self-convolution has an exactly specified near-one L² dimension 0.9862600784<1 and lacks an L² density. This exact arithmetic example clarifies a motivated convolution regularity boundary and provides a complete finite-level energy recurrence, rather than an arbitrary small numerical experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
