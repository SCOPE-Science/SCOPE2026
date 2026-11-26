---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For indexed linear words avoiding both 000 and 111, a code is precisely a clique in the graph joining words with disjoint arbitrary one-deletion shadows. The output set must include descendants outside the run-limited source; both exact implementations do so. The branching takes each possible highest remaining vertex and then restricts to its neighbors; a proper coloring of each remaining prefix bounds any extension by its number of colors. This proves the soundness of exhaustion with pruning. A fresh standard-library implementation with a different coloring order reproduces the exact optima (1,2,2,3,3,6,6,10,13) and maximum ordinary VT intersections (1,2,2,3,3,6,6,10,12), with 110 permissible inputs at n=9 and residues (11,10,12,12,10,11,10,12,12,10). It checks the explicit thirteen-word code directly. For the classical VT property, on inserting bit b at slot i of a common descendant y, the checksummed integer increases by i b plus the suffix weight of y starting at i. For b=0 and b=1 these increases lie in the disjoint ranges 0 through wt(y) and wt(y)+1 through n. Within either range repeated increases can only come from moving the inserted bit through a run of identical bits, producing the same word. Thus the residue intersections really are codes, and the first strict gap is at nine.

## originality

PASS

The ordinary VT construction and the deletion-shadow packing formulation are established. None of the inspected distinct works gives the exact optimum for the two-symbol run ceiling of two with unrestricted endpoints, or the earliest conventional VT-intersection gap under that constraint. The mirrored copy of the assigned record is not a distinct covering result.

## value

PASS

Intersecting a VT class with a maximum-run-limited source is a published, natural construction for constrained deletion channels. The first length at which this method cannot be optimal is an informative boundary: the gain of one codeword changes the optimality verdict, with an explicit alternative code and an exact upper bound. This is a small-length benchmark for constrained-code constructions, not a general asymptotic claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
