# A connected-to-disconnected inverse-sheet transition in a rational planar map

## Finding

Consider the rational plane map
\[
F_{a,b,c,d}(x,y)=\left(x+\frac{a x}{1+y^2}+b,\ y+cx+d\right).
\]
For every \(a<-1\), the targets with three distinct real preimages form one connected open strip bounded by two disjoint ordinary fold curves. At \(a=-1\), the three-preimage region has two connected components pinched at a target with a triple inverse root. The precise inverse counts and pinch exponents are given below.

## Assumptions and scope

Let \(b,d\in\mathbb R\), \(c\in\mathbb R\setminus\{0\}\), and \(a\le-1\). The domain and target are the entire real plane. The result concerns one inverse iteration, not forward attractors or basin boundaries. For a target \((X,Y)\), set
\[
w=Y-d,\qquad z=c(X-b),\qquad
H_{a,w}(y)=(w-y)\left(1+\frac{a}{1+y^2}\right).
\]
Every preimage is uniquely of the form \(x=(w-y)/c\), with \(H_{a,w}(y)=z\). Equivalently, \(y\) is a real root of
\[
P_{a,w,z}(y)=y^3+(z-w)y^2+(1+a)y+z-(1+a)w
=-(1+y^2)(H_{a,w}(y)-z).
\]
Preimage counts below refer to distinct real preimages. Algebraic multiplicities are specified separately.

## Proof

**1. Exact inverse derivative and properness.** Differentiation gives
\[
H'_{a,w}(y)=-\frac{Q_{a,w}(y)}{(1+y^2)^2},\qquad
Q_{a,w}(y)=y^4+(2-a)y^2+2awy+(1+a).
\]
In source coordinates \((w,y)=(y+cx,y)\) and target coordinates \((w,z)=(Y-d,c(X-b))\), the map is \((w,y)\mapsto(w,H_{a,w}(y))\). The respective coordinate changes have determinants \(c\) and \(-c\), so in the original coordinates \(\det DF_{a,b,c,d}(x,y)=-H'_{a,w}(y)=Q_{a,w}(y)/(1+y^2)^2\) at \(w=y+cx\).

For fixed \(w\), \(H\) tends to \(+\infty\) as \(y\to-\infty\) and to \(-\infty\) as \(y\to+\infty\), giving surjectivity. The planar map is proper: any unbounded source sequence with bounded image has a subsequence escaping to infinity. On that subsequence \(w=y+cx\) remains bounded, so \(|y|\to\infty\) and \(|x|=|(w-y)/c|\to\infty\). But then \(|X|\to\infty\) because the rational factor multiplying \(x\) tends to one, a contradiction. The root counts and monotonicity below show that the Jacobian signs on a regular fibre are \((+,-,+)\) in increasing \(y\), or one positive sign. Thus the proper map has degree \(+1\).

**2. The connected three-sheet region for \(a<-1\).** In this case
\[
Q''_{a,w}(y)=12y^2+2(2-a)>0,\qquad Q_{a,w}(0)=1+a<0.
\]
Since \(Q(y)\to+\infty\) at either end, strict convexity gives exactly two simple real zeros \(\ell_a(w)<0<r_a(w)\), which vary smoothly with \(w\). The function \(H\) decreases to its strict local minimum at \(\ell_a(w)\), increases to its strict local maximum at \(r_a(w)\), then decreases to \(-\infty\). Write
\[
z_-(w)=H_{a,w}(\ell_a(w)),\qquad z_+(w)=H_{a,w}(r_a(w)).
\]
Strict increase between the extrema gives \(z_-<z_+\). There are three distinct preimages for \(z_-<z<z_+\), two on either boundary (one double root), and one otherwise. At either critical point, \(H''=-Q'/(1+y^2)^2\ne0\); in the coordinates of step 1 this is the ordinary fold condition. The open three-preimage set
\[
\mathcal T_a=\{(w,z)\in\mathbb R^2:z_-(w)<z<z_+(w)\}
\]
is homeomorphic to \(\mathbb R\times(0,1)\) by \((w,s)\mapsto(w,(1-s)z_-(w)+sz_+(w))\), so it is connected. The affine target change preserves this topology.

**3. Critical two-component pinch at \(a=-1\).** Here
\[
H_{-1,w}(y)=\frac{(w-y)y^2}{1+y^2},\qquad Q_{-1,w}(y)=y(y^3+3y-2w).
\]
Let \(q(w)\) be the unique real root of \(q^3+3q=2w\). If \(w\ne0\), the two simple critical points are \(0\) and \(q(w)\), with values \(0\) and \(q(w)^3/2\), respectively; the latter identity uses \(w=(q^3+3q)/2\). There are three distinct roots exactly between these values, two at either endpoint (one double root), and one elsewhere. Both extrema are ordinary folds for \(w\ne0\). Since \(q(w)\) has the sign of \(w\), the three-preimage region is the disjoint union
\[
\{w>0,\ 0<z<q(w)^3/2\}\ \cup\ \{w<0,\ q(w)^3/2<z<0\}.
\]
Each half is connected by the same interpolation used in step 2, and no three-preimage target lies on \(w=0\). At \(w=0\), \(H_{-1,0}(y)=-y^3/(1+y^2)\) is strictly decreasing, with a horizontal tangent only at zero. Hence there is one distinct preimage for every target on this line. At \(w=z=0\) the cubic is \(P(y)=y^3\), giving a triple root. This is not an ordinary Whitney cusp: the differential of the Jacobian determinant vanishes at that point, as is seen from \(Q_{-1,w}(y)=y^4+3y^2-2wy\). The expansion \(q(w)=2w/3+O(w^3)\) gives the cubic pinch width
\[
\frac{|q(w)|^3}{2}=\frac{4|w|^3}{27}+O(|w|^5).
\]

**4. Sharp opening of the neck.** For \(a=-1-\delta\), \(\delta>0\), and \(w=0\), the two critical points are \(\pm\sqrt t\), where
\[
t=\frac{a-2+\sqrt{a(a-8)}}{2}
=\frac{\delta}{3}-\frac{4\delta^2}{27}+O(\delta^3).
\]
Indeed, \(t\) is the positive root of \(t^2+(3+\delta)t-\delta=0\). Oddness of \(H_{a,0}\) then gives
\[
z_+(0)-z_-(0)=-2\sqrt t\left(1+\frac{a}{1+t}\right)
=\frac{2\sqrt t(\delta-t)}{1+t}
=\frac{4}{3\sqrt3}\delta^{3/2}+O(\delta^{5/2}).
\]
This is positive since \(\delta=t(t+3+\delta)>t\). Thus the section at \(w=0\) opens with the stated \(3/2\) power below the critical parameter.

## Verification

The source package includes a standalone Python checker, `check.py`, using exact rational arithmetic for the cubic discriminant and derivative identities, and numerical bisection at sample fold locations. These are finite checks, not the proof for all parameters. Independently, the cleared cubic and Jacobian identities can be checked by symbolic expansion and differentiation. For \((a,w,z)=(-3/2,0,0),(-3/2,0,8),(-1,2,0),(-1,2,1/4),(-1,2,1/2),(-1,-2,-1/4),(-1,0,0)\), exact real-root isolation of \(P\) gives distinct counts \(3,1,2,3,2,3,1\); the third, fifth and seventh cases have respectively a double, double and triple root.

## Relationship to prior work

The originating Zhang et al. article defines this exact map in Eq. (1) and analyzes fixed points, numerical attractors and their basins, including parameters \(a=-3\) and \(a=-1\). It does not state the three-preimage connectivity classification. A same-map calculation for \(a>-1\) uses positivity of \(1+a/(1+y^2)\); this excludes the parameter regime of the theorem. In particular it cannot divide by that factor at the zeros responsible for the transition. General cubic discriminants and fold theory are standard background, not claimed as original.

## Limitations

This is a one-step real inverse-fibre classification for \(a\le-1\); it does not identify forward invariant sets, chaotic attractors, multistability, or numerical reconstruction robustness. The fold and width formulas concern the stated affine target coordinates. The literature comparison cannot exclude an unindexed equivalent inverse analysis. The publisher records an accepted-manuscript online date of 5 December 2021 and a 2022 issue date for the originating article.

## References

- Zhang, Liu, Wei, Jiang and Bi, *A class of two-dimensional rational maps with self-excited and hidden attractors*, Chinese Physics B 31 (2022), 030503. https://doi.org/10.1088/1674-1056/ac4025. Publisher full HTML: https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_3_030503.shtml.
- Publisher metadata giving the accepted-manuscript online date 2021-12-05: https://cpb.cpsjournals.org/EN/10.1088/1674-1056/ac4025.
- Indexed same-map calculation for \(a>-1\): `dce0a6248844`.
- Standard background: one-variable cubic discriminant, regular-value degree, and nondegenerate folds.
