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

Put M=N+1. The unitary row DFT at each radius groups z^j with bar(z) z^(j+1) for 0<=j<N, and groups z^N with bar(z) in the last residue. Each 2-by-2 determinant acquires M, and the first N unnormalized determinants are (rs)^j exp(ij phi)(s^2-r^2); the last modulus is rs times the displayed residual modulus. Squaring yields (1) and the exact N=1 rank exception. Scaling both radii by s multiplies the squared determinant by s^(2M^2); the shape factor is nonnegative, not strictly positive at N=1 with aligned diameters as one sentence of the frozen proof says. This harmless wording does not affect any claim: those shapes have zero determinant and the maximizer is positive; the rank exception is explicitly correct. The angular factor is strictly maximized by exp(iM phi)=-1. On this branch the log objective is strictly concave: its potentially positive last curvature term is at most 2b(b-1)/t^2 for b>1, less than a/t^2; for b<=1 it is nonpositive. The objective vanishes at 0 and 1, giving a unique interior root, with t_1=1/3. Equation (2) gives 2Nt/(1-t)=N^2/2+O(N), hence 1-t=4/N+O(N^-2). The open disk has the same supremum but no maximizer by scaling. Independent explicit matrices (18 determinant comparisons across N=1,2,3,4,8,16), aligned ranks for N=1,2, and direct log-determinant optimization agree; independently calculated t_2=0.3729574942374566 and t_8=0.6543792459132516. Replay: python /workspace/branches/reproduce_frozen.py (disks section). Inspected the frozen checker and verification notes without execution. This is not an unrestricted Fekete-node theorem.

## originality

PASS

The best-supported distinction is the exact finite bianalytic evaluation factorization, non-generic rank classification and joint radius/phase solution for each degree. Half-step staggering of cyclic kernel orbits and general generic-rank theory are already known; the claim does not rest on those features alone.

## value

PASS

Two equally populated rings are a natural minimal symmetry-restricted sampling design for radially and angularly structured disk data. The theorem supplies usable exact nodes for every degree, shows exactly when rank fails, and tells how close the rings must approach each other in squared radius at high degree. This is more than reusing a familiar staggered phase, though no claim is made about spectral conditioning or unrestricted nodes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
