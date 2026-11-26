---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Vandermonde gives the binomial-square form, and coefficientwise Lucas factorization with Frobenius shows a ternary digit 1 forces D_n(1)=0 mod 3. For the remaining even n=2m, the linear coefficient 2m(2m+1) is divisible by 3, so multiples of 3 give 1 mod 9; Legendre reflection gives the class -1. For z=1 mod 3, P_{2m}(1+2z) has no odd powers and coefficients in Z_(3), so only the constant term A_m=(-1)^m 4^(-m) binom(2m,m) survives. In (1+T)^(3a) modulo nine the terms linear in 3T(1+T) have degree 1 or 2 mod 3, proving binom(3a,3b)=binom(a,b) mod 9. Together with the exact adjoining-factor ratio this gives increments q and 1+2q mod 3 in (A_m-1)/3 when adjoining a low digit 0 or 1 to q respectively, exactly the recursion for c. For the count, at a primitive cube root zeta the two-state weight transfer on terminal digit has columns (1,zeta^2) and (1,1). The first-digit vector (1,zeta) is a (1+zeta)-eigenvector, so the complete nontrivial Fourier moment at length r is (1+zeta)^r. The trivial moment is 2^r; averaging these and the conjugate yields exactly the given six-periodic defect, including r=0. An independent replay (python3 /workspace/checks/delannoy.py) uses direct binomial sums for all nine residues through n<3^5 and exact integer cyclotomic arithmetic for word counts through r=12. This is corroboration; the algebra proves both unbounded assertions. The supplied checker was inspected but not executed.

## originality

PASS

The first-power digit restriction is exactly prior and not counted as new. The bounded search found general automaticity, prime-level digit results, and powerful valuations/range results at one argument, but no inspected earlier theorem giving the prime-square residue criterion with its universal-argument reduction or the exact enumeration. Known prime-power binomial computations furnish tools for the constant term; this is not a claim of new binomial scaling or new general automaticity.

## value

PASS

Lifting the known all-argument fixed-divisor problem from three to nine is a natural first prime-square test. The formerly independent digit restrictions become a coupled language, simultaneously controlling all argument classes. The exact six-periodic discrepancy in the block counts is additional structural information, not a pointwise congruence experiment or a restatement of automaticity. No stronger claim about arbitrary primes or 27 is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
