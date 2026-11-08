# Scientific review: balanced multipartite two-boson collision loss

## Correctness — PASS

The claim is an all-parameter classification for integer part count \(q\ge3\), integer part size \(m\ge2\), nonzero real uniform hopping, and strictly positive but potentially unequal on-site two-body loss. The single-particle space splits into block-uniform and within-block zero-sum eigenspaces with respective eigenvalues \(m(q-1)\), \(-m\), and \(0\). Their six pairwise symmetrized energy sums are distinct. The exact ranks of the diagonal restriction are \(qr_m\) on the zero-energy sector, \(q(m-1)\) on the negative-one-particle-energy mixed sector, and \(q\) on the other negative-energy sector. The remaining three restrictions are injective. These linear-algebra statements prove completeness, without inferring infinite statements from finite experiments.

The localized capture laws follow from an explicitly evaluated Gram inverse of the diagonal map on \(\operatorname{Sym}^2(\mathbf1^\perp)\), not only from dimension counting. Strict positivity of the loss rates excludes additional purely real no-jump eigenvalues. The finite exact-modular sector ranks and independent orthonormal numerical projectors were replayed from the packaged programs for the parameters documented in VERIFICATION.md. The proof covers the parameter boundaries \(q=3\) and \(m=2,3\).

## Originality — PASS on examined evidence, with residual priority risk

The nearest established mechanisms are dark states associated with quantum-walk degeneracy (Krovi–Brun, arXiv:quant-ph/0606094), the noninteracting two-boson adjacency Kronecker sum and Green functions (Gamble et al., arXiv:1002.3003), and Zeno subspaces for a physically different hard-core nonlocal-loss lattice (Everest et al., arXiv:1406.6097). The two-part complete-bipartite collision-loss calculation covers \(q=2\), not the three distinct dark energy sectors arising for \(q\ge3\). The exact dimension contributions and localized capture laws do not appear as stated or immediately covered special cases in the inspected source material. A historical equivalent published outside the indexed corpus remains possible; the search is not proof of uniqueness.

The stronger-coverage concern is explicit: balanced complete multipartite graphs are strongly regular, so the general noninteracting two-particle propagator framework of Gamble et al. applies. Nevertheless, it does not evaluate an absorbing coincidence detector, its joint spectral kernels, or the stated asymptotic capture probabilities. Computing those requires the separate diagonal-rank and projection analysis supplied here.

## Mathematical value — PASS

A natural dense-network family displays a three-channel division of loss-free states, with a genuinely collective channel appearing exactly at four or more parts. The middle channel has dimension \(q(q-2)(m-1)\) and is absent in the bipartite predecessor. A localized pair can avoid loss across distinct parts even at the minimum size, whereas same-part partial immunity starts only at four vertices per part. The simple exact capture laws provide physical observables beyond a subspace count. The result is an infinite-family classification with a sharp structural boundary, not a routine parameter substitution or a finite table alone.

## Scope and risk

Only uniform nonzero hopping, equal-sized parts, exactly two noninteracting bosons, on-site pair loss, and eventual total capture are addressed. No claim concerns generalized weights, other particle numbers, interactions, or finite-time decay rates. The examined literature and searched public index cannot exhaust all historical variants.

Self-review: passed. Independent audit: not yet performed.
