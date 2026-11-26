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

The finite sine sum gives (H_du)_i=cos((i-1/2)theta_k)/(2 sin(theta_k/2)); the proposed sine vector equals (-1)^(k-1) times that cosine vector. Its eigenvalues are ordered by decreasing magnitude, not algebraic size, and have alternating signs. Alternatively H=U J for unit upper triangular summation matrix U and reversal J, so H^(-1)=J(I-S) for upper shift S. Its square is the tridiagonal first-difference Gram matrix with cos((i-1/2)theta_k) modes. Full column rank permits rectangular congruence after extending a basis, giving exactly n-d additional zeros. For every B, loading is equivalent to H+eta I being PSD (take B=I); k=2 is the most negative eigenvalue, including d=2. In a symmetric binary PSD supermask, all entries in row one are one, forcing all diagonal entries to be one by principal minors. The zero quadratic forms on e_1-e_j then force every column to equal the first. The d(d-1)/2 additions count ordered products. The geometric positive-vector example has invertible B for q>0 and each missing product has norm at most (d+3)q^d; the full Gram norm is at least d+3. For fixed d the relative error goes to zero while negative inertia persists. The d=2 determinant is -9q^2. Independent bounded check: 63 inverse spectra (d=2 through 64) and exact negative principal-minor witnesses for all strict completions among 598 binary masks (d=2 through 6), via python3 /workspace/branches/reproduce_records_1_to_4.py. The universal claims follow from proof, not these ranges. Frozen verification and same-model evidence were read, not counted as independent experiments.

## originality

PASS

Best-of-knowledge pass for the combined ideal triangular Gram cone diagnosis, limited to the product-retention rigidity and explicit arbitrarily accurate yet indefinite split families as distinct substantive content. Credit the classical Brownian spectrum and the signed-spectrum and diagonal-loading calculations that are direct consequences once its modes are known. No standalone novelty of those spectral constants or of Sylvester congruence is credited. The matching schedule is prior; inspected statements do not already establish the combined Gram conclusion. Direct Sra and Carson–Ma passage retrieval remained access-limited.

## value

PASS

For a motivated truncation schedule the result distinguishes normwise approximation from cone preservation in a complete ideal Gram model. It answers two distinct design questions with sharp boundaries: a scalar coefficient shift works at a precise cutoff, whereas a binary completion cannot save any omitted products. The positive, full-rank small-error example establishes that the obstruction is not limited to large relative error or mixed-sign inputs. No hardware or optimal accuracy claim is required or supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
