---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The steady-state balances force c_i=J/k_i, e_a=E_a-s_aJ and x_i=((k_i^-+k_i)/(k_i^+k_i))J/(E_a-s_aJ). Their conservation gives F=alpha J+sum b_a J/(E_a-s_a J)-T=0 with strictly positive derivative and a unique interior root. Implicit differentiation gives J_Ea>0 and the exact cross-curvature bracket 2/J+2s_a/u_a+2s_b/u_b-K/H. K/H is a strict positive-weight average of 0 and 2s_c/u_c, proving all q=2 brackets positive. For the three-pool rational example, exact symbolic simplification reproduces B=-2P/[j(j-3)(10j-11)Q], Q>0, and a one-sign-change transformed sextic, hence one positive root; exact rational checks recover cross derivative +71805312/33856161185 at j=1/2 and -4675/1203052 at j=1. No extrapolated stability claim is needed: distinct-enzyme global convergence is credited to the primary source.

## originality

PASS

The q=2 all-parameter strict mixed-current complementarity and q=3 sharp counterexample with exactly one load sign reversal concern additive derivatives in conserved enzyme totals of closed mass-action HMM cycles. Inspected predecessor gives equilibria and dynamics but not these second derivatives. Earlier epistasis and enzyme-allocation studies use different kinetics, control quantities or constraints. This is best-of-knowledge, subject to older second-order metabolic-control literature.

## value

PASS

The number of enzyme pools is an intrinsic discrete architectural complexity measure for a conserved biochemical cycle; q=2 universal positive complementarity versus an explicit q=3 globally stable unique sign reversal is a sharp, motivated structural boundary. The exact algebraic threshold and fixed-total derivative provide reusable diagnostics beyond routine implicit differentiation. This is not a generic renaming or an arbitrary small numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
