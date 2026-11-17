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

Reconstructed seven nonabsorbing-state Markov first-step linear equations. The reported rational formula (T_center-T_leaf)=N(c,t)/D(c,t) has positive denominator for c,t>0. Inspected symbolic checker rebuilds the 7-state generator and computes exact rational inverse, then verifies polynomial numerator and coefficient root isolation rather than relying only on a saved log. Each coefficient A_j(t) has one positive threshold, strictly ordered from theta0=1 to theta7=6; Descartes signs in c give a single positive crossover for 1<t<6, with opposite uniform signs outside. Two-state generator gives a difference with c-independent sign, proving minimality. Independent rational inversions at t=2 gave T_center-T_leaf=-38243/145208 for c=1 and +10721/179952 for c=3. Finite samples are only corroboration.

## originality

PASS

Best-of-knowledge originality survives statement/implication comparison: The older all-discount center-protection theorem assumes uniform pre-treatment hazards with one common distinguished hazard q and covers the homogeneous t=1 slice. This finding varies baseline center t and changes that center hazard to t/2 versus a leaf to 1/2. The named reductions and remaining inaccessible plausible sources are recorded as residual risks, not treated as proof of originality.

## value

PASS

The competing interventions have a natural fixed-cost comparison and mean time to global extinction is a standard persistence invariant. The complete hazard-ratio 1/6 phase diagram and unique colonization crossover are mathematically useful extensions beyond the known homogeneous-patch result; the finite three-habitat boundary is motivated, not an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
