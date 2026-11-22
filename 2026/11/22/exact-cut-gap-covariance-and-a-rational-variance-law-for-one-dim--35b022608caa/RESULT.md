# Exact cut-gap covariance and a rational variance law for one-dimensional two-nearest-neighbor graphs

## Finding

Let \(n\ge3\) independent points be uniform on the unit interval and form the **undirected two-nearest-neighbor graph**: each point is joined to its two closest distinct sample points, and an undirected edge is retained whenever either endpoint chooses the other. Write \(C_n\) for the number of connected components and \(m=(n-5)_+\). Then

\[
\mathbb E C_n=1+\frac{7m}{54}.
\]

Set \(p=7/54\), \(q_3=2071/90000\), and \(q_4=6389/324000\). The **exact finite-sample variance**, for every \(n\ge3\), is

\[
\operatorname{Var}(C_n)=mp(1-p)+2\sum_{h=1}^4(m-h)_+(q_h-p^2),
\quad q_1=q_2=0.
\]

In particular, for \(n\ge10\),

\[
\operatorname{Var}(C_n)=\frac{5747}{90000}(n-5)+\frac{146737}{3645000}.
\]

The density converges in \(L^2\), and the centered fluctuations satisfy

\[
\frac{C_n}{n}\xrightarrow{L^2}\frac7{54},\qquad
\frac{C_n-\mathbb EC_n}{\sqrt n}\xrightarrow{\mathrm d}
N\left(0,\frac{5747}{90000}\right).
\]

Consequently the asymptotic variance-to-mean ratio of the component count is \(2463/5000\), strictly less than one. The exact local cut process is four-dependent: cut indicators at separation one or two are mutually exclusive, at separations three and four are positively correlated, and at separation at least five are independent.

## Assumptions and scope

The points are independent and continuously uniform on \((0,1)\). Distances are ordinary absolute Euclidean distances on the line, **not** circular distances and not independently sampled random-link distances. The graph is symmetric by union of directed neighbor choices, rather than by requiring mutual choices. There are no ties almost surely. For \(n=3,4,5\) the graph is deterministically connected. The exact formulas hold for all \(n\ge3\); all limits are for \(n\to\infty\) with exactly two neighbors per vertex.

Let \(X_{(1)}<\cdots<X_{(n)}\) be the ordered sample, with interior spacings \(G_i=X_{(i+1)}-X_{(i)}\), \(1\le i\le n-1\). For \(3\le i\le n-3\), define

\[
J_i=\mathbf1\{G_i>G_{i-1}+G_{i-2}\ \text{and}\ G_i>G_{i+1}+G_{i+2}\}.
\]

An empty index range means an empty sum. The fundamental deterministic characterization is \(C_n=1+\sum_{i=3}^{n-3}J_i\).

## Proof

**1. Deterministic cut characterization.** A connected component of a one-dimensional undirected nearest-neighbor graph is a consecutive block of sorted sites. Indeed, if an edge connects sites with indices \(a<b\), the endpoint that chose the other endpoint also chooses (and therefore connects to) every intervening point, which is strictly closer. Thus no component can skip an intervening site. A cut between sites \(i\) and \(i+1\) is absent of graph edges across it exactly when the two nearest neighbors of site \(i\) lie to its left and the two nearest neighbors of site \(i+1\) lie to its right. At an interior index this is equivalent to

\[
G_i>G_{i-1}+G_{i-2},\qquad G_i>G_{i+1}+G_{i+2}.
\]

For indices within two sites of the boundary, one endpoint has fewer than two neighbors on its outer side, so the cut cannot occur. If the displayed inequalities hold, no more remote vertex can cross the cut: a vertex at least two positions from the cut has two strictly closer vertices on its own side, while an immediately adjacent nonboundary vertex has two closer same-side candidates by the inequalities. The number of components therefore equals one plus the number of cuts, proving the characterization.

**2. Exact independent-clock representation.** The \(n+1\) spacings including the two boundary spacings have the Dirichlet\((1,\ldots,1)\) law. They can be represented as independent unit exponential variables divided by their positive total. Since the inequalities defining cuts are homogeneous, the denominator cancels. Thus \(\sum J_i\) has exactly the law of a sum of \(m\) consecutive terms of the stationary process

\[
I_j=\mathbf1\{E_j>E_{j-1}+E_{j-2},\ E_j>E_{j+1}+E_{j+2}\},
\]

with \((E_j)_{j\in\mathbb Z}\) independent \(\operatorname{Exp}(1)\). This process is four-dependent.

**3. Single and joint cut probabilities.** Put \(F(t)=1-e^{-t}(1+t)\), the distribution function of a sum of two unit exponentials. Conditioning on the central exponential gives

\[
p=\Pr(I_0=1)=\int_0^\infty e^{-t}F(t)^2\,dt=\frac7{54}.
\]

Cuts one or two positions apart are impossible because they would require one central exponential to be greater than the other plus a positive gap, in both directions. For separation three the two events share the sum \(S=E_1+E_2\), of Gamma\((2,1)\) law. Let

\[
B(t)=\int_t^\infty e^{-x}F(x)\,dx
=e^{-t}-e^{-2t}\left(\frac t2+\frac34\right).
\]

Conditional independence given \(S\) yields

\[
q_3=\Pr(I_0=I_3=1)=\int_0^\infty t e^{-t}B(t)^2\,dt=\frac{2071}{90000}.
\]

For separation four the two events share a single exponential \(E_2=t\). Define

\[
A(t)=\int_t^\infty e^{-x}F(x)(1-e^{-(x-t)})\,dx
=\frac12e^{-t}-e^{-2t}\left(\frac t6+\frac{11}{36}\right).
\]

Conditional independence given that shared exponential gives

\[
q_4=\Pr(I_0=I_4=1)=\int_0^\infty e^{-t}A(t)^2\,dt=\frac{6389}{324000}.
\]

At separation at least five, the two cut events use disjoint independent exponentials, so the joint probability is \(p^2\). Expanding the finite sum variance and counting ordered pairs at each lag gives the exact formula in the Finding section. The coefficient of \(m\) is

\[
\sigma^2=p(1-p)+2\sum_{h=1}^4(q_h-p^2)
=p-9p^2+2(q_3+q_4)=\frac{5747}{90000}>0.
\]

For \(m\ge5\), the boundary correction equals \(20p^2-6q_3-8q_4=146737/3645000\), proving the stated linear formula for \(n\ge10\).

**4. Limits.** The mean and variance calculations imply \(C_n/n\to p\) in \(L^2\). The stationary sequence \((I_j)\) is bounded and four-dependent, with nonzero long-run variance \(\sigma^2\). The classical central limit theorem for fixed-range dependent stationary sequences therefore applies to its first \(m\) terms. The distributional exponential-spacings representation and \(m/n\to1\) transfer that central limit theorem to \(C_n\). The variance-to-mean limit is

\[
\frac{\sigma^2}{p}=\frac{2463}{5000}.
\]

## Verification

The complete Python 3 standard-library script `checker.py` evaluates the exponential-polynomial integrals using exact rational arithmetic, checks the joint probabilities and variance coefficient, and independently tests the deterministic cut formula against explicitly constructed two-nearest-neighbor graphs. It exhausts all permutations of binary-power gap configurations through eight vertices and tests additional larger configurations. Run `python3 checker.py` from the folder containing the file. It returns `PASS: 102595 exact assertions`. These finite tests do not replace the proof of the infinite statements.

## Relationship to prior work

Wade's 2006 preprint on explicit laws of large numbers for nearest-neighbor-type graphs treats power-weighted total edge lengths for general nearest-neighbor rules, rather than the exact connected-component count for two neighbors on the line. Penrose and Wade's 2006 preprint computes moments of directed one-nearest-neighbor total length using Dirichlet spacings, not the two-neighbor cut process. Penrose and Yukich (2001) provide a general component-count central limit theorem for nearest-neighbor graphs; consequently the **existence of a Gaussian limit alone is not claimed as new**. The specific five-gap cut characterization and finite-sample rational covariance spectrum, including \(7/54\) and \(5747/90000\), were not identified in the literature examined. General stochastic-geometry central limit frameworks do not by themselves evaluate these constants or establish the exact finite-\(n\) formula.

## Limitations

The model is one-dimensional with fixed neighbor count two and independent uniform sites. The result does not give an explicit full distribution of \(C_n\), a local central limit theorem, quantitative Gaussian error estimates, or higher-dimensional constants. Full text of the potentially relevant Penrose–Yukich (2001) article was not accessible during this literature comparison. Although its abstract confirms a generic component-count CLT, whether an overlooked section gives the same exact rational finite moment formulas remains a historical-priority risk. No independent external mathematical audit is claimed.

## References

1. A. R. Wade, *Explicit laws of large numbers for random nearest-neighbour type graphs*, arXiv:math/0603559, first public version 2006-03-23, https://arxiv.org/abs/math/0603559.
2. M. D. Penrose and A. R. Wade, *Limit theory for the random on-line nearest-neighbour graph*, arXiv:math/0603561, first public version 2006-03-23, https://arxiv.org/abs/math/0603561.
3. M. D. Penrose and J. E. Yukich, *Central limit theorems for some graphs in computational geometry*, Annals of Applied Probability 11 (2001), 1005–1041, https://doi.org/10.1214/aoap/1015345393.
