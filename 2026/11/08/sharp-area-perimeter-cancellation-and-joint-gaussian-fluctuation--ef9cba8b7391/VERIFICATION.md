---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Uniformly chosen m-subsets correspond, after cyclic rooting, to uniform positive integer compositions of n; exactly the law of m iid geometric(p_n=m/n) gaps conditioned on total n. Exact chord and shoelace gap expressions give D_P=π³(S_3−n)/(3n³)−π⁵(S_5−n)/(60n⁵)+O(n^-7 S_7) and 2D_P−D_A=π⁵(S_5−n)/(10n⁵)+O(n^-7 S_7). The strict inequality 0<D_A<2D_P for proper selections is equivalent to strict concavity of f(t)=4sin t−sin(2t)/2; deleting one vertex yields limiting ratio 2. Under m/n→α∈(0,1), geometric moment identities determine the stated c3,c5. Conditioning on total n removes regression on G from (G³,G⁵), producing the Schur-complement residual covariance C_ij(p), a nonsingular matrix since no nontrivial cubic/quintic combination is affine on all positive integers. Fourier local CLT supplies the two-scale joint Gaussian, not just an unconditioned CLT. Independently exhaustively checked strict finite inequality for all 3≤m<n≤9.

## originality

PASS

PASS for a fixed-retained-count (hypergeometric/composition-conditioned) two-scale covariance theorem, not for the older Bernoulli independently thinned lattice or continuous-Dirichlet polygon model. The existing Bernoulli result has random retained count and renewal covariance p E[(G^i−rho_i G)(G^j−rho_j G)], whereas fixed m conditions total gap and uses Schur complement Cov(G^i,G^j)−Cov(G^i,G)Cov(G^j,G)/Var(G). Both the finite deterministic inequality and precise conditional Gaussian joint law survive that comparison. General conditional CLT methods are standard; historical exact model coverage remains possible.

## value

PASS

The area-perimeter ratio reaches a sharp global deterministic boundary and the first nontrivial residual geometric noise is four powers below the main perimeter scale in a natural finite-population sample. Conditioning on exact sample size is common in geometric design and materially changes covariance, making the exact two-scale result useful independently of Bernoulli thinning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
