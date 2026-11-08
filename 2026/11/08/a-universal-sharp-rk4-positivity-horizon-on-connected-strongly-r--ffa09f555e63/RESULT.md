# A universal sharp RK4 positivity horizon on connected strongly regular graphs

## Finding
Let \(G\) be any finite, simple, connected, noncomplete strongly regular graph with parameters \((v,k,\lambda,\mu)\). Let \(A\) be its unweighted adjacency matrix and \(L=kI-A\). Consider the classical fourth-order Runge–Kutta endpoint heat step
\[
T(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24},\qquad h\ge0.
\]
Set
\[
a=2k-\lambda,\quad b=(k-\lambda-1)(k-\mu),\quad
F(h)=1-\frac{a}{2}h+\frac{a^2-b}{6}h^2-\frac{a^3-b(2a+\mu)}{24}h^3.
\]
Then \(F\) is strictly decreasing on the entire nonnegative axis, with exactly one positive zero \(\tau\), and
\[
\boxed{T(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le\tau.}
\]
For every \(h>0\), all diagonal and all **nonadjacent** entries of \(T(h)\) are strictly positive. Each adjacent entry is exactly \(hF(h)\), so after \(\tau\) all edge entries become negative permanently: there is no later positivity interval. The threshold depends only on the parameter triple \((k,\lambda,\mu)\), not on the number of vertices or the isomorphism type of the graph. Every such graph also satisfies the strict forward-Euler improvement \(\tau>1/k\).

## Assumptions and scope
A strongly regular graph here is a simple \(k\)-regular graph on \(v\) vertices such that adjacent distinct vertices have exactly \(\lambda\) common neighbors, whereas nonadjacent distinct vertices have exactly \(\mu\) common neighbors. The graph is assumed connected and noncomplete, hence
\[
1\le\mu\le k,\qquad 0\le\lambda\le k-2,\qquad k\ge2.
\]
The conclusion concerns entrywise positivity of the completed RK4 linear update for **arbitrary nonnegative initial vectors**. It does not assert stagewise nonnegativity, positivity for directed or weighted graphs, or positivity of other Runge–Kutta schemes. All quantifiers range over every finite graph satisfying these assumptions, every pair of its vertices, and every real timestep \(h\ge0\).

## Proof
**1. Three entry classes.** Write \(J\) for the all-ones matrix. The strongly regular identity is
\[
A^2=(k-\mu)I+(\lambda-\mu)A+\mu J,\qquad AJ=kJ.
\]
It follows by multiplication that every power of \(L=kI-A\) has entries constant on the diagonal, on edges, and on nonedges. For an edge \(ij\), the relevant values for \(L,L^2,L^3,L^4\) are respectively
\[
-1,\quad -a,\quad -(a^2-b),\quad -(a^3-b(2a+\mu)).
\]
Consequently the RK4 entry on every edge is exactly \(hF(h)\).

For a nonedge \(ij\), put \(s=k-\lambda+\mu>0\) and
\[
C=3ks+(k-s)^2+(k-\mu)>0.
\]
The four entries of \(L,L^2,L^3,L^4\), respectively, are \(0,\mu,\mu(k+s),\mu C\), yielding
\[
T(h)_{ij}=\frac{\mu h^2}{24}\left[12-4(k+s)h+Ch^2\right].
\]
The bracket's quadratic discriminant equals
\[
16\big[(k+s)^2-3C\big]
=-16\big[2k^2+ks+2s^2+3(k-\mu)\big]<0.
\]
It has positive leading coefficient and is therefore strictly positive for every real \(h\). This proves the nonedge statement.

**2. All diagonal entries remain positive.** The graph Laplacian \(L\) is real symmetric positive semidefinite. For every \(x\ge0\), the scalar fourth-order Taylor polynomial \(R_4(-x)=\sum_{j=0}^4(-x)^j/j!\) exceeds \(e^{-x}>0\), by the signed fifth-order Taylor remainder (with equality at \(x=0\)). Thus \(R_4(-hL)\) is positive definite and all its diagonal entries are strictly positive.

**3. A unique edge sign change.** Let \(p=k-\lambda-1\ge1\) and \(q=k-\mu\ge0\). Then \(b=pq\), \(a=k+p+1\), so
\[
0\le t:=b/a^2<\tfrac14,\qquad 0<u:=\mu/a<1.
\]
Indeed \(pq\le pk\le(p+k)^2/4<a^2/4\). Define \(m_3=a^2-b=a^2(1-t)>0\) and \(m_4=a^3-b(2a+\mu)=a^3[1-(2+u)t]>0\). The derivative is the concave quadratic
\[
F'(h)=-\frac a2+\frac{m_3}{3}h-\frac{m_4}{8}h^2.
\]
Its discriminant is strictly negative because
\[
9am_4-4m_3^2
=a^4\left[5-(10+9u)t-4t^2\right]>0.
\]
For the final inequality, the expression inside brackets is decreasing in \(t\ge0\) and \(u\ge0\), and at the excluded endpoint \((t,u)=(1/4,1)\) it equals zero. Since \(F'(0)=-a/2<0\), this proves \(F'<0\) everywhere. Since \(F(0)=1\) and its cubic leading coefficient is strictly negative, \(F\) has precisely one zero \(\tau>0\), and its sign is positive below and negative above \(\tau\). Steps 1 and 2 complete the equivalence.

**4. Strict gain over forward Euler.** Let \(P=A/k\), a stochastic matrix with positive edge entries and positive two-step entries across nonedges. The exact expansion
\[
R_4(P-I)=\frac38I+\frac13P+\frac14P^2+\frac1{24}P^4
\]
has nonnegative coefficients and every entry is strictly positive: the identity term covers the diagonal, \(P\) covers edges, and \(P^2\) covers nonedges because \(\mu>0\). Hence \(T(1/k)\) is strictly positive; in particular \(F(1/k)>0\). As \(F\) decreases strictly, \(\tau>1/k\).

## Verification
The standalone `verification.py` runs without third-party packages. It independently multiplies the adjacency algebra symbolically over the integer polynomial ring in \((k,\lambda,\mu)\), confirms the four class coefficients and the quadratic discriminant identity, and compares the polynomial predictions with complete exact-rational RK4 matrices on 12 strongly regular graphs: the Petersen graph, two triangular graphs, two rook graphs, the Shrikhande graph, two complete bipartite graphs, and Paley graphs of orders \(5,13,17,29\). It verifies all \(9{,}768\) sampled matrix entries and stochastic row sums. The infinitely many possible graph parameters and all real timesteps are settled by the proof above; the finite tests are secondary checks only. Reproduce with `python3 verification.py`.

## Relationship to prior work
Horváth, Song, and Terlaky (2014) provide a general first-positive-zero framework for polyhedral invariance of Taylor discretizations. That framework motivates checking coefficient polynomials, but does not give this three-parameter graph formula, prove the uniform strict positivity of every nonedge entry for all timesteps, or establish the global single-crossing property. Horváth (2005) analyzes strict Runge–Kutta positivity thresholds and invariant cones in general classes, without this strongly regular classification. Brouwer and Haemers give the standard strongly regular adjacency identity used here, rather than a positivity theorem. Special-case RK4 threshold analyses of regular bipartite graphs, triangular graphs (and their shared-parameter Chang graphs), and complete multipartite graphs concern narrower subfamilies; their stated conclusions do not imply the universal result for Petersen, Shrikhande, Paley, and other strongly regular graphs. The present result is a graph-specific sharpening of general polynomial threshold procedures, not a new general RK positivity theorem.

## Limitations
Only endpoint positivity for unweighted undirected connected noncomplete strongly regular graphs is claimed. No uniqueness of graph realizations or of a representation is needed; graphs sharing parameters share the threshold. No independent audit has been performed. A specialist publication beyond the inspected sources may contain a closely related formula, and no finite search proves publication priority.

## References
- Z. Horváth, Y. Song, and T. Terlaky, *Steplength Thresholds for Invariance Preserving of Discretization Methods of Dynamical Systems on a Polyhedron*, arXiv:1406.6755, first public version 26 June 2014. https://arxiv.org/abs/1406.6755
- Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics **53** (2005), 341–356; online 27 October 2004. https://doi.org/10.1016/j.apnum.2004.08.026
- A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, 2006 preprint, Chapter 9, on strongly regular graph adjacency algebras. https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf
- S. Gottlieb, C.-W. Shu, and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review **43** (2001), 89–112. https://doi.org/10.1137/S003614450036757X
