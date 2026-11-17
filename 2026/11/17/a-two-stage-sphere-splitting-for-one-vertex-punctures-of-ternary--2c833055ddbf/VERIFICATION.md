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

Run `python3 verify_ternary_puncture.py` with Python 3 standard library. The program reconstructs all graph neighborhoods rather than reading precomputed face lists. It verifies both link-nerve intersection patterns for \(d=3,4,5,6\), checks every explicit local triangle-filling disk for those parameters, and enumerates all simplicial faces and binary boundary matrices in dimensions \(d=2,3,4\).

The exact checks reproduce loss counts \(14,34,62,98\) at \(d=3,4,5,6\), and the complete homology check gives \(H_2\) rank \(56\to42\) at \(d=3\) and \(489\to455\) at \(d=4\). At \(d=2\) mod-two reduced first homology changes rank \(2\to3\) and reduced second homology \(1\to0\), illustrating that the hypothesis \(d\ge3\) is substantive. Exact recorded stdout appears in `verification_output.txt`.

These are **finite mod-two tests**. They do not certify integral homotopy in arbitrary dimensions. Infinite-dimensional correctness rests on the two proved nullhomotopy attachment arguments, the simply connected clique complex of the auxiliary multipartite graph, and the standard simplicial homotopy-pushout theorem. The absolute integral Betti numbers additionally use the prior published calculation for the intact complex. The resulting equivalences are not claimed equivariant. There has been no independent external audit.
