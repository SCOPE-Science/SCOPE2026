# A connected-to-disconnected inverse-sheet transition in a rational planar map

## Finding

Consider the rational plane map
\[
F_{a,b,c,d}(x,y)=\left(x+rac{a x}{1+y^2}+b,\ y+cx+dight).
\]
The topology of its *one-step backward ambiguity* changes sharply when the rational coefficient reaches \(a=-1\). For every \(a<-1\), all targets with three distinct real preimages form **one connected open strip**, bounded by two disjoint ordinary fold curves. At \(a=-1\), this region splits into **two connected components** pinched at a triple inverse point. The precise inverse-count rule and the universal pinch exponents follow below.

## Assumptions and scope

The parameters obey \(b,d\in\mathbb R\), \(c\in\mathbb R\setminus\{0\}\), and \(a\le-1\). The domain and target are the entire real plane; the result concerns **one inverse iteration**, not forward attractors or basin boundaries. For any target \((X,Y)\), write
\[
w=Y-d,\qquad z=c(X-b),\qquad
H_{a,w}(y)=(w-y)\left(1+rac{a}{1+y^2}ight).
\]
Every preimage is uniquely of the form \(x=(w-y)/c\), with \(H_{a,w}(y)=z\). Equivalently, \(y\) is a real root of the monic cubic
\[
P_{a,w,z}(y)=y^3+(z-w)y^2+(1+a)y+z-(1+a)w.
\]
Multiplicity in this text means the number of **distinct real preimages**, except when a repeated algebraic root is explicitly identified.

## Proof

**1. Exact inverse derivative and properness.** Differentiation gives
\[
H'_{a,w}(y)=-rac{Q_{a,w}(y)}{(1+y^2)^2},\qquad
Q_{a,w}(y)=y^4+(2-a)y^2+2awy+(1+a).
\]
Moreover \(\det DF_{a,b,c,d}(x,y)=Q_{a,w}(y)/(1+y^2)^2\) after substituting \(w=y+cx\). For fixed \(w\), the scalar inverse function tends to \(+\infty\) at \(y	o-\infty\) and to \(-\infty\) at \(y	o+\infty\), so it is surjective. The whole planar map is proper: a sequence with bounded images has bounded \(w\); an unbounded source would then have \(|y|	o\infty\) and \(x=(w-y)/c	o\infty\), forcing \(X=x(1+a/(1+y^2))+b\) unbounded, a contradiction. Consequently each map has global topological degree \(+1\), because on any regular fibre the signs alternate \((+,-,+)\), or consist of one positive sign.

**2. The connected three-sheet region for \(a<-1\).** Now
\[
Q''_{a,w}(y)=12y^2+2(2-a)>0,
\qquad Q_{a,w}(0)=1+a<0,
\]
and \(Q(y)	o+\infty\) at either end. Strict convexity proves that \(Q\) has exactly two simple real zeros \(\ell_a(w)<0<r_a(w)\), which vary smoothly with \(w\). Since \(H'=-Q/(1+y^2)^2\), the function \(H\) decreases to its strict local minimum at \(\ell\), rises to its strict local maximum at \(r\), and then decreases to negative infinity. Put \(z_-(w)=H_{a,w}(\ell_a(w))\) and \(z_+(w)=H_{a,w}(r_a(w))\); strict increase between extrema gives \(z_-<z_+\). Horizontal-line intersection yields exactly three real roots for \(z_-<z<z_+\), exactly two distinct roots on either boundary (one repeated), and exactly one otherwise. Each boundary is a graph \(z=z_\pm(w)\) of a smooth function, hence an ordinary fold without a cusp. The open three-sheet set
\[
\mathcal T_a=\{(w,z)\in\mathbb R^2:z_-(w)<z<z_+(w)\}
\]
is homeomorphic to \(\mathbb R	imes(0,1)\) by \((w,s)\mapsto(w,(1-s)z_-(w)+sz_+(w))\), so it is connected. The affine target transformation from \((X,Y)\) to \((w,z)\) preserves this topology.

**3. Critical two-component pinch at \(a=-1\).** The inverse equation and derivative specialize to
\[
H_{-1,w}(y)=rac{(w-y)y^2}{1+y^2},\qquad
Q_{-1,w}(y)=y(y^3+3y-2w).
\]
Let \(q(w)\) be the unique real root of \(q^3+3q=2w\). If \(w
e0\), the two simple critical points are \(0\) and \(q(w)\), with values
\[
H_{-1,w}(0)=0,\qquad
H_{-1,w}(q(w))=rac{q(w)^3}{2},
\]
using \(w=(q^3+3q)/2\). The same monotonicity comparison proves three distinct roots exactly between these values, two at either endpoint, and one elsewhere. As \(q(w)\) has the sign of \(w\), the three-preimage region is the disjoint union
\[
\{w>0,\ 0<z<q(w)^3/2\}\ \cup\{w<0,\ q(w)^3/2<z<0\},
\]
with each half connected and neither touching \(w=0\). At \(w=0\), \(H_{-1,0}(y)=-y^3/(1+y^2)\) is strictly decreasing (away from its horizontal tangent at zero), hence injective. The inverse at \(w=z=0\) is one point of algebraic multiplicity three. The expansion \(q(w)=2w/3+O(w^3)\) yields the cubic pinch width
\[
rac{|q(w)|^3}{2}=rac{4|w|^3}{27}+O(|w|^5).
\]

**4. Sharp opening of the neck.** For \(a=-1-\delta\), \(\delta>0\), and \(w=0\), the two critical points are \(\pm\sqrt{t}\) with
\[
t=rac{a-2+\sqrt{a(a-8)}}{2}=rac{\delta}{3}+O(\delta^2).
\]
Oddness of \(H_{a,0}\) and substitution at \(\sqrt t\) give
\[
z_+(0)-z_-(0)=-2\sqrt t\left(1+rac{a}{1+t}ight)
=rac{4}{3\sqrt3}\delta^{3/2}+O(\delta^{5/2}).
\]
The sign is positive because \(0<t<\delta\) for all sufficiently small positive \(\delta\). Hence the single connected strip opens by the precise \(3/2\)-power law below the critical parameter.

## Verification

The accompanying standalone Python checker uses exact rational arithmetic for the cubic discriminant and exact derivative identities, and independent numerical bisection for sample fold locations and neck scaling. It verifies representative one/three-root regimes and the critical double/triple boundaries. These finite checks supplement, but do not replace, the preceding proofs for every real parameter in the stated domain. Run with \(	exttt{python3 check.py}\).

## Relationship to prior work

The originating article introduces the rational plane map and analyzes fixed points, numerical attractors and their basins, including parameters \(a=-3\) and \(a=-1\). It does not state this inverse-sheet connectivity classification. A related existing calculation for \(a>-1\) has a different critical-set geometry; its assumptions exclude the nonpositive \(1+a\) regime and do not imply the present connected-strip theorem or cubic pinching law. General cubic discriminants and Whitney fold theory are standard background tools, not claimed as original. This result gives an exact parameter boundary for the inverse geometry of the studied family.

## Limitations

The theorem is a complete real-plane one-step inverse-fibre count for \(a\le-1\); it does not identify forward invariant sets, chaotic attractors, multistability, or numerical reconstruction robustness. A full literature-priority search cannot exclude unindexed equivalent analyses. One publisher record dates accepted-manuscript availability to 5 December 2021 and another mirrors a later March 2022 date; the earliest explicitly recorded public date is used here.

## References

- Zhang, Liu, Wei, Jiang and Bi, A class of two-dimensional rational maps with self-excited and hidden attractors, Chinese Physics B 31 (2022), 030503, DOI 10.1088/1674-1056/ac4025. https://doi.org/10.1088/1674-1056/ac4025. Publisher full HTML: https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_3_030503.shtml.
- Publisher publication metadata giving accepted-manuscript online date 2021-12-05: https://cpb.cpsjournals.org/EN/10.1088/1674-1056/ac4025.
- Standard background: one-variable cubic discriminant, regular-value degree, and nondegenerate folds.
