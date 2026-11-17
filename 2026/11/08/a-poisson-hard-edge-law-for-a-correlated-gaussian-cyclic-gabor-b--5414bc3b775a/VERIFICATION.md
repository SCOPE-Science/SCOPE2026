---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Orthogonality of all even modulations on length N=2p gives S(i,j)=p 1_{i congruent j mod p} sum_{k=0,1}g_{i-k}conj(g_{j-k}), yielding p Hermitian 2x2 blocks W_j=[a_j,b_j][a_j,b_j]^* with independent a_j ~CN(0,I/2), b_j=a_{j-1} except b_0=U a_{p-1}. Independently constructed full Gabor matrix and p blocks for p=3,5,7, with maximum entry differences <3e-15. Square two-by-two complex Wishart has exact single-block survival P(L>x)=e^{-4x}, and distinct nonadjacent blocks are independent. Adjacent rare-event joint bound follows from determinant s|w|^2 and trace, yielding P(L_j<=eps,L_{j+1}<=eps)=O(eps^2(1+|log eps|)) after integrating Gamma(shape 2,rate 2) shared squared norm. Dependency-graph Chen–Stein hence TV(Pois(4t)) error O_t(log p/p) for fixed t; no-rare-event probability gives P(pA_p>t)->e^{-4t}. Independent nonadjacent matching gives uniform e^{-4u/3} tail majorant for p>=3, justifying all positive moments Gamma(r+1)/4^r. These arguments address all p>=3, include cyclic seam and distinguish minimum squared frame eigenvalue from singular value; numeric checks support only finite algebra.

## originality

PASS

Best-of-knowledge the Gaussian-window random lower-frame-bound Poisson hard edge at p scaling and rate four, with rare-neighbor bound and all positive moments, is not published by the identified same-mask log-determinant theorem or the phase-only exact independent-fiber Weibull theorem. The general subgroup block-equivalence and single-block Wishart survival are known inputs, but do not by themselves establish absence of clustering in the cyclic shared-Gaussian blocks. The closest external 2026 block-equivalence paper could be read only at abstract level due to authorized VPN disconnection; this remains an explicit historical-originality risk, not an automatic fail.

## value

PASS

The optimal lower frame bound controls worst-case stability of an exactly critically sampled Gabor basis; a precise exponential hard edge is a natural risk invariant and quantitatively different from a determinant CLT or phase-only frame law. Handling one-dependent Gaussian spectral fibers and proving a sharp Poisson error controls the dependence mechanism rather than merely recomputing a textbook 2x2 Wishart distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
