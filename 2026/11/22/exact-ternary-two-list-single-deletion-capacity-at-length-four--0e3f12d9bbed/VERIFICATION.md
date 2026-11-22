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

# Reproducing the exact finite certificate

Execute `python3 verify.py` in the directory containing the extracted files. Only the Python standard library is used. The program generates every \(81\) ternary four-letter word and all \(27\) three-letter received words; it removes each possible input coordinate and de-duplicates identical outputs. It checks the exact rational certificate with `fractions.Fraction`, verifies all ten reversal/relabeling orbits, checks both rational weight sums, and counts received-word loads from the literal \(21\)-word code. It also verifies the three-codeword odd conflict cycle. The program's output must agree byte-for-byte with `verification_output.txt`.

The proof's upper bound uses exact arithmetic, not a numerical optimizer. The finite enumeration is exhaustive because it covers all \(3^4=81\) source words and all \(3^3=27\) outputs, and the orbit table accounts for all source words. Its scope is exactly one deletion and list size two at ternary block length four. Reproduction of these computational checks is not independent mathematical validation or a proof of literature priority.
