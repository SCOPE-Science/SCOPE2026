# Exact affine projector norms on vertex-atomic simplices

## Finding

Let \(S\) be any nondegenerate real simplex of dimension \(d=m-1\geq1\), with vertices \(v_1,\ldots,v_m\), and let \(\mu_0\) be its uniform-volume probability measure. Fix arbitrary atom weights \(w_1,\ldots,w_m\geq0\), and set
\[
\mu=\mu_0+\sum_{j=1}^{m}w_j\delta_{v_j}.
\]
Let \(P\) be real \(L^2(\mu)\)-orthogonal projection onto the full space of affine functions on \(S\). Put
\[
c=m(m+1),\qquad r_i=(c^{-1}+w_i)^{-1},\qquad Z=c+\sum_{j=1}^{m}r_j,
\]
\[
H_i=\frac{r_i(Z-r_i)}{Z}\left[w_i+\frac1m\prod_{j\ne i}\frac{Z-r_i}{Z-r_i+r_j}\right].
\]
Then the exact attained endpoint operator norm is
\[
\boxed{\|P\|_{L^\infty(\mu)\to L^\infty(\mu)}=2\max_{1\le i\le m}H_i-1.}
\]
Precisely the vertices \(v_i\) with \(H_i=\max_jH_j\) are norming evaluation points; **no nonvertex point is norming**. All norm-attaining inputs at a given norming vertex are, up to \(\mu\)-null sets and a global sign, the signs of its kernel. The exact worst excursion among all measurable \(0\le f\le1\) is
\[
\boxed{\min_{0\le f\le1}\min_{x\in S}(Pf)(x)=1-\max_iH_i=-\frac{\|P\|-1}{2}.}
\]
An attaining nonnegative input is the indicator of the negative-kernel region at a norming vertex. All formulas are invariant under affine changes of simplex shape and multiplication of \(\mu\) by a positive constant.

In the natural one-atom case \(w_1=w>0\) and \(w_j=0\) for \(j\ge2\), set
\[
q=\frac{mw}{1+m^2w},\qquad I_0=\frac{m^m}{(m+1)^{m-1}}.
\]
Exactly the unweighted vertices \(v_2,\ldots,v_m\) are norming, and
\[
\boxed{\|P_w\|=\frac{2(m-q)^m}{(m+1)^{m-1}(1-q)}-1.}
\]
The norm increases strictly with \(w>0\), whereas the atom-bearing vertex's kernel norm decreases strictly. Moreover,
\[
\|P_w\|=2I_0-1+I_0m(m-1)w^2+O_m(w^3)\quad(w\downarrow0),
\]
\[
\lim_{w\to\infty}\|P_w\|=2(m+1)\left(\frac{m-1}{m}\right)^{m-1}-1.
\]
Thus a single increasing vertex weight causes a strictly positive *nonlocal* worst-case amplification, despite a zero first derivative at zero atom weight.

## Assumptions and scope

The simplex has \(m\ge2\) vertices and nonzero volume; all point masses are finite and nonnegative. The approximation space is the complete real affine space, not a higher-degree or piecewise polynomial space. The normalized volume measure \(\mu_0\) is retained with strictly positive coefficient, so affine interpolation is identifiable. The norm is the essential-supremum operator norm on \(L^\infty(\mu)\) with the continuous and atomic parts both included. The one-atom sharpness and asymptotics hold at fixed integer \(m\); no assertion about nonvertex maximizers under removal of the volume component is made.

## Proof

Write \(\lambda_1,\ldots,\lambda_m\) for barycentric coordinates. Every affine function is \(F=\sum_iF(v_i)\lambda_i\). Uniform-simplex moments satisfy
\[
\int_S\lambda_i\lambda_j\,d\mu_0=\frac{1+\mathbf1_{i=j}}{m(m+1)}.
\]
The Gram matrix for the \(\lambda_i\) under \(\mu\) therefore is \(G=\operatorname{diag}(c^{-1}+w_i)+c^{-1}{\bf1}{\bf1}^{\mathsf T}\). The rank-one inverse identity gives, with \(R=G^{-1}\),
\[
R_{ij}=r_i\mathbf1_{i=j}-\frac{r_ir_j}{Z}.
\]
The evaluation kernel at vertex \(v_i\) is \(K_i(y)=\sum_jR_{ij}\lambda_j(y)\). Its vertex values are
\[
K_i(v_i)=b_i:=\frac{r_i(Z-r_i)}Z>0,\qquad
K_i(v_j)=-\frac{r_ir_j}{Z}<0\quad(j\ne i).
\]
Thus its strictly positive set inside \(S\) is a simplex cap with apex \(v_i\) and base on \(K_i=0\). Along the edge from \(v_i\) to \(v_j\), its cut fraction is
\[
\theta_{ij}=\frac{b_i}{b_i+r_ir_j/Z}=\frac{Z-r_i}{Z-r_i+r_j}.
\]
Affine volume scaling gives the volume fraction \(\prod_{j\ne i}\theta_{ij}\). The mean of \(K_i\) over that cap is \(b_i/m\), since its vertex values there are \(b_i,0,\ldots,0\). In addition, the positive atomic part is exactly \(w_i b_i\). Consequently,
\[
\int (K_i)_+\,d\mu=b_i\left(w_i+\frac1m\prod_{j\ne i}\theta_{ij}\right)=H_i.
\]
Because \(P1=1\), \(\int K_i\,d\mu=1\), so \(\int|K_i|\,d\mu=2H_i-1\). For arbitrary evaluation \(x\in S\), barycentric linearity gives \(K_x=\sum_i\lambda_i(x)K_i\), hence
\[
\int|K_x|\,d\mu\le\sum_i\lambda_i(x)\int|K_i|\,d\mu\le\max_i(2H_i-1).
\]
If \(x\) is not a vertex, at least two barycentric coefficients are positive. Near one of their vertices, its kernel is positive while the other kernel is negative; this occurs on a set of positive \(\mu_0\)-measure. Therefore the triangle inequality is strict, showing no nonvertex is norming. At a vertex the sign of \(K_i\) is the unique (up to null sets and sign) bounded norm witness. For \(0\le f\le1\), taking \(f=\mathbf1_{K_i<0}\) produces \(\int(K_i)_-d\mu=1-H_i\), proving the negativity formula.

For the one-atom specialization let \(D=1+m^2w\), \(h=m^2w/D\), and \(q=h/m\). Sherman--Morrison around the atom-free matrix yields
\[
K_1(y)=\frac{m((m+1)\lambda_1(y)-1)}D,
\]
\[
K_i(y)=m((m+1)\lambda_i(y)-1)+h((m+1)\lambda_1(y)-1),\quad i\ne1.
\]
For each \(i\ne1\), the kernel has positive vertex value \(m(m-q)\), negative vertex value \(m(mq-1)\) at \(v_1\), and negative value \(-m(1+q)\) at every remaining vertex. Since its atom value is negative, the same simplex-cap integration gives
\[
H_i=\frac{(m-q)^m}{(m+1)^{m-1}(1-q)}\quad(i\ne1).
\]
At \(v_1\), the negative continuous kernel is the atom-free negative kernel divided by \(D\), while the atom contributes only positively; consequently
\[
H_1=1+\frac{I_0-1}{D}.
\]
The function \(J(q)=(m-q)^m/[(m+1)^{m-1}(1-q)]\) satisfies \(J(0)=I_0>1\) and
\[
\frac{d}{dq}\log J(q)=\frac{(m-1)q}{(m-q)(1-q)}>0\qquad(0<q<1/m).
\]
Since \(q\) increases strictly from zero to \(1/m\) as \(w\) increases, \(H_i>I_0>H_1\) for \(w>0\). This proves strict norming-vertex classification and monotonicity. Taylor expansion at \(q=0\) gives \(J(q)=I_0[1+(m-1)q^2/(2m)+O_m(q^3)]\), yielding the quadratic small-atom law; substituting \(q\to1/m\) gives the limit.

## Verification

The standalone file `checker.py` uses exact rational matrix inversion and verifies the Gram formula, signs, reproduction of constants and the complete one-atom identity in dimensions \(1\) through \(13\). In dimensions \(1\) and \(2\), it additionally integrates the continuous positive part by a separately implemented rational interval formula or exact polygon clipping and triangulation, independent of the cap product formula. All diagnostic cases pass; they are consistency checks, not substitutes for the proof for all dimensions and weights. Execute with `python checker.py`.

## Relationship to prior work

Hangelbroek--Narcowich--Sun--Ward (first arXiv posting May 13, 2010) study \(L^p\) stability of kernel-based least-squares projection on manifolds and establish general boundedness, not this finite-dimensional vertex-atomic sharp formula. Melenk--Wurzer (first arXiv posting February 28, 2013) establish trace stability for volume-measured polynomial projection on triangles and tetrahedra, not mixed discrete-continuous affine projection or sharp atomic endpoint constants. The known volume-only simplex formula is recovered by setting every \(w_i=0\), but it does not determine the arbitrary mixed-measure dependence. The known exact Dirichlet-weighted simplex result concerns an absolutely continuous Dirichlet law rather than independent point masses at vertices and does not imply this formula. General matrix inversion and simplex-cap volume identities are standard components; the exact all-weight endpoint norm, norming vertices, extremizing data, and nonlocal atom law comprise the specific result here.

## Limitations

This is a same-model mathematical proof review, not an independent audit. A complete bibliographic priority determination is unavailable, especially for older numerical-analysis literature on local weighted mass matrices. No universal sorting theorem for which \(H_i\) is largest under arbitrary unequal \(w_i\) is claimed; the finite explicit maximum is exact, and the one-atom family has a complete qualitative classification. The claims do not address other underlying measures, higher polynomial degrees, or the projector obtained after dropping the continuous-volume part.

## References

1. T. Hangelbroek, F. J. Narcowich, X. Sun, and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424 (first submitted 2010-05-13), https://arxiv.org/abs/1005.2424.
2. J. M. Melenk and T. Wurzer, *On the stability of the boundary trace of the polynomial \(L^2\)-projection on triangles and tetrahedra (extended version)*, arXiv:1302.7189 (first submitted 2013-02-28), https://arxiv.org/abs/1302.7189.
3. Standard Dirichlet \((1,\ldots,1)\) simplex moments and the Sherman--Morrison rank-one inverse identity (both derived or instantiated above).
