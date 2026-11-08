# Sharp logarithmic CDF discrepancy and phase laws for order-two almost Golomb ratios

## Finding
For the greedy order-two almost Golomb sequence, the empirical law of the normalized values \(R_n=a(n)/n\) has a complete one-parameter family of weak subsequential limits. Every limit is an explicit pushforward measure, and the Kolmogorov discrepancy from the phase-matched limit is of the **sharp logarithmic order** \(\Theta((\log N)/N)\), uniformly over the cutoff \(N\ge4\). The exact obstruction is the count of sample ratios at or above \(3/4\):
\[
\#\{1\le n\le N:R_n\ge3/4\}=\lfloor\log_2(N-1)\rfloor+\lfloor\log_2N\rfloor\qquad(N\ge4).
\]

## Assumptions and scope
Let \(a(1)=1\) and let \(a\) be the earliest nondecreasing positive-integer sequence satisfying the order-two almost Golomb relation \(a(a(n)+a(n-1))=n\) (with \(a(0)=0\)); here \(a(2)=a(3)=2\). Put \(R_n=a(n)/n\) and \(\nu_N=N^{-1}\sum_{n=1}^N\delta_{R_n}\), for all integers \(N\ge1\). For a probability law \(\rho\), write \(F_\rho(y)=\rho(( -\infty,y])\) and \(d_K(\rho,\sigma)=\sup_{y\in\mathbb R}|F_\rho(y)-F_\sigma(y)|\).

On \([1,2]\) define the continuous piecewise-rational function
\[
h(t)=\begin{cases}\frac12+\frac1{4t},&1\le t\le\frac32,\\1-\frac1{2t},&\frac32\le t\le2.\end{cases}
\]
For \(1\le\theta\le2\), define the probability measure
\[
\mu_\theta=\frac{h_\#\operatorname{Leb}_{[1,2]}+h_\#\operatorname{Leb}_{[1,\theta]}}{\theta}.
\]
The \(\operatorname{Leb}\) measures are **unnormalized** restrictions of ordinary one-dimensional Lebesgue measure; the numerator has total mass \(\theta\). Set \(\mu=\mu_1=\mu_2\).

For every \(N\ge4\), let \(K=\lfloor\log_2N\rfloor\) and \(\theta_N=N/2^K\). The claims are:
\[
\boxed{\frac{\lfloor\log_2(N-1)\rfloor+\lfloor\log_2N\rfloor}{N}\le d_K(\nu_N,\mu_{\theta_N})\le\frac{30(K+1)}N.}
\]
The set of all weak subsequential limits of \(\nu_N\) as \(N\to\infty\) is precisely \(\{\mu_\theta:1\le\theta\le2\}\), containing uncountably many distinct laws.

## Proof
**1. Exact arithmetic input.** Proposition 3.1 of Cloitre–Joshi supplies, for every integer \(k\ge2\), \(B=2^k\), and \(0\le j<B\),
\[
a(B+j)=\begin{cases}\frac{3B}{4}+\lceil j/2\rceil,&0\le j\le B/2,\\ B/2+j,&B/2<j<B.\end{cases}
\]
It follows by direct division that
\[
R_{B+j}=h(1+j/B)+\epsilon_{B,j},\qquad 0\le\epsilon_{B,j}\le\frac1{2B},
\]
where the error is zero except when \(j\) is odd and \(j\le B/2\), in which case \(\epsilon_{B,j}=1/[2(B+j)]\). This relation is exact, not asymptotic.

**2. Continuous phase law.** The range of \(h\) is \([2/3,3/4]\). For \(y\) strictly between the endpoints, the two preimages of \(y\) are
\[
u(y)=\frac1{4(y-1/2)}\in(1,3/2),\qquad v(y)=\frac1{2(1-y)}\in(3/2,2).
\]
Consequently the base cumulative distribution function is
\[
F(y)=\begin{cases}0,&y<2/3,\\ v(y)-u(y),&2/3\le y\le3/4,\\1,&y>3/4.\end{cases}
\]
Within the middle interval, the values at the endpoints are defined by continuity. The density on the open interval is
\[
F'(y)=\frac1{4(y-1/2)^2}+\frac1{2(1-y)^2}.
\]
For the phase law the additional mass from \([1,\theta]\) gives the explicit CDF
\[
F_\theta(y)=\frac{F(y)+\bigl[\min(\theta,3/2)-u(y)\bigr]_++\bigl[\min(\theta,v(y))-3/2\bigr]_+}{\theta}
\]
for \(2/3<y<3/4\), extended by \(0\) to the left and \(1\) to the right. Here \([x]_+=\max\{0,x\}\); at endpoints take continuous limits. In particular \(F_1(7/10)=5/12\) whereas \(F_{3/2}(7/10)=4/9\), and as \(\theta\) moves from \(1\) to \(5/4\) the same CDF value changes continuously and strictly; hence there are uncountably many distinct phase laws.

**3. Uniform Kolmogorov upper bound.** Fix \(y\in\mathbb R\). On each half of \([1,2]\), the function \(h\) is monotone, with \(|h'(t)|\ge1/9\). Consider a complete or truncated dyadic block \(B\le n<B+J\) with \(0\le J\le B\). Comparing the grid \(\{1+j/B:0\le j<J\}\) with the corresponding Lebesgue subinterval \([1,1+J/B]\), an interval on each monotone branch incurs at most one unit of quadrature error. Thus the count of grid points with \(h(1+j/B)\le y\) differs from \(B\operatorname{Leb}\{t\in[1,1+J/B]:h(t)\le y\}\) by at most \(2\). Replacing \(h\) by \(R_{B+j}\) only changes indicators if \(h(1+j/B)\in(y-1/(2B),y]\). Because the inverse branches are \(9\)-Lipschitz, this strip contains no more than \(6\) grid points on either monotone branch. The total discrepancy in any complete or truncated block is therefore at most \(14\), uniformly in \(B,J,y\).

Decompose \(\{1,\ldots,N\}\) into the three initial indices, the complete dyadic blocks \(2^k\le n<2^{k+1}\), \(2\le k<K\), and the final truncated block \(2^K\le n\le N\). The continuous analog contributes \((2^K-4)F(y)+2^K\operatorname{Leb}\{t\in[1,1+(N-2^K+1)/2^K]:h(t)\le y\}\). This differs from \(NF_{\theta_N}(y)=2^KF(y)+2^K\operatorname{Leb}\{t\in[1,\theta_N]:h(t)\le y\}\) by at most \(5\). Including the first three terms and the \(K-1\) dyadic blocks gives
\[
|NF_{\nu_N}(y)-NF_{\mu_{\theta_N}}(y)|\le14(K-1)+8\le30(K+1).
\]
The estimate holds for every \(y\), so taking the supremum yields the stated upper bound. The finitely many initial and low-block cases also satisfy this bound.

**4. Exact endpoint defect and sharpness.** The initial normalized values are \(R_1=R_2=1\), \(R_3=2/3\). In each dyadic block \(n=B+j\), \(k\ge2\), direct comparison in the formulas of Step 1 shows that \(R_n=3/4\) holds **exactly** at \(j=0\), and \(R_n>3/4\) holds **exactly** at \(j=1\). At every other index in the block \(R_n<3/4\). For any integer \(N\ge4\), there are \(\lfloor\log_2N\rfloor-1\) powers \(2^k\) with \(k\ge2\) not exceeding \(N\), and \(\lfloor\log_2(N-1)\rfloor-1\) successors \(2^k+1\) not exceeding \(N\), as well as the two initial exceedances. Hence
\[
\#\{n\le N:R_n\ge3/4\}=\lfloor\log_2N\rfloor+\lfloor\log_2(N-1)\rfloor.
\]
Every \(\mu_\theta\) has support in \([2/3,3/4]\) and no atom at \(3/4\). Taking \(y\uparrow3/4\) in the two CDFs makes their difference **exactly** the above count divided by \(N\). This proves the lower bound and its logarithmic sharp order.

**5. Exhaustion of weak limits.** The Kolmogorov upper bound tends to zero, uniformly as \(N\to\infty\). Every sequence \(N\to\infty\) has a subsequence along which \(\theta_N\to\theta\in[1,2]\); continuity of pushforward integrals and \(\theta\mapsto\mu_\theta\) then yields \(\nu_N\Rightarrow\mu_\theta\). Conversely, take \(N_j=\lfloor\theta2^j\rfloor\) for \(1\le\theta<2\), and \(N_j=2^{j+1}-1\) for \(\theta=2\); these realize every prescribed \(\mu_\theta\). This proves the complete classification.

## Verification
The standalone standard-library script `verify_almost_golomb.py` computes the explicit integer terms and checks the self-referential recurrence through index \(16382\), exact rational CDFs for \(308\) parameter/threshold combinations, \(4950\) further thresholds, and the exact endpoint count for every \(4\le N\le5000\). It uses exact integer and rational arithmetic. Run `python3 verify_almost_golomb.py`. These computations corroborate finite cases; the five proof steps establish the statements for all \(N\) and all phases.

## Relationship to prior work
Cloitre and Joshi, *Almost Golomb Sequences*, arXiv:2604.02404v2, derive the exact order-two dyadic formula and show that \(a(n)/n\) has no pointwise limit. The present result uses that formula as its input but determines new normalized **empirical probability measures**, all their phase-indexed weak limits, the rational CDF/density, an exact cutoff-dependent endpoint anomaly, and the optimal Kolmogorov error order. These distributional statements and the exact boundary count were not identified in the inspected source. Cloitre's *Beatty solutions of almost Golomb equations*, arXiv:2604.10822v4, concerns different Beatty-type solutions, not the greedy empirical ratios. OEIS A394217 records the sequence and dyadic formula but not the phase-law classification or discrepancy. These distinctions do not exclude unpublished or older equivalent calculations.

## Limitations
This is an analysis of the greedy **order-two** sequence only; it makes no claim for higher-memory almost Golomb sequences. The upper discrepancy constant \(30\) is explicit but not asserted optimal. The logarithmic rate is sharp in order, not in its exact leading constant. The new distribution results depend on the previously published dyadic formula; mathematical and historical-priority assessment has not been independently audited. Experimental checks alone do not prove unbounded-index statements.

## References
1. B. Cloitre and G. Joshi, *Almost Golomb Sequences*, arXiv:2604.02404v2, especially Proposition 3.1, https://arxiv.org/abs/2604.02404 . First public version: 2026-04-02.
2. B. Cloitre, *Beatty solutions of almost Golomb equations*, arXiv:2604.10822v4, https://arxiv.org/abs/2604.10822 .
3. OEIS A394217, *Earliest monotonic sequence satisfying the order-two almost Golomb recurrence*, https://oeis.org/A394217 .
