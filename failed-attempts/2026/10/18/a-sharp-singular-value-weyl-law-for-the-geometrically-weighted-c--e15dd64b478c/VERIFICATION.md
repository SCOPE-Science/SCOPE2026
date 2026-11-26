---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For fixed 0<r<1 the weight-conjugation gives D(I−sqrt(r)S)^(-1) exactly; the Neumann factor is bounded and D is compact. In the frozen finite-band proof, head rows contribute at most δ/λ to the counting error and tail rows perturb the threshold by λ times O(1/M). The first and last retained block boundaries as well as internal boundaries have only bounded-rank coupling, since the polynomial has fixed bandwidth. Entrywise removal of those couplings leaves independent blocks. Multiplication by the restricted D sandwiches each block singular value between its two endpoint scalings; the Toeplitz-to-circulant replacement has bounded rank. The Fourier grid distribution therefore gives upper/lower Darboux sums for the symbol's level distribution. One-sided envelopes suffice at jumps (including a constant-modulus symbol). Sending mesh size and head cutoff to zero and tail cutoff to infinity gives the layer-cake coefficient. Polynomial truncation at B has error singular values at most t^(B+1)/[(1−t)n] for t=sqrt(r), by the ideal inequality; the count inequalities with thresholds (1±γ)λ give the claimed limit as truncation and γ are taken to zero. Count inversion and harmonic summation give the exact Schatten and Dixmier trace statements. The constant is strictly greater than 1 because the analytic symbol has mean 1 and nonconstant phase. For nonzero eigenvalues, the first nonzero coordinate forces λ=1/m; writing y=(I−tS)^(-1)x produces y_n proportional to binom(n,m)t^(n−m) for n≥m and zero earlier, an ℓ² eigenvector after applying I−tS. The first m rows exclude a generalized vector solving (A−λ)z=x for that eigenvector, so the eigenvalues are simple. RESULT.md, VERIFICATION.md and the numerical verifier were inspected; the verifier was not executed and finite sections are not used to certify the law.

## originality

FAIL

The exact leading law, including its trace constant, is a direct specialization of the classical Birman–Solomyak singular-value Weyl law for negative-order classical pseudodifferential operators on closed manifolds. The applicability is constructive, not a possible overlap inferred from a title or from unavailable literature. The standalone block proof is correct but does not change this statement-level coverage.

## value

FAIL

The geometric weighting is natural and the elementary block argument is a useful presentation. But the sole sharp invariant and associated trace/Schatten distinctions asserted here are mechanically obtained from the standard symbol law by the exact Hardy identification. The stated result does not add a remainder, new parameter regime, obstruction, or new useful lemma outside that coverage. The alternate proof is not a distinct new scientific claim at the required bar; no surviving repaired claim is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
