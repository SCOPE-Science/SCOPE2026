---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Read actual RESULT.md blob 02bc2cf2. For W_c=C\{c}, a voter with approval-size r contributes 1 or 1-1/r to SAV, and H_r or H_(r-1)=H_r-1/r to PAV. Therefore SAV(W_c)=number_of_voters-s(c), PAV(W_c)=sum_i H_|A_i|-s(c), with s(c)=sum_{i:c approved}1/|A_i|, so ALL weak rankings/ties/winner sets coincide for nonempty ballots and m>=2. Independently tested exact rational identities on randomized approval profiles for m=2 through 7 and exhaustive direct ballot formula argument for arbitrary finite m. This is correct but only one harmonic-number decrement; it does not imply equivalence for other committee sizes.

## originality

FAIL

Prior published reverse-sequential Thiele first-removal rule and SAV normalized support directly imply the one-vacancy identity; see explicit implication.

## value

FAIL

The one-vacancy score coincidence is a single direct harmonic-number decrement already inherent in the published general Thiele elimination definitions. The purported PAV tractable regime is immediate from only m candidate committees: evaluating every one is polynomial even without this identity. It is a routine instructional calculation without a nontrivial boundary mechanism, new invariant, classification, or scientifically consequential gain sufficient for an independent research claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
