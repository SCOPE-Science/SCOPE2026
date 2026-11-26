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

The endpoint symbols fix the transition-count imbalance and the number of runs of each symbol. Distributing 00 and 11 counts as extra run lengths gives the two stars-and-bars formulas, with two start-symbol terms in the equal positive-transition case and only one in the imbalanced case. Zero transitions give only constant singleton fibers. At a fixed balanced t=k+1, set L=a+k, R=d+k. For k>0 and R>=L+2, the proposed product ratio for moving one unit from R to L exceeds one since its numerator minus denominator is k(R-L-1)>0; for k=0 all splits are equal. The ratio for adjacent k has sign relative to one given by uv-2-(u+v+3)k, so scanning the allowed interval yields the stated rounded threshold and integral tie, including u=0. For the imbalanced t>=2 case with a>=t-1, the comparison converting one 00 to a missing transition has ratio ma/[t(a+t-1)]>=1. Equality requires t=2,a=1,d=0, which gives size two below m=4. For a<=t-2 the comparison reducing the excess transition and adding a 00 has ratio with positive numerator excess 2(t-1)^2+d(t-2-a); t=1 gives a singleton. Thus both global exclusion and all equality cases follow. An independent bounded enumeration encoded each n-bit word as an integer, counted adjacent two-bit blocks over shifts 0 through m-1 and compared every resulting profile to the rounded-threshold formula and equality predicate for n=3 through 18. It gave the stated four maximizers at n=10 (size 54) and n=18 (size 8330). This corroborates the proof only finitely.

## originality

FAIL

The October 13 exact worst-case ambiguity theorem (5122acc1b9bd) already gives the same all-length maximum and all equality profiles in the same binary, linear, free-endpoint setting. The rational-threshold optimizer is a reparameterization of that theorem's mod-four rule, not a distinct refinement.

## value

FAIL

Worst-case ambiguity is a natural and useful reconstruction measure, but the frozen exact value, extremizers and sample sizes are already supplied by the earlier solution. Reexpressing its modular optimizer as a ceiling of a rational threshold and repeating finite checks does not leave a separately useful new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
