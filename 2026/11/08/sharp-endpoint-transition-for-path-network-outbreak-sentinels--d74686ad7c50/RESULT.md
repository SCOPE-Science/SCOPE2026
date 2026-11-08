# Sharp endpoint transition for path-network outbreak sentinels

## Finding

Let \(P_n\) be the undirected path on \(n\ge3\) labeled vertices \(1,\ldots,n\). Every edge is independently open with probability \(p\in(0,1)\). An epidemic starts at one uniformly selected vertex and eventually reaches precisely its open-edge connected component. Exactly \(k\) distinct vertices are perfectly monitored, with \(2\le k<n\). Detection occurs if the infected component intersects the monitored set. Write \(\mathcal D(S)\) for the probability of eventual detection by a set \(S\) of size \(k\).

Set \(N=n-k\), \(m=k-1\), and \(q=\lceil N/m\rceil\). Every globally optimal placement is characterized by taking the \(N\) largest available marginal rewards, with admissible ties, from two boundary-gap sequences and \(m\) interior-gap sequences:

\[
\begin{aligned}
 b_t&=p^t,& t&=1,2,\ldots,\\
 h_t&=p^t[1+t(1-p)],&t&=1,2,\ldots.
\end{aligned}
\]

Each sequence must be taken as an initial segment. The boundary sequences describe unmonitored vertices before the first and after the last sentinel; each interior sequence describes unmonitored vertices between consecutive sentinels. Thus this marginal rule gives the exact maximum and all maximizing placements for arbitrary \(n,k,p\), including ties. In every maximizing placement the two boundary gaps differ by at most one, the interior gaps differ by at most one, and each interior gap is at least as long as either boundary gap.

There exists a globally optimal placement monitoring **both endpoints** \(1,n\) if and only if

\[
 p^{q-1}[1+q(1-p)]\ge1.
\]

If \(q=1\), all global optima monitor both endpoints for every \(p\in(0,1)\). For each integer \(q\ge2\) there is a unique \(p_q\in(0,1)\) distinct from the trivial root \(p=1\), solving

\[
 p_q^{q-1}[1+q(1-p_q)]=1.
\]

If \(p<p_q\), no optimum monitors both endpoints; if \(p=p_q\), some optima do and some do not; if \(p>p_q\), every optimum does. These thresholds are strictly increasing with \(q\), and

\[
 1-p_q\sim\frac{2}{q^2}\qquad(q\to\infty).
\]

As an exact illustration, with \(n=10\), \(k=3\), and \(p=1/2\), the optimal sentinel sets are \(\{2,5,9\}\) and \(\{2,6,9\}\), with detection probability \(109/160\); monitoring both endpoints gives at most \(101/160\). When \(p=9/10\), the optimal sets are \(\{1,5,10\}\) and \(\{1,6,10\}\), each with probability \(486897/500000\). In this example \(q=4\) and \(p_4\approx0.868876852095\).

## Assumptions and scope

- Exactly one uniform random initial source; no further importations.
- Independent, identically retained *undirected* path edges, with one common \(p\in(0,1)\).
- Eventual reachability, not detection time, clinical cases averted, or multi-period feedback.
- Exactly \(k\) error-free sentinel vertices; no placement costs or restrictions.
- Integers \(n\ge3\), \(2\le k<n\). The single-sentinel case is the separate classical center-of-path problem, and \(k=n\) is trivially detected with probability one.

Let the ordered sentinel locations be \(s_1<\cdots<s_k\). Define nonnegative integers

\[
 L=s_1-1,\quad R=n-s_k,\quad g_i=s_{i+1}-s_i-1\ (1\le i<k).
\]

They satisfy \(L+R+\sum_i g_i=N\). Conversely, every such integer vector identifies one placement. This gives a bijection between sentinel sets and allocations of the \(N\) unmonitored vertices into \(k+1\) gaps.

## Proof

**1. Exact detection objective.** Let \(B(g)=\sum_{t=1}^{g}p^t\) and \(G(g)=2B(g)-gp^{g+1}\), with \(B(0)=G(0)=0\). An initial source at a sentinel is detected with probability one. An initial source at distance \(j\) in either outer tail is detected with probability \(p^j\). If it is between sentinels separated by \(g+1\) edges, at distance \(j\in\{1,\dots,g\}\) from the left sentinel, independent edges on the two disjoint connecting subpaths give the probability

\[
 p^j+p^{g+1-j}-p^{g+1}
\]

of reaching at least one sentinel. Summing over possible uniform sources yields exactly

\[
 n\mathcal D(S)=k+B(L)+B(R)+\sum_{i=1}^{k-1}G(g_i). \tag{1}
\]

**2. Strictly decreasing gap marginals.** Appending the \(t\)-th unmonitored vertex to a boundary gap gains \(b_t=B(t)-B(t-1)=p^t\). Appending it to an interior gap gains

\[
 h_t=G(t)-G(t-1)=p^t[1+t(1-p)].
\]

Both sequences are strictly decreasing: for every positive integer \(t\),

\[
 b_t-b_{t+1}=p^t(1-p)>0,\qquad
 h_t-h_{t+1}=(t+1)p^t(1-p)^2>0. \tag{2}
\]

Any feasible gap allocation selects initial segments of these \(k+1\) sequences, totaling \(N\) items. If a selected marginal is strictly smaller than an unselected marginal, transferring one gap unit from the end of the former sequence to the beginning of the latter increases (1). Conversely, taking the \(N\) largest marginals with any valid tie-breaking is a feasible collection of initial segments (strict decrease inside each sequence), and exchanging any unit cannot improve it. This proves both sufficiency and necessity, and characterizes every maximizing placement.

For two interior gaps differing by two or more, moving one unit from the longer to the shorter improves (1) by (2). The same holds for the two outer gaps. If an outer gap has length \(\ell>g\), where \(g\) is an interior gap, moving a unit from the outer to the interior changes the score by

\[
 h_{g+1}-b_{\ell} = p^{g+1}[1+(g+1)(1-p)]-p^\ell>0,
\]

since \(g+1\le\ell\). These exchange arguments give all stated gap inequalities.

**3. Sharp endpoint condition.** Suppose \(L=R=0\). The best such allocation distributes all \(N\) units among \(m=k-1\) identical interior sequences as evenly as possible, with every \(g_i\) equal to \(\lfloor N/m\rfloor\) or \(\lceil N/m\rceil=q\). Its smallest selected marginal is \(h_q\). Every unselected interior marginal is at most \(h_q\). The first available marginal on either empty boundary is \(b_1=p\). The top-\(N\) characterization therefore says an evenly allocated endpoint-monitoring placement is globally optimal exactly when \(h_q\ge p\), or

\[
 p^{q-1}[1+q(1-p)]\ge1. \tag{3}
\]

For \(q=1\), the left side equals \(2-p>1\). If (3) is strict, every top-\(N\) allocation excludes boundary units, so all optima monitor both endpoints. If equality holds, transferring one unit from a length-\(q\) interior gap to an outer gap preserves the objective and yields an optimum with an unmonitored endpoint. If (3) fails, no endpoint-monitoring allocation can be optimal.

For \(q\ge2\), put \(F_q(p)=p^{q-1}(q+1-qp)\). Its derivative is

\[
 F'_q(p)=p^{q-2}(q^2-1-q^2p).
\]

Thus \(F_q\) rises strictly from zero to its single maximum at \(1-q^{-2}\), then falls strictly to \(F_q(1)=1\). The maximum exceeds one, so there is exactly one crossing \(p_q\) in \((0,1-q^{-2})\); the only other root on \((0,1]\) is the boundary point one. This proves the strict phase claims.

**4. Monotonicity and quadratic scaling.** For fixed \(p\in(0,1)\),

\[
 \frac{F_{q+1}(p)}{F_q(p)}
 =\frac{p[1+(q+1)(1-p)]}{1+q(1-p)}<1.
\]

Therefore \(F_{q+1}(p_q)<1\) and the nontrivial crossing moves right: \(p_{q+1}>p_q\). For each fixed \(c>0\), substituting \(p=1-c/q^2\) gives, by Taylor expansion with a remainder uniform for fixed \(c\),

\[
 \log F_q(1-c/q^2)=\frac{c-c^2/2}{q^2}+O_c(q^{-3}). \tag{4}
\]

For every fixed \(\varepsilon\in(0,2)\), expression (4) is positive at \(c=2-\varepsilon\) and negative at \(c=2+\varepsilon\) for all large \(q\). By the unique nontrivial crossing, \(2-\varepsilon<q^2(1-p_q)<2+\varepsilon\). This proves the asymptotic law.

**5. Exact illustration.** Evaluating (1) using \(p=1/2\), \(n=10\), \(k=3\) yields the optimal \(109/160\) and best two-endpoint score \(101/160\). At \(p=9/10\), (3) holds strictly because \((9/10)^3[1+4/10]>1\). The evenly distributed interior gaps then produce precisely the stated optimal sets and the exact probability \(486897/500000\). The two as-even-as-possible interior arrangements correspond to distributing seven empty vertices as \((3,4)\) or \((4,3)\).

## Verification

Run `python verify.py` using Python 3.10 or later; no third-party dependencies. The checker independently enumerates all open-edge configurations and all uniform sources for small paths, comparing against (1). It exhaustively compares every sentinel set with the marginal allocation rule for various exact rational transmission probabilities, checks the endpoint criterion and tie cases, verifies the exact ten-vertex example, and numerically diagnoses the asymptotic threshold. At packaging, 6,546 assertions and diagnostics passed.

The finite verification does not establish the universal theorem; steps 1–4 above supply the analytical proof. The script is not a finite exhaustion of all \(n,k,p\).

## Relationship to prior work

Leskovec, Krause, Guestrin, Faloutsos, VanBriesen and Glance (2007) introduced a general outbreak-detection placement objective and submodular near-optimal methods. Khanna and Lucier (2013/2014) studied independent-cascade influence maximization on undirected networks. By symmetry of undirected connectivity, maximizing our uniform-source detection probability is *exactly equivalent* to maximizing the expected number of vertices reachable from the chosen sentinel set, divided by \(n\); hence the present work is an exact **path specialization** of their broader optimization framework, not a new diffusion model. Neither inspected source states the all-size path-gap characterization or the endpoint critical values (3)–(4), and their general approximation theorems do not logically imply those exact values.

Holme (2017) studies optimal node importance in SIR epidemiology on connected graphs up to seven vertices, including sentinel discovery time, which is distinct from eventual detection probability. Colman, Holme, Sayama and Gershenson (2019) compare heuristic sentinel placements on spatial and modular networks through SIR simulations; their optimization objective emphasizes cases potentially averted or detection delay, not the exact path endpoint transition. These are useful context but do not settle (3) in their inspected material. A further source under a synonym such as path influence maximization, probabilistic coverage, or facility location may give the same threshold; that historical priority risk remains.

## Limitations

The theorem is structural and exact for paths, uniform source distribution, homogeneous independent *undirected* transmission, perfect final-case detection, and fixed sentinel number only. It gives no claim about arbitrary trees, cycles, heterogeneous edges, correlated transmissions, source priors, temporal detection, vaccination efficacy, dilution, or real surveillance costs. Endpoint optimality can coexist with several tied placements at the threshold. The literature review is not a proof of historical uniqueness, and independent review has not been performed.

## References

1. J. Leskovec, A. Krause, C. Guestrin, C. Faloutsos, J. VanBriesen and N. Glance, "Cost-effective outbreak detection in networks," *ACM SIGKDD* (2007), doi:10.1145/1281192.1281239. Lawful technical report: https://www-cs.stanford.edu/~jure/pubs/detect-techRept.pdf (dated June 2007, with no day stated); conference proceedings dated August 12–15, 2007.
2. S. Khanna and B. Lucier, "Influence maximization in undirected networks," *SODA* (2014), online December 18, 2013, doi:10.1137/1.9781611973402.109. Public manuscript: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/Influence-Maximization-in-Undirected-Networks.pdf.
3. P. Holme, "Three faces of node importance in network epidemiology: Exact results for small graphs," *Physical Review E* **96**, 062305 (2017), doi:10.1103/PhysRevE.96.062305; arXiv:1708.06456.
4. E. Colman, P. Holme, H. Sayama and C. Gershenson, "Efficient sentinel surveillance strategies for preventing epidemics on networks," *PLOS Computational Biology* **15** (2019), e1007517, doi:10.1371/journal.pcbi.1007517, https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007517.
