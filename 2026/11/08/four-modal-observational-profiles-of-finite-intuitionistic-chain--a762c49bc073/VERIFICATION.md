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

# Verification and limits

The threshold equalities in the proof are algebraic equalities for all \(n\ge1\), all binary relations, all upset inputs, and all fixed worlds. Their validity does not depend on finite testing. The reconstruction threshold, \(2n\) sparse-representative bound, and lower bound \(9^{n-2}2^{n^2-4n+2}\) for \(n\ge4\) likewise have direct proofs in `RESULT.md`.

The exact finite table is reproducible using `checks/profile_census.cpp`. Compile with a C++17 implementation and run it; the program enumerates all \(1+n(n+1)/2\) row types for each of up to five rows, weighting each nonempty type \((a,b)\) by the exact number of relations having those extrema. It groups every type vector by four running-extremum profiles, reports both the distinct-class count and largest weighted fibre, and checks the invariant total of \(2^{n^2}\) relations. Its 60-bit integer encoding is lossless for the stipulated maximum of five worlds because all \(4n\) profile values use three bits after shifting the \(b\)-profiles by one.

An independent implementation, `checks/direct_semantics.py`, directly evaluates each of the four quantified modal clauses over every upset, every world, and every relation for chain lengths \(1\) through \(4\). It does not use row-extremum profiles to construct its observational signature. In completed executions both checkers returned the overlapping counts \((2,16,279,7171)\) and largest fibres \((1,1,8,324)\). The fifth row \((235152,93312)\) is supplied by the complete weighted enumeration, not by direct enumeration in the second checker. The exact analytic large-fibre example gives \(93312\) on five worlds as an independent lower-bound witness; maximality there is the exhaustive part.

No independent mathematical audit or historical-priority validation has been performed. No theorem is claimed for infinite orders or for a closed all-length quotient count.
