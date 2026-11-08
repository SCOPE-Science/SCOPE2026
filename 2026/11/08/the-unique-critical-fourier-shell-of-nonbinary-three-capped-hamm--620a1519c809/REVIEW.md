# Scientific review

## Correctness — PASS

For each nonconstant character of \((\mathbb Z/q\mathbb Z)^n\), unnormalized convolution with the \(p\)-th power of the clipped Hamming distance has the exact degree-\(k\) eigenvalue
\[\lambda_k(p)=t_k+B_k2^p-(1+t_k+B_k)3^p,\quad t_k=(q-1)n-qk,\quad B_k=[t_k^2-(q-2)t_k-(q-1)n]/2.\]
The second-shell identity follows by expanding the sum of independent coordinate character sums. Consecutive eigenvalue differences have a fixed sign pattern for every \(0<p<1\), because \(2<(3^p-1)/(3^p-2^p)<3\). The unique maximal nontrivial Fourier shell therefore has degree \(k_*\) independent of \(p\). Algebraic endpoint inequalities prove that its eigenvalue is strictly increasing from \(-1\) at \(p=0\) to a positive value at \(p=1\). The proof directly verifies these inequalities for all \(q\ge3,n\ge4\), including the congruence-sensitive \(t_*=-3\) case. Since the critical multiplier continues increasing, no larger exponent can restore negative type. Standard Fourier diagonalization and double centering establish the full endpoint kernel and minimal embedding dimension; an exact Taylor expansion establishes the periodic second-order law.

The independent finite calculation in `CHECK.py` evaluates actual character sums, not only the closed formula, for 701 characters at two exponents and tests 784 parameter pairs. The code is corroborating evidence, not an infinite proof.

## Originality — PASS under bounded literature comparison

The classical Hamming Krawtchouk spectrum and Schoenberg embedding equivalence are prior theory, not originality claims. Murugan, *Generalized roundness of vertex transitive graphs* (arXiv:1112.5657; examined Sections 2–4), provides general negative-type methods and binary graph applications without a clipped nonbinary-product threshold. Brouwer, Cioabă, Ihringer and McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters* (arXiv:1709.09011; examined introduction and Hamming section), optimize individual distance-class eigenvalues, not the mixed kernel \(\min\{d,3\}^p\) or its exponent-uniform optimizing shell. Existing binary clipped-metric classifications concern \(q=2\), which is outside the theorem. Positive-definite Turán-mass results for nonbinary radius-three Hamming balls optimize a different feasibility problem and do not imply conditional negative definiteness of a powered truncated distance.

The bounded searches found no theorem with the same parameter range, clipped metric, exact threshold, shell equality criterion, and second-order residue law. An unrecognized general weighted-association-scheme extremal theorem remains a historical-priority risk; absence in a search index is not proof of novelty.

## Value — PASS

Truncation destroys the coordinate-additive structure of ordinary Hamming distance. Its negative-type threshold is the exact boundary for Hilbert-square-root embeddings and for universal positivity of the corresponding Gaussian kernels, hence a natural quantitative invariant. The theorem classifies every nonbinary alphabet size (including composite sizes) and every dimension at least four. The nontrivial fixed critical Fourier shell, high-multiplicity endpoint degeneracy, explicit minimal embedding dimension, and residue-periodic finite-size correction go beyond an isolated numerical threshold or an obvious reuse of the binary case.

## Scientific limits and sources

No statement is made for unequal alphabet sizes, other clipping radii, or one fixed Gaussian bandwidth. The paper establishes the universal theorem mathematically and gives finite numerical corroboration, not independent proof validation. Primary comparison sources: arXiv:1112.5657 and arXiv:1709.09011; fundamental background: Schoenberg (1938), DOI 10.1090/S0002-9947-1938-1501980-0.

Self-review: passed. Independent audit: not yet performed.
