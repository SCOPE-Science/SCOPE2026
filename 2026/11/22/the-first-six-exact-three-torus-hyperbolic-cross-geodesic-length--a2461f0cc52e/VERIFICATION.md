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

The winding is constant-speed, so its normalized arclength equals ds/(2π) in the stated parameter. The Fourier integral vanishes exactly when m·v≠0. Unit frequencies exclude zero coordinates; signed permutations preserve the cross, and division by a common factor preserves every nonvanishing dot product. Thus positive ordered primitive triples suffice. At each displayed cap any equally short or shorter triple is in the bounded search, which includes equality. An independent calculation solves m₃=−(a m₁+b m₂)/c by divisibility for |m₁|,|m₂|≤t; when m₁=m₂=0 there is no nonzero orthogonal frequency. It finds one survivor per cap with exactly the stated winding norms (21,65,101,133,133,314), primitive candidate counts (9,41,80,119,119,421), and cross cardinalities (27,81,135,225,279,405). Each survivor attains its cap and the physical length is 2π times its norm, proving minimality and the signed-permutation classification.

## originality

PASS

The generic Fourier criterion, the cross itself and the t=1 cube answer are not new. The supported distinct result is the sharp finite three-dimensional classification at strengths 2 through 6, including equality cases; the strongest related theorems treat a different dimension or set of frequencies, weaker optimality, or a different objective.

## value

PASS

For an independently motivated Fourier exact-design problem, the shortest primitive winding gives the exact cost of a single periodic trajectory. Beyond the known cube baseline, the first five nonbox cases locate a genuine plateau despite 54 added frequencies and then an exact jump from 133 to 314 in squared cost; in particular (3,−2,0) enters at strength six and obstructs the old optimum. This initial classification with rigidity provides precise feasible designs and benchmarks for sharpening higher-dimensional length bounds, not just examples at one selected parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
