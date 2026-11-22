# Complete \(F\)-congruence lattices of flat semilattice actions

## Finding
Let \(X\) be a finite set with at least two elements, let a finite group \(G\) act on \(X\), and adjoin a bottom \(0\) and top \(1\) to the flat meet-semilattice on \(X\). Thus distinct elements of \(X\) meet to \(0\). Write \(E_X=\{0,1\}\sqcup X\), and form the inverse monoid \(S=E_X\rtimes G\) using this action.

**Complete classification.** Every congruence of \(S\) preserving the maximum-of-minimum-group-class operation is uniquely
\[
(e,g)\;\rho_{\theta,N}\;(f,h)
\quad\Longleftrightarrow\quad
 e\mathrel\theta f\ \text{and}\ gh^{-1}\in N,
\]
where \(\theta\) is a \(G\)-invariant congruence of the semilattice \(E_X\), \(N\triangleleft G\), and \(N\) acts trivially on \(E_X/\theta\).

For this flat semilattice the eligible \(\theta\)'s are exactly: (a) collapse \(0\) together with an arbitrary union \(U\) of \(G\)-orbits in \(X\), leaving every other point separate; (b) for a globally fixed atom \(a\in X^G\), the two classes \(\{1,a\}\) and \(\{0\}\cup(X\setminus\{a\})\); or (c) the universal relation. Let
\[
K_A=\{g\in G:g\cdot a=a\ \text{for all}\ a\in A\},\qquad
\nu_G(K)=\big|\{N\triangleleft G:N\le K\}\big|.
\]
For \(U\) ranging over unions of orbits, the exact count is
\[
\boxed{\displaystyle
|\operatorname{Con}_F(S)|=
\sum_{U\in\mathcal U(X/G)}\nu_G(K_{X\setminus U})
+(|X^G|+1)\nu_G(G).}
\]
Here \(K_\varnothing=G\), and \(\operatorname{Con}_F\) means the congruence lattice in the enriched \(F\)-inverse signature.

**Faithful transitive rigidity.** If the action is faithful and transitive, every nonidentity \(F\)-congruence collapses the entire set \(\{0\}\cup X\) of semilattice elements into one class. Moreover,
\[
\boxed{\displaystyle
\operatorname{Con}_F(S)\cong
\{\widehat 0\}\sqcup\bigl(\mathcal N(G)\times C_2\bigr),
\qquad |\operatorname{Con}_F(S)|=1+2|\mathcal N(G)|,}
\]
where \(\widehat0\) is an additional least lattice element and \(\mathcal N(G)\) is the normal-subgroup lattice ordered by inclusion. The proper nonidentity quotients are exactly \(G/N\) and \(C_2\times(G/N)\) as inverse monoids, for \(N\triangleleft G\), where \(C_2\) denotes the two-element meet-chain, not the cyclic group in this product.

For the regular action of \(C_m\) on \(m\ge2\) atoms the number is \(1+2\tau(m)\), with \(\tau\) the positive-divisor function. The natural degree-\(m\) action has exactly five such congruences for \(G=A_m\), \(m\ge5\), and seven for \(G=S_m\), \(m\ge5\), independent of the rapidly growing monoid order.

## Assumptions and scope
The semilattice has bottom \(0\), top \(1\), and pairwise-incomparable atoms \(X\). The multiplication in \(S\) is
\[
(e,g)(f,h)=(e\wedge(g\cdot f),gh).
\]
For general \(E_X\) the group action need not be faithful or transitive. The inverse operation is \((e,g)^{-1}=(g^{-1}\cdot e,g^{-1})\). The minimum group congruence \(\sigma\) relates exactly elements having the same group coordinate, and the maximum of the \(\sigma\)-class of \((e,g)\) is \((1,g)\). Hence \(S\) is an \(F\)-inverse monoid.

An \(F\)-congruence is a semigroup congruence \(\rho\) such that \((e,g)\rho(f,h)\) implies \((1,g)\rho(1,h)\). Such a congruence also preserves inversion, as do ordinary inverse-semigroup congruences. The classification concerns all enriched-signature congruences, not the entire, potentially larger, lattice of ordinary semigroup congruences.

## Proof
**1. Separating group and semilattice data.** The projection \((e,g)\mapsto g\) is a surjective homomorphism from \(S\) onto \(G\), while \((e,g)\le(1,g)\) in the natural inverse-monoid order. Thus exactly the elements with fixed group coordinate lie in each minimum group-congruence class, with unique maximum \((1,g)\).

Let \(\rho\) be an \(F\)-congruence. Restricting to the idempotents \((e,1_G)\) gives a semilattice congruence \(\theta\); restricting to the group of units \((1,g)\) gives a normal subgroup \(N\triangleleft G\). Conjugating idempotents by units shows \(\theta\) is \(G\)-invariant. Conjugating the relation \((1,n)\rho(1,1_G)\) for every \(n\in N\) shows \((n\cdot e,1_G)\rho(e,1_G)\), so \(N\) acts trivially on \(E_X/\theta\).

Suppose \((e,g)\rho(f,h)\). Preservation of the maximum operation gives \((1,g)\rho(1,h)\), so \(gh^{-1}\in N\). Right multiplication by \((1,g^{-1})\) gives \((e,1_G)\rho(f,hg^{-1})\), while \((1,hg^{-1})\rho(1,1_G)\) implies \((f,hg^{-1})\rho(f,1_G)\). Hence \(e\mathrel\theta f\). Conversely, if \(e\mathrel\theta f\) and \(gh^{-1}\in N\), then \((e,1_G)\rho(f,1_G)\) and \((1,g)\rho(1,h)\); multiplying gives \((e,g)\rho(f,h)\). The pair \((\theta,N)\) is therefore unique.

Conversely, for a \(G\)-invariant semilattice congruence \(\theta\) and \(N\triangleleft G\) acting trivially on \(E_X/\theta\), the action descends to \(G/N\) on \(E_X/\theta\). The map
\[
(e,g)\longmapsto([e]_\theta,gN)
\]
is an onto homomorphism of inverse monoids from \(S\) to \((E_X/\theta)\rtimes(G/N)\), and it preserves the maximum operation. Its kernel is precisely the displayed relation \(\rho_{\theta,N}\). This completes the general splitting classification and identifies its quotient monoids.

**2. Flat-semilattice congruences.** If a semilattice congruence identifies distinct atoms \(a\) and \(b\), then intersecting the equality with \(a\) yields \(a\sim0\), and similarly \(b\sim0\). Thus, unless the top is identified with something, the only possible nontrivial class consists of \(0\) and an arbitrary subset \(U\subseteq X\), with all remaining atoms and the top singleton. If \(1\sim a\) for some atom, intersecting with any other atom \(b\) forces \(b\sim0\); either \(a\not\sim0\) and the quotient has exactly the two classes stated in the finding, or the relation is universal. If \(1\sim0\), the relation is universal. Every listed partition indeed respects meet, proving exhaustiveness.

The \(G\)-invariant partitions of the first kind are exactly those with \(U\) a union of orbits. The partition with \(1\sim a\) is invariant exactly when \(a\) is fixed by the whole group. Every such two-class quotient has trivial induced group action; so does the universal quotient. For the first kind, the noncollapsed atoms \(X\setminus U\) are distinct in the quotient. Thus \(N\) acts trivially on it exactly when \(N\le K_{X\setminus U}\). Counting the admissible normal subgroups separately in these disjoint cases gives the stated exact sum.

**3. Faithful transitive consequence and lattice order.** Faithful transitivity with \(|X|\ge2\) leaves exactly two invariant subsets \(U\), namely \(\varnothing\) and \(X\), and no globally fixed atom. In the empty-\(U\) case, admissible normal subgroups lie in the kernel of the faithful action and hence consist only of \(\{1_G\}\). That produces the identity congruence. In the full-\(U\) case and in the universal semilattice case, every normal subgroup is admissible. These are two layers, ordered coordinatewise by normal-subgroup inclusion and semilattice-congruence inclusion, both strictly above the identity. This proves the lattice isomorphism, the formula \(1+2|\mathcal N(G)|\), and the description of all proper quotients. The normal-subgroup counts of cyclic, alternating, and symmetric groups give the examples.

## Verification
The included standalone Python program `verify.py` uses the exact multiplication table and the maximum operation. It builds every \(F\)-congruence by closing each candidate element identification under multiplication on both sides and the maximum operation, then traverses the finite lattice of all generated congruences. Thus its enumeration does not use the theorem's partition formulas to generate candidate congruences. It independently compares the resulting complete lattice with the formula-derived partitions.

The following exact cases were executed and passed: regular cyclic actions \(C_2\), \(C_3\), and \(C_4\), giving respectively \(5,5,7\) \(F\)-congruences on monoids of orders \(8,15,24\); a nontransitive \(C_2\)-action swapping two atoms and fixing a third, giving \(10\) \(F\)-congruences on an order-\(10\) monoid; and the faithful nonabelian degree-three \(S_3\)-action, giving \(7\) \(F\)-congruences on an order-\(30\) monoid. An independent scan of all \(4{,}140\) partitions of the order-eight example found exactly seven ordinary congruences and five \(F\)-congruences.

Run `python3 verify.py` from the directory containing this document. All computations are finite consistency checks; the unbounded group-action theorem is established by the proof, not inferred from these examples.

## Relationship to prior work
Lemut Furlani (first publicly posted 15 August 2026) introduces \(F\)-congruences and proves general characterizations through kernel normal systems and congruence pairs (Theorems 3.7 and 3.10). Its Examples 4.5 and 4.7 analyze an order-eight semidirect product with two atoms switched by \(C_2\), showing in particular that its greatest idempotent-separating \(F\)-congruence is trivial. The classification here specializes the general setting to an arbitrary finite permutation action on a flat semilattice, determining the entire lattice, all quotients, and a new orbit/kernel counting formula, including that example. The present finding does not claim a new definition or characterization of \(F\)-congruences in general.

The literature on semidirect products of semilattices by groups (for example, Silva--Soares) supplies structural context but not the displayed exact \(F\)-congruence lattice. The separate literature on congruence identities of semilattices, including Martin-Maroto--Ricciardo--de Polavieja, does not compute these action-constrained quotients. Historical implicit consequences of broader congruence theories remain a possible priority issue.

## Limitations
The explicit orbit-sum census requires finite \(X\) and \(G\) and at least two atoms. The general splitting argument works for any semilattice with top acted on by a group, but beyond the flat case it does not itself enumerate all invariant semilattice congruences. Ordinary congruences that fail preservation of the maximum operation are not classified. The result is a mathematical derivation supported by finite reproducibility checks, not an independently audited proof or a claim about all prior historical literature.

## References
- A. Lemut Furlani, *\(F\)-congruences on \(F\)-inverse monoids*, arXiv:2608.15114, first version 15 August 2026; https://arxiv.org/abs/2608.15114.
- P. V. Silva and F. Soares, *Howson's property for semidirect products of semilattices by groups*, arXiv:1412.3048 (2014); https://arxiv.org/abs/1412.3048.
- F. Martin-Maroto, A. Ricciardo, and G. de Polavieja, *The pairwise distributive law of semilattice congruences*, *Algebra universalis* 87 (2026), article 29; https://doi.org/10.1007/s00012-026-00942-x.
