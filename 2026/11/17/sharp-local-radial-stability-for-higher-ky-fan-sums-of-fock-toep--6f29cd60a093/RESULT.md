# Sharp local radial stability for higher Ky Fan sums of Fock Toeplitz operators

## Finding
Fix an integer \(N\ge2\) and an area \(s>0\). On the standard Gaussian Bargmann--Fock Hilbert space
\[
\mathcal F^2=\left\{f\text{ entire}:\int_{\mathbb C}|f(z)|^2e^{-\pi|z|^2}\,dA(z)<\infty\right\}
\]
let \(T_\Omega f=P_{\mathcal F}(\mathbf 1_\Omega f)\), where \(P_{\mathcal F}\) is the orthogonal Fock projection and \(\Omega\subset\mathbb C\) is measurable of finite area. Write \(K_N(\Omega)\) for the sum of the \(N\) largest eigenvalues of the positive trace-class operator \(T_\Omega\), counted with multiplicity. Let \(D_s=\{z:\pi|z|^2<s\}\).

For every
\[
0<\delta<\delta_0(N,s):=\frac{e^{-s}s^N}{2N!},
\]
the exact minimum of the Ky Fan deficit among **all origin-centered radial measurable sets** satisfying \(|\Omega|=s\) and \(|\Omega\triangle D_s|=2\delta\) is
\[
\boxed{\ \inf_\Omega[K_N(D_s)-K_N(\Omega)]=\Delta_N(s,\delta):=2F_N(s)-F_N(s-\delta)-F_N(s+\delta)\ },
\]
where
\[
F_N(x)=N-e^{-x}\sum_{j=0}^{N-1}\frac{(N-j)x^j}{j!},\qquad x\ge0.
\]
The infimum is attained uniquely up to planar area-null sets by the **boundary-exchange annulus**
\[
\boxed{\ \Omega_{s,\delta}=\{z:0\le\pi|z|^2<s-\delta\}\;\cup\;\{z:s<\pi|z|^2<s+\delta\}.\ }
\]
Moreover,
\[
\Delta_N(s,\delta)=\frac{e^{-s}s^{N-1}}{(N-1)!}\,\delta^2+O_{N,s}(\delta^4)\quad(\delta\downarrow0).
\]
Consequently the quadratic power and its area- and rank-dependent positive coefficient are best possible for this constrained radial problem. No regularity or finite-component restriction is imposed on the competing radial sets.

## Assumptions and scope
All sets are Lebesgue measurable and radially symmetric about the fixed origin. Use the area coordinate \(t=\pi|z|^2\); then their planar area equals the ordinary Lebesgue measure of the associated set \(E\subset[0,\infty)\). The reference disk corresponds to \([0,s]\). Symmetric difference of planar area \(2\delta\), combined with \(|\Omega|=s\), means that both the removed and added radial-coordinate subsets have length \(\delta\). The condition on \(\delta\) implies \(\delta<s\), since the disk spectral gap \(e^{-s}s^N/N!\) is at most its trace \(s\).

The range \(N\ge2\) is deliberate: the first-eigenvalue stability problem has a separate substantial literature. The local-radius condition is a sufficient explicit uniform *spectral no-crossing condition*, not a claim that it is the largest possible neighborhood. The sharpness asserted is exact for each allowed fixed \(N,s,\delta\), not the optimality of the neighborhood endpoint.

## Proof
**1. Radial diagonalization.** The normalized monomials \(e_j(z)=(\pi^j/j!)^{1/2}z^j\), \(j\ge0\), form an orthonormal basis. For radial \(\Omega\) corresponding to \(E\), angular orthogonality makes \(T_\Omega\) diagonal with entries
\[
\lambda_j(E)=\int_E p_j(t)\,dt,\qquad p_j(t)=e^{-t}\frac{t^j}{j!},\quad j=0,1,\ldots.
\]
At the disk, \(\lambda_j([0,s])=1-e^{-s}\sum_{k=0}^j s^k/k!\), a strictly decreasing sequence. Its gap between coordinates \(N-1\) and \(N\) is
\[
g_N(s):=\lambda_{N-1}([0,s])-\lambda_N([0,s])=e^{-s}\frac{s^N}{N!}>0.
\]

**2. Uniform spectral-index preservation.** Write \(A=[0,s]\setminus E\) and \(B=E\setminus[0,s]\). Then \(|A|=|B|=\delta\). Since \(0\le p_j(t)\le1\) (the \(p_j(t)\) are point probabilities of a Poisson law), each of \(\int_Ap_j\) and \(\int_Bp_j\) belongs to \([0,\delta]\). Therefore
\[
|\lambda_j(E)-\lambda_j([0,s])|=\left|\int_Bp_j-\int_Ap_j\right|\le\delta\quad\text{for every }j\ge0.
\]
If \(2\delta<g_N(s)\), then every one of the first \(N\) diagonal entries of \(T_\Omega\) is strictly larger than every entry with index at least \(N\). It follows that their sum, *without any possible eigenvalue reordering across the cutoff*, is
\[
K_N(\Omega)=\sum_{j=0}^{N-1}\lambda_j(E)=\int_Eq_N(t)\,dt,\qquad q_N(t)=e^{-t}\sum_{j=0}^{N-1}\frac{t^j}{j!}.
\]

**3. Sharp deficit and rigidity.** The crucial derivative is
\[
q_N'(t)=-e^{-t}\frac{t^{N-1}}{(N-1)!}<0\qquad(t>0).
\]
For sets \(A\subset[0,s]\) and \(B\subset[s,\infty)\) of measure \(\delta\), strict monotonicity gives
\[
\int_Aq_N(t)\,dt\ge\int_{s-\delta}^sq_N(t)\,dt,\qquad
\int_Bq_N(t)\,dt\le\int_s^{s+\delta}q_N(t)\,dt.
\]
Both inequalities are equalities simultaneously only when \(A=[s-\delta,s]\) and \(B=[s,s+\delta]\) up to null sets. (For instance, swapping any positive-measure piece of an alleged optimum farther from the boundary with a piece closer to it strictly lowers its removed integral or raises its added integral.) Consequently
\[
K_N(D_s)-K_N(\Omega)=\int_Aq_N-\int_Bq_N\ge
\int_{s-\delta}^sq_N-\int_s^{s+\delta}q_N.
\]
The stated boundary-exchange set realizes equality and is the unique radial equality case. Since \(F_N'(x)=q_N(x)\), the right-hand side equals \(2F_N(s)-F_N(s-\delta)-F_N(s+\delta)\), which is strictly positive.

**4. Exact local coefficient.** Taylor expansion at the fixed positive point \(s\) cancels the odd powers and yields
\[
2F_N(s)-F_N(s-\delta)-F_N(s+\delta)
=-F_N''(s)\delta^2+O_{N,s}(\delta^4)
=\frac{e^{-s}s^{N-1}}{(N-1)!}\delta^2+O_{N,s}(\delta^4).
\]
The exact equality family proves that neither the exponent nor the coefficient in the sharp *local constrained* modulus can be improved.

## Verification
The theorem is analytical. The included standard-library Python script, `check_radial.py`, performs 880 supplementary finite diagnostic assertions: it computes radial monomial integrals, compares finitely many eigenvalues, tests randomly placed removed and added annuli at several ranks and areas, and compares their deficits to the boundary-exchange formula. These checks do not replace the infinite-dimensional diagonalization, no-crossing argument, or rearrangement proof. Run `python check_radial.py` from the package directory; it requires no external Python modules.

## Relationship to prior work
Nicola, Riccardi and Tilli (arXiv:2503.07069, first circulated March 10, 2025), Theorem 1.5, prove that disks uniquely maximize the rank-\(N\) Ky Fan sum among radial domains, and in their introduction explicitly identify quantitative refinements as a future direction. Abreu (arXiv:2607.28376, July 30, 2026) proves the unrestricted disk-maximization inequality for all measurable domains and all ranks. The present theorem does **not** claim these maximization or radial uniqueness statements: it determines the exact *nonzero* optimal deficit at a prescribed small symmetric-difference distance, its rigid realizing shape, and its sharp quadratic coefficient for higher ranks. Its key additional step is uniform identification of the first \(N\) eigenvalue indices under arbitrary radial perturbations before applying a fixed-density bathtub comparison.

Gómez, Guerra, Ramos and Tilli (arXiv:2307.09304) prove a quantitative first-eigenvalue concentration theorem; Nicola and Riccardi (arXiv:2401.04659) treat the Hilbert--Schmidt norm, a different spectral functional. Neither is claimed as new here. Published literature could contain an equivalent higher-rank quantitative local statement under different terminology; this cannot be excluded absolutely.

## Limitations
The result is specific to the one-complex-dimensional Gaussian Fock space, origin-centered radial sets, higher-rank Ky Fan *sums*, and the explicitly stated neighborhood \(0<\delta<g_N(s)/2\). It does not yield global stability for nonradial perturbations, does not optimize the size of the admissible neighborhood, and does not provide an inverse estimate in an optimally translation-invariant asymmetry. Finite diagnostics do not establish the theorem; they merely check sample instances. The comparison with earlier work does not establish absolute priority.

## References
1. F. Nicola, F. Riccardi and P. Tilli, *The isoperimetric inequality for partial sums of Toeplitz eigenvalues in the Fock space*, arXiv:2503.07069 (2025), https://arxiv.org/abs/2503.07069 .
2. L. D. Abreu, *The isoperimetric inequality for the Ky Fan norm*, arXiv:2607.28376 (2026), https://arxiv.org/abs/2607.28376 .
3. J. Gómez, A. Guerra, J. P. G. Ramos and P. Tilli, *Stability of the Faber--Krahn inequality for the short-time Fourier transform*, arXiv:2307.09304 (2023), https://arxiv.org/abs/2307.09304 .
4. F. Nicola and F. Riccardi, *The quantitative isoperimetric inequality for the Hilbert--Schmidt norm of localization operators*, arXiv:2401.04659 (2024), https://arxiv.org/abs/2401.04659 .
