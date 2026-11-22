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

# Verification

The graph is explicitly constructed from all two-element and three-element subsets of a five-element ground set. A code is checked against all twenty closed-neighborhood coverage conditions and all 190 pair-separation conditions; the proof in `RESULT.md` explains why these are equivalent to resistance to any one detector deletion.

Reproduce the independent verifications with:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_main.cpp -o verify_main
./verify_main
python3 verify_secondary.py
```

Observed results:

```text
VERIFY_OK: 5945 codes; 15 four-cycle optima; TAR threshold 15
INDEPENDENT_DIRECT_ERASURE_OK 15 optima and zero size-11 codes
INDEPENDENT_ALL_WEIGHT_AND_TAR_OK 5945
```

The C++ program enumerates all \(2^{20}\) subsets, independently generates the fifteen geometric optimal masks, checks the \(S_5\) orbit, and exhaustively tests TAR reachability at budgets \(12\), \(13\), \(14\), and \(15\). The Python program directly deletes every selected detector and examines nonempty, distinct signatures for all omitted sets of size eight or nine. It separately checks all 1,048,576 masks against independently built coverage and separation masks, reproduces every coefficient of the polynomial, and repeats the TAR breadth-first searches. Excluding nine omissions excludes larger omissions by monotonicity. All tests are finite exact integer checks; no probability or sampling is involved.

No external code, data files, downloaded articles, or machine-learning artifacts are necessary to reproduce the checks. This is not an independent scholarly audit. Publication-priority coverage is incomplete as described in `REVIEW.md` and `AUDIT.json`.
