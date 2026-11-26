---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reconstructed RESULT.md lines 44–102. With X=x-u+1 the three branch images partition [0,1+δ); the first return to [0,1) is addition of λ modulo 1, with one extra step precisely on [1−λ,1−λ+δ). For λ=p/q the q base visits form a grid of spacing 1/q; its phase meets the delay interval n or n+1 times on respective fractions 1−θ and θ, where qδ=n+θ (exactly n when θ=0). The q return steps are necessary before any physical return, and the corresponding tower class has length (q+m)/q times its base length. Integrating the linear phase fractions against |dy|=d(qδ)/(qc) gives half weights at the two endpoints, unit weights inside, and normalization pq+p²/2. At δ=λ the grid has p delayed visits; at and above y* the interval [-v−(1−λ),-v+λ) carries the width-one rotation. In the irrational case each orbit visits the base and is dense there and in the extra level; every invariant probability restricts to a positive base mass inducing a rotation-invariant probability, and its extra-level mass is forced by the base restriction. Thus normalized length is the only invariant probability. Changes on branch rays affect at most countably many translated null sets under iteration. The supplied exact-rational script was inspected, not executed; its recorded finite checks do not justify the universal claims, which were established analytically.

## originality

FAIL

A distinct indexed result, 5b1c8ed826f4, states the same area law verbatim up to reversed indexing and proves the same slice-length and irrational conclusions for the same cone map. Its complementary first-return model and the frozen delay tower count the same trajectories. This is demonstrated equivalent coverage, not an assertion about which result had priority or about dependence between the records.

## value

FAIL

A complete angle-independent area census is useful in its own right, particularly because it weights starting points rather than orbit phases. But this precise census, both types of slice dynamics, and the size bias are already available in the matching indexed result. The change of first-return section and an explicit statement of the elementary boundary limits leave no separately substantial mathematical contribution in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
