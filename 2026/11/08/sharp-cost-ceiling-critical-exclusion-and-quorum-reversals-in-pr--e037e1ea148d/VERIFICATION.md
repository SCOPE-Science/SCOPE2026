---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Reassessed the quorum-comparison repair. For each fixed z, x+ρy=ρ(1−z)+(1−ρ)x; among 0<z<1 the unique optimum in x is at x=0, and the remaining beta-shaped factor peaks only at z=h/n. The weighted benefit and advantage are constant at ω=0; the new text explicitly limits weighted uniqueness to ω>0 and distinguishes normalized ceilings when ω=0. The sign of the adjacent binomial-peak ratio is controlled by the strict increase of (1+1/u)^u. For s≥2 the risk-factor ratio is 1−1/(Σ_{i=0}^{s−1}ρ^(−i)), strictly falling from 1 to (s−1)/s. In the late-quorum case the binomial ratio is strictly between 1 and s/(s−1), by the two strict log bounds log(1+t)<t and log(1+t)>t/(1+t). These yield the exact unique crossing including equality, while symmetry of the binomial peak and the strictly falling risk factor give the unique first quorum, also when n=2. For N=5 the ratio is (9/8)/(1+ρ) and 765/2048<3/8<405/1024 as stated. Also checked the withdrawn dynamics: monotone z/x confines the trajectory to a compact set missing the unique normalized maximizer and yields its uniform-in-time gap; at z=0 the scalar edge bracket is increasing and the transverse rate at an interior edge equilibrium is −k. The vanishing perturbation and isolated scalar zeros justify convergence but do not make it novel. The frozen exact-rational checker was read, not run; the reported 13,680 composition cases and finitely sampled comparisons do not prove the general crossover or the original dynamics. The repaired proof independently establishes the comparisons.

## originality

PASS

The same exact ceiling and critical-threshold elimination were already covered, and both are explicitly treated as known or withdrawn in the repair. The new evaluated claim is the sharp global and adjacent comparison of the known ceilings as functions of quorum and survival factor. The source's stability diagrams compare a different quantity; the closest exact ceiling statement does not give the crossing classification, and deriving it needs a strict ratio comparison including both endpoint limits. No novelty is claimed for the standard binomial limits or the scalar edge classification.

## value

PASS

The comparative statics distinguish a globally optimal smallest quorum from nonmonotone behavior among larger quorums. The crossing theorem identifies exactly where the effect of an adjacent quorum increment reverses, at arbitrary group size; it yields strict incentive differences at intermediate costs without conflating them with stable coexistence. This is a useful structural property of the modeled risk-weighted incentive ceiling beyond its already known formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
