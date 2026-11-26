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

Greedy arches give a universal word up to their number; the sequence of arch-ending symbols followed by a symbol missing from the unfinished suffix witnesses nonuniversality at the next length. Marking each closure in the three-state automaton and decomposing a height-H Dyck word into primitive excursions gives the stated exact matrix recursion. Eliminating the automaton states gives F₂=(1−2x+xt)/((1−x)(1−2x)) and F₃=[1+t(F₂−1)/(1−xF₂)]/(1−x), with x=ut; this simplifies to the stated numerator and denominator. F₂ yields the claimed two-point law, including the degenerate n=1 case. At u=1 the candidate denominator factors are (1−t)²(1−3t+t²), so the simple root r=(3−√5)/2 is separated and uncancelled. Subtracting its simple pole gives an analytic remainder bounded uniformly on a larger fixed circle for u near one; hence the log-mgf is n log(r(1)/r(eˢ)) plus an analytic amplitude and an exponentially small error. The pole equation there is eˢ(2r(eˢ)+r(eˢ)^(3/2))=1. At s=0 put a=2r and b=r^(3/2); a+b=1 and a+3b/2=√5/2. The first log-mgf coefficient per n is 1/(a+3b/2); the second is ab/[4(a+3b/2)³]>0. These equal the claimed constants. Taylor expansion at an imaginary argument of order n⁻¹/² gives the normal limit; the analytic amplitude cancels at s=0 and adds only o(1) at that scale. A separate exhaustive direct-subsequence check matched all coefficients for H=1,2,3 and n≤8; for H=3,n=8 it gives {5:50,6:432,7:127,8:1}.

## originality

FAIL

Earlier catalogue records already give the full marked height-three generating function, the exact height-two census, and the deterministic height-one case. The earlier height-three record does not state the positive exact variance or CLT, but its identical bivariate rational function has the same isolated simple moving pole. Standard quasi-powers, with two derivatives of precisely the same denominator, implies the explicit refinement without any new enumeration or structural estimate.

## value

FAIL

The depth at which linear variance appears is a natural question. In this record the two exact laws that settle it are already known, and the only remaining refinement is the usual curvature and quasi-power limit at an already identified simple dominant pole. No new depth classification, probabilistic mechanism, or nonroutine estimate survives as a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
