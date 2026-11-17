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

In the real normalized Fourier basis of 1 constant plus r cosine/sine modes, demixed two-sensor samples have one constant column and r square 2×2 blocks. The raw time matrix is diag(V,V) times this demixed map, V the Vandermonde of distinct real spectral values. In the codimension-one rectangular case Cauchy–Binet/cofactor transport yields det(B*R*RB)=|det R|² det(B*B)||R^{-*}w||²; w is the sensor-block difference in the constant coordinate. Solving V^T a=e0 via the Lagrange cardinal polynomial gives the exact sum a_t², hence determinant factor (2/N)^(2r+1)(det V)^4(sum a_t²)∏sin²(2πkd/N). Rank is full iff N/gcd(N,2d)>r. For r=2, y=sin²θ gives 4y²(1−y), unique max y=2/3, so every discrete D-optimum belongs to floor(Mα),floor(Mα)+1; the algebraic-integer obstruction forbids reaching 16/27 on a finite rational grid. A global second derivative bound gives O(N^-2) and strict mismatch with demixed condition-optimum for 6|N,N≥42. Independent full raw Fourier-sample Gram comparisons matched 219 (N,r,d) cases; finite tests are corroboration, not proof.

## originality

PASS

The closest full published finite-cycle result optimizes the spectrally demixed frame condition number, which is a different measurement norm; the new codimension-one raw Gram determinant transport, evolution-independent sensor-volume maximization and explicit five-mode optimum are not stated there. The full published normalized-path determinant theorem covers a single sensor and different graph spectrum. General graph dynamical-sampling literature motivates but does not visibly entail the exact raw-trajectory law. Best of knowledge, with inaccessible recent full primary sources explicitly noted.

## value

PASS

A natural exact D-optimal design criterion for untreated space-time measurements yields a universal determinant formula independent of evolution for sensor placement and reduces every five-mode cycle to two candidate gaps; it sharply demonstrates that optimal demixed conditioning and optimal raw information volume can disagree. The distinction prevents a common but mathematically invalid transfer of measurement criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
