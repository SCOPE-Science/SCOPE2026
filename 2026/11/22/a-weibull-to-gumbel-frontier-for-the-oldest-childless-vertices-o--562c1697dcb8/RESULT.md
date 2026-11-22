# A Weibull-to-Gumbel frontier for the oldest childless vertices of recursive DAGs

## Finding

Let \(n\ge2\), and construct a uniform recursive directed multigraph on vertices \(0,\ldots,n-1\): for each \(t\ge1\), vertex \(t\) independently chooses \(k\) parents, each uniformly with replacement from \(0,\ldots,t-1\). A *childless* vertex is one never selected by a later vertex. Let \(J_n\) be the smallest childless label and \(I_{n,i}\) its indicator at label \(i\). All the following statements hold with the same construction and without conditioning on simplicity.

**Exact joint law.** For every integer \(k\ge1\), \(n\ge2\), \(1\le r\le n-1\), and \(1\le i_1<\cdots<i_r\le n-1\),
\[
\Pr(I_{n,i_1}=\cdots=I_{n,i_r}=1)
=\left(\prod_{a=1}^{r}\frac{i_a-a+1}{n-a}\right)^k.
\tag{1}
\]
In particular \(\Pr(I_{n,i}=1)=(i/(n-1))^k\) and all distinct childless indicators are nonpositively correlated.

**Fixed fan-in.** For every fixed integer \(k\ge2\), with \(s_n=(n-1)^{k/(k+1)}\),
\[
\sum_{i=1}^{n-1}I_{n,i}\,\delta_{i/s_n}
\ \Rightarrow\ \operatorname{PPP}(x^k\,dx)
\quad\text{on }[0,\infty),
\tag{2}
\]
and therefore, for every \(x\ge0\),
\[
\lim_{n\to\infty}\Pr(J_n/s_n>x)
=\exp\left(-\frac{x^{k+1}}{k+1}\right).
\tag{3}
\]
The \(r\)-th oldest childless label, on this scale, converges to \(((k+1)G_r)^{1/(k+1)}\) with \(G_r\sim\operatorname{Gamma}(r,1)\), jointly for each fixed number of ranks.

**Logarithmic fan-in.** Let \(k=k_n\ge2\) be integer-valued and \(k_n/\log n\to c\in(0,\infty)\). Put
\[
 b_n=\bigl((k_n+1)(n-1)^{k_n}\bigr)^{1/(k_n+1)},
 \qquad Y_{n,i}=(k_n+1)\log(i/b_n).
\]
Then
\[
\sum_{i=1}^{n-1} I_{n,i}\,\delta_{Y_{n,i}}
\ \Rightarrow\ \operatorname{PPP}(e^y\,dy)
\quad\text{on }\mathbb R,
\tag{4}
\]
so the first childless label obeys the *reversed Gumbel* survival law
\[
\lim_{n\to\infty}
\Pr\{(k_n+1)\log(J_n/b_n)>y\}=\exp(-e^y),
\qquad y\in\mathbb R.
\tag{5}
\]
In particular \(J_n/n\to e^{-1/c}\) in probability. More generally, the complete macroscopic frontier is
\[
\frac{J_n}{n}\xrightarrow{\Pr}
\begin{cases}
0,&k_n/\log n\to0,\\
e^{-1/c},&k_n/\log n\to c\in(0,\infty),\\
1,&k_n/\log n\to\infty.
\end{cases}
\tag{6}
\]
This identifies logarithmically many parent selections as the threshold for the earliest surviving childless vertex to occupy a positive fraction of the birth chronology.

## Assumptions and scope

Parent selections are independent across times and within each new vertex; repeated parent labels are permitted and counted as separate directed edges. Childless refers to indegree zero when edges point from new vertices to their chosen parents, or equivalently to outdegree zero under the reversed circuit orientation. The root \(0\) is not childless for \(n\ge2\), and vertex \(n-1\) always is. For (2) and (3) \(k\ge2\) is fixed. For (4) and (5), \(k_n\) varies between final-size ensembles, held constant through each ensemble's growth, with \(k_n/\log n\to c>0\). For (6), all integer sequences \(k_n\ge2\) are allowed under the indicated ratio limits. Point-process convergence means vague weak convergence; order-statistic limits follow from bounded-window count laws and the tail bounds below.

## Proof

**1. Exact multivariate survival and domination.** At time \(t\), a particular parent choice is uniform on \(\{0,\ldots,t-1\}\). For prescribed labels \(i_1<\cdots<i_r\), let \(h_t=\#\{a:i_a<t\}\). Their simultaneous survival probability is
\[
\prod_{t=1}^{n-1}\left(1-\frac{h_t}{t}\right)^k.
\]
Order the forbidden labels by birth. At every step after \(i_a\), conditional avoidance of the first \(a-1\) labels leaves \(t-a+1\) candidate parent vertices. Thus the additional requirement to avoid \(i_a\) has probability \(\prod_{t=i_a+1}^{n-1}(t-a)/(t-a+1)=(i_a-a+1)/(n-a)\) for each of the \(k\) independent parent-selection sequences. Multiplying proves (1). (Equivalently the one-parent identity telescopes and the \(k\)-parent probability is its \(k\)-th power.) Because
\[
\frac{i_a-a+1}{n-a}\le\frac{i_a}{n-1}
\qquad (1\le i_a\le n-1),
\]
we have the uniform all-order factorial domination
\[
\Pr\{I_{n,i}=1\ \forall i\in S\}
\le\prod_{i\in S}q_{n,i},\qquad
q_{n,i}=\left(\frac{i}{n-1}\right)^k.
\tag{7}
\]
For two distinct labels \(i<j\), the joint probability is \((i(j-1)/[(n-1)(n-2)])^k\), giving nonpositive covariance, with equality only if \(j=n-1\) (or an indicator is deterministic). This includes the finite boundary cases.

**2. A Poisson-process criterion for the survival law.** In either regime, assign deterministic locations \(z_{n,i}\) and weights \(q_{n,i}\) from (7). For every compactly supported continuous \(f\ge0\), set \(h_{n,i}=1-e^{-f(z_{n,i})}\). If (i) \(\sum_i h_{n,i}q_{n,i}\to A_f=\int(1-e^{-f})\,d\mu\), (ii) \(\max_{i:h_{n,i}>0}q_{n,i}\to0\), and (iii) for every fixed \(r\), the ratio of (1) to \(\prod_{a=1}^r q_{n,i_a}\) tends uniformly to one after discarding positions with arbitrarily small total \(q\)-mass, then the \(r\)-th unsigned coefficient in the finite Laplace-product expansion tends to \(A_f^r/r!\). Indeed the contribution of repeated labels to the independent \(r\)-fold sum is bounded by \(O_r(\max q_{n,i})\), and discarded labels contribute at most their total \(q\)-mass by (7). The domination (7) bounds the coefficient by \(A_{n,f}^r/r!\) with \(A_{n,f}=\sum h_{n,i}q_{n,i}=O(1)\), uniformly in \(n,r\). Dominated convergence of the alternating power series gives
\[
\mathbb E\exp\left(-\sum_i f(z_{n,i})I_{n,i}\right)
\longrightarrow\exp\left[-\int(1-e^{-f})\,d\mu\right].
\tag{8}
\]
This is the Laplace functional of the stated Poisson point process.

**3. Fixed fan-in and Weibull extremes.** Write \(s_n=(n-1)^{k/(k+1)}\) and \(z_{n,i}=i/s_n\). By Riemann sums, for \(0\le a<b<\infty\),
\[
\sum_{as_n<i\le bs_n}q_{n,i}
\longrightarrow\int_a^b x^k\,dx.
\]
The maximum single weight on compact windows is \(O(n^{-k/(k+1)})\). For fixed \(r\) and \(i_a\ge\varepsilon s_n\), the joint-to-product ratio is
\[
\prod_{a=1}^r
\left[\left(1-\frac{a-1}{i_a}\right)
\frac{n-1}{n-a}\right]^k\longrightarrow1
\]
uniformly; the labels below \(\varepsilon s_n\) have asymptotic \(q\)-mass at most \(\varepsilon^{k+1}/(k+1)\). Apply (8), then let \(\varepsilon\downarrow0\), proving (2). Void probabilities on \([0,x]\) give (3); mapping \(x\mapsto x^{k+1}/(k+1)\) converts the limit to a unit-rate Poisson process and gives the order-statistic statement.

**4. Logarithmic fan-in and the Gumbel window.** Suppose \(k_n/\log n\to c\in(0,\infty)\), and use the indicated \(b_n\). Then \(b_n/n\to e^{-1/c}>0\), \(k_n=O(\log n)\), and for every fixed \(y\in\mathbb R\), summing the powers gives
\[
\begin{aligned}
\sum_{1\le i\le b_n e^{y/(k_n+1)}}q_{n,i}
&=\frac{(b_n e^{y/(k_n+1)})^{k_n+1}}
{(k_n+1)(n-1)^{k_n}}
\left(1+O\left(\frac{k_n+1}{b_n}\right)\right)\\
&=e^y(1+o(1)).
\end{aligned}
\tag{9}
\]
Here the integral bound for \(\sum_{i\le x}i^{k_n}\) proves the uniform error on bounded \(y\)-windows. Hence the limiting intensity is \(e^y\,dy\). On any bounded \(Y\)-window all underlying indices have order \(n\), and the joint-to-product ratio above is \(1+O_r(k_n/n)=1+o(1)\), uniformly. Also \(\max q_{n,i}=O(k_n/n)\) there, from (9) or the explicit formula for \(b_n\). Apply (8) to prove (4). Since the expected number of points with \(Y\le -M\) tends to \(e^{-M}\), Markov's inequality excludes escape of an earlier point toward \(-\infty\). The void probability on \((-\infty,y]\) therefore tends to \(\exp(-e^y)\), proving (5). As \((k_n+1)\log(J_n/b_n)\) is tight and \(k_n\to\infty\), we get \(J_n/b_n\to1\) in probability and thus the middle case of (6).

**5. The two outer macroscopic regimes.** If \(k_n/\log n\to\infty\), then, for each \(0<\varepsilon<1\),
\[
\mathbb E\sum_{i\le(1-\varepsilon)n}I_{n,i}
\le n(1-\varepsilon)^{k_n}\longrightarrow0,
\]
so \(J_n/n\to1\) by Markov's inequality. If \(k_n/\log n\to0\), then for each fixed \(\varepsilon\in(0,1)\), the mean \(\mu_n=\sum_{i\le\varepsilon n}q_{n,i}\) satisfies \(\mu_n\ge C_\varepsilon n(\varepsilon/2)^{k_n}\to\infty\) (take indices between \(\varepsilon n/2\) and \(\varepsilon n\)). Pairwise nonpositive covariance gives \(\operatorname{Var}\sum_{i\le\varepsilon n}I_{n,i}\le\mu_n\); Chebyshev's inequality bounds the no-childless probability by \(1/\mu_n\to0\). Thus \(J_n/n\to0\). This completes (6).

## Verification

Run the standalone Python 3 standard-library script `verify.py` from this package. It enumerates all parent-selection outcomes for twelve small parameter pairs, checks the exact joint law for every subset of labels, verifies mean/covariance identities and finite-size nonpositive pairwise covariance, and probes the deterministic first-moment scaling in both regimes. The completed replay reported 497 passing checks. Finite enumerations and numerical probes are not proofs of (2)–(6); the proofs are the analytic domination and Laplace-functional arguments above.

## Relationship to prior work

Devroye and Janson [1] define the same with-replacement uniform recursive \(k\)-DAG and investigate shortest/longest root-path depths, not childless birth-age extremes. Javanian and Vahidi-Asl [2] analyze the *total number* of outputs, proving a Gaussian limit with fixed fan-in under *distinct-parent* sampling and multiple initial inputs; their global-output theorem does not imply the extreme birth-label laws or logarithmically growing fan-in. Tsukiji and Mahmoud [3] establish a binary-circuit total-output limit; the accessible abstract does not resolve the earliest-birth-label question and the complete paper was not accessible for inspection. The published result [4] establishes the \(k=1\) one-parent recursive-tree Poisson birth-age process; it is explicitly excluded from the new fixed-fan-in assertion, and its model cannot imply the sharp \(k\ge2\) exponent or the \(k_n\asymp\log n\) macroscopic/Gumbel crossover. Janson [5] studies the number of ancestors/descendants in the same multi-parent model, a different statistic from zero-child count and earliest zero-child label.

## Limitations

All parent choices are uniform with replacement. No corresponding finite exact formula or phase limit is claimed for distinct-parent circuit sampling or biased attachment. The fixed-fan-in Poisson result is for each fixed \(k\ge2\), while the Gumbel window is proved for \(k_n/\log n\to c\in(0,\infty)\); no Gumbel normalization is claimed for general intermediate growth sequences. The paper [3] and an older internal-degree paper by Mahmoud and Tsukiji (2002) were not fully accessible, so a surviving historical-priority risk remains. No quantitative convergence rates and no independent audit are asserted.

## References

1. L. Devroye and S. Janson, *Long and short paths in uniform random recursive dags*, arXiv:0906.0152v1, first posted 2009-05-31; later Arkiv för Matematik 49 (2011), 61–77. https://arxiv.org/abs/0906.0152.
2. M. Javanian and M. Q. Vahidi-Asl, *Outputs in random f-ary recursive circuits*, Journal of Prime Research in Mathematics 7 (2011), 9–18; readable full text https://www.researchgate.net/publication/266836497_Outputs_in_random_f-ary_recursive_circuits.
3. T. Tsukiji and H. M. Mahmoud, *A limit law for outputs in random recursive circuits*, Algorithmica 31 (2001), 403–412. DOI: 10.1007/s00453-001-0044-4.
4. *The oldest leaves of random recursive trees form a Poisson point process* (2026), public mathematical research record: public mathematical research note dated 2026-10-18.
5. S. Janson, *The number of descendants in a random directed acyclic graph*, Random Structures & Algorithms 64 (2024), 768–803, first published 2023-11-07. DOI: 10.1002/rsa.21195.
