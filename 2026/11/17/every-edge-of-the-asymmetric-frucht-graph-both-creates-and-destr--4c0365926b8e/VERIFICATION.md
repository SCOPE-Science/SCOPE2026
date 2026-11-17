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

# Reproducibility

This finite result was checked with two distinct Python 3 standard-library programs included in this package: `enumerate_forward.py` and `enumerate_functional_graph.py`.

From a directory containing the two programs, execute:

```
python3 enumerate_forward.py > forward.json
python3 enumerate_functional_graph.py > functional.json
python3 - <<'PY'
import json
with open('forward.json', encoding='utf-8') as f: a=json.load(f)
with open('functional.json', encoding='utf-8') as f: b=json.load(f)
assert a['edges']==b['edges_original_labels']
assert a['runs']==b['runs']
assert len(a['runs'])==19
assert a['runs'][0]['unanimity']==1240
assert all(x['new_consensus_initials']>0 and x['lost_consensus_initials']>0 for x in a['runs'][1:])
assert sum(x['delta_unanimity']>0 for x in a['runs'][1:])==11
assert sum(x['delta_unanimity']<0 for x in a['runs'][1:])==7
assert max(x['maximum_entry'] for x in a['runs'])==8
print('All 19 complete censuses and headline checks agree.')
PY
```

The exact original output files are `forward.json` and `functional.json`. The first program explicitly follows every input until it first satisfies the period-two relation, with an assertion bounding that search; the second uses a full functional-graph cycle decomposition. The second uses a different graph encoding (Hamiltonian LCF) and an independent three-input Boolean-majority implementation. Both include all 4,096 inputs to each of 19 systems. The original graph's 12 fixed states, 268 primitive-two states, seven-step maximum, and the signed gain/loss table agree. Direct update conditions and exhaustive coverage are part of the program source, not inferred from output logs alone.

The statement is exact only on these finite graphs. No completeness assertion beyond this finite state domain, independent audit, or priority certification is made.
