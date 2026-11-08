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

# Finite integral homotopy certificate

The graph is defined by the twelve Hamming-distance-one edges among the eight binary words of length three. Its line graph has twelve vertices and twenty-four edges. A face mask is accepted exactly when all induced vertex degrees are at most one. This tests all masks from 1 through 4095 without a sample or truncation.

`certificate.json` contains the explicit matched face pairs, critical faces, cube-edge labels and topological ordering. `verify.py` derives the complete face set independently from the graph, checks every certificate entry, and orients all 1512 covering relations. Kahn's exact directed-acyclicity algorithm removes all 455 face-poset nodes. There are 211 matched pairs, one unmatched zero-dimensional cell and 32 unmatched three-dimensional cells. By Forman's theorem this is a CW model with the stated integral sphere-wedge homotopy type.

`independent_homology.py` separately computes all 56 forbidden connected triples, enumerates faces and carries out mod-two simplicial boundary reduction. Its reduced Betti vector is (0,0,0,32,0); this corroborates but does not by itself prove the integral homotopy type.

To reproduce from the delivered package, place the four files `certificate.json`, `verify.py`, `independent_homology.py` and this document in one directory and execute `python3 verify.py` and `python3 independent_homology.py`. Compare with `verify_output.txt` and `independent_output.txt`. There is no external software dependency beyond Python 3 standard library.

Limitations: a finite proof for this particular graph only. Independent mathematical audit has not been performed; no statement about priority follows from machine verification.
