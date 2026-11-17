---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For irrational alpha>1, the one-step inverse y=floor(x/alpha)+1 exists exactly if u={x/alpha}>1-1/alpha. The second inversion reduces to {v+(1-u)/alpha}>1-1/alpha with v={x/alpha²}. Since the unreduced argument lies in (0,2), its split at 1 gives exactly the stated C_alpha and disjoint E_alpha: 1-1/alpha<u<2-alpha and v>2-2/alpha+u/alpha. The triangular branch exists only if alpha<phi; its Lebesgue area is (1-alpha+1/alpha)^2/(2alpha), equal to natural density under rational independence by Kronecker–Weyl. For alpha=sqrt(2) restricted fractional orbit makes E empty. Direct finite independent decimal membership tests support but do not establish the infinite density.

## originality

PASS

Best-of-knowledge original under actual inspected statements; significant access or historical-priority risks are explicitly retained.

## value

PASS

The first nontrivial iterated Beatty range predicate has a sharp golden-ratio parameter cutoff, explicit omitted region and an exact generic natural density, answering a natural lower-parameter question without claiming higher iterates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
