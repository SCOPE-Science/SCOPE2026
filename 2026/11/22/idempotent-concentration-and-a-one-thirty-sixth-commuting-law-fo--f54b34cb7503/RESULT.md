# Idempotent concentration and a one-thirty-sixth commuting law for chain partial isometries

## Finding

For each integer \(n\ge2\), write \(\mathcal D_n\) for the inverse monoid of every distance-preserving partial injection on the standard metric chain \([n]\). For two independent uniform elements \(U_n,V_n\), the commuting probability satisfies

\[\boxed{\Pr(U_nV_n=V_nU_n)=\frac{1}{36}+O(0.99^n).}\]

More precisely, if \(E_n\) denotes the set of idempotents and \(C_n\) the number of ordered commuting pairs, then
\[|E_n|=2^n,\quad |\mathcal D_n|=6\cdot2^n-n^2-4n-5,\quad C_n=4^n+O\left(|\mathcal D_n|^2\left(n2^{-n/4}+(7/8)^{n/6}\right)\right).\]
Here the error counts commuting pairs with at least one non-idempotent factor, and its implied constant is absolute. Consequently,
\[\Pr(U_n\in E_n,\ V_n\in E_n\mid U_nV_n=V_nU_n)\longrightarrow1.\]

## Assumptions and scope

Every map is a partial injective function \(a:A\to[n]\), where \(A\subseteq[n]\) may be empty, with \(|a(x)-a(y)|=|x-y|\) for all \(x,y\in A\). The monoid product is composition of partial functions, and equality includes equality of their domains. An idempotent is exactly the identity on some subset of \([n]\). All asymptotics are for integer \(n\to\infty\); the limit concerns two independently and uniformly chosen whole-monoid elements, not a rank-conditioned sample or the submonoid with interval domains.

## Proof

**1. Affine representatives and exact size.** For domain size at least two, a distance-preserving map has a unique ambient affine representative \(g(x)=\epsilon x+c\) with \(\epsilon\in\{-1,1}\}\) and integer \(c\). Its admissible support \(S_g=\{x\in[n]:g(x)\in[n]\}\) is an interval. For each fixed sign, exactly one affine representative has support size \(n\), and exactly two have each support size \(1,\ldots,n-1\). The number of restrictions of a representative with support size \(\ell\) and domain size at least two is \(2^\ell-\ell-1\). This does not double-count since two domain points determine the ambient affine representative uniquely. Adding the \(n^2\) singleton maps and the empty map gives
\[|\mathcal D_n|=1+n^2+2(2^n-n-1)+4\sum_{\ell=1}^{n-1}(2^\ell-\ell-1)=6\cdot2^n-n^2-4n-5.\]
All \(2^n\) partial identities commute pairwise and are the only idempotents, hence exactly \(4^n\) ordered commuting pairs have both factors idempotent.

**2. Exponentially rare small representatives.** Call a restriction *short* when it has domain size at most one, or its unique affine representative has support size below \(3n/4\). There are at most \(4n-2\) ambient affine representatives, and each contributes at most \(2^{3n/4}\) restrictions. Thus the total number of short elements is bounded by
\[L_n\le n^2+1+4n2^{3n/4}.\]
As \(|\mathcal D_n|\ge2^n\), the probability that either of two uniform elements is short is \(O(n2^{-n/4})\).

**3. A disjoint family of local obstructions.** Fix two affine representatives \(f,g\), both with support sizes at least \(3n/4\), and suppose at least one is not the full identity. Relabel the two maps so that \(g\) is not the identity. Put
\[T=\{x\in S_g:g(x)\in S_f,\ g(x)\ne x\}.\]
Because \(g(S_g)\) and \(S_f\) are both subsets of \([n]\) with cardinalities at least \(3n/4\), their intersection has size at least \(n/2\). A nonidentity isometry of an integer line has at most one fixed point, so \(|T|\ge n/2-1\).

If \(g(x)=x+c\) is a nontrivial translation, the edges \(x\to g(x)\), \(x\in T\), have distinct underlying unoriented edges and form paths of maximum degree two; greedily selecting an edge and discarding its at most two neighboring edges gives at least \(|T|/3\) vertex-disjoint edges. If \(g(x)=c-x\) is a reflection, its nonfixed orbits are disjoint two-cycles, and each orbit contributes at most two directed edges to \(T\); choosing one per represented orbit gives at least \(|T|/2\) disjoint edges. Thus in both cases we obtain initial vertices \(J\) of at least \(|T|/3\) edges with pairwise disjoint endpoint sets.

Independently select uniform random subsets \(A\subseteq S_f\) and \(B\subseteq S_g\), and consider restrictions \(f|_A\) and \(g|_B\). For each \(x\in J\), the event
\[x\in B,\quad g(x)\in A,\quad x\notin A\]
forces \(f|_A\circ g|_B\) to be defined at \(x\), but \(g|_B\circ f|_A\) to be undefined there. If \(x\notin S_f\), the last condition is automatic; otherwise its probability is \(1/2\). Since \(g(x)\ne x\) and these selected edges are vertex-disjoint, the witness events are independent, and each has probability at least \(1/8\). Hence the probability of commuting under independent unrestricted Bernoulli subset sampling is at most
\[(7/8)^{|J|}\le(7/8)^{(n/2-1)/3}.\]
For \(n\ge8\), every support considered here has at least three points. Uniform restrictions with domain size at least two are obtained by conditioning on a Bernoulli subset of cardinality at least two, an event of probability \(1-(\ell+1)/2^\ell\ge1/2\). Conditioning the two selections therefore increases the upper bound by a factor at most four. The same conclusion holds when one of the two representatives is the identity, since the other is chosen as \(g\).

**4. Summation over types.** A commuting pair with at least one non-idempotent factor is either short in at least one coordinate, or has two long representatives of which at least one is nonidentity. The estimates above, uniform in the representatives, show
\[0\le\frac{C_n-4^n}{|\mathcal D_n|^2}\le\frac{2L_n}{|\mathcal D_n|}+4(7/8)^{(n/2-1)/3}\qquad(n\ge8).\]
The right side is \(O(n2^{-n/4}+(7/8)^{n/6})\). Finally,
\[\frac{4^n}{|\mathcal D_n|^2}=\frac1{36}+O(n^2 2^{-n}),\]
so the probability tends to \(1/36\), with exponential error \(O(0.99^n)\). Dividing the rare non-idempotent commuting-pair probability by the commuting probability, which has a positive limit, gives the conditional assertion. All claims hold for arbitrary integer \(n\ge2\), with the quantitative inequality explicitly proved for \(n\ge8\).

## Verification

The standalone Python program `verify_commuting.py` enumerates all partial isometries via singleton maps and unique rank-at-least-two affine restrictions, computes every ordered pair of compositions, and compares the result to the exact size and idempotent formulas for \(2\le n\le7\). The exact commuting totals are \(31,204,1089,5104,21021,81210\) for \(n=2,3,4,5,6,7\). The program checks the non-idempotent difference from \(4^n\). These finite tests corroborate but do not replace the infinite proof; the disjoint-edge argument establishes the asymptotic theorem.

## Relationship to prior work

Kehinde and Umar, *On the Semigroup of Partial Isometries of a Finite Chain* (arXiv:1101.0049, originally public 2010-12-30), already provide the chain monoid, its cardinality \(|\mathcal D_n|\), ranks, and fixed-point enumeration; **none of these is claimed as new here**. Namnak, Laysirikul and Sawatraksa, *Natural Partial Order on the Semigroups of Partial Isometries of a Finite Chain* (online 2023-05-16), give the natural order and maximal/minimal elements; the full available PDF was checked and does not address commuting probability. Results on the more restrictive interval-domain partial-translation rook monoid concern a different algebra and have limiting commuting probability \(3/10\); they do not imply the full partial-isometry \(1/36\) law. A recent rank-of-product distribution for order-preserving chain partial translations does not determine whether two products are **equal** in both orders. The finding here is asymptotic concentration of *commuting pairs* on two idempotents.

## Limitations

This result does not give an exact formula for \(C_n\), its optimal convergence exponent, or higher-arity commuting tuples. It is an analytic infinite proof with small-degree computational checks. Published-source search cannot certify global priority; in particular, an unindexed older result about commuting probabilities of partial transformations might cover this claim. The web date attached to the motivating Thai Journal article is 2023-05-16; the PDF bears 2018 copyright, so the precise earliest availability before the indexed posting is uncertain, although both dates fall within the same middle-year category.

## References

1. R. Kehinde and A. Umar, *On the Semigroup of Partial Isometries of a Finite Chain*, arXiv:1101.0049v1 (2010-12-30), accessible full text: https://www.academia.edu/50883282/On_the_Semigroup_of_Partial_Isometries_of_a_Finite_Chain.
2. C. Namnak, E. Laysirikul, N. Sawatraksa, *Natural Partial Order on the Semigroups of Partial Isometries of a Finite Chain*, Thai Journal of Mathematics, 97–108, online publication listed 2023-05-16: https://thaijmath.com/index.php/thaijmath/article/view/760 ; full PDF: https://thaijmath.com/index.php/thaijmath/article/download/760/757/781.
3. F. Al-Kharousi, R. Kehinde, A. Umar, *Combinatorial results for certain semigroups of partial isometries of a finite chain* (2014), https://www.researchgate.net/publication/261708216_Combinatorial_results_for_certain_semigroups_of_partial_isometries_of_a_finite_chain.
