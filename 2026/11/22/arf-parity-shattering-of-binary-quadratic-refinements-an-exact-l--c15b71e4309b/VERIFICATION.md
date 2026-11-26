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

Differences of refinements of the fixed polar form are linear and identify uniquely with B(a,-). Translating the Gauss sum of Q_0 gives 2^m times (-1)^Q_0(a), so Q_0(a) is precisely the parity constraint. On a dependent support, the evaluation trace is an affine translate of a proper subspace and cannot be surjective. On an independent support the fibers for all traces are the cosets of K=span(S)^perp. Their intrinsic polar form is B restricted to K; if nonzero, no fiber is constant and both parities occur in every fiber. For isotropic K of dimension r, linearity of Q_0 on K makes the equation B(a,k)=Q_0(k) for all k in K solvable, with solutions an affine translate of K^perp. It yields exactly 2^[2(m-r)] constant fibers. The elementary signed Gauss sum of Q_0 is 2^m, and each nonconstant fiber contributes zero. If r<m and all constant fibers had one parity their sum would have magnitude 2^(2m-r)>2^m, a contradiction; hence both parities miss some trace. If r=m the sole constant fiber must have even parity to give the positive Gauss sum, and the even class shatters. This independently verifies the Lagrangian exception without requiring a quotient-Arf identity. The k-dimensional spans correspond bijectively to the (2m-k)-dimensional kernels; each span gives exactly |GL(k,2)|/k! unordered bases. Counting isotropic frames by choosing each next vector in the current perpendicular outside its span gives the stated product and A_(m,m)=product(2^i+1). At m=3 the parity difference is 28*135=3780 at degree 3 only, as displayed. For m>=2 a symplectic two-plane kernel achieves 2m-2; kernels of dimension zero or one cannot give larger supports, and at m=1 the formula gives dimensions one and zero. The empty support is counted in both classes. Replay: RESULT.md lines 45–68 and the signed-coset calculation above. Both verifier sources were inspected but not run; their finite sample and exhaustive low-dimension tests are supplementary to the general argument.

## originality

PASS

The distinct contribution is the all-support classification, exact enumerator and degree-m parity defect for incidence with Arf-filtered refinements of one polar form. The quadratic-form identities and symplectic frame counts are classical; the VC dimension alone is not the originality basis. The close same-day Lagrangian incidence theorem uses a materially different concept class and gives an inequivalent criterion. No inspected source was found whose actual statements give this support polynomial or classification, including under the affine projection reformulation.

## value

PASS

For this fixed symplectic incidence family the two parities have the same VC dimension in all ranks at least two, so dimension alone cannot detect their discrepancy. The exact polynomial and the underlying if-and-only-if geometry identify precisely which query supports are lost: the independent bases with Lagrangian kernel, in one degree only. This is a meaningful complete finite-geometric invariant, not a recomputation of the number of quadratic forms or isotropic subspaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
