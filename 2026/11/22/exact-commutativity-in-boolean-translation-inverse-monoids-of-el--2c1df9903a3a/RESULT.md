# Exact commutativity in Boolean translation inverse monoids of elementary two-groups

## Finding
Let \(G=(C_2)^k\) with \(k\ge1\), and put \(n=|G|=2^k\). Let \(E=\mathcal P(G)\) be the Boolean meet-semilattice under intersection, with the regular translation action of \(G\). Define the finite inverse monoid \(W_G=E\rtimes G\) by
\[
(S,a)(T,b)=(S\cap(a+T),a+b).
\]
Let \(M_G\) be the inverse monoid of all restrictions of translations \(x\mapsto x+a\) of \(G\), with all empty restrictions identified as one zero. It is the quotient of \(W_G\) identifying its \(n\) elements \((\varnothing,a)\).

Write \(C(W_G)\) and \(C(M_G)\) for the numbers of **ordered** commuting pairs, including equal pairs and empty-subset cases. If \(k\ge2\), then
\[
C(W_G)=4^n+3(n-1)10^{n/2}+(n-1)(n-2)58^{n/4},
\]
\[
|M_G|=1+n(2^n-1),\qquad
C(M_G)=C(W_G)-2n(n-1)2^n+(n-1)^2.
\]
For \(k=1\), \(C(W_G)=46\), \(C(M_G)=31\), and \(|M_G|=7\); the first formula also holds if its last term is interpreted as zero. In both monoids there are exactly \(2^n\) idempotents. Consequently, as \(k\to\infty\),
\[
\Pr_{u,v\in M_G}(uv=vu)
=\frac{1}{n^2}\left(1+O\bigl(n^2(\sqrt {10}/4)^n\bigr)\right),
\]
and the conditional probability that two uniformly sampled commuting elements of \(M_G\) are both idempotent is
\[
1-O\bigl(n^2(\sqrt {10}/4)^n\bigr).
\]
The implied constants are absolute. The exact appearance of \(10\) and \(58\) reflects the two-element and four-element orbits of one or two independent translations.

## Assumptions and scope
Every subset of \(G\) is allowed, including the empty subset; multiplication in \(W_G\) retains the group label even for the empty subset, while \(M_G\) collapses all empty-label elements to one zero. For a nonempty subset \(S\), \((S,a)\) represents the partial translation with domain \(S-a\) and range \(S\), so distinct pairs with nonempty \(S\) represent different partial maps. The group is elementary abelian of exponent two; the formula is not asserted for arbitrary finite groups or cyclic groups of higher exponent. All probabilities are for independent uniform sampling from the specified finite monoid.

## Proof
Write \(s_x=\mathbf1_{x\in S}\) and \(t_x=\mathbf1_{x\in T}\). Since \(G\) is abelian, the group labels of \((S,a)(T,b)\) and \((T,b)(S,a)\) agree. The pairs commute exactly when
\[
   s_x t_{x+a}=t_xs_{x+b}\quad\text{for every }x\in G. \tag{1}
\]
Fix \(a,b\in G\). All coordinates split into cosets of \(H=\langle a,b\rangle\), and equation (1) couples only coordinates in the same coset. Thus the total number of admissible ordered subset pairs is the corresponding one-coset count raised to \([G:H]\).

There are four disjoint cases.

**Case I, \(a=b=0\).** Equation (1) is automatic; there are \(4^n\) ordered pairs of subsets.

**Case II, exactly one of \(a,b\) is zero.** On each two-element coset, after interchanging \(S,T\) if necessary, the equations are \(s_0(t_0-t_1)=s_1(t_1-t_0)=0\). If \((t_0,t_1)\) is equal, there are four choices of \(S\) for each of its two choices, contributing eight; if the coordinates of \(T\) differ, then \(S\) must be empty, contributing two. The local total is \(10\), and hence the global total is \(10^{n/2}\).

**Case III, \(a=b\ne0\).** On each two-element orbit equation (1) reduces to \(s_0t_1=t_0s_1\). Regarding \((s_i,t_i)\) as vectors in \(\mathbb F_2^2\), this is their determinant-zero condition. There are four pairs when the first vector is zero, and two choices of the second vector for each of the three nonzero first vectors, giving \(4+6=10\). Again the global count is \(10^{n/2}\).

**Case IV, \(a,b\) are distinct and nonzero.** They are independent in the elementary two-group, so \(H\) has four elements. For a given subset \(S\subset H\), equation (1) is a homogeneous system over \(\mathbb F_2\) in the four unknowns \(t_x\), with one row per \(x\in H\):
\[
     s_{x+b}t_x+s_xt_{x+a}=0.
\]
The coefficient matrix has rank \(0,2,4\) for respectively \(1,9,6\) of the sixteen subsets \(S\). More explicitly, the \((|S|,\operatorname{rank})\) frequencies are
\[
(0,0):1,\quad(1,2):4,\quad(2,2):4,\quad
(2,4):2,\quad(3,4):4,\quad(4,2):1.
\]
This table follows by inspecting the possible support sizes and, at support size two, distinguishing the two \(\{x,x+a\}\) pairs from the four other pairs. It can also be checked by row-reducing the displayed four-variable system. A rank-\(r\) homogeneous system has \(2^{4-r}\) solutions. Hence the four-element orbit contributes
\[
 1\cdot16+9\cdot4+6\cdot1=58
\]
choices, and all of \(G\) contributes \(58^{n/4}\).

There is one ordered label pair of type I; there are exactly \(3(n-1)\) pairs of types II and III; and there are \((n-1)(n-2)\) pairs of type IV. Summing yields the formula for \(C(W_G)\).

There are \(n2^n\) labeled elements in \(W_G\), of which \(n\) have empty subset. Every ordered pair containing an empty-subset element commutes (since both products have empty subset and the same group label). Their number is \(2n^2 2^n-n^2\). In \(M_G\) the \(n\) empty-subset elements become one zero, and the number of ordered pairs containing this zero is \(2|M_G|-1=2n2^n-2n+1\). No two nonempty pairs acquire a new commutation relation under this collapse, because their products already have the same group label and equality of their subsets is exactly the criterion both before and after collapse. Taking the difference gives
\[
C(M_G)=C(W_G)-2n(n-1)2^n+(n-1)^2.
\]
All idempotents in \(W_G\) are \((S,0)\), since an idempotent label satisfies \(2a=a\) and therefore \(a=0\); in the quotient these are exactly the partial identities, including zero. Thus both have \(2^n\) idempotents, and all idempotent pairs commute, giving exactly \(4^n\) such pairs.

Finally, \(\sqrt{10}/4<1\) and \(58^{1/4}/4<\sqrt{10}/4\). The exact formula gives
\[
C(M_G)=4^n\left(1+O\bigl(n^2(\sqrt{10}/4)^n\bigr)\right),
\]
while \(|M_G|^2=n^24^n(1+O(2^{-n}))\). Division proves the two asymptotic assertions. All bounds hold uniformly for integer powers \(n=2^k\).

## Verification
The standalone `checker.py` uses the exact commutation equations, counts each fixed translation-label pair by binary Gaussian elimination, independently compares direct semigroup multiplication for \(n=2,4\), and verifies the sixteen-case rank table. Running `python checker.py` yields the accompanying `checker_output.txt`. It checks the full formula for \(n=2,4,8\), including the quotient correction. These computations are finite checks, not substitutes for the orbit decomposition proof for all \(k\).

## Relationship to prior work
Silva and Soares, *Howson's property for semidirect products of semilattices by groups* (2014, arXiv:1412.3048), develop the semilattice-by-group framework and classify a finite-generation property; their Sections 2–3 do not supply a formula for commuting-pair multiplicities of the Boolean regular-translation action. Araújo, Bentz and Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup* (2012, arXiv:1205.1664), give a general commutation criterion for partial bijections and study clique numbers, largest commutative subsemigroups and diameters (not this submonoid's total ordered-pair count). The distinction matters: a result for the full symmetric inverse semigroup does not automatically enumerate pairs inside the restrictive translation submonoid, and their paper's Proposition 2.2 provides a criterion, not the present orbit totals. The present theorem refines these structural contexts with an explicit \(4^n\), \(10^{n/2}\), \(58^{n/4}\) decomposition and an idempotent-dominance limit. An implicit earlier derivation in semidirect-product or partial-bijection literature remains a priority risk.

## Limitations
The formula concerns the regular action of elementary two-groups, not all finite group actions, arbitrary Boolean semilattice automorphisms, or nonabelian translations. It counts commuting pairs but does not determine all element-centralizer sizes or the complete commuting graph. The large-\(k\) asymptotic follows for the sequence \(n=2^k\), not for every integer \(n\). Originality is a best-knowledge comparison, not proof of priority.

## References
- P. V. Silva and F. Soares, *Howson's property for semidirect products of semilattices by groups*, arXiv:1412.3048 (first submitted 2014-12-09), https://arxiv.org/abs/1412.3048.
- J. Araújo, W. Bentz and J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664 (first submitted 2012-05-08), https://arxiv.org/html/1205.1664v1.
- G. Kudryavtseva, *Partial monoid actions and a class of restriction semigroups*, J. Algebra 429 (2015), 342–370, https://doi.org/10.1016/j.jalgebra.2015.01.017 (general W-product/semidirect-product background).
