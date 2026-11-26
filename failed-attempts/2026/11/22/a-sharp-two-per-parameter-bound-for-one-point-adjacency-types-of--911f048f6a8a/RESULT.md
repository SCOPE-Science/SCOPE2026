# A sharp two-per-parameter bound for one-point adjacency types of finite cographs

## Finding

Let \(G\) be a finite simple undirected cograph (equivalently, a graph with no induced four-vertex path), and let \(\varnothing\ne A\subseteq V(G)\), with \(|A|=m\). Let
\[
\mathcal T(G,A)=\{N_G(v)\cap A:v\in V(G)\},\qquad
\mathcal T_{\mathrm{ext}}(G,A)=\{N_G(v)\cap A:v\in V(G)\setminus A\}.
\]
Then
\[
|\mathcal T_{\mathrm{ext}}(G,A)|\le |\mathcal T(G,A)|\le 2m.
\]
The constant \(2\) is optimal for every \(m\ge1\), even when only external witnesses are counted. More precisely, a cograph with exactly \(m\) parameters and \(2m\) distinct external adjacency traces must have at least \(3m\) vertices, and an explicit construction meets this minimum for every \(m\).

## Assumptions and scope

Graphs are finite, loopless, undirected and simple. Neighborhoods are **open**: \(v\notin N_G(v)\). The parameter set is nonempty, its labels are fixed, and external one-point quantifier-free types mean realizations by vertices not among the parameters. Over the adjacency/equality language, such an external type is specified by its adjacency set in \(A\): equality to any parameter is false. These statements do not concern closed neighborhoods, arbitrary first-order quantifier ranks, or arbitrary graph classes.

## Proof

**A strengthened induction.** Write \(T=\mathcal T(G,A)\), \(t=|T|\), \(e=\mathbf1_{\varnothing\in T}\) and \(f=\mathbf1_{A\in T}\). We claim the stronger universal inequality
\[
t+(1-e)+(1-f)\le 2|A|.\tag{1}
\]
Every nonempty finite cograph is constructed from a one-vertex graph by disjoint union and join, so we induct on such a construction. On a singleton with its unique vertex in \(A\), the open-neighborhood family is \(T=\{\varnothing\}\): the left side of (1) is \(1+0+1=2\). If a union/join child contains no parameters, the only trace contributed by its vertices is \(\varnothing\) for a union, or the full set \(A\) for a join. Adding that trace, if absent, simultaneously removes exactly one of the two penalty terms; thus (1) is preserved without changing \(|A|\). If there are multiple empty-parameter children the argument applies repeatedly.

Suppose both children have nonempty parameter sets \(A_1,A_2\), of cardinalities \(m_1,m_2\), with corresponding \(t_i,e_i,f_i\). For **disjoint union**, the trace family of the first child is supported in \(A_1\), and that of the second in \(A_2\). As the supports are disjoint, their intersection, if any, consists only of the empty set. Consequently
\[
t=t_1+t_2-e_1e_2,\qquad e=e_1\lor e_2,\qquad f=0.
\]
Using \(e_1e_2+(e_1\lor e_2)=e_1+e_2\), the left side of (1) equals \(t_1+t_2+2-e_1-e_2\). The induction hypotheses give
\[
t_1+t_2+2-e_1-e_2\le 2(m_1+m_2)-2+f_1+f_2\le 2(m_1+m_2).
\]
For **join**, a trace from the first child has form \(S\cup A_2\) with \(S\in T_1\), and a trace from the second has form \(A_1\cup S'\) with \(S'\in T_2\). These two trace families intersect only at \(A=A_1\cup A_2\), when both child families contain their respective full sets. Therefore
\[
t=t_1+t_2-f_1f_2,\qquad f=f_1\lor f_2,\qquad e=0,
\]
and, symmetrically, the left side of (1) becomes \(t_1+t_2+2-f_1-f_2\), bounded by \(2(m_1+m_2)-2+e_1+e_2\le 2(m_1+m_2)\). This completes the induction. Dropping the nonnegative penalty terms proves \(|T|\le2m\), and \(\mathcal T_{\rm ext}\subseteq T\) gives the external bound.

**Sharp extremizers and minimum size.** Choose any rooted *full* binary tree with exactly \(m\) leaves. Associate a named parameter \(a_i\) and a nonparameter twin \(b_i\) to each leaf; its base graph is the edge \(a_ib_i\). At every internal tree node, form the disjoint union of its two child graphs and then join a single new apex vertex to this union. Finally, add one globally isolated vertex. The resulting graph is a cograph, since each step is a disjoint union or a join with a singleton.

There are \(m\) parameters, \(m\) twins, \(m-1\) internal-node apex vertices, and one isolated vertex, for exactly \(3m\) vertices. Each twin \(b_i\) has adjacency trace \(\{a_i\}\). Each apex has adjacency trace equal to the set of parameters labeling the leaves beneath its own tree node: no edges were added between distinct child subgraphs, while apex vertices at higher nodes do not change the traces of lower vertices. These \(m+(m-1)=2m-1\) nonempty sets are distinct because the leaf sets of different nodes of a rooted full binary tree are distinct. The isolated vertex realizes \(\varnothing\), giving \(2m\) **distinct external** traces. Conversely, any graph realizing \(2m\) external types has at least \(2m\) distinct vertices outside \(A\) and \(m\) vertices inside, so it necessarily has at least \(3m\) vertices. This proves exact sharpness of both claims, including \(m=1\).

## Verification

The standalone `verify.py` implements the theorem using bitmask adjacency. It exhaustively checks every labeled simple graph with up to six vertices that has no induced \(P_4\), and every nonempty parameter set in each such graph, against inequality (1) and the external bound. It also checks the sharp constructions for \(m=1,\ldots,12\) by directly examining every possible induced four-vertex subgraph, and performs 5,000 reproducible randomly generated cotree cases. Executing `python verify.py` gave:

```text
VERIFY_OK exhaustive_cographs=6039 exhaustive_parameter_cases=362227 extremal_witnesses=12 randomized_cotree_cases=5000
```

These finite checks corroborate the definitions, boundary cases, constructions and calculations; the all-size statement follows from the induction, not from finite enumeration.

## Relationship to prior work

Dreier, Mählmann and Toruńczyk (2026, arXiv:2611.08143) establish broad polynomial bounds on finite-rank types over parameter sets in monadically dependent graph classes, motivating an exact rank-zero case. Their general theorem supplies neither the exact \(2m\) coefficient nor the sharp minimum graph order \(3m\) for cographs. Bonnet, Foucaud, Lehtilä and Parreau (2023) prove \(\nu(d,m)\le(d+2)2^{d+1}m\) for twin-width at most \(d\); the \(d=0\) consequence for cographs is \(4m\), which does not imply the stronger bound \(2m\). The 2026 work of Berthe and collaborators treats sharp neighborhood constants for bounded treewidth/pathwidth, a different structural regime and primarily closed neighborhoods. The present proof exploits the exact union/join cotree decomposition, not the general twin-width method.

## Limitations

The result concerns only open adjacency traces on finite cographs and one-point quantifier-free external types; it does not provide bounds for arbitrary first-order formulas or quantify over a varying number of free variables. The construction is optimal in vertex count given the external-type count, but no uniqueness of optimal constructions is claimed. Older unpublished or differently worded exact cograph bounds might exist; a targeted literature and record search found no dominating statement, which is not a proof of priority. No independent mathematical or historical-priority review has been performed.

## References

1. J. Dreier, N. Mählmann and S. Toruńczyk, *First-Order Model Checking on Monadically Dependent Graph Classes*, arXiv:2611.08143v1 (first posted 2026-11-05). https://arxiv.org/abs/2611.08143
2. É. Bonnet, F. Foucaud, T. Lehtilä and A. Parreau, *Neighbourhood complexity of graphs of bounded twin-width*, arXiv:2301.04217 (2023), European Journal of Combinatorics 115 (2024), 103772. https://arxiv.org/abs/2301.04217
3. É. Bonnet, J. Duron, J. Sylvester and V. Zamaraev, *Adjacency Labeling Schemes for Small Classes*, ITCS 2025, Article 21. https://doi.org/10.4230/LIPIcs.ITCS.2025.21
4. G. Berthe, F. Foucaud, T. Lehtilä and A. Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, arXiv:2607.16889 (first posted 2026-07-18). https://arxiv.org/abs/2607.16889
