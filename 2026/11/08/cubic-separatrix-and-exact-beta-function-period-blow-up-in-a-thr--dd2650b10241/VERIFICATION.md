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

# Reproduction and scope

The analytic proof is in `RESULT.md`. Execute `python verify.py` with NumPy and SciPy installed. The script uses the exact Hamiltonian \(H(x,y)=\sin x+\sin y-\sin(x+y)\), tests the trigonometric factorization and central energy, and evaluates the original-time period via a polar-area radial integral. It compares several small energy levels with the claimed \(2^{2/3}B(1/3,1/3)\) coefficient. It also checks the small-oval period \(4\pi/3\).

A successful execution reports `VERIFY_OK factor_identity=16 center_energy=1 period_levels=4 center_limit=1 beta_constant=1`. It does not exhaust energy values or prove the asymptotic; the uniformly dominated local Euler-field integral in `RESULT.md` supplies the infinite-domain argument. The numerical checker measures period in the unscaled ODE time, with no resampling or time change. Independent validation and definitive historical-priority assessment have not been performed.
