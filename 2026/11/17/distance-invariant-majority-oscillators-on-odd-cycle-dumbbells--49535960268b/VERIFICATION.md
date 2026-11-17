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

The complete source and expected output of two independently structured checks accompany this result. Compile `verify_corridors.cpp` with `g++ -std=c++17 -O2 verify_corridors.cpp -o verify_corridors` and run `./verify_corridors`. It exhausts all labelled states of 56 eligible odd-cycle dumbbells with \(3\le a\le b\le9\), connecting path lengths one through six, and at most twenty sites, comparing counts and flipping masks. The output finishes with `PASS graph_parameter_cases=56`.

Run `python3 verify_corridors_construct.py`. It enumerates all two-colored run words through length eighteen, reconstructs the predicted periodic configurations for eight cases (including a seven-edge connector), directly checks each two-step return, and checks the rational generating coefficients and Fibonacci correction through length one hundred. The output finishes with `PASS combinatorial_coefficients=99 constructive_cases=8`.

These programs were run successfully from the accompanying source files. Their logs are included for reproducibility. They do **not** establish the infinite theorem by enumeration; universal correctness depends on the explicit degree-two propagation proof and complete two-phase parametrization. The calculation excludes odd-cycle lengths below three, even rings, multiple connectors, and all transient basin claims.
