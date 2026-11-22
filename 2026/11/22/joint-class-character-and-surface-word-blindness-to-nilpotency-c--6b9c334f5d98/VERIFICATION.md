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

The construction requires \(p\ge5\), \(n=2p\), and \(b=p\). Its two Jordan partitions are \((p-1,3,1^{p-2})\) and \((2^p)\). Both obey \(N^{p-1}=0\), have \(\dim\ker N=p\), and have different nilpotency indices. Proof-level checks establish that \(\operatorname{im}(T^j-I)=NV\) for all \(j\ne0\), then give exact conjugacy class and irreducible degree counts and the conditional uniform commutator law.

Executable artifact: `checker.py`, standard Python 3, no third-party dependencies. Run `python checker.py`. Captured result: `checker_output.txt`; terminal line `ALL CHECKS PASS`.

The checker constructs eight finite-field examples for \(p=5,7\). For the two small four-dimensional module partitions at each prime it exhaustively enumerates every conjugacy class of the associated groups. For the large partitions, it checks finite-field action ranks and all conditional commutator-map image ranks, not all enormous group elements. These finite checks do not constitute proof of the all-prime statement; the paper's algebraic argument is required. No independent audit was performed.
