# Sharp optimal dephasing on a trapped friendship quantum network

## Finding

For each integer \(m\ge3\), let \(F_m\) be the friendship graph of \(m\) triangles sharing one hub. Choose a peripheral trap vertex \(t\), and initialize one excitation at a peripheral vertex in a *different* triangle. Under unit uniform coherent hopping, uniform site-dephasing rate \(g>0\) (off-diagonal density-matrix entries decay at rate \(g\)), and irreversible population loss at the trap at rate \(2\), let \(T_m(g)\) denote the mean time to capture. Then every excitation is eventually captured, \(T_m(g)\) is finite, and

\[
\lim_{m\to\infty}\frac{T_m(z\sqrt m)}{m^{3/2}}
=F(z):=\frac{2(z^2+1)(z^2+2)}{z(3z^2+4)}\qquad(z>0).
\]

Moreover, the infimum over all positive dephasing rates is attained for each \(m\), and for **every** choice \(g_m^*\in\operatorname{argmin}_{g>0}T_m(g)\),

\[
\frac{g_m^*}{\sqrt m}\longrightarrow z_*=1.2269294870486\ldots,
\qquad
\frac{\min_{g>0}T_m(g)}{m^{3/2}}
\longrightarrow F(z_*)=1.6810198549942\ldots,
\]

where \(z_*\) is the unique positive solution of \(3z^6+3z^4-6z^2-8=0\). The finite-size mean also obeys the nonasymptotic inequalities

\[
T_m(g)\ge\frac{m^2}{4(g+1)},\qquad
T_m(g)\ge\frac{mg}{4}\qquad(m\ge3,\ g>0).
\]

This is a single fixed-normalization transport theorem; it is not an assertion about arbitrary trap rates, coupling weights, or quantum multi-excitation sectors.

## Assumptions and scope

Write the vertices as the hub \(h\), the trap \(t\), its pairmate \(p\), and \(2(m-1)\) generic peripherals \(b_{j,0},b_{j,1}\), with edges \(ht,hp,tp\) and \(hb_{j,0},hb_{j,1},b_{j,0}b_{j,1}\) for each \(1\le j\le m-1\). Let \(A_m\) be this graph's unweighted adjacency matrix and \(P=|t\rangle\langle t|\). On the one-excitation site Hilbert space the trace-decreasing Lindblad equation is

\[
\frac{d\rho}{ds}=\mathcal L_g(\rho):=
-i[A_m,\rho]
+g\left(\sum_v P_v\rho P_v-\rho\right)
-\{P,\rho\},\qquad P_v=|v\rangle\langle v|.
\]

The initial state is \(\rho(0)=|b_{1,0}\rangle\langle b_{1,0}|\); all different-triangle peripheral starting vertices have the same law by symmetry. The capture-time survival probability is \(\operatorname{Tr}\rho(s)\) and the mean is \(T_m(g)=\int_0^\infty\operatorname{Tr}\rho(s)\,ds\). Time and energy are dimensionless, with \(\hbar=1\), hopping magnitude one, and trap population loss rate two. No population decay occurs anywhere else.

## Proof

**Existence of the mean.** For any complex matrix \(X\), the real Hilbert–Schmidt quadratic form of \(\mathcal L_g\) is nonpositive: the commutator is skew-adjoint, site dephasing contributes \(-g\sum_{v\ne w}|X_{vw}|^2\), and the trap contribution is \(-\|PX\|_F^2-\|XP\|_F^2\). An eigenvector with an eigenvalue of nonnegative real part would therefore have no off-diagonal entries and would vanish in the trap row and column. Its commutator with \(A_m\) would then require all diagonal entries to agree across every edge. Connectivity and the zero trap diagonal force \(X=0\), a contradiction. Thus \(\mathcal L_g\) is strictly stable for every \(g>0\), and the integrated operator satisfies \(\mathcal L_g(X)=-\rho(0)\), with \(T_m(g)=\operatorname{Tr}X\).

**Exact symmetry reduction.** Average the initial density matrix over permutations of the other \(m-1\) triangles and independent swaps of the two sites in each. The resulting initial matrix has diagonal value \(1/[2(m-1)]\) on every generic peripheral. Linearity and invariance of the trace mean the same capture time is obtained. The Hermitian matrices invariant under those automorphisms have exactly eighteen real coordinates: four site-orbit diagonals; real and imaginary parts of the six off-diagonal orbit classes \(tp,th,ph,tb,pb,hb\); and two real peripheral–peripheral orbit classes, namely within-pair and between-pair. The displayed generator preserves this space. Denote its real generator matrix by \(M(m,g)\), with basis and coefficient construction given explicitly in `verify_friendship.py`. With its fourth coordinate indexing the common generic diagonal, let \(e_b\) be that coordinate vector and \(w=(1,1,1,2(m-1),0,\ldots,0)^\top\). Then

\[
T_m(g)=-\frac{1}{2(m-1)}w^\top M(m,g)^{-1}e_b.
\]

Each coefficient of \(M\) is affine in \(m\), because each term in the commutator changes only one site index and sums at most once over the other triangles. The remaining generator terms do not sum over triangles. Accordingly \(M(m,g)\) is determined **exactly** by the two concrete cases \(m=3,4\), separately for the Hamiltonian, dephasing, and sink operators. The supplied checker constructs all eighteen orbit basis matrices directly, obtains the exact symbolic \(M\), and performs rational matrix inversion; no asymptotic or sampled-size interpolation is used in place of this structural argument.

**Polynomial identity and limits.** Rational elimination yields \(T_m(g)=N(m,g)/D(m,g)\), where both are exact integer-coefficient polynomials, with the denominator including the factors \(2g(g+1)\). Both \(N(m,g)\) and \(D(m,g)\) have nonnegative coefficients upon expansion in \(g\) and \(y=m-2\), and \(D(m,g)>0\) for \(m\ge3,g>0\). The checker gives the complete reproducible polynomial identity and certifies every coefficient, rather than assuming numerical positivity. In the scaling \(g=z\sqrt m\), the leading terms are

\[
\begin{aligned}
\frac{N(m,z\sqrt m)}{m^{13/2}}&\longrightarrow
4z^{11}+28z^9+72z^7+80z^5+32z^3,\\
\frac{D(m,z\sqrt m)}{m^5}&\longrightarrow
2z^2(3z^8+16z^6+28z^4+16z^2).
\end{aligned}
\]

Their quotient is the claimed \(F(z)\). The same exact polynomial identity proves \(\lim_{g\downarrow0}gT_m(g)=2m-3\) and \(\lim_{g\to\infty}T_m(g)/g=(2m+1)/3\) for fixed \(m\), so a minimizer exists. Crucially, coefficientwise nonnegative polynomial identities in \(g\) and \(y=m-2\) certify both

\[
(g+1)N-\frac{m^2}4D\ge0,
\qquad N-\frac{mg}{4}D\ge0.
\]

These are exact finite algebraic certificates, reproduced by the attached code. They imply that any near-minimizing sequence with \(g/\sqrt m\to0\) or \(g/\sqrt m\to\infty\) has \(T_m(g)/m^{3/2}\to\infty\). On compact subintervals of \(0<z<\infty\), rational polynomial scaling converges uniformly to \(F(z)\), so all minimizers have asymptotically finite positive scaled rates. Finally,

\[
F'(z)=\frac{2(3z^6+3z^4-6z^2-8)}{z^2(3z^2+4)^2}.
\]

The numerator as a cubic in \(z^2>0\) has exactly one positive root (one sign change in descending coefficients and opposite signs at zero and infinity). Hence \(z_*\) uniquely minimizes \(F\), proving both optimizer and optimum limits.

## Verification

Run `OPENBLAS_NUM_THREADS=1 python verify_friendship.py` with NumPy, SciPy and SymPy installed. Its exact symbolic rational operations reconstruct the generator and integrated mean, derive both polynomial coefficient-positivity certificates, establish the scaling identity and endpoint limits, and check the derivative. Independently, for fifteen parameter choices with \(3\le m\le7\), it builds and solves the entire complex \((2m+1)^2\)-dimensional Liouvillian from scratch, comparing the physical trace mean with the orbit-reduced result to tolerance \(10^{-7}\). The finite comparisons are cross-checks only: the all-size proof rests on the exact symbolic identities and the orbit-invariance argument, not on these tests.

## Relationship to prior work

Plenio–Huelga established the dephasing-assisted transport phenomenon for coherent networks. Caruso–Chin–Datta–Huelga–Plenio derived a symmetry-based exact solution for a **fully connected** network and explored dark-state release by noise. The present result concerns a graph with only triangles coupled through one hub and a peripheral sink. Fully connected formulas do not supply its eighteen-orbit generator, sharp scaling function, or optimal coefficient. Prior exact dephased star calculations involve **no peripheral–peripheral bonds**; their strong-hub asymptotics do not imply the distinct friendship-network function \(F\) or its minimizing constant. The mathematical distinction is explicit in the extra within-triangle and between-triangle matrix orbits.

## Limitations

The theorem fixes uniform unit adjacency hopping, trap population loss rate two, and the exact site-dephasing convention written above. It addresses the mean capture time, not its full distribution, time-dependent transient efficiency, arbitrary nonuniform noise, or multi-particle quantum transport. The coefficient-based rational identities are provided as a reproducible finite computation. Full historical priority is not claimed; equivalent specialized formulas could exist outside the examined sources. No independent audit has been performed.

## References

1. M. B. Plenio and S. F. Huelga, *Dephasing assisted transport: Quantum networks and biomolecules*, arXiv:0807.4902, first posted 2008-07-30. https://arxiv.org/abs/0807.4902
2. F. Caruso, A. W. Chin, A. Datta, S. F. Huelga and M. B. Plenio, *Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport*, arXiv:0901.4454, first posted 2009-01-28. https://arxiv.org/abs/0901.4454
3. S. Lloyd and M. Mohseni, *Symmetry-enhanced supertransfer of delocalized quantum states*, arXiv:1005.2579, first posted 2010-05-14. https://arxiv.org/abs/1005.2579
