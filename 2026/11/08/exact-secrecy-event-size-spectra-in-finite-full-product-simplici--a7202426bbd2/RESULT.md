# Exact secrecy-event size spectra in finite full-product simplicial models

## Finding

A complete chromatic product has one vertex of each agent-colour in each facet, with all coordinate combinations present. For every owner local state, the possible truth sets of an atomic proposition that are secret for that owner have a **complete size enumerator**, a sharp minimum number of false facets, and an explicit number of extremal events.

For \(k\ge2\), let the agents be \(A=\{a\}\cup B\), with \(B\ne\varnothing\). For each agent \(i\), take \(n_i\ge1\) distinct local-state vertices, and all facets \(F=\prod_{i\in A}[n_i]\). Fix one owner vertex \(v\in[n_a]\). An event \(U\subseteq F\) is *owner-secret-realizable* if some valuation of one atom \(p\) and some secrecy neighborhood functions satisfying (SN) make its truth set exactly \(U\) and make \(S_a p\) true at every facet in the star of \(v\).

Put \(N=\prod_{i\in A}n_i\), and write \(E_h\) for the number of owner-secret-realizable events with exactly \(h\) false facets. Then their exact generating polynomial is

\[
\boxed{\sum_{h=0}^{N} E_h z^h =
\sum_{(t_b)_{b\in B}\,:\,0\le t_b\le n_b}
(-1)^{\sum_{b\in B}(n_b-t_b)}
\left(\prod_{b\in B}\binom{n_b}{t_b}\right)
(1+z)^{(n_a-1)\prod_{b\in B}t_b}.}
\]

If \(n_a=1\), the polynomial is zero: no atomic secret event is possible at that owner state. If \(n_a\ge2\), put \(t=\max_{b\in B}n_b\), and choose any \(b_*\in B\) with \(n_{b_*}=t\). The sharp minimum number of false facets, the largest possible secret truth set, and the exact number of maximal-size secret events are respectively

\[
\boxed{\min\{h:E_h>0\}=t,\qquad \max |U|=N-t,\qquad
E_t=(n_a-1)^t\prod_{b\in B\setminus\{b_*\}} n_b!\left\{\begin{matrix}t\\ n_b\end{matrix}\right\}.}
\]

Here \(\left\{\begin{smallmatrix}t\\q\end{smallmatrix}\right\}\) denotes a Stirling number of the second kind (so \(q!\left\{\begin{smallmatrix}t\\q\end{smallmatrix}\right\}\) counts surjections from a \(t\)-element set to a \(q\)-element set). The displayed expression is independent of which tied largest coordinate is chosen as \(b_*\).

In the two-agent case \(B=\{b\}\), the enumerator simplifies to

\[
\boxed{\sum_h E_hz^h=\big((1+z)^{n_a-1}-1\big)^{n_b},\qquad
\sum_h E_h=(2^{n_a-1}-1)^{n_b}.}
\]

Thus a complete \(3\times3\) grid has exactly \(27\) owner-secret-realizable atomic events, of which \(8\) have the maximum possible size \(6\). A \(2\times2\times2\) grid has polynomial \(2z^2+4z^3+z^4\), so its \(7\) eligible events include exactly \(2\) extremal ones.

## Assumptions and scope

The complex is the downward closure of the **full** Cartesian product of finite nonempty local-state sets, with every facet containing exactly one vertex from each agent. All facets are distinct, and atomic valuations are arbitrary subsets of facets. The owner local vertex \(v\) is fixed, rather than averaged over vertices. The agent set has cardinality at least two. The secrecy semantics are exactly the local-state neighborhood semantics of Wang, *A Logic of Secrecy on Simplicial Models*, Definition 3.8 (condition (SN)) and Definition 3.10, first posted April 3, 2026. No assumptions of upward closure, regularity, or logical omniscience are imposed on the secrecy neighborhood family beyond the source's definition.

If \(\operatorname{St}(v)\) denotes the owner's star, then \(S_a p\) at any facet in this star requires both \(\operatorname{St}(v)\subseteq U\) and \(U\in N_a^S(v)\). The designated neighborhood may be exactly \(\{U\}\); all other agent-vertex neighborhoods may be empty. The counting is of distinct **events** \(U\) with the owner fixed, not of neighborhoods or all models.

## Proof

**1. Projection characterization.** For every facet \(X\), two facets are indistinguishable to agent \(b\) precisely when their \(b\)-coordinates agree. Let \(H=F\setminus U\). If \(S_a p\) is true at the owner state, the knowledge conjunct forces \(\operatorname{St}(v)\subseteq U\), so \(H\subseteq F\setminus\operatorname{St}(v)\). The (SN) clause requires that for every \(X\in\operatorname{St}(v)\) and every \(b\in B\), there be \(Y\in H\) with \(Y_b=X_b\). In a full product, the values \(X_b\) as \(X\) ranges through the owner star exhaust \([n_b]\). Therefore (SN) is equivalent to

\[
\boxed{\pi_b(H)=[n_b]\quad\text{for every }b\in B.}
\]

Conversely, given such an \(H\) outside the owner star, set \(U=F\setminus H\), value the atom \(p\) true exactly on \(U\), put \(N_a^S(v)=\{U\}\), and set all other secrecy neighborhoods to the empty family. The projection condition supplies every witness required by (SN), and knowledge holds because the whole owner star lies in \(U\). Thus this construction realizes exactly the claimed events, including all their possible sizes.

**2. Exact generating polynomial.** The outside-star cells form the product \(G=([n_a]\setminus\{v\})\times\prod_{b\in B}[n_b]\), of cardinality \((n_a-1)\prod_{b\in B}n_b\). A chosen subset \(H\subseteq G\) fails to cover a value \(j\in[n_b]\) precisely when it avoids the hyperplane \(\{x\in G:x_b=j\}\). Apply inclusion-exclusion over all forbidden missing coordinate values, independently for all \(b\in B\). If \(t_b\) labels for coordinate \(b\) are still allowed, there are \((n_a-1)\prod_b t_b\) available outside-star cells. The size-generating function of all their subsets is \((1+z)^{(n_a-1)\prod_b t_b}\). The sign and multiplicity of each allowed-label choice are \((-1)^{\sum_b(n_b-t_b)}\prod_b\binom{n_b}{t_b}\). Summing yields the stated polynomial. For \(n_a=1\), no \(H\) can project onto the nonempty non-owner coordinate sets, so every coefficient vanishes.

**3. Sharp minimum and its multiplicity.** Assume \(n_a\ge2\). Every \(H\) projecting surjectively onto the largest non-owner coordinate \([t]\) has \(|H|\ge t\). Conversely, label \(t\) selected facets by the distinct values of \(b_*\). For each of the other agents \(b\in B\setminus\{b_*\}\), choose a surjective assignment from these \(t\) labels onto \([n_b]\); for the owner's coordinate choose independently one of its \(n_a-1\) non-\(v\) local states for each label. These choices produce \(t\) distinct facets, cover every required non-owner coordinate, and so attain the lower bound.

At equality \(|H|=t\), the \(b_*\)-projection is a bijection, giving a unique labeling by \([t]\) for each such \(H\). Each other coordinate is exactly a surjective function on that label set; it has \(n_b!\left\{\begin{smallmatrix}t\\n_b\end{smallmatrix}\right\}\) possibilities. The owner coordinate has \((n_a-1)^t\) choices. Multiplying proves the extremizer formula and shows there is no overcounting. The same argument works with any coordinate tied for the maximum.

**4. Two agents.** When \(B\) has one agent \(b\), the outside-star cells split into \(n_b\) disjoint columns of size \(n_a-1\). Each column must contain a nonempty part of \(H\), whose polynomial is \((1+z)^{n_a-1}-1\). Multiplying over columns proves the stated specialization.

## Verification

The standalone Python 3 checker `CHECKER.py` has no external dependencies. Run `python3 CHECKER.py` to compare, for each tested full product, direct enumeration of all atomic events satisfying the original (SN) clause against a separately evaluated inclusion-exclusion coefficient array. It additionally checks the sharp minimum and extremizer formula, including the \(n_a=1\) impossibility boundary. In the completed local test it reported `PASS: 108 parameter vectors, 54522 candidate-event inspections`, including all configurations with two to four agents in the stated script loops and at most twelve cells outside the owner star. Further assertions check the examples and a larger symbolic \((4,3,5,2)\) case whose extremizer count is \(1{,}093{,}500\).

The proof above establishes the statements for all finite parameters; exhaustive checks are finite corroboration, not an infinite proof. Values are exact integers; no randomization, numerical approximation, or unreported computation is needed.

## Relationship to prior work

Wang's April 3, 2026 preprint introduces the original (SN) secrecy-neighborhood semantics, establishes the owner-local restriction in Lemma 3.12, and supplies a \(3\times3\) example (Example 3.13). Those definitions and the example are prior work; they are not claimed here as new. The inspected source concerns semantics, axiomatization, and completeness and does not give the full size enumerator or the sharp arbitrary-agent extremal spectrum proved here.

The proof uses classical inclusion-exclusion, surjection counts, and Stirling numbers, which are standard mathematical tools. The result should be read as an exact classification of owner-secret-realizable events under these specific new modal semantics, not as a new general theorem about arbitrary Cartesian-product relations or covering arrays. The full-product and atom-valuability assumptions are essential.

## Limitations

The theorem applies to full-product chromatic complexes and a fixed owner local state; sparse subcomplexes, restrictions on valuations, and simultaneous secrecy constraints at multiple owner states may have different spectra. An event being compatible with the semantics is not a proof of cryptographic privacy in a communication protocol. No independent mathematical or historical-priority audit has been performed. Equivalent counting formulas in older combinatorial literature remain a priority risk; the structural translation into the specific secrecy semantics is the domain-specific contribution.

## References

- Shanxia Wang, *A Logic of Secrecy on Simplicial Models*, arXiv:2604.02673v1 (posted 2026-04-03), Sections 3.2–3.5, especially Definitions 3.8 and 3.10, Lemma 3.12, and Example 3.13. https://arxiv.org/html/2604.02673v1
- Standard inclusion-exclusion and Stirling-number identities are used in the proof, without claiming priority over their classical combinatorial forms.
