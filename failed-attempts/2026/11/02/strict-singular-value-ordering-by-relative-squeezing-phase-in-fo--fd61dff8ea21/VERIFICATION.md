---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reviewed RESULT.md lines 5–117 and the verification notes and supplied matrix checker by inspection. Each factor is Hilbert–Schmidt by the monomial generating sum and the subcritical Gaussian integral. The reproducing kernel of T is exp(tz²+conj(s) w̄²+r²zw̄); the second Gaussian integral gives Q=TT* with a=t+bs, b=r⁴/σ and c=σ^(-1/2). The bound 2|a|+b<1 gives p>2b and b<d≤1, including the possible cancellation a=0. For the spectral lemma the kernel is positive trace class also directly as cVV*, with Vf(z)=exp(az²)f(√b z). The larger root gives h=ad/(d−b²), |h|<1/2; applying the kernel to the stated entire generating family rescales its generating variable by b/d. The nonzero coefficients are eigenvectors of distinct eigenvalues, and equality of the diagonal trace and their geometric sum excludes any residual positive eigenvalue. Square roots and geometric summation give the claimed singular values and Schatten formulas. At fixed positive magnitudes, |a|² grows strictly with the phase cosine, d decreases strictly, and all singular values therefore grow strictly. Independently, a 48×48 monomial-basis computation at r=0.4, t=0.07 exp(0.47i), s=0.05 exp(−0.83i) agreed for the first four singular values (1.00754410097,0.16364855562,0.02658032510,0.00431726195), with max discrepancy about 2.2×10^−16; aligned and antialigned phases bracket those four values. The uploaded checker was not executed and finite agreement does not establish the spectrum.

## originality

FAIL

The full spectrum and its strict ordering are covered by the known thermal normal form for a Gaussian density operator plus a direct one-mode covariance substitution. This is stronger coverage than a geometric upper bound or the restricted canonical Fock SVD; it does not require anyone to have previously used the submitted notation or stated its relative-phase comparison verbatim. The explicit implication below covers all independent phases and all indices. No distinct surviving scientific claim was established for repair.

## value

FAIL

The operator family and phase optimization are naturally motivated and the formula is a convenient specialization, but the claimed exact invariant and monotone order are mechanically recovered from the known Gaussian thermal spectrum. The elementary proof and numerical agreement do not establish a separate novel, useful boundary, ordering mechanism, or invariant that could be retained on repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
