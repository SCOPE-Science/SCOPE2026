# Sharp branching cutoff and reentrant positivity for Radau IIA on symmetric double-star trees

## Finding

For every integer \(m\ge2\), let \(D_m\) be the unweighted double-star tree with adjacent hubs, each of which has exactly \(m\) private leaves. Write \(L_m\) for its combinatorial Laplacian. The completed two-stage, order-three Radau IIA heat step is
\[
T_m(h)=(6I-2hL_m)(h^2L_m^2+4hL_m+6I)^{-1},\qquad h\ge0.
\]
**Theorem.** The endpoint map \(T_m(h)\) is entrywise nonnegative for every \(h\ge0\) exactly when \(2\le m\le5\). In fact all entries are strictly positive for every \(h>0\) in these four cases. For each integer \(m\ge6\), every leaf diagonal is strictly negative at \(h=10\), but there exist positive numbers \(\varepsilon_m,H_m\) such that all entries are strictly positive when \(0<h<\varepsilon_m\) or \(h>H_m\). Thus unconditional endpoint positivity fails at precisely six or more leaves on each hub, with positivity reappearing at large steps.

At the first failing parameter \(m=6\), the leaf diagonal at \(h=10\) is exactly \(-27666199/7741730811\).

## Assumptions and scope

All edges have unit weight, \(m\) is an integer at least two, and \(h\) is a nonnegative real. There are \(2m+2\) vertices. Positivity refers **only to the fully completed endpoint matrix** acting on every nonnegative initial vector; it does not assert that internal Runge–Kutta stages remain nonnegative. The graph diffusion equation is \(y'=-L_my\), and no source terms are included. The scalar stability function of this Radau IIA method is
\[
r(z)=\frac{6-2z}{z^2+4z+6}.
\]

## Proof

**1. Exact spectral reduction.** Order the hubs and then the two leaf classes. The four-dimensional subspace of functions constant within either leaf class is invariant under \(L_m\), with quotient matrix
\[
Q_m=\begin{pmatrix}
m+1&-1&-m&0\\
-1&m+1&0&-m\\
-1&0&1&0\\
0&-1&0&1
\end{pmatrix}.
\]
On each leaf zero-sum space the Laplacian acts as the identity. Let
\[
B_m(h)=(6I-2hQ_m)(h^2Q_m^2+4hQ_m+6I)^{-1},\quad
r_1(h)=\frac{6-2h}{h^2+4h+6}.
\]
Rows and columns of \(B\) are indexed by the two hubs and the two leaf classes, in that order (zero-based indices 0,1,2,3). Graph automorphisms and the direct-sum decomposition give exactly seven entry types:
\[
\begin{array}{lll}
\text{hub diagonal}:B_{00},&\text{hub to hub}:B_{01},&
\text{hub to own leaf}:B_{02}/m,\\
\text{hub to opposite leaf}:B_{03}/m,&
\text{leaf diagonal}:B_{22}/m+(1-1/m)r_1,&
\text{same-side distinct leaves}:(B_{22}-r_1)/m,\\
\text{opposite-side leaves}:B_{23}/m.
\end{array}
\]
These formulas cover every matrix entry and preserve its actual normalization, not merely an aggregated quotient entry. The factor \(h^2 L_m^2+4hL_m+6I\) is positive definite for \(h\ge0\), so the endpoint map is always well-defined.

**2. The four all-step-positive cases.** For each of the four integer values \(m=2,3,4,5\), reduce each of the seven entries above to an exact rational function in \(h\). Their denominators factor into polynomials with strictly positive coefficients. Extract and remove the maximal factor of \(h\) from each numerator where present. Each resulting numerator polynomial has positive constant and leading coefficient and exactly **zero positive real roots**. This last assertion is an exact, finite Sturm-theorem calculation, not interpolation or a floating-point sample. There are \(4\times7=28\) checked polynomials. The complete rational calculations, including the quotient construction, denominator positivity checks and exact Sturm root counts, are reproduced by `verify.py`. A real polynomial that is positive at zero and has no positive real zero cannot change sign on \([0,\infty)\); therefore all seven entries are strictly positive for \(h>0\). At \(h=0\), \(T_m(0)=I\), which is nonnegative.

**3. A uniform exact negative witness for all greater branching.** The rational expression for any leaf diagonal has denominator
\[
\begin{split}
D_m(h)={}&(h^2+4h+6)\\
&\cdot\bigl(h^2(m+1)^2+4h(m+1)+6\bigr)\\
&\cdot\bigl(2h^4+4h^3m+12h^3+3h^2m^2+18h^2m+31h^2+12hm+36h+18\bigr).
\end{split}
\]
Each factor is strictly positive for \(m\ge2,h\ge0\). The numerator \(N_m(h)\) is given by the symbolic rational expression in `verify.py`; its exact substitution \(m=6+t,h=10\) yields
\[
N_{6+t}(10)=-420000t^4-14576000t^3-183761600t^2-764053760t-221329592.
\]
This is strictly negative for every real \(t\ge0\), proving that every \(m\ge6\) fails positivity at step \(h=10\). At \(m=6\), evaluation of the same fraction gives the exact value in the theorem.

**4. Positivity returns for small and large steps.** The Runge–Kutta stability function has expansion \(r(z)=1-z+z^2/2-z^3/6+O(z^4)\). On the diameter-three tree \(D_m\), distinct vertices at distance \(d\in\{1,2,3\}\) have leading off-diagonal entry \(c_{ij}h^d/d!\), where \(c_{ij}\) counts shortest paths and is positive. The diagonal tends to one as \(h\downarrow0\). Hence the full end-step is strictly positive for all sufficiently small positive \(h\). For large \(h\), symmetry of the connected Laplacian and the decay \(r(z)\to0\) for \(z\to\infty\) give \(T_m(h)\to\mathbf1\mathbf1^T/(2m+2)\). Its entries are strictly positive, establishing positivity for all sufficiently large \(h\). Continuity and the negative witness at \(h=10\) imply a nonempty intermediate interval of failure.

These four steps establish all assertions for every integer \(m\ge2\).

## Verification

Run `python verify.py` with SymPy installed (tested against SymPy 1.14.0). The verifier reconstructs the four-dimensional quotient directly, generates the seven rational entry classes, checks denominator coefficient signs, uses exact Sturm root counting on every one of the 28 numerators, verifies the exact polynomial witness after substitution, and independently compares all seven classes to entries of the full \((2m+2)\)-vertex matrix at 15 rational graph/step configurations (105 comparisons). Full matrices were also checked to preserve constants. The infinite-family negative conclusion is proved symbolically by the polynomial with strictly negative coefficients, not by testing finitely many \(m\).

## Relationship to prior work

Horváth's study of Runge–Kutta positivity thresholds examines general positivity-preserving systems and includes the two-stage Radau IIA method on finite-difference diffusion examples, noting that guarantees over all positive problems need not describe favorable behavior for fixed special systems. The present theorem instead specifies an exact unweighted graph family and requires positivity for *all nonnegative initial vectors* on that family, for each step size. The work by Bonaventura and Della Rocca studies the different L-stable TR-BDF2 family and its monotonicity/SSP variants. General absolute-monotonicity barriers do not imply the sharp integer parameter \(m=5\) or the uniform \(h=10\) counterwitness here. Separately known graph-family positivity classifications for paths, cycles and complete multipartite graphs are not statements about these proper double-star trees.

## Limitations

The classification is for symmetric, unweighted double stars only, not unequal leaf classes, general tree topology, other Runge–Kutta schemes, or nonnegativity of stage values. Sturm verification is an exact finite polynomial certificate, reproduced with external symbolic software; it is not an independent audit. The endpoint failure at \(h=10\) does not establish an explicit exact boundary of the entire failing-step interval for each \(m\ge6\). Literature comparison cannot exclude all unindexed equivalent results.

## References

1. Z. Horváth, “On the positivity step size threshold of Runge–Kutta methods,” *Applied Numerical Mathematics* 53 (2005), 341–356, available online 27 October 2004, https://doi.org/10.1016/j.apnum.2004.08.026.
2. L. Bonaventura and A. Della Rocca, “Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions,” arXiv:1510.04303, first posted 14 October 2015, https://arxiv.org/abs/1510.04303.
