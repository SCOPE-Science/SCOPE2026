# Sharp fourth central moments and polarization transitions on complete multipartite graphs

## Finding

For every connected complete multipartite simple graph \(G=K_{n_1,\ldots,n_r}\) with \(r\ge2\), \(n_i\ge1\), \(N=\sum_i n_i\), and largest part size \(m=\max_i n_i\), give edges length one and vertices uniform mass \(1/N\). Define the sharp centered fourth-moment Lipschitz functional
\[
\mathcal M_4(G)=\max_{|f(u)-f(v)|\le1\ (uv\in E(G))}\frac1N\sum_{v\in V(G)}\left(f(v)-\frac1N\sum_{w\in V(G)}f(w)\right)^4.
\]
Put
\[
B_N(k)=\frac{k(N-k)[N^2-3k(N-k)]}{N^4}\quad(0\le k\le N),
\]
\[
T_{N,m}(t)=\frac mN+\left(\frac{6m}{N}-4\right)\frac{t^2}{N^2}-3\frac{t^4}{N^4}
\quad(0\le t\le m,\ t\equiv m\pmod2).
\]
Then the exact sharp value, for every such graph and every admissible integer parameter, is
\[
\boxed{\mathcal M_4(G)=\max\left\{\max_{0\le k\le N}B_N(k),\ \max_{\substack{0\le t\le m\\t\equiv m\ (\mathrm{mod}\ 2)}}T_{N,m}(t)\right\}.}
\]
All maximizing real functions are, up to addition of a constant, exactly the following feasible configurations whose displayed moment equals the boxed maximum: (i) an indicator of any \(k\)-vertex subset, with moment \(B_N(k)\); (ii) a function supported on **one largest part**, taking \(+1\) on \((m+t)/2\) vertices and \(-1\) on the other \((m-t)/2\), and zero elsewhere, possibly after global sign reversal, with moment \(T_{N,m}(t)\). Overlapping descriptions for degenerate two-level configurations are harmless.

There are two distinct asymptotically sharp changes of optimizer geometry. If \(N\to\infty\) and \(m/N\to w\in[0,1]\), then
\[
\lim\mathcal M_4(G)=\max\left\{\frac1{12},\ H(w)\right\},\qquad
H(w)=\begin{cases}w,&0\le w\le 2/3,\\w+3(w-2/3)^2,&2/3\le w\le1.\end{cases}
\]
Thus the asymptotic binary-to-polarized transition occurs at part density \(w=1/12\). Beyond \(w=2/3\) the optimal polarized imbalance becomes macroscopic, with \(|t|/N\to\sqrt{w-2/3}\); at or below this point it vanishes asymptotically. In the finite problem, writing \(s=m\bmod2\) and assuming \(m\ge s+2\), the minimum possible imbalance \(t=s\) ceases to maximize the polarized branch exactly when
\[
\boxed{\frac mN>\frac23+\frac{s^2+(s+2)^2}{2N^2}.}
\]
At equality both \(t=s\) and \(t=s+2\) maximize that branch; below it \(t=s\) is its sole nonnegative maximizing imbalance. The threshold is parity-sensitive: the correction is \(2/N^2\) for even \(m\), and \(5/N^2\) for odd \(m\).

## Assumptions and scope

Every graph is finite, simple, connected, complete multipartite and has at least two nonempty parts. All graph edges have length one, distances are shortest-path distances, the probability is uniform on all \(N\) vertices, and scalar functions are real-valued. The functional is the **unstandardized fourth centered moment**, equivalently the fourth power of the operator norm of the centered inclusion from the graph Lipschitz quotient into \(L^4\). It is not variance, kurtosis normalized by variance, or an uncentered fourth moment.

## Proof

**1. Reduction to integer-valued vertices.** Fix one vertex at value zero. The feasible set is the bounded graph-Lipschitz polytope given by oriented edge-difference inequalities with integral right-hand sides. Its matrix is a deleted-column directed incidence matrix, hence totally unimodular. All vertices are integer-valued. The map from this anchored space into the mean-zero subspace, \(f\mapsto f-\mathbb E f\), is injective. Because \(x\mapsto |x|^4\) is strictly convex, \(\sum_v|f(v)-\mathbb Ef|^4\) is strictly convex on the anchored space. Thus **every** maximizer, not merely at least one, is a vertex, and so is integer-valued.

**2. Vertex shapes.** Every complete multipartite graph has diameter at most two. An integer-valued feasible potential therefore has range at most two. If its range is one, it is an indicator up to translation. If the range is two, translate to levels \(-1,0,+1\). The vertices with levels \(-1\) and \(+1\) must belong to the same part because their difference is two and cross-part edges have length one. Every vertex outside that part is adjacent to both extreme levels and therefore has value zero. If a vertex in the selected part also had value zero, all its incident edges would have difference zero. Such a point cannot be a vertex of the Lipschitz polytope: a sufficiently small positive and negative perturbation of that one coordinate preserves every constraint. Hence all vertices in the selected part take \(\pm1\), all vertices outside take zero. These are the only potentially maximizing shapes.

**3. Exact moment computations.** An indicator with \(k\) ones gives the two-point law of success probability \(k/N\), whose fourth centered moment is \(B_N(k)\). If the chosen part has size \(a\) and there are \((a+t)/2\) plus and \((a-t)/2\) minus vertices, then the random function has raw moments \(\mathbb EX=t/N\), \(\mathbb EX^2=a/N\), \(\mathbb EX^3=t/N\), \(\mathbb EX^4=a/N\). Expanding \(\mathbb E(X-\mathbb EX)^4\) gives \(T_{N,a}(t)\). All these assignments satisfy the one-Lipschitz constraints, and the opposite sign gives the same moment.

**4. Only a largest part matters.** Define \(F_N(a)\) as the maximum fourth centered moment of a vector with exactly \(a\) entries in \(\{-1,+1\}\) and \(N-a\) zero entries. For \(1\le a<N\), start with an optimizer at \(a\) and change one zero entry from zero to either \(+1\) or \(-1\). Strict convexity in that coordinate gives \(\max\{\Phi(+1),\Phi(-1)\}>\Phi(0)\). Both altered vectors have exactly \(a+1\) nonzero entries. Thus \(F_N(a+1)>F_N(a)\). Hence only parts of maximum size \(m\) can support an optimal polarized vector. Together with steps 1--3 this establishes the exact formula **and every equality case**.

**5. Finite parity threshold.** As a function of the nonnegative real variable \(t\), the quartic \(T_{N,m}(t)\) is decreasing for \(m/N\le2/3\); otherwise it increases until \(t=N\sqrt{m/N-2/3}\) and decreases thereafter. For the parity lattice \(t=s,s+2,\ldots\), its minimum element \(s\) is beaten exactly when \(T_{N,m}(s+2)>T_{N,m}(s)\). Their difference equals
\[
\frac{(s+2)^2-s^2}{N^4}\left[(6m/N-4)N^2-3\bigl(s^2+(s+2)^2\bigr)\right],
\]
which has precisely the sign claimed. If the difference vanishes, unimodality gives exactly the two adjacent optimizing imbalance values.

**6. Limiting regimes.** The binary grid is dense in \([0,1]\), and maximizing \(q(1-q)[1-3q(1-q)]\) yields \(1/12\) at \(q=(1\pm1/\sqrt3)/2\). The polarized imbalance grid becomes dense in \([0,w]\); its limiting objective is \(w+(6w-4)z^2-3z^4\). The maximum is at \(z=0\) for \(w\le2/3\), and at \(z=\sqrt{w-2/3}\) for \(w>2/3\). The latter lies in the allowed interval since \(w^2-w+2/3>0\). Evaluating gives \(H(w)\), hence both asymptotic transitions.

## Verification

The included `verify_multipartite_m4.py` uses only exact Python integer arithmetic. It enumerates **every** anchored integer-valued one-Lipschitz potential taking values in \(\{-2,-1,0,1,2\}\) for all 58 complete multipartite graph types of orders \(2\) through \(8\); confirms the value and equality descriptions; checks strict part-size monotonicity for parameters through \(N=300\); and checks the precise finite skew-transition inequality for all sampled admissible parameters through \(N=300\). The script is independent corroboration of finite scopes; the universal theorem follows from the analytical argument above.

## Relationship to prior work

The graph-spread literature of Addario-Berry, Janson and McDiarmid, following Alon, Boppana and Spencer, studies maximum **variance** of one-Lipschitz functions. The relevant source provides the standard Lipschitz spread definition, integer-extremizer background, and complete-graph variance formula, but no sharp fourth-centered-moment formula for complete multipartite graphs. Higashitani, Jochemko and Michałek give a complete **facet/polar-potential classification** for complete multipartite graphs (Proposition 3.5); this structural result is prior work, not newly claimed. Its facet descriptions identify candidate extremal configurations but do not rank their centered fourth moments, select a largest part, derive the two phase thresholds, or classify which configurations maximize this quartic functional. The present result supplies those exact optimizations and limits, not a new facet-classification theorem.

## Limitations

No claim is made for nonuniform vertex probabilities, noninteger edge lengths, higher moments other than four, graphs that are not complete multipartite, or variance-normalized kurtosis. The asymptotic thresholds are limiting statements; the exact finite formula and parity criterion retain rounding effects. Primary-source comparisons reduce but do not eliminate the risk of an equivalent unindexed treatment. Reproducibility checks over finite sizes do not constitute a proof for every order. Independent validation has not been performed.

## References

1. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156 (initial public version 2009-02-06); journal version, *Combinatorics, Probability and Computing* 23 (2014), 477–504. https://arxiv.org/abs/0902.1156
2. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (2018), especially Theorem 3.1 and Proposition 3.5; *Mathematika* 65 (2019), 763–784. https://arxiv.org/abs/1807.07678
