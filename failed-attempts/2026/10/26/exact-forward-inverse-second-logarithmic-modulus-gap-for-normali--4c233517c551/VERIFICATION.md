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

For p=1+zf''/f', expanding gives p1=2a2 and p2=6a3-4a2^2. Thus, writing the Schwarz jet as u z+v z², one obtains a2=u and a3=u²+v/3. Expanding the local inverse and both logarithms yields the symmetric pair A±B, with A=u²/4 and B=v/6. Schwarz–Pick gives |v|≤1−|u|². For |u|<1 every such v occurs via the disk automorphism with input v z/(1−|u|²), multiplied by z; integrating the convexity equation realizes the map. The two reverse triangle bounds give 2 min(|A|,|B|), and moving B along the diameter through A gives every intermediate signed value. At u=0 or |u|=1 the signed difference is identically zero. The branches intersect at r=2/5, where equality in the bound requires B=±A and |v|=1−r. Schwarz–Pick equality then gives precisely the displayed rational functions and the stated signs. The final sentence about vanishing is correct as a distinction between the two listed extremizer types, not as a sufficient condition by itself: u=1/2 and v=3/8 give (1/8,0). No global inverse extension is used.

## originality

FAIL

The named same-index statistic is different from the successive-index statistics in the cited literature, but the full frozen answer is a direct corollary of an already parameterized coefficient body, including its boundary uniqueness. Ali–Raza–Raza's Lemma 2.1 and (2.1), (2.5), together with their identities for direct and inverse logarithmic coefficients, give the two observable values on the same parameter disk. The remaining work is two reverse triangle inequalities, their simultaneous realization on a diameter, and intersection of two affine branches. Their boundary formula gives exactly the reported equality family, so that family does not supply a distinct remainder. This is a judgment of mathematical implication, not a claim that a predecessor printed the number 1/5 for this named statistic.

## value

FAIL

The direct-versus-inverse question is natural, but for order two the exact joint region and its boundary functions are already known. The reported kink and extremizers come from evaluating a distance difference on a diameter of this known disk; there is no independent structural or extremal step left that meets the value threshold for a narrow exact invariant. No surviving claim is identified for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
