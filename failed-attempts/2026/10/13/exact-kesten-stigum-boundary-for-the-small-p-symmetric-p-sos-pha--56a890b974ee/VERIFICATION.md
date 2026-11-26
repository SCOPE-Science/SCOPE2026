---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The proposed boundary is false for the stated source model. Jahnel–Rozikov's Hamiltonian Eq. (1.1) has |spin difference|^p, so the endpoint weight is A=theta^(2^p), not theta^(2p). With p=1/10 the actual physical cubic is theta*y^3-y^2+(A+1)y-2*theta=0, and the corresponding nontrivial eigenvalues are (1-A)/(A+1+theta*y^2) and (A+1-2*theta^2)y^2/[(A+1+theta*y^2)(y^2+2*theta)]. At theta=8, rigorously 8<A<16, since 1<2^(1/10)<4/3. The cubic is strictly increasing in y, negative at y=3/4 (less than -7/16), and positive at y=1, so 3/4<y<1. In turn |lambda_odd|<15/(17+8*(3/4)^2)=30/43 and |lambda_even|<119/281, using the even denominator divided by y^2. Both bounds are less than 1/sqrt(2). Thus theta=8 is above the proposed 6.881894… threshold but fails the actual KS test. An independently written exact calculation, /workspace/independent_checks/check_ks.py, verified the rational counterexample bounds, reproduced the frozen resultant and root for the modified endpoint weight theta^(1/5), and verified root uniqueness there by a Descartes shift. The frozen script was inspected, not run; it certifies that alternative algebra, not the p-SOS source claim. Independent numerical evaluation of the actual equations reproduces about 1523.40549, but is not a new exact global certificate.

## originality

FAIL

The intended contribution is an exact correction of a prior numerical boundary on the same model and branch. The supposed discrepancy is due to changing the interaction, not a correction. The cited primary paper already reports the approximate crossing for the actual model. Novel exact classification on that model was not established; this is not a claim that the different-interaction polynomial itself is previously known.

## value

FAIL

An exact threshold on the real p=1/10 branch would be motivated, but none is supplied. The surviving exact elimination only concerns a changed endpoint weight selected by misreading an exponent, for which there is no independent model motivation or demonstrated need. The numerical reproduction of the real source threshold is not a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
