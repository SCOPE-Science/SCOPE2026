# Zero-truncated Poisson sink law for uniform acyclic orientations of balanced bicliques

## Finding

Let an orientation be chosen uniformly among all acyclic orientations of the labeled \(K_{n,n}\). If \(S_n\) counts its sinks (outdegree-zero vertices), then, with \(\rho=\log2\), for every \(R>1\),
\[
\sup_{|z|\le R}\left|\mathbb E z^{S_n}-(2^z-1)\right|=O_R(n^{-1}).
\]
In particular the law converges in total variation, at rate \(O(n^{-1})\), to a Poisson\((\rho)\) variable conditioned to be positive:
\[
\Pr(S_\infty=k)=\begin{cases}\rho^k/k!,&k\ge1,\0,&k=0.\end{cases}
\]
For any \(R>1\), the uniform coefficient bound
\[
\left|\Pr(S_n=k)-\Pr(S_\infty=k)\right|\le C_R/(nR^k)
\]
holds for all integers \(k\ge0\) and sufficiently large \(n\). Therefore
\[
\mathbb E S_n=2\rho+O(n^{-1}),\qquad \operatorname{Var}(S_n)=2\rho(1-\rho)+O(n^{-1}).
\]

## Assumptions and scope

The graph is the ordinary unweighted simple complete bipartite graph with two **labeled** parts, each of size \(n\ge1\). Every acyclic orientation receives equal weight; this is **not** the law obtained by orienting each edge independently without conditioning on acyclicity. A sink has all incident arrows pointing into it. All statements about the asymptotic error have fixed \(R>1\) and \(n\to\infty\); they do not assert uniformity in unbalanced bipartition ratios. The graph is finite and connected, hence every acyclic orientation has a sink. No two sinks may lie in opposite parts, since those vertices are adjacent.

Write \(B_{a,b}\) for the number of acyclic orientations of \(K_{a,b}\), including the natural isolated-vertex interpretation at zero part size, and let \(A_{a,b}(z)\) be the sum of \(z^{\#\text{sinks}}\) over its acyclic orientations. The established poly-Bernoulli enumeration [1–3] is
\[
\mathcal B(x,y)=\sum_{a,b\ge0}B_{a,b}\frac{x^a}{a!}\frac{y^b}{b!}
=\frac1{e^{-x}+e^{-y}-1}=
\frac{e^{x+y}}{1-(e^x-1)(e^y-1)}.
\]
The earliest public source directly motivating the **probabilistic balanced-orientation asymptotic question** used here is [1], initially posted on 2024-08-22. Older structural/enumeration papers are credited as foundational, not claimed as new.

## Proof

**1. Mark designated sinks.** For \(a,b\ge1\) and a specified set of \(r\ge1\) vertices in the first part, forcing them all to be sinks fixes each incident edge toward those vertices; the remaining choices are exactly acyclic orientations of \(K_{a-r,b}\), so their number is \(B_{a-r,b}\). The same applies to a designated sink set in the second part, with count \(B_{a,b-r}\). A sink set containing vertices from both parts is impossible. Expand \(z^{S}=(1+(z-1))^S\) and sum over selected subsets of the actual sinks to obtain the **exact identity**
\[
A_{a,b}(z)=B_{a,b}
+\sum_{r=1}^{a}\binom ar B_{a-r,b}(z-1)^r
+\sum_{r=1}^{b}\binom br B_{a,b-r}(z-1)^r.
\]
It extends to zero-size parts using the obvious isolated-vertex convention. Binomial convolution yields
\[
\mathcal A(x,y;z)
=\mathcal B(x,y)\left(e^{(z-1)x}+e^{(z-1)y}-1\right)
=\frac{e^{zx+y}+e^{x+zy}-e^{x+y}}{H(x,y)},
\qquad H(x,y)=1-(e^x-1)(e^y-1).
\]
For the balanced diagonal, exchange of the two parts makes the first two terms equal. With \(c_n(z)=[x^ny^n]e^{zx+y}/H(x,y)\),
\[
 p_n(z)=\frac{2c_n(z)-c_n(1)}{c_n(1)}=2\frac{c_n(z)}{c_n(1)}-1.
\]
Note that \(c_n(1)>0\) and \(p_n(1)=1\) exactly.

**2. Verify the smooth critical point.** Put \(\rho=\log2\). At \((x,y)=(\rho,\rho)\),
\[
H=0,\quad H_x=H_y=-2,\quad H_{xx}=H_{yy}=-2,\quad H_{xy}=-4.
\]
The diagonal smooth-point equation \(xH_x=yH_y\) holds. The standard bivariate smooth-point nondegeneracy expression, defined explicitly in [1, Theorem 4.2], evaluates to
\[
Q(\rho,\rho)=16\rho^3(1-\rho)>0.
\]
The singularity is **strictly minimal**: [1, Lemma 4.1] proves this for exactly \(H(x,y)=1-(e^x-1)(e^y-1)\) when its auxiliary parameter is one. The numerator \(e^{zx+y}\) is entire and nonvanishing there for every complex \(z\). Thus the fixed-diagonal bivariate smooth-point theorem [1, Theorem 4.2, after Pemantle–Wilson] applies. Its leading geometric/Gaussian factor \(D_n>0\) is independent of \(z\), and for any fixed \(R>1\),
\[
c_n(z)=D_n\left(e^{(z+1)\rho}+O_R(n^{-1})\right),\qquad |z|\le R.
\]
The uniformity in \(z\) follows because \(e^{zx+y}\) and all finitely many derivatives required in the local saddle expansion are bounded on compact parameter discs, while the same strictly minimal critical point and exponentially negligible off-saddle contours work for every \(z\) in the disc. In particular
\[
c_n(1)=D_n\left(e^{2\rho}+O(n^{-1})\right)
\]
and dividing gives
\[
\frac{c_n(z)}{c_n(1)}=e^{(z-1)\rho}+O_R(n^{-1}).
\]
Substitution into the exact generating-function identity proves
\[
p_n(z)=2e^{(z-1)\rho}-1+O_R(n^{-1})=2^z-1+O_R(n^{-1}).
\]

**3. Convert the analytic error to a probability error.** The entire function \(2^z-1=e^{\rho z}-1\) has constant coefficient zero and coefficient \(\rho^k/k!\) for every \(k\ge1\). Since \(e^\rho-1=1\), these coefficients form a probability law, which is the zero-truncated Poisson\((\rho)\) law. Cauchy's estimate on the circle \(|z|=R>1\) gives the bound \(C_R/(nR^k)\) for every coefficient. Its summation yields \(d_{\rm TV}=O_R(n^{-1})\). Uniform convergence of the probability generating functions and their first two derivatives near \(z=1\) gives the stated moment limits and errors. A sink can belong to only one bipartition class; in the balanced case the part-swap involution makes the sink-bearing side exactly fair for every \(n\), and the conditional sink-count law is its unconditional law.

## Verification

The supplied standalone file `verify_sink.py` implements both the poly-Bernoulli Stirling formula and a direct, independent enumeration of all edge orientations of \(K_{a,b}\) for \(1\le a,b\le4\) (up to \(2^{16}\) orientations). An orientation is recognized as acyclic precisely when its binary matrix has no alternating \(2\times2\) minor, which characterizes lonesum matrices [2]. The checker compares complete sink-count tables and all indicated factorial moments exactly; it also compares large finite distributions numerically with the claimed limiting law. Running `python3 verify_sink.py` produced `VERIFY_OK 182 exact-enumerative and numerical cross-checks`. The non-finite conclusions rely on the analytic proof above, not on the numerical checks.

## Relationship to prior work

The lonesum-matrix correspondence, total counts and bivariate generating function for \(B_{a,b}\) are established in [2–4], not new. General acyclic-orientation sink polynomials, including the means to recover finite distributions in principle, are studied in [5]. Exact enumeration of orientations with a *unique* sink is studied in [6] and earlier work; in particular the one-sink probability is not separately asserted as novel here. The 2024 study [1] proves a Gaussian limit for **longest directed path length** on the same balanced graphs and supplies the critical-point transfer theorem and the strict-minimality lemma used above. The contribution claimed here is the **complete non-Gaussian limit for sink count together with a geometric local probability-error bound and total-variation rate**; unlike [1], the statistic does not grow on the order of the number of vertices. These are different claims and not a mere restatement of the longest-path theorem.

## Limitations

No exact leading constant is claimed for the total-variation distance, nor any result for highly unbalanced bipartitions or arbitrary graphs. The \(O_R(n^{-1})\) constants depend on the fixed disc radius and have not been numerically optimized. The published enumeration and transfer results are essential inputs, so this is not a new counting framework or a proof of those external theorems. Historical priority remains a risk: an equivalent sink law could be embedded in earlier literature under lonesum, poly-Bernoulli, or chromatic-symmetric-function terminology. Independent validation has not been performed.

## References

[1] J. Khera and E. Lundberg, *The distribution of the length of the longest path in random acyclic orientations of a complete bipartite graph*, arXiv:2408.12716, first posted 2024-08-22. https://arxiv.org/abs/2408.12716 . In particular Theorem 4.2 and Lemma 4.1.

[2] J. Khera, E. Lundberg and S. Melczer, *Asymptotic enumeration of lonesum matrices*, arXiv:1912.08850, first posted 2019-12-18. https://arxiv.org/abs/1912.08850 .

[3] P. J. Cameron, C. A. Glass, K. Rekvényi and R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, arXiv:1412.3685, first posted 2014-12-11. https://arxiv.org/abs/1412.3685 .

[4] B. Bényi and P. Hajnal, *Combinatorial properties of poly-Bernoulli relatives*, Integers 17 (2017), paper A31. https://math.colgate.edu/~integers/r31/r31.pdf .

[5] B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh and S.-H. Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions*, arXiv:1910.10920, first posted 2019-10-24. https://arxiv.org/abs/1910.10920 .

[6] A. Ayyer, D. Hathcock and P. Tetali, *Toppleable permutations, excedances and acyclic orientations*, arXiv:2010.11236, first posted 2020-10-21. https://arxiv.org/abs/2010.11236 .
