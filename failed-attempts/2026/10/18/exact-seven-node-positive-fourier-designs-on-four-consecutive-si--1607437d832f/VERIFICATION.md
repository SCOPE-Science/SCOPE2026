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

The weighted Gram identity is exactly the mass-one equation and vanishing moments of orders ±1, ±2, ±3 for real weights. There is also an analytic lower bound: pad a putative smaller support to six distinct roots and form p(X)=∏(X−z_t) over those roots. Integrating X^(−3)p(X) using the moments would give its constant Laurent coefficient −e_3(z_t); the node sum is zero because p vanishes on the support. But e_3 is a sum of 20 powers of the primitive eleventh root with nonnegative integer multiplicities. If it vanished, cyclotomic irreducibility would force the 11 residue multiplicities to be equal, impossible since 11 does not divide 20. For seven nodes, multiplication of each Laurent column by z_t³ produces a Vandermonde matrix, so the solution is unique; conjugation and reversal of the moment equations show it is real. The [X³] coefficient of the Lagrange interpolant yields the frozen weight formula, with the coefficient sign (−1)³. The independently authored cyclotomic and rational-interval census checked all 462 six-node determinants and all 330 seven-node systems. Signs certified exactly 33 all-positive supports and a negative witness for each of the other 297; the least certified positive lower bound was about 0.0433507867. Canonical translation representatives were exactly the three stated, each of orbit size 11 by prime-order translation on a nonempty proper subset. For equal weights the first moment makes the indicator polynomial vanish at the primitive root, hence all indicator coefficients agree; the full support at weight 1/11 works by orthogonality. The supplied interval code was inspected, not executed; the independent calculation and analytic lower bound do not require its reported determinant margin.

## originality

FAIL

The distinct indexed Resultary entry f2acbe740312 explicitly classifies the very same weighted Gram problem, reproducing the minimum, exact count, uniqueness and three supports and adding the gap/reflection criterion. Its dihedral orbits coincide with translation orbits because the classified supports are reflection-invariant. The interpolation expression and equal-weight obstruction are standard consequences, not substantive uncovered claims. The matched entry has a later catalogue date; this establishes mathematical coverage, not priority or common provenance.

## value

FAIL

Strict weighted versus equal-weight feasibility is a natural finite Fourier sampling question, and a complete minimal-support census could be valuable if uncovered. Here the exact census and stronger structure are already in the indexed theorem. The frozen scope supplies a second enumeration of those same supports plus standard interpolation and cyclotomic deductions, not an independently useful uncovered finite invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
