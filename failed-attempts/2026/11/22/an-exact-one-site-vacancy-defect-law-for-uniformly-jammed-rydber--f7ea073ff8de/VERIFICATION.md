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

On the stated rings L≥4b+5 set B=b+1. An intact gap is in [B,2B−1]; a gap of length g can expose only the g−(2B−1) central sites if this number is positive. Hence the extra sector has a unique gap 2B anchored at ±B, all other gaps ordinary. Rooting a cyclic composition at any atom counts each intact n-atom state n times; the exceptional gap has a fixed root and needs no division. For example b=1,L=9 gives intact 3y³+9y⁴, intact with 0 empty 2y³+5y⁴ and extra 2y³. The intact count rooted at occupied site 0 has generating function yG/(1−yG); combined with the count in RESULT.md lines 32–62 this supplies the density limit directly without interchanging an asymptotic and a derivative. The pole at yG(z)=1 is simple and unique on its circle since consecutive exponents cannot both have phase 1 off the positive ray. Residues give limits 1 for Z times z^L, rho for the occupied-site contribution times z^L, and y rho z^(2B) for the exceptional contribution times z^L. Line 57's 'root of yG' is a local wording error; the intended denominator and root equation are explicit. At y=1, u=−B log z obeys the printed root equation; bounded u would force an unbounded geometric sum, and u/B bounded away from zero would contradict the same equation. Thus u exp(u)~B. The excess length has the mean of a truncated geometric law, bounded by 1/(exp(u/B)−1), yielding rho~1/B and P~(log b)^2/b^3 after taking the stated limits in order. Read checker.py and VERIFICATION.md without executing them.

## originality

FAIL

The exact intact pair-correlation law already covers the purported new defect observable after a direct invertible change of configurations. This is demonstrable implication, not a claim that the earlier text used the wording 'inert site' or that a search hit alone duplicates the record.

## value

FAIL

A pinned site is a natural perturbation and the formula can be convenient, but the submitted exact invariant is a normalization of two already accessible intact local probabilities. Insertion/deletion of the forced central atom and evaluation at distance 2B recover both the finite count and the thermodynamic law; the scale then follows from the standard bulk root. No additional independent gap or defect phenomenon survives as a new exact finding on the stated scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
