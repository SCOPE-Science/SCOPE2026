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

# Reproducibility and limits

Run `python check_enumeration.py` and `python check_ranks.py` using Python 3 with no third-party dependencies. Compare their outputs with the included `check_enumeration.txt` and `check_ranks.txt`.

The enumerator visits all \(2^{16}=65{,}536\) binary two-layer states on the eight-vertex sunlet and computes each state's first return, independently of the algebraic proof. The second checker constructs an explicit labelled adjacency list, evaluates powers of the \(\mathbb F_2\)-linear temporal map, and obtains fixed-space dimensions by binary Gaussian elimination for \(n=4,8,16,32,64\). It additionally checks the exact operator order on those instances.

The general result for all dyadic circumferences and every characteristic-two extension field is proved symbolically via the module \(\mathbb F_q[z,z^{-1}]/((z+1)^n)\), not by extrapolating finite tests. The checks do not establish priority and do not constitute independent mathematical review.
