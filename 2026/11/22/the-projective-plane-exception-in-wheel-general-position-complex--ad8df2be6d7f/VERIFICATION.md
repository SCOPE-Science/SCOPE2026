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

# Reproducible verification

Run `python VERIFY.py` with Python 3 and SymPy installed. The script reconstructs the wheel graph distances and forbidden triples directly; it does not reuse external numerical files.

It verifies the exact center–rim face decomposition for rim sizes \(4\le n\le13\), and the complete four-vertex simplex case at \(n=3\). It verifies the explicit nullhomotopy triangle cones for every rim size \(6\le n\le80\). For the five-vertex rim, it enumerates the five Möbius-band triangles, checks boundary incidence and vertex-link paths, and computes Smith invariants \((1,\ldots,1,2)\), establishing first integral homology \(\mathbb Z/2\). It also checks finite Morse critical-cell counts for the published higher-independence formulas at \(6\le n\le16\). All checks returned PASS when replayed from the package.

The infinite proof is given in `RESULT.md`; it uses a direct elementary nullhomotopy and the explicitly credited theorem of Deshpande and Singh. Exhaustive checks on finite ranges are not substituted for that theorem. These checks are ordinary same-model reproducibility tests only; an independent audit has not been performed.
