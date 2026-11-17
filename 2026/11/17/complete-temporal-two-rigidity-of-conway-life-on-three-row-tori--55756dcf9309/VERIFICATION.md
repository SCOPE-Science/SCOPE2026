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

# Reproducibility and limits

Run `python3 transfer_certificate.py`. It uses only Python's standard library, recomputes the full \(4096\)-vertex, \(6140\)-edge graph of mutually consistent two-time Life columns, and reconstructs every strongly connected component without a stored graph. It asserts precisely three cyclic components, whose vertex/edge sizes are \((30,75),(27,81),(4,4)\), as well as the four directed edges of the only non-phase-diagonal component. A closed-walk/periodic-configuration bijection then proves the theorem for all \(n\ge3\), including the circumference threshold.

Independently, run `g++ -O3 -std=c++17 direct_enumeration.cpp -o verify_direct && ./verify_direct`. Its direct cell-neighborhood masks enumerate all \(2^{3n}\) configurations for each \(n=3,4,5,6,7\). The exact populations in `direct_output.txt` are thereby checked independently of the transfer graph.

The two recorded output files correspond to successful runs of those programs. Neither a finite list of torus sizes nor a sampled numerical experiment alone establishes the universal theorem; its proof is the exhaustive finite graph and the closed-walk correspondence. No higher temporal periods, basins, or nonperiodic histories are classified here. Independent audit has not been performed.
