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

Audited the proof at the sharp boundary n=5 as well as for n>5. For a nonempty initially white W, a leak blocks all entry to W if it is the only vertex outside W with exactly one neighbor in W (or if there is no such vertex). The displayed singleton and diagonal traps have exactly the specified unique possible entrant; the opposite-end argument applies by reflection. Disjoint two-column windows consequently need two seeds apiece. If one pair is the inner rung, the other inner rung allows no initial force; an opposite horizontal pair can only make its corner-rung force before stopping when that target is leaked; an opposite outer vertical pair can advance only one step on its unleaked rail. Even at n=5 these steps do not meet the inner rung or enable another force. For sufficiency, choose ordinary left and right directional processes, finishing each new column in order with the seeds at that end. A horizontal pair starts by forcing the other outer corner and then its next rail vertex. For any nonempty W disjoint from the seeds, in the left process the first entry comes from the column before the leftmost column of W (or by a rung in column 1); in the right process it comes from the column after the rightmost column of W (or by a rung in column n). The two sources are distinct and each has exactly one neighbor in W, since W was still white just before that entry. Thus no single leak can leave a terminal white obstruction. Among these nine optima an exchange changes one end only, and connects its vertical pair to either horizontal pair; the two changed vertices are diagonal in that end square. This yields the claimed product and no slides. Independently enumerated minimal white obstructions by counting outside vertices with one neighbor in W; hitting them gives the exact nine sets, 12 exchanges and no slides for n=5 through 9, plus the reported small-case counts. This enumeration is corroboration, not the all-length proof.

## originality

PASS

Credit the previous grid theorem for the scalar equality at n≥8, and the earlier product construction for the specific pair of outer rungs. The distinct and supported claim is the complete optimum family for every n≥5 and its precise exchange/slide structure. The closest prior proof rules out smaller sets, not other size-four sets. The inspected ladder fort and reconfiguration records neither state nor imply the placement family for open ladders with a leak.

## value

PASS

The nine-set classification answers where a minimum single-leak robust budget can be placed, which the budget number alone cannot answer. It proves a sharp qualitative distinction between relocation by unrestricted replacements and relocation by adjacent slides at that same budget. The invariant applies uniformly to the narrowest non-path strip, with a concrete lower-bound mechanism and explicit local choices, not just finite exploration or a small extension of the known scalar bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
