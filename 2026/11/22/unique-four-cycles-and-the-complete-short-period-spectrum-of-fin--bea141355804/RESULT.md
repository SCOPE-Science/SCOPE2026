# Unique four-cycles and the complete short-period spectrum of finite reduced-ring structure graphs

## Finding

For any field \(K\), let \(\Phi_K:K^2\to K^2\) be the Vieta map
\[
\Phi_K(a,b)=(a+b,ab).
\]
The set of fixed points is exactly \(\{(a,0):a\in K\}\). There are no periodic points of least period \(2\) or \(3\). There is precisely one four-cycle when the characteristic is not \(2\) and \(-1\) has a square root \(i\in K\), namely
\[
(-1,1+i)\longrightarrow(i,-1-i)\longrightarrow(-1,1-i)
\longrightarrow(-i,-1+i)\longrightarrow(-1,1+i).
\]
Otherwise there are no four-cycles. The two choices of \(i\) describe the same cycle.

In particular, let \(R=\prod_{j=1}^r\mathbb F_{q_j}\) be a nonzero finite reduced commutative ring, with \(r\geq1\). Define \(\varepsilon_j=1\) when \(q_j\equiv1\pmod4\), and \(\varepsilon_j=0\) otherwise. The number \(C_m(R)\) of directed cycles of least length \(m\) in its structure graph obeys
\[
C_1(R)=|R|,\quad C_2(R)=C_3(R)=0,\quad
C_4(R)=\frac14\left(\prod_{j=1}^r(q_j+4\varepsilon_j)-\prod_{j=1}^r q_j\right).
\]
For example, \(\mathbb F_5\times\mathbb F_5\) has exactly \(14\) four-cycles and \(25\) loops.

## Assumptions and scope

A structure graph is the functional directed graph whose vertices are the ordered pairs \((a,b)\in R^2\), with edge \((a,b)\to(a+b,ab)\). A cycle is counted once up to cyclic rotation; its period is its least positive return time. Fields may have arbitrary characteristic for the first claim. The product enumeration requires the ring to be finite, unital, commutative, reduced, and nonzero. In that case the standard structure theorem gives a finite direct product of fields.

## Proof

Write \(x,y\) for two commuting indeterminates, and define recursively \((A_0,B_0)=(x,y)\) and \((A_{n+1},B_{n+1})=(A_n+B_n,A_nB_n)\) over \(\mathbb Z[x,y]\). Fixed-point equations give \(y=0\). Since \(A_2-x=y(x+1)\) and \(B_2-y=y(x(x+y)-1)\), there are no extra solutions of \(\Phi^2(x,y)=(x,y)\) over a field: if \(y\ne0\), the first equation forces \(x=-1\), and the second then forces \(y=0\), a contradiction.

For period three, factor out \(y\) from each return equation. Exact integral elimination gives
\[
\operatorname{Res}_y\left(\frac{A_3-x}y,\frac{B_3-y}y\right)
=x(x^2+x+1)^2.
\]
The first factor is explicitly \((A_3-x)/y=x^2+xy+x+1\). If \(y\ne0\), the resultant forces either \(x=0\), which makes the first factor \(1\), or \(x^2+x+1=0\), which makes it \(xy\ne0\). Both are contradictions. This argument remains valid in every characteristic since the elimination identity is an integer-polynomial identity.

For period four, again divide the return equations by \(y\). The first factorization is
\[
\frac{A_4-x}y=(x+1)H(x,y),\qquad
H=x^2y+x^2+xy^2+xy+1.
\]
An exact Sylvester determinant over \(\mathbb Z[x]\) gives the identity
\[
\operatorname{Res}_y\left(H,\frac{B_4-y}y\right)=x^3(x^2+1)^4.
\]
If \(y\ne0\), the case \(x=0\) is impossible as \(H(0,y)=1\). Thus any four-periodic point has \(x=-1\) or \(x^2=-1\). When \(x=-1\), the second return equation reduces to
\[
\left.\frac{B_4-y}y\right|_{x=-1}
=-y(y^2-2y+2),
\]
so a nonzero \(y\) must be \(1\pm i\), where \(i^2=-1\). In characteristic \(2\) this equation has only \(y=0\), hence no four-cycle. In other characteristics, for \(x^2=-1\) the first return equation reduces modulo \(x^2+1\) to \(y((x-1)y-2)=0\); since \(x\ne1\) and \(y\ne0\), it forces \(y=-1-x\). Direct substitution in the second return equation confirms these two points. These are precisely the four points in the displayed cycle, which are distinct when the characteristic differs from \(2\). Thus every four-cycle is the displayed one.

For a finite reduced commutative ring, the Vieta map acts coordinatewise on its field factors. Each field factor has \(q_j\) period-one points and \(4\varepsilon_j\) period-four points, with no other periodic points whose period divides \(4\). Therefore the fourth iterate has \(\prod_j(q_j+4\varepsilon_j)\) fixed points, of which \(\prod_jq_j\) have least period one. All remaining points have least period four, so division by four proves the formula. No periods two or three occur in a product because none occurs in any field factor.

## Verification

Run `python CHECK.py` with Python 3 and SymPy installed. It checks both integer-polynomial resultant identities exactly, the required specializations, all prime fields of orders \(2\) through \(101\), binary extension fields of orders \(2,4,8,16,32,64\), and the field of order \(9\). It also checks the combinatorial product-count formulas. The symbolic identities—not the finite enumeration—justify all-field statements; the computation is independently reproducible algebraic verification of the exact identities.

## Relationship to prior work

Chernev and Chernev (arXiv:2611.07521v1, November 5, 2026) study the same Vieta functional graph, establish a four-cycle when the characteristic is an odd prime congruent to one modulo four, and formulate a classification problem for rings with no nontrivial cycles. Their Section 5 supplies an existence argument, not the uniqueness or an exact all-reduced-ring four-cycle count. Lipkovski's 2017 structural-graph paper and its 2012 antecedent address short cycles, including length-three criteria and numerical examples; their already established absence criteria are treated as prior work here. The distinct contribution is the complete number and shape of four-cycles over every field and an exact short-period census for every finite reduced commutative ring.

## Limitations

This result does not classify periods greater than four; in particular it does not resolve the global no-nontrivial-cycle conjecture for prime fields or characteristic-two extensions. Nonreduced or noncommutative rings can have two-cycles, so the product formula does not extend without its hypotheses. Search coverage does not prove historical novelty: older or unindexed computations of short cycles could overlap the four-cycle uniqueness statement. Independent mathematical validation has not been performed.

## References

1. A. M. Chernev and N. A. Chernev, *On the Connected Components of Structure Graphs of Associative Rings*, arXiv:2611.07521v1 (first public November 5, 2026), https://arxiv.org/html/2611.07521v1.
2. A. T. Lipkovski, *Structure Graphs of Rings: Definitions and First Results*, J. Math. Sci. 225 (2017), 658–665, https://doi.org/10.1007/s10958-017-3484-3.
3. A. T. Lipkovski, *Digraphs associated with finite rings*, Publ. Inst. Math. 92 (2012), 35–41, https://doi.org/10.2298/PIM1206035L.
