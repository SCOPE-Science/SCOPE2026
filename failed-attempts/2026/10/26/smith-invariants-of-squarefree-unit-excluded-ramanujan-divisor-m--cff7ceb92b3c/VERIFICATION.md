---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The nonunit divisor zeta and Möbius factors are integral and unimodular. The omitted unit term gives a rank-one update, and Möbius inversion on the nonunit index set transforms the matrix to B=D+1u^T with D=diag(d) and u_d=mu(d). Each prime of squarefree n occurs in h=2^(r-1) of those d, so the determinant lemma gives det B=n^(h-1) phi(n). For primes not dividing n, the invertible diagonal plus one rank-one update has nullity at most one. For p dividing n, let T be the h indices divisible by p. The right and left mod-p kernels both vanish off T and are respectively u_T-orthogonal and 1_T-orthogonal hyperplanes. The divided pairing y^T B x/p mod p is well-defined on these kernels; Smith reduction shows its rank counts exactly the p-exponents equal to one. Choose integer lifts supported on T; the rank-one term is divisible by p^2 and the remaining diagonal pairing has units d/p. Its restriction to the two hyperplanes has rank at least h-2. Thus h-2 positive exponents are one and the last is 1+v_p(phi(n)) by the determinant, with h-1 positive exponents total. Combining primes in divisibility order yields the stated Smith diagonal and both corollaries. For a prime modulus n=p the entry is p-1. Independent bounded SymPy Smith spot checks using products of the prime values p-1 or -1, rather than the uploaded incidence code, agreed for n=5187,3298,57,10374. These checks are supplemental; the frozen script was inspected, not executed.

## originality

FAIL

A distinct indexed Resultary result, 3189e6142132, gives the complete integral Smith form for the same matrix at every integer n>=2. Its rule specializes to exactly the frozen diagonal, including the prime boundary, the cokernel and the congruence-kernel corollary. This is demonstrated coverage, not an inference that the catalogue entry has historical priority over the frozen source. The older inspected full-table papers by themselves would not imply this verdict.

## value

FAIL

The integral invariant is natural and useful in isolation. As submitted, however, it delivers precisely a restriction of an available complete classification and standard corollaries; no genuinely different application, scope or needed exact fact survives that comparison. The squarefree pairing proof is concise but the frozen finding is the same invariant, not a separate valuable proof-method result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
