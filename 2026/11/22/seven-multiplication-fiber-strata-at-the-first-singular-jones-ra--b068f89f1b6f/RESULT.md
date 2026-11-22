# Seven multiplication-fiber strata at the first singular Jones rank

## Finding

Let \(\mathcal J_n\) be the Jones (planar Temperley–Lieb) diagram monoid on two rows of \(n\) boundary vertices, with closed middle components discarded on multiplication. For every integer \(n\ge4\), let \(X_n\) be its rank-\(n-2\) Green class and define the ordered prescribed-target fiber
\[
\Phi_n(h)=\#\{(x,y)\in X_n^2:xy=h\},\qquad h\in\mathcal J_n.
\]
Every output has rank \(n-2\) or \(n-4\). Every diagram of either rank occurs; no other diagram occurs. On every rank-\(n-2\) target,
\[
\Phi_n(h)=3n-5.
\]
On the rank-\(n-4\) targets, the fiber size belongs to \(\{1,2,3,4,5,6,8\}\); the value \(7\) is impossible. Put \(m=n-3\). The numbers of individual rank-\(n-4\) target diagrams having each fiber size are:

| Fiber size | Number of targets |
| ---: | ---: |
| \(1\) | \(m(m-1)\) |
| \(2\) | \(m(m^2-m+1)\) |
| \(3\) | \(2m(m-1)\) |
| \(4\) | \(m(m+1)(m^2-3m+6)/4\) |
| \(5\) | \(m(m-1)(m-2)\) |
| \(6\) | \(5m(m-1)/2\) |
| \(8\) | \(m\) |

Here and below all squares and rational expressions are exact integer-valued counts. In particular, the minimum possible fiber in the rank-\(n-4\) class is one whenever \(n\ge5\), and the maximum is eight for every \(n\ge4\).

More precisely, rank-\(n-4\) targets have independent upper and lower half-diagrams of the following forms, using indices \(0,\ldots,n-1\) on each row:

* \(D(a,b)\), two disjoint adjacent caps joining \((a,a+1)\) and \((b,b+1)\), with \(0\le a\), \(a+2\le b\le n-2\);
* \(N(a)\), nested caps joining \((a,a+3)\) and \((a+1,a+2)\), with \(0\le a\le n-4\).

The same symbols describe two lower cups, using the same left-to-right coordinate convention. The remaining \(n-4\) vertices connect by the unique planar order-preserving propagating strands. With \(\delta_{u,v}\) denoting one when \(u=v\) and zero otherwise, every prescribed rank-\(n-4\) fiber has the exact formula
\[
\begin{aligned}
\Phi_n(N(a),N(c))&=1+\delta_{a,c},\\
\Phi_n(N(a),D(c,d))&=2+\delta_{a,c}+\delta_{a+2,d},\\
\Phi_n(D(a,b),N(c))&=2+\delta_{a,c}+\delta_{b,c+2},\\
\Phi_n(D(a,b),D(c,d))&=4+\delta_{a,c}+\delta_{b,d}+\delta_{b,c+2}+\delta_{d,a+2}.
\end{aligned}
\]
These formulas give all target-specific multiplicities, not just an aggregate rank census.

## Assumptions and scope

A Jones diagram is a planar perfect matching of the \(2n\) boundary points. The propagating rank is the number of edges joining the two rows. Multiplication is obtained by stacking two diagrams and taking the matching induced on the external boundary, discarding connected components contained entirely in the glued middle row. The order in \(xy\) places \(x\) above \(y\). Factors are sampled from the entire rank-\(n-2\) class, not just its idempotents or elementary generators. The counting statement assumes \(n\ge4\), without field, characteristic, or coefficient parameters. The Jones monoid is untwisted: middle loops contribute no scalar factors.

## Proof

**One-cap factors and possible ranks.** A rank-\(n-2\) diagram has one top cap \((i,i+1)\) and one bottom cup \((j,j+1)\), and all its other connections are forced in order. Call it \(A(i,j)\), where \(0\le i,j\le n-2\); thus \(|X_n|=(n-1)^2\). If \(A(i,j)A(k,\ell)\) is formed, its two middle caps lie at positions \(j,j+1\) and \(k,k+1\). If \(|j-k|\le1\), these share a vertex or form a closed two-edge middle component, and the output retains rank \(n-2\). Otherwise they are disjoint, causing two additional outer caps and rank \(n-4\). In the first case the output has top-cap index \(i\) and bottom-cup index \(\ell\); there are exactly \((n-1)+2(n-2)=3n-5\) choices of \((j,k)\), independently of \(i,\ell\).

**Half-diagrams.** A planar half-diagram with exactly two caps and \(n-4\) unpaired through points has either two disjoint adjacent caps \(D(a,b)\) or one nested consecutive double cap \(N(a)\). The numbers of each shape are \(d=(n-2)(n-3)/2\) and \(m=n-3\) respectively. The lower half may be chosen independently, so there are \((d+m)^2=[n(n-3)/2]^2\) rank-\(n-4\) target diagrams.

**Gluing branches.** Consider a rank-decreasing product \(A(i,j)A(k,\ell)\). Delete the top cap \((i,i+1)\) of the first factor and the middle cup \((j,j+1)\); the surviving strands identify the two ordered complements. The second factor's top cap pulls back to the other cap of the resulting upper half. If the upper half is \(D(a,b)\), choosing its first cap as the first factor's original cap gives the two possible branches
\[
(i=a,\ k=b,\ j\le b-2),\qquad (i=a,\ k=b-2,\ j\ge b).
\]
Choosing its second cap gives
\[
(i=b,\ k=a+2,\ j\le a),\qquad(i=b,\ k=a,\ j\ge a+2).
\]
For \(N(a)\), the first factor's cap is necessarily the inner one \((a+1,a+2)\), and only the last two branches remain, with \(i=a+1\). Reflecting the diagram vertically yields the corresponding lower branches with the triples \((i,j,k)\) and \((\ell,k,j)\) exchanged. Every branch chooses the intermediate cap indices uniquely, so counting compatible upper/lower branch pairs counts the factorizations without overcounting.

For an explicit branch certificate, label the four upper \(D(a,b)\) branches in displayed order by \(A,B,C,D\), and the four vertically reflected lower \(D(c,d)\) branches in corresponding order by \(A',B',C',D'\). Each compatible branch pair determines exactly one \((i,j,k,\ell)\). Writing \(\mathbf1_P\) for the indicator of proposition \(P\), their full compatibility table is:

| Upper / lower | \(A'\) | \(B'\) | \(C'\) | \(D'\) |
|:---:|:---:|:---:|:---:|:---:|
| \(A\) | \(0\) | \(\mathbf1_{d\le b}\) | \(0\) | \(\mathbf1_{c\le b-2}\) |
| \(B\) | \(\mathbf1_{d\ge b}\) | \(0\) | \(\mathbf1_{c\ge b-2}\) | \(0\) |
| \(C\) | \(0\) | \(\mathbf1_{d\le a+2}\) | \(0\) | \(\mathbf1_{c\le a}\) |
| \(D\) | \(\mathbf1_{d\ge a+2}\) | \(0\) | \(\mathbf1_{c\ge a}\) | \(0\) |

This table follows by substituting the prescribed lower-branch middle index \(j\) into the upper-branch inequality and the upper-branch middle index \(k\) into the lower-branch inequality. The eight potentially nonzero terms pair into the four complementary comparisons \(d\le b\) versus \(d\ge b\), \(c\le b-2\) versus \(c\ge b-2\), \(d\le a+2\) versus \(d\ge a+2\), and \(c\le a\) versus \(c\ge a\). Each pair sums to \(1+\delta\) at equality. This proves the displayed \(D,D\) formula. A nested upper half retains only rows \(C,D\) of the table (with the nested parameter replacing \(a\)); a nested lower half retains only columns \(C',D'\) (with its nested parameter replacing \(c\)). These restrictions give the other three displayed formulas. Thus the count is an exact branch bijection, with no probabilistic or asymptotic assumption.

**Spectrum and its multiplicities.** Write \(m=n-3\) and \(d=m(m+1)/2\). In the \(N,N\) block, exactly \(m\) targets have fiber two and \(m(m-1)\) have fiber one. In the two \(N,D\) and \(D,N\) blocks together, fiber sizes two, three and four have respective multiplicities \(m^2(m-1)\), \(2m(m-1)\) and \(2m\).

In the \(D,D\) block the four equality corrections are
\[
E_1:(a=c),\quad E_2:(b=d),\quad E_3:(b=c+2),\quad E_4:(d=a+2).
\]
Any three of these four conditions force the fourth, so the correction sum is never three: fiber seven is impossible. Each fourfold coincidence is an adjacent double-cap pair \(D(a,a+2)\) against itself, yielding exactly \(m\) fibers of size eight. Elementary index summation gives the total number of satisfied individual equalities, pairwise intersections, triple intersections and fourfold intersections, respectively, as
\[
S_1=m(m+1)^2,\qquad S_2=5d+m,\qquad S_3=4m,\qquad S_4=m.
\]
For example, five of the six pairwise intersections have size \(d\), while \(E_3\cap E_4\) has size \(m\). Using the absence of a three-correction case, the numbers of \(D,D\) targets with correction sums two and one are
\[
S_2-6m=\frac{5m(m-1)}2,\qquad S_1-2(S_2-6m)-4m=m(m-1)(m-2).
\]
The number with no correction is \(d^2\) minus these and \(m\), or \(m(m-1)(m^2-m+2)/4\). Combining the four half-shape blocks gives the seven-row table.

As arithmetic consistency checks, the table sums to \([n(n-3)/2]^2\) targets, and the sum of its fiber sizes weighted by the listed multiplicities is \((n-3)(n-2)(n-1)^2\), exactly the number of rank-decreasing factor pairs. Adding the rank-preserving count \((n-1)^2(3n-5)\) gives \(|X_n|^2=(n-1)^4\), proving that all ordered pairs are accounted for.

## Verification

The standard-library checker `check_jones.py` independently constructs rank-\(n-2\) diagrams, multiplies them by an explicit three-row connectivity/union-find calculation, and compares each target against the four half-shape formulas and the complete multiplicity table for \(3\le n\le10\). For \(3\le n\le8\), a second recursive Catalan enumeration confirms that every rank-\(n-2\) diagram is represented. The recorded output in `CHECK_OUTPUT.txt` ends in `ALL_CHECKS_PASS`. These are finite cross-checks; the unrestricted result for \(n\ge4\) follows from the branch bijection and indicator-count proof above.

## Relationship to prior work

East and Gray, *Diagram monoids and Graham–Houghton graphs: idempotents and generating sets of ideals* (first public version April 9, 2014), study the Jones rank classes, their Green structure, and the rank-preserving adjacency graph. Their Lemma 9.7 gives the \(|j-k|\le1\) adjacency in the principal factor, which motivates and is consistent with the rank-preserving part here. Their Section 9 establishes ideal-generation and idempotent-generation results but does not supply the prescribed rank-\(n-4\) multiplication fibers or their seven-value distribution. The rank-preserving adjacency is not claimed as novel.

Dolinka and collaborators, *Enumeration of idempotents in planar diagram monoids* (arXiv:1507.04838, initial version July 17, 2015), treat idempotents and interface-graph enumeration in Jones, Kauffman and Motzkin monoids. Their studied counting predicate \(xy=x\) on a single element or idempotent conditions is not the prescribed unrestricted two-factor fiber of \(X_n^2\). The multiplication conventions agree with the three-row gluing used here. The classical Temperley–Lieb monoid generators and planar normal forms are background, not an originality claim.

## Limitations

The theorem is restricted to *two* factors each of rank \(n-2\) in the untwisted planar monoid. It does not count factors of other ranks, arbitrary-length words, scalar loop weights in the Kauffman or Temperley–Lieb algebra, or products restricted to idempotents. It gives no historical priority guarantee against unindexed general multiplication-coefficient formulas. At \(n=3\) the rank-\(n-4\) class does not exist; all four rank-one target diagrams have four such factorizations, separately checked.

## References

1. J. East and R. D. Gray, *Diagram monoids and Graham–Houghton graphs: idempotents and generating sets of ideals*, arXiv:1404.2359, initial public date 2014-04-09, https://arxiv.org/abs/1404.2359. See Section 9, especially Lemma 9.7.
2. I. Dolinka, J. East, A. Evangelou, D. FitzGerald, N. Ham, J. Hyde, N. Loughlin and J. D. Mitchell, *Enumeration of idempotents in planar diagram monoids*, arXiv:1507.04838, initial public date 2015-07-17, https://arxiv.org/abs/1507.04838. See Sections 2–4 for multiplication and idempotent counting.
3. Standard Temperley–Lieb planar-diagram presentation and the Jones relations, as recalled in the references of item 1.
