---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For bi-infinite periodic nonconstant binary words, run differentiation gives a primitive circular derivative. A primitive inverse alternates two symbols and uses one run-length period for even derivative period or two for odd; the inverse least period equals the corresponding sum. Every X1 primitive derivative avoids cyclic 111/222, forcing at least one symbol 2 per three positions, so inverse length grows at least 4/3. Any depth-ten period <=269 descends nine steps to an X1 primitive period <=floor(269(3/4)^9)=20. I independently enumerated all primitive oriented binary necklaces without cyclic triples at length 2..20 and expanded every retained inverse orientation, pruning only lengths>269; 2170 seeds, level counts [2170,3474,5632,9073,11218,5590,2666,300,32,16], least period counts [(2,1),(3,2),(8,1),(12,2),(18,4),(27,8),(80,4),(120,8),(180,16),(269,16)]. This reproduces the exact first-ten table with a genuinely exhaustive finite cutoff for each claimed depth, not an inference that any infinite-depth word is periodic. The proof's distinct rotation/complement handling is necessary and present.

## originality

PASS

Best-of-knowledge PASS for the motivated finite-depth primitive-period and minimizing-orbit census, not for the established differentiation hierarchy or elementary run-length inversion. Full relevant Kolakoski/smooth-word primary introductions and mathematical sections checked; Resultary search returned the same claim but no stronger covering Kolakoski-period census.

## value

PASS

The natural derivative-depth filtration X_k poses a concrete primitive periodic-orbit systole question that is not a textbook substitution. A proved growth cutoff makes the finite-depth classification complete, and exact periods and counts through ten (especially sharp 269 with sixteen oriented orbits) are reusable finite combinatorics for smooth-word and symbolic-dynamics comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
