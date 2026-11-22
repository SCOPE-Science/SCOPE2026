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

# Reproducible verification

From this package root, compile `code/verify_direct.cpp` with any C++17 compiler using `g++ -std=c++17 -O3 code/verify_direct.cpp -o verify_direct`; run `./verify_direct`. The program constructs the two-hub, paired-page neighbor graph explicitly, evaluates synchronous threshold-two updates on all labelled initial states for page counts one through six, classifies the first all-rest update, and checks that no state remains non-resting after update three. Its recorded output is `evidence/direct_output.txt`.

Run `python3 code/verify_symbolic.py` using Python 3 without third-party dependencies. It independently enumerates the permitted nine page-pair states for each of the nine hub assignments, convolves their capped bivariate excited-neighbor count polynomials for page counts one through thirty, and compares with the proposed all-size closed form. Its recorded output is `evidence/symbolic_output.txt`.

All checks completed successfully for the actual embedded code paths. The direct finite test includes 5,380,830 configurations; the symbolic test checks thirty separate page counts, but neither constitutes a computational proof over all page counts. The all-size proof is the causal exclusion of time-two excitation and the exact symbolic hub-case enumeration in `RESULT.md`. Literature comparison carries ordinary residual coverage risk, and no independent external audit has been conducted.
