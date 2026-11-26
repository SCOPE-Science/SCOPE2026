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

A rung fixes both vertices of its column; along a rung-free interval rail counts on the interfaces then alternate between zero and two, giving disjoint dimers. The only rung-free matchings are the two rim pairings, regular for even n and exceptional for odd n. For n≥4 a square is necessarily two neighboring rungs and the two connecting rails: zero rungs would require the whole rim, odd rung count would require at least n rails, and two rungs force the two connecting rails. Toggling one dimer gives the Lucas-cube edges, and deleting then inserting differing dimers realizes Hamming distance. The count is L_n plus the odd exceptions; for each possible dimer, its containing independent sets correspond to the F_(n−1) independent sets of the remaining path, giving nF_(n−1) edges. For odd n the symmetric difference with a regular matching contains an odd number of rungs. Numbering rim vertices modulo 2n, these rungs contribute n mod 2n, so the signed rim displacement needs at least n unit steps. A single such flip costs at least n+1, and flipping directly between the exceptions costs 2n. The unique rim-path matchings after removing both endpoints of one rung, together with that rung, give one alternating arc-plus-rung of length n+1 from either exception. The cutoff is inclusive. The analytic proof covers all n≥4; the frozen Python and C++ checks were read, not executed.

## originality

FAIL

There is direct equivalent published catalogue coverage, not merely a plausible match. The earlier October 26 record proves the same square-flip decomposition and distances. A distinct November 2 record proves the same even/odd cutoff for a single simple alternating cycle, including isolation below n+1 and attainment at n+1. The catalogue establishes overlap, not which same-day record came first or any independent authorship inference.

## value

FAIL

The parity obstruction and its sharp length are mathematically useful, but the frozen package adds no distinct invariant beyond the equivalent catalogue results. The distance and count restate known square-flip geometry; rerunning bounded checks on the covered theorem does not supply a surviving new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
