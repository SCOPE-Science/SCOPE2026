---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 verify.py` using standard Python 3. It constructs all \(n\)-world alternating-partition models for \(1\le n\le100\) and checks the S5 properties (reflexivity, symmetry, transitivity) of each of the two initial relations. It then evaluates the fixed formula from the current relation at every stage, checks that exactly the rightmost active target disappears per round, and confirms first stabilization at exactly stage \(n\). The terminal model has no arrows and is fixed.

The checker also tests a distinct one-agent construction for \(0\le r\le4\) atoms and \(1\le n\le30\) worlds. It instantiates the complete Boolean valuation types, a universal initial S5 relation, and the disjunctive next-type announcement formula and asserts first stabilization after exactly \(\min\{n,2^r\}\) rounds.

These are finite sanity checks, not a substitute for the induction arguments in RESULT.md. The all-n claims rely on the common-target recurrence, alternate-pair induction, and the per-class valuation-type argument. The program has no dependencies beyond Python's standard library.

Independent mathematical and priority audits: not performed.
