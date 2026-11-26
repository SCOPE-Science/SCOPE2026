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

PASS

The polynomial is even-valued and is an isometry from the even inputs onto the even targets; each even target gets one such input. For the four odd classes 1,7,5,3 modulo eight, the factorizations at -2 and 2 give the square normal forms in RESULT.md lines 73–85. The root of 1+8t/b lying in 1+4Z_2 exists uniquely because ( (1+4a)^2-1 )/8=a+2a^2 is an isometric permutation; root differences gain two valuations. Thus the first two square coordinates are isometric permutations, and the last two, after factoring a dilation from their differences, are bijections onto all odds. The first two contribute eight lifts per square root modulo 2^(k-6); in the last two four odd square roots modulo 2^(k-4) each give four lifts, on 110 and 18 modulo 128. Reducing those same branches at k=3,4,5,6 and inspecting k=1,2 gives the stated table. For the square count S_m, zero has 2^floor(m/2) roots and a nonzero target of valuation 2s is governed by 2^s times the unit-root count at precision d=m-2s. For odd m>=3 the unique maximizing target has d=3 and unit 1 modulo eight; for even m>=4 the maximizers are zero, the one at d=2, and the two at d=4. The constant branches dominate at k=7, tie at k=8, and are strictly below the maximum at k>=9, giving exactly the reported extrema. An independent direct enumerator matched all 8190 target counts and the extrema at k=1 through 12; the uploaded checker was read, not run. Replay: /workspace/branches/3374c2ce-90c9-4a2b-982f-f399c11ba37f/direct_fiber_crosscheck.py and direct-k12.log in that directory. Mathematical proof, not finite replay, supplies the unbounded result.

## originality

FAIL

The indexed trace-polynomial record 7802afd6e155 provides the same complete finite law. The lower precisions descend by reduction and the maximum and maximizer census follow by direct optimization of its shell multiplicity. These are not independently distinct arithmetic content merely because stated explicitly here. The conclusion concerns demonstrable catalogue coverage, not which same-day record came first. The inaccessible 1991 theorem text is a separate historical risk, not the reason for failure.

## value

FAIL

The whole finite fiber classification for a natural nonpermuting cubic is mathematically useful, but it is already supplied by the matching shell law. The only extra explicit finite invariants are the maximum and its census, obtained by a routine two-shell comparison in that law, and the levels below four, obtained by reduction. There is no separate unknown precise fact or structural gain in the extra assertions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
