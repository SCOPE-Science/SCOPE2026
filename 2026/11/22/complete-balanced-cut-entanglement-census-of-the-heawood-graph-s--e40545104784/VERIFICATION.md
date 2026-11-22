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

## Reproducibility

Use Python 3 with standard library only. Invoke `python3 verify_direct.py` and `python3 verify_blocks.py` from the directory containing those files.

The first independently constructs the adjacency matrix from binary point–line orthogonality, checks its 21-edge cubic structure, exhausts all 3432 labelled seven-element vertex subsets, and calculates their cross-adjacency ranks using integer bit masks. It also checks the exact mean \(5021/858\), canonical point–line rank four, and 336 maximal-entropy cuts each at crossing-edge counts eleven and thirteen.

The second uses the cyclic seven-triple Fano plane presentation and independent list-of-lists Gaussian elimination for the two square off-diagonal incidence blocks. It checks all 3432 cases, including the full point-count-by-rank table. Both return the common histogram \(\{4:100,5:980,6:1680,7:672\}\).

The analytic reduction from reduced-state Schmidt spectrum to binary cut rank and its normalization are in RESULT.md. The exhaustive computation applies only to the fixed 14-qubit graph; no generalization to larger projective planes or independently certified novelty is asserted.
