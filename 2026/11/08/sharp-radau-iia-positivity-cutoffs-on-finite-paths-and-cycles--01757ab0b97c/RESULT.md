# Sharp Radau IIA positivity cutoffs on finite paths and cycles

## Finding

**Theorem.** Let \(G\) be an unweighted simple path \(P_n\) with \(n\ge2\), or an unweighted simple cycle \(C_n\) with \(n\ge3\). Let \(L_G=D_G-A_G\) be its combinatorial Laplacian. Apply the ordinary two-stage, third-order Radau IIA Runge–Kutta method to the linear graph heat equation \(u'=-L_Gu\); its completed step is
\[
T_G(h)=R(hL_G),\qquad R(x)=\frac{1-x/3}{1+2x/3+x^2/6},\qquad h\ge0.
\]
Then \(T_G(h)\) is entrywise nonnegative for **every** \(h\ge0\) if and only if
\[
G=P_n\text{ with }2\le n\le5,\quad\text{or}\quad G=C_n\text{ with }3\le n\le9.
\]
For every listed graph, every entry is **strictly positive** whenever \(h>0\), so the step is a positive, symmetric, row-stochastic matrix. For each excluded path (\(n\ge6\)) and cycle (\(n\ge10\)), any vertices at graph distance five have \(T_G(h)_{uv}<0\) for all sufficiently small positive \(h\).

More generally, if a finite **connected** simple unweighted undirected graph has diameter at least five, the same method has a negative matrix entry at arbitrarily small positive steps. For a disconnected graph the conclusion holds if one of its connected components has diameter at least five. This diameter obstruction is a lemma explaining the sharp endpoints, not a claim about graphs of smaller diameter.

## Assumptions and scope

Paths carry unit conductance between consecutive numbered vertices; cycles carry unit conductance around their ring. For \(C_3\), its three distinct edges are counted once each. There are no boundary killing terms, no extra reaction terms, and no spatial mesh normalization: \(h\) is the scalar time step multiplying the **unweighted** Laplacian. A positive initial vector here means componentwise nonnegative input; preservation for every such input is equivalent to entrywise nonnegativity of \(T_G(h)\). Claims concern the *completed* step, not the internal RK stages.

## Proof

**The small-step obstruction.** Ordinary exact power-series division gives
\[
R(x)=1-x+\frac{x^2}{2}-\frac{x^3}{6}+\frac{x^4}{36}+\frac{x^5}{108}+O(x^6).
\]
If \(d_G(u,v)=5\), all \((L_G^j)_{uv}\) vanish for \(0\le j<5\), since each off-diagonal factor can traverse at most one edge. In \((L_G^5)_{uv}\), exactly five off-diagonal moves are required. Thus every contributing term has sign \((-1)^5\); writing \(\nu_5(u,v)\ge1\) for the number of shortest five-edge walks, we have
\[
(L_G^5)_{uv}=-\nu_5(u,v),\quad
[T_G(h)]_{uv}=-\frac{\nu_5(u,v)}{108}h^5+O(h^6)<0
\]
for sufficiently small \(h>0\). Every \(P_n\) with \(n\ge6\) contains a distance-five pair, as does every \(C_n\) with \(n\ge10\). For the boundary witnesses \((P_6,0,5)\) and \((C_{10},0,5)\), \(\nu_5\) equals one and two respectively. The same argument proves the diameter lemma for arbitrary finite simple unweighted connected graphs; disconnected graphs with a diameter-five component also qualify componentwise.

**The all-step finite half.** Only the eleven graph orders \(P_2,\ldots,P_5\) and \(C_3,\ldots,C_9\) remain. Put
\[
Q_G(h)=I+\frac{2h}{3}L_G+\frac{h^2}{6}L_G^2,\qquad
A_G(h)=I-\frac h3L_G.
\]
Since \(L_G\) is symmetric positive semidefinite and \(1+2x/3+x^2/6>0\) for \(x\ge0\), \(Q_G(h)\) is invertible for every \(h\ge0\), and \(T_G(h)=Q_G(h)^{-1}A_G(h)\). In exact rational arithmetic each relevant entry reduces to \(N_{uv}(h)/D_{uv}(h)\) with integer polynomial coefficients. The full, independently reproducible data appear in `CERTIFICATE.json`. Across all sixty distinct symmetry-reduced entries, **every** coefficient of \(N_{uv}\) and \(D_{uv}\) is nonnegative, \(D_{uv}(0)>0\), and \(N_{uv}\) is not zero. Every off-diagonal \(N_{uv}\) has zero constant term but at least one strictly positive higher coefficient. Consequently all entries are strictly positive for every \(h>0\).

The certificate exhausts the full upper triangle for each path, since \(T_G\) is symmetric, and only distances \(0,1,\ldots,\lfloor n/2\rfloor\) for each cycle, since \(T_G\) is symmetric circulant. The verifier computes the exact matrix rational functions from \(Q_G^{-1}A_G\), checks these coefficients against the embedded certificate and independently checks the fifth-order witness identities. There is no inference from finite *numerical sampling* to an infinite time interval: the signs of exact polynomials certify all real \(h\ge0\).

Finally \(L_G\mathbf1=0\) and \(R(0)=1\), so \(T_G(h)\mathbf1=\mathbf1\). Symmetry and entrywise positivity establish strict stochasticity for \(h>0\), completing the proof.

## Verification

Run `python VERIFY.py` alongside `CERTIFICATE.json` with SymPy installed. The checked exact rational identities cover all path upper-triangle entries and all cycle-distance entries for the eleven listed orders. The script reports `VERIFY_OK` only after comparing all sixty rational numerator/denominator coefficient pairs and independently testing the Taylor coefficient and the path/cycle distance-five walks.

A representative stringent certificate is the antipodal-distance-four entry for \(C_9\):
\[
[T_{C_9}(h)]_{0,4}=\frac{4h^4+36h^5+54h^6+20h^7+h^8}{144+864h+2376h^2+3728h^3+3580h^4+2088h^5+708h^6+120h^7+9h^8}.
\]
Every coefficient in this displayed fraction is nonnegative and the denominator is positive. The general claim is covered by the complete certificate rather than by this example alone.

## Relationship to prior work

Bolley and Crouzeix (1978) proved a universal obstruction to unconditional positivity of higher-order one-step methods over *all* positive parabolic generators; their proof uses matrix chains to expose derivative signs. That quantified universal result does not classify any single fixed path or cycle family for all timesteps. Lóczi and Ketcheson (first public arXiv version March 26, 2013) analyze absolute-monotonicity radii of rational Runge–Kutta stability functions, rather than graph-order cutoffs for the specific two-stage Radau IIA map. Horváth, Song and Terlaky (first public arXiv version June 26, 2014) develop general step-length bounds for rational discretizations on invariant polyhedra, not a sharp exact finite-size classification for these graphs.

The present claim combines the fifth-order path-distance obstruction with all-step exact positivity of the finite exceptional set. It does **not** assert general unconditional positivity across all graphs, or novelty of the Radau IIA stability function, absolute monotonicity, matrix functional calculus or the shortest-walk argument as separate techniques.

## Limitations

The theorem is restricted to **unweighted** paths/cycles with no killing boundary condition. Different conductances, directed networks, reaction terms, internal-stage positivity and nonlinear problems are not addressed. The rational-coefficient certificate relies on reproducible exact computer algebra for the finite part; no independent external mathematical audit has been performed. The accessible literature comparison does not establish global publication priority beyond the inspected sources and searched records.

## References

1. C. Bolley and M. Crouzeix, *Conservation de la positivité lors de la discrétisation des problèmes d'évolution paraboliques*, RAIRO Analyse numérique 12 (1978), 237–245, https://doi.org/10.1051/m2an/1978120302371, full text https://www.numdam.org/article/M2AN_1978__12_3_237_0.pdf.
2. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651 (first publicly posted 2013-03-26), https://arxiv.org/abs/1303.6651; LMS Journal of Computation and Mathematics 17 (2014), 159–205.
3. Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, arXiv:1406.6755 (first posted 2014-06-26), https://arxiv.org/abs/1406.6755; DCDS 35 (2015), 2997–3013.
