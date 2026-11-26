---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The generator recursion gives the displayed triangular matrix and satisfies the identity on all basis products, including [e_n,e_1]=0. For a_1=0 the first nonzero shift J^r times an invertible polynomial in J has rank n−r. For a_1≠0 one can independently check the obstruction by representing D/a_1 as E+g on xF_q[x]/(x^{2p+1}), where E=x d/dx and g=Σ(a_{r+1}/a_1)x^r acts by multiplication. Conjugating by a unit h of degree <p with h(0)=1 adds Eh/h to g; degrees 1 to p−1 can be killed successively since each of those degrees is invertible. Factoring h into linear factors over an algebraic closure shows that the x^p coefficient of Eh/h is the pth power of its x coefficient, via the geometric series for each factor's logarithmic derivative. Thus the only coupling in the two zero-diagonal positions is the x^p coefficient a_{p+1}/a_1−(a_2/a_1)^p. In detail, rows below degree p force all earlier coordinates to zero, and the rows between p and 2p then have nonzero diagonal with no contribution from coordinate p. The kernel dimension is 2 exactly on the stated graph and 1 off it. The graph has (q−1)q^{2p−2} points and its complement in the open set (q−1)^2q^{2p−2}; adding the shift stratum gives exactly the census. In smaller dimensions the open stratum has zero or one zero-diagonal position, with constant rank. This works at p=2 as well as odd p and over characteristic-p extensions.

## originality

FAIL

Two earlier catalogue records give general finite-field nullity results. The earlier Frobenius-resonance equation specializes to the same hypersurface on a_1≠0 and immediately gives its graph geometry. The claimed sharp first dimension and complete rank census are likewise specializations, not a surviving distinct finding.

## value

FAIL

The first nonconstant modular rank would be a natural boundary and the geometric interpretation is apt. Here the exact answer already follows by setting ⌊n/p⌋=2 in a known complete test, and the geometry is the immediate coordinate-graph description of one solved equation. There is no additional geometric invariant or rank result not mechanically implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
