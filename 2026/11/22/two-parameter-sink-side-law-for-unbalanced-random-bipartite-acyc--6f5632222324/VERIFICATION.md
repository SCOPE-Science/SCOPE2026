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

Reconstructed the finite alternating-block bijection by repeatedly removing all sinks: opposite colors cannot both contain sinks, and removing a set of one color cannot turn any vertex of that same color into a new sink. Reversal gives a canonical alternating block sequence, and all opposite-color edges must point toward the later block. For a terminal A-block the prefix EGF is Y(1+X)/(1-XY) with X=e^x-1 and Y=e^y-1, and the terminal factor is e^{zx}-1; transpose for B. These are exact for strictly positive mixed sizes. The repair also derives them from the earlier designated-sink sum and its value at z=0, independently verifying that only pure terms differ. For fixed k, marked numerators over H=1-XY are e^x Y x^k/k! and e^y X y^k/k!, versus XY(e^x+e^y) unmarked. Khera–Lundberg–Melczer give the unique varying positive critical point, strict minimality and nondegenerate smooth transfer uniformly on compact positive ratio ranges (their denominator e^{-x}+e^{-y}-1 is e^{-x-y}H). The same Gaussian and exponential factors cancel in the ratio, and XY=1 yields the reported weights and conditional truncated Poisson masses. The limiting masses sum to one, so fixed-k convergence implies total variation by truncation. Writing p=1-e^{-a} gives b=-log p and rho=L(p)/L(1-p), where L(u)=-log(1-u)/u is strictly increasing; thus the weight favors the larger side for unequal limiting ratios. A positive mixture of two exponentials k!P(S=k) with distinct bases is strictly log-convex, not geometric, proving it is not a single truncated Poisson. Equal ratios give a=b=log 2. The frozen small-instance verifier was inspected, not executed; finite counts do not certify the limit.

## originality

PASS

For the repaired claim only: the joint total-variation limit for unequal positive limiting ratios, with the class bias and distinct mixture parameters, remains supported. The original contribution statement overcredited the exact finite formulas: the earlier all-size designated-sink identity mechanically gives both marked functions, even though it presents only the total marked function. The repair explicitly attributes that finite content and the balanced law and does not claim a new counting or transfer technique. The strongest inspected general asymptotic theorem counts lonesum matrices without marking sinks; the closest marked Resultary limit is diagonal-only and uses equal terms by exchange of classes.

## value

PASS

The unequal-ratio result resolves a natural question not answered by balanced symmetry: how sink class and count are jointly distributed once the sides differ. It identifies a direction of class bias, a dependence on that class, and a genuinely different marginal law rather than a change of a single Poisson parameter. The value is this complete limiting description, not the repackaging of exact finite counts or a new asymptotic method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
