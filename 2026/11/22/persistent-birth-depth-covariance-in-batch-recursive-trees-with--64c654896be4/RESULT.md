# Persistent birth-depth covariance in batch recursive trees, with a three-child optimum

## Finding

Consider the uniformly recruited batch-recursive tree: starting from one root, at each integer step a uniformly selected existing vertex receives \(m\) new children, with the integer batch size \(m\ge1\) fixed. Let \(D_t\) be the common root-to-vertex depth of the batch born at step \(t\ge2\). For every pair of different batches \(2\le i<j\), and \(c=1/m\),

\[
\operatorname{Cov}(D_i,D_j)=C_m(i)
=\sum_{r=1}^{i-2}\frac{r+c-1}{(r+c)^2(r+c+1)}.
\]

The empty sum at \(i=2\) is zero. For \(i\ge3\), covariance is strictly positive and **independent of the later batch index** \(j\); it strictly increases with the earlier index \(i\). The persistent birth-depth covariance tends to

\[
L_m=\lim_{i\to\infty}C_m(i)=\frac{2m}{m+1}-\sum_{r=1}^\infty\frac1{(r+1/m)^2}>0,
\qquad \lim_{i\to\infty}i\,[L_m-C_m(i)]=1.
\]

Among all positive *integer* batch sizes, \(L_m\) attains its **unique maximum at \(m=3\)**. The limiting covariance is about \(0.4044028746\) for \(m=3\), versus \(0.3985311328\) for \(m=2\) and \(0.4026708455\) for \(m=4\). Thus the strength of shared depth fluctuations does not simply increase with batch size.

## Assumptions and scope

Fix any integer \(m\ge1\). The initial tree has one root at depth zero. At each step \(t\ge2\), choose independently and uniformly one of the \(N_{t-1}=1+m(t-2)\) existing vertices, then attach exactly \(m\) new depth-one-more children to it. All batches remain in the same growing random tree. The displayed covariance concerns the depths of two distinct *birth batches*, not the almost surely equal depths of two siblings in the same batch. It is unaffected by any later growth after the second batch. Limits in \(i\) hold along **any** choice of \(j=j_i>i\); the optimization is among positive integer \(m\).

## Proof

Write \(S_t\) for the sum of all depths after step \(t\), \(Q_t\) for the mean squared depth, and \(A_t=S_t/N_t\). Put \(a_t=m/N_t=1/(t-1+c)\) and let \(X_{t-1}\) be the sampled recruiter depth at step \(t\). Conditional on the previous tree, \(\mathbb E[X_{t-1}\mid\mathcal F_{t-1}]=A_{t-1}\) and \(D_t=1+X_{t-1}\). The exact averages obey

\[
A_t=A_{t-1}+a_t(1+X_{t-1}-A_{t-1}),\qquad
\mathbb E[Q_t\mid\mathcal F_{t-1}]=Q_{t-1}+a_t(1+2A_{t-1}).
\]

Define \(H_t=\sum_{k=2}^t a_k\) and \(R_t=\sum_{k=2}^t a_k^2\), with \(H_1=R_1=0\). Induction in the preceding recursions gives

\[
\mathbb E A_t=H_t,\quad
\mathbb E Q_t=H_t+H_t^2-R_t,\quad
B_{t-1}:=\operatorname{Var}(D_t)=H_{t-1}-R_{t-1}.
\]

Let \(V_t=\operatorname{Var}(A_t)\), \(V_1=0\), and \(q_t=\mathbb E[Q_{t-1}-A_{t-1}^2]=B_{t-1}-V_{t-1}\). Since \(A_t-H_t\) is a martingale whose increment is \(a_t(X_{t-1}-A_{t-1})\),

\[
V_t=V_{t-1}+a_t^2q_t,\qquad
q_{t+1}=(1-a_t^2)q_t+a_t(1-a_t).
\]

For any \(j>i\), iterated conditioning produces

\[
\mathbb E[D_j\mid\mathcal F_i]=1+A_i+\sum_{k=i+1}^{j-1}a_k.
\]

Consequently the future index cancels:

\[
C_m(i)=\operatorname{Cov}(D_i,D_j)=\operatorname{Cov}(D_i,A_i)
=V_{i-1}+a_iq_i.
\]

Here \(C_m(2)=0\). Using both recursions and \(a_{i+1}=a_i/(1+a_i)\) yields the exact **telescoping difference**

\[
C_m(i+1)-C_m(i)=a_i a_{i+1}(1-a_i)
=\frac{i+c-2}{(i+c-1)^2(i+c)}.
\]

Summing over \(i\) proves the finite covariance formula; every summand is positive. Partial fractions give

\[
\frac{r+c-1}{(r+c)^2(r+c+1)}
=\frac2{r+c}-\frac1{(r+c)^2}-\frac2{r+c+1},
\]

which proves the convergent expression for \(L_m\). The tail summand is \(r^{-2}+O(r^{-3})\), uniformly for fixed \(m\), hence \(L_m-C_m(i)=i^{-1}+O(i^{-2})\).

It remains to establish the **global integer optimum**. For real \(c>0\), put \(f(c)=2/(1+c)-\sum_{r\ge1}(r+c)^{-2}\). Then \(L_m=f(1/m)\), and

\[
f'(c)=\frac2{(1+c)^2}\left(g(1+c)-1\right),\quad
g(x)=x^2\sum_{k\ge0}(x+k)^{-3}.
\]

The function \(g\) is strictly decreasing on \((0,\infty)\): using \(x>0\),

\[
g(x)=\frac12\int_0^\infty\frac{u^2e^{-u}}{x(1-e^{-u/x})}\,du,
\]

and \(x(1-e^{-u/x})\) strictly increases in \(x\) for every \(u>0\). At \(x=5/4\),

\[
\sum_{k\ge0}(5/4+k)^{-3}
>\left(\frac45\right)^3+\left(\frac49\right)^3+\frac1{2(13/4)^2}
>\left(\frac45\right)^2.
\]

Thus \(g(5/4)>1\), so \(f\) is strictly increasing on \((0,1/4]\). Therefore among \(m\ge4\) the largest value is at \(m=4\). To compare \(m=1,2,3,4\), for \(K=30\) the elementary integral test yields exact rational bounds

\[
\frac2{1+c}-\sum_{r=1}^K\frac1{(r+c)^2}-\frac1{K+c}
\le f(c)\le
\frac2{1+c}-\sum_{r=1}^K\frac1{(r+c)^2}-\frac1{K+1+c}.
\]

The disjoint intervals certified by the accompanying exact-rational checker are \(L_1\in(0.35455,0.35556)\), \(L_2\in(0.39799,0.39905)\), \(L_3\in(0.40386,0.40492)\), and \(L_4\in(0.40213,0.40319)\). Their strict separation proves \(L_3>L_4,L_2,L_1\), completing the unique-maximum proof.

## Verification

The standalone \(\texttt{CHECK.py}\) (Python standard library only) independently enumerates the *complete* finite depth-history law for several batch sizes and sample sizes, checking means, variances and every off-diagonal covariance against the recurrence and the closed formula using rational arithmetic. Additional rational assertions verify the identity through earlier batch \(i=200\) for twenty values of \(m\), compare finite certified tail intervals, and check the key derivative inequality. Execution: \(\texttt{python CHECK.py}\), with **4,332 assertions passed**. The unbounded statements are proved analytically above; no finite enumeration is claimed to certify them.

## Relationship to prior work

Bhutani, Kalpathy, Lesny, Mahmoud and Neininger introduced the batch \(m\)-ary tree and analyzed individual depth distributions, height, internal path length and the Wiener index. Their internal-path-length variance constant is compatible with the limiting aggregate effect of \(L_m\); that aggregate constant is **not** claimed as new. The present statement instead resolves all cross-batch **birth-indexed** depth covariances, their invariance in the second birth index, the universal convergence correction, and the optimum for normalized pairwise depth dependence. Lodewijks establishes joint normalized depth limit laws for labeled vertices in the ordinary \(m=1\) recursive tree; such Gaussian limits do not determine the finite \(O(1)\) cross-depth covariance. Desmarais analyzes insertion depths in general recursive metric spaces; the cited older level-size study analyzes aggregate level counts of ordinary recursive trees. Neither inspected text directly supplies this complete batch-depth cross-index law. These differences are statements of coverage of the examined materials, not a blanket guarantee of historical novelty.

## Limitations

This concerns fixed integer \(m\) and uniform recruiter selection. No claim is made for changing batch sizes, nonuniform attachment, joint depth distribution beyond covariance, or fixed-leaf-height conditional laws. The global variance constant of total path length is already part of the motivating literature; the present individual-index covariance law must not be confused with it. Historical literature indexing is incomplete and an independently validated priority claim is not asserted.

## References

1. K. Bhutani, R. Kalpathy, F. Lesny, H. Mahmoud and R. Neininger, *Distances in m-ary recursive trees*, arXiv:2609.33636, first posted 2026-09-27, https://arxiv.org/abs/2609.33636.
2. C. Desmarais, *Depths in random recursive metric spaces*, arXiv:2210.03557, first posted 2022-10-07, https://arxiv.org/abs/2210.03557.
3. R. van der Hofstad, G. Hooghiemstra and P. Van Mieghem, *On the covariance of the level sizes in random recursive trees*, *Random Structures & Algorithms* (2002), accessible author copy https://www.nas.ewi.tudelft.nl/people/Piet/papers/covarRSA.pdf.
4. B. Lodewijks, *On joint properties of vertices with a given degree or label in the random recursive tree*, arXiv:2204.09032, first posted 2022-04-19, https://arxiv.org/abs/2204.09032.
5. R. P. Dobrow and J. A. Fill, *Total Path Length for Random Recursive Trees*, *Combinatorics, Probability and Computing* (1999); abstract https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/total-path-length-for-random-recursive-trees/FDA48E70E384342C0D8ABC47B510BCF4.
