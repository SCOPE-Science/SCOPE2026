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

# Reproduction and mathematical scope

Execute `python3 diamond.py` and `python3 diamond_quotients.py` with Python 3 and SymPy. Both programs carry their full graph data, generators, signs and matrix construction in their source files and require no network or other research files.

The first program checks \(d^2=0\), exact rational differential ranks, signed involution relations and intertwining with \(d\); it computes all four cohomology characters and multiplicity sequences. The second program independently builds invariant cochain bases as signed group-orbit sums and calculates all quotient Betti vectors using exact rational ranks. Their recorded outputs are included, and the independent outputs equal those implied by character averaging for all degrees zero through nine.

The computations are exhaustive for the specified nine-generator Chevalley–Eilenberg algebra, but their results do not address arbitrary graphs, integral torsion, the cup-product algebra, or publication priority. Nomizu's theorem and rational invariant-cohomology transfer are the theoretical bridges used in the proof. Independent mathematical audit has not been performed.
