---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The actual D+ piecewise-affine vertex strings generate 2(j+2)+1 self-block branches and 2(j+2) adjacent-block branches, giving the finite multigraph M_K with endpoint escapes excluded. Expanding branches ensure that the survivor’s finite edge shift has entropy log rho; multiple endpoint codings contribute no entropy. Symmetrization produces Jacobi d_j=2j+5 and b_j=2sqrt((j+2)(j+3)), so the continuant P_{j+1}=(z-2j-5)P_j-4(j+1)(j+2)P_{j-1}. Identity 6K-<v,Jv>=sum b_j (v_{j+1}-v_j)^2+sum (6K-V_j)v_j² localizes eigenvectors on K^(1/3) terminal sites. The rigorous limsup via Dirichlet test functions and liminf via energy-tightness, compactness and lower semicontinuity identify -2u+6t u with u(0)=0. Airy zero a1 gives constant (2·6²)^(1/3). Directly verified finite Jacobi/Perron identity K=1..18 and rho(M1)=11; those finite checks do not prove the asymptotic.

## originality

PASS

Original source Proposition 5.2 constructs the explicit mixing infinite-entropy map but does not compute topological entropy of its initial K+1 block survivors or Airy correction. Relevant previously published finite-core Perron result concerns a different four-adically branching map with O(1) edge displacement, not the 6K−const·K^(1/3) regime. A periodic weighted-shift Airy theorem concerns an infinite geometrically weighted shift, not this increasing-coefficient finite Jacobi/interval survivor. Generic extreme Jacobi-zero literature is a nontrivial potential implication risk and is not claimed absent.

## value

PASS

The finite-core entropy of a specific published infinite-entropy dynamical system is a natural invariant measuring divergence under bounded-orbit restriction. Exact recurrence and sharp Airy boundary layer quantify the rate where qualitative infinite-entropy conclusions do not; the K^(1/3) correction requires nontrivial variational localization rather than a routine finite cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
