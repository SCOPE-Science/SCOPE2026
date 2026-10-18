# Exact Crank–Nicolson positivity threshold on complete bipartite Markov graphs
## Finding
For the unit-edge-rate continuous-time random walk on the complete bipartite graph \(K_{p,q}\), let \(1\le p\le q\), \(n=p+q\), and let \(L\) be its combinatorial Laplacian. One Crank–Nicolson step for \(u'=-Lu\) is
\[
C_h=(I+\tfrac h2L)^{-1}(I-\tfrac h2L),\qquad h\ge0.
\]
The matrix \(C_h\) has row sums one for every \(h\ge0\). For \(p=q=1\), it is entrywise nonnegative for every finite \(h\). For \(n>2\), it is entrywise nonnegative exactly for
\[
0\le h\le h_*(p,q),\qquad
h_*(p,q)=\frac{p+\sqrt{p^2+4q(n-2)}}{q(n-2)}.
\]
At \(h=h_*(p,q)\), the diagonal entries on the \(p\)-vertex part are zero; for larger \(h\) those entries are negative. Thus the smaller part, whose vertices have degree \(q\), is the first location of positivity loss.

A graph-independent reduction is also valid. For every connected undirected graph Laplacian \(L\), set
\[
R_h=(I+\tfrac h2L)^{-1}.
\]
Because \(C_h=2R_h-I\) and \(R_h\) has positive off-diagonal entries, \(C_h\ge0\) entrywise if and only if \((R_h)_{ii}\ge1/2\) for every vertex \(i\).

## Assumptions and scope
The graph is finite, simple, connected, and unweighted; each edge carries jump rate one. The claim concerns the one-step Crank–Nicolson transition matrix itself, not a filtered or restarted variant. The complete-bipartite threshold is proved for every pair of integers \(1\le p\le q\). The graph-independent criterion uses only connectedness and symmetry of the graph Laplacian.

The rate normalization matters: multiplying all edge rates by \(\lambda>0\) replaces \(h\) by \(\lambda h\). No claim is made here for directed generators, weighted nonsymmetric chains, nonlinear positivity, or higher Padé maps.

## Proof
Write \(s=h/2\) and \(R=(I+sL)^{-1}\). Since \(I+sL\) is a nonsingular irreducible \(M\)-matrix for \(s>0\), \(R\) is entrywise positive. Also \(L\mathbf1=0\), hence \(R\mathbf1=\mathbf1\). Therefore
\[
C_h=(I+sL)^{-1}(I-sL)=2R-I
\]
has row sums one, and every off-diagonal entry of \(C_h\) is positive. Consequently, \(C_h\ge0\) is equivalent to \(R_{ii}\ge1/2\) for all \(i\).

For \(K_{p,q}\), the Laplacian spectrum is \(0\), \(q\) with multiplicity \(p-1\), \(p\) with multiplicity \(q-1\), and \(n=p+q\) with multiplicity one. The corresponding orthogonal spectral projectors give two diagonal resolvent values. On a vertex in the \(p\)-part,
\[
r_p(s)=\frac1n+\frac{p-1}{p(1+qs)}+\frac q{pn(1+ns)}.
\]
On a vertex in the \(q\)-part,
\[
r_q(s)=\frac1n+\frac{q-1}{q(1+ps)}+\frac p{qn(1+ns)}.
\]
Their difference factors as
\[
r_p(s)-r_q(s)=
\frac{s(p-q)(1+(n-1)s)}{(1+ps)(1+qs)(1+ns)}.
\]
Thus \(p\le q\) implies \(r_p(s)\le r_q(s)\), so the \(p\)-part controls positivity. A second exact simplification is
\[
r_p(s)-\frac12=
\frac{1+ps-q(n-2)s^2}{2(1+qs)(1+ns)}.
\]
If \(n=2\), then \(p=q=1\) and this quantity is positive for every finite \(s\). If \(n>2\), the numerator is a concave quadratic with one positive root,
\[
s_*=rac{p+\sqrt{p^2+4q(n-2)}}{2q(n-2)}.
\]
Hence \(C_h\ge0\) exactly for \(0\le s\le s_*\), equivalently \(0\le h\le2s_*=h_*(p,q)\).

For comparison with the general absolute-monotonicity guarantee, forward Euler on this generator is nonnegative only for \(h\le1/q\), because \(q\) is the maximum degree. The Crank–Nicolson absolute-monotonicity radius is \(2\), so the generic guarantee is \(h\le2/q\). The exact biclique threshold is strictly larger when \(n>2\):
\[
p^2+4q(n-2)-\bigl(2(n-2)-p\bigr)^2=8(n-2)>0,
\]
which implies \(h_*(p,q)>2/q\). If \(p/q\) approaches a positive constant as \(q\to\infty\), then \(h_*(p,q)=2/q+O(q^{-2})\).

## Verification
The accompanying `verify.py` reconstructs \(K_{p,q}\) Laplacians with exact rational arithmetic, inverts \(I+sL\) by rational Gauss–Jordan elimination, and checks the two diagonal formulas, their factorizations, row stochasticity, and strict off-diagonal positivity for a grid of exact rational test values with \(1\le p\le5\) and \(p\le q\le6\). These finite checks are supplementary: the all-\(p,q\) statement is proved symbolically above.

As an exact witness beyond threshold, take \(K_{2,3}\) and \(h=1\). The theorem gives
\[
h_*(2,3)=\frac{2+2\sqrt{10}}9<1.
\]
Direct exact inversion yields Crank–Nicolson diagonal entries
\[
-\frac1{35},\ -\frac1{35},\ \frac17,\ \frac17,\ \frac17,
\]
so the two vertices in the smaller part are already negative while every row still sums to one.

## Relationship to prior work
Bonaventura and Della Rocca analyze monotonicity and positivity of time integrators through absolute monotonicity and record the Crank–Nicolson radius as \(2\). Their framework therefore supplies the generic \(2/q\) sufficient bound after the forward-Euler positivity scale \(1/q\) is inserted, but it does not give the graph-dependent resolvent-diagonal criterion or the exact \(K_{p,q}\) threshold above.

The closest published semantic-index records found in the overlap search concern backward-Euler-filtered Crank–Nicolson positivity on one-dimensional lattices and a positivity barrier for a different \([2/2]\) Padé map. Neither statement implies the raw Crank–Nicolson complete-bipartite threshold proved here. The present result is instead a topology-resolved refinement of the general conditional-positivity picture.

## Limitations
The proof exploits symmetry of undirected graph Laplacians and the four-eigenspace decomposition of \(K_{p,q}\). It does not classify arbitrary graphs by a closed-form timestep threshold; for a general graph, the exact criterion remains the diagonal-resolvent condition \((I+\tfrac h2L)^{-1}_{ii}\ge1/2\). The literature search did not establish that no older graph-specific calculation exists under different terminology, so that remains a residual originality risk.

## References
1. L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, MOX Report 56/2015, 14 October 2015, arXiv:1510.04303. The report lists AMS classifications 65L05, 65L06, 65L20, 65M20 and states that Crank–Nicolson has absolute-monotonicity radius \(2\).
2. published-finding corpus record `2026/9/20/SCOPE-backward-euler-filtered-cn-lattice-positivity--1f6f56bd0eac`, *Unconditional lattice positivity from backward-Euler-filtered Crank-Nicolson*.
3. published-finding corpus record `2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab`, *Eight-state barrier for Markov positivity of the [2/2] Padé map*.
