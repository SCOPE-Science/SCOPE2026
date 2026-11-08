# Mathematical review

## Correctness — PASS
The proof explicitly decomposes real Hermitian matrices into orthogonal diagonal and positive-difference Fourier sectors, including the factors needed for the singular values under normalized continuous-time energy. A sparse-polynomial generalized Vandermonde lemma is proved via Rolle induction and gives exact rank for every distinct set of real Gaussian-bin centers, without a genericity assumption. Difference-counting proves the extremal support law, and the trace-one statement follows from diagonal kernel dimensions, an augmented determinant, an analytic nonzero witness, and a direct symmetric-bin example. The checker additionally constructs independent full matrices and tests 2656 assertions. The finite checks do not establish the theorem without the proof.

## Originality — PASS relative to inspected literature and available mathematical records
The closest contemporary sources establish uniqueness up to global phase for *pure bandlimited signals* with two filtered frequency channels. They do not control the linear lifting of **arbitrary Hermitian matrices**, whose diagonal sector requires more channels, or its exact dependence on each frequency-difference multiplicity. A previously established three-frequency special calculation and classical Chebyshev/Vandermonde interpolation are expressly excluded from novelty claims. Nearby discrete Gabor operator-rank theorems concern different finite cyclic Weyl orbits and do not dominate the arbitrary integer-frequency, continuous-time Gaussian-bin formula. No matching or stronger implication was located in accessible published mathematical-record searches or primary sources, but different terminology in tomography or filter-bank literature remains a specific priority risk.

## Mathematical value — PASS
The full difference-multiplicity law identifies exactly where deterministic Gaussian filtering loses linear information, while the sharp optimality criterion connects sensor count to additive difference geometry. It distinguishes pure-state phase uniqueness from mixed-state information completeness, gives both universal and generic minimum channel counts, and constructs a concrete non-generic trace-one failure. These are natural decision criteria for frequency-filtered sensing, not merely new notation or a finite numerical table.

## Scope and unresolved issues
The frequencies must be distinct integers and time observations span the full circle. Noise sensitivity, spectral bandwidth costs of rank-optimal designs, and classification of general trace-one exceptional sets are unresolved. The self-review is not independent peer review; an equivalent result under another name cannot be excluded conclusively.

Self-review: passed. Independent audit: not yet performed.
