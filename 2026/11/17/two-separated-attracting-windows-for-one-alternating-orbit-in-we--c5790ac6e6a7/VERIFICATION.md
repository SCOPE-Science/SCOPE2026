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

PASS. On the colour-constant invariant two-shore subspace, biregularity makes the phase gap δ alternate between π+t and π-t exactly when h(r+s)q(t)=2t, q(t)=(4/5)sin(t)(1+cos^2 t). The identity q(t)>0 and q(t)-t q′(t)>0 for 0<t<π makes K(t)=2t/q(t) strictly increasing from 5/4 to infinity, so the same primitive symmetric 2-cycle exists uniquely above onset. The positive weighted connected bipartite graph Laplacian has largest simple eigenvalue Λ=r+s via irreducible signless Laplacian/Perron-Frobenius. The one-step Jacobian at both points is J=I-h q′(t)L, and the two-step multipliers are (1-h q′(t)λ_j)^2; common phase λ=0 is neutral and removed. For all other eigenvalues 0<λ_j<=Λ, |1-hq′λ_j|<1 iff 0<h q′<2/Λ. Since q′=(4/5)cos(t)(3cos²t-1), this holds for 0<t<acos(1/sqrt3) and π/2<t<π-acos(1/sqrt3). Else each λ>0 gives >1, yielding the exact two disjoint attracting windows and intervening repelling windows. All four hΛ cutoffs match the formula and numerical diagnostics; boundaries deliberately have no nonlinear attracting verdict.

## originality

PASS

PASS best-of-knowledge. Published κ-dependent first-plus-third harmonic theorem treats only the *local* flip near onset; pure-sine biregular and weighted bipartite results treat κ=0 and have a single attracting window, so neither establishes global continuation of this κ=1/5 orbit through two disjoint stable ranges. Broader generic odd-interaction network theory covers small steps but not these exact four thresholds. Reentrance remains a plausible historical-priority risk in older multiharmonic map literature.

## value

PASS

PASS. A physically motivated third-harmonic perturbation creates genuine global reentrant local stability of one explicitly continued 2-cycle, uniform over every connected positively weighted biregular bipartite graph. Four sharp boundaries, full transverse spectral verification and graph universality give substantive dynamical structure beyond the local period-doubling theorem or one numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
