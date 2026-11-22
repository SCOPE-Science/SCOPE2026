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

The general statement is proved in `RESULT.md` by the gap-vector support criterion, connectivity of the adjacent-swap graph of linear extensions, the cross-adjacency singleton test, and explicit balanced/unbalanced parity witnesses.

Reproduce finite checks using `python3 verify_parity_shuffles.py` and `g++ -std=c++17 -O2 -Wall -Wextra verify_parity_shuffles.cpp -o verifier && ./verifier` in a directory containing the extracted files. The programs enumerate every ordered positive profile with \(a+b\le12\), compare direct even-shuffle traces against the independently formulated odd-word obstruction, and check the formula for VC dimension. `python_report.txt` and `cpp_report.txt` contain the records of one successful execution. The finite range is not evidence of a general theorem without the proof.

The alternating-group (unrestricted-permutation) and unrestricted two-chain publications are not equivalent to the parity-restricted two-chain class. The supplied verifiers do not establish historical priority, optimal asymptotic decision complexity, or independent validation.
