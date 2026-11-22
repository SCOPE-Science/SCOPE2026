# A marked Poisson law for the last isolation deaths in randomly uncovered cycle powers

## Finding
Fix an integer \(d\geq1\). On \(C_n^d\), the \(d\)-th power of the labelled cycle with vertex set \(\mathbb Z/n\mathbb Z\), reveal all vertices in a uniformly random order. Write \(P_v\in\{1,\ldots,n\}\) for the forward reveal rank of vertex \(v\), and \(R_v=n+1-P_v\) for its reverse rank. Let
\[
N_d(v)=\{v-d,\ldots,v-1,v+1,\ldots,v+d\}\pmod n,
\quad a_n=n^{1-1/(2d)},
\quad T_v=\max_{w\in N_d(v)}R_w.
\]
When \(R_v>T_v\), vertex \(v\) is isolated on its arrival and ceases to be isolated exactly when the earliest of its \(2d\) neighbours appears. Let \(J_v\in\{-d,\ldots,-1,1,\ldots,d\}\) be the unique signed offset of the neighbour attaining the maximum reverse rank in \(T_v\). Put \(\mathbb T=\mathbb R/\mathbb Z\), and form the point measure
\[
\Xi_{n,d}=\sum_{v:R_v>T_v}\delta_{(T_v/a_n,\ v/n,\ P_v/n,\ J_v)}.
\]
Here the four coordinates are the scaled number of vertices still hidden when this isolated vertex dies; the dying vertex's position on the cycle; its *original* arrival fraction; and the signed direction of the neighbour that kills its isolation.

**Theorem (marked late-death process).** For every fixed \(d\geq1\), as \(n\to\infty\), \(\Xi_{n,d}\) converges vaguely in distribution on \((0,\infty)\times\mathbb T\times[0,1]\times\{-d,\ldots,-1,1,\ldots,d\}\setminus\{0\}\) to a Poisson point process with intensity
\[
\boxed{\quad 2d\,x^{2d-1}\,dx\;ds\;du\;\frac1{2d}\sum_{j\in\{-d,\ldots,-1,1,\ldots,d\}}\delta_j.\quad}
\]
Thus the location, original arrival fraction, and killing direction are independent uniform marks, and independent of the limiting death-time coordinate. This is a *joint spatial-temporal* statement, not solely a Poisson approximation for an isolated-vertex count at one time.

For any fixed \(m\geq1\), let \(\xi_{n,1}\leq\cdots\leq\xi_{n,m}\) be the first \(m\) time coordinates in \(\Xi_{n,d}\), with attached marks (the convention for too few points is irrelevant asymptotically). Then the vector of times and marks converges to the first \(m\) atoms of the limit process. In particular, if \(\xi_1<\xi_2<\cdots\) are the limiting ordered times,
\[
\boxed{\quad \xi_j^{2d}\sim\operatorname{Gamma}(j,1),\qquad
f_{\xi_j}(x)=\frac{2d}{(j-1)!}x^{2dj-1}e^{-x^{2d}}\quad(x>0).\quad}
\]
Their associated spatial positions and original arrival fractions are independent uniforms, and their killing directions are independent uniforms among the \(2d\) neighbours, jointly independent of the entire ordered time sequence. The \(j=1\) time law is the previously known Weibull last-isolation law; the multi-event process and independent marks are the contribution assessed here.

## Assumptions and scope
The integer \(d\) is *fixed* as \(n\to\infty\), and \(n>2d+1\) so each cyclic neighbourhood has exactly \(2d\) distinct vertices. Every vertex is revealed exactly once, in a uniformly random permutation, with no edge deletions or extra randomness. All point-process statements use bounded sets of scaled reverse time, and weak/vague convergence against compactly supported continuous test functions; no claim about uniformity for \(d\) growing with \(n\) or about the entire unscaled history is made. Birth ranks \(P_v\) are normalized by \(n\), not by \(n-1\). The spatial coordinate \(v/n\) is interpreted modulo one.

## Proof
**1. Exact isolation-interval identity.** In the reverse process after \(k\) vertices have been removed from the forward visible set, the unseen-forward set is \(U_k=\{v:R_v\leq k\}\). Vertex \(v\) is visible and isolated in the forward induced graph precisely when all its neighbours are in \(U_k\) but \(v\notin U_k\), that is,
\[
T_v\leq k<R_v.
\]
Consequently \(v\) is ever isolated if and only if \(T_v<R_v\); its last forward-isolated time is \(n-T_v\), and its isolation is ended by the neighbour with reverse rank \(T_v\). Distinct vertex ranks guarantee the unique signed direction \(J_v\).

**2. Independent priorities and the proxy.** Assign independent \(Y_v\sim\operatorname{Unif}(0,1)\), and let the reverse permutation expose vertices in increasing order of \(Y_v\). Put \(\varepsilon_n=n^{-1/(2d)}\), so \(a_n=n\varepsilon_n\), and for every center define
\[
Z_v=\varepsilon_n^{-1}\max_{w\in N_d(v)}Y_w,
\quad B_v=1-Y_v,
\quad I_v=\arg\max_{j\in\{-d,\ldots,-1,1,\ldots,d\}}Y_{v+j}.
\]
Consider first the *proxy* point process \(\widetilde\Xi_{n,d}=\sum_v\delta_{(Z_v,v/n,B_v,I_v)}\). The proxy includes even those centers whose own reverse arrival might occur too early. Such invalid centers are asymptotically absent from every bounded time window, as proved in step 5.

**3. One-center intensity, including all marks.** For \(0\leq a<b<\infty\), an arc \(S\subseteq\mathbb T\) with null-boundary and a birth-fraction interval \(U\subseteq[0,1]\), and any particular direction \(j\), the independent uniforms give, for sufficiently large \(n\),
\[
\mathbb P\{Z_v\in(a,b],B_v\in U,I_v=j\}
=\frac{|U|}{2d}\,\frac{b^{2d}-a^{2d}}{n}.
\]
There are \(n|S|+o(n)\) centers with \(v/n\in S\), so the expected count in this product set tends to
\[
|S|\,|U|\,\frac{b^{2d}-a^{2d}}{2d}.
\]
This agrees with the advertised intensity, including its spatial and directional normalizations.

**4. All mixed factorial moments.** Take a fixed collection of disjoint continuity sets that are finite unions of product boxes as in step 3, with time coordinates bounded by \(M\). Expand any joint mixed factorial moment as a sum over ordered *distinct* centers. If their closed radius-\(d\) neighborhoods are pairwise disjoint, the relevant independent-priority variables are disjoint, so the summand factors exactly. All but \(O_{d,q}(n^{q-1})\) ordered \(q\)-tuples have this property, and the contribution from the disjoint tuples converges to the product of the corresponding intensity masses.

For the remaining tuples, first build the graph connecting centers whose **open** neighbor sets overlap. A component with one center uses \(2d\) neighbor sites; a component containing multiple distinct centers uses at least \(2d+1\) neighbor sites, since for all large \(n\) the fixed-radius open neighborhoods are distinct. If the overlap graph has \(c\) components, including \(h\geq1\) nonsingletons, the total number of required small-priority neighbor vertices is at least \(2dc+h\). There are \(O_{d,q}(n^c)\) placements of every fixed overlap type. The probability that all those neighbor priorities are at most \(M\varepsilon_n\) is at most \((M\varepsilon_n)^{2dc+h}\). Hence the total contribution is
\[
O_{d,q,M}\bigl(n^c\varepsilon_n^{2dc+h}\bigr)
=O_{d,q,M}\bigl(n^{-h/(2d)}\bigr)=o(1).
\]
Any remaining tuples with intersecting closed neighborhoods but *disjoint* open neighbor sets occur in only \(O_{d,q}(n^{q-1})\) placements; their neighbor-priority events are independent and have probability at most \((M\varepsilon_n)^{2dq}=O(n^{-q})\), so they contribute \(O(n^{-1})\). Marks cannot increase these bounds. Thus all mixed factorial moments converge to the independent Poisson values for every disjoint family of continuity boxes. Local boundedness of expected counts and a standard countable continuity-box determination imply vague convergence of \(\widetilde\Xi_{n,d}\) to the advertised marked Poisson point process.

**5. Invalid centers are negligible.** A proxy center with \(Z_v\leq M\) that is not a genuine isolation-death center must satisfy \(Y_v\leq\max_{w\in N_d(v)}Y_w\leq M\varepsilon_n\). Together with all \(2d\) neighbor priorities being at most \(M\varepsilon_n\), this event has probability at most \((M\varepsilon_n)^{2d+1}\). The expected number of such centers is bounded by
\[
n(M\varepsilon_n)^{2d+1}=M^{2d+1}n^{-1/(2d)}\longrightarrow0.
\]
Therefore, with probability tending to one, proxy and genuine centers coincide throughout the time window \([0,M]\). Moreover, for such a center the true killer direction \(J_v\) equals the proxy direction \(I_v\).

**6. Replacing priority times by permutation ranks.** Define the empirical counting function \(N_n(y)=\#\{v:Y_v\leq y\}\). For each fixed \(M\),
\[
\sup_{0\leq y\leq M\varepsilon_n}|N_n(y)-ny|=O_{\mathbb P}(\sqrt{a_n})=o_{\mathbb P}(a_n).
\]
For completeness, first \(N_n(M\varepsilon_n)\) is binomial with mean \(Ma_n\) and fluctuation \(O_{\mathbb P}(\sqrt{a_n})\); conditional on this count, the priorities inside that interval are independent uniforms, whose empirical distribution has uniform count error \(O_{\mathbb P}(\sqrt{a_n})\) by the elementary empirical-distribution maximal bound. Thus \(R_v=N_n(Y_v)\) gives \(T_v/a_n-Z_v\to0\) in probability uniformly for all proxy atoms with \(Z_v\leq M\). The global empirical-distribution law also gives \(\sup_v|R_v/n-Y_v|\to0\) in probability, and therefore \(P_v/n-B_v\to0\) uniformly. These perturbations preserve the vague point-process limit because its intensity has no atoms on coordinate boundaries.

**7. Ordered late deaths.** The limiting process has cumulative time intensity \(\Lambda(x)=x^{2d}\), which increases strictly to infinity. Its transformed event times \(\xi_j^{2d}\) are therefore the arrival times of a unit-rate Poisson process, hence \(\operatorname{Gamma}(j,1)\). The independent marking theorem follows directly here from the product intensity (and independently from the factorial-moment construction). Convergence of the first fixed \(m\) ordered atoms follows from local point-process convergence, absence of ties, and the bounds \(\Lambda(x)\downarrow0\) as \(x\downarrow0\), \(\Lambda(x)\uparrow\infty\) as \(x\uparrow\infty\). This completes the proof.

## Verification
The standalone \(CHECKER.py\) enumerates all forward reveal permutations for \((n,d)=(5,1),(6,1),(7,1),(8,1),(6,2),(7,2)\), independently reconstructs the entire forward isolation history at each time, and compares it against the rank-based isolation intervals and killer directions for every center. It also verifies, using integer cross-multiplication, the exact expected active-isolate count at every reverse time \(k\):
\[
\mathbb E I_{n,d}(k)=n\frac{(k)_{2d}(n-k)}{(n)_{2d+1}},
\]
where \((z)_r=z(z-1)\cdots(z-r+1)\) denotes the falling factorial. This identity follows directly by requiring the center to remain visible and its full neighbor set to be removed. The checker passed \(944805\) exact combinatorial assertions. These finite computations test definitions, ordering, edge cases and normalization; they do **not** replace the infinite proof in steps 2–7.

## Relationship to prior work
Kleiner (2026), arXiv:2609.29488v1, proves an exact finite law and the scalar Weibull limit for the single *last* isolation time in powers of cycles, and a single-time Poisson limit for completed-neighborhood counts. Its Section 6 uses overlap factorial-moment bounds that are also useful here. It does **not** state the marked space-time point-process theorem, the joint order-statistic laws for multiple late deaths, or the asymptotic joint independence of the original reveal fraction, spatial location and killing direction.

Janson, *Uncovering a graph* (first circulated 2023; journal 2025), studies globally centered Gaussian processes of visible edges and related small-subgraph counts, not extreme late-isolation deaths. Arratia, Goldstein and Gordon (1989) supplies the general locally dependent Poisson-approximation framework; the explicit decorated limit here is a model-specific specialization whose normalization and true-versus-proxy comparison require proof. No priority claim is made for general point-process convergence technology or for the known single-last-death Weibull law.

## Limitations
The proof assumes fixed \(d\); it does not handle graph powers growing with \(n\), nonuniform reveal orders, or arbitrary graph sequences. The theorem concerns finitely many late deaths and compact scaled time windows; it does not give exact finite multivariate probabilities or a global coupling error rate in total variation. It supplies asymptotic uniform birth fractions, not exact finite-\(n\) uniformity. The general marked Poisson paradigm is classical and a different literature may already contain an equivalent specialized result; absence of one from the searches conducted is not a proof of priority. Independent mathematical assessment has not been performed.

## References
1. I. Kleiner, *The Last Isolated Vertex in Random-Order Uncovering of Cycles and Their Powers: Exact Enumeration and Weibull Limits*, arXiv:2609.29488v1, first public 2026-08-24. https://arxiv.org/html/2609.29488v1 ; https://arxiv.org/abs/2609.29488 .
2. S. Janson, *Uncovering a graph*, Probability Theory and Related Fields **195** (2026), 689–740, first online 2025-09-01, arXiv:2312.13823 (2023). https://doi.org/10.1007/s00440-025-01401-9 .
3. R. Arratia, L. Goldstein and L. Gordon, *Two moments suffice for Poisson approximations: the Chen–Stein method*, Annals of Probability **17** (1989), 9–25. https://doi.org/10.1214/aop/1176991491 .
