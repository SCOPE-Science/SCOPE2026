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

# Verification record

Run `python3 check.py` in a directory containing the standalone Python source. The program uses only the Python standard library.

The direct enumerator loops over every legal labelled cycle independent set for sizes \(5\le n\le20\), explicitly constructs every reachable one-token exact-two-hop neighbor, deduplicates target states, and compares the resulting histogram with the anchored-gap binomial formula. The aggregate number of independent sets inspected is **39,585**. It separately checks the vertex counts \(F_{n-1}+F_{n+1}\), the edge counts \(nF_{n-3}\), existence of each predicted degree, and the four-residue extremal counts. For lengths \(21\le n\le75\) it checks identities in the same analytic gap-count formulas; those tests are consistency checks, not independent enumeration.

The finite experiments are *not* an all-length proof. The all-length proof appears in `RESULT.md` and uses the local gap move characterization, rooted circular compositions, a finite case split for maximal mobility, and independent-set counts of a path.

No Lean proof, external expert audit, historical-priority guarantee, or independent mathematical certification is asserted.
