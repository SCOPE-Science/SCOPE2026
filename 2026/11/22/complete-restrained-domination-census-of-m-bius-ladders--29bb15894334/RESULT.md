# Complete restrained-domination census of Möbius ladders

## Finding

Let \(M_{2n}\) be the labelled Möbius ladder with vertices \(\mathbb Z/(2n)\mathbb Z\), cycle edges joining consecutive residues and chords joining residues differing by \(n\), for each integer \(n\ge3\). Let \(R_n(z)=\sum_{S}z^{|S|}\), where \(S\) ranges over **all** restrained dominating vertex sets: each vertex outside \(S\) has at least one neighbor in \(S\) and at least one neighbor outside \(S\).

Set
\[
\begin{aligned}
D_+(y,z)={}&1-yz-yz^2-y^2z-2y^2z^2+y^2z^3\\
 &-2y^3z^2-2y^3z^3-y^3z^4+y^5z^3+y^6z^4,\\
D_-(y,z)={}&1-yz+y^2z+y^2z^2-y^3z^2.
\end{aligned}
\]
Then the **entire cardinality polynomial**, for every \(n\ge3\), is
\[
\boxed{R_n(z)=[y^n]\left(-y\frac{\partial}{\partial y}\log\frac{D_+(y,z)}{D_-(y,z)}\right).}
\]
Here \([y^n]\) denotes formal coefficient extraction; the logarithm is expanded at \(y=0\). No infinite numerical approximation is involved.

The restrained-domination number and number \(m_n\) of minimum sets are
\[
\boxed{\gamma_r(M_{2n})=\begin{cases}
 n/2,&n\equiv2\pmod4,\\
 n/2+1,&n\equiv0\pmod4,\\
 (n+1)/2,&n\text{ odd},
\end{cases}}
\]
and
\[
\boxed{m_n=\begin{cases}
4,&n\equiv2\pmod4,\\
n^2,&n\equiv0\pmod4,\\
2n,&n\text{ odd},\ n\ge5,\\
9,&n=3.
\end{cases}}
\]
The cardinality minimum and efficient-domination existence criterion have antecedents in the literature, as acknowledged below. The substantive census claim is the full polynomial and the exact minimum-set multiplicities, including the quadratic residue class.

## Assumptions and scope

Every graph here is finite, simple, undirected, and labelled. The index \(n\) counts antipodal chords or twisted ladder columns; the graph has \(2n\) vertices and is cubic for \(n\ge3\). No assertion is made for the degenerate small indices \(n=1,2\). Cardinalities refer to distinct vertex subsets, not colorings, equivalence classes under automorphisms, or choices of witnesses.

Write a column as two bits \(b=(b_0,b_1)\in\{0,1\}^2\), with \(b_r=1\) meaning the row-\(r\) vertex is selected. Number the \(n\) columns from \(0\) to \(n-1\). The horizontal boundary is twisted: after the final column the two rows exchange. Let \(\tau(b_0,b_1)=(b_1,b_0)\).

## Proof

**1. Local equivalence.** Each vertex has three neighbors. For the triple of consecutive columns \((a,b,c)\), the middle column satisfies restrained domination exactly when, for each row \(r\in\{0,1\}\), either \(b_r=1\), or
\[
1\le a_r+b_{1-r}+c_r\le2.
\]
The lower inequality requires a selected neighbor; the upper inequality ensures at least one unselected neighbor. Thus this test is necessary and sufficient, not merely a relaxation.

**2. Exact transfer and twist.** On the sixteen ordered-pair states \((a,b)\), define a matrix \(T(z)\): its entry from \((a,b)\) to \((b,c)\) equals \(z^{b_0+b_1}\) if the middle-column test holds, and zero otherwise. Let \(J\) act by \(J(a,b)=(\tau(a),\tau(b))\). The local rule is invariant under swapping rows, so \(JT=TJ\).

A closed walk contributing to \(\operatorname{tr}(JT^n)\) is exactly a sequence of \(n\) columns with the boundary constraints \(c_{-1}=\tau(c_{n-1})\) and \(c_n=\tau(c_0)\). Every legal selected subset corresponds to one such walk, and each middle-column weight occurs once. Therefore
\[
R_n(z)=\operatorname{tr}(JT(z)^n).
\]
The involution \(J\) has plus/minus eigenspaces of dimensions ten and six. Let \(T_+\) and \(T_-\) be the corresponding restrictions. By the explicit rule above, direct finite determinant expansion gives
\[
\det(I-yT_+)=D_+(y,z),\qquad \det(I-yT_-)=D_-(y,z).
\]
This finite polynomial identity is independently specified and checked symbolically in the included `verify_transfer.py`; no unstated external lemma is needed. Since
\[
-\log\det(I-yA)=\sum_{j\ge1}\frac{y^j}{j}\operatorname{tr}(A^j)
\]
for any finite matrix \(A\) over a characteristic-zero commutative ring, and the eigenvalue of \(J\) is plus one on the first space and minus one on the second, the displayed coefficient formula follows.

**3. Minimum and exact leading coefficient.** The direct domination bound is \(2n\le4|S|\) because the closed neighborhood of each selected vertex covers at most four vertices. To determine whether this bound is attained and count all minimum sets, introduce \(z=t^2\), \(y=w/t\), and the formal series
\[
L(w,t)=\log\frac{D_-(w/t,t^2)}{D_+(w/t,t^2)}.
\]
Both denominator constant terms in \(t\) are invertible formal series in \(w\); hence this is a formal nonnegative-power series in \(t\), and
\[
t^{-n}R_n(t^2)=[w^n]w\frac{\partial L}{\partial w}.
\]
Write \(L=L_0+tL_1+t^2L_2+O(t^3)\). Direct expansion of the two explicit finite polynomials yields
\[
\begin{aligned}
L_0(w)&=\log\frac{1+w^2}{1-w^2},\\
L_1(w)&=\frac{w^3(3-w^2)}{1-w^2},\\
L_2(w)&=\frac{w^2(w^{10}-w^8-3w^6+3w^4+2w^2+6)}{2(1-w^2)^2(1+w^2)}.
\end{aligned}
\]
The \(w\)-derivative of \(L_0\) has coefficient four at exactly the degrees congruent to two modulo four; it has coefficient zero at all positive degrees divisible by four and all odd degrees. The first odd-degree contribution comes from \(L_1\): its coefficient is three at degree three, and two at every odd degree at least five. The projection of \(L_2\) onto degrees divisible by four is exactly
\[
\frac{L_2(w)+L_2(iw)}2=\frac{4w^4}{(1-w^4)^2},\qquad i^2=-1,
\]
so the coefficient of \(w^{4m}\) in \(L_2\) equals \(4m\) for each integer \(m\ge1\). Differentiating multiplies the coefficient by the degree \(n\). Thus the respective first nonzero coefficients in \(R_n(z)\) are \(4\), \(n^2\), \(2n\), or nine in the four indicated cases. No lower cardinality can occur because no negative power of \(t\) occurs in \(L\), and the first nonzero terms have the stated degrees. This proves both the minimum and its exact multiplicity for every \(n\ge3\).

## Verification

The independent direct graph checker `verify_direct.py` enumerates every subset of the \(2n\) labelled vertices for \(3\le n\le10\), computing eligibility from the original chord-and-cycle adjacency rather than the transfer. The second program `verify_transfer.py` constructs the twisted automaton from the local bit rule, verifies both determinant identities over exact symbolic polynomials, checks the leading-coefficient algebra, and computes the cardinality distribution through \(n=40\). Both completed successfully. Examples of the full polynomials are
\[
\begin{aligned}
R_3(z)&=9z^2+18z^3+9z^4+z^6,\\
R_4(z)&=16z^3+38z^4+24z^5+12z^6+z^8.
\end{aligned}
\]
These numerical checks are corroborations; the finite transfer identity and formal series argument above establish the infinite assertion.

## Relationship to prior work

Restrained domination is a classical graph parameter; Henning's 1999 work gives structural general results. Knor and Potočnik (2012), Lemma 2.2, explicitly establish that \(M_{2n}\) has an efficient dominating set if and only if \(n\equiv2\pmod4\). That existence threshold is not claimed as new here. Hemalatha, Chandrakala, Sooryanarayana and Kumar (2023), Theorem 5.3, discuss numerical domination and restrained-domination parameters of Möbius ladders. Their paper does not present the complete restrained-domination cardinality polynomial or the number of optimal subsets. The coefficient formula and multiplicity calculation here do not rely on their printed case distinction.

Other exact Möbius-ladder results concern one-limited domination, a different predicate: one-limited sets restrict neighbors outside the selected set *of selected vertices*, whereas restrained domination constrains neighbors *of unselected vertices*. Neither condition implies the other in general. Their optima and polynomials therefore do not determine the enumerator above. An ordinary circular ladder has untwisted closure and a trace \(\operatorname{tr}(T^n)\) instead of \(\operatorname{tr}(JT^n)\); the minus sector in the present result measures precisely the effect of the twist.

## Limitations

This is an exact result for the indicated labelled graph family only; it is not a general formula for arbitrary cubic graphs or any other domination variant. It does not classify the symmetry orbits or the reconfiguration graph of the optimal sets. Finite checks alone do not certify the infinite case; that part rests on the explicit transfer identity and formal algebra. The published 2023 numerical treatment contains overlapping or ambiguous printed residue cases, so its exact numerical implications were not assumed. Priority outside the inspected published papers and accessible indexed records cannot be ruled out; an independent scholarly audit has not been performed.

## References

1. M. A. Henning, *Graphs with large restrained domination number*, Discrete Mathematics 197–198 (1999), 415–429. DOI: https://doi.org/10.1016/S0012-365X(99)90095-X . Public publication date recorded as 1999-02-28.
2. M. Knor and P. Potočnik, *Efficient domination in cubic vertex-transitive graphs*, European Journal of Combinatorics 33 (2012), 1755–1764. Author-hosted preprint: https://www.math.sk/knor/PREP/p076.pdf . DOI: https://doi.org/10.1016/j.ejc.2012.04.007 . Especially Lemma 2.2.
3. N. C. Hemalatha, S. B. Chandrakala, B. Sooryanarayana and M. Vishu Kumar, *Restrained and Total Restrained Domination of Ladder Graphs*, Communications in Mathematics and Applications 14 (2023), 1311–1323. https://www.rgnpublications.com/journals/index.php/cma/article/download/2569/1604/9079 . Especially Theorem 5.3.
