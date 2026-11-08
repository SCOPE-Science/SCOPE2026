# A three-stage two-leader transition on quadrilateral book graphs

## Finding

For each integer \(m\ge2\), let \(B_m\) be the *quadrilateral book* (equivalently, \(K_{1,m}\square K_2\)): its vertices are two common-edge endpoints \(u,v\) and \(m\) pairs \(a_i,b_i\), with \(1\le i\le m\); its edges are \(uv\), \(ua_i\), \(a_ib_i\), and \(b_iv\), all with unit conductance. Choose exactly two distinct noise-free leaders \(S\). Let \(L\) be the ordinary (combinatorial) graph Laplacian, \(F=V(B_m)\setminus S\), and \(J(S)=\operatorname{tr}((L_{FF})^{-1})\), retaining original degrees when grounding leaders.

**Theorem.** The complete set of minimizers of \(J\), their number, and the optimum are

| Number of pages | All optimal leader sets | Number | Minimum \(J\) |
|---|---|---|---|
| \(m=2\) | \(\{a_i,b_j\}\) with \(i\ne j\) | \(2\) | \(46/21\) |
| \(m=3\) | \(\{u,b_i\}\) and \(\{v,a_i\}\) | \(6\) | \(95/24\) |
| \(m\ge4\) | \(\{u,v\}\) | \(1\) | \(4m/3\) |

Every optimal set above is strictly better than every other two-element set. In particular, the geometry changes successively from two different pages, to a hub paired with an outer vertex *not directly adjacent to it*, to the two hubs.

## Assumptions and scope

The graph is finite, simple, connected and unweighted, with \(m\ge2\) integral. Leaders have zero state error and do not contribute to the inverse-trace objective. The graph Laplacian is not the Laplacian of the vertex-induced follower graph: edges from followers to grounded leaders remain in the diagonal. For this connected graph, \(L_{FF}\) is positive definite whenever \(S\) is nonempty. The theorem addresses exactly two leaders, not controllability rank, noisy leaders, arbitrary weights, or other leader budgets. If isotropic unit-variance white disturbances drive follower dynamics \(\dot z=-L_{FF}z+\dot W\), stationary total variance is \(J(S)/2\); this fixed factor does not affect minimizers.

## Proof

**Step 1: a two-terminal resistance identity.** Let \(G\) be any connected unit-resistor graph of order \(N\), with effective resistance \(R_{xy}\) between vertices \(x,y\). Ground distinct vertices \(s,t\), and inject unit current at a remaining vertex \(z\). If fractions \(\alpha\) and \(1-\alpha\) are withdrawn at \(s,t\), the minimum dissipated energy for that injection vector, by the resistance-distance quadratic form, is

\[
E_z(\alpha)=\alpha R_{zs}+(1-\alpha)R_{zt}-\alpha(1-\alpha)R_{st}.
\]

The shorting of \(s,t\) permits the current division that minimizes this strictly convex quadratic, with \(\alpha=(R_{zs}-R_{zt}+R_{st})/(2R_{st})\). Hence the diagonal of the grounded Green matrix at \(z\) equals

\[
(L_{FF}^{-1})_{zz}=\frac{R_{zs}+R_{zt}}2-\frac{R_{st}}4-\frac{(R_{zs}-R_{zt})^2}{4R_{st}}.
\]

The right side vanishes if \(z\) is either terminal. Summing over *all* \(N\) vertices, and writing \(S_x=\sum_zR_{xz}\), gives the exact identity

\[
\boxed{J(\{s,t\})=\frac{S_s+S_t}{2}-\frac{N R_{st}}4-\frac{1}{4R_{st}}\sum_z(R_{zs}-R_{zt})^2.}\tag{1}
\]

This calculation establishes the normalization, including the factor \(N\), without using a probabilistic approximation.

**Step 2: all resistance types of the book.** For \(i\ne j\), direct series-parallel and symmetry reductions give

| Pair type | Effective resistance |
|---|---|
| \(u,v\) | \(r=3/(m+3)\) |
| \(u,a_i\), \(v,b_i\), or \(a_i,b_i\) | \(e=(2m+7)/(3(m+3))\) |
| \(u,b_i\) or \(v,a_i\) | \(f=2(m+5)/(3(m+3))\) |
| \(a_i,a_j\) or \(b_i,b_j\) | \(h=4/3\) |
| \(a_i,b_j\), \(i\ne j\) | \(g=(4m+13)/(3(m+3))\) |

Here is a direct derivation covering the less immediate entries. The direct common edge and the \(m\) three-edge routes in parallel give \(r=1/(1+m/3)\). For a pair in one page, replace the other \(m-1\) routes by one hub-to-hub conductance \((m+2)/3\). Then an adjacent page edge has unit resistance in parallel with a route of resistance \(2+3/(m+2)\), yielding \(e\); the nonincident hub-to-page pair has paths of resistance \(2\) and \(1+3/(m+2)\) in parallel, yielding \(f\). For the same-side pair \(a_i,a_j\), interchanging pages \(i,j\) changes the sign of the injected-current solution, so both hubs have zero potential; each of the two terminals is attached to zero by paths of resistances \(1\) and \(2\) in parallel, giving \(h=2(1\parallel2)=4/3\).

For \(a_i,b_j\) in different pages, eliminate the other \(m-2\) pages and the unused vertex of each retained page. The resulting four-terminal network has hub-to-hub conductance \(c=(m+1)/3\); \(a_i\) connects to \(u,v\) with conductances \(1,1/2\), and \(b_j\) connects to \(u,v\) with conductances \(1/2,1\). Under unit current injection at \(a_i\) and withdrawal at \(b_j\), symmetry makes the potentials \((t,-t,s,-s)\) at \((a_i,b_j,u,v)\). Kirchhoff's equations are \(3t-s=2\) and \((4c+3)s=t\), giving \(R_{a_i b_j}=2t=(4c+3)/(3c+2)=g\). All these reductions use exact circuit equivalence, not finite-size interpolation.

**Step 3: all possible leader orbits.** The graph's page permutations and simultaneous hub exchange with \(a\leftrightarrow b\) put every two-element set in exactly one of six classes. Substituting the resistances in (1), with \(N=2m+2\), and counting the two hub vertices and \(m\) vertices of each outer type, gives the complete formulas

| Leader class | Representative | \(J\) |
|---|---|---|
| both hubs \(H\) | \(\{u,v\}\) | \(4m/3\) |
| hub/near \(A\) | \(\{u,a_i\}\) | \((8m^2+33m-5)/(3(2m+7))\) |
| hub/far \(B\) | \(\{u,b_i\}\) | \((8m^2+45m-17)/(6(m+5))\) |
| within page \(C\) | \(\{a_i,b_i\}\) | \(2(7m^2+21m-10)/(3(2m+7))\) |
| same side, different pages \(D\) | \(\{a_i,a_j\}\) | \((12m^2+25m-29)/(6(m+3))\) |
| opposite sides, different pages \(E\) | \(\{a_i,b_j\}\) | \(2(4m^2+9m-11)/(4m+13)\) |

Every formula is for the entire indicated orbit, with \(i\ne j\) in the final two rows. For transparency, the first-class calculation can also be read directly: grounding the hubs separates the \(m\) pages, each with follower block \(\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\) and inverse trace \(4/3\), so \(J_H=4m/3\). The remaining five follow from the complete five-type resistance table, (1), and the same finite counting; `verify.py` checks their values against *independently inverted grounded Laplacians*.

**Step 4: strict global comparisons.** Straight rational subtraction yields, for every integer \(m\ge2\),

\[
\begin{aligned}
J_A-J_H&=\frac{5(m-1)}{3(2m+7)}>0,\\
J_C-J_H&=\frac{2(m-1)(3m+10)}{3(2m+7)}>0,\\
J_D-J_E&=\frac{4m^2+17m+19}{6(m+3)(4m+13)}>0,\\
J_B-J_H&=\frac{5m-17}{6(m+5)},\\
J_E-J_H&=\frac{2(m+3)(4m-11)}{3(4m+13)},\\
J_E-J_B&=\frac{16m^3+64m^2-109m-439}{6(m+5)(4m+13)}.
\end{aligned}
\]

The last numerator equals \(-273\) at \(m=2\), equals \(242\) at \(m=3\), and is strictly increasing for integers \(m\ge2\), since its consecutive difference is \(48m^2+176m-29>0\). Therefore \(J_E<J_B\) at \(m=2\) and \(J_B<J_E\) for all \(m\ge3\). At \(m=2\), also \(J_E<J_H\); at \(m=3\), \(J_B<J_H<J_E\); at all \(m\ge4\), \(J_H<J_B\) and \(J_H<J_E\). The first three strict comparisons eliminate the other three classes. This proves every stated minimizer, strict uniqueness up to the displayed orbit, and the exact objective values. Their counts are respectively \(m(m-1)=2\), \(2m=6\), and \(1\). \(\square\)

## Verification

The standalone standard-library script `verify.py` constructs each complete graph and independently inverts each grounded Laplacian using rational Gauss-Jordan elimination. For all page counts \(2\le m\le9\), it compares the resulting inverse trace for **every unordered leader pair** with the applicable closed formula (708 exact pair comparisons). It also directly checks all six types of two-terminal resistances for page counts \(2\le m\le6\) (30 independent checks), the complete optimum orbit/count for each test size, and 198 additional exact-integer page-size sign samples. Its observed final line is `VERIFY_OK exact_grounded_pair_comparisons=708; resistance_sample_checks=30; sign_samples=198`. These tests are not a substitute for the all-\(m\) derivation above.

## Relationship to prior work

Lin, Fardad and Jovanović (2013) formulate inverse-trace leader selection for stochastic consensus and provide general optimization and relaxation methods. Fitch and Leonard (first public 2014) give a general joint-centrality characterization for two noise-free leaders, together with explicit examples for paths and cycles. Patterson, McGlohon and Dyagilev (2014) solve \(k\)-leader selection algorithmically on paths and rings. The complete \(m\)-page book is neither a path nor a ring. The general joint-centrality formula does not by itself evaluate the six leader orbits or establish the two sharp integer thresholds found here. The graph also differs from triangular friendship graphs, which share a *vertex*, rather than one edge, across pages.

Book-graph matching complexes and dual general-position numbers appearing in related research are different invariants and neither imply a grounded-Laplacian inverse-trace optimum. The graph also has the Cartesian-product description \(K_{1,m}\square K_2\), which was included in targeted searches. No claim of priority beyond the inspected sources is made.

## Limitations

The result applies to unit conductances, two perfectly fixed leaders, and the particular inverse-trace performance measure. It does not assert the same optimal sets for other objectives, nonuniform disturbances, three or more leaders, or unequal edge weights. Searches and inspected literature reduce but cannot eliminate the possibility of unindexed earlier equivalent statements. No independent mathematical audit has been performed.

## References

1. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, first public February 3, 2013. https://arxiv.org/abs/1302.0450
2. K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first public July 7, 2014. https://arxiv.org/abs/1407.1569
3. S. Patterson, N. McGlohon, and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first public December 20, 2014. https://arxiv.org/abs/1412.6595
