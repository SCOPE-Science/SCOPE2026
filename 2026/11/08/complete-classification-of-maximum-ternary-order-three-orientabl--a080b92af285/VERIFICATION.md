---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

At order three on three labeled symbols, nine nonpalindromic reversal pairs bound any orientable cyclic word by nine windows. Every extremal cyclic word chooses one directed edge from each of nine pairs, and Euler balance/strong connectivity characterize its admissibility. The actual verify_euler.py enumerates all 512 choices, ten balanced masks, two connected masks; the matrix-tree/BEST calculation gives four cyclic Euler circuits for each. Independent direct enumeration of all 3^9 rooted words gives exactly eight rotation classes; all six symbol permutations plus reversal split them into orbit sizes 6 and 2. The reported eight canonical words were reobtained independently. No extrapolation to higher orders is used.

## originality

PASS

The period-nine bound and individual examples were published before this result, but the examined primary papers describe constructions/upper bounds, not the exact eight-cycle population and two alphabet/reversal symmetry classes. A search did not discover a stronger complete low-order orbit census. Historical conference catalogs remain a qualified risk.

## value

PASS

This is an exact complete extremal-census result for the first nonbinary low-window orientable sequence setting. Counting all maximizers and their genuine symmetry types is useful for direction-and-position identifiers even though maximum length is established. The classification is exhaustive with a principled Euler-tour proof rather than an arbitrary selection of examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
