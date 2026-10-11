---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For every positive period-k orbit of the boundary Ricker recurrence, summing log(x_{j+1}/x_j)=r(1-x_j) over one period gives arithmetic mean exactly one. The transverse predator variational equation multiplies to the stated product multiplier, so strict AM-GM gives a threshold above one for every nonconstant cycle. The r=2.2 numerical two-cycle and both two-step multipliers are consistent with the formulas. Most importantly, the complete same-model primary paper was read through the relevant boundary-cycle section: its Proposition 3.3 already derives for the attracting two-cycle that x1+x2=2, x1 x2<1, and the transverse multiplier is (beta b)^2 x1 x2, with the exact stability threshold beta b sqrt(x1 x2)=1.

## originality

FAIL

The exact same-model 2026 paper already carries out the decisive calculation for the nonconstant boundary two-cycle: telescoping the Ricker equations gives mean one, AM-GM gives product below one, and the predator block of the monodromy matrix gives the geometric-mean invasion threshold. The submitted arbitrary-period statement repeats those identical three textbook steps with k factors instead of two. The published boundary recurrence itself immediately gives the period-k telescoping identity, and multiplying the scalar transverse derivative over k iterates is the definition of the Floquet multiplier. Under the audit rule that direct corollaries and mechanically implied extensions are covered even without matching wording, the final claim does not survive originality.

## value

FAIL

Knowing that the same threshold mechanism extends to every boundary period is useful interpretation, but in this package the extension is only the routine period-k repetition of a same-model calculation already printed for the two-cycle: telescope a scalar recurrence, multiply scalar derivatives, and apply AM-GM. That does not clear the common value bar for a new research finding even though the statement itself is correct and ecologically interpretable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
