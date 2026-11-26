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

At Walsh level k the squared mass of e_u-e_v is 4/2^d times the number of k-subsets meeting the differing coordinates oddly. For each interior k, take k-1 coordinates avoiding a fixed differing coordinate and a fixed agreeing coordinate, then append either of those two: the parity flips, so the mass is positive. Level zero is inactive and level d is active exactly for odd r. Decompose into the span of the nonzero level projections and the orthogonal remainders of the old eigenspaces. The former has one simple updated root between each pair of active levels and one above the last by secular monotonicity; none lies at an active pole. The interior remainders have dimension binom(d,k)-1>0. For odd r this gives d retained values and d disjoint new values. For even r only the inactive top level can coincide with a new root (zero cannot); substituting 2d into the secular equation gives one strictly positive weight, at which precisely one pair coalesces. For r=2, integrating (1+x)^(d-2) from zero to one gives the claimed reciprocal weight. For instance d=3 and r=2 give active masses 1,1, and their two updated unshifted levels at t=4/3 are 8/3 and 6, the latter colliding with the old top. The identity shift leaves the count unchanged and ensures positive definiteness. The CG conclusion follows from the relative minimal polynomial on a right-hand side with every eigenspace component nonzero: its degree is exactly the distinct count.

## originality

PASS

Credit the general exceptional-weight criterion and rank-one Krylov bounds as prior. The supported distinction is the explicit family-wide active-pole and Hamming-parity analysis, global count including the sole collision, and evaluated short-distance conductance. The named inaccessible early paper leaves a priority risk, not a finding of prior coverage or a guarantee of priority.

## value

PASS

The exact support and parity analysis locates an isolated eigenvalue-count defect and specifies where it occurs, showing how almost double the cube's exact Krylov grade emerges from a single added edge. The result distinguishes distances and conductances in a natural family that the general rank-one bound cannot resolve; it is more than a numerical spectrum or a restatement of a general exceptional-weight criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
