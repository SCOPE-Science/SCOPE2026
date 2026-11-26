---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Polar substitution t=|z|² in the normalized Gaussian plane and angular orthogonality give the stated diagonal eigenvalues. Integration by parts gives Δλ_j=[a^j e^(−a)−(a+L)^j e^(−a−L)]/j!, which is negative for every j at a=0 and for a>0 changes sign at most once from positive to negative as j increases. The minimum of a consecutive band is therefore an endpoint. The endpoint ratio is E[(a+S)^N]/N! for S with density e^(−s)/(1−e^(−L)) on [0,L]; it starts below one and increases strictly to infinity. At c_N=L/(e^(L/N)−1) all adjacent differences except the last are positive, and the last is zero, so the unique crossing is before c_N for N≥2 and at c_N for N=1. The last mode increases strictly up to c_N and the vacuum decreases strictly, proving unique optimal placement. At equal endpoints the sign pattern forces every interior eigenvalue strictly higher, even when adjacent modes share the peak. The integer Gamma integral gives the polynomial crossing equation. For fixed L, bounding S gives (N!)^(1/N)−L≤a_N≤(N!)^(1/N); Stirling and bounded convergence now give E[(1+S/a_N)^N]→J(L), the stated additive radius expansion, and the sharp energy equivalent. At fixed N, expansion of the same moment near (N!)^(1/N) yields −E[S]=−L/2+O_N(L²) as the first correction.

## originality

FAIL

The main theorem is demonstrably covered by distinct indexed source 98cfe113102e: its finite Hermite-band Gaussian STFT optimizer is unitarily the same finite-band Fock optimizer for every N≥2 and L>0, with the same unique balance, optimal value, equality modes and sharp fixed-area N/e expansion including constants. The frozen related-work comparison omits that decisive source. This decision rests on exact mathematical coverage in the original text, not inferred publication order, authorship or common notation. The N=1 case is implied by a separately inspected primary theorem; the polynomial restatement and fixed-N thin-area Taylor correction do not restore the claimed originality of the frozen main result.

## value

FAIL

The maximin design question itself is useful: a least eigenvalue quantifies worst-case energy capture in a finite band. But the submitted contribution repeats a complete solution of that same useful question. After accounting for the equivalent theorem and the covered N=1 case, the polynomial restatement is an incomplete-Gamma evaluation and the fixed-N thin-width shift is the immediate midpoint term of a Taylor expansion of the same root; no separate motivated new design gap or substantive extension is established by those additions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
