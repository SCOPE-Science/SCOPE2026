# Sharp origin-mode transition and large separated modal coexistence in Poisson–Mirra counts

## Finding

For the two-parameter Poisson–Mirra (PMiD) count law, the full sharp parameter boundary at which count zero ceases to be a global mode is an explicitly finite minimization over integer competitors. There are exact parameters at which counts zero and six, and no other counts, are simultaneous global modes. Moreover, as the rate approaches zero, the competing modal count at the *first* transition diverges on the inverse-rate scale, and the transition shape parameter has a sharp quadratic scaling constant.

Let \(\theta,\alpha>0\), \(q=(1+\theta)^{-1}\), \(b=\alpha/[2(1+\theta)^2]\), and \(T_k=(k+1)(k+2)\) for integers \(k\ge0\). Put
\[
 p_k=\frac{\theta^3}{(\theta^2+\alpha)(1+\theta)}q^k(1+bT_k).
\]
This is the normalized PMiD probability mass function. If \(\theta\ge2\), then \(p_0>p_k\) for every \(k\ge1\) and every \(\alpha>0\). If \(0<\theta<2\), define the **finite, nonempty** set
\[
 I_\theta=\{k\in\mathbb N:k\ge1,\ q^k(k+1)(k+2)>2\},\qquad
 B(\theta)=\min_{k\in I_\theta}\frac{1-q^k}{q^k(k+1)(k+2)-2},
 \qquad A(\theta)=2(1+\theta)^2B(\theta).
\]
Then **count zero is the unique global mode if and only if \(0<\alpha<A(\theta)\)**; at equality it is a global mode tied with at least one positive count; and for \(\alpha>A(\theta)\) it is not a global mode. The equality case has no other nonzero global competitors except the minimizers in the displayed finite formula.

At the exact rational parameters
\[
 \boxed{\theta=\tfrac15,\quad \alpha=\tfrac{279279}{2442775},\quad q=\tfrac56,\quad b=\tfrac{31031}{781688}},
\]
\(p_0=p_6>p_k\) for **all** \(k\notin\{0,6\}\). This is the sharp first transition at that rate, not merely two separated local peaks.

Finally let \(x_*>0\) be the unique positive solution of \(x_*=2(1-e^{-x_*})\). For every choice of minimizer \(k_\theta\in\arg\min_{k\in I_\theta}(1-q^k)/(q^kT_k-2)\),
\[
 \boxed{\theta k_\theta\longrightarrow x_*\approx1.59362426004004,\qquad
 \frac{A(\theta)}{\theta^2}\longrightarrow
 \frac{2(e^{x_*}-1)}{x_*^2}\approx3.08827730474174}\qquad (\theta\downarrow0).
\]
Thus the first change in the global modal count can jump a distance of order \(1/\theta\), even while \(\alpha\) is only of order \(\theta^2\).

## Assumptions and scope

The model is supported on \(\mathbb N_0\) with **strictly positive** \(\theta\) (rate) and \(\alpha\) (shape). The symbol *global mode* means an integer maximizing \(p_k\) over the entire infinite support, rather than a local maximum of adjacent probabilities. At \(\theta\ge2\), the origin result includes the endpoint \(\theta=2\). At \(0<\theta<2\), the threshold formula covers the complete comparison between zero and every positive count but does not assert which positive count maximizes the mass after zero loses globally. The asymptotic claim concerns any minimizer of this specific threshold comparison, not arbitrary local modes.

The first public model paper was published 21 April 2022. The model's first listed classification is MSC2020 \(60\mathrm E05\).

## Proof

**1. Normalization and reduction.** The model's Poisson-mixture integral yields the displayed \(p_k\); it is also straightforward to check the total mass, because
\[
 \sum_{k\ge0}q^k=\frac1{1-q},\qquad
 \sum_{k\ge0}(k+1)(k+2)q^k=\frac2{(1-q)^3}.
\]
With \(C=\theta^3/[(\theta^2+\alpha)(1+\theta)]\), substitution into \(C[(1-q)^{-1}+2b(1-q)^{-3}]\) gives one. All origin comparisons therefore reduce to positive multiples of \(q^k(1+bT_k)\).

**2. Sharp boundary and finite candidate set.** For every \(k\ge1\), direct subtraction gives
\[
 \frac{p_k-p_0}{C}=-(1-q^k)+b(q^kT_k-2).
\]
When \(q^kT_k\le2\), the right side is strictly negative for every \(b>0\). For \(\theta\ge2\), \(q\le1/3\), and \(q^kT_k\le6q\le2\) for all \(k\ge1\), since
\[
 \frac{q^{k+1}T_{k+1}}{q^kT_k}=q\frac{k+3}{k+1}<1\qquad(k\ge1).
\]
Thus the origin is always uniquely global there. For \(0<\theta<2\), \(q>1/3\), so \(qT_1=6q>2\), proving nonemptiness of \(I_\theta\). Its finiteness follows from \(q^kT_k\to0\). For every \(k\in I_\theta\), \(p_k\ge p_0\) exactly when \(b\ge(1-q^k)/(q^kT_k-2)\). Taking the finite minimum establishes the three sharp boundary cases, including the full set of equality competitors.

**3. A genuine separated global tie with a closed tail certificate.** Put \(\theta=1/5\), \(q=5/6\). Equating the unnormalized masses at zero and six gives
\[
 b=\frac{1-q^6}{56q^6-2}=\frac{31031}{781688},\qquad \alpha=2(1+\theta)^2b=\frac{279279}{2442775}.
\]
Successive differences satisfy the exact identity
\[
 \operatorname{sgn}(p_{k+1}-p_k)=
 \operatorname{sgn}\bigl(b(k+2)[2-\theta(k+1)]-\theta\bigr)
 =\operatorname{sgn}\bigl(b(k+2)(9-k)-1\bigr).
\]
For \(k=0,1\) the factors \((k+2)(9-k)\) equal \(18,24\), below \(1/b\). For \(k=2,3,4,5\) they equal \(28,30,30,28\), above \(1/b\). For every \(k\ge6\), the factor is at most \(24\), so the successive differences are strictly negative forever. Hence
\[
 p_0>p_1>p_2<p_3<p_4<p_5<p_6>p_7>p_8>\cdots.
\]
The exact equality \(p_0=p_6\) makes these and only these counts global modes. Further, the finitely many positive-peak sign tests and the uniform quadratic bound for the entire tail remain strict in a neighborhood of \(b\); hence the only possible global modes nearby are zero and six. Their masses cross strictly as \(b\) passes the displayed value, so zero is uniquely global immediately below and six uniquely global immediately above. The infinite-support assertion follows from the polynomial sign for **all** \(k\ge6\), not a finite scan.

**4. Small-rate scaling and diverging first modal jump.** Write \(s=\log(1+\theta)\); the finite minimand can equivalently be written
\[
 B_k(\theta)=\frac{e^{ks}-1}{(k+1)(k+2)-2e^{ks}}
\]
where the denominator is strictly positive exactly for \(k\in I_\theta\). For any sequence \(\theta\downarrow0\) and positive integers \(k=k(\theta)\) with \(k\theta\to x\in(0,\infty)\), the denominator is positive eventually and
\[
 \frac{B_k(\theta)}{\theta^2}\longrightarrow f(x)=\frac{e^x-1}{x^2}.
\]
Using \(k=\lfloor x/\theta\rfloor\) supplies a uniform upper bound of order \(\theta^2\) for the minimum. Its minimizing indices cannot escape either end of the \(k\theta\)-axis: because the denominator is at most \(T_k\),
\[
 \frac{B_k(\theta)}{\theta^2}\ge
 \frac{e^{ks}-1}{\theta^2(k+1)(k+2)}.
\]
For \(0<\theta\le1\), \(\theta/2\le s\le\theta\). If \(k\theta\to0\), use \(e^{ks}-1\ge ks\ge k\theta/2\): the lower bound diverges as \(1/(k\theta)\) up to a bounded positive factor, uniformly also for bounded \(k\). If \(k\theta\to\infty\), use \(e^{ks}-1\ge e^{k\theta/2}-1\): it dominates the quadratic denominator. Therefore every minimizer obeys \(0<c\le k\theta\le C<\infty\) along small rates. Compactness and the pointwise scaling on these rescaled compact intervals reduce the minimizer limit to the unique global minimizer of \(f\).

Now \(f(x)\to\infty\) both as \(x\downarrow0\) and \(x\to\infty\). Its derivative has the sign of \((x-2)e^x+2\); this expression decreases from zero, has its unique interior minimum before \(x=1\), and then rises to infinity. It consequently has exactly one strictly positive zero \(x_*\in(1,2)\), satisfying \(x_*=2(1-e^{-x_*})\). Hence \(k_\theta\theta\to x_*\), and the minimum divided by \(\theta^2\) tends to \(f(x_*)\). Finally \(A(\theta)=2(1+\theta)^2B(\theta)\), proving the stated constant.

## Verification

Run the accompanying Python standard-library program `checker.py`. It reproduces the rational equality \(p_0=p_6\), all relevant adjacent-difference inequalities, the normalization, the exact finite candidate minimization at \(\theta=1/5\), rational parameter-side checks, and finite-rate asymptotic diagnostics. Its current execution passes 1192 assertions. The proof above supplies the infinite tail and limiting-minimizer arguments: a finite list of numerical checks alone would establish neither.

## Relationship to prior work

Maya et al. (2022), Sections 3.1–3.2, give the two-parameter PMiD mass function and quadratic necessary inequalities for *local* modes; their discussion describes the absence of a bimodal feature as a possible limitation. The earlier one-parameter Poisson–xgamma law of Altun, Cordeiro and Ristić (first published 9 February 2021) is the diagonal specialization \(\alpha=\theta\), and its Proposition 2 **already identifies** a decrease–increase–decrease configuration and two local peaks for certain parameters. Therefore the existence of two local peaks is not asserted to be new. The new claim is the **sharp global origin-mode boundary for independent \(\alpha,\theta\)**, an exact globally tied and nonadjacent pair, and the \(\alpha\asymp\theta^2\) / modal-distance \(1/\theta\) transition inaccessible along the diagonal \(\alpha=\theta\). The 2022 paper's local quadratic inequalities do not give these complete global comparisons or the asymptotic first-crossing result. Other published findings on modal jumps in compound Poisson laws concern different probability families and do not imply this threshold formula.

## Limitations

This result does not classify every successive positive-to-positive modal transition after zero stops being global. It proves the onset of nonzero global dominance and the precise first transition at the rational example, not uniqueness of the positive competitor at every real \(\theta\). The limiting scale does not give a uniform finite-rate error constant. The earlier Poisson–xgamma paper covers qualitative local bimodality in a special subfamily; no claim is made to discover that phenomenon anew. Independent historical-priority and independent mathematical reviews remain outstanding.

## References

1. R. Maya, M. R. Irshad, C. Chesneau, S. L. Nitin and D. S. Shibu, “On Discrete Poisson–Mirra Distribution: Regression, INAR(1) Process and Applications,” *Axioms* **11** (2022), 193, first public 21 April 2022, https://doi.org/10.3390/axioms11050193 .
2. E. Altun, G. M. Cordeiro and M. M. Ristić, “An one-parameter compounding discrete distribution,” *Journal of Applied Statistics* **49** (2022), 1935–1956, first public 9 February 2021, https://doi.org/10.1080/02664763.2021.1884846 ; accessible full text https://pmc.ncbi.nlm.nih.gov/articles/PMC9225500/ .
