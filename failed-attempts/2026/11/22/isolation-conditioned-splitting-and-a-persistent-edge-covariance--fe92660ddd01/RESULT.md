# Isolation-conditioned splitting and a persistent edge covariance in uniform random interval graphs

## Finding

**Theorem (exact isolation-conditioned decomposition and covariance).** Let \(n\ge2\). Generate \(n\) intervals by sampling two independent \(\operatorname{Uniform}[0,1]\) endpoints per vertex, independently across vertices; include an edge when two closed intervals intersect. Write \(G_n\) for this labeled random interval graph, \(I_i\) for the indicator that vertex \(i\) is isolated, \(Z_n=\sum_i I_i\), and \(E_n\) for the number of edges.

Condition on \(I_1=1\), and put \(m=n-1\). If \(K\) is the number of remaining intervals strictly left of interval 1, define

\[
W_{m,k}=\binom{m}{k}(2k)!\,(2m-2k)!,\qquad Q_m=\sum_{j=0}^m W_{m,j}.
\]

Then, for every \(0\le k\le m\),

\[
\Pr(K=k\mid I_1=1)=\frac{W_{m,k}}{Q_m},\qquad
\Pr(I_1=1)=p_n=\frac{2Q_m}{(2n)!}.
\]

Conditional on \(K=k\), the set of the \(k\) left-hand labels is a uniform subset of the remaining labels. On this partition, the two induced graphs are **independent standard random interval graphs** of orders \(k\) and \(m-k\), with no edges between them. An order-zero graph is taken to be empty.

Let \(H_n\) denote the induced graph on the other \(n-1\) labeled vertices, conditional on \(I_1=1\). The exact probability of a nontrivial two-sided split is

\[
r_n=\Pr(1\le K\le m-1\mid I_1=1)
=\frac{\sum_{k=1}^{m-1}W_{m,k}}{Q_m}
=\frac{1}{2n}+O(n^{-2}).
\]

Consequently, writing \(\mathcal L\) for distribution on labeled graphs,

\[
d_{\mathrm{TV}}\bigl(\mathcal L(H_n),\mathcal L(G_{n-1})\bigr)
\le r_n=\frac{1}{2n}+O(n^{-2}).
\]

Define the exterior gaps of an independent sampled interval \([L,R]\) as \(a=L\) and \(c=1-R\), with density \(2\) on \(a,c\ge0\), \(a+c\le1\). Put

\[
C_2=0,\qquad C_n=2\!\int_{a,c\ge0,\ a+c\le1}a^2c^2(a^2+c^2)^{n-3}\,da\,dc\quad(n\ge3).
\]

The exact edge–isolation covariance for every \(n\ge2\) is

\[
\boxed{\operatorname{Cov}(Z_n,E_n)
=-\frac{2}{3}n(n-1)\bigl[p_n+(n-2)C_n\bigr]<0.}
\]

In the large-order limit, \(n^2p_n\to1\), \(n^4C_n\to1/2\), and therefore

\[
\boxed{Z_n\xrightarrow{\mathbb P}0,\qquad
\operatorname{Cov}(Z_n,E_n)\longrightarrow-\frac23.}
\]

The convergence in probability of \(Z_n\) does not imply convergence of its unscaled covariance with the growing edge count.

## Assumptions and scope

Endpoints are independent and uniform, paired within labeled vertices; the resulting graph law is **not** uniform over all interval graphs and is **not** the fixed-length interval or random geometric graph model. Endpoint ties have probability zero. Every graph statement is for the induced labeled graph; where a uniform left-hand label subset is mentioned, the labels are those of vertices \(2,\ldots,n\). All finite equalities hold for integers \(n\ge2\), and the limiting statements mean \(n\to\infty\). The big-O constant in the two-sided-split probability is absolute.

## Proof

**Step 1: gap integration and the conditional split.** The original interval has left endpoint \(a\) and right endpoint \(1-c\), with joint density \(2\) over the triangle \(a,c\ge0\), \(a+c\le1\). Given \((a,c)\), a different interval falls wholly on its left with probability \(a^2\), or wholly on its right with probability \(c^2\). Thus the probability that vertex 1 is isolated and exactly \(k\) other intervals are on its left is

\[
2\binom mk\int_{a+c\le1}a^{2k}c^{2(m-k)}\,da\,dc
=\frac{2\binom mk(2k)!(2m-2k)!}{(2m+2)!}.
\]

The integral is the elementary Dirichlet simplex integral. Summing over \(k\) gives the stated exact distribution and \(p_n\). Exchangeability makes the identities of the left labels uniform among the \(k\)-subsets. Given these labels and the original interval, each left endpoint pair is independent uniform on \([0,a]\) after conditioning both endpoints to lie there, and similarly on \([1-c,1]\) on the right. Affine scaling sends either side to the original interval model, independently of \(a,c\); the two graphs are therefore independent, with no crossing edges. Integrating over the original interval does not change that product law.

**Step 2: rare mixing and total variation.** Let \(R_k=\binom mk/\binom{2m}{2k}\), so that \(W_{m,k}=(2m)!R_k\). These weights are symmetric, \(R_k=R_{m-k}\), and obey the exact ratio

\[
\frac{R_{k+1}}{R_k}=\frac{2k+1}{2m-2k-1},\qquad R_0=1,\qquad R_1=\frac1{2m-1}.
\]

For \(2\le k\le m/4\), the displayed ratio bound makes the tail sum \(O(m^{-2})\), since \(R_2=O(m^{-2})\). Between \(m/4\) and \(m/2\), monotonicity and an exponentially small bound for \(R_{\lfloor m/4\rfloor}\) make the sum exponentially small; the other half follows by symmetry. Consequently

\[
\sum_{k=0}^m R_k=2+\frac2{2m-1}+O(m^{-2}),\quad
\sum_{k=1}^{m-1}R_k=\frac2{2m-1}+O(m^{-2}).
\]

Their ratio is \(1/(2m)+O(m^{-2})\), which equals \(1/(2n)+O(n^{-2})\). On the complementary event \(K\in\{0,m\}\), the whole induced graph is exactly a standard \(G_m\). Coupling a standard \(G_m\) to the remaining graph on this event and allowing arbitrary behavior on the mixed event proves the total-variation upper bound.

**Step 3: exact covariance.** Write \(q=a^2+c^2\). Conditional on the first interval, its isolation event has probability \(q^{n-1}\), hence \(p_n=\mathbb E[q^{n-1}]\). If an edge includes vertex 1 it cannot coexist with \(I_1=1\), yielding covariance \(-2p_n/3\), since the unconditional edge probability is \(2/3\). For distinct remaining vertices \(2,3\), conditional on vertex 1 being isolated and on \((a,c)\), the only possible edge is formed by two intervals on the same side. Each such pair overlaps with probability \(2/3\) (by the four-endpoint ordering), and the two side probabilities are \(a^4\) and \(c^4\). Thus

\[
\mathbb E[I_1\mathbf1_{\{2\sim3\}}]
=\frac23\mathbb E[(a^4+c^4)q^{n-3}],\quad
\operatorname{Cov}(I_1,\mathbf1_{\{2\sim3\}})
=-\frac43\mathbb E[a^2c^2q^{n-3}]
=-\frac43C_n.
\]

There are \(n-1\) edges through vertex 1 and \(\binom{n-1}{2}\) other possible edges. By exchangeability and bilinearity of covariance,

\[
\operatorname{Cov}(Z_n,E_n)
=n\left[-(n-1)\frac{2p_n}{3}
-\binom{n-1}{2}\frac{4C_n}{3}\right]
=-\frac23n(n-1)[p_n+(n-2)C_n].
\]

The formula for \(n=2\) is obtained from the first edge type alone; its covariance equals \(-4/9\). All terms in brackets are nonnegative, and \(p_n>0\), proving strict negativity.

**Step 4: boundary Laplace limits.** Split the triangular domain into the two corner regions \(a\ge1/2\) and \(c\ge1/2\) and the remainder \(a,c\le1/2\). On the remainder \(q\le1/2\), so contributions decay exponentially. Near the corner \(a=1,c=0\), substitute \(a=1-x/n\), \(c=y/n\), \(0\le y\le x\). The integrands converge pointwise as

\[
q^{n-1}\longrightarrow e^{-2x},\qquad
n^2a^2c^2q^{n-3}\longrightarrow y^2e^{-2x}.
\]

For \(0\le x\le n/2\), \(q\le1-x/n\), furnishing an integrable exponential dominator for these scaled integrals. The other corner contributes identically. Thus

\[
\lim_{n\to\infty}n^2p_n
=4\int_0^\infty x e^{-2x}\,dx=1,
\quad
\lim_{n\to\infty}n^4C_n
=\frac43\int_0^\infty x^3e^{-2x}\,dx=\frac12.
\]

The covariance tends to \(-2/3\), since \(n(n-1)(n-2)C_n=O(n^{-1})\). Finally Markov's inequality gives \(\Pr(Z_n>0)\le\mathbb E Z_n=np_n\to0\).

## Verification

The standalone `checker.py` exhaustively enumerates unlabeled endpoint pairings, which have the same law as the labeled interval model after forgetting labels, up to orders \(n=6\). It compares exact rational edge means, isolation probabilities, full left/right count weights, edge–isolate covariances and conditional edge-count convolutions with the formulas above. It reports 168 exact assertions passed. These checks cover finite examples, not the infinite proof: the Dirichlet integral, covariance decomposition, ratio tail bound and boundary limits above are the general argument.

For independent algebraic reproduction, let

\[
A_n=\frac{2}{(2n)!}\sum_{k=0}^{n-1}\binom{n-1}{k}(2k)!(2n-2-2k)!,
\]

\[
C_n=\frac{2}{(2n)!}\sum_{k=0}^{n-3}\binom{n-3}{k}(2k+2)!(2n-4-2k)!,\quad n\ge3.
\]

Then \(A_n=p_n\), and substituting these exact rational sums into the covariance formula reproduces every finite value.

## Relationship to prior work

Scheinerman's original uniform-endpoint random interval graph is the ambient model; classical treatments establish its edge density, degree laws and typical connectivity. Boucheron and Fernández de la Vega (2001) analyze the independence number by a different greedy process. Diaconis, Holmes and Janson (2012) give the interval-graph limit representation and summarize the degree results. The contribution here is a **finite conditional distribution on the entire remaining graph after a tagged isolation event**, its quantitative one-sided concentration, and the resulting exact edge–isolation covariance limit. The fixed-range random interval and circular random geometric graphs are different sampling models. A precise historical-priority comparison with every part of the original 1988 article remains an access limitation.

## Limitations

This result concerns an exactly isolated **tagged** interval, not conditioning on at least one isolated interval without specifying its label. The total-variation estimate is an upper bound, not a sharp equality or established optimal error rate. The covariance limit is an unnormalized covariance; it does not imply nonvanishing Pearson correlation. No claim is made about other interval endpoint distributions without an order-preserving transform or about fixed-length intervals. Independent mathematical validation has not been performed.

## References

1. E. R. Scheinerman, *Random interval graphs*, Combinatorica 8 (1988), 357–371. DOI: https://doi.org/10.1007/BF02189092.
2. S. Boucheron and W. Fernández de la Vega, *On the Independence Number of Random Interval Graphs*, Combinatorics, Probability and Computing 10 (2001), 385–396. DOI: https://doi.org/10.1017/S0963548301004813. Public online date: 2001-12-10.
3. P. Diaconis, S. Holmes and S. Janson, *Interval Graph Limits*, Annals of Combinatorics 17 (2013), 27–52; first online 2012-11-21. DOI: https://doi.org/10.1007/s00026-012-0175-0. Open manuscript: https://pmc.ncbi.nlm.nih.gov/articles/PMC4578824/.
4. V. Iliopoulos, *Random Interval Graphs*, thesis, University of Essex repository: https://repository.essex.ac.uk/14414/1/M.Sc.%20thesis.pdf.
