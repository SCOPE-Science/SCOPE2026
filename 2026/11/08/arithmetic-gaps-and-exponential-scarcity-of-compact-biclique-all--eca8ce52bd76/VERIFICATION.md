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

Run `python3 verify_compact.py` using a standard Python 3 interpreter. The verifier independently constructs induced adjacencies for each complete bipartite instance, computes graph distances by breadth-first search, and tests all allowable center subsets; it does not call the generating-function or star-center criteria to decide compactness. It counts all labeled equitable allocations and compares the results with exact combinatorial predictions.

Test coverage: 51 parameter settings and 1,506,716 complete equitable allocations, with equality of the three predicted counts in every setting. Additional integer coefficient computations check the balanced four-item fraction at even sizes \(2,4,8,16,32,64\). These numerical comparisons are finite, are not infinite proof certificates, and do not independently validate originality or value. The universal theorem is established by the written proof, including the central coefficient asymptotic via Fourier inversion.

The exact printed examples are \(N_{1,1}=0\), \(N_{1,2}=N_{2,1}=29{,}700\) for \(K_{6,6}\) and \(n=3,q=4\), and \(N_{1,1}=7{,}526{,}400\), \(N_{1,2}=N_{2,1}=47{,}745{,}600\) for \(K_{8,8}\) and \(n=4,q=4\). External independent validation has not been performed.
