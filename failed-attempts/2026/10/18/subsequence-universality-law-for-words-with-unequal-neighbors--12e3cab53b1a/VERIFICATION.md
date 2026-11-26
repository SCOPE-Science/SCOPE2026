---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The greedy complete-alphabet arches characterize the index: choose one letter from each for the lower bound, and use each arch's first completion letter followed by a missing suffix letter for an unmatched pattern. At seen count j there are j-1 repeat and q-j new choices. A first arch begins with q choices, a subsequent arch q-1; grouping each run of old letters gives 1/(1-(j-1)t), and multiplying the new-letter choices gives A_0,A,B_0,B as in RESULT.md. Summing the unique decompositions B_0+u A_0 B/(1-u A) yields the boxed formula, including the empty and binary cases. In the uniform Markov word the geometric waits at each j have parameter (q-j)/(q-1) independent of the identities seen; conditional lengths therefore have the same distribution for every preceding letter, including the initial arch, with independence at stopping times. Summing geometric moments gives mu and v. For q>=3 arch lengths q and q+1 both have positive probability and the length PGF f(z)=A(z/(q-1)) is analytic beyond |z|=1; f(z)=1 only at z=1 on or within that circle. The renewal count PGF (1-f)/((1-z)(1-u f)) gives mean and factorial-second-moment PGFs f/((1-z)(1-f)) and 2 f²/((1-z)(1-f)²). With x=1-z and c=(v+mu²-mu)/2, f=1-mu x+c x²+O(x³); their pole expansions give mean n/mu+O(1) and variance n v/mu³+O(1). Inverting the iid sum CLT gives the displayed renewal CLT. Verification files were inspected but not run; a separate direct subsequence test agreed for ternary and binary through n=8. Replay: RESULT.md arch/count proof and the renewal PGF calculation here; finite tests do not prove the theorem.

## originality

FAIL

A distinct indexed Resultary record, 4cd9e1de10a7, covers the exact same all-q rational distribution and the same fixed-q renewal law, binary boundary and constants. The finite-n O(1) moment remainders follow directly from the identical rational arch-length PGF. The compared record is later-dated; this decision establishes present statement-level coverage, not priority, copying, or an earlier publication. No distinct nonmechanical remainder warrants a repaired finding.

## value

PASS

The all-size rational law and regeneration for a natural constrained language are mathematically useful: the collapse to the number of distinct letters simultaneously gives an exact combinatorial law and explicit asymptotic uncertainty. This is not a tiny-table computation. Its mathematical usefulness does not supply a distinct contribution relative to the matching indexed record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
