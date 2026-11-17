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

Expand cubic self-ambiguity to an imprimitive quadratic Gauss sum. For each k!=0, t=v_p(k), C(k,l)=0 iff p^t does not divide l; nonzero modulus p^((a+t)/2). Perturbation contributes epsilon*omega^(-k^3)*(1+omega^(lk)); nonzero Gauss values dominate 2epsilon since p>=5,a>=2, while zeros have minimum 2epsilon sin(pi/(2p^(a-1))), attained at k=p, l=(p^(a-1)±1)/2. Normalize by N+2epsilon+epsilon². Weyl conjugation diagonalizes the full N²×N² complex-linear lifting with singular values sqrt(N)|A_g|; a valuation census gives unperturbed rank (pN²+1)/(p+1), and derivative proves epsilon=1 best within (0,1]. Independent direct DFT checks at N=25 (epsilon 0.4) and N=49 (epsilon 1) reproduced exact minima/ranks; only proof handles all p,a.

## originality

PASS

Best-of-knowledge: one positive real impulse exactly repairs all prime-power cubic Gabor ambiguity zeros, with sharp all-mode margin/condition number. An earlier published cubic-chirp theorem already establishes the unperturbed zero pattern, full singular spectrum and identical rank, so that portion is not claimed new. Li 2026 already establishes cubic prime-power obstruction and general algebraic window constructions; general Gabor diagonalization is earlier. Neither the inspected full published comparison nor accessible Li abstract establishes this particular quantitative single-real-impulse cubic repair; inaccessible Li full text leaves material priority risk.

## value

PASS

The natural cubic chirp has a macroscopic rank defect for Gabor full-linear intensity tomography at prime powers; a single explicit positive real impulse removes ALL zeros and gives a sharp stability constant and exact pre-repair nullity. It responds quantitatively to a natural obstruction, beyond a routine normalization or experimental sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
