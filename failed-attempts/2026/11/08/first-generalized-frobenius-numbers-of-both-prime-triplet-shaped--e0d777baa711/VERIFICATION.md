---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The submitted residue-threshold argument correctly parametrizes n=au+2t for each of two offset patterns and bounds all residues above a two-representation threshold M while exhibiting a single-representation predecessor M-a. Independent saturated coin-count dynamic programming for k=1..15 (30 triples) reproduces the two polynomials and all terminal tails. The earlier October 18 complete theorem separately supplies a full unbounded proof of these exact formulas and also k=0 boundary cases; its correctness is not merely a verifier exit code.

## originality

FAIL

The entire submitted two-polynomial result is already published verbatim for the same nonnegative-coefficient vector counting convention in an October 18, 2026 theorem. The stronger prior theorem additionally handles k=0.

## value

FAIL

The p=1 semigroup invariants are intrinsically motivated but their complete values and proofs were already published for both exact templates. This submission supplies a rederivation, not an unknown mathematical fact or materially new structural result; value as a distinct new scientific contribution therefore fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
