# Scientific review of the heterogeneous Hamming-product FMMC theorem

## Correctness — PASS

The proof establishes the global bound, not only a symmetric-class optimum: averaging under independent coordinate-symbol permutations cannot increase \(\|P-J/N\|_2\). The averaged kernel has exactly \(d\) free coordinate weights, with the complete feasibility constraint \(\sum_i(1-1/q_i)x_i\le1\). Tensor zero-sum/constant eigenspaces yield eigenvalues \(1-\sum_{i\in S}x_i\) for all subsets. The worst nonconstant modulus equals \(\max\{1-\min_i x_i,\sum_i x_i-1\}\). The capacity constraint and sum bound imply the exact one-variable minimax lower bound, which is attained by equal coordinate relaxation rates. Equality conditions establish uniqueness *only within the invariant class*. The holding threshold and the equal-edge benchmark are checked algebraically. The standalone exact-rational program verifies representative finite cases; the universal result comes from the written proof.

## Originality — PASS on inspected evidence, qualified

Boyd–Diaconis–Parrilo–Xiao (arXiv:0709.0955, Sections 2.2, 3.2, 3.3.3) provide the underlying averaging framework and solve uniform-alphabet Hamming graphs and some edge-transitive products, but give no closed all-heterogeneous-alphabet formula, equalized-coordinate-rate rule, or associated holding-threshold statement. Boyd–Diaconis–Xiao (SIAM Review 46, 2004) establish the general SDP formulation, not the present explicit solution. Earlier two-distance Hamming-walk and coordinate-control results concern different support or objective constraints. The key distinction is between a general algorithmic reduction and an exact evaluated optimum across an unlimited number of unequal coordinate sizes; known homogeneous instances are acknowledged rather than claimed new. Remaining risk: specialized literature on mixed-alphabet product chains may have given an equivalent result under different terminology. Search evidence supports a qualified assessment, not a proof of publication priority.

## Mathematical value — PASS

Mixed alphabet products are natural state spaces for discrete product sampling and coordinate-update consensus. Optimizing the spectral SLEM under single-coordinate move support has a clear design interpretation. The exact global solution shows that per-edge rates must be inversely proportional to alphabet size, identifies a sharp change from positive optimal holding to zero holding, and quantifies an arbitrarily large relative relaxation advantage: on \(K_2\square K_Q\) the unrestricted contraction stays at \(1/3\), while the best uniform-edge contraction tends to \(1\). This is a complete structural solution in arbitrary dimension and unequal alphabet sizes, not a cosmetic parameter substitution or isolated small-graph computation.

## Closest literature and limitations

- S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955, first public 2007-09-06. The homogeneous Hamming-graph formula and symmetry-reduction theorem are prior work.
- S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), DOI: 10.1137/S0036144503423264. General SLEM optimization is prior work.

The proof does not address nonreversible chains, nonuniform target measures, multi-coordinate jumps, optimal finite-time total-variation distance, or uniqueness of all unsymmetrized minimizers. Independent mathematical validation remains to be done.

Self-review: passed. Independent audit: not yet performed.
