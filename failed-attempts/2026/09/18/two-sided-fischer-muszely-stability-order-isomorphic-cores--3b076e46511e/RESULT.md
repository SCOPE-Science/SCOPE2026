# Two-sided Fischer–Muszély stability detects order-isomorphic cores

## Result

For a map \(S:C_+\to D_+\) between positive cones of JB-algebras, define its Fischer–Muszély defect by
\[
\Delta(S)=\sup_{x,y\in C_+}
\left|
\|S(x+y)\|-\|S(x)+S(y)\|
\right|\in[0,\infty].
\]

Let \(A,B\) be nonzero JB-algebras and let \(T:A_+\to B_+\) be a bijection with
\[
\varepsilon:=\Delta(T)<\infty.
\]
By Hatori--Oi's stability theorem, there is a unique bounded positive real-linear map
\(L:A\to B\) at finite uniform distance from \(T\), and
\[
D(T,L):=\sup_{a\in A_+}\|T(a)-L(a)\|\le 3\varepsilon,
\qquad
\overline{L(A_+)}=B_+.
\]

Then the following are equivalent:

1. \(\Delta(T^{-1})<\infty\);
2. \(L\) is a bounded linear order isomorphism \(A\to B\);
3. \(T\) is at finite uniform distance on \(A_+\) from a bounded linear order isomorphism.

If
\[
\delta:=\Delta(T^{-1})<\infty,
\]
and \(M:B\to A\) is the Hatori--Oi linear asymptotic core of \(T^{-1}\), then
\[
\boxed{M=L^{-1}.}
\]
In particular,
\[
D(T,L)\le3\varepsilon,
\qquad
D(T^{-1},L^{-1})\le3\delta.
\]
The radial asymptotics are uniform:
\[
\sup_{a\in A_+}
\left\|
\frac{T(ta)}{t}-L(a)
\right\|
\le\frac{3\varepsilon}{t},
\qquad
\sup_{b\in B_+}
\left\|
\frac{T^{-1}(tb)}{t}-L^{-1}(b)
\right\|
\le\frac{3\delta}{t}
\quad(t>0).
\]

Conversely, if \(R:A\to B\) is a bounded linear order isomorphism and a bijection
\(T:A_+\to B_+\) satisfies
\[
\eta:=\sup_{a\in A_+}\|T(a)-R(a)\|<\infty,
\]
then
\[
\Delta(T)\le3\eta,
\qquad
\sup_{b\in B_+}\|T^{-1}(b)-R^{-1}(b)\|
\le \|R^{-1}\|\eta,
\]
and therefore
\[
\Delta(T^{-1})\le3\|R^{-1}\|\eta.
\]
Thus bi-approximate-FM bijections are exactly bounded perturbations of linear order isomorphisms.

As a structural consequence, whenever the equivalent conditions hold, the known order-isomorphism representation applies:
\[
L^{**}=U_{h^{1/2}}\widehat J,
\qquad
h=L^{**}(1)>0\ \text{invertible},
\]
where \(\widehat J:A^{**}\to B^{**}\) is a normal unital Jordan isomorphism. If \(A,B\) are unital, this restricts to
\[
L=U_{h^{1/2}}J
\]
for a Jordan isomorphism \(J:A\to B\).

## Proof of the two-sided criterion

Apply Hatori--Oi's Theorem 5.2 to \(T\). This gives the unique bounded positive linear core \(L\) and the bound \(D(T,L)\le3\varepsilon\).

Assume first that \(\delta=\Delta(T^{-1})<\infty\). Applying the same theorem to
\(T^{-1}:B_+\to A_+\) gives a bounded positive linear map \(M:B\to A\) such that
\[
D(T^{-1},M)\le3\delta.
\]
For \(a\in A_+\) and an integer \(n\ge1\),
\[
\begin{aligned}
\|ML(na)-na\|
&\le
\|M\|\,\|L(na)-T(na)\|
+\|M(T(na))-T^{-1}(T(na))\|\\
&\le 3\|M\|\varepsilon+3\delta.
\end{aligned}
\]
Because \(ML-I_A\) is linear, the left side equals
\[
n\|ML(a)-a\|.
\]
Dividing by \(n\) and letting \(n\to\infty\) gives \(ML(a)=a\) for every
\(a\in A_+\). Since \(A_+\) generates \(A\),
\[
ML=I_A.
\]
Interchanging \(T,L,A\) with \(T^{-1},M,B\) yields
\[
LM=I_B.
\]
Hence \(M=L^{-1}\), and both \(L\) and its inverse are positive: \(L\) is a bounded linear order isomorphism.

The implication (2)\(\Rightarrow\)(3) follows from \(D(T,L)<\infty\).
For (3)\(\Rightarrow\)(2), if an order isomorphism \(R\) is at finite uniform distance from \(T\), then the uniqueness clause in Hatori--Oi's stability theorem forces \(R=L\).

The radial estimates follow immediately from linearity:
\[
\left\|\frac{T(ta)}t-L(a)\right\|
=\frac1t\|T(ta)-L(ta)\|
\le\frac{3\varepsilon}{t},
\]
and similarly for \(T^{-1}\).

For the converse bounded-perturbation statement, linearity of \(R\) gives
\[
\begin{aligned}
\left|
\|T(a+b)\|-\|T(a)+T(b)\|
\right|
&\le
\|T(a+b)-R(a+b)\|\\
&\quad+\|T(a)-R(a)\|+\|T(b)-R(b)\|\\
&\le3\eta.
\end{aligned}
\]
If \(b=T(a)\), then
\[
\|T^{-1}(b)-R^{-1}(b)\|
=
\|a-R^{-1}T(a)\|
\le \|R^{-1}\|\eta.
\]
Applying the same three-error estimate to \(T^{-1}\) gives the displayed bound on
\(\Delta(T^{-1})\).

## Exact \(c_0\) phase transition

The two-sided condition has a sharp elementary model that extends the mechanism in Hatori--Oi's Example 5.3.

Fix \(\varepsilon>0\) and a bounded positive sequence
\[
w=(w_n),\qquad 0<w_n\le W<\infty,
\]
and define on \(c_0(\mathbb N,\mathbb R)_+\)
\[
T_w(x)_n=w_nx_n+\min\{x_n,\varepsilon\}.
\]
Put
\[
m=\inf_n w_n.
\]
Then \(T_w\) is a homeomorphism of \(c_0^+\) onto itself and
\[
\boxed{\Delta(T_w)=\varepsilon.}
\]
Its unique linear asymptotic core is
\[
L_w(x)_n=w_nx_n,
\qquad
D(T_w,L_w)=\varepsilon.
\]
Moreover,
\[
\boxed{
\Delta(T_w^{-1})=
\begin{cases}
\varepsilon/m,&m>0,\\
\infty,&m=0.
\end{cases}
}
\]
Consequently,
\[
\Delta(T_w^{-1})<\infty
\quad\Longleftrightarrow\quad
\inf_n w_n>0
\quad\Longleftrightarrow\quad
L_w\ \text{is a bounded linear order isomorphism}.
\]
When \(m>0\), one also has the exact inverse-distance formula
\[
D(T_w^{-1},L_w^{-1})=\frac{\varepsilon}{m}.
\]

To verify these assertions, note first that each scalar coordinate map
\[
\phi_w(t)=wt+\min\{t,\varepsilon\}
\]
is a strictly increasing homeomorphism of \([0,\infty)\). With
\(q_w=(1+w)\varepsilon\), its inverse is
\[
\psi_w(y)=
\begin{cases}
\dfrac{y}{1+w},&0\le y\le q_w,\\[1ex]
\dfrac{y-\varepsilon}{w},&y\ge q_w.
\end{cases}
\]
For a null sequence \(y\), eventually \(y_n<\varepsilon\le q_{w_n}\), so the first branch applies eventually and \(\psi_{w_n}(y_n)\to0\). This gives bijectivity on \(c_0^+\). Continuity of the inverse follows by using the first branch uniformly on a sufficiently far tail and finitely many scalar inverse maps on the remaining coordinates.

The linear terms cancel in
\[
T_w(x)+T_w(y)-T_w(x+y).
\]
Coordinatewise,
\[
0\le
\min\{s,\varepsilon\}+\min\{t,\varepsilon\}
-\min\{s+t,\varepsilon\}
\le\varepsilon.
\]
Hence \(\Delta(T_w)\le\varepsilon\), while \(x=y=\varepsilon e_n\) gives equality.

For the inverse, set
\[
d_w(u,v)=\psi_w(u+v)-\psi_w(u)-\psi_w(v).
\]
A direct check of the four linearity regimes gives
\[
0\le d_w(u,v)\le\frac{\varepsilon}{w}.
\]
The upper bound is attained at \(u=v=q_w\), because
\[
d_w(q_w,q_w)=\frac{\varepsilon}{w}.
\]
Since the inverse map is coordinatewise and \(d_w\ge0\),
\[
\Delta(T_w^{-1})
=\sup_n\frac{\varepsilon}{w_n},
\]
which is exactly the displayed formula.

The range of \(L_w\) contains every finitely supported sequence and is therefore dense. It is onto with positive bounded inverse exactly when \(\inf_nw_n>0\). For Hatori--Oi's specific example \(w_n=1/n\), the forward defect is exactly \(\varepsilon\) but the inverse defect is infinite. Thus the failure of surjectivity of the linear core in that example is detected precisely by loss of finite Fischer--Muszély defect in the inverse direction.

## Literature context and originality boundary

Hatori and Oi prove that every surjective approximate FM map between positive cones of arbitrary JB-algebras has a unique bounded positive linear approximation within \(3\varepsilon\), with dense positive image. Their Example 5.3 shows that this linear approximation can fail to be onto even when the original map is a continuous bijection. Their Corollary 6.2 already restores a linear order isomorphism under a coarse lower distance estimate
\[
\|T(a)-T(b)\|\ge m\|a-b\|-\kappa.
\]
Accordingly, finite FM defect for the inverse is **not** claimed to be a weakest possible extra hypothesis.

The contribution here is the two-sided characterization: for a bijective approximate FM map, finite FM defect of the inverse is equivalent to the Hatori--Oi asymptotic core being an order isomorphism, and the asymptotic core of the inverse is forced to be the exact inverse linear map. The weighted \(c_0\) family gives an exact quantitative phase transition and shows that the inverse defect measures the conditioning parameter \(1/\inf w_n\), while the forward defect remains fixed.

Tabor's classical stability theorem treats surjective FM maps from groups into whole Banach spaces and does not supply this positive-cone order-isomorphism criterion. General stability results for positive-cone nearisometries likewise concern metric perturbations rather than the two-sided FM defect considered here.

Searches for inverse approximate-FM conditions, two-sided Fischer--Muszély stability, order-isomorphic asymptotic cores, and equivalent bounded-perturbation formulations did not locate the result above. Originality is therefore asserted only to the best of our knowledge.

One material residual source risk is the unpublished 2026 manuscript by Hatori and Oi, *Order isomorphisms on positive cones of non-unital \(C^*\)-algebras*, cited by the source paper without a public identifier. Its full text was not inspected here. It is relevant because it develops order-isomorphism tools used by Hatori--Oi, although the 2026 JB-algebra paper itself states the approximate-FM stability theorem, the counterexample, and the additional coarse lower-distance criterion needed for comparison.

## Limitations

The factor \(3\) inherited from Hatori--Oi's stability theorem is not claimed sharp. The two-sided inverse-FM hypothesis is a clean exact criterion, not a minimal sufficient condition: Hatori--Oi's coarse lower-distance assumption is weaker in a different direction and already forces an order-isomorphic core. The exact \(\varepsilon/m\) formula is proved for the displayed diagonal \(c_0\) family and is not claimed to hold for arbitrary JB-algebra perturbations.

No claim is made that the weighted Jordan representation itself is new; it is an existing consequence of linear order isomorphism. The new assertion is the criterion that forces the approximate cores in the two directions to be mutual inverses, together with the exact phase-transition family.

## References

1. O. Hatori and S. Oi, *Surjective Fischer--Muszély maps on positive cones of JB-algebras*, arXiv:2609.19668 (2026). https://arxiv.org/abs/2609.19668
2. J. Tabor, *Stability of the Fischer--Muszély functional equation*, Publ. Math. Debrecen 62 (2003), 205--211. https://doi.org/10.5486/PMD.2003.2725
3. Y. Dong, D. H. Leung, and L. Li, *Stability of isometries between the positive cones of ordered Banach spaces*, Math. Ann. 389 (2024), 253--280. https://doi.org/10.1007/s00208-023-02649-z
4. D. Hirota and J. Oppekepenguin, *On the Fischer--Muszély equation for the positive cones of \(C^*\)-algebras*, arXiv:2606.28665 (2026). https://arxiv.org/abs/2606.28665
