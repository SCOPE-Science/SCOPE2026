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

Stern recursions give children L(a,b,t)=(a,a+b,t) and R(a,b,t)=(a+b,b,t+1) on primitive residue pairs times Z/h. Elementary unipotents generate SL2(Z/m), transitively on primitive pairs. The exact braid identity L R^{-1} L = R^{-1} L R^{-1} on vector coordinates has digital increments -1 versus -2; composing them supplies a pure t-translation. Thus lifted permutation action is transitive even when gcd(m,h)>1. Both moves are permutations; the directed two-move chain is irreducible and has an L-self-loop at (0,1,t), so is aperiodic. Finite Perron–Frobenius mixing yields uniform mass 1/(h J_2(m)) with exponential rate in binary depth, and binary-prefix subtree decomposition yields O(X^(1-delta)) for all X>=2. Independent bounded BFS verified full reachability for all 55 modulus pairs 2<=m<=12,2<=h<=6; this is corroboration, not proof for arbitrary m,h. Primitive pairs only, no nonprimitive exceptions.

## originality

PASS

Reznick gives the Stern adjacent-vector congruence marginal but no joint binary digit-weight residue independence; the independently verified braid-translation kills potential congruence/digital coupling. The broader modulo-eight Stern spectrum concerns one coordinate only, without popcount conditioning.

## value

PASS

The independence of arithmetic Stern pair residues and digital Hamming weight is a natural joint local statistic; a nontrivial lifted finite-group braid proves absence of all moduli correlations, including noncoprime m,h. Uniform power saving makes the result stronger than a simple marginal computation and useful in digital-arithmetic counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
