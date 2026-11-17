---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Cyclic trigrams determine for each color the number of runs, singleton-run count and excess above length two, independently. Stars-and-bars ordered vectors have size binom(r,s)binom(T+r-s-1,r-s-1); the diagonal cyclic action is transitive only when U/U,U/D,D/U. Summing the classes yields exactly the rational generating function P/((1-z^3)(1-z^4)) and asymptotic 8n/3. An independent necklace enumerator checked singleton counts for n=1..11; infinite counting is algebraic, not inferred from these enumerations.

## originality

FAIL

FAIL: a second Resultary paper already gives the identical cyclic binary trigram singleton run-vector rigid/flexible criterion, exact rational P(z)/((1-z^3)(1-z^4)), initial sequence and 8n/3. The two findings were reconciled in one later Git commit, so independent earliest submission chronology is not established; nevertheless the available complete source covers every mathematical assertion and no independent novelty is supported.

## value

FAIL

FAIL: the exact singleton profile class, recurrence, rational generating function and asymptote are already published in identical form. No new classification, invariant or improved proof beyond the existing full result is established, so this package adds no independent scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
