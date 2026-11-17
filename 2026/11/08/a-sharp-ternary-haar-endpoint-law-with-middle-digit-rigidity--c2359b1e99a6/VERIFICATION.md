---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Reconstructed normalized orthonormal ternary contrasts and exact signed kernel rows. Scalar dynamic program F_m(z) splits a row at a ternary node and carries inherited z; symmetry, convexity and 1-Lipschitz comparison reduce four local actions to B for |z|<1/2 and D for |z|>1/2, with boundary tie. Induction yields the claimed piecewise affine formula and U_d=d+5/6−1/(2·3^d). For m>=2 the strict Lipschitz bound forces intermediate visited digits 1 or 2, while first and last are unrestricted; hence 9*2^(d-2) norming words. Independently brute-forced all ancestral sign assignments for every kernel row through depth 4, reproducing norms 5/3,25/9,103/27,391/81 and norming counts 3,9,18,36. All-depth conclusion rests on Bellman induction, not low-depth enumeration.

## originality

PASS

Despite closely related published higher-arity martingale endpoint formulas, the strongest checked prior permits one predictable sign per complete difference and therefore does not contain the independent-per-contrast ternary sign class; numerical formulas and row classifications differ. Classical m-adic unconditionality estimates are finite-p/weak-type rather than this exact finite L∞ constant.

## value

PASS

The result quantifies frame-sensitive real L∞ signed unconditional growth and completely classifies extremizing rows for a nonbinary two-contrast filtration. The middle-digit rigidity is structurally nontrivial and not implied by the earlier predictable single-sign martingale transform.

The dated certificate retains the supplied scientific assessment, sources and limitations.
