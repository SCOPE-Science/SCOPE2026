---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reconstructed the unnormalized calculation: W inverse is q^(-1) conjugate W by symmetry and perfect character orthogonality; its nonidentity corner inverts the Schur complement K=B−J. The restriction-order zeta matrix is unitriangular. Expanding the product over subsets of the common support gives H=ZDZᵀ with D blocks K tensor-powered by the support size. The singular values of W give |det K|=q^(q/2); the blocks contribute the derivative exponent, with empty support contributing zero to it. Boolean Möbius inversion and one-sided character summation give q^(-1) conjugate b(x_v,y_v) at a prescribed coordinate (also when only one label is prescribed), and −(q−1)/q at each added coordinate. Possible added supports for independent U are exactly the independent subsets of the residual graph G−N[U]; if U is not independent there is no block. This gives the exact entry formula, including empty V. The rational-root theorem rules out residual-polynomial cancellation for q>=3 since the numerator q−1 is coprime to q and would have to divide 1. On paths the recurrence at −1/2 has roots (1±i)/2 and values 2^(−m/2)sin((m+2)π/4), starting at 1 and 1/2. Multiplicativity gives the mod-four law for every compatible union, including an empty residual graph. The frozen checker’s line 78 omitted the test that the predecessor also belongs to U, so its extras predicate only admitted U contained in the first vertex, undercounting (e.g. the union consisting of the second vertex of P5). This did not affect its exact multiplication test or the theorem. The repaired checker separately compares every entry against a consecutive-occupancy and residual-run test. The repair and replay path repairs/3/path_fourier_checker.py were inspected, not executed; no numerical success is asserted.

## originality

PASS

The repaired contribution is the graph-specific inverse zero pattern, uniformly across nonbinary alphabets and with the full independent-union binary path law. The original factorization and entrywise computation substantially overlap the distinct same-day Hamming-ball record: all local block calculations and Möbius sums are already there and adapt directly to other downsets. They and the determinant identity are retained as mathematical support, not advertised as a new method or independent contribution. The checked comparisons do not give the graph-wide zero pattern or translate binary cancellations into the lengths of uncovered path components. Same-day catalogue dates were not used to dismiss the overlap or infer priority.

## value

PASS

For natural local Fourier restrictions, the zero pattern determines which inverse coefficients influence which coordinate configurations. Compatibility completely determines this pattern for every nonbinary alphabet, whereas even independent unions have an additional binary obstruction; for paths the precise obstruction is a residual run of a given length modulo four, not merely the global path order. These exact graph-dependent alternatives are useful independently of whether the supporting factorization is new, and go beyond a finite small-order calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
