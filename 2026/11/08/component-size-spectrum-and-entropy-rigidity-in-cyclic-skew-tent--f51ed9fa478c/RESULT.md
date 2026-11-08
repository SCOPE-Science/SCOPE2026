# Component-size spectrum and entropy rigidity in cyclic skew-tent products

## Finding
Let \(k,n\ge2\) and let the skew-tent map \(h\) have \(k\) disjoint intervals \(I_0,\ldots,I_{k-1}\) on which \(h(I_i)=I_{i+1\bmod k}\). Let \(G\) be the cyclic product map
\[
G(z_1,\ldots,z_n)=(z_2,\ldots,z_n,h(z_1)).
\]
On the invariant core \(I^n\), where \(I=\bigcup_i I_i\), each product cell \(B_v=I_{v_1}\times\cdots\times I_{v_n}\), \(v\in(\mathbb Z/k\mathbb Z)^n\), maps to \(B_{\psi v}\) with \(\psi(v_1,\ldots,v_n)=(v_2,\ldots,v_n,v_1+1)\). For each orbit \(C\) of \(\psi\), write \(T_C=\bigcup_{v\in C}B_v\).

Define \(a\) as the largest divisor of \(n\) coprime to \(k\), and \(b=n/a\). **The complete set of component box-cycle lengths** is \(\{kbd:d\mid a\}\). For each divisor \(d\mid a\), there are exactly
\[
\boxed{M_d=\frac{1}{kbd}\sum_{e\mid d}\mu_{\rm Mob}(d/e)\,k^{be}}
\]
distinct \(\psi\)-orbits of length \(kbd\), where \(\mu_{\rm Mob}\) denotes the classical Möbius function. Every such multiplicity is positive.

Let \(\nu\) be an ergodic absolutely continuous invariant probability for \(h\) supported on \(I\). For each \(C\), condition the invariant product measure \(\nu^{\otimes n}\) on \(T_C\), obtaining \(\eta_C\). Then
\[
\boxed{\nu^{\otimes n}(T_C)=\frac{|C|}{k^n},\qquad
\mathbb P_{\nu^{\otimes n}}(|C|=kbd)
=\frac{\sum_{e\mid d}\mu_{\rm Mob}(d/e) k^{be}}{k^n}.}
\]
Despite the potentially unequal symbolic component sizes and selection weights, **every** \(\eta_C\) has the same metric entropy and the same \(n\) Lyapunov exponents (counted with multiplicity):
\[
\boxed{h_{\eta_C}(G)=\chi,\qquad
\lambda_1(\eta_C)=\cdots=\lambda_n(\eta_C)=\chi/n,
\qquad \chi:=\int_I\log|h'(z)|\,d\nu(z).}
\]
The measure \(\eta_C\) need not be asserted to be the global physical measure of an arbitrary perturbation; it is a canonical invariant probability on the exactly solvable unperturbed core.

In particular, with \(\omega(a)\) denoting the number of distinct prime divisors of \(a\), the fraction of stationary mass in shorter-than-maximum components satisfies
\[
0\le \mathbb P_{\nu^{\otimes n}}(|C|<kn)
\le\sum_{p\mid a\;\text{prime}} k^{-n(1-1/p)}
\le\omega(a)k^{-n/2}.
\]
For the three-coordinate four-band example, the census is one four-cell region of mass \(1/16\) and five twelve-cell regions, each of mass \(3/16\), yet all six carry the same entropy and Lyapunov spectrum under their conditioned stationary laws.

## Assumptions and scope
The map \(h(z)=a_Lz+1\) for \(z\le0\) and \(h(z)=a_Rz+1\) for \(z\ge0\) is taken with \((a_L,a_R)\) inside the parameter region \(S_k\) of Simpson, *Border-collision bifurcations from stable fixed points to any number of coexisting chaotic attractors* (2022), §6. In this region the core intervals are mutually disjoint, permuted cyclically by \(h\), and the return \(h^k\) is a piecewise expanding interval map (Simpson, Lemmas 6.2–6.3 and §10). Standard expanding-interval results supply an ergodic absolutely continuous invariant measure \(\nu\). In fact the conclusions about component masses hold for **any** invariant \(\nu\) supported on the cyclic intervals; the entropy and common-exponent conclusion is stated for an ergodic absolutely continuous one. Endpoints and preimages of the turning point have \(\nu\)-measure zero. All lengths \(|C|\) refer to the number of symbolic boxes in a component, not the minimal periods of individual real trajectories.

The equivalent map in Simpson's original coordinates is \(g(y_1,\ldots,y_n)=(y_2+1,\ldots,y_n+1,h(y_1)-1)\), under the translation \(z_1=y_1\), \(z_j=y_j+1\) for \(j\ge2\). The symbolic box-cycle census also applies to the trapping regions of the sufficiently small perturbed families in Simpson's §8, because their box permutation remains \(\psi\). The stationary probability and entropy formula do **not** purport to survive general perturbations.

## Proof
**1. Fixed points and allowed periods.** Direct iteration gives \(\psi^n v=v+\mathbf1\) modulo \(k\), hence \(\psi^{kn}=\mathrm{id}\). The sum of label coordinates increases by one modulo \(k\), so a fixed point of \(\psi^t\) forces \(k\mid t\). Write \(t=kj\), and \(s=\gcd(kj,n)\). Rotation of coordinates by \(t\) splits them into \(s\) cycles; in each, the cumulative affine shift equals \(kj/s\) modulo \(k\). Thus \(\psi^{kj}\) has fixed points precisely when \(s\mid j\), and in that case exactly \(k^s\) fixed points. The prime-factor calculation of Simpson's Lemma 9.4 says \(s\mid j\) exactly when \(b\mid j\). For \(j=bd\), \(d\mid a\), coprimality \(\gcd(a,k)=1\) yields \(s=b\gcd(d,a)=bd\), and therefore
\[
|\mathrm{Fix}(\psi^{kbd})|=k^{bd}.
\]
Every least period divides \(kn\) and is a multiple of \(kb\), so it has the form \(kbd\) for \(d\mid a\). Möbius inversion over the divisor lattice of \(a\) gives the number of points of exact least period \(kbd\) as \(\sum_{e\mid d}\mu_{\rm Mob}(d/e)k^{be}\); division by \(kbd\) gives \(M_d\).

An explicit structural explanation is available: \(\psi^{kb}\) rotates the \(n\) coordinates by \(kb\), creating \(b\) coordinate cycles of length \(a\). Its affine offsets sum to zero on each cycle because \((\psi^{kb})^a=\mathrm{id}\). A coordinatewise translation removes those offsets. Therefore \(\psi^{kb}\) is conjugate to a pure rotation of length-\(a\) words over an alphabet of cardinality \(k^b\). The inversion numerator is exactly the familiar number of primitive words of period \(d\), hence strictly positive. This conjugacy explains the arithmetic periods rather than merely counting them.

**2. Universal masses.** Since \(h(I_i)=I_{i+1}\) and \(\nu\) is invariant, all intervals have \(\nu(I_i)=1/k\). The product law \(\rho=\nu^{\otimes n}\) is \(G\)-invariant: \(G\) rotates coordinates and applies \(h\) to one coordinate. Each cell has \(\rho(B_v)=k^{-n}\). Since \(G\) permutes cells along \(\psi\)-orbits, each \(T_C\) is invariant and the restriction \(\eta_C=\rho(\cdot\cap T_C)/\rho(T_C)\) is invariant. Summing equal cell masses proves both probability formulas. Every coordinate's marginal under \(\eta_C\) is exactly \(\nu\): because \(\psi^n\) adds one to **every** label, every label occurs equally often in each coordinate among the cells of \(C\).

**3. Identical Lyapunov spectra.** The \(n\)-th iterate is \(G^n=(h,\ldots,h)\), with diagonal derivative almost everywhere. Under \(\eta_C\) every coordinate has marginal \(\nu\); since \(\nu\) is ergodic and \(\log|h'|\) integrable, Birkhoff's theorem holds simultaneously for all \(n\) coordinates. For \(G^{nm}\), each diagonal derivative grows at logarithmic rate \(\chi\) per \(m\), so all exponents per original \(G\)-iterate equal \(\chi/n\). Finitely many leftover iterates have uniformly bounded nonzero affine slopes, so do not change the limits.

**4. Identical entropy.** Define \(\nu_i=k\nu|_{I_i}\). Each is invariant under \(h^k\), and \(h_*\nu_i=\nu_{i+1}\). Factor monotonicity of metric entropy around the entire cyclic chain implies \(h_{\nu_i}(h^k)\) is independent of \(i\). Since \(\nu=(1/k)\sum_i\nu_i\) and \(h_\nu(h^k)=k h_\nu(h)\), every value is \(k h_\nu(h)\). The power \(G^{kn}\) preserves every cell and acts there as the product of \(n\) copies of \(h^k\). The conditional law on each cell is the product of the relevant \(\nu_i\)'s. Entropy additivity for product systems and affinity across finitely many invariant cells give \(h_{\eta_C}(G^{kn})=nk h_\nu(h)\). Division by \(kn\) yields \(h_{\eta_C}(G)=h_\nu(h)\). The Rokhlin–Pesin entropy formula for an absolutely continuous invariant measure of a piecewise expanding interval map yields \(h_\nu(h)=\int\log|h'|\,d\nu=\chi\).

**5. Short-cycle concentration.** The rotation conjugacy identifies a uniformly selected label with a uniformly selected word of length \(a\) over an alphabet of size \(k^b\). A nonprimitive word has a period dividing \(a/p\) for at least one prime \(p\mid a\), and there are at most \(k^{ba/p}\) such words for that \(p\). A union bound, divided by \(k^{ba}=k^n\), gives the stated bound. When \(a>1\), short cycles do occur, since the primitive-word numerator for \(d=1\) is positive. When \(a=1\), all symbolic components have the common length \(kn\).

## Verification
The standalone finite checker `verify.py` uses only Python standard libraries. It exhaustively enumerates the permutation \(\psi\) for 33 pairs \((k,n)\), with \(2\le k,n\le8\) and \(k^n\le15000\), totaling 36,490 labeled points; it agrees exactly with the Möbius formulas, probability normalization and the \((k,n)=(4,3)\) example. These finite tests do not prove the all-dimensional assertions or the entropy theorem; those follow from the arguments above and the stated expanding-map hypotheses. To run: `python3 verify.py`.

## Relationship to prior work
Simpson (2022), §§8–9, introduces exactly the label permutation and uses Burnside's lemma to calculate **the total number** of trapping regions. Its Lemmas 9.2–9.4 and Eq. (9.35) provide fixed-point counts from which the length census can be derived by standard Möbius inversion. The partial example of one four-box region and five twelve-box regions is also stated there; it is not new. The contribution here is the full length-by-length census **jointly with** canonical stationary component weights, exponentially small short-component mass, and common metric entropy and Lyapunov spectra across all regions. Neither this probabilistic/metric component classification nor its dimension-uniform comparison is stated in the inspected primary source. General necklace inversion, piecewise-expanding invariant-measure theory, entropy additivity, and the interval entropy formula are established mathematical tools and are not claimed as new.

## Limitations
Selection weights refer only to initial conditions sampled from the product of an invariant probability \(\nu\) of the unperturbed map on its invariant core. They are **not** claims about Lebesgue basin volumes in ambient phase space, noise-driven selection, or the perturbed systems. The Lyapunov statement is almost everywhere with respect to the corresponding conditioned stationary measure and requires an ergodic absolutely continuous \(\nu\) and nonzero branch derivatives. The theorem describes symbolic component lengths and stationary statistics, not primitive periods of individual chaotic trajectories. Source fixed-point counts nearly imply the bare length census; it should not be treated as a new inversion method. Literature-priority risk remains for equivalent component-entropy formulas in unindexed or inaccessible research.

## References
1. D. J. W. Simpson, *Border-collision bifurcations from stable fixed points to any number of coexisting chaotic attractors*, arXiv:2207.10251v1, first public 2022-07-21, especially §§5–9, 10 and 12. https://arxiv.org/abs/2207.10251
2. K. Cheng and K. Palmer, *On the dynamics of skew tent maps*, arXiv:1710.10880, 2017-10-30. https://arxiv.org/abs/1710.10880
3. A. Lasota and J. A. Yorke, *On the existence of invariant measures for piecewise monotonic transformations*, Transactions of the AMS **186** (1973), 481–488.
4. Standard results on metric entropy, product additivity and entropy formulas for piecewise-expanding interval maps are used in their classical form.
