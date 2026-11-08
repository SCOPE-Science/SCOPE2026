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

# Verification record

The standalone `verify_fnc_f4_count.cpp` uses C++17 and only integer arithmetic with the field relation \(\alpha^2+\alpha+1=0\). Compile with `c++ -O2 -std=c++17 verify_fnc_f4_count.cpp -o verify` and execute `./verify`; the observed output was `F4_EXTREMAL_SEXTICS_COUNT_PASS 960` followed by `F4_EXTREMAL_SEXTICS_PGL_ORBIT_PASS 181440 189 960`. It enumerates all \(2^{20}=4^{10}\) normalized coefficient tuples and tests nonvanishing at all 21 rational projective points. Independently it enumerates all \(4^9\) possible matrices, identifies 181,440 invertible ones and 189 stabilizers of the explicit representative; exact rank-10 interpolation on the 21 points makes the stabilizer test polynomially conclusive. Their quotient establishes one orbit of 960, agreeing with the Python method.

The independent Python 3 program `verify_fnc_f4_sextics.py` requires NumPy. Execute `python verify_fnc_f4_sextics.py` from its directory. Observed output:

```
TOTAL_NORMED_FORMS: 1048576 SMOOTH: 960
PGL3_F4_ORDER: 60480 ORBIT_SIZE: 960 STABILIZER_ORDER: 63
CANONICAL_REPRESENTATIVE_COEFFICIENTS: [3, 0, 0, 2, 0, 0, 0, 0, 0, 1]
SMOOTH_F4_FNC_SEXTIC_UNIQUE_ORBIT_PASS
```

The Python verifier checks the exact coefficient-action formula of eight projective transformations at all 21 points for each of the ten monomial basis vectors and the constant part. It checks that the whole smooth set is stable and that a breadth-first graph search from the representative visits all 960. Since every edge is an invertible projective transformation, visiting all 960 proves transitivity. These are exhaustive finite tests, not sampled experiments.

The separate algebraic proof that the gradient-zero locus is precisely \(\mathbb P^2(\mathbb F_4)\) ensures the 21 tests detect *all geometric singularities*. The programs do not independently verify the preexisting published normal-form theorem, and they are not independent mathematical audits. The claim makes no assertion about curves over other field sizes or automorphisms not defined over \(\mathbb F_4\).
