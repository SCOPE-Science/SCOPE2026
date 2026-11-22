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

# Verification and reproducibility

Run `python3 verify.py` with Python 3.9 or newer, using only its standard library. Its exact output is included in `verification_output.txt`. The program enumerates every partial-partition face for each integer \(2\le n\le7\), constructs explicit simplicial cycles for all complete non-singleton partitions, verifies integer simplicial boundaries and unit facet coordinates, and computes reduced signed Lefschetz traces using both chain-level simplices and the independently formulated induced-character rule for every conjugacy type. It confirms the strict-block-size quotient Betti prediction through \(n=7\).

The mathematical proof for all \(n\) relies on (i) Gottstein's integral cross-polytope homology basis, (ii) the coface-free equivariant facet-coordinate map, (iii) explicit signed stabilizer characters, and (iv) rational averaging and Frobenius reciprocity. The tests cannot establish a universal statement by extrapolation and do not constitute an independent audit. The quotient's integral homology, homotopy type and any unindexed literature equivalence remain outside the certificate.
