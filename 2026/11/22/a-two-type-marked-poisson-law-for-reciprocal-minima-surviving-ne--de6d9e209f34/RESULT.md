# A two-type marked Poisson law for reciprocal minima surviving near-total matrix refresh

## Finding

Let \(n\ge2\). In an \(n\times n\) array, independently draw all entries \(X_{ij}\) from the same atomless probability distribution with continuous cumulative distribution function \(F\). Independently for each cell, retain its old value with probability \(1-\varepsilon_n\), or replace it with an independent fresh observation from the same distribution with probability \(\varepsilon_n\); denote the resulting array by \(Y\). A cell is a *reciprocal minimum* of an array if it is the unique minimum of both its row and its column. A cell is *common* when it is a reciprocal minimum of both \(X\) and \(Y\).

For any \(0\le\varepsilon\le1\), let \(R_n\) count common cells whose observation is retained and \(S_n\) count common cells whose observation is replaced. Set \(m=2n-2\) and
\[
I_{a,b}(\varepsilon)=\int_0^1(1-u)^a(1-\varepsilon u)^b\,du.
\]
Their **exact**, distribution-free expectations are
\[
\boxed{\begin{aligned}
\mathbb ER_n&=n^2(1-\varepsilon)I_{m,m}(\varepsilon),\\
\mathbb ES_n&=\frac{2n^2\varepsilon}{m+1}I_{m+1,m}(\varepsilon).
\end{aligned}}
\]

Suppose \(n(1-\varepsilon_n)\to c\in[0,\infty)\). Then
\[
\boxed{(R_n,S_n)\ \xrightarrow{\mathrm d}\ (P_c,Q),\qquad
P_c\sim\operatorname{Pois}(c/4),\quad Q\sim\operatorname{Pois}(1/4),\quad P_c\perp Q.}
\]
Consequently the number of common reciprocal minima tends to \(\operatorname{Pois}((1+c)/4)\), and its probability of being zero tends to \(\exp(-(1+c)/4)\).

There is a sharper **spatial and value-marked** limit. Transform the entries to uniform quantiles \(U_{ij}=F(X_{ij})\), \(V_{ij}=F(Y_{ij})\). Place a retained common cell at \((i/n,j/n,nU_{ij})\), and a replaced common cell at \((i/n,j/n,nU_{ij},nV_{ij})\). On their respective spaces \([0,1]^2\times[0,\infty)\) and \([0,1]^2\times[0,\infty)^2\), these two point processes converge jointly to independent Poisson point processes with respective intensity measures
\[
\boxed{c\,du\,dv\,e^{-4s}\,ds
\quad\text{and}\quad du\,dv\,e^{-2(s+t)}\,ds\,dt.}
\]
In particular, retained and independently rediscovered matches have distinct, explicitly calculable value-mark profiles, even though their location coordinates are asymptotically uniform.

## Assumptions and scope

All matrix cells, refreshing decisions, and replacement draws are independent except for a retained entry's equality across the two copies. The common entry law may have gaps or singular continuous components but must be atomless with continuous cumulative distribution function; ties occur with probability zero. The theorem uses **one common noise parameter** for all cells, and concerns square arrays. Row and column labels are fixed, and the same cell must be reciprocal in both copies; this is not an optimal bipartite assignment or a geometric nearest-neighbor problem. The limiting parameter \(c\) is fixed and finite. If \(c=0\), the retained limiting process is empty.

## Proof

**1. Quantile reduction and the one-cell competitor probability.** The probability-integral transform and order preservation almost surely reduce to uniform \([0,1]\) entries; a replacement is an independent uniform variable. For one competitor cell to exceed thresholds \(x\) and \(y\) in the old and new arrays respectively, the probability is
\[
\begin{aligned}
h_\varepsilon(x,y)
&=(1-\varepsilon)(1-\max(x,y))+\varepsilon(1-x)(1-y)\\
&=(1-\max(x,y))(1-\varepsilon\min(x,y)).
\end{aligned}
\]
The conditional mark measure of a focal cell is the mixture \((1-\varepsilon)\,dx\) on the diagonal \(x=y\), plus \(\varepsilon\,dx\,dy\) off that diagonal. There are exactly \(2n-2=m\) distinct competitors in its row and column. Thus its probability of being common and retained equals \((1-\varepsilon)I_{m,m}(\varepsilon)\); its probability of being common and replaced equals \(\varepsilon\int_0^1\int_0^1h_\varepsilon(x,y)^m\,dx\,dy\). By symmetry and Fubini,
\[
\int_0^1\int_0^1h_\varepsilon(x,y)^m\,dx\,dy
=2\int_{0\le x\le y\le1}(1-y)^m(1-\varepsilon x)^m\,dx\,dy
=\frac{2}{m+1}I_{m+1,m}(\varepsilon).
\]
Multiplying by the \(n^2\) possible cells proves both finite expectation identities. At \(\varepsilon=0\) the copies agree, yielding \(\mathbb E(R_n+S_n)=n^2/(2n-1)\); at \(\varepsilon=1\) they are independent, yielding \(n^2/(2n-1)^2\). These are consistency checks, not the new asymptotic assertion.

**2. All simultaneous common-minimum events.** Two reciprocal minima in one matrix cannot occupy a shared row or column. Take \(r\) prescribed cells with all their rows and columns distinct, and condition on their \(r\) mark pairs \((x_a,y_a)\). Each selected cell has \(2(n-r)\) competitors outside the selected rows and columns. For every distinct pair of selected cells there are two cross cells, and both must exceed both selected entries in each copy. The exact conditional probability that all \(r\) cells are common minima is therefore
\[
\boxed{\prod_{a=1}^r h_\varepsilon(x_a,y_a)^{2(n-r)}
\prod_{1\le a<b\le r}
 h_\varepsilon(\max(x_a,x_b),\max(y_a,y_b))^2.}
\tag{1}
\]
There are \((n)_r^2\) ordered placements on disjoint rows and columns, where \((n)_r=n(n-1)\cdots(n-r+1)\). Formula (1) is an exact finite-dimensional integral representation; it also applies to test functions of selected positions and marks.

**3. Scaling of marked factorial moment measures.** Set \(\alpha_n=1-\varepsilon_n\), so that \(n\alpha_n\to c\) and \(\varepsilon_n\to1\). A retained selected cell has \(x=y=s/n\) and unconditioned mark mass \(\alpha_n\,ds/n\sim c\,ds/n^2\). A replaced selected cell has \(x=s/n,y=t/n\) and mass \(\varepsilon_n\,ds\,dt/n^2\sim ds\,dt/n^2\). For any fixed number of selected cells and bounded rescaled marks, their individual external-competitor factors in (1) tend respectively to
\[
h_{\varepsilon_n}(s/n,s/n)^{2(n-r)}\longrightarrow e^{-4s},
\qquad
h_{\varepsilon_n}(s/n,t/n)^{2(n-r)}\longrightarrow e^{-2(s+t)}.
\]
Every cross-cell factor in (1) tends to one. For each fixed number of cells, \((n)_r^2/n^{2r}\to1\), and the normalized row-column index sums tend to independent Lebesgue integrals over their locations. Therefore all mixed marked factorial moment measures converge to products of the two displayed intensity measures.

The limit exchange is justified, including unbounded marks. Indeed
\[
1-h_\varepsilon(x,y)
=(1-\varepsilon)\max(x,y)+\varepsilon(x+y-xy)
\ge\frac{x+y}{2}
\]
for all \(x,y\in[0,1]\). Hence, for fixed \(r\) and \(n\ge2r\),
\[
0\le h_\varepsilon(x,y)^{2(n-r)}
\le e^{-(n-r)(x+y)},
\]
which gives integrable exponential bounds on all rescaled mark variables and on their tails. For retained marks the diagonal bound becomes \(e^{-2(n-r)s/n}\), and for replaced marks it becomes \(e^{-(n-r)(s+t)/n}\). The intensities are finite, with masses \(c/4\) and \(1/4\), so first moments also control escape of points to infinite mark values.

**4. Identification of the limit.** The convergent mixed factorial moment measures (and tightness from the first-moment bounds) identify independent Poisson point processes on the two disjoint marked state spaces. Equivalently, all mixed falling-factorial moments of the unmarked counts converge to
\[
\mathbb E(R_n)_a(S_n)_b\longrightarrow(c/4)^a(1/4)^b
\qquad(a,b\in\mathbb Z_{\ge0}),
\]
which identifies two independent Poisson variables. Summing the two counts proves the stated total law and zero-count limit. This finishes the proof.

## Verification

The accompanying standalone \(`verify.py`\) uses exact rational integration and exhaustive rank-order enumeration for small matrices. It verifies the finite expectation identities at the identical-copy and independent-copy endpoints, the nontrivial half-refresh identity \(\mathbb E R_2=31/60\), \(\mathbb E S_2=49/180\), and exact count moments through size three. An independent direct two-dimensional midpoint integration checks the unsimplified competitor kernel. Large-size positive-integrand quadrature checks the two limiting mean intensities. The mathematical proof of point-process convergence is (1) and the factorial-moment argument above; finite computation is not offered as proof of an infinite limit.

Run in a standard Python 3 installation:

```sh
python3 verify.py
```

## Relationship to prior work

The single-matrix reciprocal-minimum object is a local version of the **Regular Minimality** notion in the work of Trendtel, Ünlü and Dzhafarov (2010), whose full article studies the event that all rows and columns participate in a consistent matching. Dzhafarov, Ünlü, Trendtel and Colonius (2011) give the unmarked **single-matrix** distribution of the number of violations of this property. Such single-sample count information alone does not determine dependence after a partially retained resampling, let alone its retained-versus-replaced and value-marked critical limit.

Pittel and Weishaar (1999) study single-copy random bipartite nearest-neighbor graphs and matching/connectivity properties; their accessible abstract does not assert a two-copy noisy-overlap theorem. Random-link reciprocal minima on symmetric complete graphs also use a different comparison structure (one symmetric edge per pair versus a bipartite matrix of independent cell costs). More recent work on noise sensitivity of minimum spanning trees concerns a different global graph statistic and different noise scale. The claimed result is specifically the **two-type spatial and marked Poisson limit in the \(n(1-\varepsilon_n)\to c\) crossover**, not the known one-copy reciprocal-minimum enumeration, a one-copy nearest-neighbor graph, or the endpoint \(\varepsilon=1\) by itself.

## Limitations

The claim requires an entrywise refresh coupling and independent identically distributed continuous costs. It does not cover arbitrary correlated cost matrices, geometry-dependent distances, fixed-count rather than Bernoulli refresh, or growing \(c\). It does not provide a quantitative total-variation rate. The 2011 full article and the 1999 bipartite-neighbor article could not be examined in full; any stronger hidden result about correlated two-copy marked overlap would require priority reassessment. No independent audit has been performed.

## References

1. M. Trendtel, A. Ünlü and E. N. Dzhafarov, “Matrices Satisfying Regular Minimality,” *Frontiers in Psychology* 1, 211 (published 2010-12-02). https://doi.org/10.3389/fpsyg.2010.00211
2. E. N. Dzhafarov, A. Ünlü, M. Trendtel and H. Colonius, “Matrices with a given number of violations of Regular Minimality,” *Journal of Mathematical Psychology* 55 (2011), 240–250. https://doi.org/10.1016/j.jmp.2010.12.002
3. B. Pittel and R. S. Weishaar, “The random bipartite nearest neighbor graphs,” *Random Structures & Algorithms* 15 (1999), 279–310. https://doi.org/10.1002/(SICI)1098-2418(199910/12)15:3/4%3C279::AID-RSA6%3E3.0.CO;2-J
4. O. Israeli and Y. Peled, “Noise sensitivity of the minimum spanning tree of the complete graph,” arXiv:2306.07357 (2023). https://arxiv.org/abs/2306.07357
