# A six-step hitting-time census for Boolean dynamics on mixed directed cycle bouquets

## Finding

For every pair of integers \(m,k\ge1\), construct a directed graph \(D_{m,k}\) by identifying one distinguished hub vertex in \(m\) directed two-cycles and \(k\) directed three-cycles, all otherwise vertex-disjoint. Its \(n=1+m+2k\) vertices are individually labelled. Apply the synchronous *conjunctive Boolean rule* \(F\): each vertex replaces its binary state with the AND of the previous states of all its in-neighbors. Let \(\mathbf0\) and \(\mathbf1\) be the constant configurations, and let \(\tau(x)=\min\{t\ge0:F^t(x)=\mathbf0\}\), with \(\tau=\infty\) if no such update occurs.

Every configuration except \(\mathbf1\) reaches \(\mathbf0\), the only other fixed point, by update six. The exact numbers \(N_t=\#\{x:\tau(x)=t\}\) are

\[
\begin{aligned}
N_0&=1,\\
N_1&=2^{m+k}-2,\\
N_2=N_3&=(2^{m+k}-1)(2^k-1),\\
N_4&=2^k,\\
N_5&=2^{m+k}-1,\\
N_6&=2^k-1,\\
N_\infty&=1.
\end{aligned}
\]

All other \(N_t\) vanish. In particular the sixth update is necessary for exactly \(2^k-1\) labelled starting states: the hub and every two-cycle vertex and every final vertex of a three-cycle initially equal one, while at least one first vertex of a three-cycle equals zero. For a uniformly chosen binary initial configuration, as \(k\to\infty\) with any \(m\ge1\), the hitting-time distribution converges to equal mass \(1/2\) on updates two and three and zero mass elsewhere.

## Assumptions and scope

Write the common hub as \(r\), the vertices of the two-cycles as \(a_i\) for \(1\le i\le m\), and the private vertices of the three-cycles as \(b_j,c_j\) for \(1\le j\le k\). The directed edges are exactly \(r\to a_i\to r\) and \(r\to b_j\to c_j\to r\). The global update is simultaneous, not a sequential sweep. Every vertex has positive indegree; all counts are for the labelled state space of size \(2^{1+m+2k}\). Both kinds of petals must be present. The all-one state does not reach zero, and is recorded separately as \(N_\infty\).

## Proof

**1. Complementary OR process.** Set \(y_v(t)=1-x_v(t)\). By De Morgan's law, the complementary dynamics uses OR over in-neighbors, with precisely the same temporal first-hit counts after exchanging \(\mathbf0\) and \(\mathbf1\). Let \(R(t)=y_r(t)\) and similarly \(A_i(t),B_j(t),C_j(t)\). The defining edges give, for all \(t\ge0\),

\[
\begin{aligned}
R(t+1)&=\bigvee_i A_i(t)\ \vee\ \bigvee_j C_j(t),\\
A_i(t+1)&=R(t),\qquad B_j(t+1)=R(t),\\
C_j(t+1)&=B_j(t).
\end{aligned}
\]

Introduce the three disjoint initial-data summaries
\[
r_0=R(0),\qquad u=\bigvee_i A_i(0)\vee\bigvee_j C_j(0),\qquad v=\bigvee_j B_j(0).
\]
Then direct substitution yields
\[
R(0)=r_0,\quad R(1)=u,\quad R(2)=r_0\vee v,\quad R(3)=r_0\vee u,
\]
and \(R(t)=r_0\vee u\vee v\) for every \(t\ge4\), because for \(t\ge3\), \(R(t)=R(t-2)\vee R(t-3)\). For every \(t\ge2\), all \(a_i,b_j\) carry \(R(t-1)\) and all \(c_j\) carry \(R(t-2)\). Thus at those times the entire complementary configuration is one precisely when the three consecutive hub values \(R(t),R(t-1),R(t-2)\) are all one.

**2. Complete Boolean first-hit test.** The conditions for full occupation of the complementary process at each time are therefore:

| Update \(t\) | Necessary and sufficient condition for \(y(t)=\mathbf1\) |
|---|---|
| \(0\) | Every initial complementary bit equals one |
| \(1\) | \(r_0=1\), \(u=1\), and every \(B_j(0)=1\) |
| \(2\) | \(r_0=1\) and \(u=1\) |
| \(3\) | \(u=1\) and \((r_0=1\text{ or }v=1)\) |
| \(4\) | \(r_0=1\) or \((u=v=1)\) |
| \(5\) | \(r_0=1\) or \(u=1\) |
| \(6\) | \(r_0=1\) or \(u=1\) or \(v=1\) |

This accounts for all coordinates at time one as well as the recurrence at later times. Moreover, once the complementary state is all one it stays there, since every vertex has an in-neighbor. Consequently the conditions are nested and directly count the cumulative hitting populations \(H_t=\#\{x:\tau(x)\le t\}\).

**3. Exact combinatorial enumeration.** There are \(m+k\) initial bits contributing to \(u\), and independently \(k\) initial bits contributing to \(v\). Hence \(\#\{u=1\}=2^{m+k}-1\), \(\#\{v=1\}=2^k-1\), and each has one all-zero assignment. Counting the seven conditions yields

\[
\begin{aligned}
H_0&=1,\\
H_1&=2^{m+k}-1,\\
H_2&=(2^{m+k}-1)2^k,\\
H_3&=(2^{m+k}-1)(2^{k+1}-1),\\
H_4&=2^{m+2k}+(2^{m+k}-1)(2^k-1),\\
H_5&=2^{m+2k}+(2^{m+k}-1)2^k,\\
H_6&=2^{1+m+2k}-1.
\end{aligned}
\]

Taking \(H_t-H_{t-1}\) for \(t\ge1\), with \(N_0=H_0\), gives the announced census. The unique state excluded from \(H_6\) is \(y(0)=\mathbf0\), equivalently \(x(0)=\mathbf1\), which remains fixed. The other fixed state \(x=\mathbf0\) is included in \(N_0\). As \(N_6=2^k-1>0\), six steps are a sharp global bound. The time-six characterization is exactly \(r_0=u=0\) and \(v=1\) in the complementary variables, translating to the initial-state statement above.

**4. Asymptotic first-hit law.** Divide the census by \(2^{1+m+2k}\). For \(k\to\infty\) and any sequence \(m\ge1\),
\[
\frac{N_2}{2^{1+m+2k}}=\frac{N_3}{2^{1+m+2k}}=\frac12(1-2^{-(m+k)})(1-2^{-k})\longrightarrow\frac12.
\]
Every other finite or infinite time has asymptotically zero probability by the displayed formulas.

## Verification

The included standalone program `verify_rose.py` performs a direct synchronous AND update on each labelled graph, classifying all \(2^{1+m+2k}\) starting configurations for 33 parameter pairs with \(m,k\ge1\) and \(1+m+2k\le16\), totaling 299,696 checked configurations. It separately computes exact time-\(t\) in-neighbor predecessor sets by directed-walk propagation and counts occupation by a second method for the smaller cases; all these counts agree with the formulas. Big-integer sum identities were also checked for large parameter choices. Execute `python verify_rose.py` using Python 3 with no external dependencies. The recorded successful output is in `verification_output.txt`. These finite checks corroborate but do not replace the all-parameter proof above.

## Relationship to prior work

Jarrah, Laubenbacher and Veliz-Cuba established the general conjugacy of conjunctive and disjunctive Boolean networks, determined recurrent periods from strongly connected dependency graphs, and related maximum transient height to graph exponents. Their 2008 framework implies that a strongly connected graph with directed cycle lengths of gcd one has only the constant fixed points. It does not directly supply the full labelled first-hitting-time distribution above. Gao, Chen and Başar (2016) analyzed recurrent necklaces and one-coordinate perturbation transitions; their specialized term *rose* requires all constituent cycles to have equal length, unlike this mixed two/three-cycle graph. The present calculation concerns arbitrary initial states, not merely perturbations of recurrent states.

## Limitations

The formula requires both directed two-cycles and directed three-cycles sharing a single hub, with no other edges. It is not asserted for undirected flowers, longer petals, missing petal types, arbitrary strongly connected digraphs, or asynchronous updating. The generic fixed-point and period conclusions are established prior theory and are not claimed as new. The mathematical proof and accompanying code have not been independently validated; historical unindexed equivalents of the specific temporal census cannot be ruled out.

## References

- A. S. Jarrah, R. Laubenbacher, A. Veliz-Cuba, *The Dynamics of Conjunctive and Disjunctive Boolean Networks*, first posted 2008-05-02, https://arxiv.org/abs/0805.0275 .
- Z. Gao, X. Chen, T. Başar, *Stability Structures of Conjunctive Boolean Networks*, first posted 2016-03-14, https://arxiv.org/abs/1603.04415 .
- Y. Hu, P. Yuan, X. Chen, *The Generalized Exponent Sets of Primitive, Minimally Strong Digraphs (I)*, Ars Combinatoria 82 (2007), 97–124, https://combinatorialpress.com/ars-articles/volume-082-ars-articles/the-generalized-exponent-sets-of-primitive-minimally-strong-digraphs-i/ .
