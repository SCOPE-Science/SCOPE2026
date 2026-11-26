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

The spherical monomial integral and the radial gamma integral give the stated norm, and the torus characters of H applied to distinct monomials are distinct. Subtracting the squared norm of the analytic projection from the squared multiplication norm gives λ_α=(α₁+1)r_n−α₁r_(n−1), with the second term omitted for α₁=0. For x=(n+d)/m and a=1/m, the ratio Γ(x+a)/Γ(x) contributes 1+a(a−1)/(2x)+O(x⁻²) after factoring x^a. This gives the stated r_n expansion and its difference with r_(n−1). Multiplying that difference by α₁≤n leaves a uniform relative O(1/n), since 1−qα₁/n≥1/m. This both bounds the norm and makes the norm of the tail after truncating degrees tend to zero. With h=ε^(2/q), the high-shell lattice indicators are sandwiched by multiplicatively dilated regions with the stated angular radius; the low-degree shells disappear after the h^d normalization. The region is bounded with null radial boundary, so the lattice sum converges to its volume. The simplex Jacobian yields 1/d!, and the first-coordinate marginal is Beta(1,d−1). In the quartic d=2 case direct integration gives (1/8)·(31/80). Inversion of the positive counting asymptotic gives k s_k^p_c→C, whence the logarithmic mean and all normalized Dixmier traces equal C; strong Schatten summability fails.

## originality

FAIL

There is demonstrable equivalent coverage in a distinct indexed theorem, 0a1689d14441: not just the known membership threshold but the same sharp counting law, angular integral, quartic value and logarithmic residue for the whole specified family. This is a coverage decision, not a claim of earlier historical discovery by that record: its catalogue date is later than the frozen record's date. The older spectral diagonalization and membership literature is not by itself the basis for the failure.

## value

PASS

An exact angular counting law across the full radial-power family is mathematically useful independently of the attribution question. It refines the Schatten cutoff to a normalized critical trace and shows why dimension counting alone does not give the coefficient. The quartic value is a check on the general angular law, not an isolated tiny instance sold as a contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
