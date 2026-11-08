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

# Executable and theoretical verification

Run the embedded standalone `verify.py` under Python 3. No external Python modules, third-party source papers or network access are needed. The supplied `verify_output.txt` records the observed successful execution.

The program enumerates each face directly using the graph-theoretic criterion that no three selected graph edges are mutually disjoint. Independently it generates the contractible core and each two-path join. For every size \(1\le m\le4\), it asserts equality of the entire face sets, every ball–core boundary intersection and all pairwise ball overlaps. It computes the simplicial mod-two boundary ranks, checking \(\widetilde H_3\) has rank \(\binom m2\) and all other reduced mod-two groups vanish. It builds relative integral fundamental three-chains of the nine-tetrahedron joins, checks their boundaries lie in the core, and checks local-reflection and adjacent-block-permutation signs on those actual chains.

Observed counts include the empty face: 16, 137, 715 and 3478 for \(m=1,2,3,4\), respectively. All checks returned `PASS` and the run ended with `ALL_VERIFY_OK`.

These finite checks do not prove the theorem for arbitrarily many blocks. The general proof is the exhaustive active-outer-block classification, exact simplicial decomposition, three-ball boundary identity, and CW quotient argument in `RESULT.md`. The possible scientific limitations are a misidentification of an existing stronger classification or an unstated change in the graph-identification hypothesis; neither is resolved by finite experiments. The result has undergone self-review only; no independent audit or external certification is asserted.
