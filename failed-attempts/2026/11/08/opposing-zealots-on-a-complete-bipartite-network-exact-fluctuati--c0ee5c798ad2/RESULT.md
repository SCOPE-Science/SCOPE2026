# Opposing zealots on a complete bipartite network: exact fluctuations and a Beta limit

## Finding

Fix integers \(a,b\ge2\). Put one permanently opinion-1 zealot in the size-\(a\) part of the complete bipartite graph \(K_{a,b}\), and one permanently opinion-0 zealot in the size-\(b\) part. Every nonzealot vertex, independently at rate one, replaces its binary opinion by that of a uniformly sampled neighbor. Let \(F_{a,b}\) be the proportion of all \(a+b\) vertices with opinion 1 under the unique stationary distribution. Then

\[
\mathbb E[F_{a,b}]=\frac{b}{a+b},\qquad
\operatorname{Var}(F_{a,b})=\frac{(a-1)(b-1)}{(a+b-1)(3a+3b-4)}.
\]

If \(a+b\to\infty\) along **any** sequence for which \(a/(a+b)\to\alpha\in(0,1)\), with \(\beta=1-\alpha\), then

\[
F_{a,b}\ \xrightarrow{\mathrm d}\ \operatorname{Beta}(2\beta,2\alpha).
\]

The limiting variance is \(\alpha\beta/3>0\), so the stationary opinion fraction does not self-average. With balanced parts the limit is exactly uniform on \([0,1]\); unequal part sizes produce a skewed, explicitly parameterized Beta limit. The mean and full limiting shape register the placement of the two opposing zealots in differently sized parts.

## Assumptions and scope

The graph is a finite, undirected, unweighted \(K_{a,b}\), \(a,b\ge2\). The unique zealot in the left part has opinion 1; the unique zealot in the right part has opinion 0. Ordinary vertices copy one random neighbor at independent rate-one Poisson update times. The continuous-time stationary law, not a quasi-stationary law conditioned on nonconsensus, is used. Opinion-1 counts in the unpinned left and right parts are denoted \(I\in\{0,\ldots,a-1\}\) and \(J\in\{0,\ldots,b-1\}\), respectively; thus \(F_{a,b}=(1+I+J)/(a+b)\). At the law-of-large-numbers scale the two part sizes must both grow in positive limiting proportions. No claim about extreme imbalance \(\alpha=0\) or \(\alpha=1\) is made.

## Proof

**1. Generator and uniqueness.** The opinion-count process \((I,J)\) is Markov. From state \((i,j)\), its four nonzero-neighbor transition rates are

\[
\begin{aligned}
q_{(i,j),(i+1,j)}&=\frac{(a-1-i)j}{b},&
q_{(i,j),(i-1,j)}&=\frac{i(b-j)}{b},\\
q_{(i,j),(i,j+1)}&=\frac{(b-1-j)(i+1)}{a},&
q_{(i,j),(i,j-1)}&=\frac{j(a-1-i)}{a}.
\end{aligned}
\]

Out-of-range transitions have zero rate. Starting from any state, first use copies of the fixed opinion-0 vertex to change all left unpinned vertices to opinion 0, then use a left unpinned zero to change all right unpinned vertices to zero. Therefore every state can reach \((0,0)\). Conversely \((0,0)\) can reach each state except \((a-1,0)\): introduce a right opinion-1 via the fixed left zealot, generate the desired left opinion-1 count, and, when the target has no right opinion-1 vertices, use a remaining left zero to remove the temporary right one. The exceptional state \((a-1,0)\) has an exit and cannot be entered from another state, so it is transient. All other states form the unique recurrent communicating class; hence the stationary distribution is unique. Individual configurations with the same pair of counts have equal stationary probabilities by within-part permutation symmetry.

**2. Exact first moments.** By symmetry, denote the stationary mean of a free left opinion by \(x\) and that of a free right opinion by \(y\). Stationarity of each indicator yields

\[
x=\frac{b-1}{b}y,\qquad y=\frac{1+(a-1)x}{a},
\]

hence \(x=(b-1)/(a+b-1)\) and \(y=b/(a+b-1)\). Summing over all unpinned vertices and the fixed left opinion-1 gives \(\mathbb E[1+I+J]=b\). Division by \(a+b\) proves the mean formula.

**3. Exact second moments.** Let \(U\) be the stationary product moment of two distinct free left opinions, \(V\) the product moment of one free opinion from each part, and \(W\) the product moment of two distinct free right opinions. A moment requiring two free vertices in a part is used only if such a pair exists; when the part size is two its multiplicity vanishes in the final variance identity. Direct application of the generator to products gives

\[
U=\frac{b-1}{b}V,\qquad
W=\frac ya+\frac{a-1}{a}V,
\]

and

\[
2V=\frac{y+(b-2)W}{b}+\frac{2x+(a-2)U}{a}.
\]

Solving these equations and writing \(n=a+b\) gives

\[
\begin{aligned}
U&=\frac{(b-1)(a+3b-4)}{(n-1)(3n-4)},\\
V&=\frac{b(a+3b-4)}{(n-1)(3n-4)},\\
W&=\frac{b(a+3b-2)}{(n-1)(3n-4)}.
\end{aligned}
\]

When a corresponding same-part pair does not exist, these displayed expressions are algebraic extensions; no nonexistent product variable is required. The pairwise covariances for distinct left-left, left-right and right-right free vertices respectively simplify to

\[
\frac{a(b-1)(n-2)}{(n-1)^2(3n-4)},\quad
\frac{ab(n-2)}{(n-1)^2(3n-4)},\quad
\frac{b(a-1)(n-2)}{(n-1)^2(3n-4)}.
\]

Summing the Bernoulli variances and these covariances with their exact ordered-pair multiplicities yields

\[
\operatorname{Var}(1+I+J)
=\frac{(a-1)(b-1)n^2}{(n-1)(3n-4)}.
\]

Dividing by \(n^2\) proves the finite stationary variance formula, including \(a=2\) or \(b=2\).

**4. The limiting stationary law.** Take a sequence with \(a/n\to\alpha\in(0,1)\), \(b/n\to\beta=1-\alpha\). Define the partwise fractions \(p=(I+1)/a\), \(q=J/b\), their average \(z=(p+q)/2\), and their difference \(d=p-q\). The exact generator \(L\) obeys

\[
Lp=q-p+\frac{1-q}{a},\qquad
Lq=p-q-\frac p b,
\]

so

\[
Ld=-2d+\frac{1-q}{a}+\frac p b,
\qquad
Lz=\frac12\left(\frac{1-q}{a}-\frac p b\right).
\]

Jumps in \(d\) have size at most \(1/a\) or \(1/b\); their respective total rates are at most \(a\) and \(b\). Consequently the quadratic variation rate satisfies \(\Gamma(d,d)\le1/a+1/b\). Applying stationarity to \(d^2\), and using \(0\le p,q\le1\) in the resulting quadratic estimate, proves \(\mathbb E[d^2]=O(1/a+1/b)=O(1/n)\). In particular \(p-q\to0\) in probability under the stationary laws.

For a fixed polynomial \(f\), an exact jump-generator Taylor expansion, with jumps of \(z\) at most \(1/(2\min(a,b))\), shows

\[
 n Lf(z)
=\frac{1}{4\alpha\beta}
\left[2(\beta-z)f'(z)+z(1-z)f''(z)\right]+o_{L^1}(1).
\]

To justify the error: the drift expression above has error bounded by a constant times \(\lvert p-q\rvert+\lvert a/n-\alpha\rvert\); the quadratic-variation coefficient has the same form of error plus \(O(1/n)\); and the third-order Taylor remainder is \(O(1/n)\) because the total update rate is at most \(n\). All bounds are uniform on \([0,1]^2\) except the explicitly controlled \(\lvert p-q\rvert\), whose stationary first moment tends to zero.

Since the stationary distributions of \(z\) are supported on \([0,1]\), every subsequence has a further weakly convergent subsequence. Let \(\nu\) be any such limit. Stationarity and the expansion imply for all polynomials \(f\)

\[
\int_0^1\left[2(\beta-t)f'(t)+t(1-t)f''(t)\right]d\nu(t)=0.
\]

Writing \(m_k=\int t^k d\nu(t)\), applying this to \(f(t)=t^k\), \(k\ge1\), gives the exact recurrence

\[
m_0=1,\qquad m_k=\frac{k-1+2\beta}{k+1}m_{k-1}.
\]

These are precisely the moments of the \(\operatorname{Beta}(2\beta,2\alpha)\) law, since its two shape parameters sum to two. Measures supported on \([0,1]\) are determined by their polynomial moments, so every subsequential limit is that Beta distribution. Finally, \(F_{a,b}=(a p+b q)/n\), and \(F_{a,b}-z=((a-b)/(2n))(p-q)\to0\) in probability. Therefore \(F_{a,b}\) has the same weak limit. Its variance also converges to \(\alpha\beta/3\) directly from the finite formula. This completes the proof.

## Verification

The standalone `verify.py` uses Python 3 and SymPy, no outside files. Run `python3 verify.py`. It independently constructs and exactly solves the full count-process stationary linear equations for every \((a,b)\in\{2,3,4,5\}^2\), comparing means and variances with the theorem. It additionally verifies symbolic finite second-moment equations, the variance simplification, and the first twelve recurrences of the claimed Beta moments using exact rational and symbolic algebra. These computations test but do **not** replace the proof of uniqueness or weak convergence given above.

## Relationship to prior work

The initiating study by Njougouo, Reina, Tuci and Carletti develops opinion copying with zealots and heterogeneous social contact, primarily using heterogeneous mean-field analysis; its mechanisms motivate examining opposing, permanently fixed zealots on a structured network. Mobilia, Petersen and Redner analyze stationary magnetization fluctuations for zealots in the well-mixed voter model. Vendeville, Guedj and Zhou derive mean opinions through stationary linear systems for general fixed-network zealot influence. Ben-Ari and collaborators study a different object, the quasi-stationary distribution of the **zealot-free** voter model on complete bipartite graphs. Mori, Hisakado and Nakayama derive beta-related distributions in a different noisy multigroup voter process. Romero Moreno and collaborators investigate influence allocation and partial zealots on heterogeneous networks. These provide valuable background or general mean techniques, but none of the inspected material supplies the joint finite variance formula and proportional-bipartition Beta-limit theorem here. In particular the symmetric uniform limit resembles earlier well-mixed two-zealot results and is not asserted as an independently novel phenomenon; the main distinction is the exact dependence on bipartition imbalance in the finite and limiting laws.

## Limitations

The result applies to uniform-neighbor copying on an unweighted complete bipartite graph, exactly two opposed fixed zealots located in opposite parts, and positive limiting proportions of both parts. It does not cover simultaneous majority updating, biased copying, other zealot placements, stochastic network rewiring, or regimes with one part sublinear in the total size. No full closed-form finite stationary mass function is asserted; only the finite first two moments are supplied. Formal and numerical checks do not constitute an external independent audit. Publication-priority comparisons are based on identifiable inspected sources and are necessarily non-exhaustive.

## References

1. T. Njougouo, A. Reina, E. Tuci, T. Carletti, *On the role of zealots in a best-of-n problem on a heterogeneous network* (first public version 2023-12-30), https://arxiv.org/abs/2401.00114.
2. M. Mobilia, A. Petersen, S. Redner, *On the Role of Zealotry in the Voter Model* (2007), https://arxiv.org/abs/0706.2892.
3. A. Vendeville, B. Guedj, S. Zhou, *Towards control of opinion diversity by introducing zealots into a polarised social group* (2020), https://arxiv.org/abs/2006.07265.
4. I. Ben-Ari, A. Panzo, R. Speegle, K. VandenBerg, *Quasi-Stationary Distributions for the Voter Model on Complete Bipartite Graphs* (2020), https://arxiv.org/abs/2004.10187.
5. S. Mori, M. Hisakado, K. Nakayama, *A voter model on networks and multivariate beta distribution* (2018), https://arxiv.org/abs/1810.05643.
6. G. Romero Moreno, E. Manino, L. Tran-Thanh, M. Brede, *Zealotry and Influence Maximization in the Voter Model: When to Target Zealots?* (2020), https://arxiv.org/abs/2008.10012.
