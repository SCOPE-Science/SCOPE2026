# Fractional-power cover-time improvement from pairing the leaves of a star

## Finding

Let \(F_m=K_1\vee(mK_2)\) be the friendship (triangular windmill) graph with \(m\ge 1\) triangles sharing one hub. Let \(S_m=K_{1,2m}\) be the star on the same \(2m+1\) vertices. On each graph take the discrete-time simple random walk initially at the hub, and let \(C_F(m)\) and \(C_S(m)\) denote its expected number of edge traversals needed to visit every vertex, without requiring a return to the hub. Put \(H_q=\sum_{j=1}^{q}1/j\). Then the exact finite-size law is

\[
C_F(m)=3m\int_0^\infty\big[1-(1-2e^{-3u/4}+e^{-u})^m\big]du-2,
\qquad C_S(m)=4mH_{2m}-1.
\]

The difference has a *positive, sharp fractional-power asymptotic*:

\[
\boxed{\displaystyle \lim_{m\to\infty}\frac{C_S(m)-C_F(m)}{m^{2/3}}=2^{2/3}\Gamma(4/3)=1.417516616051\ldots .}
\]

In particular, pairing the star's leaves to make triangles decreases the expected cover time for all sufficiently large \(m\), while the two families have the same leading term \(4m\log(2m)\). The precise \(m^{2/3}\) scale and its gamma-function coefficient are the main claim.

## Assumptions and scope

The graphs are finite, undirected, unweighted and simple. At each integer time the walker chooses each neighboring vertex with equal probability. The hub is visited at time zero; other vertices must all be visited before stopping. The result applies to every integer \(m\ge1\) for the finite formula, and to the limit \(m\to\infty\) for the asymptotic. No continuous-time walk is being substituted for the discrete-time dynamics: an independent rate-one Poisson process is used only as an exact analytical device for counting hub-to-hub excursions.

## Proof

**1. Excursion decomposition.** Each excursion of the walk from the hub until its next return selects one of the \(m\) petals uniformly. On the chosen two-vertex petal, the walker first visits a uniformly selected peripheral vertex and then takes a geometrically distributed number of steps to hit the hub, with success parameter \(1/2\). Thus an excursion has mean length \(3\) jumps. If the petal is wholly unvisited, that excursion covers both peripheral vertices with probability \(1/2\) and exactly one with probability \(1/2\). If precisely one vertex has been visited, the excursion visits the other with probability \(3/4\): either the first vertex is new (probability \(1/2\)), or the first is old and the next step visits the new vertex (probability \(1/4\)). Consequently the state changes on a petal under independently marked excursions have exactly these probabilities.

**2. Exact Poissonized coverage.** Insert independent mean-one exponential waiting times between the excursion marks. The global Poisson process has rate one, and splitting by uniformly selected petals yields \(m\) independent Poisson processes, each of rate \(1/m\). In time \(t\), an initially untouched petal is still untouched with probability \(e^{-t/m}\), and is partially visited but not complete with probability \(2(e^{-3t/(4m)}-e^{-t/m})\). Therefore its probability of not being fully covered is

\[
q_m(t)=2e^{-3t/(4m)}-e^{-t/m}.
\]

If \(\tau_m\) denotes the first Poisson time when all petals are covered, independence gives \(\Pr(\tau_m\le t)=[1-q_m(t)]^m\). In particular,

\[
\mathbb E\tau_m=m\int_0^\infty[1-(1-2e^{-3u/4}+e^{-u})^m]du.
\]

Let \(N_m\) be the number of completed excursions needed to cover every petal. Since the exponential inter-arrival times are independent of the excursion marks, \(\mathbb EN_m=\mathbb E\tau_m\). The hub-return time after the \(N_m\)-th excursion has expectation \(3\mathbb EN_m\) by Wald's identity: the excursion lengths are identically distributed with finite mean \(3\), and \(N_m\) is a stopping time for the sequence of excursions, even though their lengths and coverage marks are correlated. The first moment when the final vertex is visited precedes that last hub return by mean \(2\) steps, by the strong Markov property at the final newly visited peripheral vertex. Hence \(C_F(m)=3\mathbb E\tau_m-2\), giving the integral formula. On the star, hub-to-leaf excursions take two steps, and the expected number needed to see all \(2m\) leaves is \(2mH_{2m}\); the last return costs one step. This proves \(C_S(m)=4mH_{2m}-1\).

For exact rational evaluation, expansion of the integrand gives

\[
C_F(m)=12m\sum_{j=1}^{m}(-1)^{j+1}\binom mj\sum_{k=0}^{j}\binom jk\frac{(-1)^k2^{j-k}}{3j+k}-2.
\]

**3. Sharp asymptotics by comparison to a shifted exponential maximum.** Set \(u_0=\tfrac43\log 2\). The law with survival probability \(\min\{1,2e^{-3u/4}\}\) is that of \(u_0+Z\), where \(Z\) has the exponential law of rate \(3/4\). The expected maximum of \(m\) such independent variables is exactly \(\tfrac43(\log2+H_m)\). Let \(I_m\) be the integral in the finding, and let

\[
D_m=\tfrac43(\log2+H_m)-I_m\ge0.
\]

The contribution to \(D_m\) from \(0\le u\le u_0\) is bounded by \(u_0 2^{-4m/3}\). In the remaining integral substitute \(x=2e^{-3u/4}\), so \(e^{-u}=2^{-4/3}x^{4/3}\), to obtain

\[
D_m=\frac43\int_0^1\frac{(1-x+2^{-4/3}x^{4/3})^m-(1-x)^m}{x}\,dx+O(2^{-4m/3}).
\]

With \(x=y/m\), the integrand after multiplication by \(m^{1/3}\) converges pointwise to \(2^{-4/3}e^{-y}y^{1/3}\). This convergence is dominated: writing \(c=2^{-4/3}<1\), the numerator is at most \(mcx^{4/3}[1-(1-c)x]^{m-1}\) by the mean-value inequality. After rescaling it is bounded by a constant times \(y^{1/3}e^{-(1-c)y/2}\) for \(m\ge2\), an integrable function. Dominated convergence therefore gives

\[
\lim_{m\to\infty}m^{1/3}D_m
=\frac43 2^{-4/3}\Gamma(4/3).
\]

It follows that

\[
C_F(m)=4m(\log2+H_m)-2^{2/3}\Gamma(4/3)m^{2/3}+o(m^{2/3}).
\]

Finally \(H_{2m}-H_m-\log2=O(m^{-1})\), so subtracting the exact star expression proves the boxed limit. All remainder estimates concern the limit of integer \(m\); no finite calculation is used to infer the infinite asymptotic.

## Verification

The standalone file `verify.py` evaluates three independent finite formulations: (i) the exact rational binomial sum above; (ii) a first-step recurrence on the numbers of untouched and partially visited petals; and (iii) the full, vertex-level absorbing Markov-chain linear equations for all visited subsets, without invoking Poissonization. The first two coincide exactly for \(1\le m\le10\), and the third coincides for \(1\le m\le4\). In particular \(C_F(1)=3\), \(C_F(2)=89/7\), \(C_F(3)=18981/770\), and \(C_F(4)=571073/15015\). Independent numerical integrations for \(m=100,1000,10000,100000\) give scaled star–friendship gaps converging toward the proved coefficient. Execute `python verify.py` with Python 3, SymPy, SciPy and NumPy installed. The proof itself is independent of software.

## Relationship to prior work

Zlatanov and Kocarev, *Random walks on networks: cumulative distribution of cover time* (arXiv:0910.3545v1, first posted 2009-10-19), give an exact inclusion–exclusion distribution for general graphs and worked simplifications for complete graphs, cycles, and paths. Their general formula provides a framework for arbitrary finite-graph cover times; it does not evaluate the paired-star family or establish the non-integer \(m^{2/3}\) gap. Aldous and Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6, Section 6.2 (1994), explicitly calculate the star's coupon-collector cover time but do not calculate the friendship family. The windmill-graph treatment in Random Services gives the relevant graph geometry and standard walk distributions, rather than this cover-time asymptotic. These are comparisons based on the material actually inspected, not proofs of historical novelty.

## Limitations

The theorem concerns a walk started at the common hub; it makes no assertion about starting at peripheral vertices. It shows a positive gap only asymptotically; positivity for every finite \(m\) is not part of the claim. The star and friendship graph have the same vertices but different numbers of edges. Its statistical-mechanical interpretation is a finite-network exploratory transport comparison, not a claim about a specific experimental system. Undiscovered earlier treatments of friendship or windmill cover time could bear on priority. The result has received no independent audit.

## References

1. N. Zlatanov and L. Kocarev, *Random walks on networks: cumulative distribution of cover time*, arXiv:0910.3545v1 (first public preprint 2009-10-19), https://arxiv.org/abs/0910.3545; *Physical Review E* **80**, 041102 (2009).
2. D. Aldous and J. A. Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6, §6.2, dated 1994-10-31, https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/Ch6.S2.html.
3. Random Services, *Random Walks*, windmill-graph section, https://www.randomservices.org/Reliability/Graphs/Walk.html (background geometry and walk kernels only).
