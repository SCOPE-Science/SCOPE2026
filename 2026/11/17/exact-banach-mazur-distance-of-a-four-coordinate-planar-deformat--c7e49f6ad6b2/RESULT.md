# Exact Banach–Mazur distance of a four-coordinate planar deformation

## Finding
For \(0\le t\le1\), equip \(\mathbb R^2\) with the norm
\[
N_t(x,y)=\max\{|x|,|y|,|x+ty|,|tx+y|\}.
\]
Writing \(X_t=(\mathbb R^2,N_t)\), its **exact real Banach–Mazur distance** to the two-dimensional supremum norm is
\[
\boxed{d_{\mathrm{BM}}(X_t,\ell_\infty^2)=1+\tfrac t2.}
\]
An optimal isomorphism to \(\ell_\infty^2\) is \(L_t(x,y)=(x+k y,kx+y)\), where \(k=t/(2+t)\). Consequently this family realizes a linear, strictly increasing path of distances from \(1\) (square) to \(3/2\) (affine-regular hexagon); the best interior distance, not just its small-parameter expansion, is determined.

## Assumptions and scope
All spaces and maps are real. Here \(t\in[0,1]\), and \(d_{\mathrm{BM}}(X,Y)=\inf_{L\text{ invertible}}\|L:X\to Y\|\|L^{-1}:Y\to X\|\). The proof includes endpoints and applies to unrestricted real linear isomorphisms, without assuming that an optimizer commutes with a coordinate symmetry.

## Proof
Put \(c=1+t/2\). The unit ball \(B_t\) has vertices \(\pm(1,0),\pm(0,1),\pm(1,-1),\pm((1+t)^{-1},(1+t)^{-1})\); its polar \(B_t^\circ\) has eight cyclic vertices
\[
v_0=(1,0),\ v_1=(1,t),\ v_2=(t,1),\ v_3=(0,1),\quad v_{i+4}=-v_i\ (0\le i\le3).
\]
For an invertible matrix \(L\) with rows \(r=(a,b)\), \(s=(e,f)\), let \(\Delta=af-be\). Define
\[
M(r,s)=\max\big\{|f|+|b|,\ |e|+|a|,\ |f-te|+|b-ta|,\ |tf-e|+|tb-a|\big\}.
\]
The exact operator norm identity is \(\|L^{-1}:\ell_\infty^2\to X_t\|=M(r,s)/|\Delta|\), while \(\|L:X_t\to\ell_\infty^2\|=\max\{N_t^*(r),N_t^*(s)\}\). It suffices to prove \(M(r,s)\ge c|\Delta|\) for both rows in \(B_t^\circ\): normalizing an arbitrary \(L\) to norm one yields this inequality. Conversely, enlarging a nonzero row separately until it reaches the polar boundary weakly decreases the ratio \(M/|\Delta|\), since each term in \(M\) is a sum of one homogeneous absolute expression in each row. Thus it suffices to take \(r,s\) on polar edges.

Here is an exact finite-cell lemma with a reproducible rational-polynomial certificate. Number the edges \(E_i=[v_i,v_{i+1}]\), indices modulo eight. Expand the four absolute-value sums defining \(M\) into the sixteen affine branches: first \(\epsilon f+\eta b\), then \(\epsilon e+\eta a\), then \(\epsilon(f-te)+\eta(b-ta)\), then \(\epsilon(tf-e)+\eta(tb-a)\), within each group in the sign order \((+,+),(+,-),(-,+),(-,-)\). Their maximum equals \(M\). For any edge pair \((E_i,E_j)\) not marked `-` in the following table, the displayed zero-based branch index \(h\) obeys \(L_h(r,s)\ge c\Delta\) **throughout that entire edge pair**, for every \(t\in[0,1]\):

```text
  j= 0  1  2  3  4  5  6  7
 i=0  4  4  -  -  6  0  0  0
 i=1  0  0  0  -  6  2  0  0
 i=2  0  0  0  -  -  2  2  0
 i=3  0  0  0  8  -  -  - 10
 i=4  5  0  0  0  7  7  -  -
 i=5  5  1  0  0  1  3  3  -
 i=6  -  1  1  0  1  1  3  -
 i=7  -  -  -  9  1  1  1 11
```

Indeed, with the two edge parameters in \([0,1]\), \(L_h-c\Delta\) is separately affine, so it is the convex bilinear interpolation of its four corner values. At those corners, each value is a rational polynomial in \(t\). The attached `checker.py` computes **exactly** its degree-eight Bernstein coefficients on each of eight closed rational subintervals of \([0,1]\); all 13,824 coefficients are nonnegative. The elementary Bernstein basis \(\binom8k u^k(1-u)^{8-k}\) is nonnegative for \(0\le u\le1\), proving every corner inequality simultaneously for the continuum of real parameters, not just finitely sampled parameters. The checked table, symbolic formulas and interval decomposition are part of the proof certificate.

The sixteen dashed cells reduce, under \((a,b)\leftrightarrow(b,a)\), independent row sign changes, and interchange of the two rows, to three cases: \((E_0,E_2)\), \((E_0,E_3)\), \((E_1,E_3)\). All those operations preserve \(M\) and \(|\Delta|\); proving \(M\ge c\Delta\) is enough, since interchanging rows changes the sign of \(\Delta\).

For \((E_0,E_2)\), write \(r=(1,tu)\), \(s=(tw,1)\), \(0\le u,w\le1\). Then \(\Delta=1-t^2uw\), and the four candidate terms in \(M\) are
\[
1+tu,\quad1+tw,\quad1+t(1-u)-t^2w,\quad1+t(1-w)-t^2u.
\]
Put \(h=1/(2+t)\). If \(u\ge h\), average the first and third terms to obtain \(c-t^2w/2\ge c\Delta\). If \(w\ge h\), average the second and fourth terms. If both are at most \(h\), the third term minus \(c\Delta\) is decreasing in each variable (its partial derivatives are at most \(-t+t^2/2\) and \(-t^2/2\)), hence is at least its zero value at \((h,h)\). The case \(t=0\) follows directly.

For \((E_0,E_3)\), write \(r=(1,tu)\), \(s=(-v,1-v)\). Then \(\Delta=1-v+tuv\le1\). Three candidates in \(M\) are \(A=1-v+tu\), \(B=1+v\), and \(C=1+t-(1-t)v-tu\). If \(u\le1/c\), \((A+C)/2-c\Delta=t(1-cu)v\ge0\). Otherwise \(A\ge c\Delta\) for \(v\le (u-1/2)/(cu-1/2)\), whereas \(B\ge c\Delta\) for \(v\ge t/[2(1+c(1-tu))]\). The first threshold is at least the second: cross-multiplication gives the concave quadratic in \(u\),
\[
F_t(u)=(2u-1)(2+2c(1-tu))-t(2cu-1),
\]
whose values at \(u=1/c\) and \(u=1\) are respectively \(8(1-t)/(2+t)\) and \(2(1-t)(2+t)\), both nonnegative. Thus the two ranges cover all \(v\). Finally, for \((E_1,E_3)\), \(r=(a,b)\) has \(a+b=1+t\), and \(s=(-v,1-v)\). The terms \(|e|+|a|=v+a\) and \(|f|+|b|=1-v+b\) average to \(c\); since \(0\le\Delta=a(1-v)+bv\le1\), this proves the bound. The lower bound is complete.

For the upper bound, put \(k=t/(2+t)\). Both rows \((1,k)\) and \((k,1)\) lie on the boundary of \(B_t^\circ\), so \(\|L_t\|=1\). All four expressions in \(M\) equal \(1+k\); \(\det L_t=1-k^2\). Therefore \(\|L_t^{-1}\|=(1+k)/(1-k^2)=1/(1-k)=c\). Equality follows.

## Verification
Run `python checker.py` with SymPy. The expected successful output is `DEFORMATION_EXACT_BERNSTEIN_OK 13824 coefficients, 48 cells`. This verifies the finite polynomial inequalities over all continuum parameter values using rational Bernstein coefficients, the listed exceptional-cell orbit coverage, the endpoint concavity expressions, and the exact upper-bound identity. The three exceptional inequalities and the normalization argument are also given analytically above. The checker is proof-supporting exact symbolic arithmetic, not a numerical parameter-grid experiment.

## Relationship to prior work
Deregowska and Lewandowska (2026) study upper bounds on Banach–Mazur distance in terms of absolute projection constants for codimension-one and codimension-two subspaces; their principal result is a general **upper estimate**, not the present exact formula for the four-coordinate norm. The public 2026 result *Sharp projection constants for a symmetric four-coordinate deformation* establishes the exact projection constant \(2(1+t)/(2+t)\) and the first-order relation \(d=1+t/2+O(t^2)\), explicitly without an exact interior-distance claim. The current theorem proves equality throughout \([0,1]\) with an unrestricted-isomorphism lower bound. Lassak (2021) establishes \(d=3/2\) for affine-regular hexagons; this covers the endpoint but not the parameterized interior. Published general bounds and endpoint formulas do not imply an equality formula for every \(t\).

## Limitations
The claim concerns only the specified two-dimensional **real** norm family and the target \(\ell_\infty^2\). It does not characterize all optimal isomorphisms or give complex Banach–Mazur distances. Priority risk remains from an equivalent unlocated planar convex-body formula, and independent expert review has not been performed.

## References
1. B. Deregowska and B. Lewandowska, *Projection Constants and Banach-Mazur Distance in Codimension Two*, arXiv:2610.06141v1, publicly submitted 5 October 2026, primary MSC 46B20. https://arxiv.org/abs/2610.06141
2. *Sharp projection constants for a symmetric four-coordinate deformation*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-projection-constants-for-a-symmetric-four-coordinate-defor--5cb469d0202c
3. M. Lassak, *Banach–Mazur Distance from the Parallelogram to the Affine-Regular Hexagon and Other Affine-Regular Even-Gons*, Results Math. 76, article 62 (2021), https://doi.org/10.1007/s00025-021-01368-8
4. T. Kobos and M. Varivoda, *On the Banach–Mazur Distance in Small Dimensions*, Discrete Comput. Geom. 74 (2025), 399–427, first published 13 April 2024. https://doi.org/10.1007/s00454-024-00641-1
