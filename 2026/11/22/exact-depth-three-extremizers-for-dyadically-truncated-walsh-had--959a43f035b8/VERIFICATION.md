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

The Finding specifies Paley column order with the Sylvester row sequence: the raw Sylvester binary column indices are bit-reversed for these displayed labels. With row r, column j, the unscaled entry is (−1)^popcount(r & reverse3(j)). Summing this product for two columns over 2^k prefix rows gives 2^k if their low k character bits match and zero otherwise, which is the stated consecutive-block condition in Paley labels. Bare Sylvester columns without the Paley reorder would relabel the listed optimizers. An independent exact checker computed these pairwise overlaps directly from signs, enumerated all 4^8 length assignments, and used rational symmetric Schur-complement pivots to test 68I−5H for strict positive definiteness. It found exactly the eight stated XOR vectors outside the bound; all other 65528 have squared norm strictly less than 17/10. Newton identities on exact traces gave t^4(t−4)(t^3−16t²+32t−16) for each exception. The exact signs q(68/5)=−3088/125 and q(14)=40 put a root above the separation, hence all exceptions have the common larger squared norm; t=8ζ transforms the top factor into the claimed cubic. Replay: python3 /workspace/branches/b602047d-6d27-4349-895a-5f6e56a17799/audit_record5.py (no --limit); full run in the adjacent full.log, with the eight vectors and all assertions checked. Uploaded verify.py inspected, not executed. The last displayed digit of the supplementary squared-norm approximation is off by about 1.1×10^−15 (the largest root begins 1.719840461515739140); the exact cubic, gap and correctly approximated norm are unaffected. This is exhaustive at size eight only.

## originality

PASS

The standard complete branch, its Walsh-character symmetry orbit, Gram rule, and its spectral computation by a known compression are not new. The verified distinct content is exclusion of every other length vector, with an exact uniform strict cutoff that establishes complete equality classification at depth three. The checked broader branching comparison in Lakey is conjectural; Hogan–Lakey explicitly defer all-truncation maximality to future work; the closest distinct Resultary record is for the standard compression only.

## value

PASS

This is a motivated finite benchmark of the published single-branch maximal-norm problem, not just a recomputation of its already motivated candidate polynomial. Quantifying every allowed column choice excludes alternative maximizing branch patterns and supplies strict quantitative separation, both facts a researcher testing a general branching comparison can use. The exhaustive result makes no claim about higher levels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
