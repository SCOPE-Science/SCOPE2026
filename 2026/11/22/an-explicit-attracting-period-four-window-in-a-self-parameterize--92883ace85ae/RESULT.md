# An explicit attracting period-four window in a self-parameterized logistic map

## Finding
For each real control \(c\) in the entire closed interval
\[
\frac{4989}{5000}\le c\le\frac{4991}{5000}
\quad\text{(that is, }0.9978\le c\le0.9982\text{)},
\]
the self-parameterized logistic interval map
\[
F_c(x)=\left(\frac{39}{10}+\frac{x+c}{25}\right)x(1-x),\qquad 0\le x\le1,
\]
possesses a locally attracting real periodic orbit of **least period exactly four**. More precisely, with the four closed, pairwise disjoint rational intervals
\[
\begin{aligned}
I_0&=[0.03935,0.03955],& I_1&=[0.14898,0.14975],\\
I_2&=[0.50023,0.50244],& I_3&=[0.989975,0.989991],
\end{aligned}
\]
the orbit has exactly one point in each \(I_j\), traversed in the order \(I_0\to I_1\to I_2\to I_3\to I_0\). Its four-step multiplier has magnitude strictly below \(16/25\), and its Lyapunov exponent is at most \(\tfrac14\log(16/25)<0\). Thus every parameter in a nondegenerate control interval within the originally studied \([0,1]\) region has an open basin of nonchaotic attraction.

## Assumptions and scope
The state is real and belongs to \([0,1]\); the control is fixed, not re-randomized between iterations. The transformation gain and bias are the original ideal-logistic choices \(M=0.01\) and \(B=0.975\), so \(c\) denotes the *external* control and is not the transformation gain. In the original construction, the effective logistic parameter is \(M(x+c)+B\), inserted into the seed map \(4u x(1-x)\), giving the displayed cubic polynomial. These constants appear in the 2021 conference precursor and the explicit 2023 journal expression. Since the coefficient of \(x(1-x)\) lies between \(3.9\) and \(3.98\), every map sends \([0,1]\) into \([0,0.995]\), a subset of \([0,1]\).

This theorem asserts an attracting orbit, not that all other invariant sets disappear, nor that the entire parameter family is nonchaotic. A strict positive-length window suffices to rule out *uniform absence of periodic attractors* across the entire control domain.

## Proof
All interval endpoints and parameters below are exact terminating decimals, hence exact rational numbers.

**Step 1: strict cyclic trapping.** The map's derivative is
\[
F'_c(x)=\left(\frac{39}{10}+\frac c{25}\right)(1-2x)+\frac{2x-3x^2}{25}.
\]
It is strictly positive on \(I_0\) and \(I_1\), strictly negative on \(I_3\), and \(\partial_cF_c=x(1-x)/25\ge0\). Evaluating the appropriate endpoint combinations over the full control interval yields the strict certified enclosing bounds
\[
\begin{aligned}
F_c(I_0)&\subset [0.14899438,\,0.14972141]\subset\operatorname{int}I_1,\\
F_c(I_1)&\subset [0.50027712,\,0.50241377]\subset\operatorname{int}I_2,\\
F_c(I_3)&\subset [0.03943226,\,0.03949482]\subset\operatorname{int}I_0.
\end{aligned}
\]
The bounds are outward-rounded displays of exact rational comparisons; `verify.py` checks the strict rational inequalities without floating-point rounding.

On \(I_2\), set \(t=x-1/2\), so \(0.00023\le t\le0.00244\), and set \(B_c=3.92+c/25\). Exactly,
\[
F_c(x)=B_c\left(\frac14-t^2\right)+\frac t{100}-\frac{t^3}{25}.
\]
For fixed \(c\), this expression is strictly concave in positive \(t\), so its minimum is reached at an interval endpoint; moreover it increases in \(c\). For the maximum, completing the square gives
\[
F_c(x)\le\frac{B_+}{4}+\frac1{40000 B_+},
\quad B_+=3.92+\frac{0.9982}{25}.
\]
(The negative cubic term is discarded for the upper bound.) Exact rational comparisons yield
\[
0.9899788236<F_c(I_2)<0.9899883133,
\]
where interval notation means every image value lies strictly between these displayed limits. Thus \(F_c(I_2)\subset\operatorname{int}I_3\). In particular \(F_c^4(I_0)\subset\operatorname{int}I_0\).

**Step 2: uniform return contraction.** For every \(x\in[0,1]\) and every permitted control, \(|F'_c(x)|<4\), by the derivative formula and the elementary bounds \(-1\le1-2x\le1\), \(-1\le2x-3x^2\le1/3\), and \(3.9+c/25\le3.94\). For \(x\in I_2\), the centered form differentiates to
\[
F'_c(x)=\frac1{100}-2B_ct-\frac{3t^2}{25}.
\]
Using \(0.00023\le t\le0.00244\) and the exact control bounds gives
\[
-0.009326<F'_c(x)<0.008179,
\quad\text{hence}\quad |F'_c(x)|<\frac1{100}.
\]
Every orbit starting in \(I_0\) visits the four boxes cyclically, so the chain rule gives
\[
\sup_{x\in I_0}|(F_c^4)'(x)|
<4\cdot4\cdot\frac1{100}\cdot4=\frac{16}{25}<1.
\]
The contraction mapping theorem produces a unique fixed point of \(F_c^4\) in \(I_0\), attracting all of \(I_0\) under the fourth iterate. The four boxes are disjoint, so this fixed point has least period exactly four. The strict inclusion gives an open local basin. The four-step multiplier and Lyapunov bound follow from the same derivative estimate.

## Verification
The standalone Python 3 program `verify.py`, using only the standard-library `fractions.Fraction`, reproduces every strict trapping comparison and both derivative bounds using exact rational operations. Run `python verify.py`. It also performs three supplementary rational orbit calculations at the lower endpoint, midpoint and upper endpoint of the control range. The certificate requires no numerical root finder, no external dependencies and no appeal to sampling for an infinite claim. The entire uncountable control interval is covered analytically by uniform inequalities.

## Relationship to prior work
Paul, Dhungel, Sadia, Hossain, Muldrey and Hasan (ICECS 2021) introduce the state-dependent parameter transformation and report numerical wide-range chaotic behavior. Paul, Dhungel, Sadia, Hossain and Hasan (2023) state the specific ideal-logistic cubic polynomial in their Table 2 and discuss its numerical Lyapunov and bifurcation plots. Neither accessible primary text supplies this rational, positive-width attracting-four-cycle certificate or its uniform contraction bounds. A distinct 2026 mathematical record on the stochastic logistic map's four-cycle response studies a different random dynamical system, not this polynomial parameterization. Similar interval-certification methods are standard and are **not** claimed as methodological innovations; the new mathematical content is the exact dynamical obstruction for this specific previously studied model.

## Limitations
The interval is a **certified subwindow**, not necessarily the maximal period-four stability window. No classification is attempted for other parameters, all basins, or coexisting repellers. A negative Lyapunov exponent is established on the attracting orbit and its basin; this is not a statement about almost every possible initial state for every parameter. External independently reviewed priority and broader unindexed equivalent results remain unresolved. The public 2021 conference precursor identifies the family; its exact online release day has not been independently established beyond the conference's November 28–December 1, 2021 dates.

## References
1. P. S. Paul, A. Dhungel, M. Sadia, M. R. Hossain, B. Muldrey and M. S. Hasan, *Self-Parameterized Chaotic Map: A Hardware-efficient Scheme Providing Wide Chaotic Range*, 28th IEEE ICECS (2021), pp. 1–5. Public manuscript: https://confcats-event-sessions.s3.amazonaws.com/icecs21/papers/2160.pdf
2. P. S. Paul, A. Dhungel, M. Sadia, M. R. Hossain and M. S. Hasan, *Self-Parameterized Chaotic Map for Low-Cost Robust Chaos*, Journal of Low Power Electronics and Applications **13** (2023), 18. Published 2023-02-13. https://doi.org/10.3390/jlpea13010018
