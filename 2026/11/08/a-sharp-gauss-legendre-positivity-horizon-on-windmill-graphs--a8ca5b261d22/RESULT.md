# A sharp Gauss–Legendre positivity horizon on windmill graphs

## Finding
For integers \(m\ge1\) and \(r\ge2\), form the unweighted windmill graph \(W_{m,r}=K_1\vee(mK_{r-1})\), consisting of \(m\) copies of \(K_r\) meeting at one apex. Let \(L\) be its combinatorial Laplacian. The completed two-stage, fourth-order Gauss–Legendre heat step is
\[
T_{m,r}(h)=F(hL),\qquad F(z)=\frac{z^2-6z+12}{z^2+6z+12},\qquad h\ge0.
\]
When \(m=1\) (a complete graph) or \(r=2\) (a star), \(T_{m,r}(h)\) is entrywise nonnegative for every \(h\ge0\) and strictly positive for \(h>0\). For \(m\ge2\) and \(r\ge3\), set \(k=r-1\), \(u=mk\),
\[
 A=u^2-u(k-1)-2k-1,\qquad B=u^2+3u+2r+3,
\]
\[
 P_{m,r}(h)=-rAh^4+6r(r+1)h^3+12Bh^2+72(u+2)h+144.
\]
There is exactly one positive root \(h_{m,r}\) of \(P_{m,r}\), and
\[
 T_{m,r}(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le h_{m,r}.
\]
Every entry is positive for \(0<h<h_{m,r}\). At \(h=h_{m,r}\), precisely the off-diagonal entries between two distinct non-apex vertices of the same clique vanish. After that threshold, exactly those entries are negative; all other entries remain positive. For each fixed \(r\ge3\), \(h_{m,r}\to\sqrt{12/r}\) as \(m\to\infty\).

## Assumptions and scope
The graph is simple and undirected; every existing edge has unit conductance. The state equation is \(\dot x=-Lx\), using the *combinatorial*, not normalized, Laplacian. The claim is about the completed end-step matrix, not internal Runge–Kutta stages. All \(h\) are real and nonnegative. Neither arbitrary unequal clique sizes nor heterogeneous conductances are claimed. Every denominator below is positive for \(h\ge0\).

## Proof
Write \(N=1+mk\) and \(D(z)=z^2+6z+12\). The scalar complement is \(g(z)=1-F(z)=12z/D(z)\). Since \(D(z)>0\) and the numerator of \(F(z)\) is \((z-3)^2+3\), the scalar \(F(z)\) is strictly positive on \([0,\infty)\).

The Laplacian has mutually orthogonal eigenspaces: constants at eigenvalue \(0\); differences of the \(m\) blade averages at eigenvalue \(1\), dimension \(m-1\); vectors of sum zero within each \(k\)-vertex blade at eigenvalue \(r\), dimension \(m(k-1)\); and the apex-against-all-leaves vector at eigenvalue \(N\), dimension one. To verify directly, a within-blade zero-sum vector has leaf Laplacian value \((k+1)x=rx\) and zero apex component, while the last vector with apex value \(-mk\) and every leaf value \(1\) has eigenvalue \(N\). Their dimensions total \(N\).

The normalized projectors for eigenvalues \(0,1,r,N\) respectively have the following off-diagonal entries: apex–leaf \((1/N,0,0,-1/N)\); leaves from different blades \((1/N,-1/(mk),0,1/(mkN))\); distinct leaves from the same blade \((1/N,(m-1)/(mk),-1/k,1/(mkN))\). These follow from subtracting the projector onto global leaf averages from the direct sum of the uniform-on-blade projectors, and the rank-one apex–leaf contrast projector. Substitution into \(F(hL)\) yields, for \(h>0\):
\[
 T_{apex,leaf}(h)=\frac{12h}{D(Nh)},
\]
\[
 T_{u,v}(h)=\frac{12h^2((N+1)h+6)}{D(h)D(Nh)}\quad\text{if the leaves are in different blades},
\]
\[
 T_{u,v}(h)=\frac{12hP_{m,r}(h)}{D(h)D(rh)D(Nh)}\quad\text{if they are distinct leaves in the same blade}.
\]
For the third identity, the sign numerator before clearing denominators is \(mNg(rh)-(m-1)Ng(h)-g(Nh)\). Multiplying it by \(D(h)D(rh)D(Nh)/(12Nh)\) yields
\[
 mrD(h)D(Nh)-(m-1)D(rh)D(Nh)-D(rh)D(h)=mkP_{m,r}(h).
\]
This proves the displayed rational formula by cancellation. Every diagonal entry of \(F(hL)\) is a sum of nonnegative orthogonal-projector diagonal weights multiplied by strictly positive \(F\)-values, including the constant-mode contribution \(1/N\); hence it is positive.

For \(m\ge2\), \(r\ge3\), we have \(k\ge2\), \(u\ge2k\), and \(A=u^2-u(k-1)-2k-1\ge2k^2-1>0\), because that expression is increasing in \(u\ge2k\). All other coefficients of \(P\) are positive. Consequently \(P(h)/h^4\) strictly decreases from \(+\infty\) to \(-rA\) on \((0,\infty)\): there is one positive zero, with positive sign before and negative sign after. The preceding entry identities give the complete claimed sign classification, including the boundary. For \(m=1\) the graph is \(K_r\), with every off-diagonal step entry \(g(rh)/r>0\). For \(r=2\) there are no distinct leaves in a blade, and the first two positive entry formulas exhaust all off-diagonal positions. At \(h=0\) the map is the identity.

For fixed \(r\ge3\), divide \(P_{m,r}\) by \(u^2\). As \(m\to\infty\), its coefficients converge to those of \(-rh^4+12h^2\) uniformly on bounded intervals. The unique positive roots are trapped between any positive values on either side of \(\sqrt{12/r}\), proving the stated limit.

## Verification
Run `python3 verify.py` with the Python standard library. It computes the matrix rational function by exact `fractions.Fraction` Gaussian elimination on 54 graphs/timesteps, checks 5,532 off-diagonal identities and signs, diagonal positivity and row sums, and verifies the quartic numerator identity in every instance. The output is `VERIFY_OK` with counts. The test is a finite reproducibility check, not a substitute for the all-parameter algebraic proof above.

## Relationship to prior work
Zappavigna–Colaneri–Kirkland–Shorten study positive-system discretization by diagonal Padé approximants and give general positivity obstructions and sufficient step conditions, rather than an exact step horizon for this graph family. Lóczi–Ketcheson study scalar rational absolute monotonicity of implicit Runge–Kutta stability functions. A previously derived convex-filter criterion for joins of cliques applies only to convex nonnegative scalar filters: the present \(F\) is not globally convex (indeed its second derivative is eventually negative), so its criterion does not imply this result. The present claim is the exact graph-specific all-timestep interval and sign pattern for a nonconvex filter.

## Limitations
Publication priority beyond the directly inspected material is not certified. The result applies only to equal-size blades with unit edge conductances and the completed two-stage Gauss–Legendre step. It does not claim positivity of intermediate stages, arbitrary Markov generators, arbitrary weighted windmills, or repeated multi-step composition beyond one completed step. The numerical verifier enumerates only finite cases. No independent mathematical audit has been performed.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland, and R. Shorten, *Essentially Negative News About Positive Systems*, 2012 public preprint, https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf ; Maynooth public record https://mural.maynoothuniversity.ie/id/eprint/3761/ .
2. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1, posted 2013-03-26, https://arxiv.org/html/1303.6651v1 .
