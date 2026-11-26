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

A finite increasing partial injection is nilpotent iff it has no fixed point: any nonempty cycle is a permutation of its support and must preserve its order, so has length one. For equal-size ordered domain and image sets a fixed point is exactly a matching ordered coordinate. Marking such coincidences splits the indicator strings into balanced pieces and gives the stated inclusion–exclusion generating function. Write D=(1−a x)(1−b x), a=(1+√y)^2, b=(1−√y)^2 and ρ=1/a. For fixed y>0 and |x|≤ρ except x=ρ, both factors have positive real part and the selected square root has positive real part. If Re x≥0 this prevents a denominator zero; if Re x<0, |√D|≥1>|xy|, also preventing one. At x=ρ the denominator is ρy and the square-root coefficient is nonzero. The other radical zero is outside the disk and nonvanishing on compact parts of a slit neighborhood persists locally under complex y-perturbation after scaling x by ρ(y); this justifies the locally uniform transfer. The resulting log-mgf limit is 2 log((1+e^{t/2})/2). Its Legendre transform gives the displayed binary-entropy rate; differentiability gives the LDP, with endpoint lower bounds obtained by interior approximation and continuity. Uniform transfer near y=1 applied at t√(8/n) in the exponential tilt gives a centered standard normal mgf limit. Independent replay matched all rank profiles for n=0,…,10, including [1,12,14,2,0] at n=4; these checks do not prove the limits.

## originality

FAIL

Bender–Lawler–Pemantle–Wilf (2004), equation (1.4), gives the exact joint size/part-count enumerator of the identical rank-marked objects under a parameter-preserving bijection. For a map on [n] of rank k, use its ordered domain and image as the cut positions in two compositions of n+1 into k+1 positive parts. A matching cut with the same index is a fixed point, so nilpotence is precisely irreducibility of the ordered pair in their definition. Their generating function is exactly xy times the frozen G(x,y), not merely the unrefined count at y=1. The two stated limits follow by standard transfer and cumulant arguments from this exact stronger precedent. The compared paper's normal approximation for a single composition is not itself the conditional CLT; the finding fails for demonstrated implication from the full enumerator, not because the limit wording was found verbatim or any paper was inaccessible.

## value

FAIL

The conditional rank is natural, but after identifying rank with the number of cuts in the previously enumerated composition pairs, the frozen LDP and CLT are standard one-parameter coefficient transfer and transforms of an explicit quadratic radical. There is no further new structural probabilistic conclusion, nonuniform boundary or local estimate, or application beyond these routine consequences. The finite replay and self-contained derivation have expository use but do not provide a distinct scientific advance under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
