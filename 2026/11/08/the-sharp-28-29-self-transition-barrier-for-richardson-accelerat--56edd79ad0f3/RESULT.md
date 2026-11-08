# The sharp 28–29 self-transition barrier for Richardson-accelerated graph diffusion

## Finding

Let \(G\) be any connected undirected weighted graph with \(n\ge2\) vertices, positive conductances on its edges, and symmetric combinatorial Laplacian \(L\). For each \(h\ge0\), define the one-step matrix of backward-Euler Richardson extrapolation by

\[
T(h)=2(I+hL/2)^{-2}-(I+hL)^{-1}=R(hL),\qquad
R(z)=\frac{4+4z-z^2}{(1+z)(2+z)^2}.
\]

Let \(z_*\) be the **unique positive root** of \(z^3-10z^2-20z-8=0\), and let \(m_*=R(z_*)\) (numerically \(m_*\approx-0.036117337306513\)). Then the following statements form one sharp self-transition classification.

1. For every \(n\ge2\),

\[
\min_{G,h,i} [T(h)]_{ii}=\frac{1+(n-1)m_*}{n},
\]

where the minimum is over connected nonnegatively weighted undirected networks with \(n\) vertices, positive weights on their edges, \(h\ge0\), and vertices \(i\). Equality at a specified vertex \(i\) occurs **if and only if** \(i\) is adjacent to every other vertex with a single common positive conductance \(a\), and \(h=z_*/(na)\); edges among its neighbors can have arbitrary nonnegative conductances. At such a vertex the exact identity

\[
[T(h)]_{ii}=\frac{1+(n-1)R(nah)}{n}
\]

holds for every \(h\ge0\), regardless of those other edges.

2. All diagonal entries of \(T(h)\) are strictly positive, for **every** connected weighted undirected graph and **every finite** \(h\ge0\), if and only if \(2\le n\le28\). For each \(n\ge29\), already the equally weighted star \(K_{1,n-1}\) has a negative hub diagonal at \(h=12/(na)\), namely

\[
[T(12/(na))]_{ii}=\frac{660-23n}{637n}<0.
\]

For \(n=29\), this is exactly \(-7/18473\).

3. For any common-conductance universal vertex in a graph with \(n\ge29\), the hub diagonal is negative on **exactly one bounded positive timestep interval**, and positive outside its closure. In terms of \(z=nah\), that interval is \((z_-(n),z_+(n))\), where \(z_-(n)<12<z_+(n)\) are the two distinct positive roots of

\[
P_n(z)=z^3+(6-n)z^2+(4n+4)z+4n.
\]

The two endpoints are zero values of the self-transition, not negative ones.

## Assumptions and scope

The graph is finite, connected, undirected, with real positive edge conductances (zero is allowed only for absent edges). Its Laplacian is the **unnormalized** weighted matrix \(L_{ii}=\sum_{j\ne i}w_{ij}\), \(L_{ij}=-w_{ij}\) for distinct \(i,j\). Each one-step map acts on column states; all inverses exist for \(h\ge0\). The Richardson formula uses two backward-Euler half-steps and one backward-Euler full step, extrapolated as twice the former minus the latter. The assertion concerns **diagonal entries only**: it does not claim that all off-diagonal entries, and hence the full one-step matrix, are nonnegative. Time is finite and nonnegative. The graph may include arbitrary edges among the neighbors of a specified universal vertex.

## Proof

**Scalar extremum.** Write \(R(z)=N(z)/D(z)\), with \(N(z)=4+4z-z^2\), \(D(z)=(z+1)(z+2)^2>0\) on \(z\ge0\). Direct differentiation gives

\[
R'(z)=\frac{z^3-10z^2-20z-8}{(z+1)^2(z+2)^3}.
\]

The cubic in the numerator has exactly one positive root by Descartes' rule of signs and the intermediate value theorem: it is negative at zero and positive for large positive \(z\). Thus \(R\) strictly decreases to its unique global minimum \(m_*\) at \(z_*\) and strictly increases afterward toward \(0\) from below. An exact strict bound is

\[
R(z)+\frac1{27}=\frac{z(z-12)^2+2(z-7)^2+14}{27(z+1)(z+2)^2}>0\quad(z\ge0).
\]

On the other hand, \(R(12)=-23/637<-1/28\). Consequently

\[
-\frac1{27}<m_*\le-\frac{23}{637}<-\frac1{28}.
\]

**Universal diagonal bound.** Because \(L\) is connected and symmetric, it has an orthonormal eigenbasis \(v_0=\mathbf1/\sqrt n,v_1,\ldots,v_{n-1}\) with \(\lambda_0=0\) and \(\lambda_j>0\) for \(j\ge1\). As \(R(0)=1\), for every vertex \(i\)

\[
[T(h)]_{ii}=\frac1n+\sum_{j=1}^{n-1}R(h\lambda_j)|v_j(i)|^2
\ge\frac1n+m_*\sum_{j=1}^{n-1}|v_j(i)|^2
=\frac{1+(n-1)m_*}{n}.
\]

This bound is independent of all graph weights and all timesteps. For \(n\le28\), the strict inequality \(m_*>-1/27\) proves positivity (including \(n=28\)); the case \(h=0\) also gives \(T(0)=I\).

**Exact equality and local rigidity.** For \(h>0\), equality in the diagonal bound holds precisely when every positive spectral atom of \(e_i\) is mapped to the unique scalar minimizing point \(z_*\). Equivalently, \(u_i=e_i-\mathbf1/n\) belongs to the single eigenspace of eigenvalue \(\lambda=z_*/h\):

\[
Lu_i=\lambda u_i.
\]

Since \(L\mathbf1=0\), this is \(Le_i=\lambda(e_i-\mathbf1/n)\). Comparing the coordinates \(j\ne i\) forces \(w_{ij}=\lambda/n\) for **every** other vertex. Conversely, if these conductances all equal \(a>0\), then \(Le_i=na(e_i-\mathbf1/n)\), whatever the other edges. The two-dimensional spectral decomposition of \(e_i\) into \(\mathbf1/n\) and \(u_i\) gives the displayed exact diagonal formula, which attains the lower bound at \(h=z_*/(na)\). This also proves the extremal infimum is a minimum, realized even by a star.

**Sharp dimension and complete sign-band classification.** For a common-conductance universal vertex put \(z=nah\). Rational simplification gives

\[
[T(h)]_{ii}=\frac{1+(n-1)R(z)}{n}
=\frac{P_n(z)}{n(z+1)(z+2)^2},
\quad P_n(z)=z^3+(6-n)z^2+(4n+4)z+4n.
\]

At \(z=12\), the diagonal equals \((660-23n)/(637n)\), which is negative exactly for integer \(n\ge29\). For each such \(n\), the coefficients of \(P_n\) have the signs \(+,-,+,+\) when ordered by decreasing degree, so Descartes' rule gives **at most two** positive roots counted with multiplicity. Because \(P_n(0)=4n>0\), \(P_n(12)<0\), and \(P_n(z)\to+\infty\) as \(z\to\infty\), the intermediate value theorem gives distinct roots on either side of \(12\). There are exactly two; continuity and no other positive roots give the claimed single negative interval and recovery of positivity afterward.

## Verification

The standalone `verify.py` executes using Python 3 standard library only. It checks exact rational identities for the rational numerator, denominator, derivative and positive sum-of-squares bound; confirms \(R(12)=-23/637\); checks the star-hub spectral eigenvector identity; and reconstructs the matrix formula \(2(I+hL/2)^{-2}-(I+hL)^{-1}\) by exact Gaussian elimination for 21 small networks with arbitrary additional neighbor edges. The script also checks the first negative dimension and the exact 29-vertex witness. Output from the packaged script is `EXACT_VERIFICATION_OK 51 algebraic/matrix/threshold checks`. These finite computations and symbolic identity checks do not by themselves establish all dimensions; the preceding spectral and root-count arguments do.

## Relationship to prior work

Richardson extrapolation and its use on diffusion discretizations are established methods. Mona, Lagzi, and Havasi (2015) give the general extrapolation formula and numerical reaction–diffusion examples, including a full-step/two-half-step construction; their tested base method is forward Euler, not the backward-Euler graph-Laplacian rational map here. Earlier Zlatev–Faragó–Havasi (2010) and Faragó–Havasi–Zlatev (2010) work addresses stability of Richardson compositions and backward-Euler extrapolation, not the universal self-transition sign cutoff stated above in the accessible abstracts. A later public mathematical research record establishes the scalar extrapolated-backward-Euler sign reversal at \(2+2\sqrt2\); the present statement does not claim novelty for that scalar fact. It characterizes instead the sharp **network-wide diagonal bound, 28/29 dimension barrier, equality networks, and finite negative timestep interval**. Stability, a scalar negative value, or an example of graph negativity alone does not imply this extremal statement and rigidity classification.

## Limitations

This is a criterion for **diagonal** nonnegativity, not for full entrywise positivity or preservation of the entire nonnegative cone. It applies to connected symmetric combinatorial Laplacians with arbitrary positive edge conductances, not to directed chains, nonuniform stationary distributions, normalized Laplacians, or repeated active extrapolation steps. Some closely related stability literature was accessible only as abstracts, so publication-priority assessment remains qualified. The work has not received an independent mathematical audit. Values of \(m_*\) are numerical illustrations; rigorous cutoff claims use only exact rational inequalities.

## References

- T. Mona, I. Lagzi, and Á. Havasi, “Solving Reaction-Diffusion and Advection Problems with Richardson Extrapolation,” *Journal of Chemistry* **2015**, article 350362, first published April 1, 2015. DOI: https://doi.org/10.1155/2015/350362 . Open-access full text: https://real.mtak.hu/32451/1/Mona_Lagzi_Havasi_jchem_published.pdf .
- Z. Zlatev, I. Faragó, and Á. Havasi, “Stability of the Richardson Extrapolation applied together with the \(\theta\)-method,” *Journal of Computational and Applied Mathematics* **235** (2010), 507–517. https://doi.org/10.1016/j.cam.2010.05.052 .
- I. Faragó, Á. Havasi, and Z. Zlatev, “Efficient implementation of stable Richardson Extrapolation algorithms,” *Computers & Mathematics with Applications* **60** (2010), 2309–2325. https://doi.org/10.1016/j.camwa.2010.08.025 .
- “Richardson acceleration creates a sharp positivity barrier for backward Euler,” public mathematical research record (October 4, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-richardson-acceleration-creates-a-sharp-positivity-barrier-for-b--c9c2b9f6d7e1 . Its accessible summary establishes scalar, not network-diagonal, bounds.
