---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

With e_j=x*-x_j, the retained ell-1 recent search directions form an orthogonal subspace W_j with dim min(j,ell-1), and exact line search implies e_j is in W_j^perp even as older directions expire. A^T s_j/sqrt(lambda) is fresh iid N(0,I_d); the source gradient d_j=lambda<z_j,e_j>z_j, and after Gram-Schmidt the nonzero update is exact orthogonal projection along v_j=(I-P_Wj)z_j. Conditional on all past, v_j is isotropic Gaussian in m_j=d-min(j,ell-1) dimensions, and R_j=1-(<e_j,v_j>/(||e_j|| ||v_j||))^2 has Beta((m_j-1)/2,1/2) distribution. Since this conditional law is deterministic, factors are mutually independent; m_j=1 gives final exact zero, while ell<d keeps m>=2 and no finite termination. Mellin moments are products and finite iff q>-(d-ell)/2 once steady state entered; E R=(m-1)/m telescopes and strong law for persistent iid logs yields digamma exponent. Independent Gaussian simulation d=6, ell=3, 7000 trajectories gave step means 0.8358,0.79784,0.74969,0.75263,0.74904 versus theory 5/6,4/5,3/4,3/4,3/4. No inference of all-d correctness from sample.

## originality

PASS

PASS, best of knowledge: The 2025 Sun–Han–Xie original Algorithm 3 defines arbitrary fixed memory ell but provides expected convergence bounds and known full-memory finite termination, not exact conditional independence and beta product. A distinct November 2 2026 Resultary theorem proves the same beta law and exponent for RCGLS, which agrees with ell=2 (one past search direction) ONLY. The submitted theorem includes every sliding-window ell>=3, varying transient dimensions, exact full-memory termination threshold and inverse-error integrability, none of which the ell=2 theorem implies by parameter renaming. Direct primary Algorithm 3 text was matched to the projection update.

## value

PASS

PASS: The exact distributional dynamics of a specified adaptive randomized solver is a substantive quantitative result beyond mean-square rates: it gives all moments, sharp rare-small-error inverse-moment cutoffs, and almost-sure rates for arbitrary memory lengths. The sliding orthogonal-window invariant is needed to justify the independence despite adaptive retained directions; the full-memory finite termination is credited as known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
