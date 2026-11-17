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

`check_symbolic.py` builds the sixteen-state occupation transfer from first principles, checks the exact characteristic polynomial and zeta denominator, checks graph primitivity, and verifies exact rational Collatz bounds for its leading eigenvalue. It then generates the full fixed-state occupation histograms through circumference seven, and computes the limiting occupation density from an implicit derivative of the weighted determinant. Its recorded output is `output_symbolic.txt`. The symbolic script requires Python 3 and SymPy; see `requirements.txt`.

`check_direct.cpp` separately applies the eight-neighbor birth test directly to every binary configuration for circumferences three through seven. It neither reads nor uses the transfer matrix, and prints the counts sorted by the number of occupied sites. Its recorded output is `output_direct.txt`. Compile with C++17, for example `g++ -O3 -std=c++17 check_direct.cpp -o check_direct`, then run `./check_direct`.

The programs' recorded histogram arrays agree entry for entry. The direct enumeration covers only the indicated small circumferences. The proof for all larger circumferences is the weighted closed-walk bijection, and the spectral limits use Perron–Frobenius theory plus a verifiable finite matrix certificate, not empirical extrapolation. The closed form counts **already fixed** configurations; it neither predicts fixation basin sizes nor establishes a general infinite-plane growth law.
