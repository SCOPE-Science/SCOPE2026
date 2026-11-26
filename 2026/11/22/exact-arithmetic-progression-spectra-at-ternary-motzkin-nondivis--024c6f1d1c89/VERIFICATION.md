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

The cited congruence is correct, but the arXiv corollary number is not: the Motzkin statement is Deutsch–Sagan Corollary 4.8, not 4.9–4.10 (which concern Motzkin prefixes and Riordan numbers). With the verified congruence, the cutoff gives exactly E_r+2=(3T_r+{0,1,2}) minus {0,1}. At each new digit level, write q=3^r and L=(q+1)/2. The two cross-block triple configurations reduce to nonnegative integer solutions of a relation of the form v+2u+w=1, giving exactly four triples, two at each of L-1 and L. Any crossing quadruple must split 2+2 because L-1 is the minimum crossing gap and 2(L-1)>L for r≥2. The first term is at most one; the start at zero overshoots on the fourth term and the start at one gives the sole quadruple. It cannot extend, ruling out longer crossing progressions. Doubling within the two blocks, then subtracting the progressions starting at the two deleted points, gives the frozen per-step counts, including r=1 and the zero counts at the top four-term step. A seven-term progression would yield three terms at equal residue modulo three whose quotients form a nonconstant progression in the carry-free ternary 0/1 set, which is impossible. Sharpness is witnessed at 7–12. Independent modular recurrence and progression enumeration matched every profile and aggregate for r=1–6, lengths 3–7, and Motzkin residues through 1092. The uploaded checker was inspected but not run.

## originality

PASS

Pass the complete per-step progression spectra for this digit-set thickening with its exact boundary truncation. The ternary congruence and the progression-free unthickened digit set are known, and the length obstruction is an elementary consequence of that structure rather than an independent priority claim. No inspected source gives or mechanically specializes to the complete evaluated spectra.

## value

PASS

This goes beyond identifying a known digit set or noticing its easy upper length bound. The complete counts separate step-one runs from inter-block progressions, show exactly which sparse large differences occur at each scale, and quantify the cutoff effect. That is a reusable exact additive invariant of a natural nondivisibility sequence, not an arbitrary small numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
