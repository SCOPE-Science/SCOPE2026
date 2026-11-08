# Mathematical review

## Correctness
PASS. The normalization is checked from the full unweighted Gabor matrix rather than inferred from fiber heuristics. Pairing indices at half-period, the even-character sum produces exactly two unit vectors per block, and cyclic wrap changes one phase difference into a phase sum. The resulting integer map has determinant two; over odd phase alphabets it is bijective, and over even alphabets it has precisely the even-parity image. A parity enumerator proves the exact survival distribution. Exhausting nearest-antipodal alphabet letters gives the optimal bound and equality cases, with the binary odd-length degeneracy treated separately. `CHECK.py` provides direct-matrix and exhaustive finite checks, not a substitute for the infinite parameter proof.

## Originality
PASS relative to the accessible source evidence. The closest primary paper, Asipchuk–De Carli–Rodriguez (arXiv:2605.16139), establishes block-equivalence but not finite-alphabet parity laws or optimal quantized tightness. Salanevich–Strachan (arXiv:2509.01325) investigates random Gabor stability with different configurations and estimates, not this exact law. A continuous Haar phase spectral law for this block geometry does not imply the finite-alphabet even-parity constraint or its deterministic optimum. Relevant mathematical-record comparisons on phase-only and Gabor constructions found different operator-span or phase-retrieval objectives, rather than an implication of the claim. Residual risk: a twisted-cycle counting identity may exist under coding or communications nomenclature; novelty is not independently certified.

## Mathematical value
PASS. The exact tail distribution gives finite-dimensional reconstruction-risk probabilities for quantized windows, and the sharp design theorem identifies the minimum phase resolution for perfect conditioning. The transition at alphabet divisibility by four is a genuine arithmetic obstruction invisible to continuous random-phase sampling. The precise constants, extremizer counts and binary impossibility provide actionable sampling-design criteria; the result is limited to a specified square Gabor geometry and uniform finite phase alphabets.

Self-review: passed. Independent audit: not yet performed.
