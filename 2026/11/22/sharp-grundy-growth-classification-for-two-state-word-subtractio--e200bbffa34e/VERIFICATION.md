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

# Verification notes

Both programs take transition tables as data instead of using any published Grundy values. `checker_types.py` computes mex values recursively from all accepted suffixes for 64 ternary assignments through length eight, checking every word's closed formula when applicable and each length maximum. `checker_table.cpp` independently uses bit-coded binary words for all 16 tables through length sixteen and compares both pointwise and extremal formulas. The observed successful runs cover 629,760 and 2,097,120 word/table inputs.

To replay, execute `python3 checker_types.py`; compile `checker_table.cpp` with `g++ -O2 -std=c++17 checker_table.cpp -o checker_table` then execute `./checker_table`. The theorem for arbitrary lengths and alphabets is proved by four-map exhaustion and a strong induction, not inferred from those finite experiments. No external formal verification or independent review was performed.
