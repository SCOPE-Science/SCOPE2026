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

For any ordered selected subsequence, e_j <= s_(j+m) is necessary (otherwise m+1 are active at s_(j+m)) and sufficient (cyclic assignment). The new job's cyclic predecessor cannot still be active at acceptance, because then the m most recent accepted jobs are active. If g and o are the accepted and an arbitrary feasible index sequence, inductively g_(r-m) <= o_(r-m) implies e_(g_(r-m)) <= e_(o_(r-m)) <= s_(o_r). If there are still only r-1 acceptances at o_r, the first r-m have finished and o_r must be accepted. Base r<=m and the empty prefix hold directly. This proves cardinality optimality in each prefix; cyclic loads differ by at most one, the exact unweighted EF1/EFX condition. Half-open endpoints handle all ties. In the nested example each of the m-1 long jobs conflicts with every other job, so accepting all forces loads (3,1,...,1); deleting one long job permits (2,1,...,1), including m=2. Its length 1+2δ is within the prescribed range. Any solution of size at most m is trivially balanced; at size m+1, keep one compatible pair from an optimal schedule and isolate the other m-1 jobs. This proves the universal first obstruction size. The obstruction is outside co-ordering, not a counterexample within it.

## originality

PASS

The creditable result is the variable-duration co-ordered, irrevocable prefix theorem together with the exact first obstruction size for all m at arbitrarily small duration deviation. Earlier catalog coverage of the equal-duration theorem and the exact m=2 perturbation is material and should be cited; those parts are not new. General optimal revocable scheduling, static equitable coloring, and the older long/short witness do not establish the two extensions. This is a best-of-knowledge statement-level comparison, not a priority guarantee.

## value

PASS

The same simple no-recourse schedule certifies both fair and unconstrained welfare at every prefix for a substantive class beyond equal durations. The exact m+2 threshold identifies the smallest instance at which arbitrary intervals can lose welfare under fairness and rules out a guarantee based on near-equal durations alone. These are structural consequences, not novelty claims about cyclic coloring, general acceptance, or the obstruction template.

The dated certificate retains the supplied scientific assessment, sources and limitations.
