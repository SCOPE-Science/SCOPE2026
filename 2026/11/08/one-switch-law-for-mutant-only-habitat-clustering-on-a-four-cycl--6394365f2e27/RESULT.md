# One-switch law for mutant-only habitat clustering on a four-cycle

## Finding

A finite birth–death Moran population inhabits the four-cycle \(C_4\). Two sites give mutant fecundity \(r>0\), and the other two give mutant fecundity \(s>0\); **all resident fecundities equal one**. Let \(\rho_C(r,s)\) be the fixation probability when the two \(r\)-sites are adjacent, and \(\rho_A(r,s)\) when they alternate. In each case the initial single mutant is uniformly distributed among the four vertices. These are the only two site arrangements up to graph automorphism.

Put \(u=r+s\), \(v=rs\), and
\[
\begin{aligned}
B(u,v)={}&2u^4+3u^3v+6u^3+2u^2v^2+2u^2v+9u^2+12u+4v+8,\\
P(u,v)={}&uv^2-5uv-2u^2-3u-2v^2-4v.
\end{aligned}
\]
Then \(B(u,v)>0\), and the **exact fixation-probability difference** is
\[
\boxed{\rho_C(r,s)-\rho_A(r,s)
=-\frac{(r-s)^2(r+s+1)P(r+s,rs)}
{2(r+1)(s+1)(rs+1)B(r+s,rs)}.}
\]
The alternating arrangement has the closed form
\[
\rho_A(r,s)=\frac{rs(2rs+r+s)}{2(r+1)(s+1)(rs+1)}.
\]

For a precise complete ordering, write \(h=\max\{r,s\}\), \(\ell=\min\{r,s\}\). For \(h>\ell\), define
\[
F_\ell(h)=\ell^2h^3+(\ell^3-2\ell^2-5\ell-2)h^2
-(5\ell^2+8\ell+3)h-2\ell^2-3\ell.
\]
Let \(\ell_c\) be the **unique positive root** of \(\ell^3-2\ell^2-3\ell-3=0\), approximately \(3.22069281998732\). For every \(0<\ell<\ell_c\), there exists a **unique** \(h_*(\ell)>\ell\) with \(F_\ell(h_*)=0\). The complete strict order is
\[
\begin{cases}
\rho_C>\rho_A,&\ell<h<h_*(\ell),\\
\rho_C=\rho_A,&h=h_*(\ell),\\
\rho_C<\rho_A,&h>h_*(\ell).
\end{cases}
\]
For \(\ell\ge\ell_c\), \(\rho_C<\rho_A\) for every \(h>\ell\). When \(r=s\), the arrangements are identical and \(\rho_C=\rho_A\).

For illustration, at \(\ell=1\) the crossover is the unique positive root of \(h^3-8h^2-16h-5=0\), approximately \(9.70222288403181\). Thus for \((r,s)=(2,1)\), \(\rho_C=579/1454>7/18=\rho_A\), but for \((10,1)\), \(\rho_C=44825/70058<155/242=\rho_A\). The same mutant-fitness multiset can therefore favor either clustered or alternating sites, depending on the magnitude of the fitness contrast.

## Assumptions and scope

Vertices are \(0,1,2,3\), with undirected edges \(01,12,23,30\). At each discrete step, choose a reproducing vertex in proportion to the fecundity of its current type at that vertex, then replace one of its two neighboring individuals with equal probability. Mutant fecundity is permanently fixed at \(r\) or \(s\) by the vertex, while resident fecundity is \(1\) everywhere. No mutation occurs after initialization; \(0\) mutants and \(4\) mutants are absorbing. All parameter values in the theorem are strictly positive, and no selection-strength or approximation restriction is imposed. The result does not apply to death–birth updating or to environmental effects shared by mutant and resident.

## Proof

**1. Exact first-step equations.** Index states by the mutant mask \(M\subseteq\{0,1,2,3\}\). Set \(p(\varnothing)=0\) and \(p(\{0,1,2,3\})=1\). For every other mask let \(f_i(M)=r\) or \(s\) if \(i\in M\), according to its habitat, and let \(f_i(M)=1\) if \(i\notin M\). The exact harmonic equation is
\[
\sum_{i=0}^{3}f_i(M)\sum_{j\sim i}
\bigl(p(M^{i\to j})-p(M)\bigr)=0,
\]
where \(M^{i\to j}\) replaces the type at \(j\) by the type at \(i\). The positive total-fecundity normalization and common factor \(1/2\) cancel in this equation; same-type replacements give zero terms. Because all rates for type-changing edges are positive and the graph is connected, every mixed state is transient and the Dirichlet solution is unique.

**2. Exact rational reduction.** Under the habitat-preserving symmetry group, adjacent coloring has eight nonabsorbing state orbits; alternating coloring has seven. The orbits, integer-weight first-step matrices, exact elimination, and a separate uncompressed fourteen-state calculation are constructed from the preceding harmonic equation in `verify.py`. Solving those finite exact systems gives
\[
\rho_A(r,s)=\frac{rs(2rs+r+s)}{2(r+1)(s+1)(rs+1)}
\]
and, by subtracting the adjacent solution and factoring its numerator, the displayed expression for \(\rho_C-\rho_A\). This is an exact rational-function identity, not a fitted polynomial: the checker symbolically reconstructs and cancels both sides of the identity, then independently solves the full state space at rational parameter choices. The orbit lists also permit direct hand reconstruction of each linear equation. Each probability is the average of the four one-mutant starting-state probabilities.

**3. Sign and uniqueness.** For \(r,s>0\), we have \(u,v>0\), so every term of \(B(u,v)\) is nonnegative and its constant term is positive. All remaining factors in the denominator are positive, and \((r-s)^2(r+s+1)>0\) whenever \(r\ne s\). Thus \(\operatorname{sgn}(\rho_C-\rho_A)=-\operatorname{sgn}F_\ell(h)\). Expansion with \(r=h,s=\ell\) gives the displayed cubic \(F_\ell(h)\). For fixed \(\ell>0\), its coefficients in descending powers of \(h\) have signs \((+,\pm,-,-)\). By Descartes' rule they have exactly one sign change; since \(F_\ell(0)<0\) and its leading coefficient is \(\ell^2>0\), **exactly one positive root exists** and its sign changes from negative to positive there. On the diagonal,
\[
F_\ell(\ell)=2\ell(\ell+1)(\ell^3-2\ell^2-3\ell-3).
\]
The final cubic has precisely one positive root by the same sign-change and continuity argument. Consequently the unique root of \(F_\ell\) lies above \(\ell\) exactly when \(\ell<\ell_c\); otherwise it lies at or below \(\ell\). These observations give the complete cases and all equality conditions. At \(r=s\), the numerator of the difference vanishes identically. \(\square\)

## Verification

Run `python3 verify.py` with Python 3 and SymPy. The standalone checker constructs the update equations directly, performs exact symbolic elimination after orbit compression, checks the full rational identity and bifurcation factorization, and separately reconstructs the full fourteen-state transient matrix for seventeen parameter pairs with exact arithmetic. It passed 77 exact assertions. These computations provide a reproducible finite rational identity and diagnostic cross-check; the universal ordering and unique-root statements follow analytically from the positivity and Descartes arguments above, not from a finite parameter sample.

## Relationship to prior work

Maciejewski and Puleo (2013) introduced site-dependent fecundity on colored graphs and demonstrated that habitat arrangement can affect evolutionary fate, but in their two-color matching-reward model **both types** receive a site-dependent benefit tied to genotype–color matching, rather than mutants alone changing fecundity while residents remain at one. Alcalde Cuesta and collaborators (2015) explain exact finite Moran absorption calculations but do not establish this heterogeneous site-color arrangement classification.

Kaveh, McAvoy and Nowak (2017/2019) study mutant-specific fitness variation and in Appendix B explicitly restrict their illustrative cycle calculations to **alternating habitats**, leaving the contrast with adjacent habitats undetermined. Kaveh, McAvoy, Chatterjee and Nowak (2020) derive an exact properly colored formula, which covers \(\rho_A\) under the present parameters, and compare proper and non-proper cyclic colorings numerically under **symmetric background fitness effects on both types**. Their stated cycle-optimality observation for that distinct parameter family does not imply an ordering for mutant-only variation, nor this unique algebraic switch. The claimed additional result here is the exact clustered-versus-alternating comparison and full phase classification, **not** an independently new formula for properly colored graphs.

## Limitations

This is a complete classification on the **smallest even cycle with two habitats of each quality**, not a theorem for arbitrary cycle lengths, evolutionary games with frequency dependence, environments changing over time, or empirically measured populations. The only new priority claim is the specific exact comparison and phase diagram. Although relevant open primary texts were examined, unindexed or older literature may contain equivalent identities; no claim of exhaustive historical coverage is made.

## References

1. Maciejewski, W. and Puleo, G. J., *Environmental Evolutionary Graph Theory* (first public 2013-11-13), https://arxiv.org/abs/1311.3214.
2. Alcalde Cuesta, F., González Sequeiros, P. and Lozano Rojo, Á., *Fast and asymptotic computation of the fixation probability for Moran processes on graphs* (first public 2015-01-26), https://arxiv.org/abs/1501.06342.
3. Kaveh, K., McAvoy, A. and Nowak, M. A., *Environmental fitness heterogeneity in the Moran process* (first public 2017-09-10), https://arxiv.org/abs/1709.03031, https://doi.org/10.1098/rsos.181661.
4. Kaveh, K., McAvoy, A., Chatterjee, K. and Nowak, M. A., *The Moran process on 2-chromatic graphs* (2020), https://doi.org/10.1371/journal.pcbi.1008402.
