# Exact fastest mixing on sunlet graphs \(C_m\circ K_1\)

## Finding
For each integer \(m\ge3\), let \(S_m=C_m\circ K_1\) be the graph formed from an \(m\)-cycle by attaching one distinct pendant leaf to each cycle vertex. Let \(\mathcal P_m\) contain every real symmetric, entrywise nonnegative, row-stochastic \(2m\times2m\) matrix \(P\) with \(P_{uv}=0\) for distinct nonadjacent vertices of \(S_m\); diagonal holding probabilities are permitted. Define the second-largest eigenvalue modulus (SLEM) by
\[
\mu(P)=\left\|P-\frac{1}{2m}\mathbf 1\mathbf 1^{\mathsf T}\right\|_2.
\]
Put \(z=\sqrt{2}\sin(\pi/m)\) and \(D=z^2+2z+2\). Then the unrestricted global optimum is
\[
\boxed{\min_{P\in\mathcal P_m}\mu(P)=\frac{2(z+1)}{D}=1-\frac{z^2}{D}.}
\]
An optimal matrix places probability \(a=(z+2)/(2D)\) on each cycle edge in either direction, probability \(b=z(z+1)/D\) on each core-to-leaf edge in either direction, probability zero on each core diagonal, and probability \(1-b\) on each leaf diagonal. This optimizer is unique among matrices invariant under cycle rotations and reflections; uniqueness among all feasible matrices is not asserted. In particular \(\mu_4^*=4/5\), \(a_4=3/10\), \(b_4=2/5\), and
\[
1-\mu_m^*=\frac{\pi^2}{m^2}+O(m^{-3}),\qquad b_m=\frac{\pi}{\sqrt2\,m}+O(m^{-2}).
\]

## Assumptions and scope
The cycle is a finite simple cycle, with \(m\ge3\). States are its \(m\) core vertices \(v_i\) and its \(m\) leaves \(w_i\), indexed by \(i\in\mathbb Z/m\mathbb Z\); edges are \(v_i v_{i+1}\) and \(v_iw_i\). All probabilities are discrete-time transition probabilities. Reversibility here means matrix symmetry and the uniform stationary distribution. In particular, the feasible set permits noninvariant edge weights and nonzero holding probabilities at arbitrary vertices; the conclusion is not limited to invariant candidates. The objective uses all nontrivial eigenvalues, positive and negative.

## Proof
**1. Reduction from all feasible chains.** Denote \(J=\mathbf1\mathbf1^{\mathsf T}/(2m)\). Since every feasible \(P\) is symmetric and stochastic, its nonconstant eigenvalues are exactly those of \(P-J\), hence \(\mu(P)=\|P-J\|_2\). This norm is convex. The dihedral automorphism group permutes the core vertices and simultaneously their attached leaves. Replacing \(P\) by its automorphism average preserves symmetry, stochasticity, nonnegativity and graph support, while convexity gives an objective no larger. There is therefore an optimal invariant chain. Such a chain assigns a common cycle-edge probability \(a\), a common spoke probability \(b\), core holding \(1-2a-b\), and leaf holding \(1-b\), where \(a,b\ge0\) and \(2a+b\le1\).

**2. Exact Fourier spectrum.** Fourier transformation in the cyclic index separates the invariant matrix into symmetric blocks
\[
B(\ell)=\begin{pmatrix}1-b-a\ell&b\\ b&1-b\end{pmatrix},\qquad
\ell_k=2\bigl(1-\cos(2\pi k/m)\bigr),\quad 0\le k<m.
\]
Their eigenvalues are
\[
\lambda_\pm(\ell)=1-b-\frac{a\ell}{2}\pm\sqrt{b^2+\frac{a^2\ell^2}{4}}.
\]
For \(k=0\) these are \(1\) and \(1-2b\). The smallest positive cyclic Laplacian eigenvalue is \(\ell_1=2z^2\). For \(a>0\), \(\lambda_+(\ell_1)\) decreases strictly as \(b\) increases, since its \(b\)-derivative is \(-1+b/\sqrt{b^2+a^2z^4}<0\). Thus every invariant feasible chain obeys
\[
\mu(P)\ge\lambda_+(2z^2)\ge\phi(a):=(2-z^2)a+\sqrt{(1-2a)^2+a^2z^4},\quad 0\le a\le1/2,
\]
where the second inequality is equality when \(b=1-2a\). The case \(a=0\) has a nonconstant eigenvalue \(1\) and cannot improve upon the candidate below.

**3. Scalar minimization.** The square-root in \(\phi\) is the Euclidean norm of the affine vector \((1-2a,z^2a)\). Its second derivative is \(z^4/((1-2a)^2+z^4a^2)^{3/2}>0\); hence \(\phi\) is strictly convex. At
\[
a_* = \frac{z+2}{2D},\qquad b_*=1-2a_*=\frac{z(z+1)}{D},
\]
one has \(\sqrt{b_*^2+a_*^2z^4}=z/2\) and direct differentiation gives \(\phi'(a_*)=0\). For \(0<z\le\sqrt{3/2}\), both weights are positive and \(0<a_*<1/2\), so this is the unique minimum of the scalar lower bound. Its value is
\[
\phi(a_*)=1-b_*-a_*z^2+z/2=\frac{2(z+1)}{D}=:\rho.
\]
Every feasible chain, invariant or not, therefore has SLEM at least \(\rho\).

**4. Attainment and all remaining Fourier modes.** At these weights \(1-b_*=2a_*\), so core holding vanishes. As functions of \(\ell\ge0\), both \(\lambda_+(\ell)\) and \(\lambda_-(\ell)\) are nonincreasing, with the plus branch strictly decreasing because \(b_*>0\). Since every nonzero \(\ell_k\ge2z^2\), its positive-branch eigenvalue is at most \(\rho\), while the negative branch is bounded below by its value at \(\ell=4\):
\[
\lambda_-(\ell_k)\ge\lambda_-(4)=-\sqrt{b_*^2+4a_*^2}.
\]
The elementary identity
\[
\rho^2-(b_*^2+4a_*^2)=\frac{z(z+2)(2-z^2)}{D^2}>0
\]
shows this lower bound is strictly greater than \(-\rho\) for \(0<z\le\sqrt{3/2}\). Finally, the only other eigenvalue of the zero Fourier mode is \(1-2b_*=(2-z^2)/D\ge0\); it lies below \(\rho\) because
\[
\rho-(1-2b_*)=\frac{z(z+2)}{D}>0.
\]
Thus the candidate's SLEM equals \(\rho\), attaining the global lower bound. Strict convexity and strict monotonicity in \(b\) also establish uniqueness within the invariant class.

**5. Asymptotics.** Since \(z=\sqrt2\pi/m+O(m^{-3})\), expansion of \(z^2/(z^2+2z+2)\) gives the stated spectral gap and the formula for \(b_*\).

## Verification
The accompanying `verify.py` rechecks the closed-form identities symbolically, builds actual symmetric stochastic matrices on sunlets of multiple sizes, compares their spectral radii to the formula and Fourier blocks, and tests feasible invariant and noninvariant perturbations. Run `python verify.py` with Python 3 and the documented NumPy/SymPy dependencies. Exact algebra in the proof, not finite numerical testing, establishes global optimality for every integer \(m\ge3\).

## Relationship to prior work
Boyd, Diaconis and Xiao establish the convex/semidefinite fastest-mixing formulation for arbitrary graphs [1]. Boyd, Diaconis, Parrilo and Xiao develop symmetry averaging and explicit cases such as cycles, wheels, and Cartesian products [2]. The wheel has one central hub joined to every rim vertex, while a sunlet has a distinct degree-one leaf at each rim vertex. Their cyclic examples and ring-of-copies example do not yield the displayed sunlet weights or the spectral minimax balance. Jafarizadeh's cyclic multipartite families [3] have neighboring partite-layer connections rather than one pendant leaf per cycle vertex; his later clique-lift families [4] likewise do not identify this sunlet optimum. The triangle instance \(m=3\) is also \(K_3\circ K_1\) and is already covered by the clique-core pendant-leaf specialization; the genuinely different cyclic-core family starts at \(m=4\). The method of averaging and Fourier block reduction is known; the all-size cyclic-core formula, its sharp negative-mode certificate, and its leaf-weight asymptotic are the specific statements assessed here.

## Limitations
The result concerns symmetric chains and uniform equilibrium; arbitrary nonreversible chains or nonuniform equilibrium laws are not covered. It does not assert uniqueness outside the invariant subclass. The graph must have exactly one leaf per cycle vertex and \(m\ge3\). The comparison with prior literature is not a claim of exhaustive publication priority; specialist unindexed or inaccessible work might contain the same formula. Numerical checks are corroborative and do not establish infinite-family claims.

## References
[1] S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, https://doi.org/10.1137/S0036144503423264 ; author manuscript https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .

[2] S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (2007-09-06), https://arxiv.org/abs/0709.0955 ; full text https://ar5iv.labs.arxiv.org/html/0709.0955 .

[3] S. Jafarizadeh, *Fastest Mixing Markov Chain on Symmetric K-Partite Network*, arXiv:1008.2588v1 (2010-08-16), https://arxiv.org/abs/1008.2588 .

[4] S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, arXiv:2501.02421 (2025), https://arxiv.org/abs/2501.02421 .
