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

Euler's identity excludes common zeros of the two partial derivatives for a squarefree binary quartic, so the polar map has degree three. Its fiber over [s:t] is cut out by t f_X−s f_Y; the fixed target-coordinate change to the discriminant variables does not affect j. The three-root normalization covers all quartics in scope. Independently, in the even normal form X^4+z X²Y²+Y^4, the discriminant of the pencil with both partials divided by two is −8z³(u^4+v^4)+(z^4+72z²−432)u²v². Exact invariants give the asserted j-map; the branch discriminant in this family is 27648 z^6(z−6)^6(z−2)^2(z+2)^2(z+6)^6, vanishing precisely at J=0 among smooth inputs. The even normal form is available by conjugating a double-transposition involution of the four points to x↦−x and rescaling the two paired roots. The harmonic orbit is represented by X^4+Y^4, with cubic-power polar and branch divisor u²v². The two numerators for Φ and Φ−1728, plus the pole at infinity, give the listed partitions. Their defects sum to six, and a transitive subgroup of A4 containing a 3-cycle has order divisible by both four and three, hence equals A4. The affine change produces the classical level-three j-projection as a cover, not a modular polynomial relation involving the original quartic's own j.

## originality

FAIL

Sanyal–Sturmfels–Vinzant already print all five coefficients of the exact branch quartic for the same universal one-parameter input used in the frozen proof. Applying the classical I,J polynomials to those printed coefficients and cancelling gives the exact frozen j-map and exceptional locus, with no further polar geometry, family extension, or result-specific invariant theory needed. This implication was verified symbolically from the earlier printed coefficients, not inferred from a similar title or a failed search. The ramification and monodromy descriptions are consequences of the resulting rational function, and the modular identification compares it to an already tabulated projection by the displayed affine substitution. The prior text need not explicitly present the j-function for this to be stronger coverage under the comparison standard.

## value

FAIL

Both the polar and branch moduli are natural and the equality is a useful reformulation. Under the standard for a narrow exact invariant, however, the prior full coordinate branch formula on the same family already gives the exact fact by direct invariant substitution, and the level-three identification adds a coordinate comparison to a tabulated cover. No nonmechanical structural claim beyond that reformulation is established in the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
