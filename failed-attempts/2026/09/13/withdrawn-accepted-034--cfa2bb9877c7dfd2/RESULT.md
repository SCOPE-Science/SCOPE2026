# Morita non-equivalence of the classifying toposes of dense linear orders without endpoints and atomless Boolean algebras

## Context

Two geometric theories are Morita-equivalent when they have the same Grothendieck classifying topos up to equivalence, equivalently when they have naturally equivalent categories of models in every Grothendieck topos. The admitted target asks this for a fixed motivated pair: the coherent theory of dense linear orders without endpoints (DLO) and the coherent theory of atomless Boolean algebras (ABA). Both are classical complete uncountably-categorical-adjacent theories and standard examples in the topos-theoretic bridge literature, so deciding their Morita equivalence is a recognized classification question.

## Definitions

Let T_DLO be the single-sorted coherent theory in the language {<} with axioms: irreflexivity, transitivity, linearity/trichotomy (x<y or x=y or y<x), density (x<y implies exists z with x<z and z<y), and unboundedness above and below. Homomorphisms are maps preserving < forward.

Let T_ABA be the single-sorted coherent theory in the algebraic signature {0,1,meet,join,neg} with the Boolean algebra axioms, 0 != 1, and the atomless axiom: every nonzero x strictly exceeds some nonzero y. Homomorphisms are Boolean homomorphisms.

Let E_DLO and E_ABA be their Grothendieck classifying toposes, presented by coherent syntactic sites, with natural numbers objects. Write pt(E) = Hom(Set,E) for the Set-point category, with general geometric transformations as morphisms. By the classifying universal property, pt(E_T) is equivalent to T-mod(Set), models in Set with homomorphisms.

## Result

Theorem: E_DLO and E_ABA are not equivalent as categories, hence not equivalent as Grothendieck toposes over Set. In particular T_DLO and T_ABA are not Morita-equivalent.

The separating invariant of point categories is (P): every morphism is monic.

## Proof / evidence

Lemma 1 (DLO side): every morphism of pt(E_DLO) is monic. If f:M->N preserves < and x!=y, trichotomy gives x<y or y<x, so f(x)<f(y) or f(y)<f(x); irreflexivity in N gives f(x)!=f(y). Hence f is injective as a function. The forgetful functor U:pt(E_DLO)->Set is identity on morphisms hence faithful, and a faithful functor reflects monics from injective underlying maps: U(f) monic in Set implies f monic.

Lemma 2 (ABA side): pt(E_ABA) contains a non-monic morphism. Let B=P(N)/fin, subsets of N modulo finite symmetric difference, with 0=[empty], 1=[N]. If [A]!=0 then A is infinite; enumerating A increasingly and splitting into even- and odd-indexed parts yields two disjoint infinite subsets, so B is atomless and 0!=1. Finite products of nontrivial atomless algebras are atomless: for x=(x1,x2)!=(0,0), some xi!=0, say x1, pick 0<y1<x1, then 0!=(y1,0)<(x1,x2). Hence C=BxB is atomless. The first projection pi1:C->B and diagonal s:B->C, s(a)=(a,a), are Boolean homomorphisms with pi1 o s = id, so pi1 is a split epimorphism. It is not an isomorphism since u=(1,0)!=(1,1)=v have pi1(u)=pi1(v), so U(pi1) is not bijective and functors preserve isomorphisms. A monic split epi is an iso, so pi1 is not monic; explicitly with g1=(pi1,pi1) and g2=id_C, pi1 o g1 = pi1 o g2 while g1!=g2.

Lemma 3 (transfer): (P) is preserved under equivalence of categories. Fully faithful functors preserve monomorphisms; if F:C<->D:G is an equivalence and every morphism of C is monic, then for h' in D, G(h') is monic, F(G(h')) is monic, and h' is iso-conjugate to F(G(h')), hence monic.

Conclusion: pt(E_DLO) satisfies (P) while pt(E_ABA) does not, so the point categories are inequivalent. If E_DLO and E_ABA were equivalent toposes, postcomposition would give an equivalence of point categories, a contradiction. A fortiori there is no equivalence over Set.

## Limitations

The argument separates the toposes via Set-points under the standard readings of the theories and the usual coherent classifying-topos universal property. It does not compute finer invariants such as subtopos lattices or De Morgan skeleta, and does not address non-Grothendieck or non-classifying readings of the syntactic sites. The inequality symbol in the coherent ABA axiomatization is read classically; the robustness remark in the draft shows the same witnesses work for the purely equational nontrivial-Boolean-algebra fragment.

## Reproducibility

All steps are self-contained deduction: verify Lemma 1 from trichotomy and irreflexivity, verify B atomless by the even/odd split of an infinite subset of N, verify BxB atomless by the coordinate argument, check pi1 and s are Boolean homomorphisms with pi1 o s = id and pi1(1,0)=pi1(1,1), and apply the monic-split-epi-is-iso fact plus the fully-faithful preservation lemma. No computation or external data is required.

## References

P. T. Johnstone, Sketches of an Elephant, sections D3.1-D3.2 (classifying toposes and syntactic sites); O. Caramello, Theories, Sites, Toposes (Morita equivalence, bridges, presheaf-type and atomic characterizations); nLab, classifying topos (universal property and syntactic-site construction); P. T. Johnstone, A topos-theorist looks at dilators, J. Pure Appl. Algebra (1989) (E_DLO as atomic topos); Caramello technical exposition on unifying theory (Morita equivalence criteria and atomic-quotient examples).
