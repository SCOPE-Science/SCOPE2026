# Six-patch threshold and degree-assortativity law for fragmentation skewness on trees

## Finding

For independent site survival on a tree-shaped habitat network, the first two cumulants of the number of occupied habitat fragments depend only on the number of sites and the degree-sequence second factorial moment. The third cumulant depends additionally on the number of four-vertex simple paths, which detects degree correlations along habitat corridors. The smallest pair of distinct tree-shaped landscapes that have identical expected fragment counts and variances at every survival probability, but different skewness numerators, has six sites.

More precisely, with the definitions below, the exact third-cumulant law is

\[
\begin{aligned}
\kappa_3(K_T)={}&npq(1-2p)-mp^2q(7-17p+10p^2-2p^3)\\
&+12Hp^3q^3-6Jp^4q(1-2p)-6P_4(T)p^4q^2,
\end{aligned}
\]

where \(q=1-p\). If two trees have the same degree multiset, then

\[
\kappa_3(K_T)-\kappa_3(K_{T'})=-6p^4(1-p)^2\bigl(P_4(T)-P_4(T')\bigr).
\]

This formula is valid for all finite trees and all real \(p\in[0,1]\). Distinctness of the displayed cumulant differences is strict when \(p\in(0,1)\).

## Assumptions and scope

The fixed habitat network \(T=(V,E)\) is a finite, simple, undirected tree with \(n=|V|\ge2\) and \(m=|E|=n-1\). Each site \(v\) is retained independently with probability \(p\). The occupied graph is the vertex-induced subgraph on retained sites; a surviving habitat component is a maximal connected occupied set. The random variable \(K_T\) counts these components, with \(K_T=0\) if no sites survive. No edges survive independently: an edge is present precisely when both endpoints survive. No claim is made about spatial lattices with cycles, heterogeneous probabilities, correlated occupancy, or real ecological parameter estimates.

Write \(d_v=\deg_T(v)\), \(q=1-p\), and define

\[
H=\sum_{v\in V}\binom{d_v}{2},\qquad
J=\sum_{v\in V}\binom{d_v}{3},\qquad
P_4(T)=\sum_{uv\in E}(d_u-1)(d_v-1).
\]

The last count is exactly the number of unoriented simple paths consisting of three edges (four distinct vertices): each such path has a unique middle edge \(uv\), and its two outer vertices can be selected in \((d_u-1)(d_v-1)\) ways. Thus \(P_4\) measures adjacency of excess degrees, rather than just the degree multiset. The third cumulant is the third centered moment \(\kappa_3(K_T)=\mathbb E[(K_T-\mathbb EK_T)^3]\).

## Proof

**1. Forest identity and first two moments.** Define independent Bernoulli indicators \(X_v\) for site occupancy and \(Y_{uv}=X_uX_v\) for each edge. Every induced subgraph of a tree is a forest; its number of components is its vertices minus its edges. Therefore, with \(S=\sum_v X_v\) and \(B=\sum_{uv\in E}Y_{uv}\),

\[
K_T=S-B.
\]

Directly, \(\mathbb E S=np\) and \(\mathbb E B=mp^2\). Since \(\operatorname{Var}(X_v)=pq\), \(\operatorname{Var}(Y_e)=p^2(1-p^2)\), \(\operatorname{Cov}(X_v,Y_e)=p^2q\) if \(v\in e\) and zero otherwise, and \(\operatorname{Cov}(Y_e,Y_f)=p^3q\) for distinct adjacent edges (zero for disjoint edges), summation gives

\[
\mathbb EK_T=np-mp^2,\qquad
\operatorname{Var}(K_T)=pq\left[n-3mp+(m+2H)p^2\right].
\]

There are \(2m\) site-edge incidences and \(H\) unordered incident-edge pairs, proving the covariance multiplicities used here.

**2. The third-cumulant classification.** For variables \(U,V,W\), the mixed third cumulant is

\[
\kappa(U,V,W)=\mathbb E[UVW]-\mathbb E[UV]\mathbb EW
-\mathbb E[UW]\mathbb EV-\mathbb E[VW]\mathbb EU
+2\mathbb EU\mathbb EV\mathbb EW.
\]

It vanishes whenever the supports of the three factors split into two independent groups. Classify surviving triples using (a) repeated edge, (b) two distinct incident edges, and (c) three distinct edges forming either a three-edge star or a three-edge path. There are respectively \(m\), \(H\), \(J\), and \(P_4(T)\) underlying configurations, with the multiplicities of ordered triples built into these exact identities:

\[
\begin{aligned}
\kappa_3(S)={}&npq(1-2p),\\
\kappa(S,S,B)={}&2mp^2q(2-3p),\\
\kappa(S,B,B)={}&2mp^2q(1-2p^2)+2Hp^3q(3-4p),\\
\kappa_3(B)={}&mp^2(1-p^2)(1-2p^2)\\
&+6Hp^3q(1-2p^2)+6Jp^4q(1-2p)+6P_4(T)p^4q^2.
\end{aligned}
\]

To check the nonstandard terms explicitly: the joint cumulant of three distinct edge indicators is \(p^4q(1-2p)\) on an edge star, and \(p^4q^2\) on a length-three path; all other distinct-edge triples have disconnected dependency support and contribute zero. An incident pair with one edge repeated has cumulant \(p^3q(1-2p^2)\). Each of these contributions occurs in six orders, accounting for the coefficients of \(H\), \(J\), and \(P_4\) in the final expression for \(\kappa_3(B)\). Substitution into the multilinear identity

\[
\kappa_3(K_T)=\kappa_3(S)-3\kappa(S,S,B)
+3\kappa(S,B,B)-\kappa_3(B)
\]

gives the claimed third-cumulant formula. Since \(H\) and \(J\) are determined by the degree multiset, subtracting the formula for two trees with that multiset leaves exactly the \(P_4\) term.

**3. The smallest indistinguishable pair.** For a fixed vertex count, the first-moment polynomials agree for every pair of trees, while their variance polynomials agree for all \(p\) precisely when the two trees have the same \(H\). For \(n\le 5\), the nonisomorphic tree shapes have different \(H\): at \(n=4\) the two values are \(2,3\), and at \(n=5\) the three values are \(3,4,6\); for smaller positive sizes there is only one tree. Thus no smaller pair can have identical mean and variance curves yet different third cumulants.

At \(n=6\), the six nonisomorphic tree shapes have \(H\)-values \(4,5,5,6,7,10\). The two with \(H=5\) have three branches attached to a central degree-three vertex, with arm lengths \((3,1,1)\) and \((2,2,1)\). Both have the degree multiset \((3,2,2,1,1,1)\). Their \(P_4\) values are \(3\) and \(4\), respectively. Therefore the second-minus-first third-cumulant difference is \(-6p^4q^2\), nonzero for all \(p\in(0,1)\). This proves that six is sharp and that the first pair is unique up to isomorphism and exchange.

One fully labeled realization uses sites \(0,1,2,3,4,5\). The \((3,1,1)\) tree has edges \(\{01,02,03,34,45\}\); the \((2,2,1)\) tree has edges \(\{01,02,03,24,35\}\). In the first tree, among the \(\binom64=15\) induced four-site subsets, the fragment-count frequencies for one, two, three, four components are respectively \((4,8,2,1)\); in the second they are \((5,5,5,0)\). For all other subset sizes the two distributions coincide. Consequently, with \(t\) the component-count generating-function variable,

\[
\mathbb E[t^{K_{(2,2,1)}}]-\mathbb E[t^{K_{(3,1,1)}}]
=p^4q^2(t-3t^2+3t^3-t^4)
=-p^4q^2t(t-1)^3.
\]

This also proves the third-cumulant difference directly because the difference of the first two derivatives at \(t=1\) vanishes and the third derivative is \(-6p^4q^2\).

## Verification

The accompanying standalone `verify.py` runs using Python 3.9 or later and only the standard library:

```sh
python3 verify.py
```

It enumerates all unlabeled tree classes on two through six vertices from Prüfer codes with a canonical tree-isomorphism code, checks the exact first-, second-, and third-cumulant formulas by complete occupied-subset enumeration at four rational survival probabilities on every class, verifies that the only mean-and-variance collision at six vertices has the two distinct \(P_4\) values, and checks the witness subset-count table and rational third-cumulant difference. The exact output ends with `EXACT_OK`. The all-tree, all-probability statement is proved by the cumulant classification above; the finite checker alone would not prove it.

## Relationship to prior work

Tittmann, Averbouch and Makowsky [1], particularly their Section 8, introduced the full induced-subgraph component polynomial and explicitly derived the probability distribution of the number of surviving components under uniform independent vertex survival. Thus the *model, general probability-generating framework, and formal ability to calculate any moment* are established prior work. The claimed distinction is the structural closed formula for the third cumulant of occupied fragments on arbitrary finite trees, its exact dependence on the four-site path count after fixing degrees, and the unique sharp six-site mean/variance-indistinguishable skewness separation. Computing the complete component distribution by [1] for a given tree subsumes the ability to compute its third moment, but does not state this network-structural comparison or its minimal threshold.

Liao and Hou [2], Section 3, derive four-vertex path information from the *full* component polynomial in a regular bipartite graph. Here the graph is an arbitrary tree, the input statistics are only three low-order cumulants, and the comparison is between trees with the same degree multiset. Gastner and colleagues [3] use independent occupancy and connected patches to analyze ecological habitat fragmentation, principally for lattice and gradient models. Their ecological framing motivates this tree-network case; their scaling law does not yield a finite-tree skewness identity.

## Limitations

The finding concerns only independent, identically distributed site occupancy on finite trees. The component count may be much simpler to calculate than real-world ecological connectedness, which often includes cycles, unequal survival probabilities, dispersal across vacant patches and environmental correlations. The third cumulant determines the scalar \(P_4\) when the degree multiset is known, but does **not** generally determine a complete tree topology or a full fragment-count distribution. The structural theorem and finite cutoff have not undergone independent scientific audit; historical mathematical priority beyond the inspected primary works also remains provisional.

## References

1. P. Tittmann, I. Averbouch and J. A. Makowsky, *The Enumeration of Vertex Induced Subgraphs with respect to the Number of Components*, arXiv:0812.4147 (first public version 22 December 2008), especially Sections 2 and 8. https://arxiv.org/abs/0812.4147
2. H. Liao and Y. Hou, *Note on the Subgraph Component Polynomial*, *Electronic Journal of Combinatorics* **21** (2014), #P3.27, especially Section 3. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i3p27/pdf/
3. M. T. Gastner, B. Oborny, D. K. Zimmermann and G. Pruessner, *Transition from Connected to Fragmented Vegetation across an Environmental Gradient: Scaling Laws in Ecotone Geometry*, *The American Naturalist* **174** (2009), 23–39. https://doi.org/10.1086/599292
