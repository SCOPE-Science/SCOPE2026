# The characteristic-seven bicanonical ramification divisor of the Fermat quartic

## Finding

Let \(k=\overline{\mathbb F}_7\), and let \(C/k\) be the smooth Fermat quartic
\[C:\ X^4+Y^4+Z^4=0.\]
For the complete bicanonical linear series \(\mathcal D=|2K_C|=|\mathcal O_C(2)|\), the generic Hasse order sequence is
\[(0,1,2,3,4,7).\]
The intrinsic ramification divisor \(R_{\mathcal D}\), defined using this **nonclassical** sequence, is exactly
\[R_{\mathcal D}=3\sum_{P\in H}P+\sum_{P\in E}P,\]
where \(H\) is the set of the twelve coordinate-zero hyperflex points and
\[E=\{[X:Y:Z]\in C(k):XYZ\ne0,\ X^{24}=Y^{24}=Z^{24}\}.\]
There are exactly \(80\) distinct points in \(E\). Their local \(\mathcal D\)-orders are \((0,1,2,3,4,8)\); the twelve points of \(H\) have local orders \((0,1,2,4,5,8)\), hence ramification weight three. The divisor has degree \(116\), not the characteristic-zero bicanonical ramification degree \(108\).

Over \(\mathbb F_7\), \(E\) has eight rational points and \(H\) has none; all \(92\) reduced support points are rational over \(\mathbb F_{49}\). In fact, these 92 support points are **all** of \(C(\mathbb F_{49})\): the Hasse–Weil bound gives at most \(49+1+6\sqrt{49}=92\) points, which the support already supplies. Similarly, \(C(\mathbb F_7)\) consists of precisely the eight points of \(E(\mathbb F_7)\). The Frobenius cycle types are \(1^8 2^{36}\) on \(E\) and \(2^6\) on \(H\). The reduced support has zeta function
\[Z((R_{\mathcal D})_{\mathrm{red}}/\mathbb F_7,T)=\frac{1}{(1-T)^8(1-T^2)^{42}}.\]

## Assumptions and scope

The ground field has characteristic exactly seven, and the quartic has its displayed coefficient-one model. The linear series is the full complete bicanonical series, not an arbitrary six-dimensional subseries. A Hasse order is defined using the coefficient of the corresponding power in a formal local expansion. At a point the ramification weight is the sum of its six local orders minus the sum of the six generic orders. The zeta function concerns the **reduced support** of the ramification divisor; it does not count multiplicities as distinct points. No analogous formula is asserted in other characteristics or for arbitrary twists.

## Proof

**1. Linear series and generic Hasse orders.** By adjunction \(K_C\simeq\mathcal O_C(1)\), \(g(C)=3\), and \(h^0(C,2K_C)=6\). On the affine chart \(Z=1\), where \(y\ne0\), set \(x=X/Z\), \(y=Y/Z\), \(Q=1+x^4=-y^4\). The six sections are represented by \(1,x,y,x^2,xy,y^2\), and \(x\) is a separating local parameter. Let \(A(h)=\sum_{n\ge0}a_nh^n\) be the unique series with \(A(0)=1\) satisfying
\[A(h)^4=\frac{1+(x+h)^4}{Q}.\]
Write \(b_n=[h^n]A(h)^2\). The Hasse jet matrix of the six sections, after pivoting on \(1,x,x^2\) and replacing the \(xy\) column by that column minus \(x\) times the \(y\) column, has the three residual rows \((a_i,a_{i-1},b_i)\) for \(i\ge3\). Set
\[\Delta_n=\det\!\begin{pmatrix}a_3&a_2&b_3\\a_4&a_3&b_4\\a_n&a_{n-1}&b_n\end{pmatrix}.\]
Formal fourth-power comparison in the rational-function field \(\mathbb F_7(x)\) gives the exact identities
\[a_3^2-a_2a_4=\frac{5x^2}{Q^4},\qquad \Delta_5=\Delta_6=0,\qquad \Delta_7=\frac{x^3(x^{24}-1)}{Q^{14}}.\]
The first identity gives five independent Hasse jet rows of orders \(0,1,2,3,4\) generically. The other two identities show that the sixth generic order is exactly \(7\). These are identities in a function field, not inferences from finite-field point experiments. The attached symbolic verifier constructs the formal series recursively and checks each identity.

**2. All noncoordinate ramification points.** The Wronskian with order rows \((0,1,2,3,4,7)\) is \(y^4\Delta_7\) up to an invertible scalar/sign. Therefore, in the local trivialization given by \(Z^2\) and parameter \(x\), its zero/pole expression is
\[W_x=\text{unit}\cdot\frac{x^3(x^{24}-1)}{(1+x^4)^{13}}.\]
On the open set \(xy\ne0\), its zeros are exactly the solutions of \(x^{24}=1\). Because \(7\nmid24\), these roots are simple. Four of the \(24\) roots satisfy \(x^4=-1\), giving \(y=0\), and lie outside this chart. Each of the remaining twenty roots has four distinct nonzero fourth roots \(y\) satisfying \(y^4=-(1+x^4)\). Thus there are \(80\) simple noncoordinate zeros. Their first five jet orders remain \((0,1,2,3,4)\), since \(5x^2/Q^4\ne0\); their final order is consequently \(8\). On such a point \(u=x^4\) is a sixth root of unity in characteristic seven, hence \(u\in\mathbb F_7^*\), and \(y^4=-1-u\in\mathbb F_7^*\). This proves the symmetric projective description of \(E\).

**3. Coordinate points and completeness.** At each point with a zero coordinate, the tangent has intersection multiplicity four, since locally its tangent coordinate changes to order four in the other coordinate. The six quadratic sections therefore have local orders \((0,1,2,4,5,8)\): take the conics \(1,t,t^2,\ell,t\ell,\ell^2\), where \(t\) is a local coordinate and the tangent-line section \(\ell\) has order four. The weight relative to \((0,1,2,3,4,7)\) is \(3\). There are four such points on each coordinate line, forming \(H\) of size twelve. The general ramification-degree formula for a basepoint-free \(g^5_8\) with generic Hasse orders \(\varepsilon_i\) gives
\[\deg R_{\mathcal D}=6\cdot8+\bigl(0+1+2+3+4+7\bigr)(2\cdot3-2)=116.\]
The points found contribute \(80+12\cdot3=116\). Since ramification weights are nonnegative, no further ramification is possible.

**4. Arithmetic.** Every nonzero element of \(\mathbb F_7\) has four fourth roots in \(\mathbb F_{49}\); indeed \(\mathbb F_7^*\) is contained in the subgroup of fourth powers of \(\mathbb F_{49}^*\). Thus all \(80\) points of \(E\) and all twelve coordinate hyperflexes lie over \(\mathbb F_{49}\). Over \(\mathbb F_7\), the nonzero fourth powers are \(\{1,2,4\}\), each with two roots. In the equation \(u+v+1=0\), the admissible ordered fourth-power pairs are precisely \((u,v)=(2,4),(4,2)\); each contributes four affine points. Hence \(\#E(\mathbb F_7)=8\). No coordinate-zero point is rational since \(-1\) is not a fourth power in \(\mathbb F_7\). The 92 support points rational over \(\mathbb F_{49}\) meet the genus-three Hasse–Weil upper bound \(49+1+2\cdot3\sqrt{49}=92\), so they constitute the entire rational point set of \(C\) over that field. In particular the eight points already found over \(\mathbb F_7\) are all the points over \(\mathbb F_7\) as well. This gives the Frobenius cycles and reduced-support zeta function as claimed. The independent finite-field verifier enumerates the two support strata and also independently counts all curve points in explicit \(\mathbb F_7\) and \(\mathbb F_{49}\) arithmetic.

## Verification

Run `python3 verify_fermat7.py` with SymPy and `python3 verify_fermat7_arithmetic.py` with standard Python 3. The first produces `FERMAT7_WRONSKIAN_SYMBOLIC_OK` after checking all stated rational-function Hasse determinant identities in characteristic seven. The second produces `FERMAT7_ARITHMETIC_COUNTS_OK` after enumerating both support strata in \(\mathbb F_7\) and \(\mathbb F_{49}\), verifying their cardinalities, total ramification degree and that both sets of rational curve points are entirely supported on the divisor. A finite-field enumeration is only an auxiliary cross-check; the infinite-field divisor classification follows from the rational-function identities and the ramification-degree theorem.

## Relationship to prior work

Stöhr–Voloch's ramification-divisor framework and the Garcia–Voloch classification of Fermat nonclassicality with respect to conics are established results. In particular, the criterion involving divisibility of \(2n-1\) already predicts nonclassicality for the Fermat quartic in characteristic seven; it is not claimed as new. Torres's exposition explains the general divisor formalism. Alwaleed–Sakai classify bicanonical Weierstrass points of the complex Kuribayashi family; their Fermat member has twelve hyperflexes and 48 ordinary sextactic points in characteristic zero. The result here specifies the different, complete characteristic-seven ramification divisor, its local weights, and its arithmetic support. The cited published results do not by themselves give the explicit eighty-point support or its finite-field splitting; a possible earlier unindexed computation is not excluded.

## Limitations

The exact 1988 Garcia–Voloch primary full text was not accessible for detailed comparison; the stated classicality criterion was checked in a full open version of a later primary paper that reproduces it. Historical priority is provisional. The divisorial formula is specific to the coefficient-one Fermat quartic in characteristic seven. The zeta function is for the reduced finite support, not the curve's Hasse–Weil zeta function. Independent external mathematical review has not been performed.

## References

- K.-O. Stöhr and J. F. Voloch, *Weierstrass points and curves over finite fields*, Proceedings of the London Mathematical Society 52 (1986), 1–19. DOI: 10.1112/plms/s3-52.1.1.
- A. Garcia and J. F. Voloch, *Fermat curves over finite fields*, Journal of Number Theory 30 (1988), 345–356. DOI: 10.1016/0022-314X(88)90007-8.
- F. Torres, *The approach of Stöhr–Voloch to the Hasse–Weil bound with applications to optimal curves and plane arcs*, first arXiv version 2000-11-14, arXiv:math/0011091, especially Section 2.2.
- K. Alwaleed and F. Sakai, *Geometry and computation of 2-Weierstrass points on Kuribayashi quartic curves*, Saitama Mathematical Journal 26 (2009), 67–82, especially the Fermat member and Table 3.
- N. Arakelian and H. Borges, *Frobenius nonclassicality of Fermat curves with respect to cubics*, first arXiv version 2015-02-20, arXiv:1502.05953, especially Theorem 2.4 recalling the conic criterion.
