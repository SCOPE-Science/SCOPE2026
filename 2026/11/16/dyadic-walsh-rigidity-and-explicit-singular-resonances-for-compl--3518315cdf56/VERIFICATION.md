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

Run `python3 check_matching_fourier.py` using Python 3 and NumPy. The checker builds all matching incidence masks of \(K_n\), computes the complete unnormalized binary Walsh transform for \(2\le n\le7\), and independently recomputes a comparison set through the matching-number expansion. It verifies precisely \(2{,}131{,}018\) computed multipliers, the announced dyadic residue in each dimension, and the exact involution valuations through order 70. It also checks the square-shifted zero witnesses at \(n=3,6,11,18\) using a separately implemented signed dynamic program. Recorded output from execution:

```
n=2 matchings=2 frequencies=2 zeros=1 2_content=2
n=3 matchings=4 frequencies=8 zeros=3 2_content=2
n=4 matchings=10 frequencies=64 zeros=0 2_content=2
n=5 matchings=26 frequencies=1024 zeros=0 2_content=2
n=6 matchings=76 frequencies=32768 zeros=6825 2_content=4
n=7 matchings=232 frequencies=2097152 zeros=269577 2_content=4
square_witness n=3 value=0
square_witness n=6 value=0
square_witness n=11 value=0
square_witness n=18 value=0
ALL_MATCHING_WALSH_DYADIC_PASS frequencies=2131018 n6_zeros=6825 n7_zeros=269577
```

The all-dimensional arithmetic statement is proved on paper, not certified by finite computation. No independent audit has been performed, and broad historical priority is not established.
