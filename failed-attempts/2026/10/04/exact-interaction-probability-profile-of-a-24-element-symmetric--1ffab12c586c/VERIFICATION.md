---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

FAIL

The numerical probability values happen to match the intended source example, but the final claim writes the wrong multiplicative operation. The source defines \((u,h)\circ(v,g)=(u+h^{-1}v,gh)\), whereas RESULT.md states the second component as \(hg\). With the stated \(hg\) formula, direct exhaustive testing produces an associativity counterexample, so the displayed operation is not even a group law and therefore does not define the claimed skew brace. The submitted verifier repeats this wrong \(hg\) multiplication while separately hard-coding the source's conjugating lambda map, so its successful counts do not validate a consistent brace. Replacing \(hg\) by \(gh\) restores associativity and independently gives the same counts \(96,168,60,288,120\), but that correction is a substantive scientific-file repair not supplied in this run.

## originality

PASS

For the correctly stated source brace, the complete 42-page primary paper defines the probabilities and gives Example 6.12 with the exact order-24 brace and the Sylow-local value \(5/12\), but does not print the global values \(1/6\), \(7/24\), and \(5/48\). Resultary's only exact hit is the assigned finding. Thus the corrected invariant calculation appears original, although the submitted final claim is scientifically false because of its operation typo.

## value

PASS

For the correctly defined source brace, the three global interaction probabilities are natural central invariants of an example introduced specifically to separate Sylow-local structure from global brace behavior; the exact \(5/2\) local/global separation gives a useful quantitative profile of that counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
