# Sharp maximum-offspring laws for subtractive random forests

## Finding

In the subtractive random forest, integer vertex \(t\geq1\) independently attaches to its parent \(t-Z_t\), where the delays \(Z_t\) are iid positive integers with masses \(q_j=\Pr(Z_t=j)>0\). For a positive vertex \(v\) let
\[
D_n(v)=\sum_{j=1}^{n-v}\mathbf1\{Z_{v+j}=j\},\qquad
D_\infty(v)=\sum_{j=1}^{\infty}\mathbf1\{Z_{v+j}=j\},
\]
with an empty finite sum interpreted as zero. Set \(M_n=\max_{1\leq v\leq n}D_n(v)\) and \(\widehat M_n=\max_{1\leq v\leq n}D_\infty(v)\).

**Theorem (two sharp degree universality classes).** Each of the following assumptions separately implies the stated pair of almost-sure limits:

1. If for some \(\beta,c>0\), \(\lim_{j\to\infty}-\log q_j/j^\beta=c\), then
\[
\frac{M_n}{((\beta+1)\log n/c)^{1/(\beta+1)}}\longrightarrow1,
\qquad
\frac{\widehat M_n}{((\beta+1)\log n/c)^{1/(\beta+1)}}\longrightarrow1
\quad\text{almost surely}.
\]
2. If for some \(s>1\), \(\lim_{j\to\infty}-\log q_j/\log j=s\), then
\[
\frac{M_n}{\log n/(s\log\log n)}\longrightarrow1,
\qquad
\frac{\widehat M_n}{\log n/(s\log\log n)}\longrightarrow1
\quad\text{almost surely}.
\]

Thus geometric delays \(q_j=(1-a)a^{j-1}\), \(0<a<1\), give the sharp limit \(M_n\sim\sqrt{2\log n/\log(1/a)}\) almost surely, while power-law masses \(q_j\asymp j^{-s}\), \(s>1\), give the strict factor \(1/s\) in the classical \(\log n/\log\log n\) growth scale. The result sharpens the distribution-free upper bound of Broutin, Devroye, Lugosi and Oliveira for these natural delay classes.

## Assumptions and scope

Every \(Z_t\) is independently drawn from the same full-support mass function \((q_j)_{j\geq1}\) on the positive integers, with \(\sum_{j\geq1}q_j=1\). The forest contains every integer \(v\leq0\) as an initial root and one parent edge \((t,t-Z_t)\) for every positive \(t\); only *offspring counts of positive vertices* enter the maxima. Degrees here mean numbers of children, not undirected degrees including the parent. The almost-sure assertions refer to a single infinite iid delay sequence, and require no finite mean for the delay distribution. The first alternative includes \(q_j\) with logarithmic stretched-exponential asymptotics; the second includes slowly varying modifications of power-law masses. A mass with zeros or a tail outside both alternatives is not claimed to be covered.

## Proof

**1. The one-vertex law.** Fix \(v\geq1\). Since different child candidates \(v+j\) use different independent delays, the variables \(\mathbf1\{Z_{v+j}=j\}\), \(j\geq1\), are independent Bernoulli variables with parameters \(q_j\). Therefore
\[
D_\infty(v)\overset d=D:=\sum_{j\geq1}B_j,
\quad B_j\sim\operatorname{Ber}(q_j)\ \text{independently}.
\]
The sum is finite almost surely because \(\sum q_j=1\), and for every \(z\geq1\),
\[
\mathbb E z^D=\prod_{j\geq1}\bigl(1+(z-1)q_j\bigr).
\]
For any integer \(k\geq1\), all of the first \(k\) trials being successful implies \(D\geq k\); hence
\[
\Pr(D\geq k)\geq p_k:=\prod_{j=1}^kq_j.\tag{1}
\]

**2. Stretched-exponential one-vertex tail.** Suppose \(-\log q_j/j^\beta\to c\), with \(\beta,c>0\). Summing logarithms in (1), using \(\sum_{j=1}^k j^\beta\sim k^{\beta+1}/(\beta+1)\), shows
\[
\liminf_{k\to\infty}\frac{\log\Pr(D\geq k)}{k^{\beta+1}}\geq-\frac{c}{\beta+1}.\tag{2}
\]
To obtain the matching bound, fix \(u\in(0,c)\). There is a finite \(C\geq1\) such that \(q_j\leq C e^{-u j^\beta}\) for every \(j\). Take \(t=e^{u k^\beta}\). Markov's inequality applied to \((1+t)^D\) gives
\[
\Pr(D\geq k)\leq (1+t)^{-k}\prod_{j\geq1}(1+tq_j).\tag{3}
\]
For \(j\leq k\), \(\log(1+tq_j)\leq u(k^\beta-j^\beta)+\log(1+C)\). For \(k<j\leq2k\), the same logarithm is at most \(\log(1+C)\). For \(j>2k\), it is bounded by \(C e^{-u(1-2^{-\beta})j^\beta}\), whose sum is bounded independently of \(k\). Consequently
\[
\log\prod_{j\geq1}(1+tq_j)
\leq u k^{\beta+1}-u\sum_{j=1}^k j^\beta+O(k).
\]
Because \(k\log(1+t)\geq u k^{\beta+1}\), (3) implies
\[
\log\Pr(D\geq k)\leq-u\sum_{j=1}^k j^\beta+O(k).
\]
Letting \(k\to\infty\) and then \(u\uparrow c\), and combining with (2), yields the **sharp marginal exponent**
\[
\lim_{k\to\infty}\frac{-\log\Pr(D\geq k)}{k^{\beta+1}}=\frac{c}{\beta+1}.\tag{4}
\]

**3. Polynomial one-vertex tail.** Suppose \(-\log q_j/\log j\to s>1\). Equation (1) gives
\[
\liminf_{k\to\infty}\frac{\log\Pr(D\geq k)}{k\log k}\geq-s,
\]
since \(\log(k!)\sim k\log k\). For any \(u\in(1,s)\) there is a finite \(C\geq1\) with \(q_j\leq Cj^{-u}\). Set \(t=k^u\). Splitting the logarithm of the product in (3) at \(j=k\),
\[
\begin{aligned}
\sum_{j=1}^k\log(1+tq_j)
&\leq k\log(1+C)+u\bigl(k\log k-\log(k!)\bigr)=O(k),\\
\sum_{j>k}\log(1+tq_j)
&\leq Ck^u\sum_{j>k}j^{-u}\leq\frac{Ck}{u-1}.
\end{aligned}
\]
Thus \(\log\Pr(D\geq k)\leq-uk\log k+O(k)\). Let \(u\uparrow s\) to obtain
\[
\lim_{k\to\infty}\frac{-\log\Pr(D\geq k)}{k\log k}=s.\tag{5}
\]

**4. Transfer from one vertex to the dependent forest maximum.** Put \(b_n=((\beta+1)\log n/c)^{1/(\beta+1)}\) in case 1, and \(b_n=\log n/(s\log\log n)\) in case 2, with \(n\) large. Fix \(\varepsilon\in(0,1)\). The tail estimates (4) or (5), together with the union bound, give
\[
\Pr\{\widehat M_n\geq\lceil(1+\varepsilon)b_n\rceil\}
\leq n\Pr\{D\geq\lceil(1+\varepsilon)b_n\rceil\}
\leq n^{-\delta_+ +o(1)},\tag{6}
\]
where \(\delta_+=(1+\varepsilon)^{\beta+1}-1>0\) in case 1 and \(\delta_+=\varepsilon>0\) in case 2.

For the lower bound let \(k=\lfloor(1-\varepsilon)b_n\rfloor\). Pick at least \(\lfloor(n-1)/(k+1)\rfloor\) positive vertices separated by \(k+1\) positions with all their first \(k\) candidate children arriving by time \(n\). At each such vertex the event that these \(k\) children all attach to it has probability \(p_k\) from (1). The events are independent because their sets of underlying \(Z_t\)'s are disjoint. Moreover, in the two cases respectively,
\[
p_k=n^{-(1-\varepsilon)^{\beta+1}+o(1)}
\quad\text{or}\quad
p_k=n^{-(1-\varepsilon)+o(1)}.
\]
Hence for some \(\delta_->0\) and all sufficiently large \(n\),
\[
\Pr\{M_n<k\}
\leq\exp\left[-\left\lfloor\frac{n-1}{k+1}\right\rfloor p_k\right]
\leq\exp(-n^{\delta_-}).\tag{7}
\]
Both bounds (6) and (7) are summable along \(n=2^m\). The first Borel-Cantelli lemma therefore gives both asymptotic inequalities almost surely along that subsequence. Both \(M_n\) and \(\widehat M_n\) are nondecreasing in \(n\), \(M_n\leq\widehat M_n\), and \(b_{2^{m+1}}/b_{2^m}\to1\). Monotone interpolation gives both claimed almost-sure limits on all integers \(n\to\infty\). This completes the proof.

## Verification

The standalone script `checker.py` performs exact, complete finite-state enumerations for the geometric law \(q_j=2^{-j}\), for each \(2\leq n\leq8\). An attachment of a vertex \(t\) to any nonpositive parent is combined into a single outcome of probability \(2^{-(t-1)}\), which is legitimate because only positive-vertex offspring counts are measured. The script compares the exact degree histograms with independently multiplied Bernoulli generating polynomials, checks expected edge totals and computes the exact maximum-degree histogram. It also checks the geometric elementary-symmetric bound
\[
2^{-k(k+1)/2}\leq\Pr(D\geq k)
\leq\frac{2^{-k(k+1)/2}}{\prod_{j=1}^k(1-2^{-j})},\quad k\geq1,
\]
by validating the underlying rational enclosure and finite cases. These finite tests verify model interpretation and algebra; they do not establish the almost-sure infinite-volume theorem, which follows from the proof above.

Reproduction: run `python checker.py` with Python 3 standard library only. A completed local run reported `PASS 398 exact assertions`.

## Relationship to prior work

Broutin, Devroye, Lugosi and Oliveira, *Subtractive random forests* (arXiv:2210.10544, first public version 19 October 2022; ALEA 21 (2024), 575–591), established the underlying model and, in their Section 6 Proposition 5, a distribution-free upper bound of asymptotic order \(\log n/\log\log n\) for the maximum positive-vertex offspring count. Their Remark 5 gives the single-vertex Bernoulli-sum representation. The present claim keeps that model and proves sharp **two-sided almost-sure constants** depending on the delay-mass tail. In the stretched-exponential class it also changes the growth exponent. The marginal Bernoulli representation, the model's general upper bound, Markov's inequality, and Borel-Cantelli are not asserted to be novel; the new assertion is the explicit tail-to-extreme classification with matching independent-window witnesses for this dependent forest process.

Calvillo, Devroye and Lugosi, *Subtractive random forests with two choices* (arXiv:2405.10455, 16 May 2024), addresses a different two-choice recommendation process and its long-term consistency, not this one-choice maximum offspring statistic. The earlier related renewal-forest literature is acknowledged without claiming an exhaustive historical-priority determination.

## Limitations

The theorem gives a first-order almost-sure growth law but neither a second-order centering nor a limiting extreme-value distribution. It assumes iid delays with full support and one parent per positive vertex; zero masses and intermediate/nonregular delay tails are not classified. Roots with nonpositive indices are excluded from the maximum. Although the proof is self-contained, the absence of an identical earlier assertion in the sources examined is not proof of global historical novelty. No independent mathematical audit has been performed.

## References

1. N. Broutin, L. Devroye, G. Lugosi and R. I. Oliveira, *Subtractive random forests*, arXiv:2210.10544 (first submitted 19 October 2022), ALEA 21 (2024), 575–591, doi:10.30757/ALEA.v21-23. https://arxiv.org/html/2210.10544v3
2. F. Calvillo, L. Devroye and G. Lugosi, *Subtractive random forests with two choices*, arXiv:2405.10455 (first submitted 16 May 2024). https://arxiv.org/abs/2405.10455
3. F. Baccelli and A. Sodre, *Renewal processes, population dynamics, and unimodular trees*, Journal of Applied Probability 56 (2019), 339–357, doi:10.1017/jpr.2019.24. https://www.cambridge.org/core/journals/journal-of-applied-probability/article/renewal-processes-population-dynamics-and-unimodular-trees/1F76AEB836FDF7FD0DF8DD2D85C390C1
