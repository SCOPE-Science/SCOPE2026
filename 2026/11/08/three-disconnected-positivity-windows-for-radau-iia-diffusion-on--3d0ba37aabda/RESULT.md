# Three disconnected positivity windows for Radau IIA diffusion on star networks

## Finding

**Theorem.** Let \(m\ge2\) be an integer. Let \(L_m\) be the combinatorial Laplacian of the unit-edge star \(K_{1,m}\), whose vertices are a hub and \(m\) leaves. The completed two-stage, order-three Radau IIA step for the heat equation \(u'=-L_m u\) is
\[
T_m(h)=(6I-2hL_m)(h^2L_m^2+4hL_m+6I)^{-1},\qquad h\ge0.
\]

For \(2\le m\le10\), the matrix \(T_m(h)\) is entrywise strictly positive for every \(h>0\). For every \(m\ge11\), put
\[
\alpha_m^\pm=\frac{m-2\pm\sqrt{m^2-10m-2}}{m+1}
\]
and define \(\beta_m^-<\beta_m^+\) to be the **two distinct positive real roots** of
\[
\begin{split}
P_m(h)={}&(m+1)h^4+(-2m^2+2m+10)h^3\\
&+(6m^2+4m+16)h^2+(24m+12)h+36.
\end{split}
\]
These four thresholds obey
\[
0<\alpha_m^-<\alpha_m^+<2<3<\beta_m^-<8<\beta_m^+.
\]
The complete nonnegative-step set is exactly
\[
\boxed{\{h\ge0:T_m(h)\text{ is entrywise nonnegative}\}
=[0,\alpha_m^-]\cup[\alpha_m^+,\beta_m^-]\cup[\beta_m^+,\infty).}
\]
Every off-diagonal entry is strictly positive at \(h>0\). On \((\alpha_m^-,\alpha_m^+)\) only the hub diagonal is negative; on \((\beta_m^-,\beta_m^+)\) only the leaf diagonals are negative. Thus there are exactly two disjoint failure windows and three safe windows. At each of the four positive endpoints, the corresponding diagonal entries vanish; at \(h=0\), \(T_m(0)=I\).

As \(m\to\infty\), the thresholds satisfy
\[
\alpha_m^-\sim\frac3m,\qquad \alpha_m^+\to2,\qquad
\beta_m^-\to3,\qquad \frac{\beta_m^+}{m}\to2.
\]

## Assumptions and scope

All edges have unit conductance, the spatial generator is the **unnormalized** graph Laplacian, and the entire completed Radau IIA endpoint update is used (no internal-stage positivity is asserted). The conclusion is about entrywise nonnegativity for **every nonnegative initial vector**, not merely Euclidean contractivity, scalar stability or a selected test state. Real time step \(h\) is arbitrary in \([0,\infty)\). The polynomial denominator of the update is positive on the nonnegative Laplacian spectrum, so the inverse always exists.

## Proof

The Radau IIA tableau has stage matrix and endpoint weights
\[
\mathsf A=\begin{pmatrix}5/12&-1/12\\3/4&1/4\end{pmatrix},\qquad
\mathsf b=(3/4,1/4).
\]
Substitution into the scalar linear test equation gives the stated rational stability function. Write \(N=m+1\), and put
\[
r(z)=\frac{6-2z}{z^2+4z+6},\qquad
A=r(h),\quad B=r(Nh),\quad D(z)=z^2+4z+6.
\]
The spectrum of \(L_m\) is \(\{0,1,N\}\) with respective multiplicities \(1,m-1,1\). The zero eigenspace is spanned by \(\mathbf1\), and the \(N\) eigenspace by \((m,-1,\ldots,-1)\). Therefore, with the usual orthogonal spectral projectors,
\[
T_m(h)=E_0+A E_1+B E_N.
\]
The four entry orbits are: hub diagonal \(H\), hub-to-leaf \(C\), leaf diagonal \(F\), and distinct-leaf entry \(J\). Direct projector multiplication gives
\[
H=\frac{1+mB}{N},\quad C=\frac{1-B}{N},\quad
F=\frac{m+B+(m-1)N A}{mN},\quad
J=\frac{m+B-N A}{mN}.
\]
Let \(D_a=D(h)\) and \(D_b=D(Nh)\). Clearing the positive denominators gives the exact identities
\[
H=\frac{Q_m(h)}{D_b},\qquad Q_m(h)=Nh^2+(4-2m)h+6,
\]
\[
F=\frac{P_m(h)}{D_a D_b},\qquad
C=\frac{h(Nh+6)}{D_b},\qquad
J=\frac{h^2\,[Nh^2+6(m+2)h+18]}{D_aD_b}.
\]
Thus for every \(h>0\), \(C,J>0\), and nonnegativity is equivalent to the simultaneous inequalities \(Q_m(h)\ge0\) and \(P_m(h)\ge0\).

The discriminant of \(Q_m\) is \(4(m^2-10m-2)\). Its two roots are positive and distinct precisely for integers \(m\ge11\), and are then \(\alpha_m^\pm\). For \(2\le m\le10\), \(Q_m(h)>0\) for every \(h\ge0\).

For the quartic, note first that \(r(z)>-1\) for every \(z\ge0\), while \(r(h)\ge0\) for \(0\le h\le3\). Hence \(F>0\) for \(h\in[0,3]\) and all \(m\ge2\). For \(h>3\), regard \(P_m(h)\) as a quadratic polynomial in the real variable \(m\); its quadratic coefficient is \(2h^2(3-h)<0\). Consequently, on the real interval \(2\le m\le10\), concavity gives
\[
P_m(h)\ge\min\{P_2(h),P_{10}(h)\}.
\]
The polynomial \(P_2(h)=3(h^4+2h^3+16h^2+20h+12)\) is positive on \([0,\infty)\). The following **exact sum-of-nonnegative-terms identity** proves positivity of the other endpoint:
\[
P_{10}(h)=h\left(h-\frac{39}{5}\right)^2\left(11h+\frac85\right)
+\frac{293}{25}h^2+\frac{19332}{125}h+36>0.
\]
This settles all integer \(m\le10\).

For \(m\ge11\), the exact evaluation
\[
P_m(8)=-4(160m^2-1392m-2593)<0
\]
holds because the quadratic inside the parentheses is positive and strictly increasing for \(m\ge11\). Since \(P_m(0)=36>0\) and its leading coefficient \(m+1\) is positive, it has at least two distinct positive roots, one on each side of \(8\). Its coefficient sign sequence in descending powers is \((+,-,+,+,+)\), with exactly two sign changes. Descartes' rule of signs therefore shows it has **exactly** these two positive roots, counting multiplicity. Thus both are simple, and \(P_m(h)<0\) exactly between \(\beta_m^-\) and \(\beta_m^+\). The earlier \(F>0\) argument gives \(\beta_m^->3\), while the root formula gives \(\alpha_m^+<2\). The gaps are disjoint and the stated union follows.

Finally, the explicit radical formula gives \(\alpha_m^-\sim3/m\) and \(\alpha_m^+\to2\). For fixed \(h>3\), the highest-order term of \(P_m(h)\) in \(m\) is \(2m^2h^2(3-h)<0\), whereas \(P_m(3)>0\). This forces \(\beta_m^-\to3\). At \(h=tm\), the leading term of \(m^{-5}P_m(tm)\) is \(t^3(t-2)\), uniformly for \(t\) in compact subsets of \((0,\infty)\). Since \(\beta_m^+>8\) is the sole larger positive root, sign bracketing at \(t=2\pm\varepsilon\) gives \(\beta_m^+/m\to2\). This proves the theorem.

## Verification

The accompanying standard-library-only `verify.py` independently checks four exact bivariate polynomial identities, the exact polynomial-coefficient positivity certificate at \(m=10\), the sign thresholds at \(h=8\), and \(2{,}046\) rational full-matrix assertions, using spectral projectors and the original matrix rational equation. It reports `VERIFY_OK 2228`. The symbolic polynomial identities hold for the indeterminate \(m,h\), whereas the finite matrix tests are **supplemental checks**, not substitutes for the above all-size proof. Run `python3 verify.py` from the extracted package directory.

For illustration at \(m=11\), the hub gap is \((1/2,1)\), while the leaf gap is approximately \((6.0684116041764,11.7642575953540)\). These approximate endpoints are not used for certification.

## Relationship to prior work

The method and its third-order Radau IIA construction are classical. Brugnano, Iavernaro and Magherini (2013) treat efficient implementation of Radau collocation and discuss the two-stage method. Flaig (2013) treats implicit Radau schemes for parabolic optimal control; Bresten et al. (2013) study positivity and SSP restrictions for **explicit multistep** Runge–Kutta formulas; Kovács, Li and Lubich (2015) prove discrete maximal regularity for A-stable schemes, including Radau IIA. Neither maximal regularity nor A-/L-stability implies positivity of the completed step. The examined portions of these works do not evaluate the star-dependent two-gap positivity set here. Earlier exact classifications for other implicit schemes or different graph families concern different method–graph pairs; none alone implies the quartic sign analysis here.

## Limitations

The result covers only uniform, finite, unweighted stars and the **two-stage** Radau IIA endpoint method; it makes no claim about nonuniform edge weights, higher-stage Radau formulas, nonlinear ODEs, or positivity of intermediate stages. Numerical illustrations are not an infinite proof. The literature comparison is not a proof that no uncatalogued or differently formulated result exists. Independent verification beyond the supplied reproducible calculations is not claimed.

## References

1. L. Brugnano, F. Iavernaro and C. Magherini, *Efficient implementation of Radau collocation methods*, arXiv:1302.1037v1, publicly posted 2013-02-05. https://arxiv.org/abs/1302.1037
2. T. G. Flaig, *Implicit Runge-Kutta schemes for optimal control problems with evolution equations*, arXiv:1311.0640v1, publicly posted 2013-11-04. https://arxiv.org/abs/1311.0640
3. C. Bresten, S. Gottlieb, Z. Grant, D. Higgs, D. I. Ketcheson and A. Németh, *Strong Stability Preserving Multistep Runge-Kutta Methods*, arXiv:1307.8058v1, publicly posted 2013-07-30. https://arxiv.org/abs/1307.8058
4. B. Kovács, B. Li and C. Lubich, *A-stable time discretizations preserve maximal parabolic regularity*, arXiv:1511.07823v1, publicly posted 2015-11-24. https://arxiv.org/abs/1511.07823
