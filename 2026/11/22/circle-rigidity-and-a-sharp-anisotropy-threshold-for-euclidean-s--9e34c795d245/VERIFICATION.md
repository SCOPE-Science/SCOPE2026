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

Put s≤T for the two side lengths and let d be the shorter diagonal. The best boundary-only tree costs 2s+T. For d<T, the two opposite short sides plus that diagonal give a strictly cheaper tree. For d≥T, boundary-first Kruskal achieves the boundary-only tree; in particular the decisive equality does not force a shortcut. This uses chords between consecutive sample vertices, not oval arcs. For a circle the diagonals are strictly longer; on a noncircle the radius along a regular arc has a nonzero derivative somewhere. Orienting toward increase, the gain |u+v|−2|u| equals |v|−|u| up to a quadratic error for nearby points and is strictly positive. This persists on an open set. The modulo-π half-gap and mid-angle are independent by the uniform torus shear. In the ellipse coordinates with z=tan δ, d² is at least both side-length squares exactly for q_k² z≥2h_k and 2h_k z≤r_k², with the unrestricted interval when h_k=0. This gives the stated clipped arctangent and its uniform mid-angle integral. Using r_k² q_k²−h_k²=k², the interval is empty iff 3h_k²>k²; its equality is a singleton separation, and the equality set in mid-angle has zero measure. Hence the exact orientation fraction is H(k), with onset strictly above sqrt(3); at sqrt(3) the axis-endpoint pair has diagonals 2 and 2sqrt(3) and sides 2, so a boundary-only tie really occurs. Only ties in the deciding comparison matter, not the repeated opposite side lengths. Each arctangent argument increases off the axes with k, and a neighborhood of an axis stays unsaturated for every finite comparison, giving strict increase. At fixed nonaxial t the product of the arguments tends to 4, and the uniform first-order expansion near k=1 averages to 16/π². The bounded independent replay python3 /workspace/independent_sanity.py checked best boundary-only versus best overall cost by enumerating all 16 trees for 5,766 grid configurations away from numerical decision ties. This corroborates rather than proves the law.

## originality

PASS

The known proximity-graph screening and spanning-tree criteria are ingredients, not new claims. The inspected nearby results do not cover the probabilistic ellipse invariant, all-separation aspect-ratio threshold, or rigidity among smooth centrally symmetric ovals. Assessment is scoped to checked evidence.

## value

PASS

Antipodal pairing produces a natural four-point test of when Euclidean optimal connections leave the sampled boundary cycle. The universal rigidity, uniform-angle frequency, sharp onset of positive-measure saturation, and first variation describe one concrete geometric mechanism at several levels; the near-circle coefficient and all-separation threshold are not routine restatements of a graph criterion. Probability is only for independent uniform eccentric anomalies modulo antipodes, not arclength.

The dated certificate retains the supplied scientific assessment, sources and limitations.
