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

# Finite verification and scope

Run `python3 verify_cobalancing.py` with Python 3 and its standard library. The script generates the Pell, associated Pell, and cobalancing sequences using their separate recurrences. It independently forms \(a_n=b_n^2/4\), computes exact shifted sums and their GCDs for \(1\le k\le500\), and checks the two-case formula against those GCDs and the GCDs of adjacent shift differences. It checks the telescoping sum identity for several offsets, as well as \(u_{n+2^r}-u_n\equiv2^{r-1}\pmod{2^r}\) and the squared-block valuation for \(2\le r\le8\).

Observed output:

```text
VERIFY_OK k=1..500 gcd_windows=6000 gcd_differences=6000
PELL_SUM_IDENTITY_OK samples=2500
DYADIC_SHIFT_OK r=2..8 n=0..79
EXAMPLES {1: 4, 3: 4, 4: 8, 6: 20, 8: 16, 12: 120, 21: 28, 24: 240, 30: 100, 42: 140, 60: 600}
```

Finite testing alone does not establish an infinite GCD identity. The accompanying proof uses a four-term invertible recurrence to reduce the infinite difference GCD, and an exact dyadic lifting argument to determine the remaining valuation. The proof covers all \(k\ge1\); no exhaustive claim is made beyond the explicitly checked finite range.
