# Independent scientific audit — SCOPE-20260921-efe7f86dd392

Audited at: 2026-10-01T23:13:29.436856Z

Disposition: **failed**

## Correctness — PASS

The negative-integer polylogarithm identity gives the Eulerian quotient exactly. The low indices \(0,1,2\) are positive discrete Laplace transforms. For every \(i\ge3\), an Eulerian zero in \((-1,0)\) is simple and cannot cancel in the next polynomial by the Eulerian differential recurrence; under \(z=e^{-t}\) it becomes a pole in \(\Re t>0\), impossible for a completely monotone Laplace transform. The logarithmic statements follow from the explicit \(i=1\) logarithmic derivative and the same numerator-zero obstruction for \(i=2\).

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_eulerian_ratio.py
- Wei--Guo 2014

### Correctness risks

- The symbolic artifact is supplementary; the infinite classification rests on the analytic Eulerian-zero argument.

## Originality — FAIL

A published SCOPE record dated 2026-09-20, one day before the assigned record, already proves the exact complete-monotonicity cutoff \(i\le2\) for both Wei--Guo ratio families by the same Eulerian-polynomial zero and right-half-plane pole mechanism, including the same first pole at \(i=3\). The assigned logarithmic-complete-monotonicity add-on is a short derivative/pole corollary of the same formulas and does not rescue the final package as a distinct original theorem.

### Equivalent formulations

The assigned main theorem is an exact duplicate in equivalent notation.

### Broader coverage

The assigned record is not broader in its main claim; its logarithmic classification is an ancillary strengthening that follows immediately from the same low-index formulas and pole idea.

### Exact database or table

This exact prior theorem is decisive coverage rather than a database coincidence.

### Claim versus prior implication

The complete-monotonicity classification is directly covered; the remaining log-CM observation is routine from those same identities.

### Sources inspected

- Exact cutoff in the Wei--Guo complete-monotonicity conjecture — published SCOPE 2026/09/20/wei-guo-ratio-conjecture-cutoff--03d0cbb94677. COVERING: It contains the assigned main classification and proof mechanism.
- Complete Monotonicity of Functions Connected with the Exponential Function and Derivatives — https://doi.org/10.1155/2014/851213. OPEN_PROBLEM_SOURCE: It poses the all-index complete-monotonicity conjecture; the earlier SCOPE theorem already resolves it.

### Checked sources

- published SCOPE 2026/09/20/wei-guo-ratio-conjecture-cutoff--03d0cbb94677
- Wei--Guo 2014
- Resultary semantic search

### Residual risks

- No literature uncertainty can restore originality of the complete-monotonicity cutoff against the explicit earlier published theorem.

## Value — FAIL

The main scientific contribution is already published in the same corpus with the same structural proof. The added logarithmic cutoff is a short corollary of the same low-index formulas and pole obstruction, so this package is best treated as redundant rather than as a separate motivated research result.

### Value sources

- published SCOPE 2026/09/20 exact-cutoff theorem

### Value risks

- The logarithmic classification may be useful exposition, but usefulness does not make the duplicate package a distinct validated finding.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The complete-monotonicity cutoff is already covered by an earlier published theorem.
- The logarithmic-complete-monotonicity add-on does not justify retaining the duplicate package as a separate finding.
