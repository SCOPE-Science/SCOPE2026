# Functional leaf-count fluctuations in polynomial aggregation trees

## Finding

Let \(\beta>0\). For each integer \(n\ge2\), construct a rooted tree on ordered vertices \(1,\ldots,n\), starting with root \(1\). At stage \(j+1\), with \(1\le j<n\), independently choose a new-branch indicator with success probability \(q_{n,j}=(j/n)^\beta\). On success attach \(j+1\) to a uniformly selected vertex among \(1,\ldots,j\); otherwise attach it to its immediate predecessor \(j\). Let \(L_{n,j}\) count the vertices of outdegree zero after \(j\) vertices (so the root is counted as a leaf at stage one), and put \(L_{n,0}=0\).

Define \(x_\beta(0)=0\) and, for \(0<t\le1\),
\[
x_\beta(t)=\exp(-t^\beta/\beta)\int_0^t s^\beta\exp(s^\beta/\beta)\,ds,
\qquad
p_\beta(t)=t^\beta\left(1-\frac{x_\beta(t)}t\right).
\]
Then, with any coupling across the different terminal sizes \(n\),
\[
\sup_{0\le t\le1}\left|\frac{L_{n,\lfloor nt\rfloor}}n-x_\beta(t)\right|\longrightarrow0
\quad\text{almost surely}.
\]
Moreover, in \(D([0,1])\) with the \(J_1\) topology,
\[
\left(\frac{L_{n,\lfloor nt\rfloor}-nx_\beta(t)}{\sqrt n}\right)_{0\le t\le1}
\Longrightarrow (Y_\beta(t))_{0\le t\le1},
\]
where \(Y_\beta\) is the unique continuous solution of
\[
dY_\beta(t)=-t^{\beta-1}Y_\beta(t)\,dt
+\sqrt{p_\beta(t)(1-p_\beta(t))}\,dB(t),\qquad Y_\beta(0)=0.
\]
In particular, \(L_{n,n}\) is asymptotically normal with mean \(nx_\beta(1)\), scale \(\sqrt n\), and explicit limiting variance
\[
v_\beta=\int_0^1\exp\!\left(-\frac{2(1-s^\beta)}\beta\right)
 p_\beta(s)(1-p_\beta(s))\,ds>0.
\]
The leading leaf density \(x_\beta(1)\) is strictly decreasing in \(\beta\), but the fluctuation variance is not monotone: it extends continuously to the benchmark \(\beta=0\), with
\[
(x_0(1),v_0)=(1/2,1/12),\qquad
(x_1(1),v_1)=(e^{-1},(e-2)e^{-2}),
\qquad \lim_{\beta\to\infty}v_\beta=0.
\]
Thus \(v_1>v_0\), while eventually the variance decreases to zero. These benchmark constants correspond respectively to uniform recursive and uniform labelled trees. No claim is made about uniqueness or the location of the variance maximizer.

## Assumptions and scope

The branch decisions at different stages are independent, the uniform-parent choices conditional on branch decisions are independent, and the terminal-size-dependent probability is exactly \(q_{n,j}=(j/n)^\beta\), for fixed \(\beta>0\). A new-branch choice is permitted to select the predecessor itself. Outdegree-zero leaves are distinguished from unrooted degree-one leaves; their counts differ by at most one after two vertices. The convergence statement concerns the whole triangular-array growth trajectory, not a single projectively consistent tree across all terminal sizes. The almost-sure assertion requires a joint coupling only to define a common probability space; the summable tail bound below makes it valid for every such coupling. Brownian motion in the limit is standard.

## Proof

**1. Exact one-dimensional transition.** The newest vertex is always a leaf. Attaching its successor to a leaf removes one old leaf and creates one new leaf; attaching to a nonleaf creates a leaf without removing one. Conditional on the tree at size \(j\), a nonleaf is selected exactly when the new-branch Bernoulli trial succeeds and a uniform parent lies among the \(j-L_{n,j}\) nonleaves. Hence, with \(\mathcal F_{n,j}\) the history,
\[
L_{n,j+1}=L_{n,j}+I_{n,j+1},\qquad
\mathbb P(I_{n,j+1}=1\mid\mathcal F_{n,j})
=q_{n,j}\left(1-\frac{L_{n,j}}j\right)=:r_{n,j}.
\]
Writing \(\mu_{n,j}=\mathbb EL_{n,j}\), \(a_{n,j}=1-q_{n,j}/j\), and \(\xi_{n,j+1}=I_{n,j+1}-r_{n,j}\), we obtain
\[
\mu_{n,j+1}=a_{n,j}\mu_{n,j}+q_{n,j},\qquad
D_{n,j+1}=a_{n,j}D_{n,j}+\xi_{n,j+1},
\]
with \(D_{n,j}=L_{n,j}-\mu_{n,j}\), \(D_{n,1}=0\), and \(|\xi_{n,j+1}|\le1\). All the coefficients \(a_{n,j}\) lie in \([0,1]\).

**2. Deterministic trajectory and finite centering.** The stated function \(x_\beta\) uniquely solves
\[
x_\beta'(t)=t^\beta-t^{\beta-1}x_\beta(t),\quad x_\beta(0)=0.
\]
Near zero, \(x_\beta(t)=O(t^{\beta+1})\) and \(x_\beta'(t)=O(t^\beta)\). Differentiating on \((0,1]\) gives \(x_\beta''(t)=O(t^{\beta-1}+t^{2\beta-1})\), which is absolutely integrable. Therefore the Euler discretization of the differential equation has total unscaled residual at most \(\int_0^1|x_\beta''(s)|\,ds\):
\[
\sum_{j=1}^{n-1}\left|n\bigl[x_\beta((j+1)/n)-x_\beta(j/n)\bigr]-x_\beta'(j/n)\right|=O_\beta(1).
\]
Comparison with the exact linear recurrence and \(\mu_{n,1}=1\) yields
\[
\max_{1\le j\le n}|\mu_{n,j}-nx_\beta(j/n)|=O_\beta(1).
\]
Consequently, centering by the explicitly displayed continuum function is valid even at the \(\sqrt n\) fluctuation scale.

**3. Uniform strong law.** Put \(S_{n,j}=\sum_{k=1}^{j-1}\xi_{n,k+1}\). Iterating the centered recurrence represents \(D_{n,j}\) as a sum of martingale differences with deterministic nondecreasing weights (as the time index of the difference increases), between zero and one. Summation by parts gives the deterministic bound
\[
\max_{1\le j\le n}|D_{n,j}|\le2\max_{1\le j\le n}|S_{n,j}|.
\]
The maximal Azuma inequality thus bounds \(\mathbb P(\max_j|D_{n,j}|>\varepsilon n)\) by \(2\exp(-c\varepsilon^2 n)\), for an absolute constant \(c>0\). This is summable in \(n\), regardless of how distinct rows are coupled. Borel--Cantelli and the deterministic centering bound yield the uniform almost-sure law.

**4. Functional Gaussian limit.** Let \(S_n(t)=n^{-1/2}S_{n,\lfloor nt\rfloor}\). Since \(|\xi_{n,j+1}|\le1\), the conditional Lindeberg condition is immediate. For \(t\in[\delta,1]\), the strong-law approximation makes \(r_{n,j}\) uniformly close to \(p_\beta(j/n)\); the missing initial interval contributes at most \(\delta\) to each normalized quadratic variation. It follows that, uniformly in \(t\),
\[
\frac1n\sum_{j<nt}\mathbb E[\xi_{n,j+1}^2\mid\mathcal F_{n,j}]
=\frac1n\sum_{j<nt}r_{n,j}(1-r_{n,j})
\xrightarrow{\mathbb P}\int_0^t p_\beta(s)(1-p_\beta(s))\,ds.
\]
The bounded-increment martingale functional central limit theorem therefore gives
\[
S_n\Longrightarrow W_\beta,\qquad
W_\beta(t)=\int_0^t\sqrt{p_\beta(s)(1-p_\beta(s))}\,dB(s).
\]
The centered recursion, after division by \(\sqrt n\), is a discrete Volterra equation with drift coefficient \(n^{-1}(j/n)^{\beta-1}\). These coefficients have vanishing maximum and their cumulative mass on \([0,\delta]\) tends to \(\delta^\beta/\beta\). The summation-by-parts bound above makes the rescaled centered processes uniformly stochastically bounded; consequently the contribution of the singular initial interval vanishes as \(\delta\downarrow0\). On every \([\delta,1]\), ordinary Riemann-sum convergence applies. More explicitly, the martingale processes are tight, and the drift increment on a grid interval \([s,t]\) is bounded in absolute value by the centered-process supremum times \((t^\beta-s^\beta)/\beta+o(1)\). This deterministic modulus tends to zero with interval length, uniformly including the singular initial interval, so the drift family is tight with continuous limits. The integral-equation continuous-mapping argument identifies the unique limit \(Y_\beta=W_\beta-\int_0^\cdot s^{\beta-1}Y_\beta(s)\,ds\). Solving this linear equation gives
\[
Y_\beta(t)=\int_0^t\exp\!\left(-\frac{t^\beta-s^\beta}\beta\right)
\sqrt{p_\beta(s)(1-p_\beta(s))}\,dB(s).
\]
Its endpoint variance is precisely \(v_\beta\). The same martingale representation and second-moment convergence give \(\operatorname{Var}(L_{n,n})/n\to v_\beta\). This also follows directly by summing orthogonal martingale differences with squared deterministic product weights.

**5. Benchmarks and nonmonotonicity.** If \(0<\beta_1<\beta_2\), the smaller exponent yields strictly larger branch probability \(t^{\beta_1}\) for \(0<t<1\); scalar ODE comparison, using \(0<x_\beta(t)<t\), shows \(x_{\beta_1}(1)>x_{\beta_2}(1)\). As \(\beta\downarrow0\), \(x_\beta(t)\to t/2\) and the Gaussian response kernel tends to \(s/t\). Dominated convergence yields \(x_\beta(1)\to1/2\) and \(v_\beta\to\int_0^1 s^2/4\,ds=1/12\). For \(\beta=1\), direct integration gives \(x_1(t)=t-1+e^{-t}\), \(p_1(t)=1-e^{-t}\), and
\[
v_1=e^{-2}\int_0^1(e^t-1)\,dt=\frac{e-2}{e^2}>\frac1{12}.
\]
Finally, since the exponential response kernel is at most one and \(p_\beta(s)(1-p_\beta(s))\le s^\beta\), one has \(0<v_\beta\le1/(\beta+1)\to0\). The continuous variance function is therefore not monotone and attains at least one maximum for a finite positive exponent. The limits \(\beta=0\) and \(\beta=1\) reproduce the classical leading leaf densities and variances for uniform recursive and uniform labelled trees, respectively.

## Verification

The standalone standard-library program `CHECK.py` independently enumerates parent lists and compares their leaf distributions with the one-dimensional chain for small terminal sizes, checks exact mean and second-moment recurrences, compares the \(\beta=0\) Eulerian and \(\beta=1\) Prüfer-sequence formulas, and checks numerical convergence of finite moments to the integral coefficients for several positive exponents. All 343 assertions passed. This is finite verification only; the infinite functional convergence and boundary statements are established by the proof above. Execute using `python CHECK.py` in the directory containing this result.

## Relationship to prior work

Donderwinkel and van Haastert (2026) introduce the polynomial-intensity discrete aggregation tree and establish metric-measure scaling limits toward continuum aggregation trees. The current theorem concerns the complete discrete-time leaf-count trajectory, a local unscaled statistic whose Gaussian fluctuations are not consequences of Gromov--Hausdorff--Prokhorov convergence. The uniform recursive and uniform labelled tree endpoint formulas are classical, and are used as independent consistency benchmarks, not claimed as new. General martingale functional central limit theorems are standard proof tools. The available abstract and detailed independent secondary account of the 2026 source emphasize continuum scaling and compactness; the full original paper was not successfully retrieved. Accordingly, absence of an equivalent result from that paper's full text has not been certified.

## Limitations

The theorem requires fixed \(\beta>0\), independent branch/parent draws, and the precise triangular-array polynomial probability profile. It does not address arbitrary nonpolynomial profiles, joint convergence of graph shape with leaf fluctuations, or uniqueness/location of a maximum of \(v_\beta\). Almost-sure convergence is for the leaf count in the defined model, not a pathwise limit tree. Historical priority remains provisional, especially because the complete text of the closest 2026 source could not be examined. Numerical examples do not establish the infinite theorem.

## References

1. S. Donderwinkel and J. van Haastert, *Convergence and compactness of discrete aggregation trees*, arXiv:2609.13066v1, September 11, 2026. https://arxiv.org/abs/2609.13066
2. M. Isaev, A. Southwell and M. Zhukovskii, *Distribution of tree parameters by martingale approach*, arXiv:1912.09838 (2019), *Combinatorics, Probability and Computing* (2022). https://arxiv.org/abs/1912.09838
3. D. J. Aldous, *The Random Walk Construction of Uniform Spanning Trees and Uniform Labelled Trees*, *SIAM Journal on Discrete Mathematics* **3** (1990), 450--465. https://doi.org/10.1137/0403039
4. H. M. Mahmoud, R. T. Smythe and J. Szymański, *On the structure of random plane-oriented recursive trees and their branches*, *Random Structures & Algorithms* **4** (1993), 151--176. https://doi.org/10.1002/rsa.3240040204
