---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS — Every labelled vertex belongs forever to one of six cohorts determined by initial state and shore. Because activation thresholds are 1 or 2, each cohort multiplicity may be capped at 2 without changing any future excitation test; absent cohorts remain absent, so the deterministic six-cohort recurrence exhausts the trajectories of *all* m,n (not just bounded sizes). A separate implementation of all 3^6=729 capped signatures gave the complete first-entry/least-period table exactly: t0 (p1=9,p3=8,p4=8); t1 (p1=72,p4=32); t2 (p1=234,p4=56); t3 (p1=178,p4=24); t4 (p1=68,p4=8); t5 (p1=32); no other classes. All nonzero t5 signatures require >=3 left and >=2 right, and (2,0,1;0,1,1) realizes the bound at all such sizes. Primitive 3 profiles need all left three color counts >=2 and all right colors >=1, giving A_m(3^n−3·2^n+3), while primitive 4 profiles give 2 B_m(2^n−2). EGF factors 1,z,e^z−1−z count every label allocation, establishing the full all-size N_{t,p}(m,n) without extrapolating a finite-size sample. K_{6,3} counts 540 and 600; endpoint m,n>=1, mixed shore thresholds and synchronous updates are essential.

## originality

PASS

PASS best of knowledge — The 1991/2018 general excitable cellular automaton literature gives broad theory for lattice graphs or common threshold one, not this exact mixed threshold (1,2) biclique census. A published threshold-two biclique result has a superficially similar six-cohort finite method, but its **different dynamical transition** needs sizes >=6 on both shores for period3 and >=4 on both for period4; the mixed case shifts onsets to (6,3) and (4,2) and changes every temporal class. No conjugacy or parameter substitution preserves these orbit counts. Related one-edge-deleted and threshold-coloring results are different systems. Unindexed heterogeneous-threshold finite graph literature remains a priority risk; identical computational technique alone does not negate the new exact all-size data.

## value

PASS

PASS — Shore-dependent excitation thresholds are a natural heterogeneity in excitable networks. The sharp 5-step global memory horizon, exact two distinct wave onsets, and full labelled transient statistics quantify a meaningful loss of shore symmetry relative to homogeneous dynamics. Finite state space is used as a *complete* six-cohort quotient for arbitrary sizes, not a tiny unmotivated enumeration. Unlike a trivial threshold substitution, onset asymmetry yields a structural contrast future work can use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
