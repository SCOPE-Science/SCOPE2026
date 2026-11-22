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

# Reproduction and boundaries

`verify.py` is a dependency-free, fully exhaustive check for \(5\le p<2000\). For each integer in that interval it independently tests primality of \(p\) and \((p-1)/2\), then checks every nonzero difference and every potential initial term using modular powers to identify primitive roots. The output checks exact exception sets and lists the 37 safe primes covered. All computations used for the finite boundary were run successfully from the standalone source file; no table lookup or approximation is needed.

For \(p\ge2000\), the analytic proof in `RESULT.md` supplies the universal claim through the cyclic-order characterization, two fixed-sign sets, the quadratic pair-sum identity and the squarefree Weil estimate. The numerical inequality at \(2000\) is an exact integer square comparison, and the required margin increases afterward. The code does **not** verify any unbounded range.

A second direct calculation at \(p=83\) gives the normalized five-nonresidue start set \(\{52,53,54\}\). For the quadratic-residue step \(3\), each start forces a term equal to \(-1\), giving a short independent obstruction witness. Source comparisons concern the exact *all-step* five-term assertion, not only the existence of a run at difference \(1\).
