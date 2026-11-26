---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Preservation of J follows because all of J consists of nilpotent elements and an element with nonzero scalar part is a unit. Arbitrary generator images in J extend uniquely. For fixed commuting tangent idempotents, on a component V_a to W_b of Hom(V,J²), idempotence forces Q_i=0 if a_i=b_i (the multiplier a_i+b_i−1 is ±1); commutativity says (a_j−b_j)Q_i=(a_i−b_i)Q_j. If a≠b this gives exactly one free C block via Q_i=(a_i−b_i)C; if a=b all Q_i vanish. This works also in characteristic two, proves the exponent by summing the nonresonant blocks, and is precisely conjugation by v↦v+C(v), which fixes J² and has inverse v↦v−C(v). The tensor action has weights given by AND and the tangent orbit of labelled decompositions has the claimed block-diagonal stabilizer even with empty eigenspaces. Simultaneous conjugacy and the weak-composition class count follow. A commuting product fixes exactly the common image, and in the linear model its image in A has the free truncated basis on a tangent space of dimension r_S, including r_S=0 and the empty product. For d=k=2 there are four one-label profiles, five comparable two-label pairs with exponent 4 and one incomparable pair with exponent 6, giving the stated polynomial. An independent direct bit-packed substitution check over F₂ tested all 4096 generator assignments, recovered 98 idempotents and 868 commuting pairs in ten profiles, and checked product images on J; see /workspace/branches/independent_replays/replay1.py and replay1.out. This small replay does not establish arbitrary characteristic, which follows from the proof.

## originality

FAIL

The separate earlier Resultary joint-rank-spectra record 7cf73757b94c gives the same labelled profile count and simultaneous conjugacy for the nilpotent radical viewed nonunitally. Restriction and scalar extension give the same endomorphism problem. The orbit count, joint image-intersection census, singleton extension and d=k=2 formula are mechanical consequences, not supported distinct claims.

## value

FAIL

The invariant itself is natural, but the frozen work gives its already-covered census; replacing the radical by its unitalization, adding one dimension to image ranks, and specializing the formula at d=k=2 do not yield an independent scientific advance. The binary replay corroborates but does not repair the overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
