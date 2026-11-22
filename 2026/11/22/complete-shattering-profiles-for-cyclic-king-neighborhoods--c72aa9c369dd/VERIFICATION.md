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

# Verification of the cyclic-king shattering theorem

Run `python3 VERIFY.py` with standard Python 3. The program uses only `collections` and `itertools` from the standard library. It constructs actual closed neighborhoods and all Boolean trace masks, enumerates every candidate support contained in an actual neighborhood, and checks shattering, translation orbits, maximal pairs and the three motif families. Its exhaustiveness is mathematically grounded by the all-one trace reduction.

The seven complete base coefficients by size were:

| Side lengths | Coefficients |
|---|---|
| \(3,3\) | \(1\) |
| \(3,4\) | \(1,12\) |
| \(3,5\) | \(1,15,45\) |
| \(3,6\) | \(1,18,108\) |
| \(4,4\) | \(1,16,120,288\) |
| \(4,5\) | \(1,20,190,420\) |
| \(5,5\) | \(1,25,300,300\) |

Seven enlargement pairs were checked for agreement of all nonempty trace sets and shattering judgments across all 512 anchored templates each. The 512-template missing-empty checks at \((3,6),(4,5),(5,5)\) returned no critical template. On \(7\times7\), precisely 588 shattered triples were exactly the dihedral-translation images of the three displayed motifs, and 196 shattered pairs were inclusion-maximal. Additional direct censuses matched formulas for grids \((3,7),(3,8),(4,6),(4,7),(5,6),(5,7),(6,6),(6,7),(7,7)\). The complete observed final output marker was:

```
ALL_CYCLIC_KING_SHATTERING_CHECKS_PASS
```

The universal statement follows from the rigorous local overlap classification and translation orbit-stabilizer arguments in `RESULT.md` combined with these finite exhaustive computations; the finite samples alone do not prove an all-parameter result. No independent third-party or proof-assistant validation has been performed. Historical priority under alternative terminology remains a limitation.
