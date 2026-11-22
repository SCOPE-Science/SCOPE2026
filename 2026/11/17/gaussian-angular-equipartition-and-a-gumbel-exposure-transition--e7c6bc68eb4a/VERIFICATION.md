---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For every integer n>=2 and 1<t<n, the support h(g)=max(sum |g_i|,t max|g_i|) proves all 2^n corners and 2n coordinate apices are exposed; no other hull vertices exist. Gaussian direction signs and permutation symmetries give apex total p=Pr(tM>S) and individual normal angles p/(2n) and (1-p)/2^n. The finite multiple integral conditions on the unique absolute maximum, and collision C=p^2/(2n)+(1-p)^2/2^n. The random ratio S/M is atomless with positive probability in every open interval of (1,n), so p strictly increases 0 to1; strict convexity in p gives exactly one equipartition t* and absolute minimum 1/(2^n+2n). For n=2 angular integration gives p=4 arctan(t-1)/π and t*=sqrt2. For fixed s and b_n defined by nP(|G|>b_n)=1, classical half-normal extreme-value normalization yields b_n(M-b_n)=>Gumbel and b_n^2(S/(μn)-1)=o_P(1); with t_n(s)=μn/b_n(1+s/b_n^2), p=>1-exp(-e^s) and nC=>p^2/2. Reconstructed these hypotheses and scale; independently sampled Gaussian exposures at n=2 t=sqrt2 and n=3,5 plus checked support endpoints, while source checker.py was inspected. Experiments are not infinite proofs.

## originality

PASS

Best-of-knowledge: the two-orbit angular law, uniquely balanced cone angles and sharp combined Gumbel/collision window for the exact primal hull are not implied by examined isotropic-volume optimization or unconditional reflexive-combinatorial classifications. Important exact equivalence to a previously studied top-coordinate norm-ball family is openly credited.

## value

PASS

The spherical angular distribution and exact equal-cone parameter of a natural cube–crosspolytope interpolation quantify probabilistic vertex accessibility, while the Gumbel transition separates exponentially many cube vertices from only linearly many apices in collision probability. This is a motivated geometric-probabilistic classification with natural all-dimensional limits; neither correct algebra nor the regular-octagon example alone drives the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
