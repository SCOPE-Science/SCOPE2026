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

Uniform states are fixed, so immediately before the first nonuniform symmetry of an asymmetric orbit the input is still asymmetric. For a repeated d-letter output, paths on successive pairs of predecessor bits align with the indexed output by using the center of each triple; one d-step edge retains its full path multiplicity. A cyclic preimage corresponds exactly to a closed walk in this block multigraph. The 52-case lemma excludes both multi-vertex cycles and multiple loops at a vertex. Every closed walk therefore repeats the same concrete block lift, making its preimage d-periodic no matter how many output blocks are repeated. For d>=6, the repeated block 000 followed by d−3 ones is fixed and has least period d (one zero-run start per block). Swapping sites 2 and 3 in one copy changes only four centers, whose new triples 001, 010, 101, 011 give 0,0,1,1 as required. Every hypothetical period of the predecessor would be a period of the output by equivariance, hence a multiple of d; this would move the unique modified block, impossible. The largest proper divisor is n/p_min(n), including 1 for prime n. This accounts for n>=3, every eligible period, and all positive times.

## originality

PASS

The supported distinct claim is the sharp nonconstant spatial symmetry threshold for Rule 232 and the accompanying all-repetitions short-period rigidity and one-step constructions. Neither generic equivariance, temporal classification, aggregate cyclic preimage spectra, nor the inspected prior string-count formulas supply this joint spatial classification. The pair-graph method itself is prior.

## value

PASS

The canonical spatial stabilizer and standard majority dynamics give a natural existence problem at all finite ring lengths. The sharp obstruction distinguishes composite lengths that sometimes permit symmetry birth from composite lengths that do not; it gives a reusable rigidity criterion for short-period targets on arbitrarily long rings and an explicit predecessor for every longer eligible period. This is not merely a temporal settling or image count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
