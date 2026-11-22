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

Run `python3 verify.py` from the directory containing the attached verifier. The program uses only the Python standard library. It independently constructs the exact 84-vertex directed graph by lifting all weight-three or weight-six binary masks through the cyclic difference equation, and by enumerating every one of the \(3^8\) possible ternary eight-tuples and reconstructing the same graph from their differences.

Both constructors agree on all 96 distinct directed edges. The program verifies the exact four-vertex cyclic core and confirms that the other 80 vertices have no path of length three, as well as checking that the all-zero mask cannot transition to a nonzero admissible mask. It then enumerates every state at lags \(2\le k\le11\), compares the fourth and eighth iterates, and checks the closed binomial formula for each fixed count.

Expected output:

```
GRAPH_CERTIFICATE_OK nonzero_masks= 84 edges= 96 exterior_length2_walks= 80 cyclic_masks= [119, 187, 221, 238]
DIRECT_CYCLE_CHECK_OK k=2..11 fixed_counts= [9, 5, 17, 41, 49, 145, 257, 481, 1089, 1985] total_states= 265716
CERTIFIED: Fix(T_k^(8k)) = Fix(T_k^(4k)) for every integer k>=2
```

The computer checks are finite, exhaustive for the claimed 84-vertex certificate, and bounded for direct state enumeration. The proof that this one graph controls every lag, including the twisted column boundary, is provided in `RESULT.md`. No assertion about unattested full period spectra or independent validation is made.
