# Strict collision-time slowdown from adding disjoint peripheral edges to a star

## Finding

For every integer \(n\ge3\), form the graph \(G_{n,k}\) from the star with \(n\) peripheral vertices by joining \(k\) disjoint pairs of peripheral vertices, where \(0\le k\le\lfloor n/2\rfloor\). Place two independent continuous-time simple random walkers at a uniformly chosen *unordered pair of distinct peripheral vertices*. Each walker jumps at total rate one and chooses an adjacent vertex uniformly. Write \(T_{n,k}\) for their first meeting time, and \(M_{n,k}=\mathbb E T_{n,k}\).

The exact mean is

\[
M_{n,k}=\frac{10n^3+8n^2-18n+27kn^2-66kn-9k+8k^2n+10k^2-4k^3}{(n-1)(5n^2+14n+9+8k)}.
\]

For every \(n\ge3\), these means strictly increase with the number of added edges:

\[
M_{n,0}<M_{n,1}<\cdots<M_{n,\lfloor n/2\rfloor}.
\]

In contrast, every \(k>0\) introduces a positive *initial* collision hazard:

\[
\Pr(T_{n,k}\le t)=\frac{2k}{n(n-1)}t+O_{n,k}(t^2)\quad(t\downarrow0),
\]

whereas \(\Pr(T_{n,0}\le t)=O_n(t^2)\). Thus the extra edges accelerate collisions at sufficiently short times while strictly increasing the expected first collision time for the same initial sampling rule.

The star value is \(M_{n,0}=2n/(n+1)\). For \(n=2m\ge4\) and the maximum matching \(k=m\), whose graph is the friendship (windmill) graph,

\[
M_{2m,m}=\frac{5m(4m-3)}{(2m-1)(2m+3)},\qquad
\lim_{m\to\infty}\frac{M_{2m,m}}{M_{2m,0}}=\frac52.
\]

More generally, if \(2k/n\to x\in[0,1]\) as \(n\to\infty\), then

\[
M_{n,k}\longrightarrow\frac{20+27x+4x^2-x^3}{10}.
\]

## Assumptions and scope

The graphs are finite, undirected, simple, unweighted, and connected. The hub is \(h\); the \(n\) other vertices are peripheral. There are exactly \(k\) disjoint peripheral-to-peripheral edges, so \(u=n-2k\) leaves have degree one and \(2k\) paired peripheral vertices have degree two. The hub has degree \(n\). Both walkers jump independently with **total rate one**, not with unit rate per incident edge. Simultaneous jumps have probability zero. Meeting means occupying the same vertex, not traversing an edge in opposite directions. The walkers start at distinct peripheral vertices sampled uniformly, **not** from the stationary distribution. All expectations are in physical time units of these rate-one Poisson clocks.

## Proof

**1. Six-state first-step reduction.** Let \(U\) denote an unpaired peripheral vertex and \(P\) a paired peripheral vertex. The distinct-position unordered pair chain has six symmetry types, with \(A,B,C,D,E,F\) denoting the corresponding expected first meeting times:

\[
A=H\!U,\quad B=H\!P,\quad C=UU,\quad D=UP,\quad E=PP_{\rm same},\quad F=PP_{\rm different}.
\]

Every transient pair has combined jump rate two. First-step conditioning yields

\[
\begin{aligned}
C&=\frac12+A,\\
D&=\frac{2+2B+A}{3},\\
E&=\frac12+\frac B2,\\
F&=1+B,
\end{aligned}
\qquad
\begin{aligned}
A&=\frac12+\frac{u-1}{2n}C+\frac{k}{n}D,\\
B&=\frac12+\frac14B+\frac{1}{2n}E+\frac{k-1}{n}F+\frac{u}{2n}D.
\end{aligned}
\]

For example, from \(HU\), the unpaired leaf walker hits the hub at rate one and the hub walker hits that leaf at rate \(1/n\), both being absorbing moves. The hub walker's remaining transitions lead to \(UU\) at total rate \((u-1)/n\) or \(UP\) at total rate \(2k/n\). The equations above apply to types that occur; when a type has zero multiplicity at a parameter boundary, its auxiliary expression can be understood algebraically through the neighboring nondegenerate cases. The exact mean below is also directly valid at both boundaries and is checked there by a direct chain equation.

**2. Rational solution and starting law.** Solving the two equations for \(A\) and \(B\), with

\[
\Delta=8k+5n^2+14n+9,
\]

gives

\[
\begin{aligned}
A&=\frac{8k^2+18kn-14k+15n^2+22n-9}{2\Delta},\\
B&=\frac{4k^2+12kn-6k+13n^2-9}{\Delta}.
\end{aligned}
\]

Among all \(\binom n2\) unordered distinct peripheral starting pairs, the numbers of types \(UU,UP,PP_{\rm same},PP_{\rm different}\) are respectively

\[
\binom u2,\quad 2ku,\quad k,\quad 2k(k-1).
\]

Their sum is \(\binom n2\). Consequently

\[
M_{n,k}=\frac{\binom u2 C+2kuD+kE+2k(k-1)F}{\binom n2}.
\]

Substitution of the rational values of \(A,B,C,D,E,F\) and collection of terms gives exactly the displayed formula for \(M_{n,k}\). At the boundary \(k=0\), only unpaired peripheral pairs occur. Solving \(A=1/2+(n-1)(1/2+A)/(2n)\) directly gives \(C=1/2+A=2n/(n+1)\). At the opposite boundary \(u=0\), necessarily \(n=2k\), the only reachable hub type is \(HP\), whose equation is \(B=1/2+B/4+E/(2n)+(k-1)F/n\). With \(E=1/2+B/2\) and \(F=1+B\), this yields \(B=(4n-3)/(n+3)\). Averaging \(k\) same-pair and \(2k(k-1)\) different-pair peripheral starts then gives exactly \(5k(4k-3)/[(2k-1)(2k+3)]\). Therefore both endpoint laws follow from actual accessible states and do not rely on assigning physical meaning to nonexistent auxiliary types.

The chain is finite and its absorption probability is one, since from each nonmeeting state there is a positive-probability path to a meeting state, so its finite expected first collision time is the unique solution of these first-step equations.

**3. Strict effect of each added peripheral edge.** Put \(\Delta_k=5n^2+14n+9+8k\). Directly subtracting the rational formulas gives, for every admissible increment \(0\le k<\lfloor n/2\rfloor\),

\[
M_{n,k+1}-M_{n,k}=\frac{P(k,u')}{(n-1)\Delta_k(\Delta_k+8)},\qquad u'=n-2(k+1)\ge0,
\]

where

\[
\begin{aligned}
P(k,u')={}&2560k^4+5040k^3u'+10928k^3\\
&+3660k^2u'^2+15688k^2u'+14660k^2\\
&+1160ku'^3+7272ku'^2+12896ku'+5264k\\
&+135u'^4+1088u'^3+2640u'^2+1404u'-1235.
\end{aligned}
\]

All terms are nonnegative except the constant \(-1235\). As \(n=2(k+1)+u'\ge3\), at least one of \(k\) and \(u'\) is positive. It follows that \(5264k+1404u'-1235>0\). The denominator is positive, proving strict monotonicity for all \(n\) and every admissible increment. This argument proves the infinite family, not merely a finite numerical test.

**4. Early collisions and large-size limit.** An initially separated pair has a positive one-jump collision rate only if its two vertices are connected. Exactly \(k\) of the \(\binom n2\) initial pairs are joined by the new peripheral edges; for each, either walker jumps to the other at rate \(1/2\), producing combined collision rate one. All other initial pairs require at least two jumps to meet. The finite-state exponential holding-time law gives the stated small-time expansion.

The star and fully paired identities follow by substituting \(k=0\) and \(n=2m,k=m\) into the exact rational function. Dividing numerator and denominator by \(n^3\) and taking \(2k/n\to x\) proves the general limiting profile and the ratio \(5/2\).

## Verification

The accompanying standalone \(\texttt{VERIFY.py}\) reconstructs the *full* unordered two-particle continuous-time Markov generator and solves its first-meeting Poisson equation using exact \(\texttt{Fraction}\) arithmetic without using the six-state quotient. It agrees with the closed formula for all 32 admissible cases \(3\le n\le10\), and it checks 5,549 adjacent-increment identities and positivity tests for \(3\le n<150\), as well as the exact end-point identities. The finite calculations support, but do not replace, the all-size algebraic proof above. Invoke \(\texttt{python3 VERIFY.py}\) in a standard Python 3 environment; no external packages are required.

## Relationship to prior work

Sanders (2009) studies mean recurrence intervals between particle encounters, rather than the present first-collision law under peripheral-pair initialization. Zhang, Tan, and Krishnamachari (2014) compute meeting times on regular graphs, including cycles and tori; the graphs here are nonregular. Cooper and collaborators (2012) establish coalescence-time bounds for arbitrary graphs, not these exact expectations. George, Patel, and Bullo (2018) provide general multiple-walker meeting-time linear systems, which in principle apply to these graphs; the present contribution is their explicit closed evaluation over a natural one-edge-at-a-time family and the strictly signed comparison with an opposite short-time effect. Sakumoto and Ohsaki (2020) analyze degree heterogeneity and approximate first-meeting scaling, not this exact matching perturbation. The older collision problem of Coppersmith, Tetali, and Winkler (1993) allows adversarial selection of moving tokens, a different dynamical rule. No claim is made to invent the generator method or the friendship graphs.

## Limitations

The result concerns independently moving walkers with unit **total** jump rates, a specific uniform initial distribution over distinct peripheral pairs, and fixed undirected unweighted matching additions. Changing to per-edge rates, stationary initialization, discrete synchronous time, exclusion on edge traversals, or arbitrary new peripheral edges changes the process and need not preserve the monotonicity. The large-size limit is for a density of disjoint peripheral matching edges. A comparison with all historical papers and unpublished calculations is not independently certified; general generator methods could have been specialized elsewhere. The mathematical checks are exact finite tests and a presented analytic proof, not an external formal certification.

## References

1. D. P. Sanders, *Exact encounter times for many random walkers on regular and complex networks*, arXiv:0906.0810 (first public 2009-06-04), https://arxiv.org/abs/0906.0810.
2. C. Cooper and collaborators, *Coalescing Random Walks and Voting on Connected Graphs*, arXiv:1204.4106 (2012), https://arxiv.org/abs/1204.4106.
3. Y. Zhang, Z. Tan, and B. Krishnamachari, *On the Meeting Time for Two Random Walks on a Regular Graph*, arXiv:1408.2005 (2014), https://arxiv.org/abs/1408.2005.
4. B. George, S. Patel, and F. Bullo, *The Meeting Time of Multiple Random Walks*, arXiv:1806.08843 (2018), https://arxiv.org/abs/1806.08843.
5. Y. Sakumoto and H. Ohsaki, *Graph Degree Heterogeneity Facilitates Random Walker Meetings*, arXiv:2005.11161 (2020), https://arxiv.org/abs/2005.11161.
6. D. Coppersmith, P. Tetali, and P. Winkler, *Collisions Among Random Walks on a Graph*, SIAM J. Discrete Math. 6 (1993), 363–374, https://doi.org/10.1137/0406029.
