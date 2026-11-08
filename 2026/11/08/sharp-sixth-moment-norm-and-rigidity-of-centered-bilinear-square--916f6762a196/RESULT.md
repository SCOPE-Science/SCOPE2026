# Sharp sixth-moment norm and rigidity of centered bilinear square elements

## Finding
Let \(Q=[-1,1]^2\) carry normalized area \(d\mu=\tfrac14\,du\,dv\). For the real, three-dimensional, mean-zero tensor-product polynomial space
\[
\mathcal V=\{f(u,v)=\sqrt3\,a u+\sqrt3\,b v+3cuv:\ a,b,c\in\mathbb R\},
\]
we have the **sharp and attained** two-sided inequality
\[
\boxed{\frac{27}{7}\,\|f\|_2^6\ \le\ \|f\|_6^6\ \le\ K\,\|f\|_2^6},\qquad
K=\frac{15039\sqrt{42889}}{3080}-\frac{275103}{280}=28.6989300417\ldots.
\]
The corresponding exact embedding norm \(\sup_{f\ne0}\|f\|_6/\|f\|_2\) is \(K^{1/6}\). Lower equality holds precisely for nonzero scalar multiples of \(u\) or \(v\). Define
\[
 r=\frac{231-\sqrt{42889}}{44}=0.5432591859\ldots.
\]
Upper equality holds precisely for real nonzero triples satisfying
\[
 a^2=b^2=\frac{1-r}{2}(a^2+b^2+c^2),\qquad c^2=r(a^2+b^2+c^2).
\]
The signs of \(a,b,c\) are independent. The same statement holds for affine pullbacks of this space to any nondegenerate parallelogram with normalized area.

## Assumptions and scope
All coefficients are **real**, the measure on the reference square is uniform probability, and every norm is \(\|f\|_p=(\int_Q|f|^p\,d\mu)^{1/p}\). The basis functions \(\sqrt3u\), \(\sqrt3v\), and \(3uv\) are orthonormal in \(L^2(\mu)\); hence \(S:=\|f\|_2^2=a^2+b^2+c^2\). For \(f\ne0\), write \(x=a^2/S\), \(y=b^2/S\), \(z=c^2/S\), so \(x,y,z\ge0\) and \(x+y+z=1\). The space is the constant-orthogonal component of the standard four-dimensional bilinear \(Q_1\) element.

## Proof
**Step 1: an exact sixth-moment polynomial.** Independence and symmetry of the uniform coordinates give \(\int_{-1}^1u^{2j}\,du/2=1/(2j+1)\) and vanishing odd moments. In the multinomial expansion of \(f^6\), a term containing \(i,j,k\) factors from \(u,v,uv\), respectively, survives integration only when \(i+k\) and \(j+k\) are even. Since \(i+j+k=6\), all three multiplicities must then be even. Its coefficient is
\[
 \frac{6!}{i!j!k!}\frac{3^{(i+j)/2+k}}{(i+k+1)(j+k+1)}a^i b^j c^k.
\]
Summing the ten surviving terms gives, with \(M=\|f\|_6^6/S^3\),
\[
\begin{aligned}
M={}&\frac{27}{7}(x^3+y^3)+\frac{729}{49}z^3
 +27xy(x+y)+\frac{405}{7}z(x^2+y^2)\\
&+\frac{729}{7}z^2(x+y)+\frac{1458}{5}xyz.
\end{aligned}
\tag{1}
\]
In particular, the sixth moment depends only on squared coefficient magnitudes, not their signs.

**Step 2: sharp lower deficit.** Subtract \(\tfrac{27}{7}(x+y+z)^3=\tfrac{27}{7}\) from (1) and collect terms:
\[
\boxed{M-\frac{27}{7}
=\frac{108}{7}xy(x+y)+\frac{324}{7}z(x^2+y^2)
 +\frac{648}{7}z^2(x+y)+\frac{9396}{35}xyz+\frac{540}{49}z^3.}
\tag{2}
\]
Every term is nonnegative. Equality requires \(z=0\) by the last term, and then \(xy(x+y)=0\), so the only normalized equality triples are \((1,0,0)\) and \((0,1,0)\). Both attain the lower bound.

**Step 3: exact reduction of the upper problem.** Set \(t=x+y=1-z\) and \(p=xy\). Use \(x^3+y^3=t^3-3pt\) and \(x^2+y^2=t^2-2p\) in (1). Since \(p\le t^2/4\), a direct collection gives the exact identity
\[
\boxed{M=\Phi(z)-D(z)(x-y)^2,}
\qquad
\Phi(z)=\frac{27}{245}\bigl(44z^3-693z^2+714z+70\bigr),
\qquad
D(z)=\frac{27}{7}(1-z)+\frac{1539}{35}z.
\tag{3}
\]
The coefficient \(D(z)\) is strictly positive on \([0,1]\). Therefore for fixed \(z\), equality in \(M\le\Phi(z)\) holds exactly at \(x=y=(1-z)/2\).

**Step 4: unique maximizing energy proportion.** Differentiation yields
\[
\Phi'(z)=\frac{162}{245}(22z^2-231z+119),\qquad
\Phi''(z)=\frac{1782}{245}(4z-21)<0 \quad(0\le z\le1).
\]
The derivative is positive at zero and negative at one, hence has exactly one zero in \((0,1)\). Solving the quadratic gives \(z=r=(231-\sqrt{42889})/44\). Substitution gives \(\Phi(r)=K\), proving the sharp upper endpoint and the claimed equality family.

**Step 5: sharp endpoint stability.** Using \(\Phi'(r)=0\), the cubic factors exactly:
\[
\boxed{K-M=D(z)(x-y)^2+
\frac{27}{245}(z-r)^2\bigl[693-44(z+2r)\bigr].}
\tag{4}
\]
Here \(0\le z,r\le1\), so the bracket exceeds or equals \(561>0\), and \(D(z)\ge27/7\). Thus
\[
K-M\ge\frac{27}{7}(x-y)^2+\frac{15147}{245}(z-r)^2.
\]
This proves quantitative rigidity in normalized squared coefficient energies as well as the exact upper equality classification. The lower identity (2) proves the other complete equality classification.

**Step 6: affine invariance.** Under an invertible affine map from \(Q\) onto a parallelogram, the normalized area measure is the pushforward of \(\mu\). A bilinear reference function pulls back to the natural mapped \(Q_1\) finite-element space; every \(L^p\) norm is unchanged, so all assertions transfer.

## Verification
The accompanying self-contained `check_q1_sixth.py` computes the exact sixth-moment coefficients by rational multinomial integration, matches (1) and the invariant reduction (3), verifies every coefficient of the lower deficit (2), and verifies the upper symmetry deficit (3). It also checks the stationary polynomial and all boundary and equality witnesses. Execute `python3 check_q1_sixth.py` using Python 3. The program is a *finite algebraic identity check*, not a substitute for Steps 2–5, which establish the inequalities for all real coefficients.

## Relationship to prior work
Sharp \(2\to q\) norm optimization is studied in the more general computational/analytic framework of Barak, Brandão, Harrow, Kelner, Steurer and Zhou [1]. Wolff [2] treats hypercontractivity for simple discrete random variables and associated moment comparisons, rather than this continuous tensor-product polynomial subspace. Graham, Hackbusch and Sauter [3] establish inverse-type finite-element estimates on broad classes of meshes; they do not specify this three-dimensional exact \(L^2\to L^6\) constant or its equality cases. Bojanov, Haußmann and Nikolov [4] study fixed-leading-term least-deviation polynomials on disks and triangles, a different optimization problem from the present centered \(Q_1\) norm quotient. The exact identities (1)–(4), interior upper extremizer and two complete equality families are the distinguishing claim; none follows as a stated numerical sharp case of the results inspected in [1]–[4]. A prior specialized sharp \(Q_1\) inverse-norm formula not found in the consulted literature remains possible.

## Limitations
No result is asserted for general non-parallelogram quadrilaterals, since the bilinear reference mapping there generally has nonconstant Jacobian. The sharp constants concern real coefficients, uniform probability measure, and exponent six only; they do not automatically extend to nonuniform weights or higher tensor polynomial degree. The comparison with published work establishes best-knowledge originality, not a global literature uniqueness certificate. Independent validation has not been performed.

## References
[1] B. Barak, F. G. S. L. Brandão, A. W. Harrow, J. A. Kelner, D. Steurer, Y. Zhou, *Hypercontractivity, Sum-of-Squares Proofs, and their Applications*, arXiv:1205.4484 (first submitted 2012-05-21), especially Introduction and Section 2.

[2] P. Wolff, *Hypercontractivity of simple random variables*, Studia Mathematica 180 (2007), 219–236, DOI:10.4064/sm180-3-3, Sections 1–2.

[3] I. G. Graham, W. Hackbusch, S. A. Sauter, *Finite Elements on Degenerate Meshes: Inverse-type Inequalities and Applications*, preprint dated 2004-06-04, Sections 1–3, University of Bath preprint GrHaSa04.

[4] B. D. Bojanov, W. Haußmann, G. P. Nikolov, *Bivariate Polynomials of Least Deviation from Zero*, Canadian Journal of Mathematics 53 (2001), 489–505, DOI:10.4153/CJM-2001-021-3, Introduction and Sections 1–4.
