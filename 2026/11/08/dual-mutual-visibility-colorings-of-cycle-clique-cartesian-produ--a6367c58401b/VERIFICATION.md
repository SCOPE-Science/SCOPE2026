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
# Reproduction and limits

Run `python3 verify.py prism_certificate.tsv` with standard Python 3.10 or later. The checker uses direct Cartesian graph adjacency, BFS geodesics and an independent exact-cover recursion.

- The 34 rows of `prism_certificate.tsv` exhaust the \(\binom42+\binom82=34\) pairs whose endpoints lie both in or both out of the selected four-set \(\{0,1,9,10\}\) of \(C_6\square K_2\). Each row supplies a shortest, selected-interior-free geodesic and the checker independently verifies lengths and interiors. This is a complete, finite certificate for the local compatibility lemma.
- All offsets \(j=0,\ldots,5\) in \(C_6\square K_2\), and \(j=0,\ldots,4\) in \(C_5\square K_2\), are checked from first principles. Only \(j=3\) of the six-cycle survives.
- All vertex subsets are independently tested on \(C_5\square K_m\) for \(m=1,2,3\), \(C_6\square K_m\) for \(m=1,2,3\), and \(C_7\square K_m\) for \(m=1,2\). The observed nonempty dual-set counts agree with the polynomial predictions.
- Independent exact-cover enumeration over the predicted sets gives minimum numbers of classes and unordered optimum counts for \(m=1,\ldots,5\): \((3,2),(3,2),(6,48),(6,48),(9,4320)\).

The unrestricted formulas are justified by the proof's convex restriction, the excluded-offset obstructions, the 34-pair local certificate, and perfect matching arguments. The smaller exhaustive instances alone do not establish the infinite family. The software does not assess historical priority or provide independent mathematical certification.
