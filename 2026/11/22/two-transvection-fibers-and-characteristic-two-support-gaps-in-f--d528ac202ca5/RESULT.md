# Two-transvection fibers and characteristic-two support gaps in finite symplectic groups

## Finding
Fix any prime power \(q\), integer \(m\geq1\), and symplectic \(2m\)-space \((V,B)\) over \(\mathbb F_q\). For \(v\ne0\) and \(a\ne0\), write
\[
T_{v,a}(x)=x+aB(x,v)v.
\]
Let \(\mathcal T\) be the set of all distinct nonidentity symplectic transvections, of size \(N=q^{2m}-1\), and define the prescribed-product fiber
\[
F(g)=\#\{(X,Y)\in\mathcal T^2:XY=g\},\qquad g\in\operatorname{Sp}_{2m}(q).
\]
For \(W_g=\operatorname{im}(g-I)\), the following *complete* formula holds in every characteristic:
\[
F(g)=\begin{cases}
N,&g=I,\\
q-2,&\operatorname{rank}(g-I)=1,\\
\#\{L\in\mathbb P(W_g):Q_g|_L\ne0\},&\operatorname{rank}(g-I)=2,\\
0,&\operatorname{rank}(g-I)\ge3,
\end{cases}
\]
where for rank two, \(Q_g((g-I)x)=B(x,(g-I)x)\) is independent of the chosen preimage. In particular, when \(q=2\), no nonidentity transvection is a product of two nonidentity transvections.

The rank-two formula admits an exact universal **source-resolved multiplicity census**. Put
\[
D_m=\frac{q^{2m-2}(q^{2m}-1)}{q^2-1},\qquad
I_m=\frac{(q^{2m}-1)(q^{2m-2}-1)}{(q-1)(q^2-1)}.
\]
These are respectively the numbers of nondegenerate and totally isotropic two-planes in \(V\), with \(I_1=0\). In the following tables a row \((f,c)\) means that **exactly \(c\) elements** \(g\) of the indicated rank-two geometric type satisfy \(F(g)=f\). Entries with zero count are absent.

For odd \(q\):

| Type of \(W_g\) | Fiber size \(f\) | Number of targets \(c\) |
| --- | ---: | ---: |
| Nondegenerate | \(q+1\) | \(D_m q(q-1)^2/2\) |
| Nondegenerate | \(q-1\) | \(D_m q(q+1)(q-3)/2\) |
| Nondegenerate | \(q\) | \(D_m(q^2-1)\) |
| Nondegenerate | \(0\) | \(D_m\) |
| Totally isotropic | \(q+1\) | \(I_m q(q-1)^2/2\) |
| Totally isotropic | \(q-1\) | \(I_m q(q+1)(q-1)/2\) |

For even \(q\):

| Type of \(W_g\) | Fiber size \(f\) | Number of targets \(c\) |
| --- | ---: | ---: |
| Nondegenerate | \(q+1\) | \(D_m q^2(q-1)/2\) |
| Nondegenerate | \(q-1\) | \(D_m q(q+1)(q-2)/2\) |
| Totally isotropic | \(q\) | \(I_m(q-1)(q^2-1)\) |
| Totally isotropic | \(0\) | \(I_m(q-1)\) |

The **complete support cardinality**, counting the identity and the rank-one outputs in addition to rank-two outputs, is
\[
|\mathcal T^2|=\begin{cases}
1+N+D_m(q^3-q^2-q-1)+I_mq^2(q-1),&q\text{ odd},\\
1+\mathbf1_{\{q>2\}}N+D_m(q^3-q^2-q)+I_m(q-1)(q^2-1),&q\text{ even}.
\end{cases}
\]
For any target \(g\) omitted from the positive rows, its fiber is zero. Thus the formula determines every prescribed product, including zero fibers and all coincidences of numerical fiber sizes.

## Assumptions and scope
The finite field may have characteristic two; \(m\ge1\). A nonidentity transvection is counted once as a group element, regardless of how many parameter pairs \((v,a)\) represent it. The ordered product is \(XY\), with ordered factors \((X,Y)\). All rank conditions concern \(g-I\). A nondegenerate two-plane has a nondegenerate restricted alternating form; a totally isotropic two-plane has identically zero restricted form. No conjugacy-class choice for the transvection parameter is imposed (for odd \(q\), both square classes are included).

## Proof
**(1) Root groups and rank.** There are \((q^{2m}-1)/(q-1)\) projective directions, each with \(q-1\) different nonzero transvection parameters, so \(|\mathcal T|=N\). Transvections on one direction form an additive one-parameter root group. Every \(X\) has exactly one inverse, hence \(F(I)=N\); every nonidentity transvection has exactly \(q-2\) ordered same-direction factorizations. If two factor directions are independent, the image of \(XY-I\) is two-dimensional: writing \(X=I+u\otimes\alpha\), \(Y=I+v\otimes\beta\), one has
\[
XY-I=u\otimes(\alpha+\alpha(v)\beta)+v\otimes\beta.
\]
The two displayed functionals are independent because \(\alpha,\beta\) are independent, so the rank is two. This excludes rank one from independent directions, and rank at least three from all pairs.

**(2) The Wall-line bijection.** Write \(M=g-I\). Symplecticity gives \(\ker M=(\operatorname{im} M)^\perp\). Consequently \(Q_g(Mx)=B(x,Mx)\) is well-defined on \(W_g\): replacing \(x\) by a vector of \(\ker M\) does not alter its pairing with \(Mx\). Fix rank \(M=2\), a projective line \(L\subset W_g\), and a nonzero \(w=Mx\in L\). If \(Q_g(w)\ne0\), set
\[
X=T_{w,\,Q_g(w)^{-1}}.
\]
Then \(X^{-1}g\) fixes \(\ker M\) and also fixes \(x\notin\ker M\), because
\[
X^{-1}gx=x+w-Q_g(w)^{-1}B(x+w,w)w=x.
\]
Thus \(Y=X^{-1}g\) has rank \(Y-I\le1\); it cannot be the identity, because \(g\) has rank two. A nonidentity symplectic map with rank \(Y-I=1\) is a transvection (its rank-one correction is nilpotent and symplectic). Scaling \(w\) multiplies \(Q_g(w)\) by the square of the scalar, leaving \(X\) unchanged. Hence each nonisotropic Wall line yields exactly one ordered factorization. Conversely, if \(g=XY\) with independent factor directions \(L=\operatorname{im}(X-I)\) and \(L'=\operatorname{im}(Y-I)\), choose \(x\in\ker(Y-I)\) for which \((X-I)x\ne0\). Then \(Mx=(X-I)x\) lies in \(L\), and \(Q_g(Mx)=B(x,(X-I)x)\ne0\). The preceding construction recovers \(X\) uniquely. This proves the fiber formula, and works without dividing by two.

**(3) Nondegenerate image plane.** When \(W_g\) is nondegenerate, \(V=W_g\perp W_g^\perp\). Every vector of \(W_g^\perp=\ker M\) is fixed by \(g\); hence \(g\) restricts to \(U\in\operatorname{Sp}(W_g)=\operatorname{SL}_2(q)\), with \(\det(U-I)\ne0\). On \(W_g\), writing \(w=(U-I)x\) gives \(Q_g(w)=B(x,Ux)\); this vanishes precisely when \(Kx\) is a rational eigenline of \(U\). Thus \(F(g)\) is \(q+1\) minus the number of rational eigenlines of \(U\). The matrix classes with no \(1\)-eigenvector are easily counted from their centralizers: for odd \(q\), the nonsplit regular, split regular, nontrivial \(-1\)-Jordan, and scalar \(-I\) types have respective populations
\[
\frac{q(q-1)^2}{2},\quad \frac{q(q+1)(q-3)}{2},\quad q^2-1,\quad1.
\]
Their eigenline counts are \(0,2,1,q+1\). For even \(q\), there are nonsplit and split regular types only, with respective counts \(q^2(q-1)/2\) and \(q(q+1)(q-2)/2\), having \(0,2\) eigenlines. This produces the nondegenerate rows once multiplied by the number \(D_m\) of symplectic two-planes.

**(4) Isotropic image plane.** If \(W_g\) is totally isotropic, then \(M^2=0\), since \(\operatorname{im}M\subseteq(\operatorname{im}M)^\perp=\ker M\). The symplectic condition reduces to symmetry of the Wall bilinear form
\[
H_g(Mx,My)=B(x,My).
\]
This is a nondegenerate symmetric form on the two-dimensional space \(W_g\), and every such symmetric form determines a unique permissible \(g\). Its diagonal is \(Q_g(w)=H_g(w,w)\). There are \(q^2(q-1)\) invertible symmetric binary matrices. For odd \(q\), counting pairs \((H,L)\) where \(L\) is an isotropic projective line shows that \(q(q-1)(q+1)/2\) forms are split (two zero lines) and \(q(q-1)^2/2\) are anisotropic (zero zero lines). For even \(q\), exactly \(q-1\) nondegenerate alternating symmetric forms have \(Q_g\equiv0\); the other \((q-1)(q^2-1)\) forms have exactly one zero line, because a nonzero diagonal map on a binary space in characteristic two has a one-dimensional zero locus. Substituting into the Wall-line formula yields every isotropic row.

**(5) Ambient plane counts and support.** Counting ordered hyperbolic pairs gives \(D_m=q^{2m-2}(q^{2m}-1)/(q^2-1)\). Counting isotropic lines and then their disjoint partners gives \(I_m=(q^{2m}-1)(q^{2m-2}-1)/((q-1)(q^2-1))\). Each target of rank two has a unique image plane, so the above classifications do not double count. Adding the positive target counts in the two tables, the identity, and the rank-one targets when \(q>2\) gives the displayed support formula. Directly multiplying target multiplicities by their fiber sizes and adding the identity and rank-one fibers recovers \(N^2\), as required for all ordered pairs.

## Verification
The standalone Python standard-library program `verify.py` independently constructs the symplectic form and the full set of nonidentity transvections, enumerates all ordered pair products, computes rank and Wall-line invariants from each output matrix, and checks both prescribed-fiber values and support formulas. It runs prime and extension fields of orders \(2,3,4,5,7,9\), in dimensions \(2,4,6\), with ten complete enumeration configurations; the largest uses \(65{,}025\) ordered pairs. Output from replay is included as `verify_output.txt`. This is a finite check, not the proof of the all-field statements; that proof is given above. Independently, the class-population weights satisfy the exact identity \(\sum_gF(g)=N^2\) symbolically.

## Relationship to prior work
Knüppel (1992) proves symplectic transvection *length* theorems and a shortening criterion via the Wall form; the shortening idea in step (2) is classical and **is not presented as new**. Ellers and Malzan (1991) study the shortest products from a fixed transvection conjugacy class over odd fields, not the unrestricted two-factor counts stated here. Arias-de-Reyna, Dieulefait and Wiese (first posted May 6, 2014) provide the standard parametrization of finite-field symplectic transvections in the setting of subgroup classification. Özden (2018) proves dimension stability of filtered class-sum structure constants; the targeted introduction and structure-constant section do not present the evaluated all-characteristic rank-two multiplicity tables or characteristic-two zero-fiber strata here. Exact structure constants for unrestricted finite symplectic-group multiplication are not asserted to be a new concept; the proposed contribution is the concrete all-characteristic **two-transvection prescribed-target and multiplicity evaluation**.

## Limitations
The result concerns all nonidentity symplectic transvections together, not one odd-characteristic square class; it does not evaluate three-factor or longer convolutions. The formula does not claim new results on minimal transvection length or general symplectic class-algebra stability. The 1991 fixed-class factorization article was accessible at abstract level but not inspected in full; its detailed formulas remain a historical-priority risk. The full historical literature may contain an equivalent evaluated census. Computations establish only the finite cases listed. The result has received no independent mathematical audit.

## References
1. F. Knüppel, *Factorization into Symmetries and Transvections of Given Conjugacy Classes*, Canadian Mathematical Bulletin 35 (1992), 400–409, DOI https://doi.org/10.4153/CMB-1992-053-5, especially Section 4 and Lemma 4.1.1.
2. E. W. Ellers and J. Malzan, *Products of \(\lambda\)-Transvections in \(\operatorname{Sp}(2n,q)\)*, Linear Algebra and its Applications 146 (1991), 121–132 (abstract and bibliography accessible; full text not inspected).
3. S. Arias-de-Reyna, L. Dieulefait and G. Wiese, *Classification of subgroups of symplectic groups over finite fields containing a transvection*, arXiv:1405.1258, first publicly posted 2014-05-06, https://arxiv.org/abs/1405.1258.
4. Ş. Özden, *Stability of the center of the symplectic group rings over finite fields*, arXiv:1812.04720, first posted 2018-12-11, especially Introduction and Section 4.5, https://arxiv.org/abs/1812.04720.
5. G. E. Wall, *On the conjugacy classes in the unitary, symplectic and orthogonal groups*, Journal of the Australian Mathematical Society 3 (1963), 1–62 (Wall forms and rational conjugacy theory).
