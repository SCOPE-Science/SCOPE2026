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

The set of available k-subsets grows, preserving every earlier distinct sample. On a sample operation, exactly E_{t−1}−D_{t−1} currently available subsets count as hits, even for multiplicities >2, so the predictable Bernoulli mean is q(E_{t−1}−D_{t−1})/binom(k+B_{t−1},k). This includes initial times. For B_{t−1}≥p(t−1)/2 the mean is bounded by C t^{1−k}, and the complement has exponentially small probability; summing expectations proves both claims for k≥3. Almost surely B_{t−1}=pt+O(t^{2/3}) by summable concentration. At k=2, a_t=O(1/t) eventually; the martingale differences divided by log(t+1) have a.s. summable conditional variances and bounded increments. Localization, convergence and Kronecker give M_n/log n→0, then D_n=O(log n). Substitution gives a_t=c_p/t+O(t^{-4/3}+log(t)/t²), so A_n−c_p log n converges a.s. and Σ a_t²<∞. The predictable variance is c_p log n+O(1) a.s.; divided by c_p log n it tends to one, and bounded increments give conditional Lindeberg at that normalization. The martingale CLT and the bounded centering error prove the stated normal limit. Both graphs have the same vertices and components, so Euler's cycle-rank formula subtracts exactly the number of repeat attempts. This applies for every fixed 0<p<1 without a percolation hypothesis. The frozen checker was inspected but not run; its enumeration and simulations are finite diagnostics and do not enter the proof.

## originality

PASS

The supported distinct result is the with-replacement repeat-attempt dichotomy, in particular the sharp graph constant, strong law and CLT. The birth-versus-uniform-selection mechanism is related to Krapivsky's model, but his triadic rule explicitly forbids repeated triples. The deterministic graph cycle-rank identity is a classical Euler consequence, not original by itself.

## value

PASS

The repeat count measures a natural difference between two practical graph versions that have the same connectivity. It is invisible at extensive scales yet diverges with a sharp constant and nontrivial fluctuation scale for pairs, while larger subsets cause only integrably many defects. The phase-independent theorem explains exactly what is lost by collapsing parallel edges in the graph case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
