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

# Verification and limits

The proof is in `RESULT.md`. For \(q\ge169\), it derives an explicit lower bound for the number of ordered, pairwise distinct nonzero-cubic-residue triples representing each target, positive by an elementary cubic-polynomial inequality. The proof treats every finite characteristic, including two.

The finite certificate for \(4\le q<169\) is reproducible without dependencies: execute `python3 verify_cubic_three_sums.py` (Python 3 standard library). It enumerates all \(24\) eligible prime-power fields and all \(131116\) unordered three-element subsets of their cubic-residue groups, checking every possible sum target. It checks extension-field multiplication, nonzero elements' \(q-1\) power, complete subgroup cardinality, total triples and exact missing counts. An expected success line is `VERIFY_OK fields=24 distinct_triples=131116 threshold=49 exceptional_covering_field=37`.

Finite exhaustion is a proof of the finitely many cases **only**, not the infinite theorem. The analytic inequality supplies the infinite range. Historical originality and independent mathematical audit remain unperformed.
