# Complete connected zero-forcing polynomials of partially whiskered cycles

## Finding
For every integer \(n\ge3\) and every subset \(A\subseteq\mathbb Z/n\mathbb Z\), let \(H(n,A)\) have cycle vertices \(v_0,\ldots,v_{n-1}\) and, for each \(i\in A\), exactly one private leaf \(w_i\) adjacent to \(v_i\). Its connected zero-forcing polynomial, marking the number of initially blue vertices, admits an explicit formula depending on the entire cyclic pattern \(A\), not only its cardinality.

For an integer \(2\le\ell<n\) and a starting index \(s\), put
\[
I_{s,\ell}=(s,s+1,\ldots,s+\ell-1),\qquad
J_{s,\ell}=(s+\ell,s+\ell+1,\ldots,s+n-1),
\]
where all indices are modulo \(n\). Let \(u=s+\ell-1\) and \(v=s\) be the boundary vertices of the selected interval, and let \(d_{s,\ell}=|A\cap\{s+1,\ldots,s+\ell-2\}|\), its number of leaf-bearing interior vertices. Write \(m=n-\ell\) and \(B_{s,\ell}=\{j\in\{1,\ldots,m\}:s+\ell+j-1\in A\}\). For \(e,f\in\{0,1\}\), define
\[
L_e=\begin{cases}0,&e=0,\\ \min B_{s,\ell},&e=1,\ B_{s,\ell}\ne\varnothing,\\m,&e=1,\ B_{s,\ell}=\varnothing,\end{cases}
\quad
R_f=\begin{cases}0,&f=0,\\m+1-\max B_{s,\ell},&f=1,\ B_{s,\ell}\ne\varnothing,\\m,&f=1,\ B_{s,\ell}=\varnothing.\end{cases}
\]
For a boundary vertex \(x\), set
\[
w_x(e;z)=\begin{cases}1,&x\notin A,\ e=1,\\0,&x\notin A,\ e=0,\\z,&x\in A,\ e=1,\\1,&x\in A,\ e=0.\end{cases}
\]
Then the **complete all-cardinality identity** is
\[
\boxed{
Z_C(H(n,A);z)=z^n(1+z)^{|A|}
+\sum_{\ell=2}^{n-1}\sum_{s=0}^{n-1}z^{\ell}(1+z)^{d_{s,\ell}}
\sum_{e,f\in\{0,1\}}w_u(e;z)w_v(f;z)
\mathbf1\{L_e+R_f\ge m\}.
}
\]
Here \(\mathbf1\) denotes the indicator of the displayed inequality. In particular, the two degree-sequence-equivalent graphs \(H(7,\{0,1,2\})\) and \(H(7,\{0,2,4\})\) have distinct complete polynomials:
\[
\begin{aligned}
Z_C(H(7,\{0,1,2\});z)&=6z^3+14z^4+22z^5+30z^6+32z^7+21z^8+7z^9+z^{10},\\
Z_C(H(7,\{0,2,4\});z)&=8z^5+20z^6+26z^7+19z^8+7z^9+z^{10}.
\end{aligned}
\]
The associated minimum connected forcing numbers \(3\) and \(5\) are included only to illustrate the new all-weight enumeration; the scalar minimum for arbitrary unicyclic graphs has a previously published algorithm.

## Assumptions and scope
All graphs are finite, simple, undirected, and labelled as specified. The initial blue set \(S\) is a connected zero-forcing set when \(H(n,A)[S]\) is connected and ordinary zero forcing (a blue vertex with exactly one white neighbor makes that neighbor blue) colors the entire graph. The polynomial is \(Z_C(H;z)=\sum_{S\text{ connected zero-forcing}}z^{|S|}\). At most one leaf may be attached to each cycle vertex. The empty set \(A\) and the full set \(A=\mathbb Z/n\mathbb Z\) are included.

## Proof
**1. Initial connected configurations.** A selected leaf whose support cycle vertex is not selected is isolated in the initially induced graph, unless it is the sole selected vertex. A lone leaf can force its cycle support, but that support then has two white cycle neighbors and the process stops. Hence all selected leaves have initially selected supports. A set containing fewer than two cycle vertices cannot force the cycle: one blue cycle vertex has two white cycle neighbors, and any initially blue private leaf cannot provide a second cycle seed. Therefore a connected forcing set either contains every cycle vertex or contains a unique selected cyclic interval \(I_{s,\ell}\) of size \(2\le\ell<n\). For the full cycle, the leaves are arbitrary, contributing \(z^n(1+z)^{|A|}\).

**2. The two-front obstruction.** Fix a proper initially blue interval \(I_{s,\ell}\), whose complementary white cycle segment has \(m=n-\ell\) vertices indexed \(1,\ldots,m\) from the end \(u\) toward \(v\). A boundary \(u\) can start forcing clockwise into the white segment precisely when it has no private leaf or its private leaf is initially blue. Let its activity flag be \(e=1\), and similarly let \(f=1\) mark an active opposite boundary \(v\). An inactive boundary has both an uncolored cycle neighbor and a white private leaf, so it cannot start a cycle force.

A forcing front that enters the white segment advances through undecorated cycle vertices. It can color the first decorated vertex, but that newly blue vertex has a white private leaf and, until the opposite front arrives, a white next cycle vertex. It consequently cannot advance farther into the segment. Thus the left front can color at most its first \(L_e\) vertices and the right front at most its last \(R_f\) vertices. This remains true for any interleaving of legal forces: a private leaf cannot color its parent when the parent was white, because that leaf was not initially selected, and a stalled decorated frontier cannot advance over a still-white core neighbor. If \(L_e+R_f<m\), a nonempty middle portion of the cycle stays permanently white. Thus the inequality is necessary.

Conversely, when \(L_e+R_f\ge m\), start the active left and right fronts and extend each through its allowed portion, stopping if the other front already colored a vertex. Their union covers the entire white cycle segment. At that point every cycle vertex is blue, and every still-white private leaf is the unique white neighbor of its parent and is forced. This proves sufficiency, including a one-vertex white segment and the possibility that one front is inactive.

**3. Counting without double counting.** Once \(I_{s,\ell}\) is fixed, every leaf at an internal vertex of the interval may independently be initially blue or white, giving \((1+z)^{d_{s,\ell}}\). For a boundary vertex in \(A\), the inactive and active choices respectively mean its leaf is initially white (weight \(1\)) or blue (weight \(z\)); for a boundary without a leaf only the active choice occurs, weight \(1\). The white gap is forceable exactly when the two reach lengths sum to at least \(m\). Multiplying these weights with the \(\ell\) initially blue cycle vertices gives the inner summand. Each proper nonempty cyclic interval has a unique starting index and length, so the double sum counts every connected forcing set once. The full-cycle case is disjoint. This proves the formula.

**4. Placement sensitivity.** Substitution of the two stated three-leaf patterns yields the displayed polynomials. Both graphs have three degree-one vertices, four degree-two vertices, and three degree-three vertices, so their degree multisets agree, while their entire connected-forcing distributions differ. For \(A=\mathbb Z/n\mathbb Z\) the formula reduces to the already known sunlet polynomial and the known minimum coefficient \(3n+1\) for \(n\ge4\); this specialization is not asserted as a new result.

## Verification
The standalone file `verify.py` evaluates the explicit interval formula and separately enumerates **every initial subset**, testing induced connectivity by graph traversal and reachability under the ordinary color-change rule. It verifies all \(2^n\) leaf-placement patterns for every \(n\in\{3,4,5,6\}\), a total of 120 patterns, and separately checks the two seven-cycle examples by exhaustive enumeration. It checks the full-sunlet specialization for \(3\le n\le14\).

Replay with `python verify.py`; the observed output is:

```text
VERIFY_OK exhaustive_leaf_patterns=120 n=3..6 labelled_placement_comparisons=120
DEGREE_SEQUENCE_CONTRAST_PASS n=7 three_leaves min_sizes=3_and_5
KNOWN_SUNLET_SPECIALIZATION_PASS n=3..14
```

These are finite checks of the explicit theorem. The infinite family is established by the preceding two-front proof, not by extrapolation from computation.

## Relationship to prior work
Mukherjee and Ray (arXiv:2611.10985, first posted 7 November 2026) recently developed connected zero-forcing polynomials for finite trees. The present graph family is unicyclic and therefore outside the tree theorem.

Brimkov (arXiv:1607.00658, Section 5.1) previously analyzed omitted cycle segments and derived a linear-time algorithm for the **minimum connected forcing number** of arbitrary unicyclic graphs. Its structural treatment strongly overlaps with the two-front obstruction. It does not supply the present all-size polynomial with arbitrary optional leaf seeds and their weights; no novelty is claimed for the scalar minimum problem or for the general concept of feasible cycle segments.

Brimkov, Davila, and Schuerger (arXiv:2507.11194, Sections 3 and 6.3) study connected-forcing counts for trees, extremal connected forcing sets, and coronas with an isolate-free attached graph. Their corona results do not cover a single private leaf (the attached \(K_1\) has an isolated vertex), and their tree formula is not a formula for partial cycles.

A published connected forcing polynomial for the fully leaf-decorated sunlet is already known (published-finding corpus record `2026/10/13/SCOPE-cardinality-enumerator-of-connected-forcing-sets-of-sunlet-graph--a54ae5ebc761`). Its full result was inspected. The present formula subsumes that previously covered endpoint \(A=\mathbb Z/n\mathbb Z\), but its claim is the **arbitrary cyclic subset** formula and the arrangement-sensitive full distribution, not the sunlet specialization. Separate earlier connected-forcing results for a cycle with one attached pendant path also address only a special case. Searches for partial sunlet, arbitrary leaf placement, connected forcing enumerators, and equivalent gap descriptions found no full-pattern all-size result; unknown unindexed literature remains a historical-priority risk.

## Limitations
This proof does not cover two or more pendant leaves at one cycle vertex, longer attached pendant paths, general unicyclic graphs with branching off the cycle, or the number of forcing chronologies. It supplies a finite explicit coefficient formula rather than a closed expression depending only on \(n\) and \(|A|\), which in general cannot determine the polynomial. The result is subject to independent verification and historical-priority review. The finite checks do not certify an unrestricted infinite search.

## References
1. S. Mukherjee and P. Ray, *On the connected zero forcing polynomial of finite trees*, arXiv:2611.10985v1 (7 November 2026), https://arxiv.org/abs/2611.10985 .
2. B. Brimkov, *Complexity and Computation of Connected Zero Forcing*, arXiv:1607.00658 (3 July 2016), https://arxiv.org/abs/1607.00658 .
3. B. Brimkov, R. Davila, and H. Schuerger, *Connected forcing density and related problems*, arXiv:2507.11194 (15 July 2025), https://arxiv.org/html/2507.11194v1 .
4. *Cardinality enumerator of connected forcing sets of sunlet graphs*, published-finding corpus (13 October 2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-cardinality-enumerator-of-connected-forcing-sets-of-sunlet-graph--a54ae5ebc761/RESULT.md .
