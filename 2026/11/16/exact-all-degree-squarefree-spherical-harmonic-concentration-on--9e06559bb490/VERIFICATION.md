---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Independent centered Gaussian normalization gives conditional sign correlation rho_m(d,s)=C(d,d-s)^-1 sum_j (-1)^j C(m,j)C(d-m,d-s-j). The normalized monomials x_S are orthonormal on S^(d-1); off-diagonal restriction entries are w(2/pi)^(k-r)rho_(2(k-r)), where r=|S∩T|, w=2^-d C(d,s). Binomial inversion expands this matrix in W_l W_l^T inclusion products, whose classical Johnson eigenvalues on V_i are C(k-i,l-i)C(d-l-i,k-l), multiplicities C(d,i)-C(d,i-1). The proof accounts for every C(d,k) dimension and gives a strict 0<lambda<1 because nonzero homogeneous polynomials cannot vanish on open subsets of region/complement. rho2=(t²-d)/(d(d-1)) with t=2s-d gives k1 isotropy iff t²=d. For k2, rho4|_(t²=d)=-2/((d-2)(d-3)) excludes isotropy, and Kneser pair-disjoint adjacency gives the displayed three levels. Independent full-matrix eigenvalue comparisons over d4..9 supported these exact identities. This proof does NOT claim all pure harmonics, only the squarefree subspace.

## originality

PASS

The Johnson inclusion eigenvalues and Krawtchouk sign-shell correlation are established prior combinatorial facts, and the spherical Slepian framework is established. The continuous sign-count-region compression requires integrating Gaussian absolute moments, introducing (2/pi)^h factors and strict positive definiteness, and leads to distinct isotropy/obstruction laws. Compared published discrete Hamming-shell and continuous hemisphere work: neither has the same operator or proves the all-(d,k,s) assembled squarefree spectrum. Best-knowledge original assembled result; specialized earlier continuous sphere-plus-Johnson reduction remains a risk.

## value

PASS

Fixed-coordinate-sign-count sectors are natural observation regions of the sphere, and squarefree harmonic monomials form a canonical symmetric degree-k subspace. Exact all-degree concentration spectra and sharp leakage quantify observability; the unexpected square-dimension linear isotropy and its quadratic obstruction are nontrivial classification boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
