# Maximal annihilating subsemigroups of finite-chain partial isotone maps

## Finding
For every integer \(n\ge2\), let \(\mathcal P_n\) be the semigroup of partial order-preserving selfmaps of the chain \([n]\), with the empty map \(0\). An *annihilating subsemigroup* means a nonempty subsemigroup \(S\) satisfying \(fg=0\) for every ordered pair \(f,g\in S\), including equal pairs. For each nonempty proper subset \(D\subset[n]\), set
\[
M_D=\{f\in\mathcal P_n:\operatorname{dom}f\subseteq D,\ \operatorname{im}f\subseteq[n]\setminus D\}.
\]
The inclusion-maximal annihilating subsemigroups are **exactly** the \(M_D\). Thus there are \(2^n-2\) of them. For \(d=|D|\) and \(e=n-d\), the complete joint domain-size and image-rank polynomial is
\[
P_{d,e}(u,v)=1+\sum_{r=1}^{\min(d,e)}\binom er v^r\sum_{k=r}^{d}\binom dk\binom{k-1}{r-1}u^k.
\]
The polynomial depends only on \((d,e)\), not on the positions of \(D\). Its cardinality \(B(d,e)=P_{d,e}(1,1)\) satisfies the rational bivariate identity
\[
\sum_{d\ge0,e\ge1}B(d,e)x^dy^e=\frac{y}{1-2x-y+xy}.
\]
Consequently, with \(F_0=0,F_1=1\) the ordinary Fibonacci numbers,
\[
\sum_{d=0}^{n-1}B(d,n-d)=F_{2n},\qquad
\sum_{d=1}^{n-1}B(d,n-d)=F_{2n}-1.
\]
The last sums contain **one cardinality representative for each allowed domain size**, not one term for each labelled subset. The full size multiset of maximal annihilating subsemigroups consists of \(\binom nd\) copies of \(B(d,n-d)\) for \(1\le d<n\).

## Assumptions and scope
No restriction is imposed on whether a partial map is injective; empty domain is allowed. Composition is ordinary partial-map composition, and rank is the number of distinct images, not the domain size. The classification is only for subsemigroups all of whose pairwise products are the **ambient empty map**; it does not purport to classify all abstract null subsemigroups with a possibly nonempty zero. The formulas hold for all \(n\ge2\) and all subsets \(D\) as specified. For the generating series the formal auxiliary value \(B(0,e)=1\) is used.

## Proof
Given any annihilating \(S\), define \(U=\bigcup_{f\in S}\operatorname{dom}f\) and \(V=\bigcup_{f\in S}\operatorname{im}f\). The fact that every composition is empty means \(U\cap V=\varnothing\): if \(z\in V\cap U\), some \(f\) has an input sent to \(z\), and some \(g\) is defined at \(z\); then one of the ordered compositions is nonempty. Hence \(S\subseteq M_U\). Conversely all compositions within \(M_D\) vanish because their possible intermediate values belong to \([n]\setminus D\), disjoint from every domain.

If \(S\) is maximal and contains a nonempty map, \(U\) is nonempty and proper, so \(S=M_U\). Each \(M_D\) contains every singleton map \(x\mapsto y\) for \(x\in D,y\notin D\), so its union of domains is \(D\) and its union of images is its complement. Any annihilating supersemigroup must have domain union containing \(D\) and image union containing its complement, which by disjointness forces both to be unchanged. It therefore lies inside \(M_D\). The singleton \(\{0\}\) is not maximal for \(n\ge2\), proving the classification and distinctness.

Choose a partial map in \(M_D\) with domain size \(k\ge1\) and image rank \(r\ge1\). Its ordered domain can be chosen in \(\binom dk\) ways, and its ordered image set in \(\binom er\) ways. A weakly increasing surjection of a \(k\)-chain onto a fixed \(r\)-chain consists of \(r\) nonempty consecutive fibers and is therefore counted by \(\binom{k-1}{r-1}\). Every such choice gives a different map, producing the polynomial. The empty map contributes \(1\).

Summing the rank count and using \(\sum_{r=1}^k\binom er\binom{k-1}{r-1}=\binom{e+k-1}{k}\) (count weakly increasing words of length \(k\) in an \(e\)-letter alphabet) gives
\[
B(d,e)=\sum_{k=0}^{d}\binom dk\binom{e+k-1}{k}.
\]
For fixed \(e\ge1\), its ordinary generating function in \(d\) is \( (1-x)^{e-1}/(1-2x)^e\). This follows by exchanging the \(d,k\) sums and using \(\sum_{d\ge k}\binom dkx^d=x^k/(1-x)^{k+1}\). Summing over \(e\ge1\) now gives \(y/(1-2x-y+xy)\). Setting \(x=y=t\) yields \(t/(1-3t+t^2)=\sum_{n\ge1}F_{2n}t^n\), since \(F_{2n}\) obeys the recurrence \(a_n=3a_{n-1}-a_{n-2}\) with initial values \(1,3\). Removing the formal \(d=0\) term proves the final identity.

## Verification
The accompanying `check.py` enumerates every partial order-preserving map for \(2\le n\le5\), independently groups each \(M_D\) by domain and image rank, and checks every coefficient. It also tests, for all outsiders through \(n=5\), a singleton-map witness to maximality and verifies the Fibonacci profile sums. Execute `python check.py`. The proof, not these finite tests, establishes arbitrary \(n\).

## Relationship to prior work
Garba's 1994 study of nilpotents in partial order-preserving semigroups concerns nilpotent-generated semigroups, ranks and depth; it is not the same as the maximal pairwise-empty-product family and its full size and joint-rank spectrum. Cameron–Gadouleau–Mitchell–Peresse (2015) study subsemigroup chains and null-semigroup constructions in the full transformation and order-preserving **full** transformation monoids; their null principal-factor constructions differ from an ambient-empty-product classification of all partial isotone maps. General null-transformation and partial nilpotent census results concern either a nonempty designated zero, unrestricted transformations, or elementwise nilpotence rather than the present maximal family. These comparisons do not establish that no earlier equivalent exists.

## Limitations
The simple support-disjointness structural lemma can be adapted to unrestricted partial maps, so the distinctive enumeration here is the precise isotone rank spectrum and its rational/Fibonacci size-profile structure. The identity \(F_{2n}\) is a sum over one size representative per \(d\), **not** the sum of the orders of all \(2^n-2\) labelled maximal families. This result does not classify larger classes of nilpotent semigroups or all null semigroups having nonempty zero. Originality beyond the specifically inspected literature is not independently established.

## References
- G. U. Garba, “Nilpotents in semigroups of partial order-preserving transformations,” *Proceedings of the Edinburgh Mathematical Society* 37 (1994), 361–377. DOI: 10.1017/S001309150001885X.
- P. J. Cameron, M. Gadouleau, J. D. Mitchell, Y. Peresse, “Chains of subsemigroups,” arXiv:1501.06394v1 (26 January 2015), especially sections 4, 5 and 9.
