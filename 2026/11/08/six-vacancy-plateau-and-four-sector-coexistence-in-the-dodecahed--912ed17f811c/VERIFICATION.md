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

# Verification and limits

The proof has two fully finite, exact procedures. Both operate on the generalized Petersen graph \(GP(10,2)\), with twenty labeled spins taking values \(-1,0,1\).

From this folder, run:

```bash
python3 verify_dp.py > dp.out
cmp sector_minima.csv dp.out
g++ -O3 -std=c++17 verify_gray.cpp -o gray_check
./gray_check > mag.out
cmp sector_magnetization.csv mag.out
```

The first command uses exact min-cost/tie-count factor elimination. The second enumerates every one of the \(3^{20}=3,486,784,401\) configurations, updating energies by exact integers and recording all \((Q,M)\) sector minima. All comparisons above completed successfully; the enumeration printed `EXHAUSTED 3486784401 expected 3486784401`. The independent algorithms also agree on all twenty-one occupancy-sector energies and counts. No external data, numerical fitting, probabilistic approximation, or proprietary computation is needed.

The complete occupancy-sector integer table certifies the rational convex envelope and two crossings. The checks prove the finite specified model only, not a field-dependent or thermodynamic statement. They do not establish historical priority or independent external scientific validation.
