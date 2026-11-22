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

# Verification of the exact two-gate law

The proof in `RESULT.md` establishes the theorem for every finite affine plane of odd order. It does not assume the existence of coordinates. In particular, the only route from the possible rank-losing left kernel to two parallel line coordinates uses parity sums over all parallel classes; the candidate left-kernel vector is then explicitly constructed as the indicator of the union of those two lines. The factor of one entropy bit is proved by injectivity of the original transpose incidence map.

`VERIFY.py` provides an independent direct matrix-rank test using Python's integer bit operations. It constructs the point-line incidence matrix, toggles omitted entries, and recomputes its rank over \(\mathbb F_2\). All one-gate deletions and all two-gate deletion pairs were checked at \(q=3,5,7\), and all single plus 5000 seeded pairs at \(q=9\), built using \(\mathbb F_3[u]/(u^2+1)\). Exact output in `verification_output.txt` records each tested case count. This is not an exhaustive computational check for every plane order; the all-order claim depends on the written geometric proof.

Source comparison read the graph-state rank and edge-deletion sections of Hein–Eisert–Briegel (2003/2004), the main rank/graph-family sections of Severini (2005), and the complete relevant published even-order projective-plane theorem. The compared papers supply the foundations but do not directly state the affine odd-order two-gate iff. The independent review channel has not been performed.
