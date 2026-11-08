# Universal spectrum and exact relaxation of exchangeable partial-permutation shuffles

## Finding
Fix an integer \(n\ge 2\). At every step of a Markov chain on the permutations of \(n\) distinct cards, independently choose a random subset size \(K\in\{0,\ldots,n\}\) with arbitrary probabilities \(w_k\); choose a uniform \(K\)-subset of positions; and replace the arrangement on those positions by a uniformly random permutation, leaving every other position unchanged. The same size law is used on every step.

For a partition \(\lambda\vdash n\), write \(f^\lambda\) for the number of standard Young tableaux of shape \(\lambda\), and \(f^{\lambda/(k)}\) for the number of standard Young tableaux of the skew diagram obtained by deleting the leftmost \(k\) cells of the first row; set this number to zero if \(k>\lambda_1\), and use \(f^{\lambda/(0)}=f^\lambda\). The complete transition spectrum, counted with multiplicity, is
\[
\eta_\lambda=\frac{1}{f^\lambda}\sum_{k=0}^n w_k f^{\lambda/(k)},
\qquad \text{multiplicity }(f^\lambda)^2.
\]
Coincident numerical eigenvalues have their multiplicities added. All eigenvalues lie in \([0,1]\). The largest eigenvalue is one, arising from \(\lambda=(n)\), and the largest *nontrivial* eigenvalue is attained by \(\lambda=(n-1,1)\):
\[
\eta_* = \frac{n-\mathbb E K-w_0}{n-1},
\qquad
\operatorname{gap}(P)=\frac{\mathbb E K+w_0-1}{n-1}.
\]
The spectral gap is strictly positive precisely when \(\Pr(K\ge2)>0\), which is also precisely the irreducibility condition. In the Bernoulli marking model, where positions are independently selected with probability \(p\in[0,1]\), this specializes to
\[
\operatorname{gap}(P)=\frac{np+(1-p)^n-1}{n-1}.
\]
For a fixed size \(K=k\), the gap is \((k-1)/(n-1)\) for \(k\ge1\), with the frozen \(k=0\) case having gap zero. Hence an entire family of exchangeable selection laws has its exact relaxation rate determined by only two statistics, \(\mathbb E K\) and \(\Pr(K=0)\), even though their other eigenvalues may differ.

## Assumptions and scope
The probability distribution \((w_0,\ldots,w_n)\) is arbitrary, nonnegative, and sums to one. Position subsets are sampled uniformly conditional on their size. The internal rearrangement on the chosen subset is fully uniform, independent of past states and future steps. No bounds on \(n\), nondegeneracy, or regularity of \(w\) are required. By “nontrivial eigenvalue” we mean eigenvalues of irreducible representation sectors other than the trivial representation, even if the chain is reducible; in that case the value may be one. The gap is the Markov operator's \(L^2\) spectral gap; it is *not* a claimed total-variation mixing-time formula.

## Proof
**Centrality and nonnegative Fourier spectrum.** For a set of positions \(S\), let \(H_S\) be the subgroup of all permutations supported on \(S\). A uniform average over \(H_S\) is an orthogonal projection in every unitary representation of the symmetric group. Write the one-step measure as the mixture of these subgroup averages, first over the uniform sets of a prescribed size and then over \(w\). For fixed \(k\), conjugation by any permutation sends \(H_S\) to \(H_{gS}\), so the average over all \(k\)-subsets is central. Thus every irreducible representation \(\lambda\) receives a scalar \(\eta_\lambda(k)\), nonnegative because it is an average of orthogonal projections.

**Branching calculation.** The trace of the uniform average over any one subgroup \(H_S\cong S_k\) on the irreducible representation \(V^\lambda\) equals the dimension of its \(S_k\)-fixed subspace. Successive Young branching from \(S_n\) to \(S_k\) identifies that dimension with \(f^{\lambda/(k)}\): the trivial \(S_k\) representation corresponds to the horizontal partition \((k)\), and the rest of the branching path is a standard tableau of \(\lambda/(k)\). Dividing the trace by \(f^\lambda\) gives \(\eta_\lambda(k)=f^{\lambda/(k)}/f^\lambda\). Averaging over \(w_k\) gives the asserted eigenvalues. The regular representation contains \(f^\lambda\) copies of \(V^\lambda\), giving multiplicity \((f^\lambda)^2\).

**A sharp tableau inequality.** For every \(\lambda\ne(n)\) and \(1\le k\le n\),
\[
\frac{f^{\lambda/(k)}}{f^\lambda}\le\frac{n-k}{n-1}.
\]
To prove this, choose a uniformly random standard tableau of shape \(\lambda\), and let \(E_k\) be the event that entries \(1,\ldots,k\) lie in the first row. Standard tableau order immediately gives \(\Pr(E_k)=f^{\lambda/(k)}/f^\lambda\), and \(\Pr(E_1)=1\). Conditional on \(E_k\), with \(1\le k<n\) and positive conditional probability, the remaining cells form the skew poset \(\lambda/(k)\) with \(N=n-k\) cells. The cell in second row, first column is a minimal element because its only possible predecessor has already been removed. In any finite poset of size \(N\), a specified minimal element has probability at least \(1/N\) to be first in a uniform random linear extension: writing \(c_j\) for the number of extensions in which that element is at position \(j\), swapping it with the immediately preceding element gives an injection from extensions counted by \(c_j\) to those counted by \(c_{j-1}\), so \(c_1\ge\cdots\ge c_N\). The next tableau entry is in the first row only if this second-row minimum is not first. Therefore
\[
\Pr(E_{k+1}\mid E_k)\le 1-\frac1{n-k}.
\]
Multiplication from \(k=1\) yields \(\Pr(E_k)\le (n-k)/(n-1)\). If \(E_k\) has zero probability, later cases are trivial. In shape \((n-1,1)\), after its first \(k\) top-row cells are removed, the sole second-row cell is incomparable with every remaining top-row cell. It is exactly uniformly positioned among the \(n-k\) remaining tableau entries, giving equality at each positive step, and equality in the displayed bound for every \(k\).

**Top nontrivial eigenvalue and examples.** Combining the sharp inequality with nonnegative \(w_k\) shows that \(\eta_\lambda\le\sum_k w_k(n-k)/(n-1)\) for \(\lambda\ne(n)\) when \(k\ge1\), while for \(k=0\) every ratio is one. Shape \((n-1,1)\) attains all upper bounds simultaneously. Simplifying yields \(\eta_*=(n-\mathbb E K-w_0)/(n-1)\). Since \(\eta_*\le1\) and the spectrum is nonnegative, the gap follows. A positive probability of selecting at least two positions gives positive probability for every transposition and also for holding, proving irreducibility and aperiodicity; otherwise all moves are identities. Finally substitute the mean and zero-selection mass of a binomial size distribution to obtain the Bernoulli formula.

## Verification
The companion `verify.py` uses only the Python standard library. It independently enumerates all partitions for \(2\le n\le6\), recursively counts the relevant ordinary and skew tableaux, reconstructs the exact conjugacy-invariant one-step probability of every permutation, and compares the first two (and, for \(n\le5\), the first three) spectral trace moments against direct convolution moments. It also checks total probability, positivity, multiplicities, the tableau domination inequality and the top sector for point-mass, binomial and non-binomial size laws. The recorded result is `VERIFICATION_OK 1752 exact rational assertions`. These are finite checks; the proof covers all integers \(n\ge2\).

For reproduction, run `python3 verify.py` from the extracted package directory; no network or nonstandard libraries are required.

## Relationship to prior work
Pittel's 2025 investigation of partially resampled permutations uses the same one-step independent marking and uniform internal permutation, but studies the expected number of records for an arbitrary starting deck rather than iterates, the full Markov spectrum or relaxation. Nestoridi–Priestley–Schmid analyze uniform random shuffling of *consecutive* blocks of a fixed size, a noncentral kernel with different spectral behavior. Hermon–Pymar analyze uniform-interchange dynamics on general hypergraphs and derive comparisons and bounds for spectral gaps, rather than the complete exact spectrum for a uniform mixture of complete hyperedges. Bate–Connor–Matheau-Raven derive representation-theoretic spectral results for one-sided *transpositions* with a distinct transition measure. General symmetric-group Fourier analysis and Young branching are classical tools used in the proof, not claimed new.

## Limitations
This theorem does not establish an optimal total-variation cutoff, a mixing profile, a spectral formula for nonexchangeable subset selection, or universality when the within-subset permutation is not uniform. Its finite exact checker is not an infinite proof. The originality comparison cannot rule out an older, more general character-theoretic or complete-hypergraph interchange theorem implicitly covering this precise spectrum and gap; historical priority needs independent review. The structural conclusion is the explicit finite-size spectrum and the exact universal spectral-gap reduction under the stated kernel.

## References
- B. Pittel, *Counting records in a random, non-uniform, permutation*, first publicly posted January 12, 2025, arXiv:2501.06905, https://arxiv.org/abs/2501.06905.
- E. Nestoridi, A. Priestley, D. Schmid, *The S_k shuffle block dynamics*, first posted April 5, 2023, arXiv:2304.02588, https://arxiv.org/abs/2304.02588.
- J. Hermon, R. Pymar, *A direct comparison between the mixing time of the interchange process with "few" particles and independent random walks*, first posted May 27, 2021, arXiv:2105.13486, https://arxiv.org/abs/2105.13486.
- M. E. Bate, S. B. Connor, O. Matheau-Raven, *Cutoff for a One-sided Transposition Shuffle*, first posted July 28, 2019, arXiv:1907.12074, https://arxiv.org/abs/1907.12074.
