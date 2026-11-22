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

# Reproducibility and limits

Run `python3 verify_psl.py`. This enumerates every element of \(\operatorname{PSL}_2(p)\) for the prime fields \(p=3,5,7\), computes all trace patterns on every partial matching of size three and binary ranks of the admitted triangle boundaries. Its expected outputs are ranks \(414\) and \(1504\) in prime fields \(5\) and \(7\), respectively.

Build the separately implemented character-based verifier with `c++ -O2 -std=c++17 verify_character.cpp -o verify_character` and execute `./verify_character`. It independently constructs all three-face incidence using products of two-by-two determinants and finite-field quadratic characters; binary elimination returns the same ranks and asserts a nonsquare three-cycle on which the cochain evaluates to one.

Both programs are standalone and require no downloaded data or third-party libraries. Exhaustive computation verifies the finite numerical claims only. The all-odd-prime-power classification, purity and cohomology nonvanishing are supported by the proof in `RESULT.md`, not by extrapolation from prime-field experiments. Neither program computes integral homology, and there is no independent mathematical audit.
