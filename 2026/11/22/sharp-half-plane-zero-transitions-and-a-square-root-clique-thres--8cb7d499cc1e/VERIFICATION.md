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

The join permits cycle-only independent sets and the h singleton clique sets, giving the linear perturbation at common fugacity. The transfer recurrence has characteristic roots (1±sqrt(1+4z))/2; the d distinct Chebyshev phase zeros give the stated factorization with constant 1. On the positive imaginary axis the unwrapped phase increases from 0 to dπ/2, so only the phases (4j+3)π/2 with 4j+3<d occur; zero itself is excluded. At a crossing F'/F=A−iyB, with A>0, giving P_z=u(1−y²B)−iuyA and Re(dz/du)=y²A/[u((1−y²B)²+y²A²)]>0. This proves simplicity, the forward direction, and the counts even at tied gains (the crossing pairs are then distinct); the fixed leading coefficient prevents any other change for d≥2, and d=1 is a stable positive linear polynomial. For C8 the positive-gain solution gives 72+56sqrt(2), strictly between 151 and 152. The first two coefficients give sum(a)=n and sum(a²)=3n. For the envelope minimizer t=y² the stationarity sum is between 3nt/(1+16t) and 3nt, pinning t between 1/(3n) and 1/(3n−16) for large n. Thus log H at its minimum is (1+log(3n))/2+O(1/n). On this frequency scale the phase grows with derivative n+O(1); an admissible phase lies O(1/n) away in frequency. The curvature of log H is O(n) there, so discretizing the envelope incurs only O(1/n) relative loss. This proves the frozen constant sqrt(3e). A fresh independent recurrence, rational isolation of the even part in y², and exact rectangle root counts checked C7, C8, C12, C16, C17 including 0, 2 and 4 RHP zeros. In addition P(12,35)=(2z²+1)(z⁴+18z³+52z²+47z+1), with a simple axis pair and a strictly stable quotient; this checks the strict boundary convention at an integer gain.

## originality

PASS

Credit the known clique-join eventual-instability phenomenon and the related equal-root corona census. The supported distinct contribution is the exact cycle gain census with the cycle-specific boundary and discrete-to-envelope asymptotic sqrt(3e), not the generic idea of testing imaginary-axis crossings or the existence of unstable joins. No inspected statement supplies or implies this combination; the literature assessment remains bounded.

## value

PASS

The sharp onset for a natural cycle-plus-clique model is not determined by real-rootedness of the cycle or qualitative large-clique instability. The gain census distinguishes strict stability, neutral boundary, and multiple unstable pairs, and the sharp growing threshold distinguishes a fixed-size clique from the first possible instability scale. This is substantive even though the method uses standard root-continuity tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
