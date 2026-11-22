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

Run `python verify.py` in this directory with Python 3 and no external packages. The program constructs feasible orders by independently calculating the number of star edges crossing each prefix cut. It builds legal adjacent-position swaps and breadth-first distances directly, then checks the theorem's vertex counts, component structure, edge counts, all pairwise distance values in the connected case (using the exact leaf-label-relabeling symmetry), and connected-component diameters in the frozen-hub case.

The completed run passed every budget for \(2\le r\le7\), plus \((r,k)=(8,4)\) and \((r,k)=(8,5)\), totalling 35 parameter cases. The largest completed graph has 120,960 vertices and 443,520 edges. The proof in `RESULT.md` separately covers all integers \(r\ge2\) and \(0\le k\le r\); finite checks do not establish infinite validity. Independent mathematical audit has not been performed.
