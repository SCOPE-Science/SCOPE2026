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

Frobenius factorization gives the stated carry transitions in F_3; the parity-conditioned starts encode twice the floor of 3n/2, and the parity filter counts each ternary word exactly once, including zero. Integral transitions stay in the five carries −2 through 2. The independently rebuilt graphs have 8 and 10 states and the stated counts satisfy the candidate recurrences through L=25. After multiplying the candidate annihilators by the combined graph's degree-18 characteristic polynomial, zero initial differences of lengths 20 and 21 suffice for equality at all levels. A direct algebraic check collapses the two sign partners in the tables: let h=1 for support, h=−1 for signed count, and let A,C,D be the continuation series at even-branch states 0,2,1. They satisfy A=1+z(A+C+D), C=1+z(2A+hD), D=hz(A+D). The odd start contributes zA/(1−hz), by its two transient states. Eliminating gives total (1+z)(1+(1−h)z)/(1−(1+h)z−2z²+(2h−1)z³), which is exactly the pair of claimed series. The bias recurrence is positive and its positive root dominates because the other two roots are conjugate with modulus √(3/ρ)<ρ; the numerator is positive at the dominant pole. Direct polynomial multiplication for all n<729 independently agreed on every full block through L=6. Replay: direct_polymul_check.py and independent_transfer_check.py in /workspace/branches/810b7590-de31-41ce-8264-3d2c524b9080. Uploaded code was not executed. No assertion is made for arbitrary cutoffs or higher prime powers.

## originality

PASS

The supported new content is the evaluated all-level ternary-block census for the central quadrinomial sequence, in particular the signed secondary term alongside the Fibonacci support. The base sequence and generic congruence-automaton construction are known. None of the examined exact matches for the underlying sequence, alternate indexing, special-index congruences, or general automata provides the evaluated paired counts. This bounded assessment does not establish historical priority.

## value

PASS

Complete ternary blocks are the natural padded-digit sample space, and the central coefficient is a standard object. The count determines all three residues at every depth and separates the nonzero-support rate from the strictly smaller but positive bias rate, a feature genuinely beyond a nonvanishing census or ordinary sequence table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
