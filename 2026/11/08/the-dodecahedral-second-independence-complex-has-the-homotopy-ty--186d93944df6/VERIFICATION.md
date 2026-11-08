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

# Reproducibility and verification

Compile the enclosed C++17 sources using, for example:

```
g++ -O3 -std=c++17 verify_morse.cpp -o verify_morse
./verify_morse
g++ -O3 -std=c++17 verify_mod2.cpp -o verify_mod2
./verify_mod2
```

The first program checks the explicit \(GP(10,2)\) graph, all \(2^{20}\) subsets against both the recursive construction and the sixty forbidden three-vertex paths, then the face vector, the \(31{,}569\) pairs, all \(410{,}520\) Hasse incidences, complete acyclicity, and the integral signed Morse boundary \((1,1)\). Its expected final line is `ALL_CHECKS_PASS`. The second reduces all augmented simplicial boundary matrices modulo two, checking \(\widetilde H_6\) has dimension one and all other reduced homology groups vanish; its expected final line is `ALL_MOD2_CHECKS_PASS`.

The recorded outputs are `verification_morse.txt` and `verification_mod2.txt`. Both checkers execute on finite combinatorial data; extrapolation to other generalized Petersen graphs is neither tested nor claimed. The integral homotopy proof uses the exact signed Morse attaching degree and the Hurewicz theorem, not finite-field homology alone. Independent mathematical audit has not been performed.
