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

# Verification and reproduction

The all-length proof relies on sorting cyclic rotations and a counted successor-pair bijection. The computational cross-checks do **not** prove a statement for unbounded length.

Run from the directory containing the supplied standalone files:

```sh
python3 verify_near_permutation.py
g++ -std=c++17 -O2 -Wall -Wextra -o verify_last_columns verify_last_columns.cpp
./verify_last_columns
```

The source-word verifier independently constructs canonical necklaces of exact content \((2,1,\ldots,1)\), sorts full cyclic rotations, calculates the last column, checks the successor-adjacency theorem, and checks each labeled successor pair is realized \((n-3)!\) times. It covers all necklaces for every \(3\le n\le9\).

The last-column verifier instead enumerates each possible ordered fixed-content BWT output, builds the stable LF map from letter occurrence ranks and sorted first-column offsets, retains only single-cycle outputs, and counts linear output runs. This independently covers all candidate last columns over the same lengths and agrees with the first verifier and formula. Its LF one-cycle test is valid because all necklaces of the specified content are primitive.

For example, with occupied alphabet \(\{0,1,2,3,4\}\), `002134` has sentinel-free BWT `402013` and six runs; `001234` has sentinel-free BWT `400123` and five runs. Both are length-six examples, not limits.

Actual reproduced standard output from both programs is in `verification_output.txt`. All tests finished without an assertion failure. Total last-column candidate words and accepted single-cycle words are separately reported, so enumeration completeness is explicit. Only lengths up to nine were computationally checked, and no independent audit or external certification has been performed.
