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

With sink a_0, b_2 is not a sink neighbor even at n=4. Its three neighbors are independent and deleting its closed neighborhood leaves a connected graph containing the sink: the remaining top rim is a path, and every remaining lower vertex has its rung into that path. Thus the prescribed height-2 exterior burns, then the three height-1 neighbors burn, then b_2. An addition at b_2 topples it alone and loses no grain. For the apex-sunk bipyramid, recurrence forces some rim site at height 3 because otherwise no first burn is possible. Any rim toppling loses a grain directly, and a toppling at the other apex forces the saturated rim vertex to topple if no rim site has yet toppled. Hence no positive zero-loss avalanche is possible there. The prism faces give exactly the stated plane dual; the standard dual critical-group isomorphism then applies. An independently written exhaustive census filters stable states by all nonempty forbidden subsets, stabilizes with legal batches of topplings, and measures loss by total-mass difference. It gives cube (384 states, 2688 additions, 1162 zero toppling, 1226 zero loss), with 45 and 19 one-toppling zero-loss events at distances two and three, respectively. For the octahedron it gives (384, 1920, 1133, 1133), with no positive zero-loss events. The cube fraction is 64/2688=1/42.

## originality

PASS

The critical-group isomorphism and avalanche-polynomial formalism are established. The distinct claim supported by this comparison is the explicit all-n specified-sink separation for a plane-dual pair, with exact cube/octahedron event counts. No distinct source inspected establishes or immediately implies that comparison. This is a bounded assessment, not a priority guarantee.

## value

PASS

This is a structural counterexample to critical-group determination of a natural dynamical event, not just unrelated graphs with matching group sizes. The two graphs are exact plane duals and the distinction persists for every n≥4. The one-toppling witness and forced-dissipation obstruction identify why one side differs from the other. The exact cube/octahedron counts quantify that distinction on familiar dual graphs but are not the sole contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
