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

# Verification

The proof's unrestricted step is the regular-sequence Koszul argument followed by polynomial divisibility using coprime maximal minors. It establishes \(AR(F)_r=S_{r-3a+3}\Delta\) simultaneously for all \(r\le(m-2)a\). Generic first-jet incidence shows that the assumed gcd and transversality conditions hold on a nonempty Zariski-open set and that its singular support is exactly the finite base complete intersection.

Run `python3 check.py` with SymPy installed. The script recomputes the four signed minors in the explicit quadratic example, checks their gcd and both Jacobian annihilation identities, verifies a transverse eight-point base via Gröbner bases, and performs exact modular elimination to determine the seven low-degree kernel dimensions. Expected dimensions: `0 0 0 1 4 10 20`. The modular calculation is finite computational support only. It neither certifies the general theorem nor addresses any omitted degrees or nongeneric configurations.

The independent mathematical audit remains unperformed.
