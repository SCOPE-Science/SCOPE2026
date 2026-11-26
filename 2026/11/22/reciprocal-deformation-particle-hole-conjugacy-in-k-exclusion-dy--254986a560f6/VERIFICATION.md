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

Checked the published rate convention. Combining complement with reflection sends a marked bond to the reflected bond with its orientation unchanged and changes old source/target occupations (a,b) to (K−b,K−a). Using [K]_t−[b]_t=t^b[K−b]_t and the reciprocal finite sum, the transformed rate is exactly t^(2−2K) times the original. The same direction-specific factor 1 or q multiplies both rates, including q=0, and the forbidden-hop zeros match. Summation gives the diagonal, so the generator proof works also in the one-state sectors. Positive scalar multiplication and permutation give the spectral, semigroup and path-law statements, and relabeling the successful marks gives the current and jump-count identities without a sign change. At q=0 the model is still irreducible within each nontrivial sector: a legal backward adjacent move can be effected by one forward hop along each arc of the complementary directed path. At empty intermediate sites do the arrival first, at full ones the departure first; these local precedence constraints along a path have no cycle. The allowed undirected nearest-neighbor transfers connect the sector. Thus stationary laws are uniquely transported, and the worst-start total-variation distance at time s is the original one at t^(2−2K)s, giving the inverse time factor for mixing. Frozen exact script read as supporting evidence, not executed.

## originality

PASS

The distinct established claim is complementary-sector marked generator conjugacy at reciprocal deformation, including its exact deterministic clock. The published stationary symmetries and all standard consequences of generator conjugacy receive no independent novelty credit. The rate calculation is short but establishes a stronger dynamic equivalence not supplied by composing equalities of stationary weights.

## value

PASS

The natural motivating gap is between two known stationary symmetries and what happens away from stationarity. The simultaneous complement and reflection with reciprocal t recovers the complete finite dynamics, including directional current fluctuations at any time, and relates sectors and relaxation clocks before any diagonalization or stochastic asymptotics. This is a useful exact structural equivalence, rather than a restatement of the equilibrium invariances or a numerical special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
