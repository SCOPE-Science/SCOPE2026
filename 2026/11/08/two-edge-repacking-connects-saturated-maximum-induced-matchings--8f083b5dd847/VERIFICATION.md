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

The source files `direct_verify.py` and `structural_verify.py` are standalone Python 3 programs requiring only the standard library. Run `python3 direct_verify.py` and `python3 structural_verify.py` in the directory containing the files; compare their stdout with the embedded `direct_output.txt` and `structural_output.txt` respectively.

The direct implementation explicitly builds the original rook graph edges, tests induced matchings using endpoint nonadjacency, enumerates all \(2t\)-edge optima for \(t=1,2\), checks that no \((2t+1)\)-edge induced matchings exist in these cases, constructs exchanges and breadth-first-search distance layers. It finds 9 and 8100 maxima and \((1,8)\) and \((1,42,705,4904,2448)\) distance profiles. The structurally independent implementation uses permutations of labeled row and column resources instead of graph-edge backtracking, constructs all proposed exchange moves, checks inducedness directly, and confirms the valency and connectivity for both small cases.

The unrestricted assertions are justified by a separate combinatorial proof in `RESULT.md`. Finite checks do not prove all-size connectivity or the factorial formula. The diameter assertion is confined to \(t=2\) and combines exhaustive one-source BFS with the proved vertex-transitivity. No external or independent scholarly audit is asserted.
