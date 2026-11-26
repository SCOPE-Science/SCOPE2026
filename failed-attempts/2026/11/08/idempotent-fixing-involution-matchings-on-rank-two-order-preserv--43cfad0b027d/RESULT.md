# Idempotent-fixing involution matchings on rank-two order-preserving transformations

## Finding
For each integer \(n\ge2\), let \(\mathcal O_n\) be the monoid of order-preserving maps of the chain \([n]=\{1,\ldots,n\}\), under composition. Its rank-two Green \(\mathcal D\)-class admits an explicit inverse matching of order two that fixes every idempotent and is equivariant under reversing the chain. Every non-idempotent belongs to a two-cycle canonically labeled by a three-element subset of \([n]\). There are exactly \(\binom n3\) such two-cycles and \(\binom{n+1}3\) fixed points.

## Assumptions and scope
An inverse of an element \(f\) in a semigroup is a map \(g\) satisfying \(f\circ g\circ f=f\) and \(g\circ f\circ g=g\); it need not be a functional inverse. An *involution matching* is a permutation \(\Theta\) satisfying \(\Theta^2=\mathrm{id}\) and \(\Theta(f)\) is such an inverse of \(f\). The domain is the single Green \(\mathcal D\)-class of all **rank-two** transformations in \(\mathcal O_n\), not the entire monoid.

Every rank-two order-preserving map has a unique triple \((k,a,b)\) with \(1\le k<n\), \(1\le a<b\le n\), namely
\[
f_{k,a,b}(i)=\begin{cases}a,&i\le k,\\ b,&i>k.\end{cases}
\]
Define the following map on these triples:
\[
\Theta(f_{k,a,b})=\begin{cases}
f_{k,a,b},&a\le k<b,\\
f_{b-1,k,a},&k<a,\\
f_{a,b,k+1},&k\ge b.
\end{cases}
\]
All three branches produce valid increasing image pairs. In particular, the formula is valid for every \(n\ge2\), without parity restrictions.

## Proof
**Inverse criterion.** For rank-two maps \(f=f_{k,a,b}\) and \(g=f_{h,c,d}\), the two identities \(f\circ g\circ f=f\) and \(g\circ f\circ g=g\) hold if and only if
\[
 a\le h<b\quad\text{and}\quad c\le k<d.
\]
Indeed, for \(f\circ g\circ f=f\), the restriction of \(g\) to \(\{a,b\}\) must map these two values to different sides of the cut \(k\). As \(g\) is nondecreasing, this forces \(a\le h<b\) and \(c\le k<d\). Conversely these inequalities give \(f(g(a))=a\) and \(f(g(b))=b\), establishing the first identity, and symmetrically \(g(f(c))=c\), \(g(f(d))=d\), establishing the second.

**Three disjoint cases.** If \(a\le k<b\), the map \(f\) is idempotent, hence is its own semigroup inverse. If \(k<a<b\), the output \(g=f_{b-1,k,a}\) satisfies \(k\le k<a\) and \(a\le b-1<b\), the inverse inequalities above, and lies in the third branch because its new cut \(b-1\) is at least its right image \(a\). Applying \(\Theta\) again returns \(f_{k,a,b}\). If \(a<b\le k\), the output \(g=f_{a,b,k+1}\) satisfies \(a\le a<b\), \(b\le k<k+1\), and lies in the second branch; applying \(\Theta\) again likewise recovers \(f\). This proves \(\Theta^2=\mathrm{id}\) and the inverse condition for every element.

**Fixed points and transpositions.** Direct substitution gives \(f_{k,a,b}^2=f_{k,a,b}\) precisely when \(a\le k<b\). All such maps are fixed by \(\Theta\); no others are. The count is
\[
\sum_{k=1}^{n-1} k(n-k)=\binom{n+1}{3}.
\]
Every nonfixed pair has the form
\[
f_{x,y,z}\longleftrightarrow f_{z-1,x,y}\qquad(1\le x<y<z\le n),
\]
and this representation is unique because exactly one element in each pair satisfies cut \(<\) left image. Hence there are \(\binom n3\) transpositions. As a cross-check, the total \(\binom{n+1}{3}+2\binom n3\) equals \((n-1)\binom n2\), the total number of rank-two order-preserving transformations.

**Reversal symmetry.** Let \(\rho(i)=n+1-i\), and let \(R(f)=\rho\circ f\circ\rho\). Then
\[
R(f_{k,a,b})=f_{n-k,n+1-b,n+1-a}.
\]
The reversal sends the idempotent branch to itself and interchanges the two non-idempotent branches. In each nontrivial pair it sends the triple \((x,y,z)\) to \((n+1-z,n+1-y,n+1-x)\). Consequently \(R\circ\Theta=\Theta\circ R\).

## Verification
The standalone `verify.py` checks, for every \(2\le n\le16\) and every rank-two triple, the two semigroup inverse identities by direct function composition, the involution identity, the equivalence of fixed points and idempotents, and commutation with reversal. It also verifies the exact counts. This is an exhaustive finite check over the stated range, not an infinite proof. The general theorem is established by the preceding case analysis. Recorded outcome: `VERIFY_OK n=2..16 elements=7820`.

## Relationship to prior work
Higgins (2026, Theorem B) proves existence of *permutation* matchings for all ranks of the order-preserving transformation monoid by balanced weightings; the cited theorem neither requires the matching to be involutive nor supplies this triple-indexed rank-two construction. Higgins (2024, Proposition 2.3) proves an involution matching when the number of columns of a combinatorial \(\mathcal D\)-class is a multiple of its number of rows. For this rank-two class those parameters are \(\binom n2\) and \(n-1\), with ratio \(n/2\), so that proposition directly applies for even \(n\) but not odd \(n\). The same 2024 paper discusses additional congruence cases and asks a broader open involution-matching question. Higgins (2019) constructs a natural involution for orientation-preserving/orientation-reversing transformation monoids, but its construction does not restrict to all order-preserving maps. The present result is a concrete, idempotent-fixing and reversal-equivariant rank-two construction, including odd sizes, not a solution of the all-ranks involution question.

## Limitations
The construction applies only to rank two; extending it to higher Green \(\mathcal D\)-classes or to all of \(\mathcal O_n\) is not proved. The two-cycle count is a consequence of fixing precisely all idempotents. No claim is made that the construction is unique or that the mutual inverses are *strong* inverses. Literature searches cannot guarantee historical priority; equivalent special-case constructions may be implicit in older combinatorial treatments.

## References
1. P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1, publicly submitted 2026-10-01. https://arxiv.org/abs/2610.01912
2. P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, Semigroup Forum 109 (2024), 141–147. https://doi.org/10.1007/s00233-024-10430-0
3. P. M. Higgins, *Involution matchings, the semigroup of orientation-preserving and orientation-reversing mappings, and inverse covers of the full transformation semigroup*, Semigroup Forum 98 (2019), 669–689. https://doi.org/10.1007/s00233-019-10018-z
