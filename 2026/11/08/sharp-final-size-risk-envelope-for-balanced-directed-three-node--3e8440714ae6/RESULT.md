# Sharp final-size risk envelope for balanced directed three-node SIR networks

## Finding
For a balanced zero-loop directed transmission network on three individuals, the entire continuous-time stochastic SIR final-size distribution admits an exact one-parameter formula. With a fixed next-generation spectral radius, the probability of a complete three-person outbreak and the mean final size are **minimized by a one-way directed triangle** and **maximized by the symmetric two-way triangle**. This gives a sharp stochastic-order comparison—not merely a comparison of expectations—and an exact optimal gap across transmission/recovery ratios.

## Assumptions and scope
There are exactly three individuals labeled \(0,1,2\). Initially one is infectious and two are susceptible; once an individual recovers, immunity is permanent. An infectious individual \(i\) infects a susceptible individual \(j\) at instantaneous rate \(\beta a_{ij}\), independently of recovery, and recovers at rate \(\gamma>0\). Assume \(\beta>0\), \(a_{ii}=0\), \(a_{ij}\ge0\), and every row and column of \(A=(a_{ij})\) sums to one. Zero transmission rates are allowed. All infectious periods are independent exponentials; transmissions use the standard continuous-time Markov chain rates. Define \(b=\beta/\gamma\), and let \(K\in\{1,2,3\}\) count the individuals ever infected (including the seed). The process terminates almost surely because it has only three individuals and no reinfection.

With a cyclic labeling, row and column sum constraints force
\[
A_p=\begin{pmatrix}0&p&1-p\\1-p&0&p\\p&1-p&0\end{pmatrix},\qquad 0\le p\le1.
\]
The normalized next-generation matrix at the all-susceptible state is \(bA_p\) or its transpose, depending on convention. Its Perron root is exactly \(b\), independent of \(p\), since all row sums are one.

The exact distribution is
\[
\Pr(K=1)=\frac1{1+b},\qquad
\Pr(K=2)=\frac{b}{(1+b)(1+b+b^2p(1-p))},
\]
\[
\Pr(K=3)=\frac{b^2(1+bp(1-p))}{(1+b)(1+b+b^2p(1-p))}.
\]
For fixed \(b>0\), larger \(p(1-p)\) means a larger final size in first-order stochastic order. Strictness holds for the upper tail \(\Pr(K\ge3)\) whenever the products differ; the other nontrivial tail \(\Pr(K\ge2)\) is fixed. The unique maximizing matrix is \(p=1/2\); the minimizing matrices are the directed cycles \(p=0\) and \(p=1\). Their difference is
\[
\Delta(b)=\Pr_{p=1/2}(K=3)-\Pr_{p=0}(K=3)=\frac{b^3}{(1+b)^2(2+b)^2}.
\]
The same difference holds for \(\mathbb E[K]\). Maximizing over all \(b>0\) gives
\[
\max_{b>0}\Delta(b)=\frac{33\sqrt{33}-189}{8},
\quad b_{\mathrm{opt}}=\frac{3+\sqrt{33}}2.
\]

## Proof
**Exhaustiveness of the contact family.** Write \(a_{01}=p\); row zero forces \(a_{02}=1-p\). Column two then forces \(a_{12}=p\) and row one forces \(a_{10}=1-p\). The remaining row and column constraints determine the third row \((p,1-p,0)\). Nonnegativity forces \(0\le p\le1\). Since the matrix is row stochastic, \(A_p\mathbf1=\mathbf1\). Its infinity norm is one, so its spectral radius is one; hence \(\rho(bA_p)=b\).

**Exact epidemic size.** Rescale time so each infectious recovery rate is one. At the initial state the seed has total infection hazard \(b\) and recovery hazard one. Therefore the probability of no secondary case is \(1/(1+b)\), and the probability of at least one is \(b/(1+b)\). Condition on a second infection occurring. Exactly two people are infectious at that moment, and the exponential memoryless property gives each an independent fresh unit-rate residual infectious lifetime. Their rates toward the third, still-susceptible person are \(bp\) and \(b(1-p)\), in some order, regardless of which neighbor became infected. The probability that neither infects the third before its own recovery is
\[
\frac1{1+bp}\cdot\frac1{1+b(1-p)}
=\frac1{1+b+b^2p(1-p)}.
\]
This also remains valid at the directed-cycle endpoints where one of the two infection rates is zero. Consequently \(\Pr(K=2)=\frac{b}{1+b}[1+b+b^2p(1-p)]^{-1}\), and subtracting from the probability of a second infection yields the asserted third-infection probability. Cyclic symmetry makes the result independent of the seed.

**Sharp stochastic ordering.** Let \(q=p(1-p)\), so \(0\le q\le1/4\). The lower nontrivial tail satisfies \(\Pr(K\ge2)=b/(1+b)\) for all \(q\). The upper tail satisfies
\[
\Pr(K\ge3)=\frac b{1+b}\left(1-\frac1{1+b+b^2q}\right),\quad
\frac{\partial\Pr(K\ge3)}{\partial q}=\frac{b^3}{(1+b)(1+b+b^2q)^2}>0.
\]
Since these are the only nontrivial tail events for \(K\in\{1,2,3\}\), this establishes the exact first-order stochastic order. The range and unique maximizer of \(q=p(1-p)\) establish sharpness.

**Universal maximum of the spread.** Subtracting the values at \(q=1/4\) and \(q=0\) gives \(\Delta(b)\) above, and \(\mathbb E[K]=1+\Pr(K\ge2)+\Pr(K\ge3)\) gives the same expectation gap. Differentiation yields
\[
\Delta'(b)=-\frac{b^2(b^2-3b-6)}{(1+b)^3(2+b)^3}.
\]
The polynomial in the numerator has exactly one positive root, \(b=(3+\sqrt{33})/2\). The derivative is positive below and negative above it. Since \(\Delta(b)\to0\) as \(b\to0^+\) and \(b\to\infty\), this is the unique global maximizer. Exact substitution yields \((33\sqrt{33}-189)/8\).

## Verification
For \(b=1\), the directed-cycle endpoints give \(\Pr(K=1,2,3)=(1/2,1/4,1/4)\), while the symmetric triangle gives \((1/2,2/9,5/18)\), a complete-outbreak difference of \(1/36\). The independent `CHECKER.py` builds the finite SIR Markov chain using infectious and recovered bitmasks, recursively evaluates the hitting probability of all three individuals becoming infected, and verifies the exact formula, derivative, maximizer, and rational example symbolically. It requires Python 3 and SymPy and can be run as `python3 CHECKER.py`. No simulation result is used in place of the proof.

## Relationship to prior work
Ueki, Thompson and Banaji (2026, arXiv:2601.13730), publicly available from January 20, 2026, define a stochastic network/metapopulation SIR generator and next-generation matrix and study outbreak vulnerability under different network architectures. Their main results rely on simulations and approximations for larger subnetworks; their analytic complete-symmetric appendix does not give this exact directed-balanced three-person extremum.

McCulloch, Roberts and Laing (2016, DOI below) derive exact final sizes for **undirected unweighted** small SIR graphs including the equal-edge triangle; this includes the symmetric \(p=1/2\) endpoint after rescaling rates and is not claimed as new. Their discussion explicitly identifies directed small-network extensions as further study. The present distinction is the *entire* continuous balanced directed family and its sharp, global, fixed-\(\rho\) stochastic-order and risk-gap optimization.

Wilkinson, Ball and Sharkey (2017) develop a directed-contact stochastic SIR/message-passing framework; Hall and Siebert (2023) give exact tree solutions and general bounds. Neither inspected result states this exact cyclic weighted three-node extremum. General finite-state Markov methods can of course compute fixed parameter choices, so publication-level novelty remains subject to specialist confirmation.

## Limitations
The result assumes exactly three nodes, a single initial infective, independent exponential recoveries, static rates, and both row and column balance. It does not establish a monotone ordering for arbitrary asymmetric directed networks, for correlated recovery times, for four or more nodes, or for post-outbreak immunity or vaccination strategies. It does not claim that reproduction number alone orders outbreak risk; in fact, it constructs a continuum of distinct risks with the same reproduction number. The undirected equal-edge endpoint is covered by prior work. An unknown equivalent weighted-three-node calculation or stronger general ordering theorem remains a scholarly priority to check independently.

## References
- M. Ueki, R. N. Thompson and M. Banaji, *Outbreak dynamics and population vulnerability in stochastic epidemic models on networks*, arXiv:2601.13730 (first posted January 20, 2026), https://arxiv.org/abs/2601.13730 .
- K. McCulloch, M. G. Roberts and C. R. Laing, *Exact analytical expressions for the final epidemic size of an SIR model on small networks*, ANZIAM J. 57 (2016), 429–444, https://doi.org/10.1017/S1446181116000043 .
- R. Wilkinson, F. Ball and K. Sharkey, *The relationships between message passing, pairwise, Kermack–McKendrick and stochastic SIR epidemic models*, J. Math. Biol. (2017), https://doi.org/10.1007/s00285-017-1123-8 .
- C. L. Hall and B. A. Siebert, *Exact solutions and bounds for network SIR and SEIR models using a rooted-tree approximation*, J. Math. Biol. (2023), https://doi.org/10.1007/s00285-022-01854-9 .
