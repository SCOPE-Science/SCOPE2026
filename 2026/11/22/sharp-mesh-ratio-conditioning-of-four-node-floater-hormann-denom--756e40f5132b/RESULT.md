# Sharp mesh-ratio conditioning of four-node Floater–Hormann denominator sums

## Finding

Let \(x_0<x_1<x_2<x_3\) be four arbitrary distinct real interpolation nodes and let \(a=x_1-x_0\), \(b=x_2-x_1\), \(c=x_3-x_2\). In the degree-one Floater–Hormann (FH) first barycentric denominator, write
\[
\lambda_i(x)=\frac{(-1)^i}{(x-x_i)(x-x_{i+1})},\qquad i=0,1,2,
\]
and define its termwise relative summation condition factor
\[
\Gamma_1(x)=\frac{\sum_{i=0}^2|\lambda_i(x)|}{|\sum_{i=0}^2\lambda_i(x)|}\qquad(x\notin\{x_0,x_1,x_2,x_3\}).
\]
At a node, define \(\Gamma_1=1\) by the continuous limit. Set \(C=(a+b)(b+c)\). Then throughout the middle gap \(\Gamma_1=1\), while on the first and last gaps respectively,
\[
\Gamma_1(x_1-q)=1+\frac{2q(a-q)}{q^2+bq+C}\quad(0<q<a),
\qquad
\Gamma_1(x_2+q)=1+\frac{2q(c-q)}{q^2+bq+C}\quad(0<q<c).
\]
Each outer gap has exactly one strict maximum. If \(a>c\), the first-gap maximum is the unique global maximum; if \(c>a\), it lies uniquely in the last gap. If \(a=c\), there are exactly two reflected global maximizers.

For mesh ratio \(\mu=\max(a,b,c)/\min(a,b,c)\ge1\), the **sharp universal bound** is
\[
\boxed{\max_{x\in[x_0,x_3]}\Gamma_1(x)\le \mathcal C_4(\mu):=\frac{(\sqrt{2\mu+4}-1)^2}{2\sqrt{2\mu+4}-3}.}
\]
Equality holds if and only if the gaps are proportional to \((\mu,1,1)\) or \((1,1,\mu)\). In that extremizing grid scaled to its smallest gap being one, the maximizing point is a distance \(q_*=\sqrt{2\mu+4}-2\) inside the long outer cell from its inner endpoint. Moreover,
\[
\lim_{\mu\to\infty}\mathcal C_4(\mu)/\sqrt\mu=1/\sqrt2.
\]
For degree one and two or three nodes, the analogous denominator factor is identically one on the interpolation interval. Hence four nodes are minimal for any cancellation and the \(\sqrt\mu\) growth cannot be removed from a uniform four-node estimate.

## Assumptions and scope

The grid is real and strictly ordered; all three gaps are positive, but no quasi-uniformity assumption is imposed. The interpolation blending degree is exactly one, with exactly four data sites. The quantity \(\Gamma_1\) measures sensitivity of direct summation of the three first-barycentric denominator terms to componentwise relative perturbation; it is *not* the Lebesgue constant, interpolation error, or a universal lower bound on floating-point error for an alternative rearrangement. Statements concern real points in the closed data interval. The factors are defined by limiting values at nodes.

## Proof

**1. Exact cell formulas and signs.** Translation permits \((x_0,x_1,x_2,x_3)=(0,a,a+b,a+b+c)\). For \(x\in(x_0,x_1)\), the signs of \((\lambda_0,\lambda_1,\lambda_2)\) are \((-,-,+)\); for \(x\in(x_1,x_2)\), all three are positive; on \((x_2,x_3)\), the signs are \((+,-,-)\). In particular, there is no zero of the denominator in the open interval. Put \(q=x_1-x\) in the first gap. Directly combine the rational terms and use \(\Gamma_1=1+2\lambda_2/|\sum\lambda_i|\) to obtain
\[
\Gamma_1(x_1-q)-1=\frac{2q(a-q)}{q^2+bq+(a+b)(b+c)}.
\]
Reflection of the grid gives the last-gap identity. Positive terms give exactly one on the middle gap; the outer-cell formulas tend to one at their endpoints.

**2. Exact extrema and their location.** For \(L>0\), define
\[
F_L(q)=\frac{2q(L-q)}{q^2+bq+C}\quad(0\le q\le L).
\]
Its derivative has the sign of
\[
P_L(q)=LC-2Cq-(L+b)q^2.
\]
Since \(P_L'(q)=-2C-2(L+b)q<0\), \(P_L(0)>0\), and \(P_L(L)<0\), its unique root and strict maximum are
\[
q_L=\frac{\sqrt{C^2+CL(L+b)}-C}{L+b}\in(0,L).
\]
For any fixed \(q\in(0,\min(a,c))\), \(F_a(q)>F_c(q)\) if \(a>c\); the same strict maximum ordering holds because the larger-cell function is strictly larger at the smaller cell's unique maximizer. This proves the location classification, including exactly two maximizers when \(a=c\).

**3. Sharp fixed-mesh-ratio envelope.** Scale the least gap to one. Write \(L=\max(a,c)\le\mu\), \(s=\min(a,c)\ge1\), and \(b\ge1\). Since \(C=(L+b)(s+b)\ge2(L+1)\), for every admissible \(q\in(0,L)\),
\[
F_L(q)\le H_L(q):=\frac{2q(L-q)}{q^2+q+2(L+1)}.
\]
At fixed \(q>0\), the right side is strictly increasing in \(L>q\), since
\[
\frac{\partial H_L(q)}{\partial L}=
\frac{2q(q^2+3q+2)}{[q^2+q+2(L+1)]^2}>0.
\]
Thus \(F_L(q)\le H_\mu(q)\) and the global condition factor is bounded by \(1+\max_{0\le q\le\mu}H_\mu(q)\). Its derivative vanishes exactly at \(q_*=\sqrt{2\mu+4}-2\), which lies in \((0,\mu)\). Substitution and simplifying yields
\[
1+H_\mu(q_*)=\frac{(\sqrt{2\mu+4}-1)^2}{2\sqrt{2\mu+4}-3}.
\]
The inequalities are strict except when \(L=\mu\), \(b=1\), \(s=1\), and \(q=q_*\), proving both sharpness and the exact equality cases. Expanding this explicit formula gives the stated square-root asymptotic.

**4. Minimal four-node obstruction.** With only two sites, there is one local window term; with three sites there are two degree-one terms of the same sign on both intervals between adjacent nodes. Hence in either case the absolute values sum to the absolute value of the sum and \(\Gamma_1\equiv1\). All claims follow.

## Verification

The standalone standard-library Python program `verify.py` independently evaluates the rational terms with exact fractions, checks both outer-cell identities and the middle-cell identity on a rational grid, compares 10 mesh geometries against their exact critical-point values and the universal envelope, tests equality configurations and the square-root limit, and checks the three-node minimality statement. The saved output is in `verify_output.txt`: 7,579 checks passed. Finite tests corroborate but do not replace the preceding proof of universal quantifiers. Reproduce with `python3 verify.py`.

## Relationship to prior work

Fuda, Campagna and Hormann (first publicly released September 17, 2022) establish the denominator sensitivity factor and an all-degree mesh-ratio upper bound; their paper's degree-one bound scales quadratically in \(\mu\). The present result sharpens the first nontrivial four-node case to an *attained* \(\sqrt\mu\)-scale law, with a full gapwise optimizer classification and extremal mesh. Themistoclakis and Van Barel (first public September 17, 2024) study generalized FH approximants and error estimates on arbitrary node configurations, a different invariant. Existing work on the range overshoot or total variation of FH interpolation concerns the map from data to interpolated values, rather than the termwise denominator-sum condition factor. This theorem does not assert global novelty of the starting FH identity or general numerical-stability machinery.

## Limitations

The sharp formula is specific to exactly four nodes, degree one and evaluation within their convex hull. It is not a finite-precision lower bound for every implementation; restructured algorithms may avoid direct large-term cancellation. No claim is made about arbitrary node counts, higher FH degrees, extrapolation outside the interval, Lebesgue constants or interpolation-error rates. Historical priority against inaccessible full-text references is not conclusively settled.

## References

1. C. Fuda, R. Campagna, K. Hormann, “On the numerical stability of linear barycentric rational interpolation,” *Numerische Mathematik* 152 (2022), 761–786. First public September 17, 2022. https://doi.org/10.1007/s00211-022-01316-w
2. W. Themistoclakis, M. Van Barel, “A note on generalized Floater–Hormann interpolation at arbitrary distributions of nodes,” *Numerical Algorithms* 100 (2025), 729–744. First public September 17, 2024. https://doi.org/10.1007/s11075-024-01933-6
3. A. P. de Camargo, “On the numerical stability of Floater–Hormann’s rational interpolant,” *Numerical Algorithms* 72 (2016), 1109–1131. https://doi.org/10.1007/s11075-015-0037-z
