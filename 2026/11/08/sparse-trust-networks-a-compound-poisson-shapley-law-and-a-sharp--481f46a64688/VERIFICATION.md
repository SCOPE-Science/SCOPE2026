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

# Verification performed

Run `python3 verify.py` from the extracted files. Only the Python standard library is needed. This checker reads each coalition's internal arcs and externally supported vertices independently of the stated formula; it computes all Shapley marginals exactly as rational numbers. It checks every labeled loopless directed graph of order 2, 3 and 4 (4, 64 and 4096 graphs), all vertices, and efficiency. It constructs the independent-binomial sum distribution by convolution at edge probability 1/3 and compares every probability mass to the exhaustive graph enumeration, as well as the zero-credit mass and mean. It prints three finite-network values illustrating that the expected excess of nonisolated zero-credit players over isolated vertices decreases near the critical window.

Observed output:
```
n=2: 4 complete labeled directed graphs, 2 exact root-payoff values, P(phi=0)=2/3, E(phi)=1/3
n=3: 64 complete labeled directed graphs, 9 exact root-payoff values, P(phi=0)=256/729, E(phi)=2/3
n=4: 4096 complete labeled directed graphs, 33 exact root-payoff values, P(phi=0)=85184/531441, E(phi)=1
critical n=1000: expected null=1.110211, expected isolate=0.994976, difference=0.115236
critical n=10000: expected null=1.045883, expected isolate=0.998801, difference=0.047083
critical n=100000: expected null=1.018150, expected isolate=0.999784, difference=0.018366
All exact checks passed.
```

The finite checks do not establish the Poisson or empirical weak limits, which are established by the proof in `RESULT.md`. The theorem is not claimed for correlated arcs or arbitrary trust weights. Independent validation has not been performed.
