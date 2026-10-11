---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For n=p^a m with m squarefree and coprime to p, every exponential-unitary divisor is m p^d with d unitary in a. Thus the harmonic mean equals p^a m t_a/E_a(p). Because the d=a term is 1 and every other term is divisible by p, E_a(p) is coprime to p. Cancelling gcd(E_a,t_a) reduces integrality exactly to M_a(p) dividing m; squarefreeness of m then gives the displayed generator condition. Standard squarefree counting coprime to the fixed modulus pM gives the stated constant and O(sqrt X) error. Independent spot calculations reproduce E_2(2)=3, E_4(2)=9, E_4(3)=28 and E_6(2)=57.

## originality

FAIL

A decisive prior exact database criterion has existed since 6 November 2021. OEIS A349025 is multiplicative with local factor a(p^e)=sum_{d||e}p^{e-d}, and its revision history records the statement that k is exponential-unitary harmonic iff A349025(k) divides k*A278908(k). For k=p^a m with squarefree m, A349025(m)=1 and A278908(k)=t_a, so this prior global iff specializes immediately to E_a(p)|p^a m t_a and, since E_a(p) is coprime to p, to the submitted M_a(p)|m condition. The squarefree-generator reformulation and fixed-modulus density then use only elementary cancellation and the standard squarefree counting theorem. Under the required implication standard, the central classification and asymptotic are therefore covered as a routine corollary of an older global exact criterion.

## value

FAIL

Once the pre-existing all-integer iff criterion is specialized, the generator condition is elementary gcd cancellation and the density is the standard squarefree-coprime count. The slice is natural, but the submitted work does not clear the value bar as an independent mathematical gap because its main classification is a routine corollary of a known global exact database formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
