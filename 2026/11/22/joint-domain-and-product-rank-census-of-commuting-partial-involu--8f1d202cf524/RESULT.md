# Joint domain and product-rank census of commuting partial involutions

## Finding

For any finite set \(X\) of size \(n\geq 0\) and integer \(t\geq 1\), let \(\mathcal I(X)\) be its symmetric inverse monoid (partial injective self-maps). Let \(\mathcal T_{n,t}\) be the set of ordered tuples \((s_1,\ldots,s_t)\) such that \(s_i^3=s_i\) and \(s_i s_j=s_j s_i\) for all \(i,j\). Thus each \(s_i\) is a partial involution, including the empty map and partial identities.

For \(\mathbf y=(y_1,\ldots,y_t)\), define
\[
T_{n,t}(\mathbf y,z)=\sum_{(s_i)\in\mathcal T_{n,t}}\left(\prod_{i=1}^t y_i^{|\operatorname{dom}(s_i)|}\right)z^{\operatorname{rank}(s_1\cdots s_t)}.
\]
Let \(\binom{k}{r}_2\) denote the number of codimension-\(r\) subspaces of \(\mathbb F_2^k\), equal to the Gaussian binomial coefficient (one for \(k=r=0\)). Then the following identity of formal power series holds for every \(t\geq1\):
\[
\boxed{\sum_{n\geq0}T_{n,t}(\mathbf y,z)\frac{u^n}{n!}=
\exp\!\left(\sum_{S\subseteq[t]}\sum_{r=0}^{|S|}
\binom{|S|}{r}_2\frac{u^{2^r}}{2^r}
\prod_{i\in S}y_i^{2^r}
 z^{2^r\mathbf1_{S=[t]}}\right).}
\]
Empty products equal one. This is simultaneously a complete enumerator for all individual domain ranks and the rank of the common product. In particular, setting all marking variables to one gives the exact all-arity count
\[
\sum_{n\geq0}|\mathcal T_{n,t}|\frac{u^n}{n!}=
\exp\!\left(\sum_{r=0}^t \frac{u^{2^r}}{2^r}
\sum_{k=r}^t\binom tk\binom kr_2\right).
\]
For ordered commuting pairs it simplifies to
\[
\boxed{\sum_{n\geq0}|\mathcal T_{n,2}|\frac{u^n}{n!}=\exp(4u+\tfrac52u^2+\tfrac14u^4).}
\]
Consequently \(|\mathcal T_{n,2}|\) begins \(1,4,21,124,817,5844,45061\) for \(n=0,\ldots,6\), and satisfies, with \(a_j=0\) for \(j<0\),
\[
a_{n+1}=4a_n+5n a_{n-1}+n(n-1)(n-2)a_{n-3},\qquad a_0=1.
\]
The product is a partial involution supported exactly on the intersection of the constituent domains; thus the \(z\)-variable also tracks their common domain intersection.

## Assumptions and scope

All finite sets are labelled; tuples are ordered, contain repetitions, and may include the empty partial map. Multiplication is composition of partial maps, using either consistent composition convention. A partial involution means an element \(s=s^{-1}\) of the inverse monoid, equivalently \(s^3=s\): it is an involutive permutation of its domain, undefined elsewhere. The formula covers every \(n\geq0\) and \(t\geq1\), not merely fixed finite cutoffs. The coefficients lie in \(\mathbb Z[\mathbf y,z]\), although rational coefficients appear in the exponential representation. No probability limit law is asserted.

## Proof

**1. The domains form invariant membership blocks.** For \((s_i)\in\mathcal T_{n,t}\), put \(D_i=\operatorname{dom}(s_i)\) and \(e_i=s_i^2\). Since \(s_i\) is a partial involution, \(e_i\) is the partial identity on \(D_i\). Pairwise commutativity implies \(s_i e_j=e_j s_i\) for every \(i,j\). Evaluating at a point \(x\in D_i\), the latter equality implies
\[
x\in D_j\quad\Longleftrightarrow\quad s_i(x)\in D_j.
\]
This holds for \(j=i\) as well, because \(s_i\) permutes \(D_i\). Consequently the disjoint membership blocks
\[
X_S=\{x\in X:\{i:x\in D_i\}=S\},\qquad S\subseteq[t],
\]
are invariant under each \(s_i\) for which \(i\in S\). A generator with \(i\notin S\) is undefined throughout \(X_S\).

**2. Classification by elementary abelian group actions.** On a fixed block \(X_S\), the active restrictions \(s_i|_{X_S}\), \(i\in S\), are pairwise commuting full permutations of order dividing two. They define a permutation action of the elementary abelian group \(V_S=(C_2)^{|S|}\). Conversely, arbitrarily partition \(X\) into labelled blocks \((X_S)_{S\subseteq[t]}\), give each block a \(V_S\)-action, and let \(s_i\) act by its distinguished generator on blocks containing \(i\), undefined on all other blocks. This reconstructs one and only one commuting tuple of partial involutions. Thus the correspondence is bijective, including empty blocks and nonfaithful actions.

**3. Connected orbit count.** Every transitive \(V_S\)-set is \(V_S/H\) for a subgroup \(H\le V_S\). Since \(V_S\) is abelian, two such sets are isomorphic exactly when their subgroups coincide, and the action automorphism group of \(V_S/H\) has cardinality \(d=[V_S:H]\). If \(H\) has codimension \(r\), then \(d=2^r\), and there are \(\binom{|S|}{r}_2\) choices for \(H\). On any prescribed labelled set of size \(d\), each transitive action type therefore has exactly \(d!/d\) realizations: all bijections of a standard model onto those labels modulo its \(d\) automorphisms. Its labelled exponential generating function contribution is \(u^d/d\). The orbit decomposition is unique; by the labelled exponential formula, all actions on the block are counted by the exponential of the sum of these orbit contributions.

**4. Rank markings and the product.** A transitive orbit of size \(d\) inside \(X_S\) contributes \(d\) to \(|D_i|\) exactly when \(i\in S\), hence contributes \(\prod_{i\in S}y_i^d\). Because membership is invariant along every active map, the product \(s_1\cdots s_t\) is defined precisely on \(X_{[t]}=\bigcap_i D_i\), where it is a permutation (indeed an involution), so an orbit in \(X_{[t]}\) contributes \(z^d\), and no other orbit contributes a \(z\)-factor. Multiplying orbit weights and applying the labelled exponential formula across every block gives the displayed master identity.

**5. Pair specialization.** For \(t=2\), the four membership sets \(\varnothing,\{1\},\{2\},\{1,2\}\) have orbit exponents respectively \(u\), \(u+u^2/2\), \(u+u^2/2\), and \(u+3u^2/2+u^4/4\). Their sum is \(4u+5u^2/2+u^4/4\). Differentiating the exponential gives \(F'(u)=(4+5u+u^3)F(u)\), which yields the recurrence after multiplying coefficients by factorials.

## Verification

The standalone file `computations/checker.py` generates all partial involutions directly by selecting domains and pairing cycles of lengths one and two, composes explicit partial maps pointwise, and counts ordered tuples satisfying all pairwise commutation equations. Independently, it computes the predicted multivariate series from Gaussian-binomial coefficients, matching **every individual-domain-rank and product-rank stratum**, not just the totals.

The checker compares exhaustive distributions for \((t,n)=(1,5)\), \((2,0),\ldots,(2,6)\), \((3,0),\ldots,(3,4)\), and \((4,2),(4,3)\). For instance, the totals at \(t=3\), \(n=0,1,2,3,4\), are \(1,8,83,968,12535\); at \(t=4\), \(n=2,3\), they are \(321,7216\). These finite checks corroborate, but do not replace, the all-parameter combinatorial proof.

Reproduce from an ordinary Python 3 interpreter by running `python computations/checker.py`. No third-party packages or downloaded input files are necessary.

## Relationship to prior work

Araújo, Bentz, and Konieczny (2012, Proposition 2.2 and Sections 2–6) describe commuting elements of the full symmetric inverse semigroup, then study maximum commutative subsemigroups and commuting-graph diameters; their stated results do not give the present all-arity, joint-domain-rank and product-rank enumerator. The classification here is compatible with their cycle/chain commuting criterion but specializes to self-inverse maps and assembles the membership blocks into a weighted elementary-abelian action species.

The classical theory of finite permutation actions supplies the transitive \(G/H\)-decomposition and the labelled exponential formula; the full-permutation case of commuting involutions follows by retaining only the full-membership block \(S=[t]\). The partial-domain blocks, and especially the common-product-rank marker, are additional content not supplied by an unweighted full-action enumeration. Nearby published research on logical types of commuting involutions and on the single-element involution spectra of constrained inverse monoids concerns different objects or invariants. The result does not claim priority for the underlying action-counting machinery.

## Limitations

The claim concerns only partial involutions, not arbitrary partial injections or higher-order torsion, and counts labelled structures rather than simultaneous-conjugacy classes. Independent expert review has not occurred; undetected older implicit treatments of the same weighted formula remain a priority risk. Exhaustive tests stop at the finite sizes explicitly listed. No asymptotic conclusions are inferred solely from the tests.

## References

1. J. Araújo, W. Bentz, J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664v1, first posted 2012-05-08. Full lawful text: https://arxiv.org/html/1205.1664v1 . Sections 1–3 and 4–7, especially Proposition 2.2.
2. S. Lipscomb, *Symmetric Inverse Semigroups*, AMS Mathematical Surveys and Monographs 46 (1996), cited for background definitions in reference 1; its complete book was not inspected here.
3. C. Bates, D. Bundy, S. Perkins, P. Rowley, *Commuting involution graphs for symmetric groups*, J. Algebra 266 (2003), 133–153, cited for the **full permutation group** setting in reference 1. This work is not cited as containing the present partial-map enumeration.
