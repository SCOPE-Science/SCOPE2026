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

The simultaneous-rung configurations contribute (zB)^2, giving Z=I_n^2+(a−1)(zB)^2 with B=I_{v−2}I_{n−v−1}. For a<1 factor using √(1−a); the factors are path polynomials with marked vertex weights 1±√(1−a). The symmetric weighted adjacency matrix on P_{n+1} gives their negative roots by pairing ± eigenvalues. For 0<a<1 the tridiagonal matrix has positive off-diagonals and simple spectrum; at a=0 splitting at a zero edge still gives only negative finite zeros, with no degree or multiplicity claim needed. For a>1 the sum of squares on the real axis vanishes only at a shared root of I_n and B (z=0 is excluded), and the squared simple I_n derivative gives exactly multiplicity two. Path angles jπ/(n+2) lie below π/2, so equality with a subpath root is exactly divisibility of jv or j(v+1) by n+2. The two classes are disjoint and a gcd d contributes floor((d−1)/2) indices. At a=1 all m roots are double. For a>0 every pair of maximum independent sets has positive weight, so degree 2m holds even if no maximum set contains v; this clarifies the use of 'maximal' in the proof. At an unprotected root use the analytic implicit function theorem on the separate factors with parameter τ=√(1−a) or i√(a−1); the derivative in τ is ∓rB(r)/I_n′(r). Independent example: n=4,v=2 gives Z=(1+z)^2[(1+3z)^2+(a−1)z^2], with exactly the protected double root −1 for a>1. The frozen verifier was read, not executed; its finite enumeration and distinct-root counts are corroborative, not the all-n or multiplicity proof.

## originality

PASS

The scoped contribution is the interior-site arithmetic survival and multiplicity census at all attractive strengths. The endpoint case and its opening law are exactly covered by the distinct centered-bond record and are not credited separately; the matching real-rootedness ingredient is classical. No inspected result covered the interior census, including the equivalent formulation with a conjugate-complex weight at an interior matching edge.

## value

PASS

The all-site gcd criterion identifies when an attractive local perturbation leaves some fugacity zeros exactly protected and when all disappear. The exact locations, multiplicities and parameter independence give usable finite-volume information for a natural two-replica model, including interior behavior qualitatively absent from the endpoint case. No thermodynamic or general multirung conclusion is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
