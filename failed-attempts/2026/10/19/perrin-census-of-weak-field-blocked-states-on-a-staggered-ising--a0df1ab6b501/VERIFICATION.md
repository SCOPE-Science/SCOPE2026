---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The staggered gauge t_i=(−1)^i s_i is compatible with the periodic edge for even n and gives Δ_iH=2t_i[h−J(t_{i−1}+t_{i+1})]. For 0<h<2J the bracket is negative exactly when both neighbors are +1 and positive otherwise. Hence defects are independent and every aligned site has a defect neighbor: this is precisely a maximal independent subset of the labeled cycle. The interdefect distances are 2 or 3. For k defects exactly n−2k of the gaps are long, and marking a defect gives n times the binomial count with k-mark multiplicity, irrespective of rotational symmetry. The three-state gap automaton counts labeled closed paths, with characteristic polynomial x³−x−1 and initial traces 3,0,2. Its nonreal roots have common modulus ρ^(−1/2), yielding log ρ along the even lengths. At h=2J the energy is −nJ+4J times the number of adjacent defect pairs, so all independent sets are ground states and the Lucas comparison is correct; the domination condition is lost. A separately written exact physical-flip census at J=1,h=3/4 tested every spin assignment for n=4,6,…,18, the individual stability equivalence, and every k coefficient; totals were 2,5,10,17,29,51,90,158. Replay: branches/aa7d57d7-bcca-4481-9276-5311771a405f/independent_census_check.py and independent_census_results.txt. The single sampled field does not prove the open-interval assertion; the sign classification does. The supplied verifier was inspected, not run.

## originality

FAIL

The weighted one-spin partition is exactly the fixed-hub sector of the inspected antiferromagnetic wheel theorem, after the staggered gauge. The reduction works across the entire open weak-field interval because changing h to J does not change any local flip sign. Earlier graph theory also already covers the Perrin and 2/3-gap ingredients. This is a mathematical coverage decision, not an inference from catalogue dates or the wheel record's uncited comment about an equivalent chain coding.

## value

FAIL

The model's local-minimum census is a meaningful observable, but this frozen result reproduces an existing weighted partition after taking a hub sector and changing a field without changing any local flip sign. It adds neither a new stability mechanism nor a different counting problem; the endpoint comparison is already known and the only leftover size is elementary. As a standalone contribution it is a routine specialization rather than a new useful exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
