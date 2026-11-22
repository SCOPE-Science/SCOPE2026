# Sharp quadratic permeability threshold for a mortality-limited parallel habitat corridor

## Finding

A parallel stepping-stone route can strictly **improve source-to-target electrical conductance** while strictly **lowering the probability that a mortal disperser reaches the target**. There is a sharp route-permeability threshold, independent of the new route's entry-edge rate, and that threshold grows quadratically with the number of intermediate stepping stones.

Specifically, fix direct source-to-target jumping rate \(d>0\), death rate \(\kappa>0\), and new-route entry rate \(\alpha>0\). Let the added route be
\[
s\;\xleftrightarrow{\alpha}\;v_1\;\xleftrightarrow{g}\;v_2\;\xleftrightarrow{g}\;\cdots\;\xleftrightarrow{g}\;v_n\;\xleftrightarrow{g}\;t,
\]
with \(n\ge1\) and \(g>0\), in parallel with the pre-existing edge \(s\xleftrightarrow{d}t\). Continuous-time dispersers jump independently along each incident edge at its displayed rate, die at rate \(\kappa\) at every non-target node, start at \(s\), and succeed if they first reach \(t\) before death. Write \(P_n(d,\kappa,\alpha,g)\) for this probability and \(P_0=d/(d+\kappa)\) for the probability without the new route.

Define \(\theta=\operatorname{arcosh}(1+\kappa/(2g))\) and
\[
Z_n(g)=\frac{\cosh(\theta/2)}{\cosh((n+1/2)\theta)}.
\]
Then, for all stated parameters, the following equivalence holds, including the equality case:
\[
\boxed{\quad \operatorname{sgn}(P_n-P_0)=\operatorname{sgn}(Z_n(g)-P_0).\quad}
\]
For each integer \(n\ge1\) there is one and only one critical rate \(g_c(n;d,\kappa)>0\) defined by \(Z_n(g_c)=P_0\). The added route strictly worsens success for \(g<g_c\), leaves it unchanged at equality, and strictly improves success for \(g>g_c\), **for every** \(\alpha>0\). Yet the electrical conductance is always strictly larger:
\[
C_{\mathrm{new}}=d+\left(\alpha^{-1}+n/g\right)^{-1}>d.
\]
Moreover, \(g_c(1;d,\kappa)=d\), \(g_c(n+1;d,\kappa)>g_c(n;d,\kappa)\), and
\[
\boxed{\quad \lim_{n\to\infty}\frac{g_c(n;d,\kappa)}{n^2}
=\frac{\kappa}{\operatorname{arcosh}(1+\kappa/d)^2}.\quad}
\]
A finite-network extension is also valid: replacing the homogeneous detour by any finite positive-conductance side network meeting the source only at \(v_1\), the change in target-hitting probability has the sign of the side network's isolated, mortality-discounted target-hitting probability from \(v_1\), minus \(P_0\).

## Assumptions and scope

All network edges are undirected with positive symmetric continuous-time jump rates. The target \(t\) absorbs immediately, and the independent exponential mortality clock of rate \(\kappa\) continues through every living visit, including repeated returns. There are no births, saturation effects, changing rates, deadline constraints, or stochastic failures of edges. The base graph has just \(s,t\) and one edge of rate \(d\). The new route consists of \(n\) **new** intermediate vertices and \(n+1\) new edges; it is not a one-edge shortcut. The electrical conductance comparison ignores death, as ordinary static effective resistance does. Nothing here equates effective conductance with commute-time distance or asserts the latter decreases when the route is installed.

For the finite side-network extension, let \(B\) denote the nonsingular positive-definite killed Dirichlet matrix of all side-network non-target vertices when the edge to \(s\) is removed, and let \(b\) be their nonnegative vector of direct jumping rates to \(t\). Let \(e\) select the gateway vertex \(v_1\). Assume the side network has an internal route from \(v_1\) to \(t\), and all its living vertices have strictly positive death rate \(\kappa\).

## Proof

**1. Exact gateway screening, including arbitrary finite side networks.** Without the new route, first-event conditioning at \(s\) gives \(P_0=d/(d+\kappa)\). Put \(z=e^{\mathsf T}B^{-1}b\in(0,1)\) and \(R=e^{\mathsf T}B^{-1}e>0\). If \(p\) is the target-success probability from \(s\) after attaching the side network at rate \(\alpha\), then its vector of side-network success probabilities is
\[
q=(B+\alpha ee^{\mathsf T})^{-1}(b+\alpha ep).
\]
Sherman–Morrison, or multiplication of this equation by \(B^{-1}\), gives
\[
e^{\mathsf T}q=\frac{z+\alpha Rp}{1+\alpha R}.
\]
The source first-event equation is \((d+\kappa+\alpha)p=d+\alpha e^{\mathsf T}q\). Defining \(\beta=\alpha/(1+\alpha R)>0\), substitution yields
\[
p=\frac{d+\beta z}{d+\kappa+\beta},\qquad
p-P_0=\frac{\beta(z-P_0)}{d+\kappa+\beta}.
\]
This exact identity proves the asserted sign law and, crucially, its independence from \(\alpha\). Since \(B\) is a strictly killed positive weighted graph Dirichlet matrix, it is invertible, with nonnegative inverse; \(R>0\), and \(z\) is the corresponding isolated success probability.

**2. The homogeneous reflecting detour.** With \(s\) disconnected, let \(z_j\) be the probability of reaching \(t\) before death starting at \(v_j\). The backward equations are
\[
(g+\kappa)z_1=gz_2\quad(n>1),\qquad
(2g+\kappa)z_j=g(z_{j-1}+z_{j+1})\quad(2\le j\le n),
\]
where \(z_{n+1}=1\); for \(n=1\) the boundary reads \((g+\kappa)z_1=g\). Equivalently impose the reflecting ghost condition \(z_0=z_1\) in the second-order recurrence. Its unique solution, using \(\cosh\theta=1+\kappa/(2g)\), is
\[
z_j=\frac{\cosh((j-1/2)\theta)}{\cosh((n+1/2)\theta)},\qquad 1\le j\le n+1.
\]
Thus \(z_1=Z_n(g)\). Electrical resistances on the added series path sum, giving \(C_{\mathrm{new}}=d+(\alpha^{-1}+n/g)^{-1}\).

**3. Unique threshold and strict order by length.** For each \(n\), let \(\tau_n\) be the almost surely finite first target-hitting time of the isolated \(n\)-site reflecting continuous-time walk with every link rate one and no killing. Scaling all link rates to \(g\) divides that hitting time by \(g\). Consequently
\[
Z_n(g)=\mathbb E\big[\exp(-\kappa\tau_n/g)\big].
\]
Since \(\tau_n>0\) almost surely, this is continuous and strictly increasing from \(0\) to \(1\) as \(g\) ranges over \((0,\infty)\), giving exactly one \(g_c\). The explicit hyperbolic formula shows \(Z_{n+1}(g)<Z_n(g)\) for every \(g>0\), so the critical rates strictly increase with \(n\). For \(n=1\), \(Z_1(g)=g/(g+\kappa)\), whence \(g_c=d\).

**4. Quadratic long-path law.** Write \(\theta_n=\operatorname{arcosh}(1+\kappa/(2g_c(n)))\). The equality defining \(g_c\) becomes
\[
\frac{\cosh((n+1/2)\theta_n)}{\cosh(\theta_n/2)}=1+\frac{\kappa}{d}.
\]
The right side is fixed and greater than one, so \(\theta_n\to0\) and \((n+1/2)\theta_n\to L=\operatorname{arcosh}(1+\kappa/d)\). Finally \(g_c=\kappa/[2(\cosh\theta_n-1)]\sim\kappa/\theta_n^2\), proving the displayed limit.

**5. Exact, genuinely adverse example.** Set \(d=\kappa=\alpha=g=1\) and \(n=2\). The three living-node backward equations have solution \((p_s,p_{v_1},p_{v_2})=(3/7,2/7,3/7)\). The base probability is \(1/2\), so success drops by \(1/14\), even though conductance increases from \(1\) to \(4/3\). For \(n=2\) with \(d=\kappa=1\), the critical route rate is exactly \((3+\sqrt{13})/2\); it is independent of \(\alpha\).

## Verification

Run \(\texttt{python3 verify_corridor.py}\) using the bundled, standard-library-only script. The checker solves killed-network Dirichlet systems in exact rational arithmetic; checks the gateway identity and the sign equivalence on 270 parameter combinations; compares the explicit hyperbolic solution to additional rational systems; and tests illustrative critical-rate ordering and asymptotic behavior numerically. The checker reports 380 supplementary checks. The continuum-limit and universal sign proofs above are analytic, not inferred from numerical sampling.

## Relationship to prior work

Kervellec et al. (2024) place commute-time circuit distances inside spatial occupancy models and explicitly note that their construction does not include road mortality. The theorem above addresses a different mortality-limited endpoint-success quantity and a new-route design question, not that paper's calibrated occupancy model. Balakrishnan et al. (2019) develop mortal-walk trapping probabilities and one-dimensional backward equations; their methodology supports the isolated-path component, which is not claimed as an independent new idea. Gounaris and Katifori (2023) show that added shortcuts can worsen **mean first-passage-time** exploration objectives without independent mortality; that is distinct from the exact all-entry-rate mortality-success sign and the quadratic threshold proved here. Classical electrical Rayleigh monotonicity underlies the conductance comparison and is explicitly not claimed as original. The claimed contribution is the coupled gateway screening/length-threshold result under the stated corridor installation, including the exact source-success versus conductance discrepancy. The paper-comparison evidence supports provisional, not independently certified, priority.

## Limitations

This idealization assumes a single source, single absorbing destination, fixed rates, and spatially uniform mortality, and is not a field-calibrated ecological prediction. Adding a route introduces new nodes and rates; it is not the same intervention as only increasing an existing edge. Effective conductance is not commute time, and the theorem makes no claim that commute-time distance improves. At zero mortality, all finite connected routes yield eventual target success one and the strict paradox disappears. With node-dependent death, directional rates, deadline detection, or multiple sources, the homogeneous formulas and threshold may change. The literature search was targeted rather than exhaustive; general Markov-resolvent methods are acknowledged as prior mathematics, and an unlocated earlier special-case classification remains a historical-priority risk.

## References

1. Kervellec, M., Couturier, T., Bauduin, S., et al. (2024). *Bringing circuit theory into spatial occupancy models to assess landscape connectivity*. Methods in Ecology and Evolution. First published 2024-09-23. https://doi.org/10.1111/2041-210X.14418
2. Balakrishnan, V., Abad, E., Abil, T., and Kozak, J. J. (2019). *First-passage properties of mortal random walks: Ballistic behavior, effective reduction of dimensionality, and scaling functions for hierarchical graphs*. Physical Review E 99, 062110. First preprint 2019-01-29. https://arxiv.org/abs/1901.10226
3. Gounaris, G. and Katifori, E. (2023). *A Braess' paradox analog in physical networks of optimal exploration*. Preprint dated 2023-03-03. https://arxiv.org/pdf/2303.02146
4. Gómez, E. and Del Río, M. (2014). *Hitting Times of Walks on Graphs through Voltages*. 2014, 852481. https://doi.org/10.1155/2014/852481
