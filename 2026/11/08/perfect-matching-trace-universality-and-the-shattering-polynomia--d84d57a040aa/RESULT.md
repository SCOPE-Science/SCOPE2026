# Perfect-matching trace universality and the shattering polynomial of derangements

## Finding

Fix an integer \(n\ge 2\). Write \([n]=\{1,\ldots,n\}\), and let the instance domain be the off-diagonal board
\[
X_n=\{(i,j)\in[n]^2:i\ne j\}.
\]
For every fixed-point-free permutation \(\pi\) of \([n]\), take the concept \(G_\pi=\{(i,\pi(i)):i\in[n]\}\subseteq X_n\). Denote the concept family by \(\mathcal D_n\).

**Local trace universality.** If \(S\subseteq X_n\) has \(|S|\le n-2\), then
\[
\{G_\pi\cap S:\pi\text{ is a derangement}\}
=\{T\subseteq S:T\text{ is a bipartite matching}\}.
\]
Here a matching is a set of positions with no two in the same row or column. This is a statement about *all* traces, including those on nonmatching supports, not merely a VC-dimension bound.

**Sharp shattering classification.** For every \(S\subseteq X_n\), \(S\) is VC-shattered by \(\mathcal D_n\) if and only if \(S\) is a matching and \(|S|\le n-2\). Thus \(\operatorname{VCdim}(\mathcal D_n)=n-2\), including the boundary case \(n=2\).

Writing \(r_m(n)\) for the number of \(m\)-edge matchings of the crown graph \(K_{n,n}\) with the diagonal perfect matching deleted, the complete shattered-support polynomial is
\[
\Phi_n(z)=\sum_{m=0}^{n-2}r_m(n)z^m,
\quad r_m(n)=\sum_{j=0}^{m}(-1)^j\binom nj\binom{n-j}{m-j}^{\!2}(m-j)!.
\]
All higher coefficients are zero. For example,
\[
\Phi_3(z)=1+6z,\quad
\Phi_4(z)=1+12z+42z^2,\quad
\Phi_5(z)=1+20z+130z^2+320z^3.\]
\[
\Phi_6(z)=1+30z+315z^2+1420z^3+2715z^4.
\]
If \(m=m(n)\) distinct positions are sampled uniformly without replacement from \(X_n\), and \(m/\sqrt n\longrightarrow c\in[0,\infty)\), their shattering probability satisfies
\[
\Pr(S\text{ shattered})\longrightarrow e^{-c^2}.
\]
In particular, \(m=o(\sqrt n)\) gives probability tending to one and \(m/\sqrt n\to\infty\) gives probability tending to zero.

## Assumptions and scope

The two copies of \([n]\) are distinguished as row and column vertices. Concepts are graph sets of *all* derangements, with no empty concept or diagonal position adjoined. All supports are *unordered, distinct* subsets of the off-diagonal board; shattering requires every Boolean trace, including the empty and full traces. The formulas hold for all integers \(n\ge2\). For the sampling limit, sampling is without replacement from the \(n(n-1)\) positions; the case \(m=0\) is permitted.

## Proof

**1. Trace-extension lemma.** Let \(S\subseteq X_n\), \(|S|\le n-2\), and let \(T\subseteq S\) be any matching. Fix the rows and columns matched by \(T\). The residual complete bipartite board has \(k=n-|T|\ge2\) rows and \(k\) columns. The prohibited diagonal cells still present in this board form a partial matching \(D\); complete \(D\) arbitrarily to a perfect matching \(D'\) of the residual complete bipartite graph. This is possible because the graph is complete.

The edges outside \(D'\) partition into \(k-1\) pairwise edge-disjoint perfect matchings: label the remaining rows and columns so that \(D'\) becomes the identity, and take the \(k-1\) nonidentity cyclic shift permutations. Every such matching avoids every residual diagonal cell. At most \(|S|-|T|\le k-2\) further cells are forbidden by \(S\setminus T\); each can meet at most one of those \(k-1\) pairwise edge-disjoint perfect matchings. Hence at least one residual perfect matching avoids *all* cells in \(S\setminus T\) and all original diagonal cells. Joining it with \(T\) gives a derangement whose graph intersects \(S\) in precisely \(T\).

Conversely, the intersection of any perfect matching with \(S\) is itself a matching. These two inclusions prove local trace universality.

**2. Exact boundary.** If \(S\) is shattered, its full trace \(S\) occurs and therefore \(S\) must be a matching. The trace lemma shatters every matching of at most \(n-2\) edges. No matching \(S\) of size \(n-1\) is shattered. To see this, let \(a\) be its unique unused row and \(b\) its unique unused column. If \(a=b\), completing \(S\) would force the forbidden diagonal cell \((a,a)\); thus the full trace does not occur. If \(a\ne b\), row \(b\) is occupied in \(S\), say by \(e=(b,t)\). If a derangement had trace \(S\setminus\{e\}\), the only two residual row-column assignments on rows \(\{a,b\}\) and columns \(\{b,t\}\) would either contain \(e=(b,t)\), or contain the forbidden diagonal cell \((b,b)\). Both contradict the prescribed trace. Thus that trace cannot occur. Since shattering is hereditary, no support of size at least \(n-1\) is shattered. Every matching of size \(n-2\) exists on the off-diagonal board (take \(n-2\) edges of a cyclic derangement), so the VC dimension is exactly \(n-2\).

**3. Counting.** The coefficient \(r_m(n)\) counts size-\(m\) partial permutation matrices with no diagonal entry. Apply inclusion-exclusion to the \(n\) forbidden diagonal cells. For any chosen \(j\) diagonal positions, the number of size-\(m\) matchings containing them is \(\binom{n-j}{m-j}^2(m-j)!\). Summing over the \(\binom nj\) choices with alternating signs gives the displayed formula. The coefficient at degree zero is one; all degrees \(m\ge n-1\) vanish by Step 2.

**4. Random-support transition.** For \(m\le n-2\), the exact shattering probability is \(r_m(n)/\binom{n(n-1)}m\). Compare uniform sampling of \(m\) off-diagonal cells with uniform sampling of \(m\) cells from the full \(n\)-by-\(n\) board. The latter hits a diagonal cell with probability at most \(m/n\); thus, for \(m=O(\sqrt n)\), conditioning on avoiding the diagonal changes the matching probability by \(o(1)\). In the full board, the probability that \(m\) distinct sampled positions form a matching is exactly
\[
\frac{(n)_m^2}{(n^2)_m}
=\prod_{j=0}^{m-1}\frac{(n-j)^2}{n^2-j}.
\]
For \(m=O(\sqrt n)\), expanding logarithms gives \(\log\Pr(\text{matching})=-m(m-1)/n+o(1)\). Hence the critical limit is \(e^{-c^2}\). The subcritical limit follows with \(c=0\); for supercritical \(m/\sqrt n\to\infty\), monotonicity of the shattering event as the sample size increases and comparison with \(\lfloor C\sqrt n\rfloor\) for each fixed \(C\) yield an upper bound \(e^{-C^2}\), which tends to zero as \(C\to\infty\).

## Verification

The standalone script `check_derangement_shattering.py` directly enumerates derangements, computes their trace sets and independently enumerates matchings of each support. It exhaustively examines every support of size at most \(n\) for \(2\le n\le5\), and every support of size at most five for \(n=6\). It checks random supports for \(n=6,7,8\). Separately, a row-by-row matching dynamic program checks all coefficients against the inclusion-exclusion expression for \(2\le n\le9\). The checker outputs 197,657 support tests and successful comparisons. The universal proof uses the explicit edge-disjoint factor construction, not finite extrapolation.

## Relationship to prior work

The 2019 preprint by Bucić, Devlin, Hendon, Horne and Lund studies the intersection proportions and counts of perfect matchings and graph derangements; its main theorems do not give an edge-incidence VC shattering classification. Johnson and Wickes (first public 2021) study all ordering patterns on chosen *symbols* realized by families of permutations. Their notion of permutation shattering is different from the Boolean trace problem on *row-column positions* treated here. The rook-polynomial inclusion-exclusion formula and factorization of a complete bipartite graph are standard ingredients and are not presented as novel in isolation. The assessed result is the sharp trace universality theorem linking them to the derangement concept class, with its exact VC spectrum and random threshold.

## Limitations

The result is for the complete off-diagonal board and all its perfect matchings; arbitrary forbidden boards need not have this trace property. The asymptotic limit concerns uniformly sampled *distinct* board positions. Self-review only; independent mathematical validation and exhaustive historical-priority certification have not been performed. An equivalent result could be present under matching-preclusion, partial-permutation, or rook-board terminology.

## References

1. M. Bucić, P. Devlin, M. Hendon, D. Horne, B. Lund, *Perfect matchings and derangements on graphs*, arXiv:1906.05908 (first version June 13, 2019), Journal of Graph Theory 97 (2021), 340–354. https://arxiv.org/abs/1906.05908
2. J. R. Johnson, B. Wickes, *Shattering \(k\)-sets with Permutations*, arXiv:2112.01946 (first version December 3, 2021), Order 41 (2024), 419–436. https://arxiv.org/abs/2112.01946
