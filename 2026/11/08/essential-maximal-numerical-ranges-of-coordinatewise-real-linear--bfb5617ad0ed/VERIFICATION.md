---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For each unit phase the local numerical value is z=a+bw and the local squared image norm is |z|². The two quantities for a full unit vector are the corresponding probability averages using squared coordinate magnitudes. A compact weak limit of the distributions has support in F×𝕋: for each finite cutoff the weight before it tends to zero, so the limit is supported on the intersection of closed coefficient tails. The essential norm equals the tail limsup of |a_j|+|b_j| by comparing truncations with weakly null single-coordinate norming vectors against any compact real-linear perturbation. Since r²−|z|² is nonnegative on the limit support, its vanishing integral under norm saturation confines the measure to Γ. Every finite mixture on Γ is realized with squared magnitudes equal to its weights at distinct indices beyond a growing cutoff (each cluster point has infinitely many approximating indices). Without saturation this yields the convex hull of the scalar circles, equivalently of their disks. Equality on the norm-circle forces every positively weighted summand to be that boundary point, so the reconstruction is valid. The realness of the weights' square roots makes the argument valid for real-linear maps. The compact-net construction realizes E; for r=0, coefficients tend to zero and both ranges are {0}, with no eventual zero assumption. Independently, writing x=u+iv with real u,v, the perturbation sends it to u+i(2ε−1)v, so its squared-norm deficit on the unit sphere is 4ε(1−ε)||v||². For ε>0 saturation forces v→0 and numerical value→1, realized by real coordinate vectors. At ε=0 all vectors norm, and disjoint remote phased coordinates give the disk. The disks for the ordinary range are nested inside the unit disk, and the leftmost point gives exactly 2ε; the norm of I−C and the maximal range jump are both checked on the opposite axis directions. The frozen numerical checker only supplies local diagnostics (including a float conversion in the difference-norm test), not the general argument.

## originality

PASS

Best-of-knowledge for the exact coefficient-cluster formula for mixed scalar blocks and its geometric consequences jointly. The definition, compact convexity, and the pure conjugation endpoint are already consequences of prior work. The possible shapes can already be realized by complex-linear diagonal examples; the informative direction is that no other shapes occur throughout this mixed diagonal class.

## value

PASS

The classification computes a recently defined invariant for arbitrary bounded coefficient sequences, establishes which extremal geometries are ruled out in a basic mixed real-linear model, and identifies exactly what can be recovered from ordinary essential-range contacts. The sharp collapse at fixed unit essential norm distinguishes two otherwise closely related invariants in operator norm; neither the old fact that the range is convex nor the endpoint disk alone gives this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
