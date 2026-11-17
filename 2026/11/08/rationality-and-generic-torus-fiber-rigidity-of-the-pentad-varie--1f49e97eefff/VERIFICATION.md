---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For any generic pair of rank-two Plücker configurations, separate GL2 row changes normalize its first three x_i and y_i to (0,1,2), simultaneous column scaling fixes first input factors, and global scaling fixes λ1=1. The invariant target ratios u2,u3, uj,vj,wj recover every normalized coordinate: xj=2(wj−vj)/(1−2vj+wj), Bj=(1−vj)xj+vj, yj=xj/Bj, λj=uj Bj, λ2=u2, λ3=u3. Direct substitution yields the identity on an explicit nonempty dense open; the intrinsic ratios give a rational inverse and transcendence basis of size 3n−7. Because all generic pairs admit this normalization, fiber equality means they differ by the simultaneous free diagonal torus; no extra generic components. Independent exact rational substitutions of 24 nondegenerate parameter sets for n=5,6,8 corroborated inverse and projective coordinate normalization. The statement is only generic over C, with denominators required nonzero.

## originality

PASS

Koefler–Ventura–Yu (2026) define Pen_n and their Proposition 4.8 supplies the underlying parameterization and Jacobian rank, while their Remark 4.9 identifies a torus orbit as a fiber component. The submitted explicit rational inverse proves degree one and no additional generic components, a logically stronger algebraic conclusion. The critical recent primary paper was not fully accessible in this run, so potential hidden rationality or inverse elsewhere in its body/appendices is a material residual risk; accepted as best of knowledge, not certified historical priority.

## value

PASS

Rationality of an entire naturally defined algebraic family and identifiability of its source modulo precisely its expected torus are central structural questions; the inverse gives a concrete birational chart and improves an orbit-as-component statement to generic fiber uniqueness. This is not merely relabelling parameters, and does not pretend to classify boundary fibers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
