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

Independently checked the last-occurrence subtraction by fixing the output length L=i-t: the duplicate strings are exactly the new letter appended to a distinct length-(L-1) string from the prefix before its previous occurrence p. For the first symbol of run j the subtraction at t=2 is 1 if the preceding run is single and 0 otherwise. At t=3 it is respectively the one-deletion count j-3+a_{j-2} and 1. At the optional second symbol, the t=3 increment is the two-deletion count after the first symbol minus the two-deletion count before it, hence j-2. These facts give the displayed run recurrences. In the sum, a double in run h<=R-2 contributes through H_{j-1} for R-h steps and through the three local terms with combined coefficient 2h-7, so contributes 2R-7 irrespective of h; truncation at h=R-1,R gives the two indicated terminal corrections. This includes R=3 and the empty descendant. Fibonacci joins give one new 11 at even depth starting at depth four, and no 00 or 111; the terminal blocks 101 and 110 yield the stated flags. The limiting cubic term gives (2/phi^2)^3, while all other terms are quadratic or smaller. Read RESULT.md, VERIFICATION.md and verify.py; the supplied checks were inspected rather than run. Their literal deletion-set and earliest-occurrence automaton tests are finite corroboration, not used for the general proof.

## originality

PASS

The full run-statistic law with possible double runs and the ensuing all-depth Fibonacci count are the distinct claims. The alternating case is already an exact consequence of Sloane; both the basic recurrence and previously known deletion-sphere bounds or extrema are outside the originality claim.

## value

PASS

This counts source-specific synchronization ambiguity, not deletion positions, on a natural forbidden-factor language containing finite Fibonacci words. The source-independent contribution of every interior double run, with all order dependence concentrated at the terminal flags, is useful structural information beyond alternating extremality or a per-input computation. The exact depth formula and nontrivial normalized limit give concrete applications inside the language.

The dated certificate retains the supplied scientific assessment, sources and limitations.
