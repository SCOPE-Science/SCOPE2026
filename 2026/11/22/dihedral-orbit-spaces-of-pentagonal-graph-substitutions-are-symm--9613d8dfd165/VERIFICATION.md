---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

## Executed checks

The standalone `VERIFY.py` was run with Python 3 without third-party dependencies. For \(d=0,1,2,3\), it generated the complete nonempty independence-face collections for the five-cycle substitution with \(H=(d+1)K_2\), canonicalized all faces under the ten-element dihedral group, and compared their orbits bijectively with the two-element stabilizer orbits of the chosen diagonal-pair join. Counts: \((30,5)\), \((360,44)\), \((3510,377)\), \((32400,3320)\) for (faces, orbits), respectively. It independently exercised the standard integral projective-cell-boundary formula through \(d=8\), including the degree-four \(\mathbb Z/2\) class for \(d=2\).

## Proof-level checks

The unrestricted result follows from uniqueness of two-support outer independence sets, the exact treatment of single-support overlaps, a compact-Hausdorff quotient argument, an equivariant sphere model, and an orthogonal conjugacy between factor swap and a sign involution. The claimed homology shifts follow from integer cellular boundary coefficients \(0\) and \(2\), not from mod-two Betti numbers alone.

## Limits

Finite enumerations do not prove an arbitrary-graph or all-dimensions theorem; that scope rests on the written proof. The script does not construct a full chain equivalence of the orbit spaces, because the proof establishes an actual homeomorphism. Independent mathematical audit has not been performed.
