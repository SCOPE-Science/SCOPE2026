# A sharp four-patch corridor-budget inversion at \(B=\sqrt{3}\,d\)

## Finding
Consider a connected, simple, undirected habitat graph on at least two vertices with one refuge and otherwise drought-affected patches. Fix a total *undirected edge-conductance budget* \(B>0\): when a graph has \(m\) edges, each edge receives symmetric migration conductance \(B/m\). Refuge low-density growth is \(r>0\), and every other patch has mortality \(d>0\). The rare-population linearization is
\[
\dot x=H_Gx,\qquad H_G=\operatorname{diag}(r,-d,\ldots,-d)-\frac Bm L_G,
\]
where \(L_G\) is the usual combinatorial graph Laplacian. Define \(r_G(B,d)>0\) by the criterion that the largest real eigenvalue of \(H_G\) is positive exactly when \(r>r_G(B,d)\), and equals zero exactly when \(r=r_G(B,d)\).

For four patches, compare the **path** \(P\) with edges \(01,03,12\) and refuge at vertex 0 (an interior path vertex), against the **diamond** \(D\) with edges \(01,02,03,12,23\) and refuge at vertex 0 (a degree-three vertex). The exact invasion-growth thresholds are
\[
 r_P=\frac{3Bd(B^2+6Bd+6d^2)}{(B+3d)(B^2+9Bd+9d^2)},\qquad
 r_D=\frac{3Bd}{B+5d}.
\]
Consequently
\[
\boxed{r_P-r_D=\frac{3Bd^2(3d^2-B^2)}{(B+3d)(B+5d)(B^2+9Bd+9d^2)}}.
\]
In particular, the five-corridor diamond admits invasion for a strictly larger range of refuge growth rates when \(0<B<\sqrt3\,d\); the three-corridor path admits invasion for a strictly larger range when \(B>\sqrt3\,d\). They tie at precisely \(B=\sqrt3\,d\). On either side, the open interval between the two critical growth rates consists entirely of parameters for which exactly one of these two landscapes has a positive invasion exponent.

**Minimality.** For each fixed patch count \(n\) equal to two or three, every pair of connected simple undirected graphs on \(n\) vertices, with any choice of one refuge vertex, has a fixed ordering of its corresponding thresholds as \(B/d\) varies. Four patches are therefore the smallest order at which this *budget-normalized graph-ranking inversion* is possible.

For the optional density-limited extension \(\dot x=H_Gx-c(x_i^2)_i\) with \(c>0\), a positive invasion exponent is equivalent to a unique strictly positive equilibrium attracting every nonzero nonnegative initial condition. At zero or negative invasion exponent, every nonnegative initial condition tends to zero. Hence the intervals above also represent deterministic persistence-versus-extinction differences for this specified logistic model.

## Assumptions and scope
All parameters \(B,d,r,c\) are strictly positive when used. Migration is conservative, instantaneous, symmetric, and linear; each undirected edge contributes the same conductance within its own graph. The sum of undirected edge conductances—not the total outflow from the refuge, the mean vertex degree, or a per-edge rate—is fixed at \(B\). The only favorable patch is vertex 0, with intrinsic low-density rate \(r\); all remaining patches have equal intrinsic rate \(-d\). Patches have equal modeled units and no demographic noise. The graph need not be geometrically embedded. The result compares two specifically defined four-vertex networks, and establishes minimality among *all* connected simple undirected networks with at most three vertices under this same one-refuge rule. It does not classify all networks on four vertices.

## Proof
**1. A general invasion test.** Set \(u=r+d\), let \(e\) be the unit vector at the refuge, and put \(Q=dI+(B/m)L_G\). Then
\[
H_G=-Q+uee^\top.
\]
The symmetric matrix \(Q\) is positive definite since the graph Laplacian is positive semidefinite and \(d>0\). Congruence by \(Q^{-1/2}\) transforms \(H_G\) to \(-I+uww^\top\) with \(w=Q^{-1/2}e\). By Sylvester's inertia theorem, the largest eigenvalue of \(H_G\) is positive, zero, or negative according as
\[
u\,e^\top Q^{-1}e \quad\text{is greater than, equal to, or less than }1.
\]
At equality the zero eigenvalue is simple. Since \(H_G\) is an irreducible symmetric Metzler matrix, the largest eigenvalue has a strictly positive eigenvector; hence the sign criterion determines population invasion.

Write \(z=d/B\) and define the grounded refuge resolvent
\[
F_G(z)=e^\top\bigl(zI+L_G/m\bigr)^{-1}e.
\]
Then \(e^\top Q^{-1}e=F_G(z)/B\), so the critical growth is
\[
r_G(B,d)=\frac{B}{F_G(d/B)}-d.
\]
This value is strictly positive: \(Q\succeq dI\) and, because the refuge has a neighbor, \(e\) is not in the zero-eigenspace of \(L_G\), giving \(e^\top Q^{-1}e<1/d\).

**2. Exact four-patch resolvents.** Direct inversion of the specified four-by-four matrices gives
\[
F_P(z)=\frac{(3z+1)(9z^2+9z+1)}{z(3z+2)(9z^2+12z+2)},
\qquad
F_D(z)=\frac{5z+1}{z(5z+4)}.
\]
Their difference factors exactly as
\[
F_P(z)-F_D(z)=\frac{-3(3z^2-1)}{(3z+2)(5z+4)(9z^2+12z+2)}.
\]
All factors in the denominator are strictly positive for \(z>0\). Therefore the difference changes sign once, at \(z=1/\sqrt3\). Applying the reciprocal formula for \(r_G\) and simplifying yields
\[
\frac{r_P-r_D}{B}=\frac{3z^2(3z^2-1)}{(3z+1)(5z+1)(9z^2+9z+1)}.
\]
This proves both the closed-form thresholds and the exact ordering, including strictness and the tie. Because \(r\mapsto u=r+d\) increases strictly, any \(r\) strictly between distinct thresholds makes one eigenvalue positive and the other negative.

**3. Sharp small-graph obstruction.** There is just one connected simple graph with two vertices. With three vertices, the only connected graph types are the two-edge path and the triangle. The path has two possible refuge positions: center or endpoint. In units \(z=d/B\), their resolvents are
\[
F_{\mathrm{center}}=\frac{2z+1}{z(2z+3)},\qquad
F_{\mathrm{end}}=\frac{4z^2+6z+1}{z(2z+1)(2z+3)},\qquad
F_{\mathrm{triangle}}=\frac{3z+1}{3z(z+1)}.
\]
Exact subtraction gives
\[
F_{\mathrm{end}}-F_{\mathrm{triangle}}=\frac{2(z+2)}{3(z+1)(2z+1)(2z+3)}>0,
\]
\[
F_{\mathrm{triangle}}-F_{\mathrm{center}}=\frac{2}{3(z+1)(2z+3)}>0.
\]
Thus for every \(z>0\), \(r_{\mathrm{end}}<r_{\mathrm{triangle}}<r_{\mathrm{center}}\), as the threshold reverses the order of the resolvent. This exhausts every connected graph/refuge choice for fixed patch counts \(n=2,3\) and proves the stated minimality for comparing networks of equal size.

**4. Logistic persistence interpretation.** The equation \(\dot x=H_Gx-c(x_i^2)_i\) is cooperative in the positive orthant. If the principal eigenvalue \(\lambda\le0\), multiplication by its positive eigenvector \(v\) gives
\[
\frac{d}{dt}(v^\top x)=\lambda v^\top x-c\sum_i v_i x_i^2\le -\frac c{\sum_i v_i}(v^\top x)^2,
\]
so all coordinates tend to zero. If \(\lambda>0\), a sufficiently small positive multiple of \(v\) is a strict subsolution, while a sufficiently large constant vector is a supersolution. Cooperative comparison gives a positive equilibrium. To prove uniqueness, if two positive equilibria \(x,y\) differ, let \(\theta=\max_i x_i/y_i>1\), after swapping them if necessary. At a coordinate with \(x_i=\theta y_i\), cooperativity implies \(0=f_i(x)\le f_i(\theta y)=-c\theta(\theta-1)y_i^2<0\), a contradiction. Positivity of the flow for all positive times and squeezing between sub- and supersolutions gives convergence of every nonzero nonnegative solution to this unique positive equilibrium.

## Verification
The symbolic checker `check.py` constructs the exact graph Laplacians, inverts all relevant symbolic matrices, verifies every displayed factorization by zero symbolic remainder, verifies the exhaustive three-vertex comparisons, and checks that two rational parameter examples straddle the distinct thresholds. It also independently evaluates numerical eigenvalues on a range of ratios, with eigenvalues at the exact constructed invasion boundaries within numerical tolerance. Run with `python check.py` using Python 3, SymPy, and NumPy. The exact symbolic identities corroborate—not replace—the analytical sign and inertia arguments.

The opposite persistence regimes can be reproduced without floating-point calculations: at \(B=1,d=1/2\), the path threshold is \(66/155\), the diamond threshold is \(3/7\), and \(r=107/250\) lies strictly between them; at \(B=1,d=1\), the diamond threshold is \(1/2\), the path threshold is \(39/76\), and \(r=51/100\) lies strictly between them.

## Relationship to prior work
The empirical four-patch corridor experiment of Li, Memmott and Clements (2023) motivates the importance of corridor quality, the number of drought-affected habitats, and the spatial configuration of four patches. That study does not use this rank-one, heterogeneous linear refuge model and does not calculate its fixed-budget invasion cutoffs. Nicoletti and coauthors (2023) derive a much broader microscopic metapopulation dispersal kernel, including a graph-Laplacian resolvent and spectral survival criteria. Their general framework and resolvent method are acknowledged as prior knowledge; the new claim is the exact path-versus-diamond *invasion-threshold* comparison under normalized total corridor conductance, together with its four-vertex minimality, rather than a new spectral technique. Karnatak and Wollrab (2020) analyze dispersal and extinction in a different degree-normalized network model; no implication establishes this fixed-total-conductance comparison. General source-sink spectral thresholds and standard rank-one updates are not new claims.

## Limitations
The source model is an idealization; the paper does not infer actual habitat conductances or demographic parameters from the cited microcosm. In particular, improving a corridor in the experiment is not modeled as uniformly redistributing a fixed total migration budget between different graphs. The conclusion is only about the specified one-refuge, equal-sink-mortality model and its deterministic logistic extension, not noisy finite-population extinction times, all possible four-node layouts, or spatially heterogeneous movement costs. Historical priority outside the inspected primary literature and searchable research records remains uncertain; generic graph spectral principles may subsume parts of the proof, but no stronger inspected statement supplied the explicit threshold comparison and minimality.

## References
1. Li, D., Memmott, J., and Clements, C. F., “Corridor quality buffers extinction under extreme droughts in experimental metapopulations,” *Ecology and Evolution* 13 (2023), e10166. First public publication 2023-06-01. https://doi.org/10.1002/ece3.10166
2. Nicoletti, G. et al., “Emergent encoding of dispersal network topologies in spatial metapopulation models,” *PNAS* 120 (2023), e2311548120. Public 2023-11-06. https://doi.org/10.1073/pnas.2311548120
3. Karnatak, R. and Wollrab, S., “A probabilistic approach to dispersal in spatially explicit meta-populations,” *Scientific Reports* 10 (2020), 22234. https://doi.org/10.1038/s41598-020-79162-9
4. Cosner, C., “The effects of spatial heterogeneity in population dynamics,” *Journal of Mathematical Biology* (1991). https://doi.org/10.1007/BF00167155
5. Bansaye, V. and Lambert, A., “Past, growth and persistence of source-sink metapopulations” (2011). https://arxiv.org/abs/1111.2535
