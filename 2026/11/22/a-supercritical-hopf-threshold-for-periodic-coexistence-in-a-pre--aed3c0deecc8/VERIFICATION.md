---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The cited model's equations yield the stated reduction: reproduction and capture differences are both 1/2, and their population averages are 5/8+x and 1, respectively. For k=1/K the unique interior equilibrium is (3/8+k,1,1) whenever 0<k<5/8. At k=1/8 its characteristic polynomial is (lambda+1/8)(lambda^2+1); differentiating the moving-equilibrium polynomial at lambda=i gives d(lambda)/dk=(-32-4i)/65 and d Re(lambda)/dK=1/130. Independently from the centered polynomial, B(q,qbar)=0, B(q,q)=(0,-2i,2i), and C(q,q,qbar)=(1/64,0,0). To replay the nonzero resolvent, write A=(2iI-J)^(-1)B(q,q); A_V=(996+512i)/771, A_X=i A_V/16, A_U=2i(A_V-1). Contracting B(qbar,A)+C(q,q,qbar) with the stated normalized left row gives G21=-369/33410-521107i/801840 and l1=-369/66820 in that normalization. The simple transverse pair, negative third eigenvalue and negative l1 prove the local attracting branch on K>8. Its vanishing amplitude at an interior point ensures positivity. No global cycle uniqueness or persistence follows. VERIFICATION.md and verify_hopf.py were inspected but the bundled script was not run.

## originality

PASS

Pass only the exact analytic witness with the specified payoff matrices and beta=1, not the existence of a positive-payoff supercritical Hopf in this model. An earlier published record already proves that existence for the model's numerical Scenario 8. It should be cited in describing the contribution. Its local result for different payoffs and mortality neither proves the present coefficient nor provides a general theorem from which this witness follows mechanically.

## value

PASS

Constant averaged capture with differing individual capture payoffs gives a motivated simplification: it leaves frequency–predator feedback while fixing total prey and predator values at coexistence. The exact unit-frequency threshold and signed normal-form data then give a reproducible analytic benchmark for separating that feedback from more general capture dependence and for checking continuation or normal-form computations. This is not valuable merely for replacing one numerical threshold with a different number, and does not purport to prove the original numerical example, which already has its own proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
