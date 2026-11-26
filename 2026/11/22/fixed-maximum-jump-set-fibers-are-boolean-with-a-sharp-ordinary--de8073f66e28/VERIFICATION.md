---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

If a presentation gives T, M and every jump's positive reflected pair belong to T. Each irreducible positive element occurs as a generator in any positive presentation, otherwise its representation splits into two positive elements. An irreducible other than M cannot be 2M since M belongs to T, and cannot be 0; hence its jump is forced and belongs to P_M. Conversely the reflected generators of every proposed jump belong to T and the forced jumps supply all atoms, so the generated semigroup is exactly T. Taking differences with M proves the gcd identity and cofiniteness gives gcd one. Free choices are independent even when two distinct atoms force the same jump, giving the Boolean poset and its rank counts. For H_c the atoms are c through 2c−1; for M≥c the strongest reflection condition is 2M−(2c−1)≥c. If M is below the threshold and no smaller than c, the largest atom's reflected partner is strictly positive and below c. P_M=[1,M−c]; feasible M≤2c makes every lower partner an atom, while M≥2c gives c distinct mandatory jumps and M−2c free jumps. This covers c=1 and the common endpoint M=2c. An independent bounded enumeration confirmed the theorem across 365 observed pairs for M≤12 and the ordinary formulas on a c≤20, M≤60 grid; a direct small check gave 0,1,1,1,2,4 fibers at c=3, M=3 through 8. The supplied script was inspected, not executed. Theorem 1.1 of arXiv:2611.14316v1 depends on M and g(T); Theorem 1.2 depends on M/q and the gap count at −a mod q for q|M. The source uses the same generators including redundant 2M. Finiteness of the fixed fiber gives one common eventual threshold, not equality at every finite degree.

## originality

PASS

The source defines the construction and already recognizes that fixed-M reconstruction can be nonunique. Basic irreducibility gives the proof technique; no novelty attaches to that fact, to the eventual dimension formula or to the prior existential realization theorem. The distinguishing claim is the natural inverse classification at prescribed M, including all presentations and sharp ordinary thresholds and multiplicities; there was no covering statement or stronger classification in the inspected sources.

## value

PASS

The problem is inherited from a specific inverse reconstruction map and the object and parameter are natural. The complete classification replaces a single nonuniqueness example by an intrinsic feasibility test plus an exact set of forced and free jumps and their ranks. The ordinary-family threshold and exponential multiplicity quantify the ambiguity for an infinite, familiar family without claiming more than eventual spectral indistinguishability. This is useful even though the necessary atom argument is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
