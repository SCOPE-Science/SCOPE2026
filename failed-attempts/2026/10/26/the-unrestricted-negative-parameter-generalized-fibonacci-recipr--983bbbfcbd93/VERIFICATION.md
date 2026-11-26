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

The domain gives s≥3, λ=√(s²−4t)≥s−2≥1, and roots α≥2, 0<β≤1. Put A=α^r and B=β^r. Binet gives a positive convergent tail and geometric comparator G=λ A^(1−n)/(A−1)<S. The exact summand difference divided by λ is (B/A²)^k divided by 1−(B/A)^k. Geometrically summing after bounding the denominator below by 1−B/A, and using G^(-1)−S^(-1)=(S−G)/(GS)<(S−G)/G², gives the source's inequality (1). One can check the uniform unit bound even without splitting off (3,2): in its bracket, h(B)/B=(A−1)² A/[(A²−B)(A−B)] ≤ A/(A+1)<1, so 1−B+h(B)<1. Thus 0<D−S^(-1)< B^(n−1)/λ ≤1 for D=U_(rn)−U_(r(n−1)). Taking the floor is valid since D is integral, including D=1. At the excluded double-root pair U_j=j and the positive tail diverges, so the exclusion is substantive.

## originality

FAIL

The TrureTuring public research dossier presents the identical first-clause theorem, including convergence and all symbolic strides and parameters, and supplies a distinct reconstructible Cassini/telescoping argument, not merely a search snippet or another copy of the conjecture. This establishes exact equivalent proof coverage in the inspected evidence. The dossier has no visible release date in the passages read, so this is not a finding that its proof came first. Independently, Cui et al. cover all t=1 and Park covers a large-parameter regime. Those two partial overlaps alone would not warrant this FAIL.

## value

PASS

The scientific question is an exact named conjectural identity on a natural two-parameter recurrence family and is substantively interesting regardless of priority. The proof supplies a different quantitative and uniform explanation rather than a re-tabulation: when β<1 the positive distance from the integer endpoint decays geometrically in the cutoff, and the proof also controls β=1 and the corner λ=1. This assesses mathematical utility of the argument, not novelty for the already covered floor statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
