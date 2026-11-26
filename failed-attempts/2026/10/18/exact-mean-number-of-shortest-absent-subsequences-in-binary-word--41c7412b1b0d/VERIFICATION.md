---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

With the fixed binary alphabet, the complete arches host any target of length K, one bit per arch. The sequence of arch-final letters followed by a letter missing from the remainder greedily matches the arch ends and then fails, proving that the shortest absent length is K+1, including empty and unary inputs. Conditional on the source, an independent fair target fails at that length with probability s(w)/2^(K+1). The three states track whether an arch is fresh and whether its pending bit equals its first seen bit; the only decrement of matched-prefix surplus K subtracted from J is a return from M to F that completes an arch without matching. Every entrance to or continuation in M first raises the surplus, so no positive increment survives in a zero-surplus terminal path except the immediately cancelled F-to-M-to-F excursion. The four resulting weighted edges yield f=1+zg/2+z²f/4 and g=1+zg/2+zf, and the totals have OGF 2f(2z). The three roots lie in (-1.482,-1.481), (0.311,0.312), (2.170,2.171), certified by rational endpoint signs for the cubic. The dominant residue is -2/(z0 D'(z0)) for z0=1/rho, yielding the stated C and divided-by-2 remainder bound. Independent finite subsequence sets reproduced all totals through n=11; formal expansion reproduced all sixteen listed totals. This is not an assertion that a typical source has exponentially many such targets.

## originality

FAIL

The exact scientific claim, not merely its coefficient list, is subsumed by a distinct indexed Resultary finding, 729a1bce797c. That finding counts the same shortest absent words with the same fixed ambient alphabet and sums over the same source words, adding the universality index as a marker. Specializing that marker to 1 gives the frozen total and all its mean, recurrence and pole consequences. This is mathematical coverage in the available catalogue. The stronger entry carries a later catalogue path date, so this decision is not a claim that it preceded the frozen work or that either record derived from the other. A087955 supplies the numerical sequence but does not by itself supply the subsequence interpretation.

## value

FAIL

Identifying an exact expected number of shortest missing scattered patterns for a fair binary source is mathematically meaningful, not just an integer-sequence look-up. As a separate finding under the available coverage, however, every stated exact statistic is a direct specialization of the same family's indexed refined count. The two-state proof gives a useful explanation but the frozen record does not establish a distinct transferable theorem or a new invariant beyond that covered specialization. No surviving independent finding is established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
