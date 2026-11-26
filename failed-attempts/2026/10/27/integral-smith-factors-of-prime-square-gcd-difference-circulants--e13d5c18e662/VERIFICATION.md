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

The ring is Z; residue classes index the rows and columns, not the entries' arithmetic. Grouping indices modulo p gives G_p=cI+b(I_p⊗J_p)+J_{p²} with b=p−1 and c=pb. In the presentation, subtracting the first relation in each block leaves c times each difference generator; the primitive sum of these differences is the only coupled coordinate. This splits off p(p−2) copies of c. In the integral basis consisting of e_1, the primitive kernel vector Σ_{i>1}(e_i−e_1), and a kernel complement, J_p acts by the displayed 2×2 block plus zero. It gives p−2 blocks with entry gcd b and determinant 2c², hence factors b and 2p²b. Pivoting on the 1 in the 4×4 block leaves bT_p; T_p has entry gcd 1, every 2×2 minor a multiple of p² with one equal to p², and determinant 2p⁴(3p−2). The resulting factors combine in the asserted divisibility order, with p=2 giving 1,1,4,32. A separate exact Smith computation on the full integer matrices agrees at p=2,3,5; replay: python3 /workspace/branches/f355b5e8-f250-4436-ba9a-0e5e54520ac2/independent_snf.py. These finite cases corroborate the integral proof; they are not an argument for arbitrary primes.

## originality

FAIL

The nontrivial infinite family is exactly a specialization of a distinct indexed theorem for the full integral Smith form of cyclic power-GCD matrices at odd prime-square order. The residual p=2 case gives only one fixed 4×4 example. This is a demonstrated coverage failure to the best of current knowledge, not a finding that the broader record appeared first or that the original proof is wrong. The broader record's path is dated later; its text does not establish historical priority or dependence. The original's integral basis reduction is a different proof, but the finding asserts the invariant factors, not a new general equivalence theorem.

## value

FAIL

A full integral cokernel of this natural circulant would be worth knowing and is not obtainable merely from its determinant. But the exact infinite family is already available from the checked odd-prime power-GCD formula. The uncovered claim is one routine 4×4 Smith form, without a motivated even-prime phenomenon beyond that instance. The record does not state a new general reduction theorem as a separate surviving result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
