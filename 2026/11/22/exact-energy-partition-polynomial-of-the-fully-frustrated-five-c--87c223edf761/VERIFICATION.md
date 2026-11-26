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

With B having rows indexed by even vertices and columns by odd vertices, distinct columns have disjoint neighborhoods or two shared neighbors in a negative square; the latter contributions cancel. Thus B^T B=5I and, since B is square, BB^T=5I. The odd fields B^T u consequently have total square 80, giving b+3c=8 and a=8+2c. A prescribed field of magnitude five forces its five spins up to one common sign, giving 4096 assignments. A pair of such fields at distance two contradicts square parity; each distance-four pair has disjoint neighborhoods and contributes 256 assignments. There are 40 distance-four pairs and no triangle of them (distinct weight-four differences have xor weight two). Inclusion-exclusion gives 10240,45056,10240 assignments for c=0,1,2, respectively. Multiplying the independent odd-spin factors proves the entire Laurent polynomial. The highest profile score is 32-2c; flipping one unit field lowers it by two, so the first two multiplicities are 10240 and 8*10240+45056=126976. Score 32 means (80-32)/2=24 negative edges, and connectedness makes switching exactly two-to-one. Gauge completeness follows because the square moves interchange distinct consecutive coordinate flips in any closed walk; equal consecutive flips cancel, so squares generate the cycle space. The independent bounded replay python3 /workspace/replay_independent.py 5 used Gray-code field updates and a separate subset-sum calculation for every even assignment, verifying the three profiles, every score coefficient, symmetry and total mass 2^32. The proof, not just the replay, explains these counts.

## originality

PASS

Pass for the full labeled zero-field Q5 spin-level count and its multiplicity consequences, not for F5=24, the signed adjacency identity, or discovery of a minimizing state. Closest inspected results give the minimum and bounds, an exact census at Q4, or an infinite-dimensional/orthogonal-coupling analysis. None gives or mechanically implies the Q5 polynomial. Historical priority remains provisional, including because the 1979 scan was not independently accessible.

## value

PASS

Zero-field density of states is a natural exact invariant of the classical 32-spin fully frustrated model. The known minimum gives no entropy/degeneracy even at the ground state. This three-profile formula supplies the full thermal count and the first excitation with an exact mechanism, rather than a single arbitrary table entry. The value is for Q5 at zero field, not for higher dimensions or an orbit classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
