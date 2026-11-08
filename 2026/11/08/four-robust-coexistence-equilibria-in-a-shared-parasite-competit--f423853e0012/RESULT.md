# Four robust coexistence equilibria in a shared-parasite competition map

## Finding

The reduced two-species competition map introduced by Bravo de la Parra and Sanz (References 1–2) **attains its sharp upper bound of four strictly positive fixed points**, with all demographic and competitive coefficients strictly positive. In particular, the four-equilibrium case, which the initiating paper explicitly leaves without an example after extensive searches, exists on a nonempty open subset of admissible parameters.

The following fully rational coefficient choice supplies a reproducible witness:

\[
\begin{aligned}
\phi_1(x,y)&=\frac{63/50}{1+(1579/50)x+(9/100)y}
 +\frac{17/25}{1+(2/25)x+(731/100)y},\\
\phi_2(x,y)&=\frac{253/100}{1+(12717/100)x+(13/25)y}
 +\frac{291/50}{1+(1774/25)x+(9549/100)y}.
\end{aligned}
\]

For the map \(H(x,y)=(x\phi_1(x,y),y\phi_2(x,y))\) on the nonnegative quadrant, **exactly four distinct fixed points satisfy \(x>0\) and \(y>0\)**. Their first coordinates belong, respectively, to the disjoint rational intervals

\[
(1/10000,1/200),\quad (1/200,1/50),\quad
(1/50,3/50),\quad (3/50,9/100).
\]

The four intersections are transverse; consequently all four persist for every sufficiently small perturbation of the positive coefficients. The assertion is about fixed-point multiplicity and local structural persistence of the reduced map, not global attraction or stability type.

## Assumptions and scope

For arbitrary positive coefficients, write

\[
\phi_i(x,y)=\frac{r_S^i}{1+a_i x+b_i y}
+\frac{r_I^i}{1+c_i x+d_i y},\qquad
H(x,y)=(x\phi_1(x,y),y\phi_2(x,y)),\quad i\in\{1,2\}.
\]

All eight density-dependence coefficients \(a_i,b_i,c_i,d_i\) and all four reproduction coefficients \(r_S^i,r_I^i\) in the displayed witness are strictly positive. A *positive coexistence equilibrium* is a state \((x,y)\in(0,\infty)^2\) satisfying \(H(x,y)=(x,y)\), or equivalently \(\phi_1(x,y)=\phi_2(x,y)=1\).

This is precisely the functional form of the reduced map in Equation (9) of Reference 1. It is also realizable by the fast-infection model's biological parameters: choose equal transmission \(\beta=1/2\), recovery \(\gamma=1/4\), and hence susceptible fraction \(\nu=\gamma/\beta=1/2\). For each \(i\), set \(b_S^i=2r_S^i\) and \(b_I^i=2r_I^i\) in the source's notation. For each \(i,j\), set the two competition coefficients in the susceptible-output denominator equal to \(a_i\) if \(j=1\) and \(b_i\) if \(j=2\); set the corresponding infected-output coefficients to \(c_i\) and \(d_i\). Then the source's reduction formula \(c_{Sj}^i=\nu c_{SS}^{ij}+(1-\nu)c_{SI}^{ij}\), \(c_{Ij}^i=\nu c_{IS}^{ij}+(1-\nu)c_{II}^{ij}\) gives the rational map above. All the source-model positivity and \(0<\gamma<\beta\le 1\) requirements are satisfied. No claim about the number of equilibria of the finite-fast-step four-dimensional map is needed here.

## Proof

**1. A positive nullcline and five rational isolating brackets.** Each \(\phi_i\) is strictly decreasing in each coordinate on the nonnegative quadrant. For fixed \(x>0\), whenever \(\phi_1(x,0)>1\), there exists exactly one \(Y(x)>0\) satisfying \(\phi_1(x,Y(x))=1\). This branch is continuous by strict negativity of \(\partial_y\phi_1\), or by the implicit-function theorem. Put \(G(x)=\phi_2(x,Y(x))-1\).

For the coefficient choice in the Finding, the following rational table is an **exact-arithmetic certificate**. Each row specifies \(x\), a lower bound \(\ell\), an upper bound \(u\), and the sign of \(G(x)\). All numbers in the first three columns are rational.

| \(x\) | \(\ell\) | \(u\) | Certified sign of \(G(x)\) |
|---|---|---|---|
| \(1/10000\) | \(324927/100000\) | \(324928/100000\) | negative |
| \(1/200\) | \(182960/100000\) | \(182961/100000\) | positive |
| \(1/50\) | \(25319/100000\) | \(25320/100000\) | negative |
| \(3/50\) | \(2715/100000\) | \(2716/100000\) | positive |
| \(9/100\) | \(62/100000\) | \(63/100000\) | negative |

The exact inequalities in *every* row are

\[
0<\ell<u,\qquad
\phi_1(x,\ell)>1>\phi_1(x,u).
\]

They imply \(\ell<Y(x)<u\). At rows labeled **negative**, the verified stronger inequality is

\[
1-\phi_2(x,\ell)>\frac1{1000},
\]

so \(\phi_2(x,Y(x))<\phi_2(x,\ell)<1\). At rows labeled **positive**, the exact stronger inequality is

\[
\phi_2(x,u)-1>\frac1{1000},
\]

so \(\phi_2(x,Y(x))>\phi_2(x,u)>1\). The script `verify.py` replays all inequalities using `fractions.Fraction`, with no tolerance or floating-point arithmetic. The distinct zeros of continuous \(G\) supplied by its four sign changes lie strictly between consecutive \(x\)-values in the table. Hence there are **at least four** distinct strictly positive fixed points.

**2. Four is an upper bound for this witness.** Let

\[
U_i=1+a_ix+b_iy,\quad V_i=1+c_ix+d_iy,\quad
Q_i=U_iV_i-r_S^iV_i-r_I^iU_i.
\]

On the positive quadrant all denominators are strictly positive, so \(Q_i=0\) exactly when \(\phi_i=1\). Each \(Q_i\) has total degree at most two. In particular,

\[
Q_1=(U_1-r_I^1)(V_1-r_S^1)-r_S^1r_I^1.
\]

The coordinate change \((x,y)\mapsto(U_1,V_1)\) is nonsingular because

\[
a_1d_1-b_1c_1=
\frac{1579}{50}\frac{731}{100}-\frac9{100}\frac2{25}>0.
\]

In independent affine coordinates \((U_1,V_1)\), the polynomial \((U_1-r_I^1)(V_1-r_S^1)-r_S^1r_I^1\), with \(r_S^1r_I^1\ne0\), is an irreducible nondegenerate hyperbola over \(\mathbb C\). Thus \(Q_1\) is irreducible. The sign certificate shows that \(Q_2\) is nonzero at some points of \(Q_1=0\), so \(Q_1\) cannot divide \(Q_2\); the two plane conics have no common component. Bézout's theorem gives at most four intersections over the complex projective plane, counted with multiplicity, and hence at most four real positive intersections. Combining both directions proves **exactly four**.

**3. Simplicity and persistence.** The four distinct affine intersections consume all of Bézout's total intersection multiplicity four. Therefore each has local intersection multiplicity one, equivalently their gradients \(\nabla Q_1\) and \(\nabla Q_2\) are linearly independent. The implicit-function theorem consequently continues each strictly positive equilibrium uniquely for sufficiently small changes in the twelve coefficients. Alternatively, the strict rational brackets and their sign margins persist under sufficiently small coefficient perturbations and give four intersections directly. The conic upper bound remains valid in a sufficiently small neighborhood, so the count stays exactly four there.

**4. Independent approximate orientation check.** Elimination of \(y\) from the two quadratic equations produces a quartic in \(x\) with four simple positive roots numerically near \(0.0037059225\), \(0.0103942192\), \(0.0485773119\), and \(0.0858669842\), paired with positive \(y\)-coordinates approximately \(2.1753701\), \(0.7946889\), \(0.0473817\), and \(0.0030870\). These decimal values are diagnostics only; the proof is the rational bracket plus conic argument.

## Verification

Execute `python verify.py` with Python 3 and its standard library. It exactly constructs the coefficients and the five rational probe intervals, checks \(\phi_1(x,\ell)>1>\phi_1(x,u)\), proves the four alternating signs by inequalities with margin \(1/1000\), verifies strict ordering and nondegeneracy of the first conic, and prints `VERIFY_OK` on success. No external files or numerical libraries are necessary. The proof's finite calculations are fully exact; the continuity, irreducibility, and Bézout arguments are analytic and do not follow from test output alone.

## Relationship to prior work

Reference 1 introduces precisely this two-term mixture of Beverton–Holt/Leslie–Gower factors. Its Lemma 3.1 proves the nullclines are hyperbolas and its discussion following Theorem 3.2 supplies the upper bound of four. The authors explicitly state that extensive numerical searches had not yielded any parameter choice with four positive intersections and accordingly analyze only zero through three. The present result supplies an exact positive-parameter witness attaining that known bound and proves it occupies an open parameter set. It does **not** claim the Bézout upper bound or the hyperbolic geometry is new.

Reference 2 is the authors' later openly accessible deposit of their paper; the public date attached to the initiating research is the publisher's September 17, 2019 online release, not the 2024 deposit. Reference 3 exhibits four interior equilibria in a different, Allee-effect generalized Beverton–Holt model; that result does not entail four in the strictly decreasing-per-capita, shared-parasite mixture studied here.

## Limitations

Only the homogeneous-disease *reduced two-dimensional map* is treated, not a finite-fast-step full infection model. The proof classifies the **number and transverse persistence** of positive equilibria for the stated coefficients, not their attracting or saddle types, basins, or ecological likelihood under empirical parameter distributions. The witness's coefficients are strongly heterogeneous, so this is an existence and sharpness result rather than a claim that four coexistence states are typical. Numerical root coordinates are optional diagnostics, not certificates. The scientific priority assessment is limited to accessible indexed research and the directly inspected initiating manuscript; unindexed equivalent examples remain possible.

## References

1. R. Bravo de la Parra and L. Sanz, *A discrete model of competing species sharing a parasite*, Discrete & Continuous Dynamical Systems—B **25** (2020), 2121–2142, doi:10.3934/dcdsb.2019204; publisher first public online release September 17, 2019. https://www.aimsciences.org/article/doi/10.3934/dcdsb.2019204
2. R. Bravo de la Parra and L. Sanz, openly accessible full text of Reference 1, arXiv:2402.04041 (deposited February 6, 2024), Sections 2–4 and Appendix B. https://arxiv.org/html/2402.04041v1
3. Y. Kang, *Dynamics of a generalized Beverton–Holt competition model subject to Allee effects*, arXiv:1505.05913 (2015). https://arxiv.org/abs/1505.05913
