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

An invertible affine change preserves all attainable phase pairs, and the common translation phase cancels from orthogonality. For two normalized characters the zero condition is a+bz=-(c+dz)w with z,w on the unit circle. Equality of the two magnitudes gives H+2J Re(z)=0, also sufficient when both sides vanish. Four characters fill the four-dimensional weighted evaluation space; squared row norms are four times the masses, so four are possible exactly at uniformity. For a triple the three-column projection similarly gives 3 times each mass <=1. If H=J=0, equality of the sums and products of the positive row pairs leaves either a zero line w=-1 (if a=c and b=d with a!=b, ruling out a triple) or the opposite-equal case a=d, b=c. There the projection bound is the stated ratio-two bound; the cosine construction cancels the first two differences by C plus the reciprocal-ratio term, and the third by 2C^2-1=-r, valid including r=1/2 and after swapping the roles of a,b. Outside H=J=0 the denominator can vanish at a zero only when z=-1, a=b and c=d; its zero line likewise precludes a triple. Otherwise Re(z) is fixed and w determined, so the zeros are contained in a conjugate pair. A triple must have a nonidentity order-three difference, because both opposite points and their doubled difference must also be zeros. Strict positivity rules out either coordinate equal to 1 at order three. The only possible phase pairs then impose a=d=b+c or b=c=a+d via the real relation 1+omega+omega^2=0, each attained. Uniformity is correctly checked first. `python3 /workspace/review_replay.py 3` independently checked representative cube-root witnesses and ratio-two boundary identities in exact arithmetic; the case proof covers all real masses, not only sampled weights.

## originality

PASS

Meaningful subcases are covered or bounded by related theorems, including the existence of the two root-of-unity families from the one-dimensional classification by projection and reflection. The distinct result is the full classification on the phase-constrained parallelogram, in particular attainability throughout the opposite-equal interval under its phase constraint and the exhaustive exclusion of any other triples.

## value

PASS

The smallest planar parallelogram carries both a nontrivial dependence among the four phases and varying positive atom masses. The exact classification distinguishes existence of one zero from packing three pairwise-orthogonal characters, and exhibits both a sharp continuous threshold and isolated types of torsion resonance. Having the exhaustion on the full torus is useful and is not a restatement of finite spectrality or either related support classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
