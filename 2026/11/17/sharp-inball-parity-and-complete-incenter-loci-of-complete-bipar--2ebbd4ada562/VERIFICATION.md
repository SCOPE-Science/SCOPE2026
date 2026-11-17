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

# Checks and limits

The accompanying `verify.py` uses exact fractions, exact integer sign enumeration and exact matrix ranks via SymPy. Executed using `python3 verify.py`, it returned `PASS: 1462 exact rational checks over 25 bipartition pairs plus six balanced cases`.

The checks cover every integer \(2\le p,q\le6\): all signed facet normals are constructed and deduplicated, maximal squared normal length and origin tangency multiplicity are verified, the rank and codimension of the active-normal span are computed, and full supporting-face rank is independently checked when \(p+q\le9\). In six balanced-even sizes through twelve, exact symbolic tests confirm the monotonic endpoint comparison.

The unrestricted proof does **not** rely on these finite tests. Its nonstandard infinite steps are the extreme-potential tight-graph criterion, the parity-sensitive spanning lemma and the fact that strict slack on nonactive facets permits a relative neighborhood of optimal centers. These steps are supplied in `RESULT.md`. The tests neither establish absence of equivalent prior literature nor constitute an independent external audit.
