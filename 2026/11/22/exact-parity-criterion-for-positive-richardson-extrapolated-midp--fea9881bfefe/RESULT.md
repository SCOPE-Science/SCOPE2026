# Exact parity criterion for positive Richardson-extrapolated midpoint quadrature

## Finding
For every positive-depth integer-divisibility chain of composite midpoint rules, strict positivity of **every collected sample weight** has a complete characterization by the parities of the successive refinements. Nonnegative-weight extrapolation is possible with mixed even and odd refinements, but an even refinement at the wrong level forces a negative weight. The theorem also identifies the exact negative sample-weight mass, the sharp absolute-error amplification norm, and the largest sample weight in every regime.

Specifically, let \(d\ge1\) and \(N_0\mid N_1\mid\cdots\mid N_d\), with strictly increasing positive integers and \(r_i=N_i/N_{i-1}\ge2\) for \(1\le i\le d\). Write \(M_N(f)=N^{-1}\sum_{k=0}^{N-1}f((k+1/2)/N)\). Let \(Q_d=\sum_{j=0}^d c_jM_{N_j}\) be uniquely determined by
\[
\sum_{j=0}^d c_j=1,\qquad \sum_{j=0}^dc_jN_j^{-2q}=0\quad(1\le q\le d).
\]
After collecting coincident physical sample nodes, all weights of \(Q_d\) are strictly positive **if and only if**
\[
\boxed{\quad r_i\text{ even}\ \Longrightarrow\ i\not\equiv d\pmod 2\quad\text{for every }1\le i\le d.\quad}
\]
Thus all-odd chains are positive; mixed parity chains may also be positive. For example, the chains \((N_0,N_1,N_2)=(1,2,6)\) and \((N_0,N_1,N_2,N_3)=(1,3,6,18)\) are positive, while \((1,2)\) and \((1,3,6)\) are not.

Partition the level indices \(0,\dots,d\) into maximal consecutive blocks \([s,t]\) separated exactly at even refinement ratios. Call a block *bad* when \(d-t\) is odd. Then the sum of absolute values of negative collected weights and the sharp norm of the rule are, respectively,
\[
\boxed{H=-\sum_{[s,t]\ \mathrm{bad}}\ \sum_{j=s}^t c_j,\qquad \sum_{x}|w_x|=1+2H.}
\]
The **largest positive collected weight**, regardless of sign defects in other blocks, is attained precisely at points first appearing on the final grid and equals
\[
\boxed{\max_x w_x=\frac1{N_d}\prod_{j=0}^{d-1}\left(1-\left(\frac{N_j}{N_d}\right)^2\right)^{-1}.}
\]
Each rule is exact for every polynomial of degree at most \(2d+1\).

## Assumptions and scope
Every rule is the ordinary composite midpoint rule on \([0,1]\) in exact arithmetic. The depth \(d\) is finite but arbitrary. The panel counts \(N_j\) are positive integers with strictly increasing exact divisibility; no fixed refinement ratio, bounded depth, asymptotics, regularity of sample values, or error distribution is assumed. A *collected weight* combines only actual coincident nodes; interpolating values between distinct grids is not permitted. The sharp norm is the operator norm from bounded *absolute* perturbations of the physical sampled values to output error. For an interval \([a,b]\), the same positivity criterion holds and weights and norm are multiplied by \(b-a\).

## Proof
**1. Extrapolation coefficients.** Put \(x_j=N_j^{-2}\). They satisfy \(x_0>x_1>\cdots>x_d>0\) and \(x_{j+1}\le x_j/4\). The moment conditions say that evaluation at zero for polynomials in \(x\) through degree \(d\) is represented by Lagrange weights
\[
c_j=\prod_{k\ne j}\frac{-x_k}{x_j-x_k}=\prod_{k\ne j}\frac{N_j^2}{N_j^2-N_k^2},\quad \operatorname{sgn}(c_j)=(-1)^{d-j}.
\]
Define \(b_j=|c_j|/N_j=|c_j|\sqrt{x_j}\).

**2. Strict growth of the absolute coefficients per sample.** Direct cancellation of the Lagrange products gives
\[
\frac{b_{j+1}}{b_j}=\sqrt{\frac{x_j}{x_{j+1}}}\prod_{k\ne j,j+1}\frac{|x_j-x_k|}{|x_{j+1}-x_k|}.
\]
Every factor with \(k>j+1\) is greater than one. For \(k<j\), set \(X=x_k/x_j\ge4^{j-k}\) and \(y=x_{j+1}/x_j\le1/4\). Its factor satisfies
\[
\frac{X-1}{X-y}>1-X^{-1}\ge1-4^{-(j-k)}.
\]
The initial square root is at least two. For \(j\ge1\), therefore,
\[
\frac{b_{j+1}}{b_j}>2\prod_{q=1}^{j}(1-4^{-q})\ge 2\left(1-\sum_{q=1}^{\infty}4^{-q}\right)=\frac43>1.
\]
For \(j=0\), the product has no earlier factors and \(b_1/b_0\ge2\). Thus \(0<b_0<b_1<\cdots<b_d\). Consequently every nonempty alternating tail \(\sum_{j=m}^t c_j/N_j\) has the strict sign of its final term, namely \((-1)^{d-t}\), and absolute value at most \(b_t\), with strict inequality whenever \(m<t\). This follows by pairing successive terms starting from the largest magnitude.

**3. Coincident midpoint grids and block structure.** For integers \(N\mid N'\), a coarse midpoint \((2k+1)/(2N)\) is a fine midpoint exactly when
\[
2\ell+1=(N'/N)(2k+1)
\]
for some integer \(\ell\). This is possible for every coarse node if \(N'/N\) is odd, and impossible for every coarse node if that ratio is even. Hence two levels in distinct blocks never share a midpoint, whereas within a block every earlier grid is nested in every later grid. For a node whose first level within block \([s,t]\) is \(m\), the exact collected weight is
\[
w_x=\sum_{j=m}^{t}\frac{c_j}{N_j}.
\]
It is nonzero and has the fixed sign \((-1)^{d-t}\) by step 2. All blocks end with at least one node first appearing on their terminal grid, so every bad block creates a genuine negative weight. Strict positivity holds exactly when no block is bad. Every nonfinal block ends at \(t=i-1\) for an even refinement at position \(i\), so its sign is positive exactly when \(d-(i-1)\) is even, equivalently \(i\not\equiv d\pmod2\). The final block ends at \(d\) and is always positive. This proves both directions of the parity criterion.

**4. Exact negative mass, norm, and maximal weight.** Within a bad block \([s,t]\), all collected weights are negative. Summing its weights over its distinct nodes recovers \(\sum_{j=s}^t c_j\), because every midpoint level samples a constant with total weight one. Blocks have disjoint node sets. Summing the negatives gives the claimed formula for \(H\). Since \(\sum_jc_j=1\), the total collected weight is one, hence \(\sum_x|w_x|=1+2H\). This operator norm is attained by bounded perturbations with each sign matching its sample weight. At every node newly introduced at level \(d\), the weight is exactly \(c_d/N_d=b_d\). Every other positive collected weight belongs to an earlier-started tail with size strictly below its terminal \(b_t\le b_d\), so \(b_d\) is the strict overall maximum away from final-level new nodes. The Lagrange formula yields
\[
b_d=\frac{c_d}{N_d}=\frac1{N_d}\prod_{j=0}^{d-1}\left(1-\frac{N_j^2}{N_d^2}\right)^{-1}.
\]

**5. Polynomial exactness.** For a polynomial \(p\) of degree at most \(2d+1\), the midpoint Euler–Maclaurin identity gives
\[
M_N(p)-\int_0^1p(x)\,dx=\sum_{q=1}^{d} A_q(p)N^{-2q};
\]
there is no remainder because \(p^{(2d+2)}=0\). The moment conditions eliminate all \(d\) powers, and \(\sum_jc_j=1\). Thus \(Q_d(p)=\int_0^1p(x)\,dx\). \(\square\)

## Verification
The standalone Python standard-library verifier `artifacts/verify.py` uses exact rational arithmetic. It checks 680 strictly increasing divisibility chains built with starting panel counts 1 or 2, depths 1 through 4, and ratios in \(\{2,3,4,5\}\). It directly constructs and collects every midpoint weight and checks the parity criterion, exact negative-mass block sum, largest-weight identity, total-variation norm, coefficient growth, weight sum, and polynomial moments through degree five. Five illustrative chains additionally pass every polynomial moment through their full asserted \(2d+1\) degree. Execution output appears in `artifacts/verification.txt`. These finite checks corroborate, but do not replace, the universally quantified proof.

For \((1,2)\), the extrapolation coefficients \((-1/3,4/3)\) yield a negative central weight \(-1/3\), so the norm is \(5/3\). For \((1,2,6)\), the coefficients are \((1/105,-1/6,81/70)\) and all collected weights are positive, with largest weight \(27/140\). For \((1,3,6)\), the exact total negative mass is \(13/35\), and the sharp norm is \(61/35\).

## Relationship to prior work
The midpoint rule, polynomial Richardson conditions, Euler–Maclaurin even-power expansion, and positive classical Romberg extrapolation are established. Berrut and Trummer (2022) explicitly describe the half-cell offset defining midpoint Riemann sums and discuss extrapolation, but their inspected construction is directed at piecewise-smooth quadrature with jumps; it does not state the all-integer-chain sign classification for collected midpoint weights. Farzi (2014), Section 3.1, analyzes positivity for **composite trapezoidal** extrapolates and Romberg/Bauer/Bulirsch panel sequences. Two published findings on generalized Romberg quadrature for arbitrary integer refinement factors (2026-09-21 and 2026-10-13) prove positivity for the **closed composite trapezoidal** rules. Their coefficient formulas and the increasing-alternating-magnitude method are analogous and are not new here. Unlike nested closed trapezoidal grids, midpoint node grids separate when a refinement ratio is even; neither earlier result implies the alternating **block-sign parity criterion**, exact negative mass, or the coexistence of positive and negative midpoint refinement patterns. The earlier classical Romberg article by de Camargo (2022) was available only through its abstract and notes, and is a priority uncertainty, not a fully inspected negative comparison.

## Limitations
The parity criterion requires the ordinary half-cell midpoint offset, exact integer-divisibility panel counts, and cancellation of all even powers through depth \(d\). It does not hold verbatim for other offsets, arbitrary nonnested panel counts, arbitrary rational extrapolants, or numerical cancellation in a recursive floating-point tableau. The norm treats independently bounded absolute errors at final distinct nodes; it is not a stochastic-variance, correlated-noise, or floating-point-forward-error theorem. The result is not a superiority claim over trapezoidal Romberg, Gaussian, or Clenshaw–Curtis quadrature. Older generalized-extrapolation literature may contain an equivalent formula under different terminology; independent historical-priority review remains outstanding.

## References
1. J.-P. Berrut and M. R. Trummer, *Extrapolation quadrature from equispaced samples of functions with jumps*, Numerical Algorithms 92 (2023), 65–88, first published 19 December 2022, https://doi.org/10.1007/s11075-022-01462-0.
2. J. Farzi, *Generalized extrapolation methods for solving nonlinear Fredholm integral equations*, Mathematical Communications 19 (2014), 375–390, §3.1, https://www.mathos.unios.hr/mc/index.php/mc/article/view/619/224.
3. A. P. de Camargo, *A Chebyshev-Markov-Stieltjes separation type theorem for classical Romberg quadrature*, Numerical Algorithms 92 (2023), 2365–2376, first published 21 September 2022, https://doi.org/10.1007/s11075-022-01393-w. Abstract and notes inspected; full text unavailable.
4. *Positive-weight Richardson–Romberg quadrature on nested integer refinement chains*, published mathematical finding (13 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-positive-weight-richardson-romberg-quadrature-on-every-nested-in--663b06718b7c.
5. *Positive-weight generalized Romberg quadrature for every integer refinement factor*, published mathematical finding (21 September 2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/21/SCOPE-generalized-romberg-positive-weights-integer-refinement--b7c2819b6648.
6. A. Sidi, *A Complete Convergence and Stability Theory for a Generalized Richardson Extrapolation Process*, SIAM J. Numer. Anal. 34 (1997), https://doi.org/10.1137/S0036142994278589.
