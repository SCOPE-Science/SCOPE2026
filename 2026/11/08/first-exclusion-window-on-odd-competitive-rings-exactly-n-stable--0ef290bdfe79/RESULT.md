# First exclusion window on odd competitive rings: exactly \(n\) stable communities

## Finding

**Theorem (sharp first extinction window on an odd competition ring).** For every odd integer \(n\ge5\), let
\[
a_n=\frac1{2\cos(\pi/n)}.
\]
For every \(0<\alpha<a_n\), there is exactly one asymptotically stable equilibrium, with every species present at abundance \((1+2\alpha)^{-1}\). For every
\[
a_n<\alpha<a_{n-2},
\]
there are **exactly \(n\)** asymptotically stable equilibria. Each loses exactly two species, and its surviving species form a singleton together with a disjoint path on \(n-3\) vertices in \(C_n\), separated by one extinct species on each side. All \(n\) equilibria are hyperbolic and rotationally equivalent; no other equilibrium is asymptotically stable in this interval.

Let \(L=n-3\), and let \(z=(z_1,\ldots,z_L)\) solve \((I+\alpha A_{P_L})z=\mathbf1\). With \(e=z_1=z_L\), the equilibrium biomass and its excess over the homogeneous (unstable) equilibrium are exactly
\[
B=1+\frac{L+2\alpha e}{1+2\alpha},\qquad
B-\frac{n}{1+2\alpha}=\frac{2[\alpha(1+e)-1]}{1+2\alpha}>0.
\]
Thus symmetry breaking reduces species richness by two while increasing total biomass over the homogeneous stationary reference state.

## Assumptions and scope

The interaction network is the labeled undirected cycle \(C_n\), \(n\ge5\) odd. Nonnegative species abundances evolve according to
\[
\dot x_i=x_i\bigl(1-x_i-\alpha(x_{i-1}+x_{i+1})\bigr),
\qquad i\in\mathbb Z/n\mathbb Z,
\]
with a single common competitive interaction strength \(\alpha>0\), unit intrinsic growth and unit self-limitation. There is no immigration or stochastic forcing. Stability always means local asymptotic stability relative to the full nonnegative orthant, including invasion by initially absent species. The theorem concerns the two stated **open** parameter intervals. At the endpoints, equilibria may be nonhyperbolic and are not classified.

## Proof

**1. Stability criterion and the homogeneous state.** Write \(M=I+\alpha A_{C_n}\). The quadratic potential
\[
F(x)=\tfrac12x^{\mathsf T}Mx-\mathbf1^{\mathsf T}x
\]
satisfies \(\dot F=-\sum_i x_i(\partial_iF)^2\le0\). At any equilibrium with strictly positive support \(S\), the surviving coordinates solve \(M_Sx_S=\mathbf1\), while each missing coordinate has invasion growth \(g_j=1-\alpha\sum_{i\sim j}x_i\). A hyperbolically stable equilibrium is characterized by \(M_S\) positive definite and every \(g_j<0\): its Jacobian is block triangular, with surviving block \(-\operatorname{diag}(x_S)M_S\). Conversely any asymptotically stable equilibrium must have a positive-semidefinite surviving quadratic form and nonpositive missing-coordinate invasion growth; a singular surviving form cannot yield an isolated asymptotically stable equilibrium, since any positive supported solution then belongs to a local affine continuum of equilibria.

The least eigenvalue of \(A_{C_n}\) for odd \(n\) is \(-2\cos(\pi/n)\). Consequently \(M\) is positive definite exactly when \(\alpha<a_n\). In that range the strictly positive uniform equilibrium is the unique minimizer of \(F\) on the nonnegative orthant; it is globally attracting from strictly positive initial abundances via the usual logarithmic relative-entropy Lyapunov function. No other boundary state can be asymptotically stable. Above \(a_n\), the homogeneous state has a positive Jacobian eigenvalue and is unstable.

**2. Runs in a candidate stable support.** Now fix \(a_n<\alpha<a_{n-2}\). In particular \(1/2<\alpha<1\). At any positive surviving coordinate, its equilibrium equation implies \(0<x_i\le1\). Two adjacent extinct coordinates cannot occur in an asymptotically stable equilibrium: one of them has at most one surviving neighbor and therefore invasion growth at least \(1-\alpha>0\). Hence all missing vertices are isolated, and the surviving support is a cyclic sequence of path runs separated by single missing vertices.

For a path with \(r\ge3\) odd vertices, a strictly positive internally stable state is impossible at \(\alpha>1/2\). Indeed, if its quadratic form \(I+\alpha A_{P_r}\) is not positive definite, a positive supported equilibrium cannot be asymptotically stable. If it is positive definite, consider instead the path's alternating configuration with abundance \(1\) at odd-numbered sites and zero at even-numbered sites. Its surviving coordinates satisfy the equilibrium equations, while each absent even-numbered site has growth \(1-2\alpha<0\). This is a constrained local minimum of the strictly convex path potential, hence the unique minimizer; a distinct strictly positive stationary solution is impossible. A singleton path is, of course, allowed, with abundance \(1\).

The least eigenvalue of the path adjacency \(A_{P_r}\) is \(-2\cos(\pi/(r+1))\). For an even surviving run, internal stability therefore requires \(\alpha<(2\cos(\pi/(r+1)))^{-1}\). Since \(\alpha>a_n\), a run of length \(n-1\) cannot be stable; the maximum possible even length is \(n-3\). All even lengths up to \(n-3\) are internally stable in the stated open window.

**3. Endpoint identity and missing-species invasion.** Set
\[
\theta=\arccos\frac1{2\alpha},\qquad h=\frac\theta2,
\quad \frac\pi n<\theta<\frac\pi{n-2}.
\]
For a stable even path of length \(r\), solve the linear recurrence \(z_i+\alpha(z_{i-1}+z_{i+1})=1\), \(z_0=z_{r+1}=0\). Its unique solution is positive, and its endpoint \(e_r=z_1=z_r\) obeys
\[
G_r:=\alpha e_r
=\frac{\sin(rh)}{\sin(rh)+\sin((r+2)h)}.
\]
An explicit solution of the recurrence is
\[
z_j=\frac{1}{1+2\alpha}\left[1+\frac{(-1)^j\sin\bigl((j-(r+1)/2)\theta\bigr)}{\sin((r+1)\theta/2)}\right],\qquad 1\le j\le r.
\]
The oscillatory homogeneous roots are \(-e^{\pm i\theta}\); for \(0<(r+1)\theta<\pi\), the numerator sine has strictly smaller absolute value than the positive denominator sine, proving every \(z_j>0\). At \(j=1\), the expression reduces to the displayed \(G_r\) by the sine addition identity. A singleton has endpoint abundance \(1\).

For any two even runs of lengths \(r,s\) separated by one missing species, the missing species always invades: \(G_r+G_s<1\). After clearing strictly positive denominators, this is precisely
\[
\sin((r+2)h)\sin((s+2)h)-\sin(rh)\sin(sh)
=\sin((r+s+2)h)\sin(2h)>0.
\]
Here \(r+s+2\le n\) and \(nh<\pi\). Consequently **no two even runs can be separated only by an extinct vertex** at a stable equilibrium.

For an even run of length \(r\) next to a singleton, the missing species has growth \(1-\alpha(e_r+1)\). Elementary trigonometry in the same interval yields the exact equivalence
\[
\alpha(e_r+1)>1\quad\Longleftrightarrow\quad (r+3)\theta>\pi.
\]
Indeed \(G_r+\alpha>1\) is equivalent to \(\cot((r+2)h)<\tan h\), which is equivalent to \((r+3)h>\pi/2\). For any even \(r\le n-5\), this is impossible since \((r+3)\theta\le(n-2)\theta<\pi\). For \(r=n-3\), it holds strictly because \(n\theta>\pi\).

**4. Complete support classification.** If there are no even runs, all surviving runs are singletons separated by single missing vertices, forcing an even cycle length, contrary to odd \(n\). Thus a stable support must contain an even run. By step 3 that even run must be flanked by singletons and have length \(n-3\). Exactly \(n\) vertices are then accounted for: its \(n-3\) survivors, two isolated zeros and one singleton survivor. The pattern is unique up to the \(n\) rotations of \(C_n\). Conversely, every such rotated pattern is an equilibrium: the even chain is positive and internally stable, the singleton is at abundance \(1\), and each of the two extinct vertices has strict negative invasion growth by the length-\(n-3\) endpoint inequality. Therefore these \(n\) states are all hyperbolically stable and exhaust the asymptotically stable equilibria.

**5. Biomass formula.** Summing the \(L\) equations on the occupied chain counts each interior neighbor twice and each endpoint once, so \((1+2\alpha)\sum_{i=1}^L z_i=L+2\alpha e\). Add the singleton abundance \(1\), then subtract the homogeneous reference biomass \(n/(1+2\alpha)\). The displayed strict inequality is exactly the same gap-invasion condition \(\alpha(1+e)>1\). This proves the asserted biomass ordering.

## Verification

The accompanying Python 3 standalone program `verify.py` uses exact rational arithmetic to solve equilibrium equations and test all surviving-path principal-minor and extinct-species invasion conditions. At three distinct rational interaction strengths in the first exclusion interval for each odd cycle size \(n\in\{5,7,9,11,13,15}\}\), it checked \(131{,}022\) nonempty support candidates in total, returning precisely \(n\) stable patterns of the predicted kind in every instance. No floating-point stability decision is used for a candidate support; floating point only confirms that the chosen rational test strengths lie inside the analytically established open interval. Run `python3 verify.py` from a folder containing this document and the script. These finite checks are corroboration, not a proof for unbounded \(n\); the analytical steps above establish the theorem.

## Relationship to prior work

Marcus, Turner and Bunin (2021) study the same symmetric competitive Lotka–Volterra interaction model in sparse ecological networks. They derive intrinsic feasibility/stability cutoffs for paths (chains), concentrating on typical large locally tree-like random graphs and explaining why cycle-containing motifs do not control their thermodynamic diversity jumps. Their path cutoff is used here as supporting background; it does **not** by itself classify the simultaneous *invasion stability* of all supports of an odd full cycle, or count the first symmetry-broken stable states. Hong and Pego (2021) develop exclusion and multiplicity constraints for stable Lotka–Volterra communities; their general support antichain principle is consistent with the present \(n\) equal-cardinality supports but does not imply their exact number, layout or interval. Lischke and Löffler (2017) develop a general algorithm for enumerating stable fixed points of finite competitive systems; a fixed-instance enumeration method is not an all-odd-size analytic classification. We did not obtain their full article and do not assert complete noncoverage from its abstract alone. A previously unindexed exact ring theorem remains a publication-priority risk.

## Limitations

The theorem concerns one deterministic, identical-coefficient, nearest-neighbor species-competition model, and the first two strict parameter regions only. It does not quantify basins of attraction, stochastic extinction, transient times, ecological noise, immigration, boundary values of \(\alpha\), higher competition regimes or dissimilar interaction strengths. The biomass comparison is to a stationary but unstable homogeneous state in the strong-competition regime, not to an observed alternative attractor. Independent external validation and complete publication-priority verification have not been performed.

## References

1. Stav Marcus, Ari M. Turner, Guy Bunin, *Local and collective transitions in sparsely-interacting ecological communities*, arXiv:2110.13603 (first submitted 2021-10-26). https://arxiv.org/html/2110.13603
2. Won Eui Hong and Robert L. Pego, *Exclusion and multiplicity for stable communities in Lotka–Volterra systems*, arXiv:2102.00611 (first submitted 2021-02-01). https://arxiv.org/abs/2102.00611
3. Heike Lischke and Thomas J. Löffler, *Finding all multiple stable fixpoints of n-species Lotka–Volterra competition models*, Theoretical Population Biology 115 (2017), 24–34. https://doi.org/10.1016/j.tpb.2017.02.001
