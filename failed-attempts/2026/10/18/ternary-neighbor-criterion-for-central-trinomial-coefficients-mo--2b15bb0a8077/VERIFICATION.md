---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The constant term of f^n for f=x^−1+1+x is T_n. The exact f^3=f(x^3)+3h identity and cubing modulo nine show that for the i-th ternary digit the only first-order correction involves h(x^(3^(i−1))). The uncorrected exponent choice vanishes digitwise by reduction modulo 3, giving 3^s where s is the number of 2 digits. For a correction at i, lower exponents vanish up to i−2; the combined block at i−1 and i has absolute exponent at most 7·3^(i−1)<3^(i+1), while every higher term is a multiple of 3^(i+1). Thus the block must itself have exponent zero, and the remaining higher exponents vanish digitwise. Exact expansion gives local constant-term rows (2,2), (6,8), (16,24). A 2 outside the correction pair annihilates that correction modulo nine, and a pair of adjacent 2s has local value 24, also annihilating the correction. For one 2, the base term 3 receives +3 if the position is positive and +3 if its next higher digit is 1, giving the stated four residues. No 2 gives a unit modulo 3, not a specified residue modulo 9. For L≥2, the two end positions each give 2^(L−1) words and each interior position gives 2^(L−2); add 2^L words without a 2 to count those not divisible by nine. Direct cases L=0,1 and squeezing all cutoffs between powers of three complete the proof including n=0. A fresh check used T_n=Σ_k binom(n,k)binom(n−k,k) for n<729 and matched both censuses through L=6. This corroborates the checks without using a finite test as an unlimited proof.

## originality

FAIL

The distinct indexed complete modulo-nine spectrum covers the entire frozen claim by direct restriction and aggregation, and the distinct exact language record independently states the divisibility criterion and complementary census. This establishes current substantive coverage, not the historical priority of any of these records. Both comparison records bear later index dates than the assigned record. The classical mod-three literature and a general automaton construction alone would not have been grounds for failure. No separately supported new remainder is identified in the frozen finding.

## value

FAIL

The object and valuation boundary are natural, and the local corrections provide a readable proof. But as an exact-data contribution the submission adds no demonstrated needful datum beyond the already documented complete residue spectrum and histogram; both census quantities are read off or summed directly. There is no separately established reusable lemma or new valuation layer that would stand as a distinct valuable claim in the current comparison set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
