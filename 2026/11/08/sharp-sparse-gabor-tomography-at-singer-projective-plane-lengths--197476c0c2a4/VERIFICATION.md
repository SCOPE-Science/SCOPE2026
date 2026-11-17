---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: Complete Gabor-projector lifting diagonalizes on the unit Hilbert–Schmidt Weyl basis with singular values √N|A_g(u,v)|, multiplicity one per (u,v). A support S of size s has rank at most N|S−S|≤N[1+s(s−1)], so at N=q²+q+1 the minimal full-rank support is at least r=q+1. At support r, equality S−S=Z_N forces each ordered nonzero difference to appear once, precisely a Singer-type (N,r,1) difference set. Its cyclic trace-zero construction exists at all prime-power q. For flat amplitudes, every u≠0 has ambiguity magnitude 1/r, while u=0 has magnitudes 1 and √q/r, establishing the full claimed spectral multiplicities and maximin √N/r. For nonflat amplitudes, min pair product≤(∏ a_x)^{2/r}≤1/r, with equality only all |g_x|²=1/r, proving rigidity. Deleting one Singer point gives s=q distinct nonzero differences, and at zero shift the nontrivial Fourier coefficients are nonzero since |∑_{D}χ|=√q>1=|χ(d)|, attaining rank N(1+q(q−1)) and nullity 2qN. Explicit complex ambiguity checks at Singer q=2,3 agree, not an all-q experiment.

## originality

PASS

Best-of-knowledge original sharp maximin/optimizer-rigidity and one-site-deletion rank theorem: related 2015/2021 primary results already establish Gabor ambiguity diagonalization and difference-set sufficiency but not full all-complex minimal-support stability maximin or the exact deletion-rank optimization; Resultary related Gabor results use different families or multiwindow data.

## value

PASS

PASS: Complete linear matrix tomography with the smallest number of nonzero window coordinates is a motivated sparse measurement-design problem. The exact worst-direction stability/conditioning optimum and classification of all optimizing windows over arbitrary complex coefficients, plus sharp one-coordinate deletion rank, give nontrivial design limits and sensitivity. The Singer incidence structure and Weyl spectrum are classical inputs, but obtaining a quantitative maximin and rigidity under a support budget is a natural precise invariant and is not shown identical to a checked earlier theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
