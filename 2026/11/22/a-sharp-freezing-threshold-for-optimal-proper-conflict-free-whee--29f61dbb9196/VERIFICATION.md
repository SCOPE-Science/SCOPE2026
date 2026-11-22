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

# Reproducible checks and their scope

Run `python3 verify.py` in the package directory. It requires Python 3 standard library only. The program constructs the literal wheel graph, validates properness and open-neighbourhood witness multiplicities for every rim assignment from three named rim colours, builds the single-vertex recolouring adjacency, and determines connected-component sizes for every rim length from 3 through 11. It also separately validates the singleton-rim criterion on all proper rim assignments.

Actual replay produced the following numbers (the reconfiguration graphs have four hub-colour components with the same structure):

```
RIM=3 PCF4=24 COMPONENTS=24 SIZES=Counter({1: 6}) EDGES=0
RIM=4 PCF4=48 COMPONENTS=48 SIZES=Counter({1: 12}) EDGES=0
RIM=5 PCF4=120 COMPONENTS=8 SIZES=Counter({15: 2}) EDGES=120
RIM=6 PCF4=144 COMPONENTS=24 SIZES=Counter({6: 6}) EDGES=144
RIM=7 PCF4=168 COMPONENTS=168 SIZES=Counter({1: 42}) EDGES=0
RIM=8 PCF4=192 COMPONENTS=192 SIZES=Counter({1: 48}) EDGES=0
RIM=9 PCF4=216 COMPONENTS=216 SIZES=Counter({1: 54}) EDGES=0
RIM=10 PCF4=240 COMPONENTS=240 SIZES=Counter({1: 60}) EDGES=0
RIM=11 PCF4=264 COMPONENTS=264 SIZES=Counter({1: 66}) EDGES=0
VERIFY_OK
```

A value such as `SIZES=Counter({15: 2})` counts components for one fixed hub colour; `COMPONENTS=8` counts all four hub choices. This distinction is intentional. The finite execution verifies the small exceptional cases and several larger instances; only the structural argument in `RESULT.md` proves the claim for arbitrary rim order. The literature comparison and the proof have received self-review, not independent certification.
