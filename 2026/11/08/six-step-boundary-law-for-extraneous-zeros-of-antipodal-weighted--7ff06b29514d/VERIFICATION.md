---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The normalized RKHS kernel has K_0=1 and K_r+K_-r takes the same value D=(1-r²)^(-beta)+(1+r²)^(-beta) at r and -r; therefore 1-(K_r+K_-r)/D is the exact nonzero orthogonal projection of 1 onto the two-evaluation nullspace, with F(0)>0. Clearing denominators at t=rz yields an even polynomial P=C(1-t²)^beta-(1+t)^beta-(1-t)^beta of degree 2 beta and no pole roots at t=±1. Multiplying by eps^beta as eps=1-r²→0 and isolating near t=±1 gives precisely beta roots in each cluster by root continuity and degree. At t=1-eps v, the analytic equation v^(-beta)-1+eps^beta[(2-eps v)^(-beta)-(2-eps)^(-beta)]=0 has exactly beta simple roots v_j=omega_j+O_beta(eps^(beta+1)) by implicit-function theory at beta-th roots of unity, so t_j=1-eps omega_j+O_beta(eps^(beta+2)); evenness yields the opposite cluster. Testing the true domain |t|<r, |t_j|²-r²=eps(1-2cos(2pi j/beta))+eps²+O_beta(eps^(beta+2)). At 6|beta the tangent index has strictly positive eps², hence is EXCLUDED. There are 2ceil(beta/6)-1 roots per cluster and N=4ceil(beta/6)-2 disk roots; subtracting exactly two prescribed simple real roots leaves the quartet-forming E=4(ceil(beta/6)-1). Beta=1 and beta multiples of 6 are handled without boundary misclassification. No uniformity as beta→infinity. Independent exact rational checks verified 504 projection-polynomial assertions for beta 1..28 at three eps values; a separate boundary contour winding computation verified N for beta 1..48 at eps=.004,.012 (96 cases), with every sampled phase increment under π. Those finite tests corroborate, rather than prove, the all-beta result. The actual frozen Git tree was reconstructed from the seven actual source blob identifiers.

## originality

PASS

Best-of-knowledge PASS for the precise all-integer, two-antipodal-site, boundary-near total/extraneous zero count and the excluding tangent-branch law, rather than for the known one-site root-of-unity criterion. Hedenmalm–Zhu Proposition 3 explicitly supplies the same beta>6 one-point threshold and angular inequality; Felder–Le supplies general multi-site projection theory; Weir supplies all-zero-set zero-freeness for alpha<=1. These cover ingredients and low-beta subcases but not, as quantified statements, the full two-cluster classification for A={-r,r}, including exact count, simplicity and nonreal quartet geometry. The October 11 finite-zero-set existential theorem has a different set quantifier and real extras; the October 25 hyperplane ball result has a different RKHS kernel. A same-date public copy of the target is the target itself, not independent precedence. Relevant original full texts/sections were read as detailed below; a 2026 relevant arXiv preprint was inaccessible, named as residual risk rather than failed as a shortcut. Historical priority remains qualified.

## value

PASS

Canonical zero-based extremals can acquire unintended roots, changing how a prescribed zero set identifies a shift-invariant subspace. Two distinct antipodal evaluation sites form the smallest symmetric multi-site geometry beyond the classical one-site framework. For this natural object, the theorem gives the COMPLETE near-boundary disk zero count at every integer kernel power, identifies exactly which exponents create new quartets and settles the delicate exponents divisible by six via an O(eps²) sign not determined by first-order root location. This is a motivated sharp invariant and boundary law rather than a parameter renaming or a numerical curiosity. Its mathematical worth is modest relative to full canonical-divisor theory, and no classification for arbitrary point sets/radii is claimed; independent exact finite classification is still a useful structural benchmark for later multi-point zero theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
