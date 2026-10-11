---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The cited smooth-curve formulas and adjunction give deg Tan=D(S-N+1) and deg Sec=D(D-S+N-2)/2. Their comparison is equivalent to product(y_i+1)<=3 sum y_i+1. The coordinate increment of the difference is product over the other factors minus three, yielding the stated exclusion for four or more defining equations and the three remaining triples in codimension three. Fresh exact enumeration of 75,504 bounded tuples reproduced exactly those cases and the degree pairs, while the proof is uniform and does not rely on the enumeration.

## originality

FAIL

The classification is mathematically correct, but it is a direct complete-intersection specialization of published general tangent- and secant-degree formulas plus the standard adjunction identity. After substitution, the entire exceptional list is obtained from the elementary product-versus-sum inequality D<=3S-3N+4. Under the audit rule that corollaries and specializations of stronger published results are covered even without identical wording, originality fails.

## value

FAIL

The ordering question is natural, but the answer is a short arithmetic specialization of already published exact degree formulas and standard adjunction. The remaining product-sum inequality is routine and does not supply an independent structural ingredient beyond those formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
