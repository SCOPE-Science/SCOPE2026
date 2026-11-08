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

# Computational verification

The theorem concerns all ternary words of exactly length \(84\), not a sample. `verify_labeled.cpp` exhaustively generates all valid labeled source prefixes and verifies that the terminal level contains exactly \(6048\) words with only two transform images, of multiplicities \(4032\) and \(2016\), and that no length-\(85\) extension is valid.

`verify_rgs.py` independently generates canonical restricted-growth representatives, verifying exactly \(1008\) terminal classes, a split of \(672\) and \(336\), universal three-letter support, and no valid length-\(85\) extension. It byte-compares its complete output with `canonical84.tsv`.

Run from the directory of these files:

```
python3 verify_rgs.py
c++ -std=c++17 -O3 verify_labeled.cpp -o verify_labeled
./verify_labeled
```

Successful outputs:

```
TERMINAL_CURL_RGS_VERIFY_OK 1008 672 336
TERMINAL_CURL_LABELED_VERIFY_OK 6048 4032 2016
```

Both methods are exhaustive by prefix heredity. Every possible new overlap must end at the appended letter and therefore is found by a suffix-period test; all old overlaps have been excluded inductively. Since valid sources are overlap-free, every prefix is cubefree, and its curling number is \(2\) exactly when it ends with a square. Source-symbol permutations preserve both properties, making restricted-growth normalization complete. The code also checks the empty next level. These arguments are part of the proof, not derived merely from logged output.

The `canonical84.tsv` SHA-256 checksum is `f9cbf37faf2e799e541f6d147866ae1046d68da2cfdfbad1d4e4db2e275af2bd`.

The exact result is finite. No independent mathematical audit or external certification has been performed.
