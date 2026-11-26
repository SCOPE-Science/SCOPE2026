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

The triangle-free extension property realizes exactly independent positive neighborhoods among the individually named vertices; the join test concerns the union of positives, not the original negatives. Each Boolean interval of faces has alternating sum zero except at equal endpoints, so incidence inversion gives M=Z diag(w) Z^T with integer-unitriangular Z and w(F)=I(C_n minus N[F],-1). For nonempty F, complementary runs have lengths max(d_i-3,0) for cyclic gaps d_i, including d_1=n for a singleton. The path values 1,0,-1,-1,0,1 repeat, giving weights 0 or ±1 and excluding exactly gaps 1 mod 3. The empty-face cycle weight is 2cos(n pi/3) by the two-state transfer trace, so this is the sole source of a possible 2, precisely when 3 divides n. Rooted gap sequences with A(z)=(z^2+z^3)/(1-z^3) count each k-point set k times; n[z^n]log((1-z^3)/(1-z^2-2z^3)) plus one yields the stated integer rank recurrence. Integer congruence gives the complete Smith form and the single rank loss in characteristic two when 3 divides n. Directly constructed small matrices had rank/order 3/7, 11/11, 12/18, 15/29 through C7, with precisely the single factor 2 at C6 (`/workspace/branches/8da3627e-03a2-4c76-96cf-c27a7f91cb1e/independent_check.py`). The all-n conclusion uses the proof, not small cases or the frozen script's recorded results.

## originality

PASS

The distinct claim is the exact integral Smith form, including the full rank formula for the positive-union compatibility matrix of a cycle. The model-theoretic type criterion, incidence inversion, and link Euler characteristics have antecedents; they are not treated as independently new. The strongest related indexed statements have different matrices.

## value

PASS

Cycles are natural finite induced bases, and the integer Smith form isolates a characteristic-two obstruction invisible in the rational rank. The result gives the complete integral invariant at every cycle length, not a rephrasing of the background type criterion, empty-link Euler sum, or sample determinants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
