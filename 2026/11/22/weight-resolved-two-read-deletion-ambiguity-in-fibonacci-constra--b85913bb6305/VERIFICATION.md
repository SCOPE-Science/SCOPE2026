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

Write [a,b] for the first-to-last mismatch. Any single-deletion alignment with the deleted position in x earlier than that in y must cover [a,b]; equality outside [a,b] allows the deletion positions to be moved to a in x and b in y within constant runs, without changing the output. The other orientation gives b in x and a in y. Thus two distinct outputs require both orientations and b>a; the resulting relations x_i=y_(i+1), y_i=x_(i+1) force opposite alternating phases. Conversely the two orientations on such an interval give distinct outputs. In a pair of no-11 sources both external flanks, if present, must be zero. Independence of the two contexts and the unique 0/10 tiling of a zero-ending prefix give P²=(1−z−uz²)^−2. An even interval marks u^t z^(2t), and an odd interval marks z times this, with u tracking the lower weight. Each phase pair contributes once. Extraction and the binomial hockey-stick identity give the claimed counts and zero boundaries. Legal swaps pack any fixed-weight layer (including the singleton at maximal odd-length weight); B>0 joins consecutive positive layers, and the all-zero word is isolated. The positive double pole of A(z,1) is uniquely dominant, giving B/A→φ^−1 and the stated fractions. Independent replay: python3 /workspace/branches/independent_replay.py 5, grouping sources by distinct outputs and testing all layers through n=13. A separate direct deletion-set check extends finite comparisons through n=14; neither substitutes for the proof.

## originality

PASS

Credit the Type-A criterion, the larger Fibonacci hypercube, and its implication for the total unweighted census. The supported refinement is the fixed endpoint-composition edge census for the two-read induced source language, including its boundary and component consequences. The strongest composition match counts unrestricted sources; the strongest constrained matches either count a different overlap threshold or do not keep the weight variables. Same-day indexing does not settle priority.

## value

PASS

Composition is a natural stratification for constrained word families. The exact fixed-composition counts quantify ambiguous pairs within a constant-weight codebook and across its neighboring weights, information not supplied by the total count or by unrestricted-source edge densities. The refinement also resolves which layers meet and gives the preserve/change split. The value is this usable invariant and component structure, not the length of the generating-function derivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
