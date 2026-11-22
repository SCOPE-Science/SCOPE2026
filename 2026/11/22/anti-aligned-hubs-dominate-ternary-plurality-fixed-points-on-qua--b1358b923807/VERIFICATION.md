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

The source files require only Python 3 and use exact integers for all finite-state counts. From the folder containing this document run:

```sh
python verification/count_fixed.py
python verification/bruteforce.py
python verification/large_deviation.py
```

`count_fixed.py` implements the five- and six-page-type multinomial recurrences. It returned the three columns \((U_m,V_m,E_m)\) below:

| Pages \(m\) | \(U_m\) | \(V_m\) | \(E_m\) |
|---|---:|---:|---:|
| 1 | 5 | 4 | 39 |
| 2 | 13 | 9 | 93 |
| 3 | 61 | 58 | 531 |
| 4 | 293 | 705 | 5109 |
| 5 | 1001 | 2996 | 20979 |
| 6 | 4885 | 19446 | 131331 |
| 7 | 22765 | 152426 | 982851 |
| 8 | 88485 | 811901 | 5136861 |
| 9 | 421369 | 5036368 | 31482315 |
| 10 | 1999493 | 35037414 | 216222963 |

`bruteforce.py` independently constructs the \(2m+2\)-vertex graph, tests all \(3^{2m+2}\) configurations, and counts hub-agreement classes. For \(m=1,2,3,4,5\) it found total counts \(39,93,531,5109,20979\). The largest direct enumeration covered 531441 configurations. Both programs printed their `OK` completion markers.

`large_deviation.py` independently computes the exact integer recurrence for the random-walk left tail with step multiplicities \((3,1,2)\) for \((+1,0,-1)\). Its normalized values \(\sqrt m\,\Pr(S_m\le-1)/\rho^m\) were approximately 1.37511, 1.56865, 1.71561, and 1.81499 at \(m=50,100,200,400\), respectively, approaching the theoretically derived constant \(c\approx1.94785\). The convergence is slow and those finite values do not prove the limit.

The proof of the asymptotic uses a separate exponential tilt and a standard aperiodic lattice local central limit theorem; it does **not** rely on extrapolating finite-state simulations. No computational checks were performed for every \(m\), and no statement is made about the eventual fate of nonfixed states.
