# A logarithmic-degree jamming window for a nearly complete dimer-adsorption graph

## Finding
For each even integer \(N\ge4\), let \(G_{N,d}\) consist of a clique on \(N-1\) labeled ordinary vertices and one exceptional vertex \(v\), joined to exactly \(d\) ordinary vertices, where \(0\le d\le N-1\). Perform irreversible unit-rate dimer adsorption: whenever both endpoints of an edge are vacant, that edge may receive a dimer, and each successful event occupies both endpoints. Equivalently, select each successive accepted edge uniformly from the currently available edges. Let \(R_{N,d}\) be the terminal number of vacant vertices and let \(p_{N,d}=\Pr(R_{N,d}=2)\).

Then \(R_{N,d}\in\{0,2\}\) almost surely, and for **every** sequence of allowed degrees \(d_N\) along even \(N\to\infty\),
\[
\boxed{\frac{d_N\log N}{N}\longrightarrow c\in[0,\infty]
\quad\Longrightarrow\quad
p_{N,d_N}\longrightarrow e^{-c},\qquad e^{-\infty}:=0.}
\]
In particular, if \(d_N\sim cN/\log N\) with \(c>0\), the two-vertex jamming probability converges to \(e^{-c}\). For \(d_N=o(N/\log N)\) it converges to one, and for \(d_N\gg N/\log N\) it converges to zero. For every \(d\ge1\), the graph nevertheless has a perfect matching.

An exact rational recurrence determines every finite probability: set \(F(1,0)=1\), \(F(1,1)=0\), and, for odd \(k\ge3\), \(0\le a\le k\), and \(b=k-a\), set
\[
F(k,a)=\frac{\binom a2 F(k-2,a-2)+abF(k-2,a-1)+\binom b2 F(k-2,a)}{\binom k2+a},
\quad p_{N,d}=F(N-1,d).
\]
Terms with zero combinatorial coefficients are omitted (so no out-of-range values are needed). This is the same theorem's exact finite-volume component, not an unrelated independent finding.

## Assumptions and scope
All graphs are simple and finite. Ordinary-ordinary edges form a complete graph; there are no other edges except the indicated \(d\) edges incident to \(v\). The occupied objects are edge dimers; each available edge has the same rate, regardless of its endpoints. The adsorption stops only when no edge joins two vacant vertices. We restrict to even \(N\); no randomness in the choice of the exceptional vertex's neighborhood is required, since ordinary-vertex relabeling preserves the law. The conventions at \(d=0\) and \(d=N-1\) are included. The limit is along even integer \(N\), and \(c\) is permitted to be infinite. Logarithms are natural.

## Proof
**1. Terminal states and finite recursion.** The vacant ordinary vertices induce a clique. Consequently, at jamming at most one ordinary vertex is vacant. Since \(N\) is even and each adsorption occupies two sites, the total number of vacant sites is even. Thus it is zero or two. If exactly two are vacant they consist of \(v\) and an ordinary vertex *not* joined to \(v\). If \(v\) is occupied first, the remaining ordinary vertices are an even-size clique and are completely occupied. If \(d\ge1\), matching \(v\) to one of its neighbors and pairing the other \(N-2\) vertices exhibits a perfect matching.

As long as \(v\) remains vacant, suppose that \(k\) ordinary vertices remain vacant and that \(a\) of these are neighbors of \(v\); put \(b=k-a\). The \(\binom k2\) ordinary-ordinary edges and the \(a\) edges to \(v\) are precisely the available edges. An edge to \(v\) makes a terminal two-vacancy event impossible. An ordinary pair either removes two neighbors, one of each type, or two nonneighbors, with respective edge counts \(\binom a2\), \(ab\), and \(\binom b2\). Conditioning on the first available edge proves the displayed recurrence, with the terminal \(k=1\) boundary. The complete-graph cases give \(p_{N,0}=1\) and \(p_{N,N-1}=0\).

**2. Exact permutation representation.** Write \(m=N-1\), \(\alpha=d/m\). Independently generate a uniformly random permutation of the ordinary vertices and view its ranks \(1,\dots,m\) in reverse removal order: the ordinary vertices surviving down to an odd size \(k\) have ranks \(1,\dots,k\). The \(d\) ranks belonging to neighbors of \(v\) form a uniform \(d\)-subset \(A\subseteq\{1,\dots,m\}\). Write \(a_k=|A\cap\{1,\dots,k\}|\) and \(Q_k=\binom k2\). Given that \(v\) has survived to size \(k\), the probability that the next accepted dimer occupies two ordinary sites is \(Q_k/(Q_k+a_k)\). Conditional on this choice, the pair is uniform among ordinary pairs, independently of its vertex types. Thus the independent random ordinary-pair removal order can be pre-generated, giving the **exact identity**
\[
p_{N,d}=\mathbb E\!\left[\mathbf1_{\{1\notin A\}}\prod_{\substack{3\le k\le m\\k\ \mathrm{odd}}}\frac{Q_k}{Q_k+a_k}\right].\tag{1}
\]
The last indicator enforces that the final ordinary site is not a neighbor; if it is a neighbor, the hub is matched instead. The representation follows directly by conditioning, not from a heuristic independence assumption.

**3. Concentration of the accumulated hazard.** Define
\[
T_m=\sum_{\substack{3\le k\le m\\k\ \mathrm{odd}}}\frac{a_k}{Q_k},\qquad
L_m=\sum_{\substack{3\le k\le m\\k\ \mathrm{odd}}}\log\!\left(1+\frac{a_k}{Q_k}\right).
\]
By uniform sampling without replacement, \(\mathbb E a_k=k\alpha\), and therefore, with \(H_j=\sum_{i=1}^{j}i^{-1}\),
\[
\mathbb E T_m=\alpha H_{(m-1)/2}.\tag{2}
\]
For each rank \(r\), define \(w_r=\sum_{k\ge r,\ k\ge3,\ k\ \mathrm{odd}}^m Q_k^{-1}\). Then \(T_m=\sum_{r\in A}w_r\), and \(0\le w_r\le C/r\) with an absolute constant \(C\). In particular, \(\sum_{r=1}^m w_r^2\le C'\) uniformly. Indicators of membership in a uniform fixed-size subset have nonpositive pairwise covariances, so
\[
\operatorname{Var}(T_m)\le \frac{m}{m-1}\alpha(1-\alpha)\sum_{r=1}^m w_r^2\le C''\alpha.\tag{3}
\]
Furthermore \(\operatorname{Var}(a_k)\le k\alpha\), and hence \(\mathbb E a_k^2\le k\alpha+k^2\alpha^2\). Since \(0\le t-\log(1+t)\le t^2/2\) for \(t\ge0\), we obtain
\[
0\le\mathbb E(T_m-L_m)
\le\frac12\sum_k\frac{\mathbb E a_k^2}{Q_k^2}
\le C_0(\alpha+\alpha^2).\tag{4}
\]
All constants are absolute, since the bounding series in \(k^{-2}\) and \(k^{-3}\) converge. Equations (2)–(4) establish the hazard approximation for the full range of \(d\), including sequences not satisfying any fixed positive density assumption.

**4. Critical window and both sides.** If \(d_N\log N/N\to c<\infty\), then \(\alpha\to0\) and \(\alpha H_{(m-1)/2}\to c\). By (2)–(4), \(L_m\to c\) in probability. Moreover, \(\Pr(1\in A)=\alpha\to0\). The random quantity inside the expectation in (1) is bounded by one and converges in probability to \(e^{-c}\); taking expectations proves \(p_{N,d_N}\to e^{-c}\).

If \(d_N\log N/N\to\infty\), then \(\mathbb E T_m\to\infty\) by (2). The variance in (3) is uniformly bounded, so \(T_m\to\infty\) in probability. The nonnegative difference \(T_m-L_m\) has uniformly bounded expectation by (4), and is tight. Hence \(L_m\to\infty\) in probability, so the product in (1) tends to zero in probability. Boundedness again yields \(p_{N,d_N}\to0\), completing all three regimes. No extrapolation from finite data is used.

## Verification
The standalone file `verify.py` uses only the Python standard library. Running `python verify.py` performs independent exact-rational finite-state checks for all exceptional degrees at \(N=4,6,8,10,12\). For every test it compares the symmetry recurrence against (i) an unrestricted labeled-vertex recursive Markov-chain computation and (ii) an independently enumerated exact permutation-product identity. It then checks illustrative finite approximations in the critical window at \(N=200,400,800,1600\). The extracted checker reports `ALL CHECKS PASSED: 102`. The analytic hazard bounds, and not these finite checks, prove the asymptotic theorem.

As an exact illustration at \(N=8\), \(p_{8,2}=739/1518\), \(p_{8,6}=1/21\), and the boundary values are \(p_{8,0}=1\) and \(p_{8,7}=0\).

## Relationship to prior work
Penrose and Sudbury (2005) provide the random sequential dimer-adsorption graph framework, uniform event-order equivalence, forward equations and regular-tree formulae. These are foundational; the article's examined statements do not provide the exceptional-vertex near-clique scaling window. Bennett and Bohman (2012, first arXiv version) give a dynamic-concentration theorem for random greedy matching on regular hypergraphs with specified codegree bounds; it does not apply to the highly nonregular graph family here, and it does not quantify the probability of exactly two unsaturated vertices. Dyer and Frieze (1991) discuss randomized greedy matching generally, but only the publisher's abstract was accessible for this comparison; the possibility of an unexamined equivalent calculation remains open. This result relies on the exact hazard representation and its shrinking-degree-density concentration, not on a claim that these general foundational methods are new.

## Limitations
This theorem is specific to uniform-edge sequential dimers on the stated near-clique graph family and even total vertex count. It does not classify graph-independent degree thresholds, arbitrary nonuniform adsorption rates, finite-time coverages, or arbitrary dense graphs. A full historical-priority check of every older greedy-matching paper has not been completed; in particular, the full text of Dyer and Frieze (1991) was unavailable during comparison. Exact computations only verify finite cases; the proof of the limiting law is analytical.

## References
1. M. D. Penrose and A. Sudbury, “Exact and approximate results for deposition and annihilation processes on graphs,” *Annals of Applied Probability* **15** (2005), 853–889; original preprint 2005-03-24, https://arxiv.org/abs/math/0503519; DOI: 10.1214/105051604000000765.
2. P. Bennett and T. Bohman, “A natural barrier in random greedy hypergraph matching,” original arXiv submission 2012-10-12, https://arxiv.org/abs/1210.3581; later published in *Combinatorics, Probability and Computing* **28** (2019), 816–825.
3. M. Dyer and A. Frieze, “Randomized greedy matching,” *Random Structures & Algorithms* **2** (1991), 29–45, DOI: 10.1002/rsa.3240020104 (publisher abstract examined, full text unavailable).
