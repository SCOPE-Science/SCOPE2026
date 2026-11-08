# Exact two-clock relaxation and Poisson boundary windows for permutation quadratic stochastic maps

## Finding

The non-Volterra quadratic stochastic operator of Jamilov admits an exact nonlinear–linear factorization. Its deviation from the invariant face decays doubly exponentially, while its distribution among the remaining types relaxes as an ordinary lazy permutation chain. The latter mechanism has two different continuous-time boundary limits, one retaining the residue of the discrete permutation period and one not.

For every integer \(m\ge3\), every nonidentity permutation \(\pi\) of \(\{1,\ldots,m-1\}\), and every \(0\le\alpha\le1\), let \(P\) be the permutation matrix defined by \((Pp)_k=p_{\pi(k)}\). Write \(s\) for the order of \(P\), \(\Pi\) for the orthogonal projection onto \(\ker(P-I)\), and \(L\ge2\) for the longest cycle of \(\pi\). For any initial point with \(0<x_m(0)<1\), put \(u=2x_m(0)-1\) and \(p_k=x_k(0)/(1-x_m(0))\) for \(k<m\). Then, at every integer time \(n\ge0\),

\[
 x_m(n)=\frac{1+u^{2^n}}2,\qquad
 (x_k(n))_{k<m}=\frac{1-u^{2^n}}2\,[\alpha I+(1-\alpha)P]^n p.
\]

For fixed \(0<\alpha<1\), the directional relaxation has an *exact sharp Euclidean operator norm* at every \(n\ge1\):

\[
 \big\|[\alpha I+(1-\alpha)P]^n-\Pi\big\|_{2\to2}
 =\bigl[1-4\alpha(1-\alpha)\sin^2(\pi/L)\bigr]^{n/2}.
\]

The expression can be zero (for \(L=2\), \(\alpha=1/2\)), corresponding to exact one-step directional equilibration.

At the two singular parameter endpoints the natural time scale is proportional to the inverse distance from the endpoint. If \(n_j\to\infty\), \(\alpha_j\to0\), \(n_j\alpha_j\to t\in[0,\infty)\), and \(n_j\equiv r\pmod{s}\), then

\[
 (x_k(n_j))_{k<m}\longrightarrow
 \frac12 P^r\exp\bigl[t(P^{-1}-I)\bigr]p,
 \qquad x_m(n_j)\longrightarrow\frac12.
\]

If instead \(\alpha_j\to1\) and \(n_j(1-\alpha_j)\to t\in[0,\infty)\), no residue is required and

\[
 (x_k(n_j))_{k<m}\longrightarrow
 \frac12\exp\bigl[t(P-I)\bigr]p,
 \qquad x_m(n_j)\longrightarrow\frac12.
\]

These limiting semigroups are Poisson mixtures of forward and reverse permutation steps. For any \(p\ne\Pi p\), they differ from \(\Pi p\) at every finite \(t\), whereas they approach \(\Pi p\) as \(t\to\infty\). Thus the inverse-endpoint scaling is sharp and the left-endpoint limit retains a genuine phase residue.

## Assumptions and scope

The state space is the standard simplex \(S^{m-1}=\{x\in[0,1]^m:\sum_{k=1}^m x_k=1\}\). The quadratic map is exactly

\[
 (V_{\pi,\alpha}(x))_k=2x_m\bigl[\alpha x_k+(1-\alpha)x_{\pi(k)}\bigr]
 \quad(1\le k<m),\qquad
 (V_{\pi,\alpha}(x))_m=x_m^2+(1-x_m)^2.
\]

Coordinates are ordered as in the source paper, and the Euclidean norm is on the first \(m-1\) coordinates. The permutation \(\pi\) may have several disjoint cycles, including singleton cycles. The projection \(\Pi\) replaces coordinates on each cycle by their arithmetic mean; it preserves the total mass of each cycle. The statement about sharp operator norm uses the entire zero-cycle-mean subspace and is not a lower bound for every particular initial state (some may lack its slow Fourier mode). The two boundary limits hold for *fixed initial \(x\)* and arbitrary sequences \((n_j,\alpha_j)\) satisfying the stated quantifiers. They do not assert uniformity over initial states tending to the absorbing vertex.

If \(x_m(0)=0\), the map reaches \(e_m\) in one step; if \(x_m(0)=1\), it is already at \(e_m\). The theorem concerns the nontrivial complement of those exceptional states.

## Proof

**1. Exact scalar conjugacy.** Set \(z_n=x_m(n)\) and \(u_n=2z_n-1\). The scalar update is \(z_{n+1}=z_n^2+(1-z_n)^2\); therefore

\[
 u_{n+1}=2[z_n^2+(1-z_n)^2]-1=(2z_n-1)^2=u_n^2.
\]

Induction gives \(u_n=u_0^{2^n}\) for all \(n\ge0\), including the first time step, so \(z_n=(1+u_0^{2^n})/2\) and \(1-z_n=(1-u_0^{2^n})/2\). This is exact; an ordinary exponential estimate would lose the second intrinsic clock.

**2. Directional dynamics.** Let \(v_n=(x_k(n))_{k<m}\). Since \(\sum_{k<m}x_k(n)=1-z_n\), the update yields

\[
 v_{n+1}=2z_n Q_\alpha v_n,
 \qquad 1-z_{n+1}=2z_n(1-z_n),
 \qquad Q_\alpha=\alpha I+(1-\alpha)P.
\]

As \(0<z_n<1\), division gives \(p_{n+1}=Q_\alpha p_n\) for \(p_n=v_n/(1-z_n)\). Hence \(p_n=Q_\alpha^n p\), and multiplying by the known scalar mass establishes both finite-time formulas. No asymptotic approximation has been used.

**3. Exact spectral relaxation and two clocks.** Every permutation matrix is orthogonal and diagonalizable by a unitary change of basis. On each length-\(\ell\) cycle its eigenvalues are the \(\ell\)-th roots of unity. For an eigenvalue \(e^{i\theta}\) of \(P\), the corresponding eigenvalue of \(Q_\alpha\) is \(\alpha+(1-\alpha)e^{i\theta}\), with squared modulus

\[
 1-2\alpha(1-\alpha)(1-\cos\theta)
 =1-4\alpha(1-\alpha)\sin^2(\theta/2).
\]

The eigenvalue \(1\) corresponds precisely to the cycle-constant subspace, onto which \(\Pi\) projects. On its orthogonal complement, the largest squared modulus is attained by the first Fourier mode of a *longest* cycle, with angle magnitude \(2\pi/L\). Normality implies that the operator norm of \(Q_\alpha^n-\Pi\) is exactly the largest modulus to the \(n\)-th power. This proves the sharp claimed norm, including the exceptional zero at an involution with \(\alpha=1/2\).

The scalar and directional error contributions are orthogonal, so they also yield the exact identity

\[
 \left\|v_n-\tfrac12\Pi p\right\|_2^2
 =\frac14\left[
  (1-u^{2^n})^2\left\|Q_\alpha^n(p-\Pi p)\right\|_2^2
  +u^{2^{n+1}}\left\|\Pi p\right\|_2^2
 \right].
\]

Here the first term decays at the spectral rate whenever the initial vector contains a slow mode; the second vanishes doubly exponentially since \(|u|<1\). This demonstrates why the nonlinear and directional clocks cannot be replaced by one universal finite-time rate.

**4. Near the permutation endpoint.** Because \(P\) and \(P^{-1}\) commute,

\[
 Q_\alpha=P\bigl[I+\alpha(P^{-1}-I)\bigr],\qquad
 Q_\alpha^n=P^n\bigl[I+\alpha(P^{-1}-I)\bigr]^n.
\]

For \(n_j\alpha_j\to t\) and \(\alpha_j\to0\), finite-dimensional matrix logarithm expansion gives

\[
 n_j\log\bigl[I+\alpha_j(P^{-1}-I)\bigr]
 =n_j\alpha_j(P^{-1}-I)+O(n_j\alpha_j^2)
 \longrightarrow t(P^{-1}-I).
\]

The remainder vanishes because \(n_j\alpha_j\) stays bounded and \(\alpha_j\to0\). As \(P^s=I\), the assumed residue makes \(P^{n_j}=P^r\) exactly. The scalar factor converges to \(1/2\), proving the first joint limit.

**5. Near the identity endpoint.** Write \(\varepsilon=1-\alpha\). Then \(Q_\alpha=I+\varepsilon(P-I)\). The same logarithm argument, now with \(n_j\varepsilon_j\to t\), proves \(Q_{\alpha_j}^{n_j}\to e^{t(P-I)}\); no residue enters. The scalar factor again converges to \(1/2\).

**6. Why the boundary windows are sharp.** Both limiting exponentials have Poisson expansions, for example

\[
 e^{t(P-I)}=e^{-t}\sum_{j=0}^{\infty}\frac{t^j}{j!}P^j.
\]

They are invertible and commute with \(\Pi\). For finite \(t\), their action on \(p-\Pi p\ne0\) cannot vanish, even after multiplication by \(P^r\). Their nonconstant Fourier modes decay as \(e^{-t(1-\cos\theta)}\); hence they converge to \(\Pi\) as \(t\to\infty\). Finally, as \(\alpha\downarrow0\) or \(\alpha\uparrow1\), the sharp spectral gap is

\[
 -\log\rho(\alpha)
 \sim \bigl[1-\cos(2\pi/L)\bigr]\min\{\alpha,1-\alpha\},
 \qquad \rho(\alpha)=\sqrt{1-4\alpha(1-\alpha)\sin^2(\pi/L)}.
\]

Thus the distance-to-endpoint times iteration count is the correct critical scale for generic directional relaxation. This concludes the proof.

## Verification

The accompanying self-contained `verify.py` performs the following independent finite checks: (i) comparison of direct nonlinear iteration against the exact factorization at multiple parameters and times; (ii) convergence toward both Poisson semigroup limits at three scaled times and all four residue classes of a four-cycle; and (iii) exact sharpness of the predicted spectral factor on a first Fourier mode. All checks completed successfully. The finite tests are not used to prove any uniform-in-dimension or infinite-time assertion; those assertions follow from the six analytical steps above. Run `python3 verify.py` with Python 3 and no third-party dependencies.

## Relationship to prior work

Jamilov's *A family of non-Volterra quadratic operators corresponding to permutations* (arXiv:2210.05107, DOI 10.46298/cm.10135) introduces precisely the displayed map, describes its fixed and limit points, and proves qualitative convergence for interior mixing parameters. Its full primary text, especially equation (4), Proposition 3.2 and Theorem 3.5, was inspected. The exact finite-time radial–directional factorization, sharp spectral norm, and two endpoint-scaled semigroups above are quantitatively distinct from those stated results.

The finite-dimensional Markov-chain spectral calculation and Poisson limit \((I+tA/n)^n\to e^{tA}\) are classical tools and are **not** claimed as newly discovered general principles. The object-specific connection between the quadratic nonlinear iteration and the two boundary phase diagrams is the claimed addition. The related Jamilov–Khudoyberdiev paper *On the dynamics of non-Volterra quadratic operators corresponding to permutations* (DOI 10.1080/10236198.2023.2284827) describes fixed and periodic points and omega-limit sets in its accessible abstract; its full text was not available for a complete implication comparison and remains a priority risk. The later Jamilov–Ladra preprint arXiv:2601.17494 concerns a different convex combination, with additional pure-square and pairwise quadratic terms (its equation (5.1)); it is not a reparameterization of the displayed map. Other generic operator and cyclic-chain results do not, merely from their titles or techniques, establish this entire quantitative statement for this particular quadratic map.

## Limitations

The theorem is restricted to the explicitly defined family and fixed initial data away from \(x_m=0,1\). The exact Euclidean spectral rate is an operator norm, not the decay rate of every individual orbit. No assertion is made about perturbations of the quadratic map that destroy the permutation factorization, or about nonlinear stochastic perturbations. The correspondence with finite-state continuous-time Markov chains is an exact asymptotic reduction, not a claim of a new Markov semigroup theorem. The unavailable 2023 related full text and possible unindexed equivalent calculations limit the publication-priority assessment. No independent audit has been performed.

## References

1. U. U. Jamilov, *A family of non-Volterra quadratic operators corresponding to permutations*, arXiv:2210.05107 (first version October 11, 2022), *Communications in Mathematics* 31 (2023), 31–41, DOI 10.46298/cm.10135. https://arxiv.org/pdf/2210.05107
2. U. U. Jamilov and Kh. O. Khudoyberdiev, *On the dynamics of non-Volterra quadratic operators corresponding to permutations*, *Journal of Difference Equations and Applications* 30 (2024), 336–360, DOI 10.1080/10236198.2023.2284827. https://doi.org/10.1080/10236198.2023.2284827
3. U. U. Jamilov and M. Ladra, *On a family of non-Volterra quadratic operators acting on a simplex*, arXiv:2601.17494 (2026). https://arxiv.org/pdf/2601.17494
