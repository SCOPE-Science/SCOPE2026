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

For the corrected finding, use the increment coordinates u, in which the input seminorm is the l1 norm. Put F(a,b)=a^2/(a-b). The adjacent output differences are u_j+F(u_{j+1},u_{j+2})-F(u_j,u_{j+1}). Their Jacobian has rows with three successive entries 1-H(t_j), H(t_{j+1})-U(t_j), U(t_{j+1}), where t_j=u_{j+1}/u_j, H(t)=(1-2t)/(1-t)^2 and U(t)=1/(1-t)^2. The signs are +,-,+, so each column sum of absolute values is maximized in the limit with all relevant ratios at q. The largest sums for n=4,5,>=6 are respectively max(U,U-H), 2U-H, and 2U+1-2H (U,H at q); n=3 has no adjacent output differences. Convexity of the linear increment inequalities bounds finite pairs by the integrated Jacobian, also with weak ratio caps and positive increments. A geometric increment vector with a common ratio t<q is interior; perturbing one maximizing increment and then taking t up to q proves sharpness. The nonzero leading numerators as q tends to one are 2,3,4 in the three positive cases. The separately authored exact-rational checker passed 5,500 derivative-step, 420 finite two-input and 16 near-sharp checks; these corroborate the proof, not replace it.

## originality

PASS

The supported distinction is the sharp two-input adjacent-variation operator modulus for the full sliding transform, with the finite-length boundary regimes. Neither the geometric-error kernel nor scalar contraction/noise results in the inspected material give that modulus. The repair removes a boundary misstatement and makes no new priority claim.

## value

PASS

Exact geometric-error removal does not quantify perturbation amplification. The corrected theorem gives a sharp deterministic worst-case bound that is independent of increment size, detects when truncation at the ends changes the worst perturbation, and distinguishes the zero singleton case from the quadratic blowup of all nonzero moduli. These features inform use of the sliding transform on short traces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
