# Directed arborescences calibrate Shapley–core coincidence in trust games

## Finding

Let \(G=(V,E)\) be a finite loopless simple directed graph with every vertex's indegree \(d_i\ge2\). Give every arc \(j\to i\) the same positive weight \(b_i\in(0,1]\), depending on its target but not its source. In the standard directed trust cooperative game (Definition below), let \(\phi\) be its Shapley value and let \(c_i=d_i b_i\) be the unique core payoff. Define \(\tau_i(C)\) to be the number of spanning out-arborescences of a strongly connected component \(C\), rooted at \(i\): a directed spanning tree with every edge pointing away from \(i\).

**Theorem.** Some choice of strictly positive target weights \((b_i)\) makes \(\phi=c\) **if and only if** the condensation of \(G\) has no arcs, equivalently, \(G\) is a disjoint union of strongly connected digraphs. When this condition holds, **every** positive Shapley–core calibration is precisely
\[
 b_i=\lambda_C\,\frac{d_i+1}{d_i-1}\,\tau_i(C),\qquad i\in C,
\]
where independently for each component \(C\) the scalar \(\lambda_C>0\) is chosen small enough that \(b_i\le1\). In particular, on a strongly connected graph calibration exists and is unique up to a common positive factor. If distinct strongly connected components are joined by even one arc, no strictly positive target-homogeneous calibration exists.

The theorem gives a topology-only existence test and an explicit integer-combinatorial formula for all stabilizing trust intensities. In this restricted but natural domain, the generally different cooperative-game notions of Shapley fairness and core stability can be made to coincide exactly.

## Assumptions and scope

There are \(n=|V|\ge3\) vertices, no loops or duplicate ordered arcs, and every \(d_i=|N^-(i)|\ge2\). The game is transferable-utility, with coalition worth
\[
 v(S)=\sum_{(j,i)\in E\,:\,j,i\in S}b_i
 +\sum_{i\in S:\,N^-(i)\setminus S\ne\varnothing}b_i,
 \qquad S\subseteq V.
\]
The second term counts, for each coalition member, the minimum positive incoming weight from outside the coalition (or zero if none exists). These conventions are those of the directed trust game of Bandhana, Kroupa and García and Ryzák and Kroupa, restricted to equal weights on each vertex's incoming arcs. A *Shapley–core calibration* is a vector with \(0<b_i\le1\) for which the ordinary Shapley payoff equals the unique core allocation. The theorem makes an existence and full-parameter-classification claim for **this domain only**, not for arbitrary unequal incoming weights, isolated zero-indegree nodes, or a modified external-worth aggregator.

## Proof

**1. The unique core vector.** Fix a coalition \(S\). For each \(i\in S\), let \(r_i(S)\) be the number of its incoming arcs with tail outside \(S\). The candidate \(c_i=d_i b_i\) satisfies
\[
\sum_{i\in S}c_i-v(S)=\sum_{i\in S}b_i\bigl(r_i(S)-\mathbf1_{\{r_i(S)>0\}}\bigr)\ge0.
\]
Also \(c(V)=v(V)\), so \(c\) is in the core. Deleting vertex \(i\) from the grand coalition removes precisely the contributions of the arcs entering \(i\): any arc from \(i\) to a remaining vertex is recovered in the external minimum for that vertex. Thus \(v(V)-v(V\setminus\{i\})=d_i b_i=c_i\). Every core vector \(x\) therefore obeys \(x_i\le c_i\). Because \(x(V)=c(V)\), all these inequalities must be equalities. The core is the singleton \(\{c\}\).

**2. The exact Shapley discrepancy.** Write \(u_T(S)=\mathbf1_{\{T\subseteq S\}}\) for a unanimity game. The contribution of target \(i\) to coalition worth is exactly
\[
 v_i=b_i\left(u_{\{i\}}+\sum_{j\in N^-(i)}u_{\{i,j\}}-u_{\{i\}\cup N^-(i)}\right).
\]
Indeed, when \(i\) is present and exactly \(k<d_i\) predecessors are present, the contribution is \((k+1)b_i\); when all \(d_i\) predecessors are present it is \(d_i b_i\). Each member of the supporting set of \(u_T\) gets Shapley value \(1/|T|\). Set
\[
 t_i:=\frac{d_i-1}{2(d_i+1)}b_i>0.
\]
The contribution \(v_i\) grants player \(i\) the amount \(b_i(1+d_i/2-1/(d_i+1))=d_i b_i-d_i t_i\), while every predecessor \(j\in N^-(i)\) receives \(b_i(1/2-1/(d_i+1))=t_i\). Summing over targets gives the exact identity
\[
 \boxed{\ \phi_i-c_i=\sum_{(i,j)\in E}t_j-d_i t_i.\ }
\]
Hence Shapley–core coincidence is equivalent to the positive network-balance equations \(d_i t_i=\sum_{i\to j}t_j\) at every vertex.

**3. Arborescence balance, with a direct bijection.** In any finite strongly connected digraph \(C\), let \(\tau_i(C)>0\) count the spanning out-arborescences rooted at \(i\). We establish
\[
 d_i\tau_i(C)=\sum_{i\to j\ \mathrm{in}\ C}\tau_j(C).
\]
Count pairs consisting of an out-arborescence rooted at \(i\) and a selected incoming arc \(u\to i\). Add that arc to the tree; the resulting unique directed cycle follows the tree path from \(i\) to \(u\) and ends with \(u\to i\). If its first arc is \(i\to j\), delete \(i\to j\). The remaining tree is an out-arborescence rooted at \(j\), together with the distinguished arc \(i\to j\). Conversely, add that arc to an out-tree rooted at \(j\), and delete the arc entering \(i\) on the unique directed cycle. These operations are mutual inverses. The two sides of the displayed equation count these two types of pairs.

Suppose \(t>0\) solves the balance equations on a strongly connected \(C\). Writing \(q_i=t_i/\tau_i(C)\), the balance identities show that \(q_i\) is a convex combination of the \(q_j\) over outgoing neighbors of \(i\), with strictly positive coefficients \(\tau_j/(d_i\tau_i)\). A vertex maximizing \(q_i\) can only average equals. Strong connectivity propagates equality to every vertex. Thus \(t_i=\kappa_C\tau_i(C)\), for one \(\kappa_C>0\). Replacing \(t_i\) by its defining expression in \(b_i\) yields exactly the theorem's formula (with \(\lambda_C=2\kappa_C\)). Conversely that formula satisfies the balance equations, establishing existence and uniqueness up to scale.

**4. Why connections between components forbid positive calibration.** Suppose the condensation graph has an arc. In some weakly connected component of the condensation DAG containing an arc, take a source strongly connected component \(C\) with at least one outgoing arc; it has no incoming arc from other components. Sum the balance equations over \(i\in C\). The internal-edge contributions cancel, but each outgoing arc \(i\to j\) with \(j\notin C\) contributes the strictly positive \(t_j\) on the right, with no external contribution on the left. This is impossible. When no inter-component arcs exist, apply Step 3 independently within each strongly connected component, choosing \(\lambda_C\) sufficiently small to respect the unit upper bounds. This proves both directions and the full solution set.

## Verification

The accompanying `verify_trust.py` independently computes the game directly for every coalition, computes the Shapley value by enumerating all player permutations (not from the derived formula), and verifies the singleton-core vector against all coalition inequalities. It also independently enumerates rooted out-arborescences and checks the balance identity, and solves exact rational stationary equations on strongly connected examples.

Running `python verify_trust.py` with Python's standard library yields:

```
EXACT_CHECKS_OK graph_parameter_checks=1528 calibrated_strongly_connected=369 tree_identities=257
4-vertex calibration: ['2/3', '2/3', '2/3', '4/9'] core/Shapley: ['4/3', '4/3', '4/3', '4/3']
```

These finite checks probe the formula and boundary examples; the argument above, not finite enumeration, proves the statement for all finite graphs satisfying the assumptions. For the four-vertex example take all directed arcs except \(0\to1\), \(1\to2\), and \(2\to0\); its indegrees are \((2,2,2,3)\) and its out-arborescence counts are \((7,7,7,7)\).

## Relationship to prior work

Bandhana, Kroupa and García (2024) introduced the underlying directed trust game and used its Shapley value for global trust scoring. Ryzák and Kroupa (arXiv:2605.18157v1, first public May 18, 2026) gave the general unanimity decomposition, Shapley and Banzhaf formulas, and a singleton-core theorem, emphasizing that Shapley and core generally disagree. These formulas establish the starting objects; they do **not themselves** classify which network topologies admit a positive target-homogeneous calibration, give the unique positive calibration up to scale, or identify its spanning-arborescence enumerator. The present theorem answers that structurally restricted inverse question using a direct graph-theoretic bijection and a condensation obstruction. Standard finite-state Markov-chain stationary-vector theory provides a related interpretation of the positive balance equations, but is not needed for the proof.

## Limitations

Target homogeneity of each incoming weight and indegree at least two are essential to the specified parameterization; no existence assertion is made when these fail. The claim concerns existence and uniqueness of calibrations **given topology**, not estimation of real-world reputation or strategic resistance to dishonest reports. The general Shapley decomposition in the literature makes the derivation of the network-balance equations accessible; an independently discovered equivalent calibration criterion may exist. The program exhaustively checks only its stated finite families and is not an infinite proof. No independent scientific validation has been performed.

## References

1. Arti Bandhana, Tomáš Kroupa, and Sebastián García, *Trust in Shapley: A Cooperative Quest for Global Trust in P2P Network*, AAMAS 2024, pp. 132–140. https://aamas.csc.liv.ac.uk/Proceedings/aamas2024/pdfs/p132.pdf
2. David Ryzák and Tomáš Kroupa, *A Tractable Class of Cooperative Games Defined by Directed Networks: Unanimity Decomposition and Shapley Value*, arXiv:2605.18157v1, May 18, 2026. https://arxiv.org/html/2605.18157
