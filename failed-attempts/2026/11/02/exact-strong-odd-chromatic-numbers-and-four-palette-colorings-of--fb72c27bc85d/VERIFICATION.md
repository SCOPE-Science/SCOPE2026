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

A cubic vertex permits exactly a monochromatic or a rainbow neighborhood. For four named colors, a proper pair of columns has 12×7 states. Each coordinate of the successor is forced: use the rung partner's color when it equals the preceding rim neighbor, and otherwise use the fourth color. The two proposed entries differ, and the same rule in reverse is the inverse. With current column (a,b), the preceding column has either both coordinates swapped, neither swapped, or exactly one swapped. Applying the rule gives respectively periods 2, 4, and 6; the one-swap types occur on the same six-cycles. Their state counts 12, 24, and 48 give the labelled trace formula, including n=3 and simultaneous divisibility by 4 and 6. The three explicit blocks satisfy the neighbor rule and share first and last columns, so each seam reproduces a validated cyclic seam, yielding all odd n≥5. Even prisms have a proper bipartite coloring, valid because degree is three. In the triangular prism the two same-rim neighbors of any vertex are adjacent and hence differ, so each neighborhood must be rainbow; because its square is K6, all six colors are needed. This makes explicit the step implicit in the secondary justification at RESULT.md line 67. The independent replay `python3 /workspace/branches/frozen_replay.py 3` gave counts [0,36,0,60] for n=3,4,5,6; this finite check is not the general proof.

## originality

FAIL

A distinct earlier Resultary record, 697eedb2d5a5, states the same chromatic-number classification, the same four-named-color count under the same labelling conventions, and the same local cycle inventory; it additionally treats the five-palette count. The frozen result does not establish a separate new mathematical claim. The triangular boundary is separately a published corollary. This is demonstrated coverage, not failure to retrieve a source.

## value

FAIL

The exact prism census is a natural invariant, but this frozen finding recomputes an already recorded all-n closed form and orbit inventory with the same assumptions. The odd chromatic classification is also directly recorded. No additional exact invariant or new boundary survives this coverage; this is not a judgment against the value of the earlier theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
