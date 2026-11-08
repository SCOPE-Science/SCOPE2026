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

## Reproduction

Run `python3 VERIFY.py` in the directory containing `VERIFY.py`. It uses only the Python standard library and prints the output in `VERIFY_OUTPUT.txt`. The code constructs finite multiple chessboard complexes independently from the closed character expressions; the face predicate is compared against connected induced triples rather than reusing the chessboard description.

## Recorded checks

For orders \(4\) through \(8\), the mod-two reduced Betti vectors of the Alexander-dual complexes (in dimensions zero through three) are respectively \((0,4,1,0)\), \((0,5,0,1)\), \((0,6,0,19)\), \((0,7,0,71)\), and \((0,8,0,181)\). All \(120\) index permutations at order \(5\) and \(720\) permutations at order \(6\) were checked with and without class swapping; two deterministic 240-permutation samples at orders \(7\) and \(8\) were also checked. Exact chain ranks and signed chain traces were computed using integer bitsets and orientation parity.

## Scope of verification

The finite computation does not establish torsion-freeness or homotopy statements for arbitrary orders. The all-order proof uses a published pure-shellability theorem for a multiple chessboard complex, a relative-cell long exact sequence, combinatorial Alexander duality, and an exhaustive symbolic classification of fixed simplex types. Independent mathematical audit is not performed.
