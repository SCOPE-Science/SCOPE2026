# Characteristic-two component explosion in projection derivations of rectangular-band algebras

## Finding
Let \(k\) be any field and \(m,n\ge2\). Let \(S_{m,n}=[m]\times[n]\) be the rectangular band with \((i,j)(h,l)=(i,l)\), and write \(A=k[S_{m,n}]\). An **idempotent derivation** is a \(k\)-linear map \(D:A\to A\) satisfying the ordinary Leibniz identity \(D(xy)=D(x)y+xD(y)\) and the composition identity \(D^2=D\). Put \(b=n-1\), \(c=m-1\).

There is an intrinsic multiplication-compatible vector-space decomposition \(A=ke\oplus B\oplus C\oplus(C\otimes B)\), with \(\dim B=b\), \(\dim C=c\), and its only nonzero homogeneous products are \(e^2=e\), \(e v=v\), \(u e=u\), and \(u v=u\otimes v\), for \(v\in B\), \(u\in C\). Every derivation has a unique form
\[
\begin{aligned}
D(e)&=v_0+u_0,\\
D(v)&=S(v)+u_0\otimes v,\\
D(u)&=T(u)+u\otimes v_0,\\
D(u\otimes v)&=T(u)\otimes v+u\otimes S(v),
\end{aligned}
\]
where \(S\in\operatorname{End}(B)\), \(T\in\operatorname{End}(C)\), \(v_0\in B\), and \(u_0\in C\). It is composition-idempotent exactly under the conditions
\[
S^2=S,\quad T^2=T,\quad S(v_0)=v_0,\quad T(u_0)=u_0,
\]
together with **either** \(\operatorname{char}(k)=2\), **or** \(S=0\), **or** \(T=0\). In particular, the simultaneous nonzero projection ranks on the two opposite one-sided ideals occur only in characteristic two.

Over \(k=\mathbb F_q\), let \({d\brack r}_q\) be the Gaussian binomial coefficient (zero outside \(0\le r\le d\)). With \(z\) marking \(\operatorname{rank}_k D\), the **exact labeled rank polynomial** in characteristic two is
\[
\boxed{\mathcal P_{m,n,q}(z)=\sum_{s=0}^{b}\sum_{t=0}^{c}{b\brack s}_q{c\brack t}_q q^{s(b-s)+t(c-t)+s+t}\,z^{s m+t n-2st}.}
\]
For odd characteristic it is
\[
\boxed{\mathcal P_{m,n,q}(z)=\sum_{s=0}^{b}{b\brack s}_q q^{s(n-s)}z^{sm}+\sum_{t=1}^{c}{c\brack t}_q q^{t(m-t)}z^{tn}.}
\]
These formulas hold for every prime power, without a large-field hypothesis. In the binary \(2\)-by-\(3\) case the rank polynomial is \(1+12z^2+34z^3+4z^4\); in the \(2\)-by-\(2\) case it is \(1+8z^2\). The odd-field \(2\)-by-\(2\) polynomial is \(1+2qz^2\).

The **reduced geometric solution locus** over an algebraic closure is the disjoint union of smooth, irreducible projection-rank strata. In characteristic two it has exactly \((b+1)(c+1)=mn\) irreducible components indexed by \((s,t)\); in other characteristics it has exactly \((b+1)+(c+1)-1=m+n-1\) indexed by pairs with \(st=0\). Each existing component has dimension
\[
2s(b-s)+2t(c-t)+s+t.
\]
Every component is a vector bundle of rank \(s+t\) over a product of fixed-rank idempotent-matrix varieties. This geometric statement concerns the **reduced locus**, not the possibly nonreduced scheme of the polynomial equations.

## Assumptions and scope
The semigroup algebra is the full \(mn\)-dimensional linear span of band elements, not the finite band itself. No algebra identity is assumed. All derivations are ordinary linear derivations, rather than Hasse–Schmidt or Jordan derivations; composition idempotence is not an assertion that any algebra element is idempotent. The characteristic-two result applies to all even finite fields, not only the prime field. The structural formulas make sense over arbitrary characteristic-two or other fields. Ranks always refer to the linear operator on the entire \(mn\)-space.

## Proof
**1. Adapted multiplication.** Write \(e=e_{11}\), \(B_j=e_{1,j+1}-e_{11}\), \(C_i=e_{i+1,1}-e_{11}\), and \(W_{ij}=e_{i+1,j+1}-e_{i+1,1}-e_{1,j+1}+e_{11}\). Direct multiplication in the rectangular band yields precisely \(e^2=e\), \(e B_j=B_j\), \(C_i e=C_i\), \(C_i B_j=W_{ij}\), all other basis products zero. The \(1+b+c+bc=mn\) displayed elements form a basis, so the decomposition and its tensor multiplication are exact in every characteristic.

**2. Exhaustion of derivations.** Let \(D\) be any derivation. From \(e^2=e\), the \(e\) and \(C\otimes B\) components of \(D(e)\) vanish, leaving \(D(e)=v_0+u_0\). Differentiating \(e v=v\) and \(v e=0\) forces \(D(v)\) to have a component \(S(v)\in B\) and the fixed correction \(u_0\otimes v\in C\otimes B\), with no other components. Similarly \(u e=u\) and \(e u=0\) give \(D(u)=T(u)+u\otimes v_0\). The product \(uv=u\otimes v\) then forces the stated action on the tensor summand. Conversely, substitution into the four displayed nonzero products and every zero product verifies the Leibniz rule for arbitrary \((v_0,u_0,S,T)\). Uniqueness follows by comparing homogeneous components.

**3. Exhaustion of idempotents.** Comparing the \(B\)- and \(C\)-components of \((D^2-D)(v)\), \((D^2-D)(u)\), and \((D^2-D)(e)\), we obtain \(S^2=S\), \(T^2=T\), \(S(v_0)=v_0\), and \(T(u_0)=u_0\). On the tensor summand,
\[
(D^2-D)(u\otimes v)=2T(u)\otimes S(v).
\]
Since a pure tensor of nonzero vectors cannot vanish over a field, this condition is equivalent to characteristic two or one of \(S,T\) vanishing. The remaining components on \(e,B,C\) are \(2u_0\otimes v_0\), \(2u_0\otimes S(v)\), and \(2T(u)\otimes v_0\), respectively, and vanish automatically under the preceding conditions. This proves necessity and sufficiency, including the boundaries \(s=0\) and \(t=0\).

**4. Linear ranks.** Filter \(A\) by \(0\subset C\otimes B\subset (B\oplus C\oplus C\otimes B)\subset A\). Because \(D^2=D\), the image of each filtered piece is the intersection of that piece with \(\operatorname{im}D\), so rank is additive over the induced graded maps. These maps are \(T\otimes I_B+I_C\otimes S\), \(S\oplus T\), and zero, respectively. In characteristic two, the tensor eigenvalue is one exactly on \((\operatorname{im}T\otimes\ker S)\oplus(\ker T\otimes\operatorname{im}S)\), of dimension \(t(b-s)+(c-t)s\); the total rank is \(s+t+t(b-s)+(c-t)s=sm+tn-2st\). Outside characteristic two, one of \(S,T\) is zero and the total rank is \(sm\) or \(tn\).

**5. Exact counting.** A rank-\(s\) projection on a \(b\)-dimensional vector space is equivalent to choosing its \(s\)-dimensional image and a complementary kernel. There are \({b\brack s}_q q^{s(b-s)}\) such ordered decompositions. For each \(S\), the vector \(v_0\) ranges independently through its \(s\)-dimensional image, giving \(q^s\) choices; likewise \(q^t\) for \((T,u_0)\). Multiplying these factors and using the idempotent-pair restriction from Step 3 yields the two rank polynomials. Double-counting at \((s,t)=(0,0)\) is avoided in the odd-characteristic formula by starting the second sum at \(t=1\).

**6. Geometric components.** Rank-\(s\) idempotent matrices form a smooth irreducible variety of dimension \(2s(b-s)\), because it is the homogeneous space \(\operatorname{GL}_b/(\operatorname{GL}_s\times\operatorname{GL}_{b-s})\); similarly for \(T\). The conditions \(v_0\in\operatorname{im}S\) and \(u_0\in\operatorname{im}T\) are tautological vector bundles of ranks \(s\) and \(t\). The idempotent ranks are locally constant in an algebraic family (the image of an idempotent matrix is a finite locally free summand). Thus the solution locus is a finite disjoint union of open-and-closed rank strata. Allowed pairs are all \((s,t)\) in characteristic two, and precisely those with \(st=0\) otherwise. Each stratum is smooth and geometrically irreducible, so these are exactly the components of the reduced locus with the stated dimensions.

## Verification
The standalone `verify_rectangular_derivations.py` implements the displayed multiplication directly, builds derivation matrices from the four independent parameters, checks the original Leibniz and composition-idempotence identities on basis elements, performs exact finite-field row reduction, and compares the resulting rank histograms to separate enumeration of projected pairs. The exhaustive test parameters are \((m,n,p)=(2,2,2),(2,2,3),(2,2,5),(2,3,2),(3,2,2)\), with prime field arithmetic. A second test independently examines all \(2^{16}=65,536\) linear endomorphisms of the four-dimensional binary algebra against the original Leibniz identity; exactly \(16\) are derivations and exactly \(9\) of those are composition-idempotent. The general finite-field and geometric conclusions follow from the proof, not from these finite tests. The test script uses Python's standard library only.

## Relationship to prior work
Drozd and Plakosh (2022), Definition 1.1 and Proposition 1.3, introduce and normalize Munn algebra multiplication by a sandwich matrix and study representation types. Their result supplies structural motivation and the rank-one normalization but not the classification of projection derivations. Yu, Luo, and Li (2024), Definition 1.2 and Theorem 2.2, treat the same broader Munn construction, zero-product determination and generation by idempotent **algebra elements**; their derivation-adjacent statements do not give the operator equations here. Existing same-algebra finite-field results determine the coefficient-array rank of element commutators, and existing sandwich-semigroup results enumerate commuting **elements** satisfying their sandwich-idempotence equation. Neither concerns a composition-idempotent Leibniz derivation. Existing classifications of projection derivations on upper triangular matrix algebras use a different algebra, with different rank spectra and diagonal-label geometry. In particular, idempotent **elements** and idempotent **derivations** are not interchangeable notions. The exact simultaneous projection-rank parameterization and characteristic-two component count are not implied by these inspected results.

## Limitations
This theorem concerns the rank-one sandwich class (rectangular-band semigroup algebras), not arbitrary Munn algebras of larger sandwich rank, general semigroup rings, or nonlinear derivations. The component statement is for the reduced geometric locus; no scheme-theoretic smoothness of a possibly nonreduced polynomial equation scheme is asserted. The full literature on semigroup-algebra derivations may contain synonymous or more general results; absence from inspected texts and indexed records does not prove global priority. No independent mathematical validation was undertaken.

## References
1. Y. A. Drozd and A. I. Plakosh, *Representations of Munn algebras and related semigroups*, arXiv:2202.06103v1 (first posted 2022-02-12), https://arxiv.org/abs/2202.06103.
2. B. Yu, K. Luo, and J. Li, *Zero product and zero Jordan product determined Munn algebras*, arXiv:2407.00892v1 (first posted 2024-07-01), https://arxiv.org/abs/2407.00892.
3. *Commutator-rank census of finite rectangular-band semigroup algebras*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-commutator-rank-census-of-finite-rectangular-band-semigroup-alge--6f0f9b3726a9.
4. *Joint matrix-rank spectrum of commuting idempotents in rectangular sandwich semigroups*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-joint-matrix-rank-spectrum-of-commuting-idempotents-in-rectangul--85aa4c5711c9.
5. *Characteristic-dependent rank spectra of idempotent derivations of triangular matrix algebras*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-characteristic-dependent-rank-spectra-of-idempotent-derivations--0886e9e8597b.
