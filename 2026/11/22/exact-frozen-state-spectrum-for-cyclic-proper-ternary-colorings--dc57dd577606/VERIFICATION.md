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

An indexed proper coloring is specified by its first named color and a cyclic sign word. If p of the increments are +1, closure is 2p−n≡0, equivalently p+n≡0 (mod 3). An adjacent swap is allowed exactly when both outside neighbors are the third color, or equivalently the surrounding three increments are equal; the same argument works on the triangle where the outside neighbors coincide. Frozen words thus avoid 000 and 111, not isolated signs. The weighted trace over states 00,01,10,11 counts indexed cyclic words with no division for periodic orbits; summing the three twists implements closure and cancels the factor 1/3 against three initial colors. Direct determinant expansion gives (1−z−z²)(1+z+z²) and, for either nontrivial twist, (1−z)(1+z+z³). The traces and Newton sums produce the stated Lucas term, cubic recurrence and rational generating function, subtracting the length-two coefficient 6 (length one is zero). Minority-run capacity excludes the admissible weights at lengths 3,5,7; alternating words at even lengths and (001)^3 followed by alternating pairs at odd lengths at least nine give valid cyclic witnesses including the closing triples. The cubic has one negative real root −alpha (local extrema are positive), and the conjugate pair has modulus alpha^(-1/2) by the root product. Thus the Lucas root dominates and division by 2^n+2(−1)^n yields the claimed asymptotic fraction. /workspace/evidence/reproduce_other_checks.py verified counts for n=3..27 by a separate twelve-state trace over actual consecutive color triples. That check supports, but does not replace, the all-length proof.

## originality

PASS

The supported claim is the exact congruence-refined cycle count, exceptional lengths and asymptotics for named proper colorings under adjacent legal swaps. The swap model, path rigidity and generic weighted transfer methods are not claimed as new. The precise forbidden-word statement attributed in the frozen record to Agur et al. was not independently verified and is not used as negative coverage evidence.

## value

PASS

Isolation is the most immediate obstruction to moving within proper adjacent-swap colorings. Indexed cycles are the simplest family where the local obstruction must satisfy global color closure. The count resolves every length, explains the small odd exceptions, and gives an exponential rate for the proportion of states with no permitted first move. It does not claim to classify larger components or add a new general transfer-matrix method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
