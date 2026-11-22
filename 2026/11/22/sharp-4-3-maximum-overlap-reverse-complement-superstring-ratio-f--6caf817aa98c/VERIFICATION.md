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

# Reproduction

Run `g++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp && ./verify_cpp` and `python3 verify_python.py` in the directory containing these files. Both programs are self-contained and require no third-party dependencies beyond a C++17 compiler and Python 3.

The complete finite domain contains ten binary four-mer reverse-complement classes, hence 1023 nonempty subsets. Both programs enumerate their exact shortest covering lengths by testing every binary word of length at most thirteen; the explicit full cover `0010100001100` proves that this bound loses no optimum. Exact maximum greedy lengths follow from a terminating all-ties recurrence on independently orientable current components.

Observed results: sharp length ratio `4/3`; exactly six equality masks `131 159 183 215 407 663`, in the representative order stated in `RESULT.md`. For the full ten-class input, optimal length `13` and longest greedy length `16`. Both programs print the complete optimal/greedy joint census; totals are 1023. `verify_cpp_output.txt` and `verify_python_output.txt` are recorded console outputs and are not substituted for running the source programs.

The printed numbers are consequences of exhaustive code and the mathematical equivalences explained in `RESULT.md`; they are not general proofs outside the enumerated binary four-mer domain. No external independent assessment has been made.
