# Self-review

## Correctness — PASS

The proof establishes the random batch as a scaled orthogonal projector, derives the permutation-averaged squared update, obtains the necessary-and-sufficient second-moment stability interval and invariant covariance, and uses a conditional Gaussian mixture to derive both the unique reflection resonance and the strictly positive fourth-moment defect. Exact rational partition enumeration checks small cases without substituting finite experiments for the proof.

## Originality — PASS, qualified

Jin–Li–Liu (2018), Jin–Li–Ye–Zhou (2022), and Ye–Zhou (2022) study the random-batch algorithm and long-time approximation behavior. Xu–Zhao–Zhou (2024) analyze force-covariance variance reduction. The inspected primary material does not contain the full all-size Gaussianity resonance and fourth-defect theorem. Equivalent results elsewhere in random-affine-recursion theory remain a publication-precedence risk; the general Gaussian-mixture lemma itself is not claimed as new.

## Value — PASS

The exact distributional-shape frontier isolates a real issue in particle sampling that cannot be diagnosed from covariance or error-rate bounds alone. The invariant law has an explicit covariance at every stable step, but is Gaussian only at a single reflection step. A universal positive fourth-defect lower bound gives a substantive, parameter-explicit certificate. The resonant Gaussian is not claimed to equal the interacting Gibbs target.

## Reproducibility and limitations

Run `python3 verify_random_batch.py` from the same directory. The checker uses only Python's standard library and exact rational arithmetic. The theorem is restricted to independent uniform equal-size batches, a linear attractive interaction, independent full-rank Gaussian forcing and the fully discrete Euler update; fourth moments may be infinite outside a uniformly contractive subregime.

Self-review: passed. Independent audit: not yet performed.
