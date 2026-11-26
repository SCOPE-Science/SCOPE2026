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

The profile counts orientations with multiplicity on vertex coordinates, including isolates as sinks. Reversing the only edge at a leaf preserves acyclicity and pairs opposite signs at the singleton-leaf frequency. On a cycle, the sink transition is (incoming-forward, outgoing-backward) = (1,0), so the product trace of the stated two-state matrices counts all orientations with their signed weight. Subtract two for the constant edge words, which have no sinks. Factoring the rank-one unselected blocks J^g=2^(g-1)uu^T gives 2^(z-r) times the product of u^T M^ell u; these terms equal q_ell by the same second-order recurrence and initial pair (2,2). All selected uses tr(M^n)=q_n and none selected uses 2^n. I also checked the gap by a separate arithmetic proof. In the character expansion a nonempty prescribed sink subset U must be independent, which forces 2|U| distinct edges inward and leaves 2^(n-2|U|) orientations, all acyclic. Thus the signed sum is 2^n I(C_n[S];-1/2)-2. Each power of 2 in the expanded polynomial is 2^(n-|U|), divisible by four because |U|<=floor(n/2) and n>=3. Therefore every coefficient is 2 mod 4, and selecting an adjacent pair makes the independence polynomial evaluate to zero, attaining -2. The trivial frequency attains the mass 2^n-2, the absolute maximum by the triangle inequality. Independent component orientations give tensor products, with unit absolute multipliers for isolates and the empty product equal to one. This proves invertibility exactly without leaves and the exact magnitudes and condition numbers on that regime. `python3 /workspace/review_replay.py 5` reconstructed cycle histograms using rotating bit masks, checking all Walsh multipliers for the congruence and sharp extremes at n=3..14; the unrestricted conclusion follows from the proof, not the replay.

## originality

PASS

The sink-profile polynomial and multivariate cycle independence transfer are established, and a distinct same-day path result overlaps with the path obstruction. The surviving distinct claim is the exact all-frequency nonvanishing and sharp least absolute multiplier on acyclic cycle sink profiles, and its complete componentwise recovery classification at maximum degree two.

## value

PASS

The class combines paths, cycles and isolates and is structurally complete at maximum degree two. The exact distinction between a lost leaf frequency and uniform positive singular-value separation for all cycle frequencies determines when recovery is possible and how much errors can grow, independent of cycle size in the unnormalized lower bound. The arithmetic separation and its extremizer go beyond listing unsigned sink statistics or recomputing tabulated counts, although the result is elementary once the correct signed reduction is in hand.

The dated certificate retains the supplied scientific assessment, sources and limitations.
