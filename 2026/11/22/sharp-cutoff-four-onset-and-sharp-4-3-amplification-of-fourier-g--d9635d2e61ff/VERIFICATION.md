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

With normalized Fourier modes the generator entries are −mk a_{m−k}. The only positive exterior couplings are the pairs (K+1,K−1), (K+1,K), (K+2,K), with absolute entries γa_K/2, βb_K/2 and γc_K/2. The negative block is its conjugate and the input blocks are disjoint even at K=2. Symmetry gives leakage E_K*E_K, hence the squared largest singular value of one block. For y=γ²/s² its normalized Gram matrix has trace B+dy and determinant ACy² independently of phase; the larger root is simple also at y=0 and y=1. The factors (a+c)²−B and B−(c−a)² are positive for K≥2, so Δ>0. Differentiation gives λ'(0)=d>0 and λ'(1)=C(C−A−B)/(C−A). An interior stationary point must have y=2Bd/Δ and λ=4ACB/Δ; since Δ−2Bd=B²−(C−A)², its candidate lies inside exactly when K⁴−2K³−5K²+1>0. The polynomial is negative at 2 and 3, positive at 4 and increasing thereafter. Thus for 2,3 the root increases to C; for K≥4 the derivative sign change guarantees that the unique candidate is attained and maximal. Normalizing A,B,C,d by K⁴ and Δ by K⁸ gives limits 1 and 3 respectively, so y→2/3 and the gain over the stronger pure harmonic approaches 4/3. Positivity of the coefficient follows from β+γ≤√2s.

## originality

PASS

The Galerkin residual identity and first-harmonic leakage are prior work. The supported distinct claim is the unique two-harmonic energy allocation, exact cutoff-4 onset and asymptotic 4/3 gain under that budget. The exact published catalogue hit is this very finding, not a separate antecedent. The assessment is bounded to the examined evidence.

## value

PASS

In the simplest family where two coefficient modes compete for the same spectral boundary, this gives a sharp benchmark for a motivated Galerkin projection defect. It shows that the stronger pure harmonic can be extremal at small cutoffs yet cease to be so exactly at K=4, and quantifies the persistent gain rather than just exhibiting one favorable mixture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
