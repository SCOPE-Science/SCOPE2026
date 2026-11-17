---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Direct one-step matrix diagonalization gives delta=max_j x_j|x_j-x_{j+1}| with x_{N+1}=0. For any δ bound the quadratic yields x_j≤(x_{j+1}+sqrt(x_{j+1}²+4δ))/2 and strict monotonic propagation forces x_j≤sqrtδ R_{N+1-j}. Norm-one gives δ≥R_N^-2, and equality recursively forces x_1=1 and every x_j=R_{N+1-j}/R_N, phases arbitrary. Identity R_k(R_k-R_{k-1})=1 proves attainment, and R_N²=2N-ΣR_k^-2 with k≤R_k²≤2k gives convergent harmonic error, R_N²=2N-(1/2)logN+O(1) and reciprocal expansion. N=1 included. The independent finite checker validated 3605 exact/near-exact cases and is not the all-N proof.

## originality

PASS

Recent reduced-Embry results characterize exact quasinormality from multiple moments, rather than quantifying the sharp single-moment residual at norm one on finite nilpotent shifts. The closest prior sharp Schatten-fourth shift theorem optimizes a different nearest-neighbor quadratic norm. No inspected exact prior theorem implies this nonlinear backward-envelope recurrence or its unique extremizers. The plausible 2010 paper on exact equality could not be read in full and remains a real priority risk, not an automatic failure.

## value

PASS

A single approximate Embry moment on a norm-one nilpotent shift is a natural finite-dimensional quantitative quasinormality model. This theorem solves the complete all-dim minimax, proves a unique taper, and finds an asymptotic vanishing defect with nontrivial (log N)/N² correction, precisely measuring the absence of a dimension-free gap. Not a textbook evaluation of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
