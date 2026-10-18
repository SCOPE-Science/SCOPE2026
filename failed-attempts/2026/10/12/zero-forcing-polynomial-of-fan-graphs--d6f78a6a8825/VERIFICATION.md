---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The proof's hub-selected iff reduces to path zero forcing (endpoint or adjacent selected path pair). With the hub white, no path-to-path force is possible before hub capture, and only an endpoint selected adjacent pair or three consecutive selected path vertices can force the hub. This yields a complete iff forcing criterion. Counting the failed hub-free binary words avoiding initial/final 11 and internal 111 via the four-state transfer matrix gives (1+x)^(m+1)−xQ_m−A_m. For every m>=3, the four minimum sets are two hub/endpoints and two boundary path pairs. Independent brute-force dynamics for each subset at m=3..9 matches the criterion and cardinality counts; those finite tests do not establish the general theorem.

## originality

FAIL

Prior published exact fan theorem fully covers identical mathematical content; no distinct original claim survives.

## value

FAIL

FAIL as a distinct new contribution: the exact entire forcing-set classification, all-coefficient polynomial, and four minimum sets were already publicly reported with proofs for the same fan family in the 2026-10-04 Resultary record. Replacing its equivalent forbidden-word enumerator by a four-state automaton is a routine repackaging; no additional motivated invariant or stronger family remains in the final claim. The mathematical object is valuable, but its value is already supplied by the earlier source.

The dated certificate retains the supplied scientific assessment, sources and limitations.
