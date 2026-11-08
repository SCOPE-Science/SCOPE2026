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

# Reproduction and limits

Run `python3 verify_palindromes.py` in a directory containing the bundled executable file. It prints:

```text
VERIFY_OK pairs=4 n=1..25 palindromes=37 center_maximal=6 exhaustive_windows=23800 prefix_windows=468450
```

It generates three substitutions for both binary letters, forms all four two-block concatenations, exhaustively checks every window for sizes 1 through 25, compares the entire resulting palindromic language with a separately written literal catalogue, checks the six center-maximal palindromes, and cross-checks against a separately expanded 18,750-letter prefix. Its finite reduction is mathematically exhaustive because every factor of length at most 25 appears within one pair of consecutive level-three blocks, and each possible adjacent source pair occurs. Absence of both length-24 and length-25 palindromes rules out every longer palindrome by its centered subfactor.

This reproduces the fixed-point classification and finite computation; it does not prove bibliographic novelty, palindrome occurrence densities, or unrelated morphism statements. Independent scientific audit has not been performed.
