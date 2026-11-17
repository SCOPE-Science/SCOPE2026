# Exact RK4 positivity and spectral-stability separation on regular bipartite networks

## Finding
Let \(G\) be a finite, connected, simple, undirected, \(d\)-regular bipartite graph, with integer \(d\geq1\), adjacency matrix \(A\), combinatorial Laplacian \(L=dI-A\), and classical four-stage Runge–Kutta diffusion end-step
\[
T_G(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24},\qquad h\geq0.
\]
Let \(\rho\) be the unique positive root of
\[
\rho^3-2\rho^2+3\rho-3=0,\qquad \rho=1.392646781702\ldots.
\]
Then the exact nonnegative-matrix and spectral-stability ranges are:

* For every such \(G\), \(\|T_G(h)\|_2\leq1\) **if and only if** \(0\leq dh\leq\rho\).
* If \(G\cong K_{d,d}\), \(T_G(h)\) is entrywise nonnegative **if and only if** \(0\leq dh\leq\rho\).
* If \(G\not\cong K_{d,d}\), \(T_G(h)\) is entrywise nonnegative **if and only if** \(0\leq dh\leq1\).

Thus the complete bipartite graphs are exactly the finite connected regular bipartite graphs for which the entire RK4 spectral-stability interval is positivity preserving. For every other graph in this family, the strict interval \(1<dh\leq\rho\) is spectrally stable but not positivity preserving.

The noncomplete-graph statement and the spectral-stability statement also hold for any finite connected undirected bipartite network with strictly positive symmetric weights on its edges and a common weighted degree \(\delta>0\), after replacing \(d\) by \(\delta\). If the support is complete bipartite and all edge weights are equal, the complete-bipartite clause holds with the same replacement. No classification is asserted for nonuniform positive weights on complete bipartite support.

## Assumptions and scope
A matrix is *entrywise nonnegative* if every entry is at least zero. This ensures that \(T_G(h)z\geq0\) whenever the vector \(z\geq0\), and, since \(L\mathbf1=0\), it then makes \(T_G(h)\) a row-stochastic matrix. Here *spectral stability* means the symmetric end-step satisfies \(\|T_G(h)\|_2\leq1\), including the conserved constant mode. The result concerns the final RK4 step for the autonomous linear heat/consensus equation \(z'=-Lz\), not all internal RK stages, nonlinear systems, or error control.

In the weighted extension, \(A_{ij}=A_{ji}>0\) precisely on support edges, \(A_{ii}=0\), and \(\sum_jA_{ij}=\delta\) for every \(i\). Connectedness and bipartiteness refer to this positive-weight support. No upper bound on graph size is imposed.

## Proof
Set \(q=dh\) and \(P=A/d\). Then \(P\) is symmetric, nonnegative and row stochastic, and \(L=d(I-P)\). For \(f(t)=1-t+t^2/2-t^3/6+t^4/24\),
\[
T_G(h)=f(q(I-P))=\sum_{j=0}^{4}c_j(q)P^j,
\]
where direct binomial expansion gives
\[
\begin{aligned}
c_0(q)&=f(q),\\
c_1(q)&=q(1-q+q^2/2-q^3/6),\\
c_2(q)&=\tfrac{q^2}{2}(1-q+q^2/2),\\
c_3(q)&=\tfrac{q^3}{6}(1-q),\\
c_4(q)&=q^4/24.
\end{aligned}
\]
Every coefficient is nonnegative for \(0\leq q\leq1\), and \(\sum_jc_j(q)=1\); therefore \(T_G(h)\) is a convex combination of nonnegative stochastic matrix powers on this interval.

Suppose the graph is not complete bipartite. The two bipartition classes have equal cardinality because every vertex has degree \(d>0\). Some opposite-class pair is nonadjacent; in a connected graph this produces a pair \(u,v\) at graph distance exactly three (take the first three edges of a shortest odd path if needed). Thus \((P^j)_{uv}=0\) for \(j=0,1,2\), while \((P^3)_{uv}>0\). Bipartiteness rules out any even-length walk between these opposite-class vertices, hence \((P^4)_{uv}=0\). Consequently the **exact**, rather than asymptotic, matrix-entry identity is
\[
(T_G(h))_{uv}=\frac{q^3(1-q)}6(P^3)_{uv}
=\frac{h^3(1-dh)}6(A^3)_{uv}.
\]
It is strictly negative at every \(q>1\), proving necessity for all noncomplete connected regular bipartite graphs. This proof uses only positive edge weights, a constant positive weighted degree, and bipartiteness; the stated weighted extension follows with \(\delta\) in place of \(d\).

Now suppose \(G=K_{d,d}\). The spectrum of \(L\) is \(0\), \(d\), and \(2d\), with multiplicities \(1\), \(2d-2\), and \(1\). Let \(a=f(q)\), \(b=f(2q)\), and let \(J\) be the all-ones matrix. With \(v\) equal to \(+1\) on one part and \(-1\) on the other,
\[
T_G(h)=aI+\frac{1-a}{2d}J+\frac{b-a}{2d}vv^\top.
\]
Its entries between opposite parts equal \((1-b)/(2d)\), its distinct same-part entries equal \((1+b-2a)/(2d)\), and its diagonal entries equal \(a+(1+b-2a)/(2d)\). Exact polynomial identities yield
\[
1+f(2q)-2f(q)=\frac{q^2}{12}(7q^2-12q+12)\geq0,
\]
\[
1-f(2q)=-\frac{2q}{3}(q^3-2q^2+3q-3).
\]
The first quadratic is strictly positive for every real \(q\); also
\[
24f(q)=q^2(q-2)^2+8(q^2-3q+3)>0
\]
for all real \(q\), since \(q^2-3q+3>0\). The cubic \(q^3-2q^2+3q-3\) is strictly increasing because its derivative \(3q^2-4q+3\) is strictly positive, and it has exactly one positive root \(\rho\). Therefore all entries are nonnegative precisely when \(0\leq q\leq\rho\). The same spectral projector argument applies to uniform positive edge weight after normalizing the common weighted degree.

Finally, symmetric stochasticity of \(P\) gives \(\sigma(P)\subseteq[-1,1]\); bipartiteness gives the eigenvalue \(-1\) with the alternating sign eigenvector. Thus \(\sigma(L)\subseteq[0,2d]\) and \(2d\in\sigma(L)\). The polynomial \(f(t)>0\) on \(t\geq0\), and
\[
f(t)-1=\frac{t}{24}(t^3-4t^2+12t-24).
\]
The cubic in parentheses is strictly increasing on the real line because \(3t^2-8t+12>0\); its unique positive root is \(2\rho\). Hence \(0<f(t)\leq1\) exactly for \(0\leq t\leq2\rho\). For the symmetric matrix \(T_G(h)\), the spectral norm is the maximum of \(|f(h\lambda)|\) over eigenvalues \(\lambda\) of \(L\). Therefore \(\|T_G(h)\|_2\leq1\) precisely when \(2dh\leq2\rho\). The same reasoning uses the weighted degree \(\delta\) in the weighted case. This completes the proof.

## Verification
The included standalone `verify.py` uses exact fractions and polynomial arithmetic, with no nonstandard packages. It checks the polynomial factorizations, nonnegative walk coefficients at representative normalized steps, stochasticity, and independent matrix-polynomial evaluations on complete bipartite graphs, alternating-weight cycles, and complete bipartite graphs with a perfect matching removed. Reproduction: `python3 verify.py`. The successful recorded replay returned `VERIFY_OK: 160 exact rational and polynomial checks`.

As a concrete exact witness, on the six-cycle \(C_6\) of degree \(2\), the step \(h=3/5\) satisfies \(dh=6/5<\rho\), so RK4 is spectrally stable, but its antipodal entry is \((T_{C_6}(3/5))_{0,3}=-9/625\).

These finite checks are supplementary. The all-graph result follows from the explicit walk coefficients, parity argument, complete-bipartite projector calculation, and spectral bounds in the proof. The tests do not certify novelty or replace any universal argument.

## Relationship to prior work
The theory of absolute monotonicity and linear-problem positivity of stability functions predates this result, notably Kraaijevanger (1986) and Lóczi–Ketcheson (2013). In particular, positivity for all stochastic matrices under a suitable forward-Euler restriction is classical; it is not claimed as novel. Gottlieb–Grant–Higgs (2014) distinguish method-level strong-stability preservation, which classical four-stage fourth-order RK lacks, from linear stability-function behavior. Blanes–Iserles–Macnamara (2021) explain the broader high-order unconditional-positivity barrier for standard time integrators. These facts are compatible with, but do not by themselves provide, the **graph-by-graph** dichotomy: every noncomplete regular bipartite graph has the sharp endpoint \(dh=1\), whereas every complete bipartite graph reaches the larger spectral endpoint \(dh=\rho\). The exact distance-three/parity witness and classification are the asserted contribution.

## Limitations
This is a statement about finite symmetric graph diffusion under the final classical RK4 update. It does not establish positivity of all intermediate RK4 stages for arbitrary initial data or extend the complete-support formula to nonuniformly weighted complete bipartite networks. The classification does not assert novelty over every specialist publication; original specialist sources may contain equivalent structural criteria. Numerical tests check examples, not mathematical universality. No independent external mathematical validation is claimed.

## References
1. J. F. B. M. Kraaijevanger, *Absolute monotonicity of polynomials occurring in the numerical solution of initial value problems*, Numerische Mathematik **48** (1986), 303–322. DOI: https://doi.org/10.1007/BF01389477.
2. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651, first submitted 2013-03-26. https://arxiv.org/abs/1303.6651.
3. S. Gottlieb, Z. J. Grant, and D. Higgs, *Optimal Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order and optimal Nonlinear Order*, arXiv:1403.6519, first submitted 2014-03-25. https://arxiv.org/abs/1403.6519.
4. S. Blanes, A. Iserles, and S. Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242, first submitted 2021-02-16. https://arxiv.org/abs/2102.08242.
