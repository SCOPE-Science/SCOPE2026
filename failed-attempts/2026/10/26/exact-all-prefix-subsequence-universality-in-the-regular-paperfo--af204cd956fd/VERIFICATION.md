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

For a fixed binary alphabet, each completed shortest both-letter segment supplies one letter of any prescribed subsequence. The word of successive segment-ending letters followed by a letter absent from the remainder cannot embed: earliest matching reaches the corresponding segment ends. From the odd parts of the eight position indices, the aligned block is 110a100b, with a the even-block indicator and b the symbol at the scaled index. With empty incoming remainder the first two arches close at offsets 3 and (5 if a=0, otherwise 6); the third closes at 8 if and only if b=1. An incoming zero remainder adds a closure at offset 1 and the states agree after offset 2. The outgoing remainder is empty for b=1 and zero-only otherwise. Telescoping gives U(8k)=3k+b_(k-1)-1 and the seven partial offsets give 3k+(0,0,1,1,2-a,2,2). This yields precisely the two corrections, including U(1)=U(2)=0. The discrepancies at N≡13 mod 16 and at N=8k with k≡3 mod 4 attain +1/8 and -1, respectively; the other residues stay between them. The density, dyadic and shortest-absent consequences follow. The independently written finite checker /workspace/branches/538c09fe-c9b8-4fbe-963c-de69dd2fe263/finite-prefix-check.py tested every binary candidate necessary to determine the index at N=1 through 32; e.g. U(5)=1, U(13)=5 and U(24)=8. The furnished Python code was inspected, not run; its documented tests are finite. The scanner argument, not enumeration, establishes the result for all N.

## originality

FAIL

Direct equivalent coverage in a distinct indexed Resultary record. Its one-indexed bits are the complements of the frozen zero-indexed bits, which preserves binary universality. Its exact formula at r=0 subtracts p_T=1 precisely for odd(T)≡3 mod 4; its r=5 term is 1+(T mod 2), exactly the first residue correction. The other offsets coincide, as do discrepancy endpoints, density and dyadic values. The matched record also supplies a limiting discrepancy distribution. The date in the catalogue path is not independent evidence about authorship or priority; the scientific finding is equivalent coverage, not an attribution of how the records arose.

## value

FAIL

The exact fixed-origin invariant and its sharp discrepancy would be useful for precise subsequence capacity and shortest absent lengths. However, the frozen contribution does not add a distinct invariant, regime or implication to the existing indexed all-prefix theorem; compact floor notation is an algebraic restatement. No surviving new valuable claim was identified to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
