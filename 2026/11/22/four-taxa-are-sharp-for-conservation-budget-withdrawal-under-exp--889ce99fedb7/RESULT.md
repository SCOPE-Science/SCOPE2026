# Four taxa are sharp for conservation-budget withdrawal under exponential survival

## Finding

**Theorem (sharp taxon number for nonmonotone conservation spending).** Consider any finite rooted edge-weighted phylogenetic tree with no degree-one internal vertices and no stem edge above the root. Every pendant edge has positive length, every other edge has nonnegative length, and distinct terminal taxa survive independently with probabilities
\[p_i(x_i)=1-\rho_i e^{-k_i x_i},\qquad 0<\rho_i\le1,\quad k_i>0,\quad x_i\ge0.\]
For every budget \(B\ge0\), let \(x^*(B)\) uniquely maximize the expected **rooted** phylogenetic diversity subject to \(\sum_i x_i=B\).

1. If the tree has at most three terminal taxa, each coordinate \(x_i^*(B)\) is nondecreasing in \(B\) over \([0,\infty)\).
2. Four taxa suffice for the opposite behavior. An explicit **ultrametric** rooted four-taxon tree with the same strictly positive untreated survival probability \(1/10\) at every tip has an interior optimal allocation at \(B_\star\) for which \(\frac{d}{dB}x_1^*(B_\star)=-2/55<0\). The inequality persists on an open interval and, by perturbation, also on a strictly bifurcating ultrametric tree with positive lengths on every edge.

Thus four taxa are the sharp minimum, in this model, for an optimal conservation investment in one taxon to *decrease* when the total conservation budget increases. Uniqueness rules out a tie-breaking artifact.

## Assumptions and scope

Let \(C_e\) be the set of descendant leaves of edge \(e\), and \(\ell_e\) its length. If no descendant of \(e\) survives, that edge contributes zero; otherwise its full length contributes. Since terminal survivals are independent, writing \(q_i(x_i)=\rho_i e^{-k_i x_i}\), the expected rooted diversity is
\[F(x)=\sum_e\ell_e\left(1-\prod_{i\in C_e}q_i(x_i)\right).\]
All spending is nonnegative, and exact expenditure (rather than a cap) is imposed. Because all pendant lengths are positive, the expected diversity increases strictly with each finite coordinate; an equivalent budget-*at-most* constraint would therefore use all funds. There are no other species interactions, joint extinction risks, learning, intervention caps, or intertemporal dynamics. The four-taxon witness has strictly positive and homogeneous untreated survival probability \(1/10\) (\(\rho_i=9/10\) for all four tips).

## Proof

**Strict concavity and uniqueness.** Each edge contributes \(\ell_e(1-\rho_{C_e}e^{-\sum_{i\in C_e}k_ix_i})\), where \(\rho_{C_e}=\prod_{i\in C_e}\rho_i\). Its Hessian is negative semidefinite. The pendant-edge terms have strictly negative second derivative in each separate coordinate, hence \(-\nabla^2F\) is positive definite at every finite \(x\). On the compact budget simplex there is exactly one optimum. Moreover the optimal spending vector is continuous in \(B\) by uniqueness and compactness after rescaling to a unit simplex.

**Two taxa.** Any rooted two-taxon tree of the specified form has only the two pendant terms and possibly a common ancestral edge (the latter can have zero length). Abbreviate the pendant weights by \(a,b>0\) and their shared ancestral weight by \(c\ge0\); the objective is
\[G(y,z)=a(1-q_1)+b(1-q_2)+c(1-q_1q_2).\]
At an interior optimum under \(y+z=s\), set \(u=aq_1>0\), \(v=bq_2>0\), \(t=cq_1q_2\ge0\). Equality of marginal returns gives
\[k_1u-k_2v+(k_1-k_2)t=0.\]
Differentiate this equality at fixed \(s\), with \(z=s-y\). Its partial derivative with respect to \(y\) is \(-[k_1^2u+k_2^2v+(k_1-k_2)^2t]\), while its partial derivative with respect to \(s\) is \(k_2^2v-k_2(k_1-k_2)t\). Substituting the stationarity identity simplifies them to \(-k_1k_2(u+v)\) and \(k_1k_2u\), respectively. Consequently
\[\frac{dy^*(s)}{ds}=\frac{u}{u+v}\in(0,1),\qquad \frac{dz^*(s)}{ds}=\frac{v}{u+v}\in(0,1).\]
At a boundary optimum, the unique maximizer stays on a face with derivative either \((0,1)\) or \((1,0)\) until it enters the interior. Continuity precludes downward jumps. Thus both two-taxon optimal amounts are nondecreasing for every \(s\ge0\).

**Three taxa.** Every such rooted tree on three leaves is either a star or consists of a two-leaf descendant clade and one separate leaf. In the star case, the objective is separable into three strictly increasing, strictly concave single-taxon returns. In the second case it splits as a two-taxon return \(G(y,z)\) and a single-taxon return \(W(w)\); the connecting clade edge is included in \(G\). For every fixed pair budget \(s\), the pair optimum \(V(s)=\max_{y+z=s}G(y,z)\) is strictly increasing and strictly concave (the strict concavity of \(G\) passes to this value function). Optimal splitting of \(B=s+w\) between two increasing concave return functions is coordinatewise monotone in \(B\): its marginal-value multiplier can only decrease as total budget grows, so the optimal group budgets cannot decrease. The preceding two-taxon calculation then shows both individual allocations inside the pair cannot decrease. This covers every three-taxon topology and all admissible parameters.

**Exact four-taxon witness.** Let the root have one edge of length \(64\) to a common ancestor of taxa \(1,2,3\), each with pendant edge of length \(12\), and one separate pendant edge to taxon \(4\) of length \(76\). Every root-to-tip distance is \(76\). Take \(\rho_i=9/10\) for all taxa and efficiency vector \((k_1,k_2,k_3,k_4)=(3,1,1,1)\). The objective becomes
\[F(x)=64(1-q_1q_2q_3)+12\sum_{i=1}^3(1-q_i)+76(1-q_4),\quad q_i(x_i)=\frac9{10}e^{-k_ix_i}.\]
Define the strictly interior allocation
\[x^\star=\left(\frac{\log(54/5)}{3},\log\frac65,\log\frac65,\log\frac{57}{10}\right),\qquad B_\star=\sum_i x_i^\star.\]
At this vector the four extinction probabilities are \((1/12,3/4,3/4,3/19)\). The weighted extinction of the shared edge is \(64(1/12)(3/4)^2=3\); the pendant weighted extinctions are \((1,9,9,12)\). Therefore
\[\nabla F(x^\star)=(12,12,12,12).\]
Since \(F\) is strictly concave, this common positive marginal return is the sufficient and necessary Karush–Kuhn–Tucker condition for the unique global optimum at \(B_\star\).

The exact negative Hessian at the optimum is
\[A=-\nabla^2F(x^\star)=\begin{pmatrix}36&9&9&0\\9&12&3&0\\9&3&12&0\\0&0&0&12\end{pmatrix}.\]
It is positive definite by the general pendant-edge argument. The stationary equations and total-budget constraint implicitly define a smooth interior optimizer for budgets near \(B_\star\). Their derivative is
\[\frac{dx^*}{dB}(B_\star)=\frac{A^{-1}{\bf1}}{{\bf1}^{\mathsf T}A^{-1}{\bf1}}=\frac1{55}(-2,18,18,21).\]
The first entry is strictly negative. Numerically \(B_\star\approx2.898291333\), but the negativity is exact.

To obtain a **fully binary ultrametric** example, resolve the three-way descendant node by adding a cherry edge of length \(\varepsilon>0\) above taxa \(2,3\), shorten just those two terminal edges from \(12\) to \(12-\varepsilon\), and leave the other lengths unchanged. For sufficiently small \(\varepsilon<12\) all edges are strictly positive, the tree remains ultrametric, and the interior KKT solution and its budget derivative vary continuously with \(\varepsilon\). Thus the negative first-coordinate derivative survives. This proves the sharpness assertion also for fully binary ultrametric trees.

## Verification

The included standalone standard-library script `checks/verify.py` reconstructs the rational extinction vector, all four marginal returns, the complete Hessian, its four positive leading principal minors, the determinant \(40824\), the inverse-vector identity
\[A^{-1}{\bf1}=(-1/126,\ 1/14,\ 1/14,\ 1/12),\]
and the exact derivative \((-2,18,18,21)/55\). It also checks the two-leaf stationarity reductions over 1,057 exact rational test configurations, and independently computes the local derivative by a floating-point finite difference. All checks passed upon direct execution. The sample tests do not replace the proof for arbitrary parameters or for arbitrarily small binary resolutions.

Run from the folder containing the files with `python3 checks/verify.py`. No third-party Python packages are required.

## Relationship to prior work

Rooted phylogenetic diversity, conservation costs and individual survival probabilities are treated by Hartmann and Steel (2006), building on the Noah's Ark framework. Their exponential-budget variant uses **one common per-unit extinction multiplier across species**, while the witness here uses unequal efficiencies \((3,1,1,1)\); their greedy guarantee does not imply these comparative statics. They also explicitly caution that greedy solutions to more general Noah's Ark instances can fail. Simianer and colleagues (2003) study continuous financial investment, nonlinear extinction response, and an incremental allocation method for breed diversity; their particular diversity measure, response curves and objective differ, and the examined methods do not state the exact four-taxon monotonicity boundary or the present derivative certificate.

Published mathematical findings about greedy species selection under imperfect conservation, re-entrant **single-species** priority, and nonnested **habitat sampling** budgets address other decisions. Neither their conclusions nor the examined classical papers imply the present *smooth, unique, interior* four-taxon decrease from larger total funding. This is a statement-comparison, not proof of historical uniqueness.

## Limitations

This is a model theorem about expected rooted diversity with **independent** terminal survival, exponential extinction reduction, heterogeneous efficiency, and unlimited divisible budgets. It does not assert actual conservation policy should cut spending to particular threatened taxa. The nonmonotonicity is local around a specified budget, with homogeneous positive untreated survival; no claim is made that a taxon loses funding as the budget grows everywhere, or that four is a universal threshold under different response models. Literature coverage is substantial but not exhaustive; priority relative to wider resource-allocation comparative-statics theory remains provisional. Independent validation has not been performed.

## References

- Hartmann, K. and Steel, M. (2006). *Maximizing Phylogenetic Diversity in Biodiversity Conservation: Greedy Solutions to the Noah's Ark Problem.* Systematic Biology 55(4), 644–651. Published 2006-08-01. DOI: https://doi.org/10.1080/10635150600873876. Author-hosted complete text: https://www.math.canterbury.ac.nz/~m.steel/Non_UC/files/research/noah.pdf
- Simianer, H., Marti, S. B., Gibson, J., Hanotte, O. and Rege, J. E. O. (2003). *An approach to the optimal allocation of conservation funds to minimize loss of genetic diversity between livestock breeds.* Ecological Economics 45(3), 377–392. DOI: https://doi.org/10.1016/S0921-8009(03)00092-2. Open full text: https://www.uni-goettingen.de/de/document/download/57dcb4e6357f5d6dd02e36d8248cb675.pdf/Simianer.pdf
- Weitzman, M. L. (1998). *The Noah's Ark Problem.* Econometrica 66(6), 1279–1298. DOI: https://doi.org/10.2307/2999617
- Steel, M. (2005). *Phylogenetic Diversity and the Greedy Algorithm.* Systematic Biology 54(4), 527–529. DOI: https://doi.org/10.1080/10635150590947023
