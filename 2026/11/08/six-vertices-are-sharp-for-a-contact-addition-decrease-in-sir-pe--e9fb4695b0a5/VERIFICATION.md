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

# Exact checks and limitations

`verify_peak.py` generates every labeled simple graph on two through five vertices, filters connected graphs, canonicalizes via every vertex permutation, and confirms \(1,2,6,21\) connected isomorphism classes. Its first-event recursion uses exact SymPy polynomials; for every missing-edge, seed and threshold it checks the reduced difference has a zero numerator or nonnegative numerator and denominator coefficients, with both nonzero at \(\beta=1\). It therefore certifies the all-\(\beta>0\) signs instead of sampling rates.

Replay in four batches:

```text
python verify_peak.py --start 0 --stop 5
python verify_peak.py --start 5 --stop 10
python verify_peak.py --start 10 --stop 15
python verify_peak.py --start 15 --stop 21
python verify_peak.py --witness
python verify_peak_forward.py
```

Observed batch totals were respectively \(698,420,400,220\) tested comparisons, hence \(1738\) comparisons, of which \(1475\) gave strict increases. The highest polynomial degree was \(15\). Both rational witness implementations returned

```text
without edge 12: 14289062500/18273931533
with edge 12:    1946796875000/2491078937193
difference:      24352320312500/56704429847324259
```

`verify_peak_forward.py` is an independent subset recurrence that uses the fact that six simultaneously infectious vertices require all infections before any recovery. It does not call the general symbolic checker.

The classification is finite and exhaustive only through five vertices. No external certification, unseen-source priority guarantee, or independent audit is asserted.
