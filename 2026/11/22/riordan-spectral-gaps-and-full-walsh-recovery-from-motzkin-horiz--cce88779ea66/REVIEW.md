# Self-review

## Correctness — PASS

The claim has a complete all-length proof for the ordinary one-bit horizontal-position profile of Motzkin excursions. It follows from the exact Catalan profile count, the signed half-line transfer identity, the entrywise nonnegative operator \(B=A^2-I\), and the conjugation symmetry of \(A\). The difference identity proves radial weak monotonicity; the central coefficient is exactly the positive Riordan count for each \(n\ge4\). Direct treatment of lengths zero through three supplies the only zero modes. Walsh diagonalization establishes the ranks and exact \(\ell^2\) condition numbers. The standalone program passed 18,430 independent exact assertions but does not replace the infinite proof.

## Originality — PASS, bounded by inspected records

The closest classical sources are Chen–Deng–Yang (2006, arXiv:math/0602298), which supplies Riordan-path enumeration and a recurrence, and Sun–Ma (2013, arXiv:1305.2015), which uses global height-dependent Motzkin weights and Riordan-array minors. Their inspected texts do not establish a Boolean position-character sign classification, all-order zero-free recovery, or the sharp Riordan spectral gap. A separately recorded finite Motzkin Fourier census studies the full two-bit up/down encoding at length ten; its diagonal restriction is mathematically related, but its finite two-bit rank result neither states nor logically entails the all-length theorem. Targeted searches using flat/horizontal positions, signed Motzkin walks, Riordan numbers, Catalan moments and Fourier/Walsh terminology found no direct matching theorem.

Risks: generalized multivariate Motzkin-weight enumerations or earlier unpublished character calculations might subsume the position-dependent Fourier claim. Search nonappearance is not a proof of priority. The finite two-bit census was compared by its recoverable claim, not revalidated; no claim is made that its entire supplementary source was inspected.

## Value — PASS

Horizontal-step masks are a canonical compressed observable of Motzkin excursions; their counting distribution has Catalan multiplicities and thus nontrivial information about the underlying paths. Unlike a bare parity observation, the theorem gives a full all-size spectral sign pattern, a precise two-length singularity classification, the exact optimal Fourier deconvolution gap in classical Riordan numbers, and positive definiteness at even lengths. This settles a natural recoverability question for infinitely many even-cardinality path ensembles as well as odd-cardinality ones. The factorization of the signed transfer through a nonnegative Riordan-walk operator is the structural reason behind the sharp result.

## Scientific scope and limitations

The result uses the unnormalized Boolean convolution of the **horizontal-step profile with multiplicity**, not a zero-one indicator of the set of admissible masks and not the full two-bit up/down embedding. It does not extend automatically to local-height weights or arbitrary Motzkin restrictions. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
