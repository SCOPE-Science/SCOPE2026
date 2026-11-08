# A universal twin-edge threshold for latent trust and recovered consensus

## Finding
Consider the synchronous adaptive-confidence Hegselmann–Krause dynamics of Li, Luo, and Porter. In a finite connected simple graph \(H\), choose nonadjacent vertices \(u,v\) with the same \(d\ge1\) neighbors, and add the *latent* edge \(uv\) to form the physical graph \(G\). All edges of \(G\) start with the same confidence bound \(c\). We construct a nonempty open set of initial opinion profiles for which all physical edges except \(uv\) are initially receptive, every agent eventually shares one limit opinion, and the eventual trust state of \(uv\) changes at the exact threshold

\[
\delta_c=\frac{1}{d+1}.
\]

For \(0\le\delta\le\delta_c\), the latent edge is never receptive and its confidence tends to zero; for \(\delta>\delta_c\), it becomes receptive at an explicitly computable time and remains receptive forever, with confidence tending to one. The cutoff depends only on the shared-neighbor degree \(d\), not on the size or remaining structure of \(H\). Thus even a pair whose opinions converge to agreement can permanently lose confidence in one another, and the distinction persists under small independent perturbations of every initial opinion.

## Assumptions and scope
Let \(H=(V,E_H)\) be any finite connected simple undirected graph, with nonadjacent distinct vertices \(u,v\) such that \(N_H(u)=N_H(v)=S\), \(|S|=d\ge1\). Put \(G=(V,E_H\cup\{uv\})\). At integer time \(t\), every vertex has an opinion \(x_i(t)\in[0,1]\), and every physical edge has confidence \(c_{ij}(t)\in[0,1]\). Its receptivity indicator is \(|x_i(t)-x_j(t)|<c_{ij}(t)\), with equality counted as *nonreceptive*. Each vertex updates synchronously by averaging its own opinion and those of its currently receptive neighbors. Simultaneously, each confidence changes by

\[
c_{ij}(t+1)=\begin{cases}
c_{ij}(t)+\gamma(1-c_{ij}(t)),&\text{if receptive},\\
\delta c_{ij}(t),&\text{otherwise}.
\end{cases}
\]

Fix any \(0<c<1\), \(0<\gamma\le1\), \(0\le\delta\le1\), and choose

\[
\frac c2<a<\min\{c,\tfrac12\},\qquad
0<\varepsilon<\min\left\{a-\frac c2,\frac{c-a}{2},\frac\gamma2,\frac12-a\right\}.
\]

Initially let \(c_{ij}(0)=c\) on every physical edge. Let \(m=1/2\) and let

\[
x_i(0)=m+a(\mathbf1_{i=u}-\mathbf1_{i=v})+\eta_i,
\qquad \max_i|\eta_i|\le\varepsilon.
\]

These inequalities guarantee the opinions lie in \([0,1]\), the edge \(uv\) is initially nonreceptive, and every edge of \(H\) is initially receptive. Write \(D=x_u(0)-x_v(0)>c\) and \(\rho=1/(d+1)\). The conclusions hold for *every* admissible perturbation vector \(\eta\), not just for the symmetric choice \(\eta=0\).

**Exact dichotomy.** If \(\delta\le\rho\), the effective graph equals \(H\) at all times; all opinions converge to a common limit; \(c_{uv}(t)\to0\); and every other confidence converges to one. If \(\delta>\rho\), the initially missing edge first becomes receptive at

\[
T=\min\big\{t\in\mathbb Z_{\ge0}:D\rho^t<c\delta^t\big\}
=\left\lfloor\frac{\log(D/c)}{\log((d+1)\delta)}\right\rfloor+1.
\]

All physical edges are receptive at every time from \(T\) onward, their confidence limits all equal one, and all opinions converge to a common limit. At fixed initial profile, the exact waiting time has the critical divergence

\[
T\sim\frac{\rho\log(D/c)}{\delta-\rho}\quad\text{as }\delta\downarrow\rho\text{ from above}.
\]

For \(\eta=0\), full opinion agreement occurs exactly after the update at time \(T\), i.e. at time \(T+1\). For the clique example \(G=K_n\), \(H=K_n\setminus\{uv\}\), the cutoff is \(1/(n-1)\), and even with admissible perturbations, finite exact agreement holds by time \(T+2\) whenever \(\delta>\rho\). The smallest example has three vertices, with \(H\) the path of length two and cutoff \(1/2\).

## Proof
**The inactive-edge phase.** Let \(P_H\) be the row-stochastic opinion-averaging matrix on \(H\) when every edge in \(E_H\) is receptive (each vertex averages itself and all its \(H\)-neighbors). Since \(u,v\) are nonadjacent twins, their averaging denominators both equal \(d+1\) and their shared neighbor contributions cancel, giving

\[
(P_H z)_u-(P_H z)_v=\rho(z_u-z_v)
\]

for every opinion vector \(z\). Also the antisymmetric vector \(e_u-e_v\) is an eigenvector with eigenvalue \(\rho\): the two endpoint coordinates scale by \(\rho\), while at every other vertex the two endpoint contributions either occur together and cancel or are both absent. Consequently, starting from the unperturbed initial profile, the preactivation trajectory is exactly \(m\mathbf1+a\rho^t(e_u-e_v)\). For an arbitrary admitted perturbation, \(\|P_H^t\eta\|_\infty\le\varepsilon\) by stochasticity.

Suppose the effective graph has equaled \(H\) through time \(t-1\). At time \(t\), every \(H\)-edge has opinion gap at most \(a\rho^t+2\varepsilon\le a+2\varepsilon<c\). Its confidence has only increased since time zero, and is at least \(c\). Thus *every* \(H\)-edge remains receptive, by induction up to and including the first possible activation of \(uv\). Throughout this phase,

\[
x_u(t)-x_v(t)=D\rho^t,\qquad c_{uv}(t)=c\delta^t.
\]

Since \(D>c\), the condition for first activation is the strict inequality \(D\rho^t<c\delta^t\). If \(\delta\le\rho\), this can never hold, including equality at the critical parameter. The effective graph is then \(H\) forever. The connected, self-looped stochastic matrix \(P_H\) is primitive, so its iterates converge to a consensus projection. Since \(\delta\le\rho<1\), \(c_{uv}(t)\to0\); since \(\gamma>0\) and the other edges are always receptive, their confidence limits are one.

**The restoration phase.** If \(\delta>\rho\), the ratio \((D/c)(\rho/\delta)^t\) decreases strictly to zero, proving the stated first-activation time, including its floor-plus-one convention at exact equality. At time \(T\), all edges of \(G\) are receptive. Let \(P_G\) be the averaging matrix on the full physical graph. Because the antisymmetric deviations at \(u,v\) cancel in each other's newly enlarged neighborhoods, and cancel at every common neighbor, \(P_G[m\mathbf1+a\rho^T(e_u-e_v)]=m\mathbf1\). Meanwhile applying the row-stochastic \(P_G\) to the perturbation has infinity norm at most \(\varepsilon\). Thus at \(T+1\) every opinion lies within \(\varepsilon\) of \(m\), and every edge gap is at most \(2\varepsilon\).

Every original \(H\)-edge still has confidence at least \(c\). The newly receptive edge has confidence

\[
c_{uv}(T+1)=c\delta^T+\gamma(1-c\delta^T)\ge\gamma.
\]

Our assumption \(2\varepsilon<\min\{c,\gamma\}\) makes every physical edge receptive at \(T+1\). Further updates with \(P_G\) preserve the interval \([m-\varepsilon,m+\varepsilon]\), while confidence on all receptive edges never decreases. Induction therefore proves the effective graph remains all of \(G\) forever. Because \(G\) is connected and its stochastic update has positive diagonal, \(P_G\) is primitive and opinions converge to consensus. Every edge confidence tends to one. With \(\eta=0\), the preceding cancellation gives exact consensus at \(T+1\); when \(G\) is complete, one additional full-graph averaging step gives exact consensus for every admitted \(\eta\).

Finally, \(\log((d+1)\delta)=\log(1+(\delta-\rho)/\rho)\sim(\delta-\rho)/\rho\). The bounded floor correction in the formula for \(T\) gives the stated critical divergence. This establishes every case and boundary.

## Verification
An accompanying dependency-free Python program, `verify.py`, independently iterates the actual synchronous confidence and opinion rules using exact rational arithmetic. It builds 140 connected twin-containing graphs of orders three through nine with varied degrees and additional edges, tests five forgetting-rate regimes on each graph, checks the antisymmetric recurrence and all edge-status predictions at each step, and exercises exact activation-time equality and a near-critical delayed activation case. It reports 56,706 exact-rational assertions passed. These finite calculations corroborate but do not prove the universal graph statement; the argument above is the proof.

Reproduce with `python verify.py` from the extracted file directory, using a standard Python 3 interpreter. The code uses only the standard library. A convenient concrete setting is \(c=3/5\), \(a=2/5\), \(\gamma=1/4\): for three agents, the critical forgetting factor is \(\delta_c=1/2\); at \(\delta=2/3\), the time-one receptive inequality is exactly at equality, so the first activation occurs at time two, not time one.

## Relationship to prior work
Li, Luo, and Porter introduce the precise adaptive-confidence HK rule (their equations (2.2)–(2.3)). Their Theorems 3.2 and 3.6 establish convergence properties for confidences and effective graphs, and their numerical work exhibits same-limit-opinion dyads that become unreceptive. They do not state a graph-local formula for the sharp forgetting threshold, a uniform open neighborhood of initial conditions retaining that phase split, or the exact first recovery time. Their baseline HK Theorem 3.7 is inapplicable to shrinking confidence bounds and in fact yields a different limit-edge criterion. The heterogeneous agent-activity DW model of Li and Porter and the fixed-confidence state-dependent networks of Etesami concern different update mechanisms.

## Limitations
This is a theorem for the *synchronous* dyadic adaptive-confidence rule, with an initially unreceptive edge joining nonadjacent twins of the connected effective graph and opinions in the stated open region. It does not assert the same critical threshold for arbitrary pairs, asynchronous pair selection, alternative confidence-update laws, or all possible initial opinion profiles. The exact time formula is an analytical formula; finite numerical experiments are not a proof for infinite families. The theorem gives neither empirical estimates of human confidence parameters nor an assessment of real social networks. Priority comparisons cannot exclude an unindexed equivalent argument.

## References
1. Grace J. Li, Jiajie Luo, Mason A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563, first submitted 2023-03-14; SIAM Journal on Applied Dynamical Systems 24 (2025), 994–1041, DOI:10.1137/23M1558951. https://arxiv.org/abs/2303.07563 ; author-hosted version: https://www.math.ucla.edu/~mason/papers/BCM-dynamic-April2025.pdf
2. Grace J. Li and Mason A. Porter, *Bounded-confidence model of opinion dynamics with heterogeneous node-activity levels*, Physical Review Research 5 (2023), 023179. https://doi.org/10.1103/PhysRevResearch.5.023179
3. S. Rasoul Etesami, *A Simple Framework for Stability Analysis of State-Dependent Networks of Heterogeneous Agents*, SIAM Journal on Control and Optimization 57 (2019), 1757–1782. https://doi.org/10.1137/18M1217681
