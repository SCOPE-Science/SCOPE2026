---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS. In the actual RESULT.md (Git blob 41d44a4d...), substituting the state equation into the quadratic auxiliary update gives r_{n+1}=r_n/[1+tau*a*a*phi_n^2/S_n^2]^{1/2}; positive root is unique and modified r^2-C decreases. For C=0 along nonzero iterates put t=a*tau, q=(1+2t)^(-1/2); summing all post-reversal increments gives phi_infty/phi0=(2q^2+3q-1)/(2q), so the first negative branch remains negative at every finite n iff t >= (11+3*sqrt(17))/4. This is NOT a global theorem on later crossings. For a=phi0=1,tau=100 and 0<C<=1/2, the first state is <-17/3, subsequent r contracts by >10 and total post-first displacement is <5/3, closing all-step phi_n<-4 and phi_infty<-4 rigorously. Independent Decimal finite iterates at C=0.0001,0.1,0.5, plus direct algebraic checks of the recurrence, corroborate only these analytic bounds. C=0 is singular exactly at phi=0 and is restricted accordingly; C>0 is nonsingular.

## originality

PASS

The generic frozen-state inconsistency of EXACTLY this positive square-law SAV-BE map, including positive C and a large-step explicit example, was already proved in the Nov 2 published record; no novelty is credited for that general warning. The bounded surviving distinct claim is the exact sharp t* for permanent first sign reversal of the explicitly solved zero-shift branch, together with a uniform entire positive-shift interval at one fixed timestep. The inspected stronger large-h result only guarantees freezing when h exceeds an unspecified parameter-dependent threshold and supplies no zero-shift first-branch classification. Targeted related searches did not reveal prior exact t*; best-of-knowledge, not a proof of historical priority.

## value

PASS

The sharp reversal-branch threshold is an exact structural boundary in the limiting scalar numerical dynamics of a named positivity-preserving scheme, identifying when a wrong-sign state never recrosses; the robust positive-offset witness makes the artifact genuinely occur in the non-singular intended scheme. This is a motivated numerical-stability counterexample rather than a textbook energy calculation. The already established broad frozen-state phenomenon is explicitly not valued as newly proved; mathematical relevance is confined to the quantitative branch cutoff and fixed-step offset interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
