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

With 0<γ<1 all single-spin flips have positive rates, hence the finite ring has one stationary law. For distinct i,j, stationarity of σ_iσ_j gives a decay term −2C_ij and the two neighbor-source terms γ_i/2 and γ_j/2. Thus distinct hot spins have zero pair correlation, and with i hot and j cold the remaining factor is exactly α=γ/4. For each cold run of length l the two Dirichlet endpoints are distinct hot sites, yielding boundary values (1,0), (0,1) or (0,0). With (1,0), writing λ=(1−√(1−4α²))/(2α), the unique interior solution is C_j=(λ^j−λ^(2l+2−j))/(1−λ^(2l+2)), as checked by the recurrence and endpoints. At j=1 this gives a_l=λ(1−λ^(2l))/(1−λ^(2l+2)), equivalently the stated continued fraction from elimination. At a hot site the mean energy influx is J times the sum of the two correlations: its rate is 1/2 and the energy change is 2Jσ_i(σ_{i−1}+σ_{i+1}). There are two boundary contributions Ja_l per run and none from hot–hot pairs. Energy balance and zero hot inverse temperature give the stated outflux and entropy production. The map x↦α/(1−αx) is increasing with derivative strictly between zero and one on [0,λ], and its iterates from zero have strictly decreasing positive increments. Therefore a split replacing l by p,l−p raises the sum, and a one-unit transfer from a length at least two larger to a shorter one raises the sum. Every positive length composition with r≤min(h,c) can be realized by r nonempty hot gaps. The unique minimizing run count is one; the maximizing count and balanced lengths, and the c=1 and h=c cases, follow. The strict split comparison is a refinement of run lengths; it does not order a move that also merges other runs. A fresh rational full-generator solution for N=4, h=c=2, γ=3/5 gave Q_h/J=120/391 for one cold block and 3/5 for alternation, as predicted. The frozen verifier was inspected, not executed; the all-size result rests on the argument, not those checks.

## originality

PASS

Credit is for the arbitrary-placement finite-ring run decomposition and strict sharp rearrangement law at fixed bath counts. The stationary two-point equation, heat convention and the alternating case have prior counterparts. No inspected primary or indexed result covers the full fragmentation law.

## value

PASS

This is an arbitrary-arrangement theorem on a studied nonequilibrium model, not another calculation for one selected arrangement. Infinite-hot decorrelation makes the total heat depend only on cold-run lengths even in a finite correlated spin system. The reduction explains the exact effect of splitting, and yields sharp design rules with equality cases at each bath count. Neither finite-hot baths nor arbitrary redistributions with a simultaneous merge are included in the strict split assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
