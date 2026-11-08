# Sharp matching-channel capacity law for fastest mixing on \(K_{m,m}\)

## Finding

Label the two parts of the balanced complete bipartite graph \(K_{m,m}\) as \(\{u_1,\ldots,u_m\}\) and \(\{v_1,\ldots,v_m\}\), where \(m\ge2\), and distinguish the perfect matching \(M=\{u_iv_i:1\le i\le m\}\). Consider all real symmetric, entrywise nonnegative stochastic matrices \(P\) on these \(2m\) states, with off-diagonal entries supported on the bipartite edges, arbitrary nonnegative holding probabilities, and prescribed matched-edge probabilities \(P_{u_i v_i}=a\) for every \(i\), with \(0\le a\le1\). Define the mixing objective \(\rho(P)=\|P-\mathbf1\mathbf1^T/(2m)\|_2\). This definition counts any additional eigenvalue \(1\) arising from disconnected chains.

**Theorem.** The exact constrained optimum is
\[
\rho_m(a)=\min_P\rho(P)
=\max\!\left\{\frac{m(1-2a)}{3m-4},\;\frac{m-2+2ma}{3m-2}\right\}.
\]
The two affine branches cross only at \(a_*=2/(3m)\), where \(\rho_m(a_*)=1/3\). On the deficient-matching side \(0\le a\le a_*\), a globally optimal chain assigns the same off-matching probability and holding probability at every vertex, namely
\[
 b=\frac{2(1-2a)}{3m-4},\qquad
 c=\frac{m-2+ma}{3m-4}.
\]
On the excess-matching side \(a_*\le a\le1\), a globally optimal chain instead uses
\[
 b=\frac{2(1-a)}{3m-2},\qquad
 c=\frac{m(1-a)}{3m-2}.
\]
These formulas agree at \(a=a_*\). More generally, if every matching-edge probability is only required to lie in a common interval \([\ell,u]\subseteq[0,1]\), possibly differing from edge to edge, the optimum is
\[
\min_P\rho(P)=\rho_m(\widehat a),\qquad
\widehat a=\min\{u,\max\{\ell,2/(3m)\}\}.
\]
The displayed uniform matched-edge design at \(\widehat a\) attains the interval optimum. This asserts existence of an optimal orbit-invariant chain, not uniqueness of all optimal chains.

## Assumptions and scope

The graph is the simple unweighted \(K_{m,m}\) with holding permitted in the transition matrix (not as graph edges). The stationary target is uniform and the chain is symmetric and stochastic. The matched pairs are fixed by their indices. In the fixed-probability variant every matched edge must carry exactly \(a\); in the interval variant every matched edge is independently constrained by the same lower and upper bounds. Unmatched cross edges may have arbitrary nonnegative probabilities, subject to stochasticity. The objective is the full centered operator norm, so boundary cases with disconnected or periodic chains are included. No assertion concerns nonreversible chains, nonuniform stationary distributions, or finite-time total-variation optimality.

## Proof

**1. Symmetry reduction.** Simultaneously permuting the \(m\) matched pairs and interchanging the two parts preserves every constraint, both with fixed \(a\) and with common interval bounds. If \(G\) is this finite group and \(P\) is feasible, its average \(\overline P=|G|^{-1}\sum_{g\in G}gPg^T\) remains feasible. The rank-one stationary projector \(J=\mathbf1\mathbf1^T/(2m)\) is invariant, and convexity of the operator norm yields \(\|\overline P-J\|_2\le\|P-J\|_2\). Therefore an optimum exists with three orbit probabilities: \(a\) on matching edges, \(b\) on unmatched cross edges, and \(c=1-a-(m-1)b\) on all diagonal entries. The allowed region is \(b\ge0\), \(c\ge0\).

**2. Exact eigenspaces.** In part-major vertex order, the orbit-invariant matrix is
\[
P=\begin{pmatrix}cI_m&B\\B&cI_m\end{pmatrix},
\qquad B=(a-b)I_m+b\mathbf1_m\mathbf1_m^T.
\]
Its eigenvalue on the constant vector is \(1\). On the two-part sign vector it is \(2c-1\). On the spaces \(\{(w,w):w\perp\mathbf1_m\}\) and \(\{(w,-w):w\perp\mathbf1_m\}\), each of dimension \(m-1\), the eigenvalues are respectively \(c+a-b\) and \(c-a+b\). These spaces have total dimension \(2m\), so the full objective is exactly
\[
\rho(P)=\max\{|2c-1|,|c+a-b|,|c-a+b|\}
=\max\{|2c-1|,c+|a-b|\}.
\]
The last equality uses \(c\ge0\).

**3. Two global lower bounds.** From stochasticity \(b=(1-a-c)/(m-1)\). Hence, for every feasible \(b,c\),
\[
\rho(P)\ge\max\left\{1-2c,\frac{1-ma+(m-2)c}{m-1}\right\}
\ge\frac{m(1-2a)}{3m-4}.
\]
Indeed the first affine expression decreases in \(c\) and the second is nondecreasing, and they intersect at \(c=(m-2+ma)/(3m-4)\). The same reasoning with the other Fourier mode gives
\[
\rho(P)\ge\max\left\{1-2c,\frac{ma-1+mc}{m-1}\right\}
\ge\frac{m-2+2ma}{3m-2},
\]
with intersection at \(c=m(1-a)/(3m-2)\). These inequalities remain valid when an intersection lies outside the feasible interval, because each minimax bound was obtained by minimizing over all real \(c\).

**4. Simultaneous attainment.** Subtracting the lower branches gives
\[
\frac{m-2+2ma}{3m-2}-\frac{m(1-2a)}{3m-4}
=\frac{4(m-1)(3ma-2)}{(3m-4)(3m-2)}.
\]
Thus the first bound dominates for \(a\le a_*\), and the second for \(a\ge a_*\). In the first regime the proposed \(b,c\) are nonnegative, sum with \(a\) to one, satisfy \(b\ge a\), and give \(1-2c=c+b-a=m(1-2a)/(3m-4)\). The remaining two eigenvalue moduli do not exceed this common value because \(c\ge0\). In the second regime the proposed \(b,c\) are nonnegative, satisfy \(b\le a\), and give \(1-2c=c+a-b=(m-2+2ma)/(3m-2)\). Again the other eigenvalues have no greater modulus. This proves the fixed-\(a\) formula, including all endpoints and \(m=2\).

**5. Capacity intervals.** Symmetrization replaces arbitrary matched probabilities in \([\ell,u]\) with their common average \(a\in[\ell,u]\), without increasing the objective. The exact fixed-\(a\) optimum is strictly decreasing up to \(a_*\) and strictly increasing thereafter (the branch slopes are \(-2m/(3m-4)\) and \(2m/(3m-2)\)). Consequently its interval minimizer is the Euclidean projection \(\widehat a\) of \(a_*\) onto \([\ell,u]\). The fixed-\(\widehat a\) construction is interval-feasible and attains this bound.

## Verification

The standalone standard-library file `verify.py` carries out exact rational checks. For dimensions \(2\le m\le12\), it constructs the full \(2m\times2m\) stochastic matrix, tests its action on a basis of all four invariant eigenspaces, checks normalization and nonnegativity, and compares the attained SLEM against both lower-bound branches. It additionally tests many rational feasible off-matching probabilities and matching-capacity intervals. Run `python3 verify.py` in a directory containing this document and the checker. The finite tests are independently reproducible checks of algebraic formulas, not the proof for all \(m\); that is supplied above.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004, section 7.1) solve the unrestricted fastest-mixing problem on complete bipartite graphs and give the underlying convex symmetry principle. Their unrestricted balanced result \(\rho=1/3\) is the \(a=a_*\) point here and is not claimed new. Boyd, Diaconis, Parrilo and Xiao (2009, sections 2, 3 and 5.4.2) provide orbit-based semidefinite reductions, including edge-transitive formulas and the unrestricted complete-bipartite example. In particular the \(a=0\) crown graph is edge-transitive for \(m\ge3\), so its endpoint optimum follows from their general theorem; that endpoint is also not claimed new. Jafarizadeh (2010, sections III and V) treats symmetric layered complete multipartite networks, including the unrestricted two-layer case, but does not impose this distinguished one-factor transition constraint. The finding here is the entire exact constrained response across all \(a\), with differing slopes on either side of the mixing-optimal matching probability, plus the arbitrary-per-edge interval version.

## Limitations

Symmetry reduction yields at least one optimal orbit-invariant matrix, not a classification of all nonsymmetric optimal matrices. The SLEM optimum controls asymptotic spectral mixing rather than minimizing every finite-time distance. The endpoint \(a=0\) at \(m=2\) describes a disconnected chain with optimal centered norm \(1\), not a rapidly mixing one. Earlier general convex SDP methods make the finite problem algorithmically solvable, while the contribution assessed here is its specific closed-form all-size capacity frontier; further unindexed specialist literature might contain equivalent formulas.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46(4), 667–689 (2004), journal online October 29, 2004; earlier Stanford Statistics Technical Report 2003-04 dated February 2003, https://statistics.stanford.edu/technical-reports/fastest-mixing-markov-chain-graph ; https://doi.org/10.1137/S0036144503423264 ; open full text https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20(2), 792–819 (2009), arXiv preprint September 6, 2007, https://arxiv.org/abs/0709.0955 ; open full text https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf .
3. S. Jafarizadeh, *Fastest Mixing Markov Chain on Symmetric K-Partite Network*, preprint August 16, 2010, https://arxiv.org/abs/1008.2588 .
