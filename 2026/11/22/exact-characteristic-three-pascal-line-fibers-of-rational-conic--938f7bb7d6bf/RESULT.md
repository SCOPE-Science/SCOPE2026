# Exact characteristic-three Pascal-line fibers of rational conic hexagons

## Finding

Let \(q=3^m\) with \(m\geq2\). Let \(K\subset\mathbb P^2_{\mathbb F_q}\) be any smooth plane conic. A **rational cyclic hexagon** is an ordered list of six pairwise distinct \(\mathbb F_q\)-points of \(K\), modulo the twelve rotations and reversals. Its **Pascal line** joins the three pairwise opposite-side intersections. Distinct hexagons are counted separately, even if they give the same line.

For a fixed \(\mathbb F_q\)-line of the indicated intersection type with \(K\), the exact numbers of such hexagons are
\[
\boxed{\begin{aligned}
T_q&=\frac{q(q-1)(q-3)(q-6)}{12} &&\text{(tangent)},\\
S_q&=\frac{(q-1)(q-3)(q-5)^2}{12} &&\text{(secant)},\\
E_q&=\frac{(q+1)(q-1)(q-3)^2}{12} &&\text{(exterior)}.
\end{aligned}}
\]
These formulas apply to **every** rational line of the given type, not merely to an average line. All three counts are strictly positive for \(q\geq9\). Hence every \(\mathbb F_q\)-line is a Pascal line of a hexagon on \(K\). The first field for which six distinct conic points exist in characteristic three is \(\mathbb F_9\); its ten tangents, forty-five secants, and thirty-six exterior lines each have, respectively, \(108\), \(64\), and \(240\) preimages.

## Assumptions and scope

The conic is geometrically smooth and defined over \(\mathbb F_q\). All six vertices are rational and pairwise distinct; only dihedral equivalence of their ordering is imposed. Tangent, secant, and exterior mean that the rational line meets the rational conic in, respectively, one double geometric point, two distinct rational points, or two conjugate nonrational geometric points. The theorem applies to all positive integers \(m\geq2\), not just the sample fields in the verification.

Every smooth conic over a finite field has a rational point and is rationally projectively equivalent to the Veronese conic
\[
K_0:\quad XZ-Y^2=0,\qquad P(t)=[t^2:t:1],\quad P(\infty)=[1:0:0].
\]
The action of \(G=\operatorname{PGL}_2(\mathbb F_q)\) on \(K_0\) is sharply triply transitive on ordered triples of distinct rational points. It preserves the three classes of rational lines. Thus it suffices to work with \(K_0\).

## Proof

### 1. A normalized Pascal line

Choose a representative of an ordered sextuple in the form
\[
(P(\infty),P(0),P(1),P(a),P(b),P(c)),
\]
where \(a,b,c\in\mathbb F_q\setminus\{0,1\}\) are pairwise distinct. The sides are the six consecutive vertex-joining lines. Their pairs of opposite-side intersections yield, by explicit cross products, the Pascal-line coefficients
\[
[-c:\ ab+ac-a+c:\ -abc].
\]
These coordinates never vanish simultaneously under the stated distinctness assumptions. Dividing by \(-c\) and setting
\[
z=\frac{a(b-1)}{c}+a+1
\]
gives the line \(X-zY+abZ=0\). Its intersection with \(K_0\) is governed by \(t^2-zt+ab=0\). As the characteristic is three, the discriminant is \(\Delta=z^2-ab\). With the quadratic character \(\chi\) extended by \(\chi(0)=0\), the line is tangent, secant, or exterior precisely as \(\Delta=0\), \(\chi(\Delta)=1\), or \(\chi(\Delta)=-1\).

### 2. The four exclusions

For each ordered pair \(a,b\notin\{0,1\}\), \(a\ne b\), set \(A=a(b-1)\ne0\). The variable \(c\) runs through \(\mathbb F_q\setminus\{0,1,a,b\}\), and the injective substitution \(z=A/c+a+1\) makes \(z\) run through the whole field except the following **four distinct values**:
\[
\begin{array}{c|c}
\text{forbidden point for }c&\text{forbidden value for }z\\\hline
\infty & a+1\\
1 & ab+1\\
a & a+b\\
b & a+1+a(b-1)/b.
\end{array}
\]
Here the symbol \(c=\infty\) records the value missed by the finite reciprocal substitution; it is not an allowed sixth vertex. There are \(P=(q-2)(q-3)\) admissible ordered pairs \((a,b)\).

For any \(u\ne0\) in a field of odd cardinality,
\[
\sum_{z\in\mathbb F_q}\chi(z^2-u)=-1,
\qquad\#\{z:z^2-u=0\}=1+\chi(u).
\]
These are immediate from counting solutions of \(v^2=z^2-u\) via \((z-v)(z+v)=u\). Hence, before removing the four exclusions, the total character sum is \(-P\). The total number of zero discriminants before removal is
\[
\sum_{a,b}(1+\chi(ab))=P+\left(\sum_{a\ne0,1}\chi(a)\right)^2-\sum_{a\ne0,1}\chi(a^2)
=P+1-(q-2)=(q-3)^2.
\]

We now evaluate each omitted value. The following table shows its discriminant, its total quadratic-character contribution summed over the admissible \((a,b)\), and its number of zero-discriminant occurrences:

| Exclusion | Discriminant expression | Character sum | Zeros |
|---|---|---:|---:|
| \(c=\infty\) | \((a+1)^2-ab\) | \(-2(q-3)\) | \(q-3\) |
| \(c=1\) | \((ab-1)^2\) | \((q-3)^2\) | \(q-3\) |
| \(c=a\) | \((a-b)^2\) | \(P\) | \(0\) |
| \(c=b\) | \((1+ka)^2-ab\), \(k=-(b+1)/b\) | \(-2(q-3)\) | \(q-3\) |

For completeness, we justify the two less immediate rows. For \(c=\infty\), fix \(a\) and sum the character of \((a+1)^2-ab\) over all \(b\in\mathbb F_q\); the sum is zero. Removing \(b=0,1,a\) subtracts the characters of \((a+1)^2,(a-1)^2,1-a\). Their sums as \(a\) varies are \(q-3,q-2,-1\); thus the row's sum is \(-2(q-3)\). The discriminant vanishes at \(b=(a+1)^2/a\); this is admissible for exactly \(q-3\) values of \(a\).

For \(c=b\), fix \(b\). The quadratic in \(a\), \((1+ka)^2-ab\), has discriminant \((b-1)^2\) and leading coefficient \(k^2\), provided \(b\ne-1\). Its full-field character sum is then \(-1\). At \(b=-1\) the polynomial is linear, with full-field sum zero. For the omitted \(a=0,1,b\), the discriminants are \(1,(1-b)^3/b^2,0\), so their character contributions are \(1,\chi(1-b),0\); summing over all \(b\ne0,1\) gives \(-2(q-3)\) for the admissible row. When \(b\ne-1\), the two zeros of the quadratic are \(a=b\) (excluded) and \(a=b/(b+1)^2\) (admissible). At \(b=-1\), its only zero is the excluded \(a=b\). Thus the zero count is \(q-3\). For \(c=1\), \(ab=1\) occurs for exactly \(q-3\) admissible pairs, and \(c=a\) contributes a nonzero square because \(a\ne b\).

### 3. The normalized orbit counts

Subtracting the four rows, the number of admissible triples giving a tangent is
\[
N_T=(q-3)^2-3(q-3)=(q-3)(q-6).
\]
The signed secant-minus-exterior count is
\[
N_S-N_E=-P-\bigl[-4(q-3)+(q-3)^2+P\bigr]
=-(q-3)(3q-11).
\]
Every admissible triple yields exactly one of the three line types, so
\[
N_T+N_S+N_E=(q-2)(q-3)(q-4).
\]
Solving these two equations yields
\[
\boxed{N_T=(q-3)(q-6),\quad
N_S=\frac{(q-3)(q-5)^2}{2},\quad
N_E=\frac{(q-3)^2(q-1)}{2}.}
\]

### 4. Passing from triples to fixed-line fibers

Every ordered sextuple is uniquely obtained by applying an element of \(G\) to a normalized sextuple, because an element of \(G\) is determined by its effect on the first three vertices. Here \(|G|=q(q-1)(q+1)\). Every cyclic hexagon corresponds to exactly twelve such ordered sextuples. There are \(q+1\) rational tangents, \(q(q+1)/2\) secants, and \(q(q-1)/2\) exterior lines, each type a single \(G\)-orbit. Therefore the respective numbers per **fixed line** are
\[
\frac{|G|N_T}{12(q+1)},\qquad
\frac{|G|N_S}{12\,q(q+1)/2},\qquad
\frac{|G|N_E}{12\,q(q-1)/2},
\]
which simplify to the asserted expressions. Their positivity for every \(3\)-power \(q\ge9\) proves surjectivity. Since \(K(\mathbb F_3)\) contains only four points, no rational hexagon exists over \(\mathbb F_3\), so the first-field threshold is sharp. This completes the proof.

## Verification

The accompanying standalone script `verify_pascal3.py` implements finite fields by polynomial quotient arithmetic, independently enumerates normalized triples, and checks all three formulas over \(\mathbb F_9,\mathbb F_{27},\mathbb F_{81}\). Over \(\mathbb F_9\), it separately enumerates **all** \(60\binom{10}{6}=12600\) cyclic hexagons using direct projective cross products, without invoking the normalized Pascal-line formula. It verifies that the resulting 91 distinct lines receive the predicted multiplicities, and that the third opposite-side intersection lies on each calculated Pascal line.

| \(q\) | Normalized tangent / secant / exterior triples | Per-line tangent / secant / exterior |
|---:|---|---|
| \(9\) | \(18,48,144\) | \(108,64,240\) |
| \(27\) | \(504,5808,7488\) | \(29484,25168,34944\) |
| \(81\) | \(5850,225264,243360\) | \(3159000,3003520,3325920\) |

The symbolic character-sum proof establishes the theorem for every \(m\ge2\); finite checks are supplementary only. To reproduce, run `python verify_pascal3.py` in a directory containing the supplied script and a Python installation with SymPy.

## Relationship to prior work

Chipalkatti–Da Silva (2022) develop the geometry and degenerations of Pascal lines, including the 60 Pascal symbols and their rational maps; their results over the complex numbers do not give the characteristic-three rational-line fiber counts. Chipalkatti (2023) constructs Pascal varieties and solves *triple prescribed-line* enumerative problems, which are different from the single-line fiber counts over finite fields. Halbeisen–Hungerbühler (2024) classify conic-hexagon twins, again not these finite-field fibers. Fernandes (1993) studies finite oval characterization by Pascal properties, not the multiplicities of six-distinct-vertex hexagons mapping to a rational line.

For comparison, previously determined rational Pascal-fiber formulas in characteristic two and in characteristic at least five have disjoint domains. Their expressions cannot simply be extended by substitution to characteristic three: the cancellations \((ab+1)^2-ab=(ab-1)^2\) and \((a+b)^2-ab=(a-b)^2\) are characteristic-three identities and produce different counts. The present theorem supplies the missing arithmetic characteristic, rather than a corollary of those formulas. Projective duality restates it as a Brianchon-point fiber count for cyclic hexagons of rational tangent lines to the dual conic, without changing the proof or constituting an additional independent result.

## Limitations

The theorem counts rational hexagons with six distinct rational vertices and records the types of their associated lines. It does not classify degenerations, individual-hexagon coincidences among the sixty Pascal symbols, or geometric sextuples defined only over field extensions. It does not establish scheme-theoretic multiplicities of the Pascal morphism. Search-based priority comparison cannot rule out an unindexed older finite-geometry enumeration. Independent mathematical validation has not been performed.

## References

1. J. Chipalkatti and S. Da Silva, *Degenerations of Pascal Lines*, arXiv:2202.12975 (first public 2022-02-25), https://arxiv.org/abs/2202.12975.
2. J. Chipalkatti, *On the Enumerative Geometry of Pascal's Hexagram*, arXiv:2303.10319 (first public 2023-03-18), https://arxiv.org/abs/2303.10319.
3. L. Halbeisen and N. Hungerbühler, *Twins of conic hexagons*, *Journal of Geometry* 115 (2024), article 36, https://doi.org/10.1007/s00022-024-00731-8.
4. O. Fernandes, *On Pascal ovals*, *Journal of the Australian Mathematical Society*, Series A 54 (1993), 61–69, https://doi.org/10.1017/S1446788700036971.
