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

# Verification and reproducibility

Compile `verify_exhaustive.cpp` with a C++17 compiler (for example `g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive`) and run the binary; compare `exhaustive_output.txt`. It exhaustively checks a finite collection of wheel states at \(q=4,5,6,7\), including \(q=5,n=8\) with \(1,953,125\) labelled states, against the claimed time-two motif criterion, absence of time-three excitation, sharp clock and two separate terminal channels. Every recorded line ends in `CHECK_OK`.

Run `python3 verify_transfer.py` (standard library only); compare `transfer_output.txt`. This program independently builds a weighted four-symbol de Bruijn transition graph and computes the exact word counts from matrix traces using sparse polynomial truncation. Every overlapping finite parameter agrees with the C++ output and its run ends in `TRANSFER_OK`.

These experiments verify checked finite instances and code implementation, not the entire infinite parameter range. The proof in `RESULT.md` proves the all-size assertions by local update rules, case analysis and a cyclic-word bijection. No external or independent audit has been performed.
