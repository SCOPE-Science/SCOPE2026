# Stable Cartier ranks in a genus-five trigonal deformation in characteristic eleven

## Finding
Let \(k=\overline{\mathbb F}_{11}\), and for \(t\in k\) let \(C_t\) be the smooth projective normalization of the plane quintic
\[
XYZ^3+X^5+Y^5+tX^3Y^2=0.
\]
Precisely the parameters satisfying \(t^5\ne6\) yield genus-five smooth normalizations with the stipulated seven distinct branch points. On this smooth-parameter locus, the Jacobian \(11\)-rank \(f_t\) and Cartier \(a\)-number \(a_t\) have the **complete** stratification
\[
(f_t,a_t)=
\begin{cases}
(0,5)&t=0,\\
(2,1)&t^5=2,\\
(4,1)&t\ne0,\ t^5\ne2,6.
\end{cases}
\]
Thus no member of this genus-five pencil is ordinary. The central superspecial fiber deforms to nonzero-parameter curves with Cartier \(a\)-number one; among these, precisely five geometric fibers have the smaller stable Cartier rank. The five parameters with \(t^5=2\) constitute a single degree-five Frobenius orbit over \(\mathbb F_{11}\), and also a single geometric isomorphism orbit under fifth-root rescaling of the covering coordinate.

For every integer \(n\ge1\), among coefficient parameters in \(\mathbb F_{11^n}\), the numbers of smooth fibers with ranks \(0,2,4\), respectively, are
\[
1,\qquad5\mathbf1_{5\mid n},\qquad11^n-1-10\mathbf1_{5\mid n}.
\]
There are additionally exactly \(5\mathbf1_{5\mid n}\) excluded singular coefficient parameters. The counts concern coefficient-marked fibers, not distinct abstract isomorphism classes.

## Assumptions and scope
Work in characteristic \(11\), including all geometric parameters over the algebraic closure. The coordinate \(t\) is a fixed marked pencil coordinate. On \(X\ne0\), set \(u=Y/X\) and \(v=-Z/X\). The smooth projective curve is equivalently the cyclic cubic cover
\[
v^3=\frac{N_t(u)}{u},\qquad N_t(u)=u^5+tu^2+1.
\]
The parameter \(t=0\) is the known Kudo superspecial genus-five curve. The theorem does not claim that every genus-five trigonal curve arises from this pencil or determine Newton polygons, endomorphism rings, or full isomorphism classes of the generic fibers.

## Proof
**Smoothness and genus.** The polynomial \(N_t\) has a repeated root exactly when \(t^5=6\): a repeated root \(u\ne0\) satisfies \(5u^3+2t=0\) and \(1+(3t/5)u^2=0\); elimination gives \(t^5=6\), and conversely these equations have a solution when that relation holds. The rational function \(N_t(u)/u\) has valuation \(-1\) at \(u=0\), valuations \(+1\) at the five distinct roots of \(N_t\), and valuation \(-4\) at infinity. Thus for \(t^5\ne6\) the degree-three cover is geometrically connected and totally ramified at seven places. Riemann--Hurwitz gives \(2g-2=-6+7\cdot2=8\), hence \(g=5\). The plane quintic has its expected ordinary node at \([0:0:1]\); no additional singularities occur off the excluded discriminant locus.

**Holomorphic forms.** For \(j=1,2\), the divisors at the branch points and infinity show that
\[
\mathcal B=(u^{-1}du/v,\ du/v,\ u^{-1}du/v^2,\ du/v^2,\ u\,du/v^2)
\]
is a basis of holomorphic differentials. At \(u=0\), the orders of \(u,v,du\) are \(3,-1,2\); at infinity they are \(-3,-4,-4\); and at each root of \(N_t\) they are \(0,1,2\).

**Exact Cartier computation.** If \(j'=2\) when \(j=1\), or \(j'=1\) when \(j=2\), put \(e=(11j'-j)/3\), so \(e=7\) or \(3\). Then
\[
\frac{u^i\,du}{v^j}=\left(v^{-j'}\right)^{11}u^{i-e}N_t(u)^e\,du.
\]
The coefficient of \(u^{11(q+1)-1}\) in \(u^{i-e}N_t^e\) contributes to the output basis form \(u^qdu/v^{j'}\), with coefficient raised to the \(1/11\)-power. Consequently the *unrooted* Cartier coefficient matrix in \(\mathcal B\) is
\[
U_t=\begin{pmatrix}
0&0&0&3t&0\\
0&0&0&0&3t\\
-2t&2t^3&0&0&0\\
-5t^4&-4t^6-3t&0&0&0\\
-t^2&0&0&0&0
\end{pmatrix}.
\]
The actual Cartier matrix is obtained by taking entrywise eleventh roots; this distinction is essential for iterates over extension fields. For \(t\ne0\), the upper-right \(2\)-by-\(3\) block and lower-left \(3\)-by-\(2\) block each have rank two: their decisive minors are \(9t^2\) and \(2t^5\). Hence the Cartier rank is four and \(a_t=1\); at \(t=0\), \(U_t=0\), whence \(a_0=5\) and \(f_0=0\).

**Stable rank for nonzero parameters.** Let \(A_t\) and \(B_t\) denote the lower-left and upper-right blocks. A decisive minor of \(A_t\) using its final two rows is \(-4t^3(t^5-2)\). Since the upper-right block selects these two rows with invertible multipliers, the Frobenius-unrooted two-step block \(B_tA_t^{(1/11)}\) (equivalent to the rooted Cartier iterate after applying Frobenius) is invertible precisely when \(t\ne0\) and \(t^5\ne2\). The opposite twisted block always has rank two for \(t\ne0\). Thus for \(t^5\notin\{2,6\}\) and \(t\ne0\), all Cartier iterates have rank four, giving \(f_t=4\).

At \(t^5=2\), put \(E=\mathbb F_{11}[\tau]/(\tau^5-2)\). Since \(\tau^{11}=4\tau\) and \(\tau^{1/11}=3\tau\), exact multiplication of the ten unrooted semilinear factors \(U_\tau,U_{3\tau},\ldots,U_{3^9\tau}\) gives an idempotent matrix with only columns one and four nonzero:
\[
P_{10}=\begin{pmatrix}
1&0&0&0&0\\
-5\tau^3&0&0&0&0\\
0&0&0&-3\tau^2&0\\
0&0&0&1&0\\
0&0&0&-\tau^3&0
\end{pmatrix},\quad P_{10}^2=P_{10},\quad\operatorname{rank}(P_{10})=2.
\]
(The displayed product uses the coefficient rather than the rooted matrix; its rank equals that of the corresponding Cartier iterate.) Because the field automorphism has period five, subsequent tenfold blocks repeat, so stable rank is two. The first ten product ranks are \(4,3,2,2,2,2,2,2,2,2\). All five roots of \(t^5-2\) are Frobenius conjugate and have the same invariants.

**Arithmetic and isomorphism orbit.** The field \(\mathbb F_{11}\) contains \(\mu_5\), but its nonzero fifth powers are only \(\{\pm1\}\). Hence both \(t^5-2\) and \(t^5-6\) are irreducible Kummer polynomials of degree five. Both have five roots over \(\mathbb F_{11^n}\) exactly when \(5\mid n\); removing the singular roots gives the displayed parameter counts. Finally, \(u\mapsto\zeta u\) for \(\zeta^5=1\), accompanied by a suitable scaling of \(v\), changes \(t\) by a fifth root of unity, so the five rank-two parameters are one geometric isomorphism orbit.

## Verification
Run the accompanying `verify.py` using Python 3 standard library. It independently obtains the five-by-five coefficient matrix by both multinomial enumeration and direct polynomial multiplication, checks the critical minors, performs exact arithmetic in \(E\), computes the ten semilinear Cartier products and their ranks, verifies the idempotent, and checks the fifth-power restrictions in \(\mathbb F_{11}\). Its checked terminal line is `GENUS5_TRIGONAL_F11_DEFORMATION_VERIFIED matrix=5x5 smooth_boundary=t^5-6 stable_ranks=0,2,4 rank2_degree5=5 a_number_nonzero=1`. The proof of the geometric assertions is given above; the test program is an independent reproducibility aid, not a substitute for the algebraic arguments.

## Relationship to prior work
Kudo's 2018 preprint (*A note on certain superspecial and maximal curves of genus 5*, arXiv:1807.04394) proves the superspeciality and maximality criterion for the central monomial model. Kudo--Harashita's 2018 preprint (*Superspecial trigonal curves of genus 5*, arXiv:1804.11277) classifies superspecial genus-five trigonal curves in small characteristic and supplies a plane-adjoint Hasse--Witt method. Neither result, in the inspected theorem/proof/algorithm/appendix sections, states the geometric parameter-wise \(11\)-rank classification of the displayed one-parameter deformation. Related recorded results on cyclic-trigonal genus-four families have different genus and different branch data, and do not imply this classification. The central superspecial example and the general Cartier machinery are not claimed as new.

## Limitations
This is a coefficient-marked, one-dimensional subfamily of the genus-five trigonal moduli space, not a complete classification of all genus-five trigonal curves. The equivalence of five exceptional parameters is established, but generic geometric isomorphism classes are not enumerated. Newton polygons, complete Weil polynomials, and deformations in other characteristics are not determined. A prior unindexed equivalent computation cannot be excluded; independent mathematical audit has not been performed.

## References
- M. Kudo, *A note on certain superspecial and maximal curves of genus 5*, arXiv:1807.04394, first posted 2018-07-12, https://arxiv.org/abs/1807.04394.
- M. Kudo and S. Harashita, *Superspecial trigonal curves of genus 5*, arXiv:1804.11277, first posted 2018-04-30, https://arxiv.org/abs/1804.11277.
