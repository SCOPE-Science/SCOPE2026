# Two-scale jamming and rare maximality failure in the rank-two Kneser graph

## Finding

Consider the rank-two Kneser graph \(KG(n,2)\): its vertices are the two-element subsets of \(\{1,\ldots,n\}\), and distinct vertices are adjacent if and only if they are disjoint. Fix an integer \(n\ge5\). Give each graph vertex an independent rate-one exponential arrival time. When a vertex arrives it is accepted if no previously accepted vertex is adjacent to it. Let \(I_n\) be the final accepted set and let \(T_n\) be the time of its last successful arrival (not the last attempted arrival).

Write \(N_n=\binom n2\). Let \(E_1,E_2,E_3\) be independent exponential random variables with respective rates \(N_n,2(n-2),n-2\), and let \(M_{n-4}\) be the maximum of \(n-4\) independent rate-one exponential random variables, independent of the three \(E_i\). Set \(B_n=E_1+E_2+E_3\). Then the *complete joint law* of final cardinality and jamming time is

\[
 (|I_n|,T_n)\ \stackrel{\mathrm d}=\
 \begin{cases}
 (3,B_n),&\text{with probability }1/(n-2),\\
 (n-1,B_n+M_{n-4}),&\text{with probability }(n-3)/(n-2),
 \end{cases}
\]
where the case choice is independent of all displayed exponential variables. In the first case the selected edges of the ground complete graph form a triangle; in the second they form the full star about one ground vertex. Conditional on either shape, the labeled final family is uniform among all families of that shape.

In particular, the random greedy maximal independent set misses the maximum size by \(n-4\) with exact probability \(1/(n-2)\). Although this probability vanishes, its contribution makes

\[
 \operatorname{Var}(|I_n|)=\frac{(n-4)^2(n-3)}{(n-2)^2}\sim n,
 \qquad
 \frac{|I_n|-\mathbb E|I_n|}{\sqrt n}\xrightarrow{\mathbb P}0.
\]
Thus the centered square-root-normalized output converges to zero in probability while its variance converges to one, an explicit failure of second-moment convergence under an asymptotically optimal random greedy algorithm.

The two jamming-time mechanisms have *different time scales*. Conditional on the exceptional triangle outcome,
\[
 nT_n\xrightarrow{\mathrm d}\operatorname{Exp}(2)+\operatorname{Exp}(1)
\]
with independent summands. Conditional on the star outcome,
\[
 T_n-\log(n-4)\xrightarrow{\mathrm d}G,
 \qquad \Pr(G\le t)=\exp(-e^{-t}),
\]
where \(G\) is standard Gumbel. The exceptional event therefore jams in time of order \(1/n\), whereas typical successful outcomes require order \(\log n\).

## Assumptions and scope

Each vertex of \(KG(n,2)\) has its own one-time independent, continuous, rate-one exponential clock; rejected arrivals never become accepted later. A graph vertex represents an unordered two-subset, not an element of the underlying \(n\)-point set. All cardinality assertions are for \(n\ge5\) (the exceptional triangle and star have distinct sizes). The two time limits are conditional distributions along integer \(n\to\infty\), with the first scaled by \(n\) and the second shifted by \(\log(n-4)\). No statement is made for higher-uniformity Kneser graphs \(KG(n,k)\) with \(k\ge3\), or for non-exponential arrival clocks (although random-order final cardinality holds for any i.i.d. continuous clocks).

## Proof

1. **Structural reduction.** A set of graph vertices is independent exactly when the associated edges of the ground complete graph are pairwise intersecting. If the first two accepted edges are \(ab\) and \(ac\), every further admissible edge either contains \(a\) or is \(bc\). Accepting \(bc\) ends the process at the three-edge triangle: no other edge meets all three of \(ab,ac,bc\). Accepting a third distinct edge \(ad\), with \(d\notin\{a,b,c\}\), excludes \(bc\) forever; then exactly the remaining edges containing \(a\) are admissible, all of which must eventually be accepted. These produce the full \((n-1)\)-edge star. The symmetry of the ground labels implies conditional uniformity among triangles or stars.

2. **Exact exponential race.** Initially the \(N_n\) independent unit clocks have minimum \(\operatorname{Exp}(N_n)\). Once \(ab\) is selected, precisely \(2(n-2)\) not-yet-arrived vertices are admissible; by memorylessness the waiting time for the second successful arrival is an independent \(\operatorname{Exp}(2(n-2))\). Relabel its edge as \(ac\). Exactly \(n-2\) candidates remain: the single triangle closure \(bc\) and the \(n-3\) further star edges \(ad\). The third waiting time is independent \(\operatorname{Exp}(n-2)\), and its winner is uniform among these \(n-2\) candidates independently of all three waiting times. The triangle has probability \(1/(n-2)\).

3. **Terminal time on the star branch.** After a third edge \(ad\) is accepted, exactly \(n-4\) admissible star edges remain. Their residual unit exponential clocks are independent of the previous races and winners; each will be accepted, regardless of irrelevant rejected arrivals. Their last arrival takes another \(M_{n-4}\). This proves the joint mixture in the Finding, including independence of branch and the displayed times. The exact finite-time transform, for each \(s\ge0\), is
\[
 \mathbb E[e^{-sT_n};\ |I_n|=3]
 =\frac1{n-2}\prod_{\lambda\in\{N_n,2(n-2),n-2\}}\frac{\lambda}{\lambda+s},
\]
\[
 \mathbb E[e^{-sT_n};\ |I_n|=n-1]
 =\frac{n-3}{n-2}\prod_{\lambda\in\{N_n,2(n-2),n-2\}}\frac{\lambda}{\lambda+s}
 \prod_{j=1}^{n-4}\frac{j}{j+s}.
\]
The last product is the Laplace transform of the maximum of \(n-4\) independent unit exponentials, via exponential order-statistic spacings.

4. **Moments and limits.** The final size equals \(n-1\) minus \(n-4\) times a \(\operatorname{Bernoulli}(1/(n-2))\) variable. This gives the stated variance and convergence in probability. Furthermore \(nE_1\to0\) in probability, while \(nE_2\Rightarrow\operatorname{Exp}(2)\) and \(nE_3\Rightarrow\operatorname{Exp}(1)\). The third successful time \(B_n\to0\) in probability. Finally, for any real \(t\),
\[
 \Pr(M_{n-4}\le\log(n-4)+t)
 =\left(1-\frac{e^{-t}}{n-4}\right)^{n-4}\to e^{-e^{-t}},
\]
with the displayed finite-n formula understood for all sufficiently large \(n\). Independence and Slutsky's theorem yield the two conditional limits.

## Verification

Run `python3 check.py` from this directory. The standard-library verifier constructs exact incompatibility bitmasks for \(KG(n,2)\), recursively solves its full random-order greedy law using rational probabilities for \(n=5,6,7,8\), exhaustively tests the candidate-set counts and terminal branch shapes for each first/second/third accepted edge, and tests exact means, variances, and exponential-Laplace factors. Its deterministic execution reports the failure probabilities \(1/3,1/4,1/5,1/6\), respectively, and passes 16 grouped checks. These finite checks are supplemental; the four proof steps establish the theorem for all integers \(n\ge5\).

## Relationship to prior work

Pippenger (1989) introduced general random sequential adsorption on graphs and its jamming observable, without a stated \(KG(n,2)\) marked-time law in the accessible abstract. Dhara, van Leeuwaarden and Mukherjee (first public preprint 2016-04-13) study generalized RSA on sparse Erdős–Rényi graphs; their full accessible formulation addresses a different random-host density regime. Krivelevich, Mészáros, Michaeli and Shikhelman (2023 preprint / 2024 journal) study random greedy independent sets through local-limit theory, not this dense Kneser family or its exceptional fast jamming. Balogh, Krueger and Luo (2021 preprint / 2023 journal) study the maximum independent-set threshold in random subgraphs of Kneser graphs, not arrival-order greedy dynamics on a fixed full Kneser graph. Known structural classification of intersecting edge families underlies Step 1; the finite exponential-rate decomposition and its two conditional scales are the contribution assessed here.

## Limitations

This is an exact result for a highly structured rank-two family. It does not predict greedy performance for general Kneser graphs or arbitrary dense graphs. The nonconvergent variance phenomenon is for the *cardinality* scaled by \(\sqrt n\), not the usual independence ratio normalized by the total number \(\binom n2\) of graph vertices. Exact historical priority has not been independently established: an earlier general RSA theorem or specialized random greedy Kneser analysis might implicitly give some of these formulas. The 1989 full paper could not be read from the accessible publisher abstract; related public research summaries were compared by scientific content, not treated as complete original full texts.

## References

- N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* 2 (1989), 393–401, https://doi.org/10.1137/0402034. Published abstract and primary MSC 60K35.
- S. Dhara, J. S. H. van Leeuwaarden, D. Mukherjee, “Generalized random sequential adsorption on Erdős–Rényi random graphs,” first submitted 2016-04-13, https://arxiv.org/abs/1604.03918.
- M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, “Greedy maximal independent sets via local limits,” https://doi.org/10.1002/rsa.21200.
- J. Balogh, R. A. Krueger, H. Luo, “Sharp threshold for the Erdős–Ko–Rado theorem,” https://arxiv.org/abs/2105.02985 and https://doi.org/10.1002/rsa.21090.
