# Six-phase crossings of carrying capacity under repeated three-habitat dispersal

## Finding

Let \(T_k\) be the total population at the globally attracting positive equilibrium when a population disperses \(k\) times between successive rounds of local Beverton–Holt recruitment. The same fixed, conservative three-habitat dispersal matrix and the same local recruitment functions can yield **infinitely many alternations** between \(T_k\) exceeding and falling below the sum of isolated carrying capacities. This phenomenon occurs even though the dispersal network becomes perfectly mixed as \(k\to\infty\).

More precisely, take
\[
D=\frac12\begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix},\qquad
(g_1(z),g_2(z),g_3(z))=\left(\frac{2z}{2z+1},\frac{2z}{z+1},\frac{4z}{2z+1}\right).
\]
For every integer \(k\ge1\), let \(x^{(k)}\in(0,\infty)^3\) be the unique positive solution of \(x=G(D^kx)\), and define \(T_k=\mathbf1^T x^{(k)}\). The isolated carrying capacities are \((1/2,1,3/2)\), totaling \(3\). Then, with indices read modulo six,
\[
\boxed{T_k=3+\frac{2^{-k}}{33}h_{k\bmod6}+O(4^{-k}),\quad
(h_0,h_1,h_2,h_3,h_4,h_5)=(4,-1,-5,-4,1,5).}
\]
Consequently, for all sufficiently large \(k\), \(T_k>3\) precisely in residue classes \(k\equiv0,4,5\pmod6\), and \(T_k<3\) precisely in classes \(k\equiv1,2,3\pmod6\). There are infinitely many switches of the sign of \(T_k-3\) as the *number of dispersal rounds* increases. These are comparisons between equilibrium systems with different \(k\), **not temporal oscillations of one fixed system**.

Within the class of positive two-habitat analytic concave recruitment maps and fixed primitive conservative dispersal matrices, this genuinely six-phase eventually periodic sign pattern is impossible: when the perfect-mixing equilibrium total equals the isolated carrying-capacity total, the nonzero leading sign sequence is eventually constant or alternates only with parity. Thus three habitats are minimal for the exhibited six-phase phenomenon.

## Assumptions and scope

For the specific example, each local recruitment map \(g_i\) is a positive increasing strictly concave Beverton–Holt function with \(g_i(0)=0\), and the dispersal matrix \(D\) is primitive, doubly stochastic and fixed across the family indexed by \(k\). The dynamics for fixed \(k\) are
\[
x(t+1)=G(D^k x(t)),\qquad x(0)\ge0,\quad x(0)\ne0.
\]
Each fixed system has a unique globally attracting strictly positive equilibrium by the standard concave-map persistence theorem established for this model in the cited 2026 source. The index \(k\) is a positive *integer time-scale ratio*, not a continuous migration-rate parameter. All asymptotic estimates concern \(k\to\infty\) with unchanged demographic and dispersal coefficients.

For the general response lemma used below, allow any number \(n\ge2\) of habitats, a primitive column-stochastic \(D\), its probability right eigenvector \(v\gg0\), and \(P=v\mathbf1^T\). Assume recruitment maps are \(C^2\) in a neighborhood of the positive perfect-mixing equilibrium and that the positive equilibrium \(x^{(k)}\) is defined for all sufficiently large \(k\) and tends to \(x^0=G(vT_\infty)\). Write \(a_i=g_i'(v_iT_\infty)\), \(f(T)=\sum_i g_i(v_iT)\), and assume \(0<f'(T_\infty)=a^Tv<1\). The cited concave Beverton–Holt model supplies these assumptions.

## Proof

**1. General first-order fast-mixing response.** Set \(E_k=D^k-P\). Primitivity gives \(E_k\to0\). The equilibrium equation is \(H(x,E)=x-G((P+E)x)=0\). At \((x^0,0)\), its derivative in \(x\) is \(I-\operatorname{diag}(a)v\mathbf1^T\), invertible because \(1-a^Tv>0\). The implicit function theorem and the convergence of the positive equilibria yield
\[
x^{(k)}=x^0+\operatorname{diag}(a)\bigl(v\mathbf1^T(x^{(k)}-x^0)+E_kx^0\bigr)+O(\|E_k\|^2).
\]
Taking column sums and solving for the scalar deviation proves
\[
\boxed{T_k-T_\infty=\frac{a^T E_k x^0}{1-a^Tv}+O(\|E_k\|^2).}
\]
All norms in finite dimensions are equivalent; the remainder is uniform for sufficiently large \(k\). This is a local expansion about the *positive fixed point*, rather than a substitution of the perfect-mixing reduced model for a finite \(k\).

**2. Exact perfect-mixing data for the example.** As \(D\) is doubly stochastic, \(v=(1/3,1/3,1/3)^T\). At total \(T=3\), each patch receives one unit before recruitment and
\[
x^0=(2/3,1,4/3)^T,\quad \mathbf1^Tx^0=3,\quad a=(2/9,1/2,4/9)^T,\quad a^Tv=7/18.
\]
Strict concavity and positivity of the scalar map \(f(T)=\sum_i g_i(T/3)\) imply its unique positive fixed point is \(T_\infty=3\). Set \(b=x^0-(1,1,1)^T=(-1/3,0,1/3)^T\). Since \(P x^0=(1,1,1)^T\), we have \(E_kx^0=D^kb\).

**3. An exact six-step spectral law.** Put \(C=2D-I\); \(C\) cyclically permutes the patches and \(C^3=I\). On the zero-sum plane, the eigenvalues of \(D=(I+C)/2\) are \(2^{-1}e^{\pm i\pi/3}\). Equivalently, by finite rational matrix multiplication,
\[
D^6=P+\frac1{64}(I-P),\qquad D^{k+6}b=\frac1{64}D^kb.
\]
The six exact scalar values \(2^j a^TD^jb\), for \(j=0,\ldots,5\), are
\[
\left(\frac2{27},-\frac1{54},-\frac5{54},-\frac2{27},\frac1{54},\frac5{54}\right).
\]
Thus \(a^TD^kb=2^{-k}h_{k\bmod6}/54\). Inserting \(1-a^Tv=11/18\) in the general response formula yields \(T_k-3=2^{-k}h_{k\bmod6}/33+O(4^{-k})\), because \(\|E_k\|=O(2^{-k})\). Every entry of \(h\) is nonzero, hence the claimed signs hold for all sufficiently large \(k\).

**4. Why two habitats cannot reproduce this six-phase pattern.** For a primitive two-by-two conservative \(D\), its nonunit eigenvalue \(\lambda\) is real and satisfies \(|\lambda|<1\); in fact \(D^k=P+\lambda^k(I-P)\). For positive *analytic* concave recruitment with noncritical perfect-mixing fixed point, the equilibrium total is an analytic function \(T(\varepsilon)\) near \(\varepsilon=0\) with \(\varepsilon=\lambda^k\). If the perfect-mixing total differs from the comparison carrying-capacity sum, the sign is eventually constant. Otherwise, either \(T(\varepsilon)\) is identically that sum near zero (no strict crossings), or its first nonzero Taylor monomial has the form \(c\varepsilon^m\). Its sign as \(k\) grows is then constant if \(\lambda>0\) or \(m\) is even, or parity-alternating if \(\lambda<0\) and \(m\) is odd. If \(\lambda=0\), mixing is exact after one step. No six-class pattern with three consecutive negative classes followed by three positive classes is possible in two habitats.

## Verification

The standalone standard-library program `verify.py` uses exact rational arithmetic to check all recruitment values, derivatives, projection identities, the six-step matrix identity, and the six-class coefficient formula for 72 values of \(k\). Separately, 75-digit Decimal fixed-point iterations for \(k=4,\ldots,30\) verify the expected signs and the \(O(2^{-k})\) leading approximation numerically. It prints its explicit limitations. The infinite sign theorem relies on the proof above, not on any finite enumeration.

## Relationship to prior work

Bravo de la Parra (2026) defines the repeated-dispersal model \(x(t+1)=G(D^k x(t))\), proves positive equilibrium convergence under the stated hypotheses, and determines the limiting perfect-mixing criterion. Its detailed parameter phase analysis is two-habitat and does not provide the present finite-\(k\) spectral-response coefficient or cyclic three-habitat sign law. Segura, Marvá and Franco (online 2025) demonstrate additional, including multiply crossing, three-patch biomass responses when a *continuous migration-intensity parameter* varies. That phenomenon is credited, and is distinct from the present infinite six-class alternation as the discrete number of iterations of one fixed migration matrix tends to infinity. Grumbach and collaborators (2023) characterize two-patch dispersal-intensity effects. None of these distinctions proves global historical uniqueness; the exact repetition-count statement is the claim assessed here.

## Limitations

This is a deterministic mean-field population model. The theorem compares eventual positive equilibrium totals across different integer time-scale ratios, not a time-periodic trajectory, random survival probability, or empirical habitat response. The asymptotic expansion proves the pattern for all sufficiently large \(k\) but does not identify the smallest universal onset index. The two-patch obstruction is stated for analytic local recruitment and noncritical perfect mixing, not for every conceivable nonsmooth density-dependent model. A full independent literature-priority audit has not been performed.

## References

1. R. Bravo de la Parra, “Dispersal and Total Population Size in Discrete-Time Metapopulation Models”, *Mathematics* **14** (2026), article 3624. DOI: https://doi.org/10.3390/math14193624 (first public date 2026-10-07). Sections 2–4 and Appendix A.
2. J. Segura, M. Marvá and D. Franco, “Dispersal in multi-patch metapopulations: The impact of patch number and network topology”, *Journal of Theoretical Biology* **619** (2026), 112331; first online 2025-12-02. DOI: https://doi.org/10.1016/j.jtbi.2025.112331. Sections 2–4.
3. C. Grumbach et al., “The effect of dispersal on asymptotic total population size in discrete- and continuous-time two-patch models”, *Journal of Mathematical Biology* **87** (2023), article 60. DOI: https://doi.org/10.1007/s00285-023-01984-8.
