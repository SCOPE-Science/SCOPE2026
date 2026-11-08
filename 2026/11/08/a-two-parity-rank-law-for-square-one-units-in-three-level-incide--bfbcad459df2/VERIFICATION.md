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

Execute `python3 verify.py` in the directory containing this file. The verifier has no external runtime dependencies. It independently constructs all matrices \(A\) and \(B\) over \(\mathbb F_2\) for \(n=1,2,3\), tests every product \(AB\), calculates the rank of \(A\) by elimination, and multiplies its counts by the number of unrestricted \(C\)-blocks. It separately checks \(n=2\) over \(\mathbb F_4\) using field arithmetic modulo \(t^2+t+1\). It verifies the exact closed rank formula with rational-product Gaussian coefficients, and prints normalized total-count ratios for larger \(n\) as numerical sanity checks.

Expected exact values: \(\mathbb F_2,n=2\) yields rank multiplicities \((256,576,96)\), total \(928\); \(\mathbb F_2,n=3\) yields \((262144,1605632,1204224,86016)\), total \(3158016\); \(\mathbb F_4,n=2\) yields \((65536,307200,46080)\), total \(418816\). The script terminates with `VERIFY_OK` when all checks pass.

The checks are finite, not evidence of a proof for arbitrary \(n\). The general argument relies on exact kernel dimension and rank counts, convergence of finite-field Euler products, summable discrete-Gaussian tails, and the conditional full-rank probability of a random map into a prescribed kernel. The large-size ratio evaluations are floating-point corroboration only. No independent mathematical audit has been performed.
