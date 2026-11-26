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

Kummer counts the carries in n+2n. A first carry requires two adjacent 1 bits of n and forces the next carry because the shifted summand then has bit 1 and there is an incoming carry. A string of s ones, s>=2, gives exactly s carries, continuing through the high shifted bit; dyadic scaling leaves the count unchanged. Splitting even and odd factors gives B_{2N}/B_N=O(6N)/(O(2N)O(4N)), where O is the odd factorial part. For N=2^t a and fixed modulus, the complete odd-residue blocks have products 1 at large t (units pair by inversion; the self-inverse units multiply to 1 for k>=3; for k=2 take an even number of blocks). Therefore B_{2^t a} stabilizes at each modulus, defining U_a with the same valuation as B_a. In the exact factorial ratio B_{A+H}/(B_A B_H), the factors and inverse factors are 1+cH/j with c in {1,2,3}; for A=2^t a, H=2^(t+r)b and j<=3A, v2(j)<=t+floor(log2(3a)). The prescribed gap makes every ratio factor a unit congruent to 1 mod 2^k, so this use of ratios is valid even when B_A or B_H itself is not a unit. Passing to the limits and repeating realizes a finite product of U values at positive indices. U_1=7 and U_9=5 modulo 8; exact seed residues follow from B_8 and B_72 and stabilization modulo 8. The valuation of U_9^(2^j)-1 is j+2 by successive factorization, giving the entire subgroup 1 mod 4, and U_1 supplies its other unit coset. This works at k=1,2 with the respective trivial or order-two groups. Multiplying a seed of valuation s>=2 by units gives every class of that valuation; a sufficiently high valuation gives zero. Stabilizing at positive dyadic multiples supplies infinitely many indices for each class. This proves the count, two-adic closure and Haar measure, with no frequency assertion. Independent replay: python3 /workspace/independent_checks.py 3 used an exact consecutive-index factorial ratio checked against direct binomial evaluations and enumerated n=0..32767; it attained precisely the allowed sets for k=1..8 and checked seed residues 7 and 5. The finite image is not the all-k proof.

## originality

PASS

The valuation-one exclusion and valuation support alone overlap verified earlier indexed findings on exactly this sequence and are not singled out as new. The accepted distinct content is complete coverage of the residues within every allowed shell for all fixed powers of two, with infinite witnesses and the resulting closure. No inspected prior claim implies that coverage; the comparison is bounded.

## value

PASS

For this natural thin sequence, valuations give necessary restrictions but no completeness for modular values. The result proves saturation of every permitted shell at all exponents and supplies infinite witnesses by dyadic stabilization. The closure and measure 3/4 give an exact arithmetic invariant beyond a valuation distribution or finite residue table. It does not answer index-frequency or minimal-witness questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
