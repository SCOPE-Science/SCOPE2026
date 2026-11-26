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

A leaf cannot enter state 1. If a core vertex were excited at an update t>=3, both neighbours must have entered 1 at t-1 using both of their own core neighbours. In particular the centre was 1 at t-2, hence refractory at t-1. The centre at an update-2 excitation cannot have started in 1, so each supporter at time 1 needs its exterior core and leaf in 1 initially and must itself start in 0. These constraints are sufficient even if the centre's leaf is excited: the centre has zero initial excited core neighbours. For n=3 modular wrap equates a required 0 to a required 1; for n=4 only the endpoints of the trigger coalesce, compatibly. The triangle example (0,1,1) gives time 3. No 1 initially is equivalent to extinction by 1. No new 1 at update 1 is equivalent to extinction by 2, since without it there can be no excitation at update 2. The first cyclic trace counts choices of each local leaf subject to the triple constraint, with indices anchored by labels, not divided by n. The second cyclic trace counts avoidance of the two patterns in the periodic extension; any compatible closed run has its state fixed by the last four letters after sufficiently many repeated reading steps, so weighted paths introduce no extra multiplicity even at n=3,4. The independent exact replay reconstructed both characteristic polynomials, obtained the four published histograms by direct enumeration at n=3..6, and evaluated transfer counts (not direct evolution) through n=12. Replay: python3 /workspace/branches/e3725a4b-aded-4e09-ba95-60a9513dcba8/independent_sunlet_check.py. Finally a five-site block at n>=5 has 54/9^5 chances to trigger, and disjoint blocks are independent; at n=3,4 the stated bound is 0. The finite enumeration tests the wrap and census but does not replace the proof for arbitrary length.

## originality

PASS

The threshold-two wheel/fan/forest analogues do not cover this family or its temporal census. The standard arbitrary-graph theorem has a different threshold. No independent source retrieved gives the two sunlet traces or a stronger result that yields them. Best-of-knowledge assessment only. Correct the contextual description of the open-ladder citation in future editing: the indexed result is a long-term rate census for ordinary cyclic and Greenberg–Hastings dynamics, not evidence of a threshold-two ladder extinction census. That attribution is not used by the proof or the positive originality comparison.

## value

PASS

The corona is a standard unicyclic test graph where leaves matter at the start but cannot relay. Resolving all hitting times, not just the maximum, exposes the transient amplification mechanism and explains why a rare finite local trigger makes the sharp final layer typical as the rim length grows. The two small root-sum formulas are usable without enumeration of initial configurations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
