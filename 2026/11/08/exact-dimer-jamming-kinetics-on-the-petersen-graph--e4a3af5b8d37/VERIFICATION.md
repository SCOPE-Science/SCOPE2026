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

# Reproducible exact checks

Run both standalone standard-library Python 3 scripts in this package:

```bash
python3 verify_mask.py
python3 verify_paths.py
```

The first carries out a 272-state backward exact terminal-probability calculation and a forward rational-exponential master-equation solution on the outer-cycle/inner-star construction. The second independently realizes the Petersen graph as \(\mathrm{KG}(5,2)\), enumerates all 2,190 legal ordered successful-edge histories without memoization, and derives the transient mean from the conditional exponential waiting-time convolution. Both assert \(\Pr(X=3)=1/25\), \(\Pr(X=4)=52/75\), \(\Pr(X=5)=4/15\), and the coefficients on rates \(0,1,2,3,5,6,10,15\).

No random samples or numerical fits are involved. The finite enumerations prove only the stated ten-vertex graph case. The independent scientific audit has not been performed.
