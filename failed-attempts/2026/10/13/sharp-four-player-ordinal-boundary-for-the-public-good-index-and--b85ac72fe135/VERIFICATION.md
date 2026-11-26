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

FAIL

The main proper-game classification checks out. An independent exact truth-table replay using veto and dual least-core certificates (/workspace/branches/public-good-nucleolus-census.py) confirmed proper counts 1,3,11,80 and orbit counts 1,2,5,14, divergences 0,0,0,18 with the stated two vectors and weighted representatives, and null-free divergence 6/50. The frozen finding's unrestricted comparison (RESULT.md lines 90–100) does not hold under standard imputations x_i≥v({i}): the winning singleton in {A,BC} forces ν=(1,0,0), not (1/2,1/4,1/4). Four of the 18 normalized three-player games have at least two winning singletons and hence no imputation at all. The verifier instead imposes only x_i≥0 (lines 127–130) and evaluates all 18 (lines 275–285). Independently, the unrestricted domain with nonempty imputations has 14 games; exactly the three relabelings of {A,BC} diverge. The numerical vector in the frozen finding is consistent with the alternative simplex convention used by Elkind–Pasechnik, but the original does not state that convention or distinguish it from ordinary individual rationality. The proper part is invariant under this distinction: a winning singleton there implies dictatorship, and otherwise the singleton lower bounds are zero. Frozen scripts were read, not run.

## originality

FAIL

The exact proper-game boundary is a mechanical consequence of a previously available full canonical minimal-winner/nucleolus table through four players, even though the associated article compares a different index. I read the table, not just that article's finding, and recalculated Public Good rankings by counting set incidences in every row. The only differences are the two reported families, yielding the same 12+6 split. Neither correction of the nonproper imputation nor re-verification supplies a distinct valuable remainder.

## value

FAIL

The natural comparison is influence via minimal winning participation versus lexicographic stability. However, for the stated parameter range the entire proper classification is obtainable by direct column counts on a complete existing table, and the feasible improper contrast is forced by one individual-rationality inequality. A repeat census and a corrected convention note do not establish a distinct useful mathematical result here. No repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
