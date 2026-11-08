# The first path-graph positivity failure of three-stage Radau IIA occurs at fourteen vertices

## Finding

Let \(P_n\) denote the unweighted undirected path on \(n\) vertices, \(L_n\) its ordinary combinatorial Laplacian (both endpoints have degree one), and \(h\geq0\). The completed fifth-order, three-stage Radau IIA heat step is

\[
T_n(h)=R(-hL_n),\qquad R(z)=\frac{60+24z+3z^2}{60-36z+9z^2-z^3}.
\]

**Theorem (first path-size failure).** For every integer \(1\le n\le13\), the matrix \(T_n(h)\) is entrywise nonnegative at every real step \(h\ge0\), and every entry is strictly positive whenever \(h>0\) and \(n\ge2\). In contrast, the entry between the two endpoints of \(P_{14}\) at \(h=5/2\) is exactly

\[
(T_{14}(5/2))_{1,14}=
-\frac{513016184045167720763721348125}
{7821977770020587781141217755303635636}<0.
\]

Consequently, among unweighted paths, fourteen vertices is the **smallest order at which the completed three-stage Radau IIA update can fail positivity**. The theorem makes no assertion about all step sizes on paths with more than fourteen vertices.

## Assumptions and scope

Graphs are finite, undirected, simple paths with unit edge conductance and no boundary killing. \(L_n\) is the full graph Laplacian, not an interior Dirichlet stencil or the normalized Laplacian. The stability function is the order-five \([2/3]\) Padé approximation to the exponential, which is the completed (end-of-step) stability function of three-stage Radau IIA. The theorem addresses the matrix mapping initial graph states to their values after one completed step, not the signs of internal Runge–Kutta stages. The step \(h\) is an arbitrary real nonnegative number.

## Proof

Set

\[
P(x)=60-24x+3x^2,\qquad
Q(x)=60+36x+9x^2+x^3.
\]

Then \(T_n(h)=P(hL_n)Q(hL_n)^{-1}\), since both polynomials in \(L_n\) commute. All eigenvalues of \(L_n\) are nonnegative, \(Q(x)>0\) for \(x\ge0\), and \(L_n\) has exactly one zero eigenvalue. It follows that

\[
D_n(h)=\det Q(hL_n)>0\quad(h\ge0),\qquad
\deg D_n=3(n-1).
\]

Write \(d=3(n-1)\), \(D_n(h)=\sum_{k=0}^{d}d_kh^k\), and define the matrix polynomial

\[
N_n(h)=D_n(h)T_n(h)=\sum_{k=0}^{d}N_kh^k.
\]

The coefficients \(d_k\) are exactly computable, without spectral approximations, by applying the formal identity

\[
\log\!\frac{D_n(h)}{60^n}
=\operatorname{tr}\log\!\left(I+\frac35hL_n+\frac3{20}h^2L_n^2+\frac1{60}h^3L_n^3\right).
\]

More explicitly, let \(\ell_k\) be the coefficient of \(z^k\) in the formal series

\[
\log\left(1+\frac35z+\frac3{20}z^2+\frac1{60}z^3\right).
\]

Using \(d_0=60^n\), the exact rational recurrence is

\[
d_k=\frac1k\sum_{j=1}^k j\ell_j\operatorname{tr}(L_n^j)d_{k-j}
\quad(1\le k\le d).
\]

Coefficient comparison in

\[
Q(hL_n)N_n(h)=D_n(h)P(hL_n)
\]

gives, with out-of-range terms interpreted as zero,

\[
60N_k=60d_kI-24d_{k-1}L_n+3d_{k-2}L_n^2
-36L_nN_{k-1}-9L_n^2N_{k-2}-L_n^3N_{k-3}.
\]

This determines integer coefficient matrices exactly. The additional equations in degrees \(d+1,d+2,d+3\) are verified in the accompanying program, so the calculation is an identity of polynomials, not merely a truncated Taylor agreement.

For the twelve nontrivial orders \(2\le n\le13\), the same exact certificate establishes that every coefficient of

\[
(1+h)^{M_n}(N_n(h))_{ij}
\]

is nonnegative and that the polynomial is not identically zero, for every ordered vertex pair \((i,j)\). Sufficient integer exponents are:

| \(n\) | 2–9 | 10 | 11 | 12 | 13 |
|---|---:|---:|---:|---:|---:|
| \(M_n\) | 0 | 1 | 17 | 66 | 451 |

All these statements are checked by exact integer arithmetic. Since \((1+h)^{M_n}D_n(h)>0\) for \(h\ge0\), they imply strictly positive entries for every \(h>0\). At \(h=0\), \(T_n(0)=I\). The case \(n=1\) is immediate from \(L_1=0\).

For \(n=14\), the same coefficient recurrence, evaluated at \(h=5/2\), yields the displayed strictly negative rational endpoint entry. An independently implemented rational linear-system solution \(Q((5/2)L_{14})x=e_{14}\), followed by evaluating \((P((5/2)L_{14})x)_1\), reproduces the identical fraction. This completes the proof of the first failing order.

## Verification

The accompanying `verify.py` requires Python 3 and only the standard library. Run `python3 verify.py` in the directory containing this document and the script. It reconstructs the path Laplacians, formal determinant coefficients, polynomial numerator coefficients, all degree-elevated coefficient-sign certificates, the three trailing polynomial identities, and two independent forms of the fourteen-vertex witness. A successful run prints `VERIFY_OK 111905 exact coefficient/sign checks`.

The coefficient-sign certificate is an *all-real-step proof*: a polynomial with nonnegative coefficients and at least one positive coefficient is strictly positive at every positive real argument. This is not a finite grid of timestep experiments. The explicit rational witness is exact, not a floating-point estimate.

## Relationship to prior work

The fifth-order completed Radau IIA stability function is classical. Horváth (2005) develops general positivity step-size thresholds for Runge–Kutta discretizations, while Wade and coauthors (first published 2004) study positivity-preserving Padé-based smoothing approaches to parabolic problems. Zappavigna and coauthors (2010) study diagonal Padé maps of positive systems and exhibit nonpreservation phenomena and sufficient step-size conditions. These establish the motivating positivity-preservation problem, not this certified exact first-failure order for the particular \([2/3]\) completed map on full unit-weight path graph Laplacians. Earlier calculations for two-stage Radau IIA or two-stage Gauss have different rational stability functions and do not logically imply the stated thirteen/fourteen boundary.

## Limitations

The result concerns unweighted path graphs, completed steps, and the given fifth-order rational function only. It does not establish a monotone failure classification for every larger path size, nor a classification for weighted paths, other graph families, internal Runge–Kutta stages, or general Metzler systems. A potentially relevant historical paper on Padé smoothing could not be fully inspected; the literature comparison does not certify uniqueness across all publications. No independent mathematical audit has been performed.

## References

1. Z. Horváth, “On the positivity step size threshold of Runge–Kutta methods,” *Applied Numerical Mathematics* 53 (2005), 341–356. DOI: 10.1016/j.apnum.2004.08.026.
2. B. A. Wade, A. Q. M. Khaliq, M. Siddique and M. Yousuf, “Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data,” *Numerical Methods for Partial Differential Equations* 21 (2005), 553–573; first published online 2004-09-29. DOI: 10.1002/num.20039.
3. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, “On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems,” MTNS 2010. Author-posted full text: https://www.hamilton.ie/shravan/pade_MTNS10_long.pdf.
