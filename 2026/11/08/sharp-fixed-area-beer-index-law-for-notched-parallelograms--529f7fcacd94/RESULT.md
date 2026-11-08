# Sharp fixed-area Beer-index law for notched parallelograms

## Finding

For linearly independent vectors \(v_1,v_2\in\mathbb R^2\), define the parallelogram \(P=p_0+[0,1]v_1+[0,1]v_2\). For \(0<s,t<1\), retain the notched polygon
\[
L_{s,t}=p_0+\{xv_1+yv_2:0\le x,y\le1,\ x\le s\text{ or }y\le t\}.
\]
Its area is \((1-q)\operatorname{area}(P)\), where \(q=(1-s)(1-t)\in(0,1)\). Let \(b(L)\) be the Beer index: the probability that the complete straight segment joining two independent area-uniform points of \(L\) is contained in \(L\). Write \(B(s,t)=1-b(L_{s,t})\) for the blocked-pair probability and \(w=st/q\). Define
\[
\Psi(w)=\begin{cases}
 w-\dfrac{w^2}{4}(2-\log w),&0<w\le1,\\[2mm]
 \dfrac{2+\log w}{4},&w\ge1.
\end{cases}
\]
The two branches agree at \(w=1\). For **every** parallelogram, notch pair, and choice of its two adjacent directions,
\[
\boxed{B(s,t)=\frac{2q^2}{(1-q)^2}\Psi\!\left(\frac{st}{q}\right).}\tag{1}
\]
Thus the entire law depends on only the two normalized notch parameters, not the parallelogram's angles or lengths.

For each prescribed deleted area fraction \(q\in(0,1)\), the **unique** maximizer of the blocked-pair probability among all such adjacent-edge rectangular (affine-coordinate) notches is
\[
\boxed{s=t=1-\sqrt q.}\tag{2}
\]
Put \(w_q=(1-\sqrt q)^2/q\). The sharp fixed-area upper bound is
\[
\boxed{B(s,t)\le B_*(q):=\frac{2q^2}{(1-q)^2}\Psi(w_q).}\tag{3}
\]
In particular, the analytic expression switches branches exactly at \(q=1/4\), where \(B_*(1/4)=1/9\). For \(0<q\le1/4\),
\[
B_*(q)=\frac{q^2}{(1-q)^2}\left(1+\log\frac{1-\sqrt q}{\sqrt q}\right),\tag{4}
\]
whereas for \(1/4\le q<1\) formula (3) uses the first branch of \(\Psi\).

The optimum has a **sharp quantitative stability law**. Let
\[
K(q)=\frac{2q}{(1-q)^2}\Psi'(w_q)>0.
\]
For every admissible \(s,t\) with \((1-s)(1-t)=q\),
\[
\boxed{B_*(q)-B(s,t)\ge K(q)\left(\sqrt{1-s}-\sqrt{1-t}\right)^2.}\tag{5}
\]
The coefficient \(K(q)\) is optimal for each \(q\): replacing it by a larger constant makes (5) false for notches sufficiently close to the maximizing symmetric one. Equality in (3) and (5) holds precisely at \(s=t\).

Across all admissible \(q\), every such notched parallelogram has strictly more than one half of point pairs visible, \(b(L_{s,t})>1/2\), and this bound is sharp in the limit \(s=t\downarrow0\):
\[
\lim_{q\uparrow1}B_*(q)=\frac12,\qquad \lim_{q\downarrow0}B_*(q)=0.\tag{6}
\]

## Assumptions and scope

The edge vectors of \(P\) are linearly independent. The removed region is the far-corner affine-coordinate rectangle \((s,1]\times(t,1]\); its boundary convention has zero effect on area-uniform sampling or the probability in (1). The two random points are independent and uniform by **two-dimensional area**, not boundary measure, and the connecting segment is the unconstrained Euclidean segment. All conclusions are affine-invariant under nonsingular transformations. No claim is made for arbitrary holes, freely oriented notches, or multiple obstacles.

## Proof

**1. Affine reduction and the exclusive crossing pair.** Any invertible affine map preserves containment of straight segments and takes normalized area-uniform measure to normalized area-uniform measure. It is enough to consider \(P=[0,1]^2\). Apart from null sets, partition \(L_{s,t}\) into the bottom-right rectangle \(A=(s,1)\times(0,t)\), the top-left rectangle \(C=(0,s)\times(t,1)\), and the bottom-left rectangle \(D=(0,s)\times(0,t)\). Each pair of points belonging to a common horizontal or vertical strip sees each other. In particular, any obstruction must have one point in \(A\) and the other in \(C\). The areas of these arms are \(\operatorname{area}(A)=(1-s)t\) and \(\operatorname{area}(C)=s(1-t)\), and \(\operatorname{area}(L)=1-q\).

**2. Exact segment criterion.** For \(p=(s+X,t-Y)\in A\) and \(p'=(s-U,t+V)\in C\), the four coordinates are independent and uniform on their respective intervals
\[
0<X<1-s,\quad0<Y<t,\quad0<U<s,\quad0<V<1-t.
\]
Along the segment \(p+\tau(p'-p)\), the ordinate first reaches \(t\) at \(\tau_y=Y/(Y+V)\), while the abscissa first reaches \(s\) at \(\tau_x=X/(X+U)\). The segment enters the removed northeast rectangle exactly when \(\tau_y<\tau_x\), equivalently
\[
\boxed{XV>UY.}\tag{7}
\]
Boundary equalities have probability zero. The two orderings of endpoints contribute the factor two in (1).

**3. Product-ratio probability.** Normalize the four coordinates in (7) to independent \(U(0,1)\) variables. Write \(Z_1,Z_2\) for the products of two independent unit uniforms, each independently generated. The crossing event is \(qZ_1>stZ_2\). Since \(-\log Z_i\) has the Gamma distribution with shape two and rate one, the difference \(W=-\log Z_2+\log Z_1\) has the even density
\[
f_W(x)=\frac{1+|x|}{4}e^{-|x|},\qquad x\in\mathbb R.
\]
This follows directly by convolving the densities \(xe^{-x}\mathbf1_{x>0}\): for \(x\ge0\),
\[
\int_0^\infty y(y+x)e^{-y}e^{-(y+x)}\,dy=\frac{1+x}{4}e^{-x}.
\]
Consequently \(\Pr(W>h)=(h+2)e^{-h}/4\) for \(h\ge0\). Taking \(h=\log(st/q)\) or its negative according to the parameter range yields
\[
\Pr(qZ_1>stZ_2)=\begin{cases}
1-\dfrac{w}{4}(2-\log w),&w\le1,\\[1mm]
\dfrac{2+\log w}{4w},&w\ge1.
\end{cases}
\]
Multiplying by \(2\operatorname{area}(A)\operatorname{area}(C)/(1-q)^2=2qst/(1-q)^2\) gives (1).

**4. Exact optimizer.** Fix \(q\), and let \(a=1-s\), \(c=1-t\), so \(ac=q\). The arithmetic-geometric mean inequality gives
\[
st=(1-a)(1-c)=1-a-c+q\le(1-\sqrt q)^2,
\]
with equality if and only if \(a=c=\sqrt q\). The derivative of \(\Psi\) is
\[
\Psi'(w)=\begin{cases}1-\dfrac w4(3-2\log w),&w\le1,\\[1mm]\dfrac1{4w},&w\ge1.\end{cases}
\]
For \(0<w\le1\), \(w(3-2\log w)\le3\); hence \(\Psi'(w)\ge1/4\). For \(w\ge1\), it is also positive. As (1) is strictly increasing in \(w=st/q\) at fixed \(q\), (2) and (3) follow, including strict uniqueness. The branch threshold solves \(w_q=1\), equivalently \(q=1/4\). Substitution gives (4) and \(B_*(1/4)=1/9\).

**5. Sharp stability.** A direct differentiation shows
\[
\Psi''(w)=\begin{cases}-(1-2\log w)/4,&w<1,\\[1mm]-1/(4w^2),&w>1.\end{cases}
\]
Both are negative and they match at \(w=1\). Thus \(\Psi\) is strictly concave on \((0,\infty)\). For \(w\le w_q\), its derivative is at least \(\Psi'(w_q)\), so
\[
\Psi(w_q)-\Psi(w)\ge\Psi'(w_q)(w_q-w).
\]
The identity \(w_q-w=(\sqrt a-\sqrt c)^2/q\) proves (5). It is strict for \(w<w_q\). Along the admissible perturbations \(a=\sqrt q\,e^\epsilon\), \(c=\sqrt q\,e^{-\epsilon}\) as \(\epsilon\to0\), the ratio between the left side of (5) and the squared-root imbalance tends to \(K(q)\) by differentiability. Therefore the constant is best possible.

**6. Universal one-half boundary.** The only blocked pairs lie in opposing arms \(A,C\). Since \(\Pr(\text{cross}\mid A,C)<1\),
\[
B(s,t)<\frac{2|A||C|}{(|A|+|C|+|D|)^2}<\frac12,
\]
where the second strict inequality uses \(D\) of positive area and \(4|A||C|\le(|A|+|C|)^2\). At \(s=t\downarrow0\) the two arm areas become asymptotically equal, \(D\) is negligible relative to either, and \(q/st\to\infty\), so the conditional crossing probability tends to one by step 3. This proves (6) and sharpness.

## Verification

Run `python3 checker.py` using a standard Python 3 interpreter. The checker uses a fixed random seed and only the standard library. It tests the exact formula against an independent segment/rectangle clipping predicate on independently sampled area-uniform point pairs, separately simulates the four-uniform product event, and checks both fixed-area optimality and the sharp-stability inequality over families of asymmetric notches. It reports `L_NOTCH_BEER_INDEX_AND_FIXED_AREA_OPTIMIZER_OK` after successful checks. These are finite diagnostics, not proofs of the continuum or global optimization statements; steps 1–6 provide those proofs.

## Relationship to prior work

The Beer index and its relation to other convexity measures were studied by Balko, Jelínek, Valtr and Walczak (arXiv:1412.1769; public 2014-12-04), building on the earlier Beer-index literature. General algorithms are already known for evaluating geometric visibility probabilities in polygonal environments, including the polygonal-region approach of Buchin, Kostitsyna, Löffler and Silveira (earliest public arXiv:1402.5681, 2014-02-23; expanded Algorithmica 2019) and the general polygon Beer-index algorithm of Abrahamsen and Fredslund-Hansen (arXiv:2208.07106, 2022). García-Pelayo (arXiv:1501.00292, 2015) treats different invariant-line multi-chord distributions for concave polygons. Those general evaluation methods are not claimed as new here. The new claim is the explicit affine two-parameter profile (1) together with the sharp **fixed-deleted-area** optimizer and optimal global rigidity coefficient (2)–(5), neither of which follows directly from the general algorithmic existence statements. Historical priority remains provisional; an unindexed exact special-case calculation is possible.

## Limitations

No independent mathematical or literature audit has been performed. The exact law uses area-uniform sampling, and straight-segment visibility is not an intrinsic geodesic-distance statistic. The optimizer is confined to corner rectangles with sides parallel to the enclosing parallelogram edges, with a **fixed fraction of area removed**. The shape of the outer parallelogram itself is arbitrary, but freely varying obstacle types are not covered. Numerical checks do not extend these quantifiers. More specialized earlier formulae may exist outside the inspected sources.

## References

1. M. Balko, V. Jelínek, P. Valtr, B. Walczak, *On the Beer index of convexity and its variants*, arXiv:1412.1769 (initial public posting 2014-12-04), https://arxiv.org/abs/1412.1769.
2. R. García-Pelayo, *Computation of the multi-chord distribution of convex and concave polygons*, arXiv:1501.00292 (initial public posting 2015-01-01), https://arxiv.org/abs/1501.00292.
3. K. Buchin, I. Kostitsyna, M. Löffler, R. I. Silveira, *Region-Based Approximation of Probability Distributions (for Visibility Between Imprecise Points Among Obstacles)*, Algorithmica 81 (2019), 2682–2715; earlier arXiv:1402.5681, initially posted 2014-02-23, https://arxiv.org/abs/1402.5681 and https://doi.org/10.1007/s00453-019-00551-2.
4. M. Abrahamsen, V. Fredslund-Hansen, *Degree of Convexity and Expected Distances in Polygons*, arXiv:2208.07106 (2022), https://arxiv.org/abs/2208.07106.
