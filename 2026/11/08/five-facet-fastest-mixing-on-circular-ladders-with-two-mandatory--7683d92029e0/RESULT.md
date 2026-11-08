# Five-facet fastest mixing on circular ladders with two mandatory edge flows

## Finding

For each integer \(m\ge 4\), consider the circular ladder (prism graph) \(G_m=C_m\square K_2\) with \(2m\) vertices. Let \(P\) range over all real symmetric, entrywise nonnegative, row-stochastic matrices with nonzero off-diagonal entries permitted only on edges of \(G_m\). Require, separately, \(P_{uv}\ge\tau\) on **every** rim edge and \(P_{uv}\ge\eta\) on **every** rung edge. Here \(\tau,\eta\ge0\) and \(2\tau+\eta\le1\); these conditions are necessary and sufficient for nonempty feasibility.

Write
\[
a=2-2\cos(2\pi/m),\qquad
b=2-2\cos\!\left(\frac{2\pi\lfloor m/2\rfloor}{m}\right).
\]
The globally smallest second-largest eigenvalue modulus, with the trivial eigenvalue \(1\) excluded by one dimension even if other eigenvalues equal \(1\), is
\[
\boxed{\mu_m^*(\tau,\eta)=\max\!\left\{
\frac{b}{b+2a},\quad
\frac{b\tau}{2},\quad
\frac{b-a+2a\eta}{a+b},\quad
4\tau-1,\quad
b\tau+2\eta-1
\right\}.}
\]
An attaining matrix has a constant rim transition probability \(r\), a constant rung transition probability \(v\), and holding probability \(1-2r-v\), where, setting \(t=\mu_m^*(\tau,\eta)\),
\[
r=\max\!\left\{\tau,\frac{1-t}{a}\right\},\qquad
v=\max\!\left\{\eta,\frac{1-t}{2}\right\}.
\]
Each of the five displayed affine/constant lower bounds defines a genuinely active region when \(m\) is odd. For even \(m\), the bound \(4\tau-1\) is redundant everywhere, and each of the remaining four bounds is genuinely active. This parity distinction results from the presence, or absence, of the cycle's eigenvalue \(4\).

## Assumptions and scope

The graph is simple, unweighted, undirected, and has two cyclic layers with corresponding vertices joined by rungs. The optimization variable is the **whole** symmetric stochastic matrix, not only matrices assumed beforehand to share equal probabilities along each edge type. Self-loops are allowed and required to be nonnegative; no transitions outside graph edges or the diagonal are permitted. Both edge floors apply to every individual edge, not only to an average. The stationary distribution is uniform. The result concerns second-largest eigenvalue **modulus** (SLEM), not the second-largest eigenvalue without absolute value, finite-time total-variation mixing, or an arbitrary nonuniform stationary distribution. Boundary values, including disconnected or periodic optimal chains, are included with SLEM \(1\) where appropriate.

## Proof

**1. Global reduction without assuming symmetry of an optimizer.** The dihedral rotations/reflections of the cycle and interchange of its two layers preserve both edge classes and their floors. The SLEM objective is the spectral norm \(\lVert P-\Pi\rVert_2\), where \(\Pi\) is the uniform averaging projection. Thus it is convex and invariant under simultaneous row/column permutation. Averaging any feasible \(P\) over the displayed graph symmetries produces a feasible matrix of no larger SLEM, constant on rim edges, rung edges, and diagonal entries. The global optimum therefore equals the two-variable optimum with \(r\ge\tau\), \(v\ge\eta\), and \(2r+v\le1\).

**2. Exact spectral reduction.** For such an averaged matrix,
\[
P=I-r(L_{C_m}\otimes I_2)-v(I_m\otimes L_{K_2}).
\]
The Fourier eigenvalues are \(1-r a_k-2\varepsilon v\), where \(a_k=2-2\cos(2\pi k/m)\) and \(\varepsilon\in\{0,1\}\). The smallest positive cycle eigenvalue is \(a\), and the largest is \(b\). Since \(0\le r\le1/2\), \(a\le2\), and the excluded trivial constant mode is \((k,\varepsilon)=(0,0)\), the SLEM is exactly
\[
\mu(r,v)=\max\{1-ar,\,1-2v,\,br+2v-1\}.
\]
No intermediate cycle Fourier eigenvalue can dominate either endpoint.

**3. Five necessary bounds.** Suppose \(\mu(r,v)\le t\). Then
\[
ar\ge1-t,\qquad 2v\ge1-t,\qquad br+2v\le1+t.
\]
The first two inequalities combined with the third give \(t\ge b/(b+2a)\). Using \(r\ge\tau\) with the second and third gives \(t\ge b\tau/2\). Using \(v\ge\eta\) with the first and third gives \(t\ge(b-a+2a\eta)/(a+b)\). Using \(r\ge\tau\), the second inequality and \(2r+v\le1\) gives \(t\ge4\tau-1\). Finally, both floors with the third inequality give \(t\ge b\tau+2\eta-1\).

**4. All five bounds together suffice.** Elementary trigonometry shows \(a+b>4\). Indeed, for even \(m\), \(b=4\) and \(a>0\). For odd \(m\ge5\), \(b=2+2\cos(\pi/m)\) and \(a=2-2\cos(2\pi/m)\), so \(a+b=4+2[\cos(\pi/m)-\cos(2\pi/m)]>4\).

Set \(t\) equal to the maximum of the five bounds and define \(r,v\) by the formulas in the Finding. Because \(2\tau+\eta\le1\), all five bounds are at most \(1\), so \(0\le t\le1\). By construction, the two positive-eigenvalue inequalities hold. To verify the third inequality, expand \(br+2v\) as the maximum of the four numbers
\[
b\tau+2\eta,\quad b\tau+1-t,\quad
\frac{b(1-t)}{a}+2\eta,\quad
\left(1+\frac ba\right)(1-t).
\]
Each is at most \(1+t\), respectively by the fifth, second, third and first bounds.

Similarly, \(2r+v\) is the maximum of
\[
2\tau+\eta,\quad 2\tau+\frac{1-t}{2},\quad
\frac{2(1-t)}{a}+\eta,\quad
\left(\frac2a+\frac12\right)(1-t).
\]
The first is at most \(1\) by feasibility, the second by the fourth bound. The third follows because the third bound implies \(t\ge 1-2a(1-\eta)/(a+b)\ge 1-a(1-\eta)/2\). The fourth follows because the first bound implies \(t\ge b/(b+2a)\ge(4-a)/(4+a)\). The final two comparisons use \(a+b\ge4\). Hence \(2r+v\le1\), all matrix entries are nonnegative, and \(\mu(r,v)\le t\). The lower bounds force equality. This proves the all-parameter formula and attainment.

**5. Every claimed facet is necessary.** Let \(r_* =2/(b+2a)\), \(v_*=a/(b+2a)\), and \(t_*=b/(b+2a)\). At \((\tau,\eta)=(0,0)\), only the constant facet is maximal. Along \(\eta=0\), any \(\tau\in(r_*,2/(8-b))\) makes the rim-only facet strictly maximal; this interval is nonempty since \(a+b>4\). Along \(\tau=0\), any \(\eta\in(v_*,1)\) makes the rung-only facet strictly maximal. Because \(2r_*+v_*<1\), for all sufficiently small positive \(\varepsilon\), taking \(\tau=r_*+\varepsilon\) and \(\eta=v_*+\varepsilon\) makes the joint-floor facet strictly maximal. If \(m\) is odd, \(b<4\); at \((\tau,\eta)=(1/2,0)\) the remaining facet \(4\tau-1=1\) strictly exceeds the other four. If \(m\) is even, \(b=4\), so \(4\tau-1\le 2\tau=b\tau/2\) throughout the feasible triangle; hence this facet is redundant and all four others remain essential.

## Verification

The included `verify.py` uses only the Python standard library and exact arithmetic in \(\mathbb Q(\sqrt5)\). It checks \(1323\) feasible rational pairs of floors for each of the graph sizes \(m=4,5,6\) combined, compares the five-facet value against the computed invariant eigenvalue extrema, constructs the attaining probabilities, and checks the constraints exactly. At five representative pairs per graph, it also builds the full stochastic matrix and checks its Fourier-mode eigenvector equations entry by entry (\(150\) mode checks). Exact witness tests confirm strict activation of all five facets for \(m=5\), all four essential facets for \(m=4,6\), and redundancy of the parity facet on even instances. Run `python3 verify.py` in the same directory as this document; it prints `VERIFY_OK` on success. These are finite checks supplementing, not replacing, the analytic global proof.

As an exact example of the joint-floor regime, on \(m=5\) at \(\tau=17/50\) and \(\eta=1/4\), the joint facet is strictly active and
\[
\mu_5^*\!\left(\frac{17}{50},\frac14\right)
=\frac{35+17\sqrt5}{100}=0.7301315561\ldots.
\]

## Relationship to prior work

Boyd, Diaconis and Xiao formulated the global fastest-mixing Markov-chain problem as a convex semidefinite optimization problem [1]. Boyd, Diaconis, Parrilo and Xiao developed automorphism averaging, Cartesian-product Laplacian spectra, and explicit unrestrained examples, including cycles and tori [2]. Their results supply both the correct global optimization framework and the spectral reduction used here; their section on Cartesian products does not give the two-mandatory-edge-floor five-facet formula or its odd/even facet classification on prisms. More recent work on constrained transition probabilities on friendship graphs studies another nonisomorphic family and does not imply this formula [3]. An independent full-text prism-spectrum study provides unweighted structural Laplacian spectra and derived graph indices, not the two-edge-floor transition optimization [4]. The present claim is an exact constrained prism specialization, not a new general convexity principle or a general method for all graphs.

## Limitations

The formula optimizes SLEM for symmetric stochastic chains with uniform stationary measure and pointwise lower floors of the two designated types. It does not classify every nonsymmetric-invariant optimizer, nor does it apply directly to arbitrary transition asymmetry, nonuniform stationary distributions, cylindrical ladders with open ends, or the finite-time total-variation mixing time. Numerical checks for finitely many \(m\) do not independently establish the all-\(m\) theorem; that conclusion rests on the displayed analytic proof. Publication priority beyond the inspected primary sources and search records has not been independently established.

## References

[1] S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. DOI: 10.1137/S0036144503423264. Author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.

[2] S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, first public arXiv version September 6, 2007, arXiv:0709.0955v1; SIAM Journal on Optimization 20 (2009), 792–819. DOI: 10.1137/070689413. Full text: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.

[3] S. Jafarizadeh, *Fastest mixing reversible Markov chain on friendship graph: Trade-off between transition probabilities among friends and convergence rate*, arXiv:2501.02117v1 (2025). Full text: https://arxiv.org/abs/2501.02117.

[4] A. Raza, M. Munir, T. Abbas, S. M. Eldin, I. Khan, *Spectrum of prism graph and relation with network related quantities*, AIMS Mathematics 8 (2023), 2634–2647, published online November 8, 2022. DOI: 10.3934/math.2023137. Full text: https://www.aimspress.com/aimspress-data/math/2023/2/PDF/math-08-02-137.pdf.
