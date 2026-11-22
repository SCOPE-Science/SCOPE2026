# Self-review

## Correctness — PASS
The all-length support constraint and Fourier normalization are explicit. Direct integer butterfly transforms and independent signed finite-state recurrences agree on every character in all 13 dimensions under study. At dimension 13, the program establishes nullity 1296, rank 6896 and precisely four weight-three zero masks; there are no weight-one/two zeros. The code enumerates the full finite domain, not samples. The auxiliary general run-length parity lemma is derived by rational generating functions.

## Originality — PASS, with bounded historical confidence
Kurmaev (2010), https://arxiv.org/abs/1001.4334, treats run-length restrictions and the DFT of individual coded signals; Rho and Vesel (2016), https://doi.org/10.46298/dmtcs.2165, study the same third-order generalized Fibonacci cubes as graphs and their recognition; Azarija and colleagues (2014), https://arxiv.org/abs/1402.6377, treat isomorphism classes. None of the inspected material establishes this exact coordinate-character nullity and sharp first cubic blind-spot cutoff. The general parity congruence is ordinary enumerator background, not the originality claim. A specialized earlier full signed multivariate enumerator might imply the result and remains a priority risk.

## Value — PASS
This determines a motivated first finite threshold in low-degree Fourier recoverability for a standard constrained interconnection-network code: singularity is present earlier, but degree-three is first needed to witness it at dimension 13. Exact nullity and zero-degree distribution provide a complete reproducible benchmark, without an unsupported claim about future dimensions.

## Scope and limits
The certificate handles dimensions 1 through 13 and does not establish subsequent first-zero degrees or independent publication priority. The full exact verification resides in `check.py`.

Self-review: passed. Independent audit: not yet performed.
