---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For every n>=5 and 0<=r<=n, the Walsh basis is globally orthonormal under 2^-n counting measure. Each compressed Gram entry is the exact binomial Fourier coefficient indexed by |I Δ J|. Decomposing coefficient space under S_n into the 3-dimensional trivial block, two (n-1)-dimensional standard copies, and a C(n,2)-n dimensional row-sum-zero quadratic block yields S,T,u with complete multiplicities. Interpolation in Boolean coordinates b_i=(1-x_i)/2 and inclusion-exclusion on all subsets of size <=2 proves the sharp injectivity radius 2, ranks for radii 0/1 and determinant 2^(-nD+2n+4*C(n,2)); the observation count is exactly D. Independent SymPy expanded the unnormalized radial and standard block characteristic polynomials symbolically in n, obtaining the stated cubic, quadratic, their determinant 64, and scalar scaled eigenvalue 16. The cubic trace is ~n^4/4, the (3,3) Rayleigh lower bound is ~n^4/4, its second symmetric sum ~n^4, and its product 64; thus the three roots are ~n^4/4, 4, 64/n^4. Standard roots are ~4n^2 and 16/n^2, leaving sharp eigenvalue condition ~n^8/256 and restriction singular condition ~n^4/16. Independent full Walsh Gram enumeration for n=5..9 all 40 radii, plus n=5..10 all 51 spectra/ranks, and exact square evaluation determinants n=5,6 agreed. Finite computations corroborate, but the invariant block and root proofs establish all n. Degenerate r=0,n and n>=5 boundaries checked.

## originality

PASS

Best-of-knowledge, qualified: earlier Hogan–Lakey work provides the Slepian operator, general rank theorem and invariant-block/eigenspace procedure; it is explicitly not new. The claim surviving is the all-radius closed quadratic spectrum with sharp minimal-radius determinant and dimension-eight condition exponent including leading 1/256 constant. Neither the inspected full 2019 primary theorem/table nor the 2018 reduction states that exact special-case sharp instability, and close published low-band ball, quadratic shell, and majority-halfcube results do not imply it by mere eigenvalue reuse. General Terwilliger decomposition supplies strong methodological coverage but needs specialized ball moments and asymptotic root analysis. A 2021 direct continuation is plausibly stronger and remains inaccessible in full; no negative claim is inferred from its preview, and residual priority risk is explicit. Novelty is bounded, not certified.

## value

PASS

A degree-two Walsh signal has D independent coefficients, and the radius-two Hamming ball contains exactly D data points: a natural information-theoretic minimal cardinality sampling geometry. The result determines a complete exact spectrum across all radii and identifies the sharp, severe condition-number price of minimal injectivity, ~n^8/256 for Gram or ~n^4/16 for singular values; these rates are nontrivial spectral invariants not implied by rank or coarse numerical examples. A future researcher analyzing sampling, Slepian concentration or preconditioning on sparse Boolean domains could need these precise constants. No claim of optimality among other D-point designs or a noise recovery theorem is made. Prior general sector-reduction machinery alone is not being counted as new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
