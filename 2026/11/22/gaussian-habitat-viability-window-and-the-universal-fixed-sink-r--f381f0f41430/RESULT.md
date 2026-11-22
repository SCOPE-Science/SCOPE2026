# Gaussian habitat-viability window and the universal fixed-sink relaxation correction

## Finding

Fix a positive integer \(s\) and \(p\in(0,1)\). For \(G_n\sim G(n,p)\), let \(S\) be any deterministic set of \(s\) absorbing habitat sites, and write \(m=n-s\) for the number of viable sites. Denote by \(L_{g,n}\) the unnormalized Dirichlet Laplacian of \(G_n\) obtained by deleting the sink rows and columns of the full combinatorial Laplacian; define \(\xi_n=\lambda_{\min}(L_{g,n})\). Let \(B_n\) count edges between \(S\) and its complement. Then

\[
\boxed{m\left(\frac{B_n}{m}-\xi_n\right)\xrightarrow{\mathbb P}s(1-p),}
\]
\[
\boxed{\sqrt n\,(\xi_n-sp)\xrightarrow{d}\mathcal N(0,sp(1-p)).}
\]

Consequently, writing \(\Phi\) for the standard normal cumulative distribution function and choosing any fixed real \(a\),

\[
\boxed{\lim_{n\to\infty}\Pr\!\left(\xi_n<sp+\frac a{\sqrt n}\right)=\Phi\!\left(\frac{a}{\sqrt{sp(1-p)}}\right).}
\]

This is the complete leading crossover profile at the marginal ecological invasion threshold, together with the leading systematic difference between boundary-edge density and the actual principal eigenvalue. The correction coefficient is independent of the detailed random internal connections.

## Assumptions and scope

All graph edges are independent Bernoulli variables with the same \(p\in(0,1)\), held fixed as \(n\to\infty\). The integer \(s\ge1\) is also fixed. The absorbing set is chosen deterministically without reference to the sampled edges. Let \(L_H\) denote the combinatorial Laplacian of the induced subgraph on the \(m\) nonabsorbing vertices, and write \(z_i\) for the number of sink neighbors of the \(i\)-th viable vertex. Then \(z_i\) are independent \(\operatorname{Binomial}(s,p)\) variables, independent of \(L_H\), and

\[L_{g,n}=L_H+Z,\qquad Z=\operatorname{diag}(z_1,\ldots,z_m),\qquad B_n=\sum_{i=1}^m z_i.\]

For the linearized graph-diffusion logistic model with diffusion rate \(D>0\) and site reproduction rate \(r_n>0\), \(\dot u=D(\rho_n I-L_{g,n})u+\text{higher-order terms}\) with \(\rho_n=r_n/D\), the infinitesimal invasion exponent equals \(D(\rho_n-\xi_n)\). The theorem concerns the strict positive-invasion event. It does not equate that event with demographic persistence of a finite stochastic population.

## Proof

**1. Uniform-vector decomposition.** Put \(e=m^{-1/2}{\bf1}\) and \(Q=I-ee^{\mathsf T}\). Since \(L_He=0\),

\[\bar z=e^{\mathsf T}L_{g,n}e=B_n/m,\qquad b=QL_{g,n}e=QZe,\]

\[\|b\|^2=\frac1m\sum_{i=1}^m(z_i-\bar z)^2\xrightarrow{\mathbb P}sp(1-p).\tag{1}\]

The limit in (1) is the ordinary law of large numbers for bounded independent sink-degrees. Also \(\xi_n\le\bar z\le s\) by the Rayleigh principle.

**2. Spectral separation of internal habitat modes.** Write \(A_{ij}\) for the independent edge indicator inside the viable set. The centered Laplacian is

\[E_m=L_H-p(mI-\mathbf1\mathbf1^{\mathsf T})=\sum_{1\le i<j\le m}(A_{ij}-p)(e_i-e_j)(e_i-e_j)^{\mathsf T},\]

where now \(e_i\) denotes a coordinate unit vector. Each centered summand has operator norm at most \(2\). Its variance proxy is

\[\sum_{i<j}\mathbb E X_{ij}^2=2p(1-p)(mI-\mathbf1\mathbf1^{\mathsf T}),\]

whose norm is \(2p(1-p)m\). The self-adjoint matrix Bernstein inequality therefore yields

\[\|E_m\|=O_{\mathbb P}(\sqrt{m\log m}).\tag{2}\]

In particular, on \(e^\perp\), \(QL_HQ=pmI_{e^\perp}+O_{\mathbb P}(\sqrt{m\log m})\). Its least eigenvalue is greater than \(s\) with probability tending to one.

**3. Exact Schur identity and second-order correction.** On that high-probability event the minimizing eigenvector of \(L_{g,n}\) cannot lie entirely in \(e^\perp\), because every Rayleigh quotient there exceeds \(s\) while \(\xi_n\le s\). Projecting the eigenvalue equation onto the \(e\) and \(e^\perp\) blocks gives the exact identity

\[\bar z-\xi_n=b^{\mathsf T}\bigl(QL_HQ+QZQ-\xi_n I_{e^\perp}\bigr)^{-1}b.\tag{3}\]

As \(\|Z\|\le s\) and \(0\le\xi_n\le s\), (2) ensures the restricted inverse equals

\[\frac1{pm}\bigl(I_{e^\perp}+O_{\mathbb P}(\sqrt{\log m/m})\bigr)\]

in operator norm, where the error notation refers to a random bounded linear operator. Combining this with (1) and (3),

\[m(\bar z-\xi_n)=\frac{\|b\|^2}{p}+o_{\mathbb P}(1)\xrightarrow{\mathbb P}s(1-p).\]

For a finite deterministic consistency check, if the internal Laplacian has spectral gap \(g>s\), the same Schur identity and Rayleigh inequality show

\[0\le\bar z-\xi\le\frac{s^2}{g-s}.\tag{4}\]

**4. Gaussian invasion window.** Because every potential cross-boundary edge is independent, \(B_n\sim\operatorname{Binomial}(sm,p)\). Hence the scalar binomial central limit theorem gives

\[\sqrt n\left(\frac{B_n}{m}-sp\right)\xrightarrow{d}\mathcal N(0,sp(1-p)),\]

as \(n/m\to1\). The difference \(\bar z-\xi_n=O_{\mathbb P}(m^{-1})\) is negligible after multiplication by \(\sqrt n\); Slutsky's theorem proves the claimed spectral limit. The limiting Gaussian law is continuous, so the convergence of the strict threshold probability follows.

## Verification

The standalone Python program `check_fixed_sink.py` reconstructs all graph Laplacians directly from edge indicators. It checks 253 eligible finite deterministic eigenvalue inequalities of the form (4), 60 independent numerical instances of exact Schur identity (3), and 216 sampled Erdős–Rényi grounded spectra at \(s=2\), \(p=0.4\), and \(n\in\{96,192,384\}\). The sampled average of \(m(B_n/m-\xi_n)\) is respectively \(1.228406\), \(1.219869\), and \(1.205519\), against the rigorous limiting value \(1.2\). The predicted Gaussian variance is \(0.48\); finite-sample empirical variances are not certificates of the limit. Run `python check_fixed_sink.py` with NumPy and SciPy. The proof of every asymptotic statement is analytic, not inferred from these computations.

## Relationship to prior work

Pirani and Sundaram (2014), Section V and Theorem 3, already establish the fixed-few-sink first-order approximation \(\xi_n\sim sp\) for dense binomial random graphs, using a grounded-Laplacian eigenvector bound. Their stated estimate is a relative \(1+o(1)\) approximation and does not itself establish the \(n^{-1/2}\) distributional law or the order-\(n^{-1}\) relaxation coefficient. Apollonio, Tora and Vergni (2026), Theorem 1, formulate the ecological viability problem and establish another concentration result under growing \(s_np_n\), while explicitly studying fixed sink counts in finite-size viability bounds; they do not assert the stated Gaussian critical window and relaxation correction. Tropp's self-adjoint matrix Bernstein inequality is a standard tool used in step 2 and is not claimed as new. A closely related 2026 article by Tora and Vergni on critical patch size on networks was located; its accessible abstract concerns spectral persistence bounds, but its full text could not be reviewed. The historical-priority conclusion is therefore literature-bounded, not a uniqueness certificate.

## Limitations

The claim requires fixed \(s\), fixed interior \(p\), independent edges and a sink set selected independently of the network. No extension is proved for sparse graphs, sink counts growing with network order, adversarially positioned sinks, or heterogeneous reproduction. The crossover describes a linearized invasion eigenvalue, not the probability of survival in a finite stochastic birth–death population. The inaccessible related article and general spectral-fluctuation literature leave residual priority risk; no independent audit has been performed.

## References

- N. Apollonio, V. Tora and D. Vergni, *The Critical Patch Size Problem in Random Graphs*, arXiv:2604.00624v1 (public April 1, 2026), https://arxiv.org/html/2604.00624v1.
- M. Pirani and S. Sundaram, *On the Smallest Eigenvalue of Grounded Laplacian Matrices*, arXiv:1406.2271 (public June 5, 2014), https://arxiv.org/html/1406.2271v2, especially Sections III–V.
- V. Tora and D. Vergni, *The critical patch size problem on networks*, Mathematical Biosciences 399 (2026) 109749, DOI:10.1016/j.mbs.2026.109749 (abstract inspected; full text unavailable).
- J. A. Tropp, *User-friendly tail bounds for sums of random matrices*, Foundations of Computational Mathematics 12 (2012), 389–434, arXiv:1004.4389, https://arxiv.org/abs/1004.4389.
