# Missing-edge rigidity for the fastest symmetric Markov chain on noncomplete graphs

## Finding

For a connected, simple, noncomplete graph \(G=(V,E)\) with \(N=|V|\ge3\), define the fastest-mixing second-largest eigenvalue modulus
\[
\mu_*(G)=\min_{P\in\mathcal P(G)}\left\|P-\frac1N J\right\|_2,
\]
where \(J=\mathbf1\mathbf1^{\mathsf T}\), and \(\mathcal P(G)\) is the set of real symmetric nonnegative row-stochastic matrices whose nonzero off-diagonal entries lie on edges of \(G\). Holding probabilities are allowed.

**Theorem (exact global noncomplete-graph frontier).** For every such graph,
\[
\mu_*(G)\ge\frac1{N-1},
\]
and equality holds **exactly** when \(\overline G\) is a matching (one or more disjoint edges, with possible isolated vertices). If its missing-edge matching defines the permutation matrix \(Q\) that exchanges each missing pair and fixes every remaining vertex, then
\[
P_*=\frac{J-Q}{N-1}
\]
is an explicitly optimal symmetric stochastic transition. Its nontrivial eigenvalues all have modulus \(1/(N-1)\).

There is also a quantitative obstruction: if some vertex has \(r\ge1\) distinct nonneighbors, every \(P\in\mathcal P(G)\) satisfies
\[
\mu(P)^2\ge \frac{r}{(N-1)(N-r)}.
\]
In particular, any two forbidden edges sharing a vertex force
\[
\mu_*(G)\ge \sqrt{\frac2{(N-1)(N-2)}}>\frac1{N-1}.
\]
The displayed degree-based inequality need not itself be sharp for every graph; the sharp global classification is the equality statement above.

## Assumptions and scope

The graph is finite, undirected, simple, connected, noncomplete, and has at least three vertices. Every permitted off-diagonal edge may receive zero or positive symmetric transition probability; diagonal holding is unrestricted except by stochasticity and nonnegativity. The invariant distribution is uniform, and the convergence objective is the SLEM, not an ordinary hitting-time objective or a nonreversible mixing criterion. There is no requirement of a uniform edge weight. The graph \(K_N\), excluded here, has optimum zero using \(P=J/N\).

## Proof

Write \(H=J/N\), let \(M=P-H\), and let \(e_v\) be the coordinate vector of vertex \(v\). As \(P\) is symmetric and stochastic, \(M\mathbf1=0\), \(M=M^{\mathsf T}\), and \(\mu(P)=\|M\|_2\). Set \(x_v=e_v-\mathbf1/N\), for which
\[
\|x_v\|_2^2=\frac{N-1}{N},\qquad Mx_v=Pe_v-\frac{\mathbf1}{N}.
\]
If \(v\) has \(r\) nonneighbors, its column \(p=Pe_v\) has at least \(r\) forbidden zero coordinates. It has nonnegative entries summing to one. Cauchy--Schwarz on its at most \(N-r\) available coordinates yields
\[
\|p\|_2^2\ge\frac1{N-r};\qquad
\left\|p-\frac{\mathbf1}N\right\|_2^2=\|p\|_2^2-\frac1N
\ge\frac{r}{N(N-r)}.
\]
Hence
\[
\mu(P)^2\ge\frac{\|Mx_v\|_2^2}{\|x_v\|_2^2}
\ge\frac{r}{(N-1)(N-r)}. \tag{1}
\]
A noncomplete graph has at least one vertex with \(r\ge1\). Formula (1) gives the universal bound \(\mu(P)\ge1/(N-1)\). If the complement is not a matching, some vertex has \(r\ge2\). Since \(r/(N-r)\) strictly increases with \(r\), (1) gives the strictly larger bound \(\sqrt{2/[(N-1)(N-2)]}\). Thus equality in the universal bound forces the complement to be a matching.

Conversely suppose \(\overline G\) consists of disjoint edges (at least one), plus possible isolated vertices. Let \(Q\) be the permutation matrix formed by the corresponding disjoint transpositions and fixed points. Then \(Q=Q^{\mathsf T}\), \(Q^2=I\), \(Q\mathbf1=\mathbf1\), and each row of \(Q\) has exactly one entry equal to one. Consequently \(P_*=(J-Q)/(N-1)\) is symmetric, entrywise nonnegative, row-stochastic, and vanishes on all missing off-diagonal graph edges. All other off-diagonal edges carry probability \(1/(N-1)\). A fixed point of \(Q\) gives zero holding, which is permitted.

Since \(QH=HQ=H\) and \(H^2=H\),
\[
\left(P_*-H\right)^2
=\frac{(Q-H)^2}{(N-1)^2}
=\frac{I-H}{(N-1)^2}.
\]
The matrix \(P_*-H\) is symmetric and annihilates \(\mathbf1\). Its restriction to \(\mathbf1^\perp\) therefore has all eigenvalues of absolute value \(1/(N-1)\). Thus \(\mu(P_*)=1/(N-1)\), attaining the lower bound. This completes the proof for all graphs in the stated domain.

## Verification

`verify.py` implements exact rational checks of the involution, row sums, support, nonnegativity, and the squared centered-operator certificate for 55 canonical graph examples with \(3\le N\le15\), as well as 3,080 exact integer-parameter inequalities. Invoke `python3 verify.py` from the directory containing this file. It prints `VERIFY_OK matching_cases=55 bound_cases=3080`. The proof above is valid for all \(N\); the finite checks are only supplementary and do not test all labeled graphs.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) formulate minimization of symmetric-chain SLEM over graph-supported stochastic kernels as a convex semidefinite program. Boyd, Diaconis, Parrilo and Xiao (2007 preprint; 2009 journal) give exact spectral solutions for edge-transitive graphs and other symmetric examples. These frameworks already address particular graphs within the equality class (notably the full-matching deletion from an even complete graph), and those special cases are not asserted to be new. The theorem here is the **universal, sharp lower frontier over all connected noncomplete graphs and its graph-theoretic if-and-only-if equality classification**, including nonregular partial-matching deletions, with a local missing-neighbor stability inequality. The inspected relevant sections of those primary texts did not state this classification. A general optimization formulation alone does not imply its closed-form global equality class without the missing-column argument and explicit matching construction.

## Limitations

This is a mathematical result about symmetric stochastic kernels with uniform stationary distribution and freely selectable holding probabilities. It does not apply as stated to prescribed equilibrium weights, nonsymmetric chains, mandatory strictly positive holding, or constrained edge weights. The inequality depending on the number of forbidden neighbors is a universal lower bound, not claimed tight for all \(r\ge2\). An exhaustive priority check of every specialist publication is unavailable; no independent mathematical audit has been performed.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667--689. DOI: https://doi.org/10.1137/S0036144503423264 . Open full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792--819, DOI: https://doi.org/10.1137/070689413 . First public arXiv posting dated 2007-09-06: https://arxiv.org/abs/0709.0955 . Full text: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf .
3. S. Roch, *Bounding Fastest Mixing*, Electronic Communications in Probability 10 (2005), 282--296, arXiv:math/0409429, https://arxiv.org/abs/math/0409429 .
