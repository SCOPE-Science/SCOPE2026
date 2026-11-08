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

## Executed checks

The two embedded Python 3 programs were executed from the included paths. `verify_heawood.py` enumerated all induced triples, all 5985 possible four-edge subsets, every seven-class exact cover, all 336 Fano-incidence automorphisms and their six coloring orbits. It output 84 valid three-matchings, zero induced four-matchings, 416 exact covers after 5531 recursion nodes, orbit sizes \(8,16,56,112,112,112\), and a Burnside fixed-point sum of \(2016\).

The independent program `verify_heawood_independent.py` built the Fano plane using modular differences, built the graph and edge-conflict relation directly, used a separate recursive cover enumerator, constructed all graph automorphisms via all seven-point permutations and an explicit duality and independently reproduced all numeric counts and orbit sizes. Each script asserts the expected findings. Their actual outputs are included as `verification_main.json` and `verification_independent.txt`. Every contained claim is finite and bounded; none uses an incomplete computation to infer an infinite theorem.

## Reproduction

Run the two programs as specified in `RESULT.md`, using only the Python standard library; no external package is required. The first output also contains concrete representatives for all six automorphism orbits and a SHA-256 of a canonical list of all 416 partitions.

## Limits

This provides explicit computational proof of a finite exact classification subject to review of its small self-contained search programs. It makes no claim of external or independent scholarly audit, and its historical-priority assessment remains qualified.
