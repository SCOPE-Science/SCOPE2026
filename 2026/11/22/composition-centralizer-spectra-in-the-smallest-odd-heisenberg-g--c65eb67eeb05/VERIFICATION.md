---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the composition-centralizer census

## Exact algebraic checks

Each group endomorphism is \(f_{A,u}(w,z)=(Aw,(\det A)z+uw)\), and every pair commutes precisely when \(AB=BA\) and \(v(A-\det A\,I)=u(B-\det B\,I)\). The proof counts all scalar cases, all nonscalar cases with invertible constraint matrix, and both possible nonscalar rank-one cases. A nonscalar \(2\times2\) matrix has a centralizer algebra of dimension two. In the rank-one branch, the defining equation for the compatible matrix parameter is two nonparallel affine lines for a diagonalizable matrix, versus two parallel affine lines for a Jordan matrix. Their solution cardinalities \(2p-1\) and \(2p\) are exact for all odd primes.

Symbolic expansion of the seven coefficients yields \(p^6\) endomorphisms. Weighting by the corresponding seven centralizer sizes yields \(p^8+5p^7-8p^5+3p^3\) ordered commuting pairs. The center has two endomorphisms because precisely two centralizer sizes equal \(|M_p|=p^6\).

## Standalone computation

Run `python3 verify.py` using Python 3.9 or newer. No third-party packages are needed. This program derives every centralizer size separately by enumerating all \(p^4\) candidate matrices for a first endomorphism, finding matrices commuting with each, computing the row-space fiber multiplicities, and comparing the resulting complete histogram with the closed formula for primes \(3\), \(5\), and \(7\). It also tests all maps against all group multiplications in \(H_3\), and checks the endomorphism composition identity on generators for every ordered pair of parameters at \(p=3\).

The saved `verification_output.txt` records seven exact centralizer strata and the total commuting-pair counts at all three primes, ending with `FINITE_HEISENBERG_ENDOMORPHISM_CENTRALIZERS_PASSED`.

## Limits

Finite computation does not certify the result for every prime. The all-prime claim is proved by the exact matrix-theoretic case split, which includes the cases of Jordan degeneration, scalar matrices and noninvertible endomorphisms. No outside expert certification or independent audit is represented.
