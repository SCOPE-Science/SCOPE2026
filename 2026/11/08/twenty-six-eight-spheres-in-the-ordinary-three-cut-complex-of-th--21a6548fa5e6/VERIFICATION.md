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

# Verification protocol and limits

The standalone `verify_frucht_cut.py` requires Python 3's standard library only. Run `python3 verify_frucht_cut.py` from the directory containing the files. The record in `verification_output.txt` is the actual stdout from this invocation; the program terminates with an error if an assertion fails.

The code independently defines both the Alexander-dual membership predicate (every induced triple connected) and the ordinary cut-face membership predicate (the complement contains a disconnected triple); all \(4096\) subsets are cross-checked. The dual has \(12\) vertices, \(66\) edges, \(30\) triangles and \(1\) tetrahedron. The code verifies each of the thirty elementary free-face pairs, prints their explicit ordered vertex lists, and confirms a remaining connected graph of \(12\) vertices and \(37\) edges. Thus the integral dual first homology has rank \(26\).

An independent mod-two boundary calculation for the original cut complex yields zero reduced Betti numbers in all degrees other than degree eight, where it gives \(26\). It does not certify integral torsion by itself; the integral conclusion follows instead from the simplicial collapse and the combinatorial Alexander-duality theorem combined with Hurewicz and Whitehead as proved in `RESULT.md`.

The verification is exhaustive **only for the labeled twelve-vertex graph**. No claim about all asymmetric or cubic graphs is made. Independent external audit is not yet performed.
