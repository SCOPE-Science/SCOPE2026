# Compound-Poisson jump doublets in two-particle exclusion on friendship networks

## Finding
Let \(W_m=K_1\vee(mK_2)\), the friendship graph of \(m\ge2\) triangles with one common hub. Run continuous-time symmetric simple exclusion with exactly two indistinguishable particles, with rate one on each occupied-to-vacant oriented edge. Start from the uniform stationary law on unordered pairs and let \(C_m(t)\) count all successful jumps in \([0,t]\), including jumps that do not change the symmetry class of the occupied pair. Then
\[
\mu_m:=\lim_{t\to\infty}\frac{\mathbb E C_m(t)}t=\frac{6(2m-1)}{2m+1},\qquad
F_m:=\lim_{t\to\infty}\frac{\operatorname{Var}(C_m(t))}{\mathbb E C_m(t)}=
\frac{40m^3-52m^2+110m-71}{3(2m-1)(2m+1)^2}.
\]
The sequence \((F_m)_{m\ge2}\) is **strictly increasing**, with \(F_2=29/25\) and \(F_m\uparrow5/3\); in particular its long-time activity is always super-Poissonian. More strongly, for every fixed \(t\ge0\),
\[
 C_m(t)\ \xrightarrow[m\to\infty]{\mathrm{law}}\ P_1(t)+2P_2(t),
 \qquad P_1(t),P_2(t)\ \text{independent}\ \operatorname{Poisson}(2t).
\]
The limiting fixed-time moment-generating function is
\[
 \lim_{m\to\infty}\mathbb E e^{zC_m(t)}=
 \exp\bigl[t\{2(e^z-1)+2(e^{2z}-1)\}\bigr],\qquad z\in\mathbb R.
\]
This is a compound-Poisson **marginal-count** limit: the multiplicity-two jumps arise from rapid arrivals at and departures from the increasingly high-degree hub. No convergence in the Skorokhod \(J_1\) topology is asserted.

## Assumptions and scope
Write the vertex set as a hub \(0\) and blades \(\{a_i,b_i\}\), \(1\le i\le m\). Edges are \(0a_i\), \(0b_i\), and \(a_ib_i\). A configuration is an unordered pair of distinct occupied vertices. Every legal edge exchange occurs at its own independent rate-one exponential clock. Rejected attempts are excluded from \(C_m\). The configuration chain is finite and irreducible; symmetric jumps give the uniform stationary distribution on \(\binom{2m+1}{2}\) configurations. Limits in observation time and graph size are distinguished explicitly: the definition of \(F_m\) takes \(t\to\infty\) at fixed \(m\); the compound-Poisson statement takes \(m\to\infty\) at fixed \(t\).

## Proof
**1. Three orbit classes, including internal counted jumps.** Under permutations of blades and swaps within blades, there are exactly three occupied-pair types: \(A\) (hub and one peripheral vertex), \(B\) (two ends of one peripheral edge), and \(C\) (peripheral vertices from distinct blades). Their respective counts are \(2m,m,2m(m-1)\), so their stationary probabilities are
\[
\pi_m=\frac{1}{2m+1}(2,1,2m-2).
\]
Counting **all** legal exchanges, even those within the same orbit, gives the transition-count matrix and exit intensities
\[
T_m=\begin{pmatrix}1&1&2m-2\\2&0&0\\2&0&2\end{pmatrix},
\qquad r_m=T_m\mathbf1=\begin{pmatrix}2m\\2\\4\end{pmatrix}.
\]
For example, the first diagonal entry records moving the peripheral particle across its blade edge while the hub remains occupied; the last diagonal entry records the two blade-edge moves with particles in different blades. Thus the Markov generator on orbit functions is \(Q_m=T_m-\operatorname{diag}(r_m)\), whereas the **count-tilted** generator is
\[
L_m(z)=e^zT_m-\operatorname{diag}(r_m).
\]
Omitting the diagonal of \(T_m\) would incorrectly discard actual jumps. The orbit partition is strongly lumpable, including the marked count, since every state of a given type has the same transition-count rates to every type.

**2. Exact mean and variance.** The mean event rate is \(\mu_m=\pi_mr_m=6(2m-1)/(2m+1)\). Set \(f_m=r_m-\mu_m\mathbf1\) and solve \(-Q_mh_m=f_m\) subject to \(\pi_m h_m=0\). Direct substitution gives
\[
h_m=\frac{1}{(2m+1)^2}
\begin{pmatrix}
2(m-1)(2m-3)\\-2(m-1)(2m+5)\\11-2m
\end{pmatrix}.
\]
The maximal eigenvalue of \(L_m(z)\) near zero is analytic and produces the long-time counting cumulants. Differentiating the right-eigenvector equation at zero and using reversibility of the **underlying full chain** gives
\[
\lim_{t\to\infty}\frac{\operatorname{Var}(C_m(t))}{t}
=\mu_m+2\sum_{X\in\{A,B,C\}}\pi_m(X)f_m(X)h_m(X).
\]
The orbit reduction is valid for this formula because both \(f_m\) and its mean-zero Poisson solution are class-constant. Substitution and simplification yield the displayed \(F_m\). Independently, for \(y=e^z\) and spectral variable \(\lambda\),
\[
\begin{aligned}
\det(\lambda I-L_m(z))={}&\lambda^3+(2m-3y+6)\lambda^2\\
&+(12m+8-4my^2-4my+4y^2-10y)\lambda\\
&+16m-8my^2-8my+4y^3+4y^2-8y.
\end{aligned}
\]
At \(y=1\) this factors as \(\lambda(\lambda+2)(\lambda+2m+1)\), so the zero eigenvalue is simple. Implicit differentiation reproduces the same first two cumulants.

**3. Sharp monotonicity.** Exact factorization yields
\[
F_m-1=\frac{4(m-1)(4m^2-12m+17)}{3(2m-1)(2m+1)^2}>0,
\]
where \(4m^2-12m+17=(2m-3)^2+8\). Moreover
\[
F_{m+1}-F_m=\frac{4(2m-3)(12m^2-4m-17)}{(2m-1)(2m+1)^2(2m+3)^2}>0
\]
for every integer \(m\ge2\). The rational formula immediately gives \(\lim_{m\to\infty}F_m=5/3\).

**4. Compound-Poisson fixed-time limit.** Fix real \(z\) and set \(y=e^z>0\). The vector \(u_m(t)=e^{tL_m(z)}\mathbf1\) has nonnegative entries and satisfies
\[
\begin{aligned}
\dot u_A&=-(2m-y)u_A+yu_B+(2m-2)yu_C,\\
\dot u_B&=2yu_A-2u_B,\\
\dot u_C&=2yu_A+(2y-4)u_C,
\end{aligned}
\qquad u_A(0)=u_B(0)=u_C(0)=1.
\]
For any fixed finite time horizon \(T\) and all sufficiently large \(m\), variation of constants in the first equation, followed by Grönwall's inequality for the last two, bounds all three components uniformly on \([0,T]\). The first equation's convolution kernel \((2m-y)e^{-(2m-y)s}\) forms an approximate identity; since \(u_C\) has a uniformly bounded derivative, it follows that
\[
\int_0^T|u_A(s)-yu_C(s)|\,ds\longrightarrow0.
\]
The last equation therefore converges in its integral form to \(\dot u_C=(2y^2+2y-4)u_C\), \(u_C(0)=1\). Hence \(u_C(t)\to e^{(2y^2+2y-4)t}\), uniformly for \(t\in[0,T]\). Since \(\pi_m\to(0,0,1)\), the stationary count generating function \(\pi_m u_m(t)\) has the displayed limit. The limit is exactly the moment-generating function of the sum of independent rate-two Poisson singletons and rate-two Poisson doublets; analyticity around zero (or uniqueness of the probability-generating functions on \(0<y\le1\)) establishes convergence in law. This is a fixed-time convergence statement and does not equate the individual two rapidly separated hops to one jump in the \(J_1\) topology.

## Verification
Two independent executable checks accompany this proof. `check_symbolic.py` uses an orbit-level tilted determinant and implicit differentiation, checks the exact rational formula, positivity and monotonic difference identities, and checks the limiting slow spectral factor for every symbolic integer parameter. `check_full.py` generates the **entire unordered-pair configuration graph directly**, including internal orbit moves, solves its Poisson equation numerically, and matches the exact mean and Fano ratio for each \(1\le m\le12\), with the triangle \(m=1\) treated solely as a boundary consistency check. Run `python check_symbolic.py` with SymPy and `OPENBLAS_NUM_THREADS=1 python check_full.py` with NumPy and SciPy. Finite checks are not proofs of the all-size or fixed-time-limit claims; those follow from the preceding calculation and singular-perturbation argument.

## Relationship to prior work
Appert-Rolland, Derrida, Lecomte and van Wijland [1] introduced the integrated-activity tilted generator and calculated its cumulants for periodic one-dimensional exclusion. Lecomte, Garrahan and van Wijland [2] studied activity-biased phases of the exclusion process on a ring. These methods and the activity observable are established, not new. Published work [3] classifies exactly which finite simple exclusion networks give **Poisson** total activity, including the strict non-Poisson conclusion for friendship graphs, but does not evaluate their counting variance or establish a compound-Poisson large-graph counting limit. Published work [4] computes activity noise for Hamming graphs, whose fluctuation ratio tends instead to one in its stated fixed-alphabet large-dimension limit. Published work [5] gives the complete Laplacian spectrum of the two-token friendship graph, a related spectral structural result, but does not compute the tilted activity cumulants or the rare-hub doublet limit. These comparisons distinguish conclusions and implications, not merely titles; the common Markov-generator method is not claimed to be new.

## Limitations
Exactly two conserved, indistinguishable particles, unweighted symmetric rate-one exchanges, equilibrium initial data, and a triangular windmill are assumed. No result is claimed for higher density, irregular blade sizes, directed motion, edge-dependent rates or higher finite-size count cumulants. The compound-Poisson theorem concerns count distributions at fixed times, not path convergence in the \(J_1\) topology. The prior-work comparison is bounded to the examined accessible sources and does not prove exhaustive historical priority.

## References
[1] C. Appert-Rolland, B. Derrida, V. Lecomte, F. van Wijland, *Universal cumulants of the current in diffusive systems on a ring*, arXiv:0804.2590v1, first public 2008-04-16, especially Section II, https://arxiv.org/abs/0804.2590.

[2] V. Lecomte, J. P. Garrahan, F. van Wijland, *Inactive dynamical phase of a symmetric exclusion process on a ring*, arXiv:1203.1600v1, first public 2012-03-07, https://arxiv.org/abs/1203.1600.

[3] *Poisson activity on finite exclusion networks: a complete graph classification*, published RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-poisson-activity-on-finite-exclusion-networks-a-complete-graph-c--016805168b38/RESULT.md.

[4] *Exact jump-activity noise for two-particle exclusion on Hamming graphs*, published RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-jump-activity-noise-for-two-particle-exclusion-on-hamming--9e35afb2f386/RESULT.md.

[5] *Integral Laplacian spectrum and spanning-tree complexity of two-token friendship graphs*, published RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-integral-laplacian-spectrum-and-spanning-tree-complexity-of-two--c081d2602b88/RESULT.md.
