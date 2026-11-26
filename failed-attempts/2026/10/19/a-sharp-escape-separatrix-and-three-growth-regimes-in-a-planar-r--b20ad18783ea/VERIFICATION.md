---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Set u=cx and f(y)=1/(1+y^2). Each positive step is of width u_n, and u_{n+1}=u_n(1-q f(y_n)); u_n decreases and y_n increases. Telescoping velocity loss and comparing left rectangles with the integral gives q∫f <= u_n-v <= q∫f+q u_n[f(y_n)-f(Y)], with both bounds strict on an unbounded orbit since the first rectangle is already strict. The capture certificate follows by a geometric majorant below a chosen R>y_n; the escape certificate forces v>0 by the loss bound. The strict certificates characterize the two open nonempty phases, so their complement contains a critical trajectory. Critical u_n is asymptotic to q/y_n, giving squared-height increments tending to 2q; two critical speeds at the same height would have the ratio of their subsequent speeds bounded below by the initial ratio>1 by order preservation, yet both have the same universal leading speed. Thus the separator is unique. Strict integral bounds imply the small-q limit. For bounded height the multiplier is bounded by its limiting value strictly below one. For positive terminal speed the tail loss is q/y_n+O(y_n^-2); summation and back substitution yield the claimed summable speed error and the height's logarithm and constant. At q=1, V=yu obeys V'-1=(V-1)(1+V/(1+y^2)), so the unique critical curve is V=1; the squared height w has increments 2+1/w, implying w_n=2n+O(log n), and the difference 1/w_n-1/(2n) is summable. These arguments prove the quantified claims without finite simulations.

## originality

FAIL

Two distinct inspected Resultary records jointly cover the claim's material content. The endpoint record gives the exact same q=1 separator and stronger endpoint remainder bounds. The generic-coupling record proves a nonempty critical interval and stronger asymptotics in the identical map for a sector including all target y_0>0, and supplies the tail and monotonicity estimates. Although that record expressly leaves the singleton assertion unstated, any two critical speeds at the same height have speed ratio bounded below by their strictly ordered initial ratio, whereas its stronger critical laws force ratio one. This and the direct estimates below mechanically yield the claimed generic classification, bounds and rates. This is a finding of substantive equivalent coverage in the inspected catalogue, not a finding that either comparison record preceded the frozen manuscript or that the 2022 primary source already knew it.

## value

PASS

As a mathematical classification, an exact separator and rigorous critical and ballistic scales are useful for the natural monotone fixed-line regime of this published map. This value assessment is of the concrete mathematical content; it does not credit the manuscript with a distinct result given the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
