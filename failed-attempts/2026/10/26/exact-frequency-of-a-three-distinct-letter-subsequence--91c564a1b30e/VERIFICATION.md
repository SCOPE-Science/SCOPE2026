---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a ternary word the count is the sum, over middle letters 1, of the product of the number of earlier 0s and later 2s. A total of two forces one positive contribution (1,2) or (2,1), or two (1,1) contributions. In the last case no 0 or 2 and no third contributing 1 can intervene. Locating the first earlier 0 and last later 2 separates the free binary prefix/suffix from the forced middle, giving the disjoint OGF contributions x^4/((1-2x)^2(1-x)^3) twice and x^4/((1-2x)^2(1-x)^2) once. The neutral-letter gaps, including both ends, give F_m(x)=F_3(x/(1-(m-3)x))/(1-(m-3)x), exactly the stated expression. Independently reproduced the full rational identity with symbolic m: run python3 /workspace/checks/subsequence_automaton.py (SymPy). It caps the two proper-prefix counts at 3, rejects full-count overflow and eliminates self-loops of the monotone state graph. This is an exact series comparison, not an extrapolation of the supplied finite table; the accepted series starts at n=4.

## originality

FAIL

A distinct indexed Resultary theorem gives exactly the whole arbitrary-alphabet result as a special case, and a second record gives the exact ternary case. This is demonstrable existing coverage, not proof that someone published the formula before the frozen record or that the frozen authors derived it from these records. Both matching entries have later date labels.

## value

FAIL

Exact frequencies of literal subsequences over nonbinary alphabets are a natural counting problem, but the frozen formula and all its parameters are already supplied by the distinct broader indexed theorem. As an independently useful exact addition to the indexed results it has no remaining scope; its short derivation is not a separate scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
