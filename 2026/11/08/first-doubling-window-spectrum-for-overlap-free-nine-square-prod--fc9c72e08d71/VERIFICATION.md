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

# Reproducibility

In a directory containing the two `.py` files and `census_96.tsv`, execute:

```sh
python3 verify_by_words.py
python3 verify_by_blocks.py
```

Both programs reproduce the exact twelve-word census, length counts, and each word's nine-square decomposition. They use no nonstandard packages, network, randomness, or external files. The first program derives candidate words by every valid one-bit extension and recovers factorization lengths through dynamic programming. The second enumerates every possible overlap-free square whose half-length is at most \(40\), then every bounded nine-square concatenation. The bound \(40\) follows because the other eight nonempty squares consume at least \(16\) symbols in a word of length at most \(96\). The intermediate numbers of states are asserted in the programs. The finite proof does not assert any result beyond length \(96\), and independent verification is not claimed.
