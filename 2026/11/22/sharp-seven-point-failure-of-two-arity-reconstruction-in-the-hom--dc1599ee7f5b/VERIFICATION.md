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

# Verification protocol

Run `python3 verify.py` from the same directory; it requires Python 3 and no third-party modules. Compare its stdout byte-for-byte with `verification_output.txt`.

The program starts from the empty graph, obtains all one-point triangle-free extensions by enumerating independent old-neighborhood sets, and collapses isomorphism using degree-group-preserving canonical adjacency encodings. This is exhaustive for all triangle-free graphs through seven vertices. Every graph class is checked by exact subset bitmasks; counts of \((I,C)\) produce the complete uniqueness and cutoff certificate. The direct \(J\) count checks both third-arity witness values. Separately verified integer transfer matrices yield \(C=597\) for both bases, and \(J=11545\) versus \(11519\), confirming the numbers through a different counting method.

The output must show class counts \(1,1,2,3,7,14,38,107\), zero signature collisions through six points and exactly one two-element collision at seven points with \((I,C)=(36,597)\). The final line is `EXHAUSTIVE_FRAISSE_COLLISION_OK`.

This checks a finite census and the exhibited witnesses, not a claim of all-size exhaustive enumeration or independent certification. The all-size isolate propagation is proved symbolically by per-isolate state factors \(2,3,5\). The separate general Henson tuple-counting identities are prior work; their applicability is justified by the extension argument in `RESULT.md`.
