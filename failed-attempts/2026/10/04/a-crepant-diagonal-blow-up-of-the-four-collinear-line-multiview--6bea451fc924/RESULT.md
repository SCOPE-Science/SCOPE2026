# A crepant diagonal blow-up of the four-collinear line-multiview correction divisor

## Finding

For four translational cameras
\[
C_i=\begin{pmatrix}
1&0&0&v_i\\
0&1&0&0\\
0&0&1&0
\end{pmatrix},\qquad i=1,2,3,4,
\]
with pairwise distinct \(v_i\in\mathbb C\), let \(D_v\subset E\cong(\mathbb P^1)^4\) be the correction divisor obtained by restricting the published four-collinear line-multiview equation to the determinantal baseline component. Let
\[
\Delta=\{[y_1:z_1]=[y_2:z_2]=[y_3:z_3]=[y_4:z_4]\}\cong\mathbb P^1
\]
be the small diagonal. Then
\[
\rho:\widetilde D_v=\operatorname{Bl}_\Delta D_v\longrightarrow D_v
\]
is a smooth crepant resolution. Its exceptional divisor is canonically a constant smooth conic bundle over \(\Delta\), hence isomorphic to \(\mathbb P^1\times\mathbb P^1\). Moreover,
\[
-K_{\widetilde D_v}=\rho^*\mathcal O_{D_v}(1,1,1,1),
\]
so \(\widetilde D_v\) is a smooth weak Fano threefold.

## Assumptions and scope

Work over \(\mathbb C\). The four parameters \(v_i\) are pairwise distinct. On the baseline component \(E\), use factor coordinates \([y_i:z_i]\). The correction equation is
\[
F=\det\!\begin{pmatrix}
v_1z_1&v_2z_2&v_3z_3&v_4z_4\\
v_1y_1&v_2y_2&v_3y_3&v_4y_4\\
z_1&z_2&z_3&z_4\\
y_1&y_2&y_3&y_4
\end{pmatrix},
\qquad D_v=V_E(F).
\]
The statement concerns this intrinsic threefold divisor and its resolution. It does not assert a resolution of the full line multiview variety for arbitrary camera arrangements.

## Proof

On the affine chart \(y_1y_2y_3y_4\ne0\), put \(t_i=z_i/y_i\). Direct expansion of the determinant gives, up to the invertible factor \(y_1y_2y_3y_4\),
\[
D=(v_1-v_4)(v_2-v_3)(t_1-t_3)(t_2-t_4)
 -(v_1-v_3)(v_2-v_4)(t_1-t_4)(t_2-t_3).
\]
Write
\[
a=t_2-t_1,\qquad b=t_3-t_1,\qquad c=t_4-t_1.
\]
Then \(D=q(a,b,c)\) is independent of the common-shift coordinate \(t_1\) and is homogeneous quadratic in \((a,b,c)\). Its Hessian satisfies
\[
\det\operatorname{Hess}(q)
=2\prod_{1\le i<j\le4}(v_i-v_j),
\]
which is nonzero because the \(v_i\) are distinct. Thus \(q\) is a nondegenerate ternary quadratic form. In particular, \(F\) vanishes to order exactly two along \(\Delta\), and locally along \(\Delta\) the pair \((D_v,\Delta)\) is analytically a smooth curve times the vertex of a nondegenerate quadric cone.

Blow up the origin in the three transverse coordinates \((a,b,c)\). The strict transform of \(q=0\) is smooth: its exceptional section is the projective conic \(q=0\) in \(\mathbb P^2\), which is smooth because the Hessian is nonsingular, and the standard blow-up charts have no further critical point on the strict transform. Since \(D_v\) is already smooth away from \(\Delta\), the global strict transform in \(\operatorname{Bl}_\Delta E\), equivalently \(\operatorname{Bl}_\Delta D_v\), is smooth.

It remains to identify the exceptional surface globally. The normal bundle of the diagonal in the fourfold \(E=(\mathbb P^1)^4\) is
\[
N_{\Delta/E}\cong T_{\mathbb P^1}^{\oplus3}\cong\mathcal O_{\mathbb P^1}(2)^{\oplus3}.
\]
The divisor \(D_v\) has class \(\mathcal O_E(1,1,1,1)\), whose restriction to \(\Delta\) is \(\mathcal O_{\mathbb P^1}(4)\). Because the multiplicity along \(\Delta\) is two, the initial normal quadratic is a section of
\[
\operatorname{Sym}^2N_{\Delta/E}^*\otimes\mathcal O_{\mathbb P^1}(4)
\cong \mathcal O_{\mathbb P^1}^{\oplus6}.
\]
Hence this quadratic form is constant along \(\Delta\). Therefore the exceptional divisor is the product of \(\Delta\) with one smooth conic in \(\mathbb P^2\):
\[
\operatorname{Exc}(\rho)\cong\mathbb P^1\times\mathbb P^1.
\]

For crepancy, let \(\pi:\widetilde E=\operatorname{Bl}_\Delta E\to E\), and let \(B\) be its exceptional divisor. Since \(\Delta\) has codimension three in \(E\),
\[
K_{\widetilde E}=\pi^*K_E+2B.
\]
The multiplicity-two calculation gives
\[
\widetilde D_v=\pi^*D_v-2B.
\]
Adjunction therefore cancels the exceptional terms:
\[
K_{\widetilde D_v}
=(K_{\widetilde E}+\widetilde D_v)|_{\widetilde D_v}
=\rho^*(K_E+D_v)|_{D_v}
=\rho^*K_{D_v}.
\]
Thus \(\rho\) is crepant. Finally,
\[
K_E=\mathcal O_E(-2,-2,-2,-2),\qquad
D_v\sim\mathcal O_E(1,1,1,1),
\]
so
\[
-K_{D_v}=\mathcal O_{D_v}(1,1,1,1).
\]
Its pullback is nef and big, and it has degree zero on the exceptional fibers, hence is not ample. Therefore \(\widetilde D_v\) is weak Fano.

## Verification

The supplied `verify_crepant_resolution.py` reconstructs the affine cross-ratio numerator symbolically for arbitrary \(v_i\), changes to the three difference coordinates, and checks that the Hessian determinant is exactly
\[
2\prod_{i<j}(v_i-v_j).
\]
It then normalizes to \((v_1,v_2,v_3,v_4)=(0,1,2,3)\), where
\[
q(a,b,c)=-3ab+4ac-bc,
\]
checks \(\det\operatorname{Hess}(q)=24\), and verifies directly in all three affine blow-up charts that the strict transform has no critical point. The script uses exact symbolic arithmetic and prints `VERIFY_OK`.

The bundle calculation and discrepancy cancellation are algebraic: \(N_{\Delta/E}\cong\mathcal O(2)^{\oplus3}\), \(D_v|_\Delta\cong\mathcal O(4)\), and the multiplicity is exactly two, so the exceptional conic bundle is constant and the two exceptional contributions in adjunction cancel.

## Relationship to prior work

Breiding--Duff--Gustafsson--Rydell--Shehu give the explicit four-collinear determinant and the ideal-theoretic description of line multiview varieties for collinear translational cameras. Their equation is the input defining \(D_v\), but the inspected sections do not describe the blow-up of its diagonal, an exceptional \(\mathbb P^1\times\mathbb P^1\), or a crepant resolution.

Aluffi--Faber study closures of \(\mathrm{PGL}_2\)-orbits of point configurations on \(\mathbb P^1\). For configurations supported on at least three points, they resolve the rational orbit map from the projective space of \(2\times2\) matrices by blowing up its base lines. That is a different resolution in matrix space for the symmetric orbit closure. The result here is intrinsic to the ordered fixed-cross-ratio hypersurface in \((\mathbb P^1)^4\): a single blow-up of its singular diagonal resolves it, with a globally identified exceptional surface and zero discrepancy.

## Limitations

The parameters must be pairwise distinct and the ground field is \(\mathbb C\). The result applies to the four-camera correction divisor on the baseline component, not to arbitrary mixed camera configurations or to every singularity of the full multiview variety. The literature comparison found no source stating this exact intrinsic crepant blow-up, but equivalent ordered-orbit compactification language could exist outside the sources inspected here.

## References

1. P. Breiding, T. Duff, L. Gustafsson, F. Rydell, E. Shehu, *Line Multiview Ideals*, arXiv:2303.02066 (first public 2023-03-03); *Communications in Algebra* 52 (2024), DOI 10.1080/00927872.2024.2343762.
2. P. Aluffi, C. Faber, *Linear orbits of d-tuples of points in \(\mathbb P^1\)*, arXiv:alg-geom/9205005 (first public 1992-05-12); *Journal für die reine und angewandte Mathematik* 445 (1993), 205--220.
