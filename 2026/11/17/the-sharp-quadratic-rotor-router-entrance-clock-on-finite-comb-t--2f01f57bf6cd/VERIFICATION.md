---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

At first arrival at frontier v_j, every earlier rotor points toward it. A departure into a subtree whose rotors all point back toward the frontier makes a full excursion, moving twice along every edge in that subtree including its attachment; this follows inductively because each child starts with its rotor pointing to its parent and the next parent exit follows a complete cycle through its children. All these excursions restore the parent-pointing orientations. Before the first exit to v_{j+1}, the 2j+1 edges of the prefix tree can contribute at most 4j+2 traversals; equality uses every prefix branch and requires the untouched frontier rotor initially to point to v_{j+1}. The final exit contributes one step and puts the prefix in the same rooted form for the induction. A periodic state on the tree must be a unicycle with the chip on its cycle: over a period every vertex visited uses all its exits and thus every vertex is visited, and last-departure times strictly increase along last-exit arrows away from any nonchip vertex unless the next vertex is the terminal chip position. Conversely, removing the chip rotor from a unicycle gives rotors directed toward the chip; a full root tour restores the state. First arrival at v_{n−1} always satisfies this criterion, and summing 4j+3 gives the bound. With terminal rotor pointing to its leaf that off-chip dimer prevents earlier recurrence. With terminal rotor left and all others forward, recurrence already occurs at first arrival to v_{n−2}, including at time zero for n=2. Hence the maximizer is unique.

## originality

PASS

The bare-path law, closed-sunlet witness, general unicycle characterization and general stabilization bound each overlap with a component of the setup, but do not establish the exact maximum and its unique initial rotor configuration on an open comb.

## value

PASS

The comb is a natural next family beyond paths and a standard rotor-routing graph. The exact clock gives a benchmark for quadratic transients at an endpoint, quantifies the effect of the private leaves beyond a generic order bound, and identifies which terminal cycle delays periodic entry. The maximizer is not determined by the general recurrence characterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
