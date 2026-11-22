# Affine-retraction compatibility over odd generalized dihedral groups and recovery of hidden exponents

## Finding

Let \(A\) be a nontrivial finite abelian group of odd order and let \(G=\operatorname{Dih}(A)=A\rtimes C_2\), where the nonidentity element \(s\) of \(C_2\) acts on \(A\) by inversion. A *retraction* means a group endomorphism \(F:G\to G\) with \(F^2=F\). Two retractions are *compatible* when they commute under composition; the notion is unrelated to commuting group elements.

Every retraction except the trivial group homomorphism is uniquely
\[
 F_{P,u}(a)=P(a),\qquad F_{P,u}(s)=us,
 \qquad P^2=P\in\operatorname{End}(A),\quad u\in\ker P.
\]
The maps compose by \(F_{P,u}F_{Q,v}=F_{PQ,u+P(v)}\) (this product is meaningful for the full homomorphism monoid as well as the idempotents). Thus their compatibility relation is exactly the compatibility of idempotent affine transformations of the underlying additive group of \(A\).

Write the elementary-divisor decomposition
\[
 A=\bigoplus_{p\ \mathrm{odd}}\bigoplus_{a\ge1}
 (C_{p^a})^{m_{p,a}},\qquad r=\sum_{p,a}m_{p,a}.
\]
For a finite abelian group with the indicated type, define
\[
 \mathcal U(\mathbf m)=\prod_p p^{\sum_{a,b}m_{p,a}m_{p,b}\min(a,b)}
 \prod_a\prod_{i=1}^{m_{p,a}}(1-p^{-i}),\qquad \mathcal U(\mathbf0)=1.
\]
This is its automorphism-group order. For a fixed tuple length \(t\ge0\), let \(W=\{0,1\}^t\), let \(\mathbf1\) denote its all-one word, and take all collections of nonnegative multiplicities \(m_{p,a,w}\) with \(\sum_{w\in W}m_{p,a,w}=m_{p,a}\). Let \(A_w\) denote the abstract abelian group of that allocated type. **The exact number of ordered, pairwise-compatible \(t\)-tuples of nontrivial group retractions**, allowing repeated entries, is
\[
 \boxed{C_t(A)=\sum_{(m_{p,a,w})}
 \frac{\mathcal U(\mathbf m)}{\prod_{w\in W}\mathcal U(\mathbf m^{(w)})}
 \frac{|A|}{|A_{\mathbf1}|}.}
\]
The quotient of automorphism orders is a positive integer. With the trivial group homomorphism permitted in each position, the corresponding count is
\[
 \boxed{\widehat C_t(A)=\sum_{j=0}^t\binom tj C_j(A).}
\]
The complete clique polynomial of the full retraction-commuting graph is consequently explicit by signed-Stirling inversion:
\[
 c_k(A)=\frac1{k!}\sum_{j=0}^k s(k,j)\widehat C_j(A),
\]
where \(s(k,j)\) is a signed Stirling number of the first kind, and \(c_0=1\). All inclusion-maximal cliques have \(2^r+1\) vertices and their exact number is
\[
 \boxed{|A|\,\mathcal U(\mathbf m)\bigg/\prod_{p,a}
 m_{p,a}!\,(p^a-p^{a-1})^{m_{p,a}}.}
\]

**Mixed-exponent and invisible-exponent contrast.** For a fixed odd prime \(p\) and \(1\le a<b\), put \(A=C_{p^a}\oplus C_{p^b}\) and \(Q=2^t\). Then
\[
 \boxed{C_t(A)=1+(Q-1)p^{a+b}
 +p^{2a}(Q-1)\bigl((Q-2)p^{a+b}+p^a+p^b\bigr).}
\]
For every fixed \(t\ge1\), this is strictly increasing in \(b\), whereas the number of ordered pairwise-commuting idempotent *additive-group endomorphisms* of \(A\) is independent of \(b\) for all \(b>a\). Hence adjoining the inversion involution restores detection of the uniquely largest cyclic exponent by the whole family of compatibility counts, already by \(C_1\). For \(A=C_3\oplus C_9\), the values \((C_0,C_1,C_2,C_3)\) are \((1,136,1864,11152)\); the full group has \(137\) retractions and \(2137\) ordered commuting pairs. There are exactly \(243\) maximal compatible families, each containing five retractions.

## Assumptions and scope

The underlying group \(A\) is nontrivial, finite, abelian and of odd order; it need not be elementary abelian or a \(p\)-group. A product of endomorphisms denotes functional composition, left factor applied last. The trivial group homomorphism maps all of \(G\) to its identity; it must not be confused with any \(F_{0,u}\), which maps \(s\) to a reflection and has image of order two. The integer \(r\) counts the indecomposable cyclic prime-power direct summands, including those from different primes. Tuple entries may repeat. The clique graph includes the trivial homomorphism and identity; cliques consist of distinct retractions. All displayed sums are finite.

## Proof

**Step 1: classification.** All odd-order elements of \(G\) lie in \(A\), so a group homomorphism restricts to a unique additive endomorphism \(P\) on \(A\). Since \(s^2=1\), the image of \(s\) is either \(1\) or an element \(us\) of order two. If its image is \(1\), the relation \(sas^{-1}=-a\) forces \(P(a)=-P(a)\), hence \(P=0\) because \(A\) has odd order. Otherwise every pair \((P,u)\) defines a homomorphism (the inversion relation is respected automatically). For such pairs, direct calculation yields
\[
 F_{P,u}F_{Q,v}=F_{PQ,u+P(v)}.
\]
Consequently its square equals itself precisely when \(P^2=P\) and \(P(u)=0\). This establishes the claimed bijection, not merely a restriction to a convenient subclass.

**Step 2: common-fixed-point lemma.** To \(F_{P,u}\) attach the affine idempotent \(f(x)=P(x)+u\) of \(A\). The correspondence preserves composition. For any pairwise-commuting family \(f_1,\ldots,f_t\), their product \(e=f_1\cdots f_t\) is an idempotent, and its image is the nonempty common fixed-point set of all the \(f_i\): every point of \(\operatorname{im}e\) is fixed by all \(f_i\), while every common fixed point is fixed by \(e\). Choose \(x\) in this intersection. The translation parts then satisfy \(u_i=(1-P_i)x\). Conversely any \(x\in A\) and commuting additive projections \(P_i\) produce commuting affine projections by this rule. Two choices \(x,x'\) produce the same translations for all \(i\) exactly when \(x-x'\) belongs to \(\bigcap_i\operatorname{im}P_i\), because \(\ker(1-P_i)=\operatorname{im}P_i\). Thus the number of distinct compatible translation tuples over a fixed commuting linear-projection tuple is \(|A|/|\bigcap_i\operatorname{im}P_i|\).

**Step 3: joint Boolean splitting and enumeration.** The familiar simultaneous-idempotent identity
\[
 E_w=\prod_{i=1}^t\left(w_iP_i+(1-w_i)(1-P_i)\right),\qquad w\in\{0,1\}^t,
\]
provides mutually orthogonal additive idempotents with sum \(1\). Therefore \(A=\bigoplus_w\operatorname{im}E_w\), and \(\bigcap_i\operatorname{im}P_i=\operatorname{im}E_{\mathbf1}\). Conversely each internally embedded labeled Boolean decomposition of \(A\) recovers exactly one tuple of commuting additive projections. The finite-abelian-group elementary-divisor classification assigns to each summand an array \(\mathbf m^{(w)}\) with the specified total. The automorphism group of \(A\) acts transitively on internally embedded labeled direct decompositions having prescribed constituent isomorphism types, with stabilizer \(\prod_w\operatorname{Aut}(A_w)\). Orbit-stabilizer therefore gives the factor \(\mathcal U(\mathbf m)/\prod_w\mathcal U(\mathbf m^{(w)})\). Multiplying by the exact common-fixed-point factor \(|A|/|A_{\mathbf1}|\) proves \(C_t\). The automorphism order follows by counting the \(p\)-group homomorphisms between cyclic summands and testing invertibility of each equal-exponent diagonal block modulo \(p\). Adding the universally commuting trivial group endomorphism in any subset of tuple positions proves the binomial convolution for \(\widehat C_t\). Ordinary distinct-tuple inclusion-exclusion via signed Stirling numbers gives the clique formula.

**Step 4: maximal cliques.** Any commuting family is contained in the family of affine projections fixing a common point \(x\), based on its joint decomposition. Refine any decomposable summand into indecomposable direct summands and include all Boolean coordinate projections. Maximality forces an indecomposable direct decomposition; for finite abelian groups the indecomposables are precisely cyclic prime-power factors. Conversely the complete Boolean family corresponding to \(r\) such factors is maximal: an affine projection commuting with its constant map fixes the same point, and a linear endomorphism commuting with all coordinate projections preserves each cyclic indecomposable summand; on a cyclic group of prime-power order the only idempotent endomorphisms are zero and identity. The trivial group endomorphism adds one universal vertex. The constant map identifies the common fixed point uniquely, and the minimal nonzero linear projections identify the unordered constituent subgroups, so there is no double counting. The number of unordered indecomposable decompositions is the automorphism-group order divided by independent automorphisms of the cyclic factors and permutations of identical factors. Multiply by \(|A|\) possible fixed points to obtain the maximal-clique count.

**Step 5: mixed-exponent specialization.** Put \(B=C_{p^a}\), \(C=C_{p^b}\), \(a<b\). In a labeled Boolean decomposition, either both indecomposables receive the same word or they receive distinct words. A same-word allocation has one embedded decomposition; its common-fixed-point factor is one when the word is all-ones and \(p^{a+b}\) otherwise. This gives \(1+(Q-1)p^{a+b}\). Two distinct words specify an embedded decomposition in exactly \(p^{2a}\) ways (computed as \(|\operatorname{Aut}(B\oplus C)|/(|\operatorname{Aut}B||\operatorname{Aut}C|)\)). For ordered distinct color assignments, both words differ from all-ones in \((Q-1)(Q-2)\) cases, contributing \(p^{a+b}\) translations; placing just \(B\) or just \(C\) in the all-ones color contributes \((Q-1)p^b\) or \((Q-1)p^a\), respectively. Adding these contributions yields the closed expression. Its coefficient of \(p^b\) is strictly positive for \(t\ge1\). By contrast the unweighted additive-projection tuple count is \(Q+p^{2a}Q(Q-1)\), independent of \(b\) as long as \(b>a\). This explicit comparison proves the stated loss and recovery of exponent information.

## Verification

The accompanying standalone standard-library Python script `verify_mixed_dihedral.py` enumerates all additive endomorphisms of \(C_9\oplus C_3\), filters idempotents, and lists every associated generalized-dihedral group retraction. It independently tests the homomorphism condition on group generators against every group element, verifies idempotence on all group elements, counts all ordered commuting pairs, and enumerates all inclusion-maximal commuting affine-projection cliques. It checks the mixed-exponent formula through tuple length three and the one-tuple value at exponent \(27\). Run as `python verify_mixed_dihedral.py`. The checks are finite corroboration; the universal statements rely on the proof above.

## Relationship to prior work

Arvasi, Odabaş and Wensley describe idempotent group endomorphisms for the ordinary dihedral group of order \(2p\) in their 2019 manuscript, Section 4.4. That cyclic-prime boundary is established prior coverage; this result does not claim it as new. The published *Commuting retractions of elementary generalized dihedral groups* establishes the affine group description and a maximal-clique census for the case \(A=(C_p)^d\). Our proof extends the compatibility and exact simultaneous-tuple census to **all odd finite abelian rotation kernels**, with a type-dependent common-fixed-point weight; an elementary vector-space result alone does not supply that nonfree-module census. The published *All-arity idempotent clique spectra of finite abelian \(p\)-groups and an invisible exponent* supplies the unweighted additive-module decomposition count and proves exponent invisibility. This theorem retains that established additive classification as an input but changes the group and the invariant: the affine weighted formula gives the opposite exponent-detection behavior. Classical simultaneous diagonalization of commuting idempotents is also credited, not claimed original. The novelty claim concerns the joint weighted nonabelian retraction formula, maximal compatible systems in the arbitrary odd-kernel case, and the explicit exponent-visibility contrast, not the individual ingredients.

## Limitations

The odd-order assumption is essential to the homomorphism classification; groups with even-order rotation kernels are not treated. The formulas describe finite groups, not all affine maps of arbitrary infinite abelian groups. The result does not prove that compatible-retraction statistics reconstruct arbitrary finite abelian kernels, only the specified mixed-exponent pair. General classification of affine projections and direct-sum decompositions is classical, and the claimed new combination may have an unlocated equivalent in finite-module or semigroup literature; priority is therefore provisional. Computational checks cover only the stated finite examples. Independent mathematical audit has not been performed.

## References

1. Z. Arvasi, A. Odabaş, C. D. Wensley, *Computing 3-Dimensional Groups: Crossed Squares and Cat²-Groups*, arXiv:1911.12799, first public 2019-11-28, Section 4.4. Accepted manuscript: https://pure.bangor.ac.uk/ws/portalfiles/portal/50652037/cat2_xs2_final.pdf.
2. *Commuting retractions of elementary generalized dihedral groups*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-commuting-retractions-of-elementary-generalized-dihedral-groups--0ef9efc1c172.
3. *All-arity idempotent clique spectra of finite abelian \(p\)-groups and an invisible exponent*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-all-arity-idempotent-clique-spectra-of-finite-abelian-p-groups-a--3e67e5c96d80.
4. C. C. Edmunds, *Interchange Rings*, arXiv:1402.3699 (2014), especially the simultaneous-diagonalization results for finite abelian groups.
