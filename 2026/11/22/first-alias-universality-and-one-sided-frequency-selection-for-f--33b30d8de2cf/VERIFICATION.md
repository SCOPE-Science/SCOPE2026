---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The analytic proof in RESULT.md is the certificate for the infinitely many frequencies. Its nontrivial steps are the exact scalar multiplier identity, pole residue normalization at every nonzero \(2\pi\)-alias, uniform escape control \(\varepsilon/u_T(\xi)\le [(c_*-\eta)|\xi|^\alpha]^{-1}\), and subsequence exclusion of nonfirst aliases. These checks cover every \(T\downarrow0\), not only sampled sequences.

The standalone Python 3 program `verify_first_alias.py` was executed from the packaged files and passed 168 finite scalar diagnostics across three explicit fractional exponents, unequal/symmetric directional coefficients, lower-order damping terms, complex lobe values and the correct preferred alias sign. It uses no external libraries. Finite tests do not validate claims involving all functions, frequencies or sampling steps; the generality follows only from the supplied proof.

The results are not independently audited. The assumptions exclude nonnormal generators and endpoints \(\alpha=0,1\), and bibliographic priority cannot be asserted absolutely.
