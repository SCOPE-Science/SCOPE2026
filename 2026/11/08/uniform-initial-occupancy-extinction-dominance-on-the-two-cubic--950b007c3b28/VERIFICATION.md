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

# Mathematical verification

The standalone `verify.py` requires Python 3 and SymPy. From the extracted package, run `python verify.py`.

For the two explicit six-vertex nine-edge graphs, the code enumerates every one of the 720 vertex permutations and constructs the nine- and twelve-state automorphism orbit generators over exact rational functions of the colonization rate. It symbolically verifies the two complete-initial-occupancy formulas and exact difference. It then computes the full orbit-value vectors and forms their uniform averages across all subsets of each cardinality from one to six, verifying six symbolic gap identities, including all four distinct, explicitly printed polynomial certificates and their strictly positive coefficients.

For each graph separately, it constructs the unreduced exact 63-state Markov-chain generator at rational rates \(1/3,1,3\); each system is inverted over the rational numbers. All 36 count-by-rate-by-graph exact-value comparisons agree with the orbit-derived symbolic expressions. At zero colonization the graph-independent \(k\)-th harmonic expectation follows from pure death rates.

The infinite positive-parameter interval is proved by the exact rational-function identities and positive-coefficient signs, not by finite case testing. The checks do not establish ordering for individually prescribed subsets, nonuniform death rates, or non-Markovian dispersal. Human/independent audit has not been performed.
