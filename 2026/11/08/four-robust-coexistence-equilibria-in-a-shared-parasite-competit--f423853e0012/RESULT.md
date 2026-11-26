# Four robust coexistence equilibria in a shared-parasite competition map

## Finding

The reduced two-species competition map of Bravo de la Parra and Sanz [1,2] attains the sharp bound of **four isolated strictly positive fixed points**. The witness has strictly positive coefficients and exactly four positive fixed points, all transverse. Thus an open subset of the positive coefficient space has exactly four positive fixed points. The initiating paper reported that it had not found this case numerically.

The rational coefficient choice is
\[
\begin{aligned}
\phi_1(x,y)&=\frac{63/50}{1+(1579/50)x+(9/100)y}
 +\frac{17/25}{1+(2/25)x+(731/100)y},\\
\phi_2(x,y)&=\frac{253/100}{1+(12717/100)x+(13/25)y}
 +\frac{291/50}{1+(1774/25)x+(9549/100)y}.
\end{aligned}
\]
For \(H(x,y)=(x\phi_1(x,y),y\phi_2(x,y))\), the four positive fixed points have first coordinates in the respective disjoint intervals
\[
(1/10000,1/200),\quad (1/200,1/50),\quad
(1/50,3/50),\quad (3/50,9/100).
\]
The bound is not a bound on a continuum of nonisolated fixed points in a degenerate system with coincident nullclines. Transversality implies persistence of the equilibria, not attraction of nearby trajectories.

## Assumptions and scope

In the positive-coefficient family write
\[
\phi_i(x,y)=\frac{r_S^i}{1+a_i x+b_i y}
 +\frac{r_I^i}{1+c_i x+d_i y},\qquad
H(x,y)=(x\phi_1(x,y),y\phi_2(x,y)).
\]
A positive coexistence equilibrium is a state \((x,y)\in(0,\infty)^2\) satisfying \(\phi_1=\phi_2=1\). Isolation is relative to the open positive quadrant. All twelve coefficients are strictly positive, including in a sufficiently small neighborhood of the witness.

This is the functional form of Equation (9) in [1]. It is realizable by the reduced fast-infection model's coefficient formulas: take equal transmission \(\beta=1/2\) and recovery \(\gamma=1/4\), so \(\nu=\gamma/\beta=1/2\), and set \(b_S^i=2r_S^i\), \(b_I^i=2r_I^i\). For species index \(j=1\) set \(c_{SS}^{ij}=c_{SI}^{ij}=a_i\) and \(c_{IS}^{ij}=c_{II}^{ij}=c_i\); for \(j=2\) use \(b_i,d_i\), respectively. Then \(c_{Sj}^i=\nu c_{SS}^{ij}+(1-\nu)c_{SI}^{ij}\) and \(c_{Ij}^i=\nu c_{IS}^{ij}+(1-\nu)c_{II}^{ij}\) give the stated reduced coefficients, with all required coefficients positive and \(0<\gamma<\beta\le1\). No finite-fast-step four-dimensional assertion is made.

## Proof

**1. Four sign changes on a positive nullcline.** Each \(\phi_i\) is strictly decreasing in each coordinate in the nonnegative quadrant. Whenever \(\phi_1(x,0)>1\), there is a unique \(Y(x)>0\) with \(\phi_1(x,Y(x))=1\): the function tends to zero as \(y\to\infty\), and \(\partial_y\phi_1<0\). The latter also makes \(Y\) continuous on its domain. Put \(G(x)=\phi_2(x,Y(x))-1\).

| \(x\) | \(\ell\) | \(u\) | Sign of \(G(x)\) |
|---|---|---|---|
| \(1/10000\) | \(324927/100000\) | \(324928/100000\) | negative |
| \(1/200\) | \(182960/100000\) | \(182961/100000\) | positive |
| \(1/50\) | \(25319/100000\) | \(25320/100000\) | negative |
| \(3/50\) | \(2715/100000\) | \(2716/100000\) | positive |
| \(9/100\) | \(62/100000\) | \(63/100000\) | negative |

The exact rational inequalities in each row are \(0<\ell<u\) and \(\phi_1(x,\ell)>1>\phi_1(x,u)\), giving \(\ell<Y(x)<u\). At the negative rows \(1-\phi_2(x,\ell)>1/1000\), and at the positive rows \(\phi_2(x,u)-1>1/1000\). Decrease in \(y\) therefore gives the stated signs. Decrease in \(x\) also shows that \(\phi_1(x,0)>1\) on the entire closed range of the five probes, since it holds at the largest probe. Continuity gives at least one positive coexistence equilibrium strictly between each consecutive pair of probes.

**2. Upper bound and transversality for the witness.** Put
\[
U_i=1+a_i x+b_i y,\qquad V_i=1+c_i x+d_i y,\qquad
Q_i=U_iV_i-r_S^iV_i-r_I^iU_i.
\]
The denominators are strictly positive in the quadrant, so \(Q_i=0\) is equivalent there to \(\phi_i=1\). Also
\[
Q_i=(U_i-r_I^i)(V_i-r_S^i)-r_S^i r_I^i.
\]
For the witness, \(a_1d_1-b_1c_1=(1579/50)(731/100)-(9/100)(2/25)>0\); hence \(U_1,V_1\) are independent affine coordinates. In these coordinates \(Q_1\) is a nondegenerate irreducible hyperbola over \(\mathbb C\), with irreducible projective closure. The sign certificate shows \(Q_2\ne0\) at a point of \(Q_1=0\), so there is no common component. Both polynomials have degree two. By Bézout their total complex projective intersection multiplicity is four, so the four positive affine intersections are the only intersections, each of multiplicity one. In particular the two affine gradients are linearly independent there. Multiplying by the positive denominators does not change this independence at the zero of each equation \(\phi_i-1\).

**3. Perturbations and the general isolated bound.** The implicit-function theorem continues the four equilibria in disjoint neighborhoods within the positive quadrant. The first determinant remains nonzero for sufficiently small perturbations. The strict bracket and sign inequalities also persist, ensuring \(Q_2\) does not become a multiple of \(Q_1\). Thus the upper bound four continues to hold and there are exactly four positive fixed points throughout a nonempty open neighborhood.

For arbitrary positive coefficients, each positive nullcline is either empty or the positive part of an irreducible conic or of a line. If \(a_i d_i-b_i c_i\ne0\), the conic assertion follows from the same hyperbola form. If the determinant vanishes, \((c_i,d_i)=\lambda(a_i,b_i)\) for some \(\lambda>0\), and \(\phi_i\) is a strictly decreasing function of \(a_i x+b_i y\); thus its positive level set at one, when nonempty, lies on a single line. For distinct resulting algebraic curves, Bézout bounds their number of intersections by the product of their degrees, at most four. When the curves coincide, their positive parts agree, and every positive point on that common nullcline is nonisolated because \(\partial_y\phi_i<0\). For example, the admissible choice \(\phi_1=\phi_2=2/(1+x+y)\) gives the entire positive segment \(x+y=1\). This explains why the general bound refers to isolated points.

**4. Numerical diagnostics.** The four \(x\)-coordinates are approximately \(0.0037059225\), \(0.0103942192\), \(0.0485773119\), and \(0.0858669842\). The corresponding \(y\)-coordinates are approximately \(2.1753701\), \(0.7946889\), \(0.0473817\), and \(0.0030870\). These approximations are not used in the proof.

## Verification

Run `python3 verify.py` using only the standard library. The script checks the rational probes and their strict ordering and sign gaps, and the nonzero determinant for the first conic; success is indicated by `VERIFY_OK`. The all-domain claims use the monotonicity, continuity, irreducibility, Bézout and implicit-function arguments above, not numerical root searches.

## Relationship to prior work

Reference [1] derives this two-term mixture of Beverton–Holt/Leslie–Gower factors for its shared-parasite model, and cites an earlier fast-dispersal model [4] of the same form. Lemma 3.1 of [1] describes the nullcline geometry, and the discussion following Theorem 3.2 gives the upper bound of four intersections and reports that four positive intersections had not been found in numerical searches. The exact positive witness and its open neighborhood attain that bound; neither the bound nor the hyperbolic nullcline geometry is claimed as new. Reference [2] is the later open deposit of [1]. Reference [3] treats a different generalized Beverton–Holt competition model with an Allee effect; its multiple-intersection examples do not imply attainment for the strictly decreasing per-capita rational responses above.

## Limitations

The result concerns the reduced two-dimensional map and isolated positive equilibria. It gives no stability types, basin description, empirical parameter prediction, or finite-fast-step full-model equilibrium classification. The full text of the earlier same-form study [4] was not available for comparison, so it is not asserted that this is the first witness for a map of this form.

## References

1. R. Bravo de la Parra and L. Sanz, *A discrete model of competing species sharing a parasite*, Discrete and Continuous Dynamical Systems–B **25** (2020), 2121–2142, https://doi.org/10.3934/dcdsb.2019204. First published online September 17, 2019.
2. R. Bravo de la Parra and L. Sanz, open deposit of [1], https://arxiv.org/html/2402.04041v1, especially Sections 2–4 and Appendix B.
3. Y. Kang, *Dynamics of a generalized Beverton–Holt competition model subject to Allee effects*, https://arxiv.org/abs/1505.05913.
4. M. Marvá and R. Bravo de la Parra, *Coexistence and superior competitor exclusion in the Leslie–Gower competition model with fast dispersal*, Ecological Modelling **306** (2015), 247–256, https://doi.org/10.1016/j.ecolmodel.2014.10.039.
