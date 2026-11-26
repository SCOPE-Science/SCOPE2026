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

Even cut parity forces the two rail edges at each cut to occur together; matchings are exactly monomer–dimer tilings of the column path. Both rails at one cut cannot be shattered together, adjacent selected cuts conflict, and their endpoints cannot carry queried rungs. Forcing all selected rail queries to one reduces the remaining rung traces to disjoint intervals. A maximal alternating run beginning and ending with one has more queried columns than available neighbors: force its rungs absent and every other queried rung present. No two absent columns in the run are adjacent, and any outside neighbor of an endpoint is a queried rung forced present, so the trace is impossible. In all other runs, adjacent pairs within the run saturate the ones using distinct zeros. These pairs and selected rail cuts are disjoint and may each independently be tiled with a dimer or two monomers, proving the converse with all physical labels accounted for. The alternating-run transfer matrix gives R=1/(1-t-2zt^2+zt^3); inserting selected rails between interval factors gives R/(1-2zt^2 R) and exactly the claimed series. Expanding 4-t=3+(1-t) proves the coefficient formula, bounds and leading terms, including the empty-width convention. At n=6 the two central rungs are shattered; adjoining any rung makes a forbidden run and the only nonincident rail cuts (1 and 5) make a boundary singleton run. Cuts 1,3,5 give a shattered triple. An independent graph-based replay compared 1170 physical supports through width four and verified the size-two facet against all 14 one-edge extensions at width six.

## originality

PASS

The same-family prior work establishes the scalar VC dimension, count of matchings, and tiling reduction. The full mixed physical-support criterion, all-width polynomial, and nonpurity are not given by those results or by the inspected related matching and flip-graph results. This is a bounded priority assessment.

## value

PASS

An all-width enumerator and exact support-level criterion for the standard open ladder answer materially more than the known rank: they decide which physical queries can coexist and give all face numbers. The first supplied nonpurity witness shows why maximum cardinality is not a complete description of maximal query patterns. The result is not simply a count of matchings or resonance cubes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
