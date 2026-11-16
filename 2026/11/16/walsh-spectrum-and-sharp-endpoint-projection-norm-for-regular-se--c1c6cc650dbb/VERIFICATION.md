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

The package includes executable exact-integer checks, not merely recorded printouts. In a directory containing the four files `check_regular7.py`, `check_regular7_independent.cpp`, `walsh_quotient.csv`, and `projection_kernel.csv`, execute:

```
python3 check_regular7.py
c++ -std=c++17 -O2 check_regular7_independent.cpp -o check7
./check7
```

The Python test reconstructs all 32768 quotient configurations, checks the count 2640, computes both integer Walsh transforms, compares all 32768 entries of each CSV, checks the complete histograms, Parseval, exact projection norm and selected independent direct character sums. It reports:

```
REGULAR7_WALSH_RANGE_PASS count=2640 quotient=32768 nonzero=8656 rank=553984 gap=16 projection=11155/256
```

The C++ test enumerates the entire 2097152-element ambient orientation cube by a separate method, recognizes each regular tournament by its seven integer outdegrees, then computes the 32768 character sums **directly**, without the parity-reconstruction loop or the Walsh–Hadamard butterfly. It compares every one against `walsh_quotient.csv`, then independently spot-checks 256 entire ambient-edge characters against the affine-lift formula. It reports:

```
REGULAR7_WALSH_INDEPENDENT_DIRECT_PASS full_orientations=2097152 regular=2640 frequencies=32768 ambient_lift_samples=256
```

The checked quotient absolute spectrum, in ascending amplitude order, has multiplicities `24112,3780,420,1365,630,1260,360,630,105,105,1` at amplitudes `0,16,32,48,80,96,112,176,240,528,2640`. The checked projection-kernel absolute spectrum has multiplicities `5760,3360,6720,11760,1344,2730,560,420,112,2` at `0,16,32,48,64,80,208,240,496,8656`, respectively.

Finite exact exhaustion proves the order-seven computational constants, while the algebraic affine-frequency reduction and averaging argument prove how these constants yield the **full** 21-dimensional ambient result and optimality among unrestricted projections. Compilation of the independent cross-check requires an ordinary C++17 compiler; the primary checker requires only Python 3.8 or later. An independent mathematical audit has not been performed.
