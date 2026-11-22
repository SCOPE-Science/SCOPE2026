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

Run `python3 verify.py` from this directory with Python 3.9+ (standard library only). Compare its standard output byte-for-byte with `expected_output.txt`.

The script reconstructs each wheel from its edges, computes every geodesic forbidden triple using graph shortest paths, and enumerates every vertex subset for rim orders \(3\) through \(12\). It separately implements the cone–cycle face criterion, confirms exact equality of the entire face collections, and computes all mod-two reduced Betti numbers by elimination of simplicial boundary matrices. In the special five-rim case, it additionally checks the face vector \((6,15,10)\), the two-triangles-per-edge incidence rule, connected five-cycle links at every vertex, and Euler characteristic one. These are the checks required for the finite surface recognition in the proof. No external data or network access is required.

The exact infinite-family proof is not a numerical induction: it invokes the verified published general cycle formula for two-independence complexes and the standard homotopy-cofiber splitting for a nullhomotopic circle map. The finite tests do not replace that theorem. The first integral homology at five rim vertices follows from closed-surface classification, not from mod-two ranks alone.

Independent audit: not performed.
