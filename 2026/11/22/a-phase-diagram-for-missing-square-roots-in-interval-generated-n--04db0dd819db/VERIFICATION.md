---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For m=qa+r, a representation using s summands has s≤q and r≤ks≤kq; conversely the offset r can be distributed over q summands whenever r≤kq. Thus the missing squares lie in the disjoint open blocks (q(a+k),(q+1)a) for qk<a. Their integer root count is exactly isqrt((q+1)a−1)−isqrt(q(a+k)); neither perfect-square endpoint is included. Each root interval costs at most one in rounding, giving (3), also when a/k is integral or k≥a. In F the disappearing q=j term at t=1/j vanishes continuously but its derivative on the left is −j/(2√(j+1)), giving the claimed positive jump. Writing J=floor(1/t), ∑_{q=1}^J√q=(2/3)J^(3/2)+O(√J) and J=t⁻¹+O(1) give F(t)=2/(3√t)+O(√t). For a cutoff N=floor(sa/√k), the last quotient J=floor(N²/a)=s²/t+O(1) may be counted in full at a root-count error O(√a+1). Telescoping the lengths gives the leading contributions (a/√k)s and −(a/√k)s³/3, with errors O(√a+a/k), uniformly including s=0,1. Finally every missing root satisfies n²<a ceil(a/k), so its rescaled location is at most √(1+k/a). The uniform count and vanishing exterior range, together with the total count asymptotic, give weak convergence with mass 2/3 under the stated normalization. I inspected the supporting checker and used the proof, not execution of that code or its sampled inequalities, for the infinite claims.

## originality

PASS

The membership criterion and the ordinary-gap enumeration are prior work, and the elementary exact square-root count alone is covered as a direct extraction. The part that survives is the two-scale asymptotic classification: the full phase curve and its infinite derivative-jump set, and the uniform rescaled root profile when k grows sublinearly. The closest fixed-width profile gives the same density but cannot be specialized to this moving-width family. No inspected result covers the asymptotic claim at those quantifiers.

## value

PASS

Counting all missing-square roots refines the natural maximum-gap statistic in a distinct way. The reciprocal-width corners identify every change in the active quotient blocks, and the mesoscopic law controls the entire cumulative root population rather than simply a maximum or total. These are useful scaling statements at natural, different generator widths, not a claim of significance for a floor-sum restatement by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
