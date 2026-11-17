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
# Verification of the decagonal surface

Run `python3 verify_mirror_10.py`, using only the Python standard library. Its deterministic output is included in `verify_mirror_10_output.txt`. The script has independent constructions of (a) the union of all reflection-fixed mirror circles on sign words, and (b) the quotient barycentric flags of the whole cubical two-manifold. The mirror graph produces 424 sign vertices partitioned into ten components of cardinalities \(32,40,40,40,40,40,40,40,56,56\); the second construction finds 486 vertices, 1584 edges, 1024 triangles, Euler characteristic \(-74\), and boundary lengths \(8,8,8,8,8,8,8,8,16,16\). The counts use integer arithmetic and exhaustive supports; no numerical rank approximations or sampled faces are involved.

The zero/one sign-bit convention and the lexical order of triangle orbit identifiers are fixed in the script. The fifteen-triangle sequence \(58,57,51,15,14,13,12,3,4,5,22,24,53,55,56\) is a closed path across interior edges; each of the fifteen orientation transfers equals \(-1\). Their product is \(-1\), preventing a global orientation. With ten boundary components and \(\chi=-74\), the topological classification yields exactly 66 crosscaps. `verify_small_boundaries.py` independently checks the smaller even widths \(6,8\) and the later width \(12\); its output is included.

The general even-width mirror graph is established by the geometric fixed-arc argument in `RESULT.md`, not by extrapolating these finite computations. No homeomorphism result for arbitrary even width is asserted; the external independent audit has not been performed.
