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
# Verification of the Hermitian four-secant classification

The theorem is an exhaustive, finite-field statement. Both `verify_hermitian_q3r3.cpp` and `verify_hermitian_q3r3_independent.cpp` are standalone standard C++17 programs. The first uses \(\mathbb F_3[t]/(t^6+t+2)\), canonical \((1:a:b)\) coordinates, and joins all unordered pairs of curve points to find four-secants. The second uses \(\mathbb F_3[u]/(u^6+u^5+2)\), canonical \((a:b:1)\) coordinates, and visits every projective line to count its intersections directly. The two programs independently compute \(s(P)\) at every rational projective point by enumerating all points of each four-secant.

Reproduce from the directory containing both sources:

```sh
g++ -O3 -std=c++17 -Wall -Wextra verify_hermitian_q3r3.cpp -o check_pairs
./check_pairs
g++ -O3 -std=c++17 -Wall -Wextra verify_hermitian_q3r3_independent.cpp -o check_lines
./check_lines
```

Both complete runs finished successfully. Their respective terminal sentinels were `HERMITIAN_Q3_R3_EXHAUSTIVE_PASS` and `HERMITIAN_Q3_R3_INDEPENDENT_PASS`. Both compute exactly \(892\) curve points, \(39879\) four-secants, external minimum \(25\), external maximum \(222\), and the same 17-entry spectrum. The line-first verifier explicitly checks all four line-character counts \((158760,175420,158112,39879)\) and the \(63\) maximal external points of \(\mathbb P^2(\mathbb F_9)\).

Both programs perform exact modular arithmetic; there are no pseudorandom tests, floating-point approximations or sampled lines. The first program additionally verifies four curve points on every enumerated four-secant by evaluating the line equation, and the second checks \(39{,}879\cdot730=29{,}111{,}670\) total line–point incidences. Assertions terminate on mismatches.

**Limits:** This establishes the stated finite \(q=3,r=3\) instance only. The independent-audit status remains `not_performed`; the presence of two separately written programs does not constitute independent human review. No claim about all \(q\) or all \(r=3\) Hermitian arcs is made.
