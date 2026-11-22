# A cubic shattering polynomial for spanning trees of wheels

## Finding
For every integer \(m\ge3\), let \(W_{m+1}=K_1\vee C_m\) be a labelled wheel with rim edges \(e_i=\{v_i,v_{i+1}\}\) and spokes \(f_i=\{h,v_i\}\), where subscripts are modulo \(m\). Let \(\mathcal T_m\) consist of the edge-incidence vectors of *all* spanning trees of this wheel. A support \(S\subseteq E(W_{m+1})\) is shattered when every subset of \(S\) is the intersection of \(S\) with some spanning tree.

The complete shattering polynomial \(\Phi_m(z)=\sum_{S\text{ shattered}}z^{|S|}\) has the **all-order cubic representation**
\[
\boxed{\Phi_m(z)=p_m(z)-4z^m,\qquad m\ge3,}
\]
where
\[
\begin{split}
p_0(z)&=3,\\
p_1(z)&=1+4z,\\
p_2(z)&=1+4z+8z^2,\\
p_m(z)&=(1+4z)p_{m-1}(z)-(2z+4z^2)p_{m-2}(z)+z^2p_{m-3}(z)\quad(m\ge3).
\end{split}
\]
Equivalently, writing \(Q(t,z)=1-(1+4z)t+(2z+4z^2)t^2-z^2t^3\), its rational bivariate generating function is
\[
\boxed{\sum_{m\ge3}\Phi_m(z)t^m=\frac{(1+4z)t-(4z+8z^2)t^2+3z^2t^3}{Q(t,z)}-\frac{4zt}{1-zt}-t-(1+4z+4z^2)t^2.}
\]
In particular, the first three wheels have polynomials
\[
\begin{aligned}
\Phi_3(z)&=1+6z+15z^2+12z^3,\\
\Phi_4(z)&=1+8z+28z^2+48z^3+28z^4,\\
\Phi_5(z)&=1+10z+45z^2+110z^3+140z^4+60z^5.
\end{aligned}
\]
The total number of shattered supports is, for every \(m\ge3\),
\[
\boxed{\Phi_m(1)=\sum_{j=1}^3\bigl(2+2\cos(2\pi j/7)\bigr)^m-4,}
\]
and hence grows asymptotically as \(\bigl(2+2\cos(2\pi/7)\bigr)^m\). The VC and Littlestone dimensions both equal \(m\). The highest-degree coefficient is \(2^{m+1}-4\); this top coefficient was independently known from the wheel complementary-tree census and is not claimed as new. At rim length \(m=5\), the shattering complex is already nonpure: it has exactly five facets of size four and 60 facets of size five, in contrast to pure matroid independence complexes.

## Assumptions and scope
All edges and rim vertices are labelled and distinct; the hub is distinct from every rim vertex. A spanning tree includes all \(m+1\) vertices, and the empty query support is shattered. The enumerator counts distinct edge supports, not trace multiplicities, abstract isomorphism classes or colorings with freely permutable edge labels. The symbolic recurrence is exact for arbitrarily large \(m\), not an extrapolation from finite data. The nonpurity assertion is made explicitly at \(m=5\); no assertion about facets for all larger rim lengths is needed.

## Proof
**1. The general shattering lemma (background).** For a connected graph \(G\), the spanning-tree edge concept family shatters \(S\subseteq E(G)\) if and only if \(S\) is cycle-free and \(G-S\) is connected. Necessity is immediate from the all-positive and all-negative traces. For sufficiency, fix any desired positive subset \(P\subseteq S\). The graph \(G-(S\setminus P)\) contains the connected graph \(G-S\), hence is connected. It also contains the forest \(P\). Extending \(P\) to a spanning tree within this graph realizes exactly \(P\) on \(S\). This general lemma, also used for complete bipartite graphs in the cited earlier work, is not the novelty claimed here.

**2. Two simultaneous wheel-forest conditions.** Identify the \(m\) bounded triangular faces of the plane wheel with \(F_i=(h,v_i,v_{i+1})\), and the unbounded face with the dual hub. The planar dual is another \(m\)-rim wheel. Under its edge correspondence, the primal rim edge \(e_i\) becomes the dual spoke at \(F_i\), while primal spoke \(f_i\) becomes the dual rim edge between \(F_{i-1}\) and \(F_i\). By planar cycle-cut duality, \(G-S\) is connected exactly when the dual edges corresponding to \(S\) are cycle-free. Thus \(S\) is shattered precisely if it is a forest in both these wheel structures.

Write \(r_i=\mathbf1\{e_i\in S\}\), \(s_i=\mathbf1\{f_i\in S\}\). A wheel edge set is a forest precisely if the full rim cycle is not selected and every connected component of its selected rim-edge subgraph contains at most one selected spoke. Indeed, selected rim edges then form paths or isolated vertices, and adding two spokes to the same path creates a hub cycle; with at most one spoke per path no cycle exists. The same criterion holds in the dual, with \(r_i\) playing the role of dual spokes and \(s_i\) the role of dual rim edges, shifted by the face indexing above.

**3. An exact cyclic finite-state automaton.** At each rim index \(i\) introduce a state \((r_i,s_i,c_i,d_i)\in\{0,1\}^4\). Informally, \(c_i\) counts the selected spokes from the beginning of the current run of selected primal rim edges through \(v_i\); \(d_i\) similarly counts selected primal rim edges from the beginning of the current run of selected dual rim edges through face \(F_i\). The precise local rules, which also define the states on a circle without choosing a starting break, are
\[
\boxed{c_{i+1}=s_{i+1}+r_ic_i,\qquad d_{i+1}=r_{i+1}+s_{i+1}d_i,\qquad 0\le c_i,d_i\le1.}
\]
The first rule resets at a missing primal rim edge, and otherwise accumulates the next spoke. The second resets at a missing dual rim edge, and otherwise accumulates the next dual spoke. If both cyclic rim indicator words contain a zero, the allowed states are uniquely determined by the edge indicators and exist if and only if the primal and dual selected graphs are forests.

Index a \(16\times16\) matrix \(T(z)\) by the ordered binary quadruples. The entry from \((r,s,c,d)\) to \((R,S,C,D)\) is \(z^{R+S}\) if \(C=S+rc\le1\) and \(D=R+Sd\le1\), and is zero otherwise. Consequently \(\operatorname{tr}(T(z)^m)\) counts all length-\(m\) cyclic indicator words with allowed state assignments, weighted by their selected-edge cardinalities.

There are precisely two exceptional indicator words: all \(r_i=1,s_i=0\), and all \(r_i=0,s_i=1\). Each selects a complete rim cycle in respectively the primal and dual wheel, hence must be excluded. Each nevertheless has *two* cyclic automaton-state assignments, because its nonresetting accumulator may be constantly zero or one. Other words with one all-one rim indicator and a positive opposite indicator have no cyclic state assignment (summing the relevant recursion around the cycle gives a contradiction). Therefore the exact correction is \(4z^m\), proving
\[
\Phi_m(z)=\operatorname{tr}(T(z)^m)-4z^m.
\]

**4. Cubic reduction and rationality.** Exact polynomial elimination on the explicitly defined fixed-size transfer matrix gives
\[
\det(I-tT(z))=1-(1+4z)t+(2z+4z^2)t^2-z^2t^3=Q(t,z).
\]
The executable symbolic determinant check in `verify/check_symbolic.py` reconstructs the sixteen states and verifies this *polynomial identity*, not merely numeric specializations. From the formal identity \(-t\partial_t\log\det(I-tT)=\sum_{m\ge1}\operatorname{tr}(T^m)t^m\), the displayed rational generating function follows by subtracting \(4zt/(1-zt)\) and the formal coefficients of degrees one and two. Equivalently, the three nonzero eigenvalues of \(T\) are the roots of \(\lambda^3-(1+4z)\lambda^2+(2z+4z^2)\lambda-z^2\), counted with multiplicity. Newton identities give \(p_0,p_1,p_2\) and the cubic recurrence for all \(m\ge3\), completing the all-order calculation.

**5. Total count, degree and dimensions.** Setting \(z=1\) produces the cubic \(\lambda^3-5\lambda^2+6\lambda-1\), whose three roots are \(2+2\cos(2\pi j/7)\) for \(j=1,2,3\); substitution using the triple-angle/cyclotomic identities verifies the equation. The largest root is strictly larger in absolute value than the other two, proving the total-count formula and growth rate. Every shattered support has at most \(m\) edges because it is a forest on \(m+1\) vertices. Conversely, each nonconstant binary coloring of the rim extends in exactly two ways to an ordered pair of complementary spanning trees, by alternating spoke colors at rim-run boundaries and forcing opposite colors in their interiors. Hence there are \(2^{m+1}-4\) shattered supports of size \(m\). The VC dimension is therefore \(m\). A depth-\((m+1)\) Littlestone tree would have an all-positive branch using \(m+1\) distinct queried edges, impossible for a family of \(m\)-edge trees. Since Littlestone dimension is at least VC dimension, it is also \(m\). The complementary-tree count and the general fixed-cardinality online upper bound are previously implicit or known and serve as consistency checks, not stand-alone novelty claims.

**6. First nonpure boundary.** At \(m=5\), the support \(S=\{e_2,e_4,f_0,f_2\}\) passes the forest/complement-connectivity criterion but none of its six absent edges can be added while retaining that criterion: adding \(e_3,f_3,f_4\) creates a selected cycle, whereas adding \(e_0,e_1,f_1\) disconnects the complement. Thus it is an inclusion-maximal shattered four-support, while five-supports also exist. Exhausting the \(2^{10}=1024\) candidate supports via the precise two-graph criterion gives exactly five such four-facets and 60 five-facets. The code directly rechecks the finite claims.

## Verification
The standard-library Python script `verify/check_wheel.py` independently enumerates every edge subset for \(3\le m\le8\), testing selected acyclicity and complement connectivity with union-find, and compares each full coefficient vector with the sixteen-state automaton and cubic recurrence. It additionally compares automaton and recurrence through \(m=12\). The separately written C++17 program `verify/check_wheel.cpp` repeats complete edge-subset enumeration through \(m=9\). Finally `verify/check_symbolic.py`, using SymPy, verifies the exact two-variable determinant identity over the integer polynomial ring. The `verify/outputs.txt` file records actual invocations and their outputs. None of these finite enumerations is substituted for the infinite proof above; symbolic matrix/recurrence identities and planar duality supply the all-order argument.

## Relationship to prior work
Borbényi, Csikvári and Luo (first arXiv posting May 26, 2020) study the individual enumerators of forests and connected spanning subgraphs; the inspected full article does not give their *joint*, cardinality-refined wheel indicator polynomial. The prior published-finding corpus research finding *Wheel spanning-tree exchange centers and complementary-tree census* proves the exact \(2^{m+1}-4\) complementary-tree count and exchange radii, which is explicitly credited here. It does not determine the coefficients of degrees \(0,1,\ldots,m-1\), the cubic/rational formula, or the nonpure shattering complex. The separate *Exact shattering polynomial and a matroid boundary for spanning trees of \(K_{3,n}\)* establishes the general forest/complement-connected criterion and a closed expression for complete bipartite graphs; that expression cannot be specialized to the nonbipartite wheels, and its general lemma alone supplies no wheel enumeration. General matroid basis intersection, planar duality, and ordinary wheel spanning-tree counts are background.

## Limitations
Originality is limited to the mathematical comparisons and full texts inspected; equivalent results under different terminology or in unindexed literature remain possible. The all-order claim concerns only wheels and ordinary labelled spanning trees. The listed five-rim facet census is a finite exact computation, not a claim of a closed all-size facet polynomial. This work does not give a new general graph shattering theorem, a new count of complementary wheel-tree pairs, or an independently audited result.

## References
1. M. Borbényi, P. Csikvári and H. Luo, *On the number of forests and connected spanning subgraphs*, arXiv:2005.12752, first posted 2020-05-26; *Graphs and Combinatorics* **37** (2021), 2655–2678, DOI:10.1007/s00373-021-02382-x. Full open article: https://link.springer.com/article/10.1007/s00373-021-02382-x.
2. *Wheel spanning-tree exchange centers and complementary-tree census*, published published-finding corpus research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-wheel-spanning-tree-exchange-centers-and-complementary-tree-cens--6102930841e3. Exact overlapping top count is credited.
3. *Exact shattering polynomial and a matroid boundary for spanning trees of \(K_{3,n}\)*, published published-finding corpus research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-shattering-polynomial-and-a-matroid-boundary-for-spanning--0c288e04bf53. General shattering lemma credited.
4. Q. Fortier, C. Király, Z. Szigeti and S. Tanigawa, *On packing spanning arborescences with matroid constraint*, *Journal of Graph Theory* **93** (2020), 230–252, first online 2019-08-16, DOI:10.1002/jgt.22484.
