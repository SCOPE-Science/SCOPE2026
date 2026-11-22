---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Expand every matching character into chosen negative edges. A size-j matching in the negative graph extends to precisely I_(n-2j) matchings on all vertices, proving the exact formula. Amdeberhan–Moll Theorem 4.1 establishes v2(I_4q)=v2(I_4q+1)=q, v2(I_4q+2)=q+1, v2(I_4q+3)=q+2. Dividing the j=0,1 terms by 2^alpha_n and using an extra power of 2 for j>=2 yields respectively 1,1,1+|E(H)|,|E(H)| modulo2; an empty or singleton negative graph attains the gcd. For n=s²+2 choose special vertices a,b, ab negative, signs t_v and -t_v on their other incidences with sum(t_v)=s, and all edges of R positive. Matching sums with neither or both special vertices paired together cancel, as do one-special terms; the remaining sum equals I_(s²-2)*(s²-(sum t_v)²)=0 for s>=2, with s=1 immediate. Independent exact direct matching recurrence verified all frequencies n=2,...,6, including 6825 zeros at n6, and witnesses n=3,6,11. The all-n congruence is mathematically derived, not inferred from those finite checks.

## originality

PASS

The involution count and its two-adic valuation are classical, while the claim concerns *each independently signed matching sum*, a uniform all-frequency residue/gcd rule and an explicit infinite square-shifted cancellation family. Neither the unsigned matching polynomial nor published perfect matching orbit spectra imply these exact statements.

## value

PASS

The all-matchings family is a basic combinatorial object (involutions/monomer-dimer configurations), and its complete Boolean Fourier operator has an analytically meaningful inversion/rank question. The gcd/congruence gives an exact obstruction and quantitative pseudoinverse bound uniformly in n, while the infinite n=s²+2 explicit singular subfamily gives nontrivial counterexamples to global invertibility. Neither is simply a standard involution count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
