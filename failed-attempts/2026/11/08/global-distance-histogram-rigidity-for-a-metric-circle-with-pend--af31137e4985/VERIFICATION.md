---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For one loop of circumference c and k>=1 positive pendant arms all rooted at one point, the unconditional pair-distance density decomposes into circle-circle, same-arm, circle-arm and distinct-arm convolutions. The sole circle density jump at c/2 is -2c/L^2, f(0+)=2/L and fprime(0+)=k(k+1)/L^2 recover circle length and arm count. The distributional second derivative has least residual atom -k times the multiplicity of the next shortest positive arm, since all positive shifted/pair-sum atoms lie strictly to its right. This proves constructive recovery including ties and cancellations. However, this entire argument is already a special case of a previous larger published theorem; correctness is not historical originality.

## originality

FAIL

Decisive covering theorem: published 2026-10-25 Resultary paper on arbitrary metric roses with m>=1 loops and k>=0 pendant edges at one vertex proves recovery from the same full distance law, including all repetitions and atom collisions. Specializing its exact formulas to m=1 gives fprime(0+)=k(k+1)/L^2, the loop jump, and its signed-atom induction with coefficient C=4-2k-4m=-2k; dividing by two gives precisely the submitted -k atom rule. Nothing in the submitted scientific conclusion remains outside the stronger result.

## value

FAIL

Even though the geometry and inverse proof are correct and graph distance inversion is naturally motivated, the submitted one-loop case and its supposedly distinguishing signed-measure peeling are fully contained in the previously published all-loop theorem. It is a known exact special case without independent new structural information or a new boundary; reproducing it is not a valuable new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
