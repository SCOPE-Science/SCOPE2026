# Commuting retractions of finite full transformation semigroups: a rooted-fiber graph and exact triangle enumerator

## Finding

Let \(n\ge5\), let \(T_n\) be the full transformation semigroup on \([n]\), and let \(\mathcal R_n=\{F\in\operatorname{End}_{\mathrm{sgp}}(T_n):F\circ F=F\}\). Endomorphisms are ordinary semigroup endomorphisms, not necessarily identity-preserving. Define \(\Gamma_n\) as the simple graph on \(\mathcal R_n\setminus\{\operatorname{id}_{T_n}\}\), in which distinct vertices are adjacent exactly when the corresponding maps commute under composition.

Write \(\mathcal I_n=\{e\in T_n:e^2=e\}\), and for \(e\in\mathcal I_n\) let \(q(e)\) be the number of odd involutive permutations \(t\in\mathfrak S_n\) satisfying \(te=et=e\). Let \(I_n=|\mathcal I_n|\), \(B_n=\sum_{e\in\mathcal I_n}q(e)\), and \(H_n=|\{e\in\mathcal I_n:q(e)=0\}|\).

**Graph structure.** There is a distinguished vertex \(c\), and for each \(e\in\mathcal I_n\setminus\{\operatorname{id}_{[n]}\}\) there are two vertices \(u_e,v_e\) and \(q(e)\) vertices \(w_{t,e}\). The complete edge list consists exactly of
\[
\{c,v_e\},\quad\{u_e,v_e\},\quad\{c,w_{t,e}\},\quad\{u_e,w_{t,e}\},\quad\{v_e,w_{t,e}\}.
\]
There are no edges between distinct labels \(e\). In particular \(\Gamma_n\) is connected of diameter exactly four, has clique number three, and has \(c\) as a cut vertex. For each \(e\), the page number \(q(e)\) depends only on the sizes of the rooted fibers of \(e\): if its image roots have \(b_1,\ldots,b_r\) *nonroot* elements respectively, then
\[
q(e)=\frac12\left(\prod_{i=1}^r I(b_i)-\prod_{i=1}^r J(b_i)\right),
\quad I(b)=\sum_{j=0}^{\lfloor b/2\rfloor}\frac{b!}{2^j j!(b-2j)!},\quad
J(b)=\sum_{j=0}^{\lfloor b/2\rfloor}\frac{(-1)^j b!}{2^j j!(b-2j)!}.
\]
Moreover \(q(e)=0\) if and only if each fiber has at most two elements. Consequently
\[
I_n=\sum_{r=1}^n\binom nr r^{n-r},\qquad
H_n=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n!}{j!(n-2j)!},
\]
and the exact exponential generating function of the numbers of graph pages is
\[
\boxed{\sum_{n\ge0} B_n\frac{z^n}{n!}
=\frac12\left(\exp\!\bigl(z\exp(z+z^2/2)\bigr)-\exp\!\bigl(z\exp(z-z^2/2)\bigr)\right).}
\]
The graph has exactly \(2I_n-1+B_n\) vertices, \(2(I_n-1)+3B_n\) edges, \(2B_n\) triangles, and \(2B_n+2(H_n-1)\) inclusion-maximal cliques. Every maximal clique is either an edge or a triangle; adjoining the identity endomorphism to a maximal clique gives every maximal family of pairwise commuting retractions of \(T_n\).

For \(n=5\), the values are \(I_5=196\), \(B_5=180\), \(H_5=81\); hence \(\Gamma_5\) has \(571\) vertices, \(930\) edges, \(360\) triangles, and \(520\) maximal cliques.

## Assumptions and scope

All maps in \(T_n\) act on the same labeled set, and multiplication is transformation composition. On the endomorphism monoid we use the convention that \(FG\) applies \(F\) then \(G\); commutation and idempotence are convention-independent. "Odd" means odd sign as a permutation. For each idempotent transformation \(e\), its fibers are rooted at their unique fixed image elements. The theorem concerns \(n\ge5\); the case \(n=4\) has exceptional endomorphisms of rank seven and is deliberately excluded. For the displayed exponential generating series only, the combinatorial quantity \(B_n=\sum_eq(e)\) is also defined for \(0\le n<5\), without asserting the same graph classification there. The vertex set omits only the identity map of the endomorphism monoid, *not* the constant endomorphism with value \(\operatorname{id}_{[n]}\).

## Proof

**1. Exhaustive retraction normal form.** The Schein–Teclezghi classification, in the form of Gould–Grau–Johnson, Theorem 2.1, says that for \(n\ge5\) every nonautomorphic semigroup endomorphism is uniquely
\[
\phi_{t,e}(s)=\begin{cases}
 t,&s\text{ is an odd permutation},\\
 t^2,&s\text{ is an even permutation},\\
 e,&s\text{ is singular},
\end{cases}
\qquad t^3=t,\quad te=et=e^2=e.
\]
The only idempotent automorphism is \(\operatorname{id}_{T_n}\). Directly composing this displayed map with itself shows that every singular retraction is exactly one of the following disjoint forms: \(\phi_{e,e}\) for any \(e\in\mathcal I_n\) (rank one); \(\phi_{1,e}\) for \(e\in\mathcal I_n\setminus\{1\}\) (rank two); or \(\phi_{t,e}\), where \(e\in\mathcal I_n\setminus\{1\}\) and \(t\) is an odd involution with \(te=et=e\) (rank three). Here \(1=\operatorname{id}_{[n]}\) is the unit of \(T_n\). These forms also follow from Lemma 2.8 of Gould–Grau–Johnson. Define \(c=\phi_{1,1}\), \(u_e=\phi_{e,e}\), \(v_e=\phi_{1,e}\), \(w_{t,e}=\phi_{t,e}\).

**2. Compute commutation, including the special constant map.** Evaluate a product \(FG\) on one odd permutation, one even permutation, and one singular transformation; the three values determine it uniquely. Each \(w_{t,e}\) is left-identical on every singular endomorphism; each \(v_e\) acts on a right factor \(\phi_{u,f}\) by replacing \(u\) with \(u^2\); each \(u_e\) acts by replacing the right factor with \(\phi_{f,f}\); and \(c\) acts by replacing it with \(\phi_{u^2,u^2}\). Comparing the reverse products yields: distinct vertices of the same displayed type never commute; \(u_e\) commutes with \(v_f\) or \(w_{t,f}\) exactly when \(e=f\); \(v_e\) commutes with \(w_{t,f}\) exactly when \(e=f\); and \(c\) commutes with every \(v_e\) and \(w_{t,e}\), but with no \(u_e\) for \(e\ne1\). All other pairs fail to commute. This proves the full edge list, not merely a necessary condition. In particular the special vertex \(c\) is essential to the graph description.

**3. Odd involutions in rooted fibers.** The relations \(te=e\) and \(et=e\) say respectively that \(t\) fixes every image root and preserves every fiber of \(e\). Thus \(t\) restricts to an arbitrary involution on each set of \(b_i\) nonroot points, and all such choices occur. The count \(I(b)\) is the number of involutions on \(b\) labeled points; \(J(b)\) is their signed sum by parity. The difference of the total count and signed count, divided by two, counts exactly the odd choices. A transposition of two nonroots exists if and only if some \(b_i\ge2\), proving the zero-page criterion.

**4. Exponential enumeration.** An idempotent transformation is a set of rooted blocks: a block with \(b\) nonroot points has labeled exponential weight \(z^{b+1}/b!\). Decorating each block by an involution on its nonroot points multiplies that weight by \(I(b)\); decorating by its parity-sign sum multiplies by \(J(b)\). The labeled exponential formula gives
\[
\sum_{n\ge0}\left(\sum_{e\in\mathcal I_n}\prod_i I(b_i)\right)\frac{z^n}{n!}
=\exp\!\bigl(z\exp(z+z^2/2)\bigr),
\]
and the signed analogue uses \(z\exp(z-z^2/2)\). Their half-difference yields the asserted \(B_n\) series. Counting rooted blocks whose sizes are one or two gives \(H_n\): choose \(j\) disjoint unordered two-blocks and designate one of their two elements as root, obtaining \(n!/(j!(n-2j)!)\) possibilities. The standard image-root enumeration gives \(I_n\).

**5. Graph invariants.** Each \(e\ne1\) contributes \(u_e,v_e\) and \(q(e)\) page vertices, two spine edges and three edges per page. Every page creates exactly two triangles, one with \(u_e,v_e\), one with \(c,v_e\). Distinct pages are nonadjacent, and \(c\) and \(u_e\) are nonadjacent, so no four-clique exists. If \(q(e)>0\), the two triangles per page are exactly the maximal cliques in the corresponding piece. If \(q(e)=0\), its two spine edges are maximal. Summing proves the counts. Removing \(c\) separates the distinct rooted-fiber pieces. Every vertex is within distance two of \(c\), while \(u_e,u_f\) for distinct \(e,f\) have distance four, proving the diameter claim. The omitted identity endomorphism commutes with all vertices, so adjoining it classifies maximal commuting retraction families.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. It independently enumerates the idempotent transformations and odd involutions in dimensions three through six, checks the rooted-fiber parity formula, and for \(n=5\) constructs the rank-one, rank-two, and rank-three retractions as explicit triples of endomorphism values. It composes every pair of these retractions by evaluating the actual three possible input types, checks the edge list pair-by-pair, and computes vertex and edge counts. The finite tests corroborate the infinite proof; they do not prove all \(n\).

## Relationship to prior work

Schein and Teclezghi (1998) classify the endomorphisms of the full transformation semigroup and count endomorphisms. Gould, Grau, and Johnson (arXiv:2307.11596v1, public July 21, 2023) identify their rank types, multiplication rules, and a chain-of-right-zero-band structure on the idempotents; in particular their Theorem 2.1, Corollary 2.6, Lemma 2.8, and Proposition 3.4 supply the essential structural starting point. That algebraic multiplication information is *strong prior coverage*, and the edge criterion follows from it. The additional result here is the explicit rooted-fiber parity-multiplicity formula, the all-degree exponential enumeration of the graph's triangles and maximal commuting families, and the resulting exact graph parameters. The related published study *A MacMahon correction and an exact minimal-generator formula for endomorphisms of finite transformation monoids* enumerates conjugacy orbits for a distinct minimal-generator invariant, not the labeled commuting-retraction graph. The existing literature on commuting graphs of Rees matrix semigroups concerns a different semigroup, and does not directly provide the rooted-fiber census here.

## Limitations

The result does not concern exceptional \(n=4\), automorphisms other than the identity, or non-idempotent endomorphisms. The graph edge criterion is a direct consequence of the earlier complete multiplication table; the new mathematical content is its explicit arithmetic stratification and all-degree enumerative generating function, not a newly established classification of endomorphisms. Numerical tests stop at \(n=6\), and only \(n=5\) receives direct exhaustive composition checks. A broader earlier enumeration of the same parity-weighted rooted partitions, if found, could reduce originality; no claim of absolute bibliographic priority or independent verification is made.

## References

1. V. Gould, A. Grau, M. Johnson, *The structure of End(\(\mathcal T_n\))*, arXiv:2307.11596v1, July 21, 2023. https://arxiv.org/html/2307.11596
2. B. M. Schein, B. Teclezghi, *Endomorphisms of finite full transformation semigroups*, Proc. Amer. Math. Soc. 126 (1998), 2579–2587. DOI:10.1090/S0002-9939-98-04764-9.
3. *A MacMahon correction and an exact minimal-generator formula for endomorphisms of finite transformation monoids* (2026), published research record.
4. *Commuting graphs of Rees matrix semigroups*, Semigroup Forum (2025), https://doi.org/10.1007/s00233-025-10597-0.
