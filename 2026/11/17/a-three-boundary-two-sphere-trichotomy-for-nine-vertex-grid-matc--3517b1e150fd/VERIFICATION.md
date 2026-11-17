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

# Reproducibility of the finite homotopy certificate

Place `verify_torus.py` and `CERTIFICATE.json` in the same directory and run `python verify_torus.py`. The script uses only the Python standard library and reconstructs the three nine-vertex graphs from their coordinate definitions. It enumerates all matchings recursively and checks the result independently against every edge subset of cardinality at most four. It recomputes the mod-two simplicial boundary ranks, then **replays every pair** in the embedded elementary-collapse certificate while checking the free-face condition against the current complex. It checks that the surviving core is connected and two-dimensional; it independently checks that the supplied spanning trees reach every vertex. Finally it checks each triangular relation kills exactly one remaining fundamental-group generator and that no generator remains.

The certificate lists \(25+43+80=148\) elementary collapse pairs and \(26+48+74=148\) generator eliminations. The terminal two-dimensional Euler characteristics are \(6,17,27\). Standard topology then gives the integral homotopy theorem, including torsion-freeness and simple connectivity. The mod-two homology calculations are corroboration only; a finite mod-two calculation alone would not prove an integral homotopy equivalence. `CHECK_OUTPUT.txt` is the recorded execution output, not an alternate proof.

The checker has no network dependencies or hidden inputs. The mathematical result is limited to these three graphs, with no external independent audit performed.
