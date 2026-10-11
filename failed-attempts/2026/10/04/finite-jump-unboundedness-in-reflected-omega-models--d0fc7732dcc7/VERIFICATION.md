---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a fixed standard \(k\), membership in \(A^{(k)}\) is arithmetical in \(A\), so the relation saying that the e-th \(A^{(k)}\)-oracle characteristic computation outputs one on input y is a single arithmetical formula with parameter A. If every model set were below \(A^{(k)}\), that formula would uniformly enumerate the entire second-order part. This contradicts the source theorem on non-uniform-enumerability under the relevant reflection scheme. Finite tuples reduce to their join inside every omega-model of \(\mathsf{RCA}_0\). The proof correctly stays pointwise in standard k.

## originality

FAIL

The mathematical content is a direct specialization of Pakhomov's stronger non-uniform-enumeration theorem. Once that theorem is granted for arithmetical formulas with set parameters, choosing the particular formula that enumerates all sets computable from a fixed finite jump yields the claim in one step. Under the audit rule that corollaries are prior-covered even when their degree-theoretic wording is absent, the reformulation is not an original scientific theorem.

## value

PASS

The degree-theoretic translation is useful: it rules out principal and fixed-finite-jump-bounded Turing ideals and makes the reflection scheme's computational richness concrete. The failure is originality, not usefulness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
