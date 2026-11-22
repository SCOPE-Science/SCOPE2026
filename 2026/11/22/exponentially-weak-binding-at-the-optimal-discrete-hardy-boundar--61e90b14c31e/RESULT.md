# Exponentially weak binding at the optimal discrete Hardy boundary

## Finding

Let \(\mathbb N=\{1,2,\ldots\}\). On complex \(\ell^2(\mathbb N)\) put \(u_0=0\), and define the bounded self-adjoint operator
\[
(H_0u)_n=2u_n-u_{n-1}-u_{n+1}-w_nu_n,
\qquad
w_n=2-\sqrt{\frac{n+1}{n}}-\sqrt{\frac{n-1}{n}}.
\]
For any finitely supported, nonnegative, nonzero sequence \(V=(V_n)_{n\ge1}\), define \(S_V=\sum_{n\ge1}nV_n>0\) and \(H_t=H_0-t\operatorname{diag}(V)\) for \(t>0\).

**Theorem.** For every \(t>0\), \(H_t\) has at least one strictly negative isolated eigenvalue. For all sufficiently small \(t>0\), it has **exactly one** negative eigenvalue, of multiplicity one, denoted \(-\varepsilon_V(t)\). Its sharp logarithmic weak-binding law is
\[
\boxed{\lim_{t\downarrow0}t\log\frac1{\varepsilon_V(t)}=\frac2{S_V}.}
\]
Equivalently, \(\varepsilon_V(t)=\exp[-2/(S_Vt)+o(1/t)]\). Thus the leading exponent depends on a general finite defect only through its ground-state-weighted mass \(S_V\), not the number, arrangement, or relative positions of its supported sites.

## Assumptions and scope

All potentials are real, nonnegative, nonzero and fixed as \(t\downarrow0\), with finite support; their individual positive values need not be equal. The underlying vectors may be real or complex. The statement concerns the discrete Dirichlet half-line, the *optimal* Keller–Pinchover–Pogorzelski Hardy weight displayed above, and the bottom of the \(\ell^2\)-spectrum. It does not assert an asymptotic multiplicative prefactor for \(\varepsilon_V(t)\), uniformity for defects whose support moves with \(t\), or uniqueness of the negative spectrum for arbitrary large \(t\).

## Proof

**1. Exact ground-state identity.** Set \(u_n=\sqrt n\,g_n\) and \(c_n=\sqrt{n(n+1)}\). Direct expansion, or the established optimal Hardy identity, gives, initially for finitely supported sequences,
\[
\langle u,H_0u\rangle=\sum_{n=1}^{\infty}c_n|g_{n+1}-g_n|^2,
\qquad \|u\|_2^2=\sum_{n=1}^{\infty}n|g_n|^2.
\]
Both identities extend by density to the form domain. In particular, \(H_0\ge0\). Since \(w_n\to0\), the perturbation of the free Dirichlet Jacobi matrix is compact and \(\sigma_{\mathrm{ess}}(H_0)=[0,4]\). The key point is the **simultaneous** asymptotics \(c_n\sim n\) and mass \(m_n=n\).

**2. A critical massive capacity lemma.** For a fixed positive integer \(m\) and \(\lambda>0\), put
\[
E_\lambda(g)=\sum_{n\ge1}c_n|g_{n+1}-g_n|^2+\lambda\sum_{n\ge1}n|g_n|^2,
\qquad C_m(\lambda)=\inf_{g_m=1}E_\lambda(g).
\]
The infimum ranges over sequences of finite \(E_\lambda\)-energy. We prove
\[
\lim_{\lambda\downarrow0}C_m(\lambda)\log(1/\lambda)=2.
\tag{1}
\]
Set \(N=\lfloor\lambda^{-1/2}\rfloor\) and \(R_{i,j}=\sum_{k=i}^{j-1}c_k^{-1}\). As \(c_k^{-1}=k^{-1}+O(k^{-2})\), \(R_{m,N}=\log N+O_m(1)\). For the upper bound, take \(g_n=1\) up to \(m\), \(g_n=R_{n,N}/R_{m,N}\) from \(m\) to \(N\), and \(g_n=0\) after \(N\). Its gradient energy is exactly \(1/R_{m,N}\). The estimate \(R_{n,N}\le C(1+\log(N/n))\) shows that the massive energy is \(O_m(\lambda N^2/(\log N)^2)=O_m((\log N)^{-2})\), giving
\[
C_m(\lambda)\le\frac{1+o(1)}{\log N}.
\]
For the lower bound, it suffices to consider a near-minimizer with \(g_m=1\) and \(E_\lambda(g)=O(1/\log N)\). Among the indices \(N\le k\le2N\), at least one obeys
\[
|g_k|^2\le \frac{E_\lambda(g)}{\lambda\sum_{j=N}^{2N}j}=O((\log N)^{-1}),
\]
because the mass term is part of the energy and \(\lambda N^2\asymp1\). Discrete Cauchy–Schwarz now yields
\[
E_\lambda(g)\ge
\frac{|g_m-g_k|^2}{R_{m,k}}
\ge\frac{1-o(1)}{\log N}.
\]
As \(\log N\sim\tfrac12\log(1/\lambda)\), this proves (1) with the exact coefficient \(2\).

**3. Universal finite-defect Rayleigh threshold.** Let \(F=\{n:V_n>0\}\) and \(m=\max F\). Define
\[
T_V(\lambda)=\inf_{\sum_{i\in F}iV_i|g_i|^2=1}E_\lambda(g).
\]
Using the capacity test function of Step 2, which equals \(1\) throughout \(F\), gives the asymptotic upper bound
\[
T_V(\lambda)\le (1+o(1))\frac{C_m(\lambda)}{S_V}.
\]
For an exact or approximate minimizer normalized as displayed, the preceding bound implies \(E_\lambda(g)\to0\). For each \(i\in F\), discrete Cauchy–Schwarz along the fixed finite interval from \(i\) to \(m\) gives
\[
|g_i-g_m|^2\le R_{i,m}E_\lambda(g)=o(1).
\]
Hence normalization yields \(S_V|g_m|^2=1+o(1)\). By the definition of \(C_m\),
\[
E_\lambda(g)\ge |g_m|^2C_m(\lambda).
\]
Together with (1), this proves the exact limit
\[
\lim_{\lambda\downarrow0}T_V(\lambda)\log(1/\lambda)=\frac2{S_V}.
\tag{2}
\]

**4. Eigenvalue emergence and inversion.** For \(\lambda>0\), the finite-rank Birman–Schwinger operator
\[
B_\lambda=V^{1/2}(H_0+\lambda)^{-1}V^{1/2}
\]
is positive and compact. Its largest eigenvalue is \(1/T_V(\lambda)\). The resolvent is positivity improving on the connected Jacobi half-line, so the restriction of \(B_\lambda\) to \(F\) has strictly positive entries and a simple Perron eigenvalue. This eigenvalue is continuous and strictly decreasing in \(\lambda\). Consequently \(T_V\) is continuous and strictly increasing. Formula (2) yields \(T_V(\lambda)\to0\) as \(\lambda\downarrow0\); the resolvent bound yields \(T_V(\lambda)\to\infty\) as \(\lambda\to\infty\). Thus for each \(t>0\) there is a unique \(\lambda_t>0\) with \(T_V(\lambda_t)=t\), and \(-\lambda_t\) is the lowest negative eigenvalue of \(H_t\). Inverting (2) yields \(t\log(1/\lambda_t)\to2/S_V\).

**5. Exactly one negative eigenvalue at weak coupling.** For \(m=\max F\), consider the codimension-one hyperplane \(g_m=0\). On this hyperplane,
\[
\sum_{i\in F}iV_i|g_i|^2\le K_V\sum_{n\ge1}c_n|g_{n+1}-g_n|^2,
\qquad
K_V=\sum_{\substack{i\in F\\ i<m}}iV_iR_{i,m}<\infty.
\]
Therefore the quadratic form of \(H_t\) is nonnegative on that hyperplane whenever \(tK_V\le1\) (with no restriction if \(K_V=0\)). A negative spectral subspace of dimension at least two must intersect a codimension-one hyperplane nontrivially, contradiction. The negative eigenvalue constructed in Step 4 is therefore the only one, and is simple, for all sufficiently small positive \(t\). This completes the proof.

## Verification

The accompanying `CHECKER.py` evaluates six independent finite ground-state identities, eight finite-section negative eigenvalues for two distinct finite defects, and a one-site weak-coupling trend. The exact infinite-dimensional capacity coefficient, min–max result, and eventual uniqueness are established analytically above. Run `python CHECKER.py` in an environment with NumPy and SciPy. These finite tests are not substitutes for the limit proof, and the truncation is not used to assert convergence at machine precision.

## Relationship to prior work

Keller–Pinchover–Pogorzelski first published the improved discrete Hardy weight and its optimality in December 2016. Krejčiřík–Štampach (2021) prove the exact ground-state remainder identity used here; criticality already implies a negative spectral response to any nonzero localized attractive perturbation. The new statement is the **quantitative, support-universal logarithmic binding coefficient** \(2/S_V\) and eventual one-eigenvalue theorem, not the underlying weight, ground-state representation, or qualitative instability. Gerhat–Krejčiřík–Štampach (2023) study a distinct criticality transition for powers of the free discrete half-line Laplacian and localized perturbations of the bilaplacian. Damanik–Teschl (2005) analyze *supercritical* inverse-square tails with infinitely many eigenvalues; their counting asymptotic does not supply the critical localized-defect binding law here.

## Limitations

The estimate determines only the logarithmic exponential rate. It does not identify the finite multiplicative prefactor, perturbations changing shape or support with \(t\), sign-indefinite perturbations, or the full negative spectral count at strong coupling. Results from general critical-operator weak-binding theory might contain applicable implicit special cases, so historical priority beyond the specifically checked texts is not certified. No independent mathematical audit or external validation has been performed.

## References

1. M. Keller, Y. Pinchover, F. Pogorzelski, *Optimal Hardy inequalities for Schrödinger operators on graphs*, arXiv:1612.04051, first submitted December 13, 2016, https://arxiv.org/abs/1612.04051.
2. M. Keller, Y. Pinchover, F. Pogorzelski, *An improved discrete Hardy inequality*, arXiv:1612.05913, first submitted December 18, 2016, https://arxiv.org/abs/1612.05913.
3. D. Krejčiřík, F. Štampach, *A sharp form of the discrete Hardy inequality and the Keller–Pinchover–Pogorzelski inequality*, arXiv:2108.04379, August 9, 2021, https://arxiv.org/html/2108.04379v1.
4. B. Gerhat, D. Krejčiřík, F. Štampach, *Criticality transition for positive powers of the discrete Laplacian on the half line*, arXiv:2307.09919, July 19, 2023, https://arxiv.org/abs/2307.09919.
5. D. Damanik, G. Teschl, *Bound states of discrete Schrödinger operators with super-critical inverse square potentials*, arXiv:math/0509110, September 5, 2005, https://arxiv.org/abs/math/0509110.
