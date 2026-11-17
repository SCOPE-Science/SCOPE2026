# The ten-vertex boundary for Gini contraction of normalized path heat

## Finding

Let \(P_n\) be the unweighted path with vertices \(0,\ldots,n-1\), where \(n\ge2\). Denote its adjacency and degree matrices by \(A\) and \(D\), and set
\[
Q_n=D^{-1}A-I,\qquad H_{n,t}=\exp(tQ_n)\quad(t\ge0).
\]
On real functions modulo constants use the complete-pair Gini seminorm
\[
G_n(f)=\sum_{0\le i<j<n}|f_i-f_j|.
\]
The sharp all-time nonexpansivity classification is
\[
\boxed{\;\|H_{n,t}\|_{G_n}<1\ \text{for every }t>0\quad\Longleftrightarrow\quad 2\le n\le9.\;}
\]
In particular, the first path admitting any Gini amplification under degree-normalized heat has **ten vertices**. For every \(n\ge10\), with \(e_1\) the indicator of the vertex adjacent to endpoint \(0\),
\[
G_n(H_{n,t}e_1)>G_n(e_1)=n-1
\quad\text{whenever}\quad
0<t\le\frac{n-9}{8n(n-1)}.
\]
Furthermore, define the operator logarithmic norm
\[
\mu_n=\lim_{h\downarrow0}\frac{\|I+hQ_n\|_{G_n}-1}{h}.
\]
Its exact values for \(n=2,3,4,5,6,7,8,9\) are, in order,
\[
-2,\;-1,\;-\frac14,\;-\frac16,\;-\frac19,\;-\frac1{12},\;-\frac1{16},\;0.
\]
Thus \(n=9\) is the unique neutral case in this range: the instantaneous operator logarithmic norm vanishes, yet the semigroup is strictly contracting at every positive time.

## Assumptions and scope

The graph is the finite undirected unit-edge path, without loops; the generator is **degree normalized**, not the unnormalized combinatorial Laplacian. Endpoints jump at rate one to their sole neighbor; each interior vertex jumps at total rate one, equally distributed between its two neighbors. Signals are arbitrary real vectors. All inequalities are global operator statements on the quotient by constant vectors, not estimates only for nonnegative or monotone signals. The claimed strict contraction means the sharp two-input seminorm ratio is smaller than one at each fixed positive time, even though the identity has norm one at zero time.

## Proof

**1. A binary-cut operator norm identity.** For any real linear map \(B\) satisfying \(B\mathbf1=\mathbf1\),
\[
\|B\|_{G_n}=\max_{\varnothing\ne S\subsetneq\{0,\ldots,n-1\}}
\frac{G_n(B\mathbf1_S)}{|S|(n-|S|)}.
\]
Indeed, the scalar layer-cake representation writes every real vector as a constant plus the integral of indicators of its superlevel sets. Linearity, constant preservation, and the triangle inequality bound its image seminorm by the largest displayed cut ratio, while any cut itself attains the corresponding ratio. Complementary cuts have identical ratios because \(B\mathbf1=\mathbf1\); hence it suffices to examine cuts not containing vertex \(n-1\).

**2. An exact expression for the initial cut derivative.** Fix \(S\) with \(k=|S|\), \(1\le k<n\), and let
\[
b_i(S)=\frac{\#\{j:j\sim i,\ \mathbf1_S(j)\ne\mathbf1_S(i)\}}{\deg(i)}
\in\{0,\tfrac12,1\}.
\]
Thus \((Q_n\mathbf1_S)_i=-b_i\) on \(S\) and \((Q_n\mathbf1_S)_i=b_i\) outside it. Taking the right derivative of every pairwise absolute difference at time zero gives
\[
\begin{aligned}
\Delta_n(S):={}&\left.\frac{d}{dt}\right|_{t=0+}G_n(H_{n,t}\mathbf1_S)\\
={}&-(n-k)\sum_{i\in S}b_i-k\sum_{i\notin S}b_i\\
&+\sum_{\{i,j\}\subset S}|b_i-b_j|
+\sum_{\{i,j\}\subset S^c}|b_i-b_j|.
\end{aligned}
\]
For every sufficiently small \(h>0\), the same formula is **exact** for \(G_n((I+hQ_n)\mathbf1_S)=k(n-k)+h\Delta_n(S)\): cross-cut differences retain their original sign, and same-side differences are \(h\) times the corresponding absolute generator differences. Combining with step 1,
\[
\mu_n=\max_{\varnothing\ne S\subsetneq V(P_n)}
\frac{\Delta_n(S)}{|S|(n-|S|)}.
\]
This finite-cut formula is an exact identity, not a heuristic Taylor approximation.

**3. Exhaustive small-path certificate.** For \(n=2,\ldots,9\), every complement class of proper cuts is represented by one bit mask on the first \(n-1\) vertices, excluding the zero mask. The bundled standard-library script `check_path_gini.py` computes the displayed \(b_i\), every \(\Delta_n(S)\), and the maximum fraction, entirely with rational arithmetic. It also compares each derivative with an *independent direct evaluation* of \(G_n((I+Q_n/4)\mathbf1_S)\). The numbers of tested cuts at successive dimensions are \(1,3,7,15,31,63,127,255\), respectively, for **502 cuts in total**. The maxima are
\[
\begin{array}{c|rrrrrrrr}
n&2&3&4&5&6&7&8&9\\\hline
\mu_n&-2&-1&-1/4&-1/6&-1/9&-1/12&-1/16&0
\end{array}.
\]
The script is a transparent finite exhaustive certificate: its ranges list *all* representatives, not sampled data. The mathematical identity in step 2 establishes why checking these finitely many rational inequalities proves the small-path assertions.

**4. From infinitesimal to global contraction.** In the finite-dimensional normed quotient,
\(H_{n,t}=\lim_{m\to\infty}(I+tQ_n/m)^m\).
For sufficiently small \(h>0\), step 2 gives \(\|I+hQ_n\|_{G_n}=1+h\mu_n\), so by submultiplicativity,
\[
\|H_{n,t}\|_{G_n}\le e^{\mu_n t}.
\]
This is strictly below one for \(2\le n\le8\), and at most one for \(n=9\). Strictness also holds for \(n=9\): if a nonconstant binary cut attained equality at time \(t_0>0\), contractivity and the semigroup property would force its Gini variation to remain constant throughout \([0,t_0]\). Each coordinate difference along an analytic matrix exponential has a fixed sign on some sufficiently small interval \((0,\epsilon)\), so the variation there is a single analytic linear combination of these differences. An analytic function equal to a positive constant on an interval must equal that constant for all real times. This contradicts convergence of \(H_{n,t}\mathbf1_S\) to a constant vector as \(t\to\infty\). There are finitely many cuts, so step 1 upgrades strictness for every cut to \(\|H_{9,t}\|_{G_9}<1\).

**5. A uniform family of explicit amplifying signals.** Suppose \(n\ge10\), and take \(S=\{1\}\), the vertex immediately next to one endpoint. The escape values are \(b_1=1\), \(b_0=1\), \(b_2=1/2\), and all others zero. Directly in step 2,
\[
\Delta_n(\{1\})=\frac{n-9}{2}>0.
\]
To make the positive-time assertion quantitative, note \(\|Q_n\|_{\infty\to\infty}\le2\). For \(0<t<1/2\), the matrix-exponential remainder satisfies
\[
\|H_{n,t}\mathbf1_S-(I+tQ_n)\mathbf1_S\|_\infty
\le\sum_{r\ge2}\frac{(2t)^r}{r!}
\le\frac{2t^2}{1-2t}.
\]
The Gini seminorm of an \(n\)-vector changes by at most \(n(n-1)\) times the sup norm of its perturbation. Therefore
\[
G_n(H_{n,t}\mathbf1_{\{1\}})-G_n(\mathbf1_{\{1\}})
\ge \frac{n-9}{2}t-\frac{2n(n-1)t^2}{1-2t}.
\]
For \(0<t\le (n-9)/(8n(n-1))<1/4\), the right-hand side is strictly positive. This proves amplification in *every* dimension \(n\ge10\). Irreducibility also implies \(\|H_{n,t}\|_{G_n}\to0\) as \(t\to\infty\), so amplification is transient.

## Verification

Run `python3 check_path_gini.py` with Python 3 and no third-party dependencies. The script exhaustively enumerates the 502 relevant cut classes for dimensions 2 through 9; independently re-evaluates every right derivative from an Euler-step Gini quotient; verifies all eight rational logarithmic norms; and checks the explicit positive-time Taylor lower-bound certificate for each dimension from 10 to 100. Dimensions greater than 100 are covered by the symbolic algebra in proof step 5, **not** by finite extrapolation. The infinite-time strictness uses the analytical semigroup argument in step 4.

## Relationship to prior work

The classical Doeblin–Dobrushin formula and its Markov-operator generalizations control a quotient **oscillation** seminorm and the dual total variation of probability measures. The present \(G_n\) is instead the **sum of all pairwise differences of one function**, a different norm on real signals modulo constants. Gaubert and Qu's operator framework does not supply the ten-vertex threshold simply by replacing the norm. Fill and Kahn's birth–death chain comparisons address mixing distances to stationarity, rather than complete-pair variation of propagated signal values. Related results on graph-edge variation or graph-metric Lipschitz variation use different denominators and are not substituted for the all-pairs cut test. No claim of exhaustive historical priority is made.

## Limitations

The classification applies to the exactly degree-normalized, continuous-time simple random walk on the unweighted finite path and the unweighted complete-pair Gini seminorm. It does not cover arbitrary birth–death rates, weighted paths, graph-edge total variation, weighted pairwise Gini, discrete-time powers, or general trees. The exact operator norm for each positive time and large \(n\) is not given; the theorem classifies contractivity and provides explicit amplifying times. The novelty comparison may miss an unindexed equivalent source, and independent mathematical review remains outstanding.

## References

1. J. A. Fill and J. Kahn, *Comparison inequalities and fastest-mixing Markov chains*, first public arXiv version 28 September 2011, arXiv:1109.6075, https://arxiv.org/html/1109.6075v3.
2. S. Gaubert and Z. Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, first public arXiv version 17 July 2013, arXiv:1307.4649, https://ar5iv.labs.arxiv.org/html/1307.4649.
