# Secure-guard spectra and exact relocation distances on the Pappus incidence graph

## Finding

Let \(H\) be the **18-vertex Pappus incidence graph** specified below. Its complete secure-domination cardinality polynomial is

\[
\begin{aligned}
D_{\mathrm{sec}}(H;z)={}&1755z^{8}+13088z^{9}+24624z^{10}+24948z^{11}\\
&+16899z^{12}+8316z^{13}+3042z^{14}+816z^{15}\\
&+153z^{16}+18z^{17}+z^{18}.
\end{aligned}
\]

Thus exactly \(93660\) labelled subsets are secure dominating, and \(\gamma_s(H)=8\). The generating polynomial for **inclusion-minimal** secure dominating sets is
\[
M_{\mathrm{sec}}(H;z)=1755z^{8}+3224z^{9}.
\]
Every optimum is inclusion-minimal, but the graph also has \(3224\) inclusion-minimal nine-vertex configurations.

Form reconfiguration graphs whose vertices are the \(1755\) minimum secure dominating sets, with an edge when one selected vertex is replaced by one unselected vertex and the new set remains secure. The **token-jump graph** permits any replacement; the **token-slide graph** requires the old and new vertices to be adjacent in \(H\). Both graphs are connected. The jump graph has \(12798\) edges, radius and diameter \(8\), with every configuration of eccentricity \(8\). The slide graph has \(4320\) edges, radius \(9\), diameter \(10\), with \(1539\) configurations of eccentricity \(9\) and \(216\) of eccentricity \(10\). The full 216-element automorphism group of \(H\) has thirteen orbits on optimum configurations: one of size \(27\), eight of size \(108\), and four of size \(216\).

## Assumptions and scope

All graphs are finite and simple, and all vertex subsets are labelled; no quotient by graph symmetry is taken in the polynomials. Work over \(\mathbb F_3=\{0,1,2\}\). Label nine point-vertices \(P(x,y)\) and nine line-vertices \(L(m,b)\). The only edges are
\[
P(x,y)L(m,b)\quad\Longleftrightarrow\quad y=mx+b\pmod3.
\]
This is the Pappus configuration viewed as the affine plane of order three with the vertical parallel class removed [3].

Write \(N[v]\) for a closed neighborhood. A set \(S\subseteq V(H)\) is dominating if \(\bigcup_{s\in S}N[s]=V(H)\). It is *secure dominating* if it is dominating and, for each \(u\notin S\), some adjacent \(v\in S\) satisfies \((S\setminus\{v\})\cup\{u\}\) dominating. Inclusion-minimal means no proper subset is secure dominating; minimum means smallest possible cardinality. Token-jump and token-slide moves are always between distinct **minimum secure dominating sets**; intermediate states must remain minimum and secure. Graph distance, eccentricity, radius and diameter have their usual shortest-path meanings.

## Proof

The result is an exact finite enumeration with explicit exhaustive algorithms, rather than an all-orders symbolic formula. The following equivalence is the critical correctness lemma. For a selected vertex \(v\in S\), define its *private closed neighborhood relative to* \(S\) by
\[
\operatorname{priv}_S(v)=\{w\in V(H):N[w]\cap S=\{v\}\}.
\]
For \(u\notin S\) adjacent to \(v\), the swapped set \((S\setminus\{v\})\cup\{u\}\) dominates if and only if \(\operatorname{priv}_S(v)\subseteq N[u]\). Indeed, the only vertices that can lose their last selected closed neighbor when \(v\) is removed are precisely those private to \(v\), and adding \(u\) covers precisely \(N[u]\). This gives a finite neighborhood test for security; the accompanying independent checker directly tests domination after every candidate swap without using the private-neighborhood lemma.

For reproducibility, identify \(P(x,y)\) with bit \(3x+y\), and \(L(m,b)\) with bit \(9+3m+b\). Consequently the vertex domain is **exactly** the integers \(s\) from \(0\) through \(2^{18}-1\). Let \(C_v\) be the 18-bit mask of \(N[v]\). Define the domination mask \(c(0)=0\) and, for nonzero \(s\),
\[
c(s)=c(s\mathbin{\mathrm{xor}}\ell)\mathbin{\mathrm{or}} C_v,
\]
where \(\ell\) is the least set bit of \(s\) and \(v\) is its position. This recurrence computes \(\bigcup_{v\in S}N[v]\) by induction on the number of bits. The security test first requires \(c(s)=2^{18}-1\). Then, for each unset bit \(u\), it tests each selected neighbor \(v\) and accepts \(u\) if the mask of \((S\setminus\{v\})\cup\{u\}\) dominates. The set is secure if and only if **every** unset bit passes. The exhaustive loop visits each of the \(262144\) masks once. Grouping accepted masks by population count gives every coefficient of \(D_{\mathrm{sec}}\).

Secure domination is upward closed: a secure set remains secure after adding selected vertices. Hence a secure set is inclusion-minimal exactly when deletion of **every single** selected vertex breaks security. Applying this precise test to every accepted mask yields the coefficients of \(M_{\mathrm{sec}}\), and proves the claimed minimum and its multiplicity. No untested set or size is omitted.

For the two reconfiguration graphs, list every accepted mask with exactly eight set bits. For each such \(s\), enumerate every ordered selected/unselected pair \((u,v)\), construct the switched mask, and insert the corresponding edge if that mask appears in the optimum list; for slides also require \(uv\in E(H)\). The code checks undirected adjacency and counts each edge once. Breadth-first search from **each of the 1755 vertices** computes its complete distance row; all searches reach every vertex. The edge counts, eccentricities, radii and diameters stated above are the exact outputs of these exhaustive bounded searches.

For the symmetry orbit count, the affine transformations
\[
(x,y)\longmapsto(ax+b,cx+dy+e),
\quad a,d\in\mathbb F_3^\times,\quad b,c,e\in\mathbb F_3
\]
induce \(108\) distinct point-and-line automorphisms. Composing them with the incidence duality \(P(x,y)\leftrightarrow L(x,-y)\) gives \(108\) further automorphisms; all \(216\) permutations are checked to preserve every edge. The known full automorphism group has order \(216\) [4], so this list is exhaustive. Their images of each optimum set are explicitly collected into orbits, yielding the thirteen sizes given above.

## Verification

Run `python3 verify.py` with the Python standard library. It enumerates all masks, checks domination and secure swaps, constructs the exact jump and slide graphs, runs all-source breadth-first search, and enumerates the \(216\) explicit automorphisms and their optimum orbits; success prints `PAPPUS_SECURE_VERIFY_OK`. The independently formulated `independent_check.cpp` computes domination directly from the graph neighborhoods for every proposed swap, rather than using the cached domination-mask recurrence. Compile and run it using `c++ -std=c++17 -O2 independent_check.cpp -o check && ./check`; success prints `INDEPENDENT_DIRECT_SWAP_OK`. Both programs have been run from their actual supplied paths and passed. Their hardcoded expected counts are assertions against a complete, independently regenerated search, not input data defining the feasible sets.

## Relationship to prior work

Haythorpe and Newcombe [1] analyze secure domination in products involving paths and cycles and provide the guard-replacement definition, but do not address the Pappus incidence graph. Křišťan and Svoboda [2] study shortest **ordinary dominating-set** token slides, chiefly on trees and interval graphs, without the secure guard condition or this graph. The Pappus affine incidence construction is classical [3]; the 216-element automorphism order is known [4]. Related previously indexed classifications of secure domination on the Heawood and Möbius–Kantor graphs concern different incidence graphs; an indexed Pappus classification of *semitotal* and *locating-total* domination concerns different predicates, not consequences of this secure-domination census. No exact Pappus secure-polynomial or minimum guard-relocation classification was located in the targeted comparisons. The absence of a retrieved covering result is not a proof of absolute publication priority.

## Limitations

The theorem is specific to the labelled 18-vertex **Levi graph**, not the different nine-vertex point-collinearity graph sometimes also called the Pappus graph. Its proof is exhaustive, exact and finite, using executable code; it is not an infinite-family statement. Move edges are possible optimum-preserving relocations, not necessarily moves of a *designated defender* responding to the currently attacked vertex. The integer outputs require replay of the finite enumeration for independently checkable assurance. Independent external mathematical review and exhaustive publication-priority clearance have not been performed.

## References

1. M. Haythorpe and A. Newcombe, *The Secure Domination Number of Cartesian Products of Small Graphs with Paths and Cycles*, arXiv:2103.01406, first public 2021-03-02, https://arxiv.org/abs/2103.01406.
2. J. M. Křišťan and J. Svoboda, *Shortest Dominating Set Reconfiguration under Token Sliding*, arXiv:2307.10847, first public 2023-07-20, https://arxiv.org/abs/2307.10847.
3. K. Stokes, *Irreducibility of configurations*, Ars Mathematica Contemporanea 10 (2016), 169–181, first online 2015-09-11, §4.2 (affine-line construction of Pappus), https://dlib.si/stream/URN%3ANBN%3ASI%3ADOC-OCBGMHAN/db7b0708-b365-4c1d-ad1e-eb6bd0f88a7b/PDF.
4. *Pappus graph*, standard graph reference recording its 216 automorphisms, https://en.wikipedia.org/wiki/Pappus_graph.
