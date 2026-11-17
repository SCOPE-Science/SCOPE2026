---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Run counts follow exactly from G00=binom(A,2)-A+r0 and G11=binom(B,2)-B+r1; opposite pair orientations satisfy G01+G10=AB-(t-1). At four runs, 0^a1^b0^c1^d gives G10=bc-1 and reverse orientation gives G01=bc-1; factor-pair bijection counts all candidates and no different-run words match. At A=B=K+1, p=K has tau(K) factor pairs and reflected product K(K+1)>K^2, yielding exact tau(K). Independent literal deck enumeration checked 16,382 small words through length 13, not an unbounded proof.

## originality

FAIL

FAIL: October 26 published result already establishes the same complete four-run fibre formula and reflected multiplication-table code size, with exactly the same ≤3-run uniqueness exception and unbounded ambiguity. Reparametrization q=G01 and identity G01+G10=AB-3 make both two-summand formulae literally identical. The exact tau(K) family is an immediate specialization of its factor-count formula, not an independent new theorem.

## value

FAIL

FAIL: Although exact fibre enumeration is mathematically useful in its original publication, this repeated claim supplies no previously unknown structural classification or motivated independent invariant beyond that published result; choosing the exact tau(K) family is a direct numerical substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
