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

The proof concerns a symmetric one-dimensional passive-scalar slab with a midplane sheet source of strength per unit horizontal area, not a three-dimensional point emitter. On either half the hyperbolic profile obeys the homogeneous ODE, with the Robin slope at the boundary and inward-coordinate slope Q/(2D) at the midplane, giving the correct source jump. Uniqueness follows from the homogeneous energy identity with positive bulk and boundary terms. The matched bulk value is Q/[2Dk(a+t)] in the paper's variables. Its ratio comparison uses a strictly increasing half-profile F with F(0)=1; (a+t)(B-1)=sinh(a)-a+t(cosh(a)-1)>0 and (a+t)(F(L/2)-B)=a cosh(a)-sinh(a)+t(a+t)sinh(a)>0. Hence there is exactly one crossing per half; the quadratic in exp(kz) is negative at 1 and increases through its larger root above 1, which is the displayed root. The exact mean sign follows independently by subtracting the two steady balances: rL times the mean difference equals 2Dkappa times the uniform value minus the wall value, strictly positive. The stated explicit mean follows by integrating the profile. For the switch-on claim in the proof, the passive Robin semigroup is sub-Markovian with the bulk factor exp(-rT), so the time integrals equal their steady values times T up to bounded remainders. Strict ordering is for each fixed height off the crossings, common positive breathing and a strictly increasing response, not a uniform exposure time or a claim at the crossings. The supplied finite checker was inspected, not executed.

## originality

PASS

The models and the possibility of spatial sign reversals are not new. The inspected precedents do not supply the exact two-level crossing classification and simultaneously strict mean bias for every positive parameter in the stated matched symmetric slab.

## value

PASS

The model pair is motivated by whether replacing boundary losses with a matched volume loss preserves concentration ordering. The exact all-parameter result gives a concrete counterexample to a one-sided approximation: the model underestimates the mean while overestimating near both boundaries, with exactly determined sign regions. The simultaneous signs and exact count add usable information beyond the standard Green function or a numerical sign-reversal example. The value is limited to this passive, symmetric idealization, not a prediction for real rooms or a validation of an empirical calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
