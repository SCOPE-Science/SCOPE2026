---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For integral mu>0 and n>mu, Grau--Oller-Marcen--Sadornil Theorem 2(iv) gives n in S_mu iff mu/n+sum_{p|n}1/p is an integer. The only Omega(n)<=2 shapes are p,p^2,pq with p<q. In each case the positive numerator mu+1, mu+p, or mu+p+q is at most the corresponding denominator and strictly below twice it, so the integer is 1, giving mu=p-1, mu=p(p-1), or mu=pq-p-q, each with a direct converse. For mu=673: 674 composite, discriminant 1+4*673=2693 is between 51^2 and 52^2, and (p-1)(q-1)=674=2*337 has no pair giving distinct primes. This is an infinite theorem only within Omega<=2; the supplied small finite test is not its proof.

## originality

FAIL

The exact general iff arithmetic characterization for all mu-Sondow numbers in Grau--Oller-Marcen--Sadornil Theorem 2(iv), together with the elementary three-shape split and 0<mu<n, mechanically yields the proposed iff families. Its mu=673 obstruction is the immediate tiny factor-pair/nonsquare-discriminant corollary. That published stronger characterization directly covers the new claim by elementary specialization even though the displayed classification or the number 673 is not stated. Matching title/phrase is not required for implication.

## value

PASS

The low-Omega slice of the open large-witness conjecture is a natural, unbounded factor-complexity boundary; the source singled out mu=673 as computationally difficult. Proving any future witness there needs at least three prime factors is a motivated exact structural sieve, although it does not solve existence and the proof itself is short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
