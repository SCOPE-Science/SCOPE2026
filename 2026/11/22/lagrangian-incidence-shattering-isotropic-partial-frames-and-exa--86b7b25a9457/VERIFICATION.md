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
# Reproducibility and verification

The universal theorem is proved by isotropic extension and exact orthogonal-complement counts, not inferred from finite experiments. The rank-one case starts from the three isolated nonzero binary vectors. In binary rank two, the full family has 15 Lagrangians and the shattering complex has face counts \((1,15,45)\), augmented boundary ranks \((1,14)\), and reduced \(\widetilde\beta_1=31\). In binary rank three, 135 Lagrangians produce \((1,63,945,3780)\) faces, augmented boundary ranks \((1,62,883)\), and only \(\widetilde\beta_2=2897\). These ranks arise from actual binary Gaussian elimination of signed simplicial boundaries reduced modulo two.

The first implementation independently enumerates binary Lagrangian spans, builds Boolean traces, and reduces boundary matrices; the C++17 implementation separately enumerates generating tuples and their spans, rederives traces, and computes ranks. They both check their face lists against the symplectic pairwise-orthogonality and linear-independence criterion rather than assuming it. A distinct odd-field implementation verifies the ternary rank-two instance of 40 Lagrangians, 80 shattered singleton supports and 960 pairs.

Run from the directory containing this file:

```sh
python3 checks/lagrangian_check.py
python3 checks/lagrangian_q3.py
c++ -std=c++17 -O2 checks/lagrangian_independent.cpp -o lagrangian_check
./lagrangian_check
```

The computational checks verify exactly the stated small cases, not the universal proof or claims about integral homology and higher-rank topology. The classification is internally reviewed but has not received independent mathematical validation.
