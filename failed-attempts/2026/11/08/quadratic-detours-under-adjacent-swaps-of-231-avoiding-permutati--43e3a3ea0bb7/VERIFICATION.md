---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Maximum-separation lemma holds for Av(231); first crossings of n force two exchanges of each smaller-value pair, giving (n−1)^2 lower bound, while rightmost descent sorts any avoider to identity, giving matching upper bound. Independent BFS for n=2..7 produced distances 1,4,9,16,25,36; infinite claim rests on all-n proof.

## originality

FAIL

The October 26 Av(132) result is exactly isomorphic by reversal of one-line position order: reverse(132)=231 and adjacency is preserved; previous endpoints e_n=(1,...,n) and r_n=(n,1,...,n−1) become B_n and A_n. It proves the identical (n−1)^2 distance and connectivity.

## value

FAIL

The claimed unbounded detour and canonical pair are the same previously established result, not a new Catalan reconfiguration invariant; a purely reversed pattern label has no added mathematical content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
