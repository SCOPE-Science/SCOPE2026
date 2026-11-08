# A Poisson hard-edge law for a correlated Gaussian cyclic Gabor basis

## Finding
For each integer \(p\ge3\) put \(N=2p\). Let \(g=(g_0,\ldots,g_{N-1})\in\mathbb C^N\) have independent circular complex Gaussian entries with \(\mathbb E|g_j|^2=1/N\). Let the \(N\)-by-\(N\) synthesis matrix \(G_p\) have the columns
\[
M_{2\ell}T_k g,\qquad 0\le\ell<p,\quad k\in\{0,1\},
\]
where \((T_k g)_j=g_{j-k\pmod N}\) and \((M_hg)_j=e^{2\pi i hj/N}g_j\). Write \(S_p=G_pG_p^*\) and \(A_p=\lambda_{\min}(S_p)\), the optimal lower frame bound. The matrix \(G_p\) is invertible almost surely, and the sharp lower-bound scaling is
\[
\boxed{\lim_{p\to\infty}\mathbb P(pA_p>t)=e^{-4t}\quad\text{for every }t\ge0.}
\]
More precisely, for fixed \(t>0\), the number \(Z_{p,t}\) of two-dimensional Fourier fibers with least eigenvalue at most \(t/p\) converges in total variation to a Poisson law of mean \(4t\). The total-variation error is \(O_t((\log p)/p)\). Thus \(pA_p\) converges in distribution to an exponential random variable of rate four, and for every real \(r>0\),
\[
\boxed{\lim_{p\to\infty}\mathbb E[(pA_p)^r]=\frac{\Gamma(r+1)}{4^r}.}
\]
The constants refer to the stated complex-Gaussian variance, unnormalized time-frequency shifts, and frame-operator (squared singular value) convention.

## Assumptions and scope
All vector indices are cyclic modulo \(2p\). A circular complex Gaussian of variance \(v\) means that its real and imaginary parts are independent \(N(0,v/2)\). The modulation subgroup consists of the even residues and the translation set consists of two adjacent residues. Every finite \(p\ge3\) is included in the exact block identities and almost-sure invertibility; the distributional and moment conclusions concern \(p\to\infty\). The assertion is for a square, critically sized Gabor matrix, not for an oversampled frame.

For a positive Hermitian matrix \(H\), \(\lambda_{\min}(H)\) denotes its smallest eigenvalue. Total variation is \(d_{\mathrm{TV}}(\mu,\nu)=\sup_E|\mu(E)-\nu(E)|\). The Poisson count convergence is a fixed-threshold statement, not a claim of convergence of the entire eigenvalue point process.

## Proof
**1. Exact correlated two-by-two blocks.** Orthogonality of the \(p\) even-modulation characters gives
\[
S_p(i,j)=p\,\mathbf1_{i\equiv j\ (\mathrm{mod}\ p)}\sum_{k=0}^1g_{i-k}\overline{g_{j-k}}.
\]
Thus, after grouping the coordinates \((j,j+p)\), \(0\le j<p\), the operator is a direct sum of \(p\) Hermitian blocks. Put
\[
a_j=\sqrt p\,(g_j,g_{j+p})^T\in\mathbb C^2,
\qquad U=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
These \(a_j\) are independent circular complex Gaussian vectors of covariance \(\tfrac12 I_2\). With \(b_j=a_{j-1}\) for \(1\le j<p\) and \(b_0=Ua_{p-1}\), the \(j\)-th block is exactly
\[
W_j=[a_j,b_j][a_j,b_j]^*.
\]
The swap at \(j=0\) is forced by the cyclic translation; omitting it gives a different finite matrix. Write \(L_j=\lambda_{\min}(W_j)\). Then \(A_p=\min_{0\le j<p}L_j\). Every block has two independent Gaussian columns, hence is positive definite almost surely. Blocks with nonadjacent indices on the cyclic \(p\)-cycle are independent. Adjacent blocks share exactly one Gaussian vector. The boundary swap is unitary and preserves the isotropic Gaussian law.

**2. Exact single-block hard-edge probability.** The two-by-two complex Wishart density for a matrix \(W=[a,b][a,b]^*\) with independent \(\mathcal N_{\mathbb C}(0,\tfrac12 I_2)\) columns is proportional to \(e^{-2\operatorname{tr}W}\) on the cone of positive Hermitian matrices. (The determinant-power factor is zero because the Gaussian matrix is square.) Translating that cone by \(xI_2\) yields, for every \(x\ge0\),
\[
\mathbb P\{\lambda_{\min}(W)>x\}
=\frac{\int_{W>xI_2}e^{-2\operatorname{tr}W}\,dW}
{\int_{W>0}e^{-2\operatorname{tr}W}\,dW}=e^{-4x}.
\]
Equivalently, this follows by translating both variables in the standard complex-Wishart eigenvalue density proportional to \(e^{-2(\lambda_1+\lambda_2)}(\lambda_1-\lambda_2)^2\). Therefore
\[
\mathbb P(L_j\le\varepsilon)=q_\varepsilon=1-e^{-4\varepsilon}
\]
exactly for all \(j\), including the swapped boundary block.

**3. Adjacent small eigenvalues do not cluster.** Consider adjacent blocks sharing a vector \(b\), conditional on which their other Gaussian columns are independent. The conditional probability of a small least eigenvalue depends only on \(s=\|b\|^2\), since multiplication by a fixed unitary is immaterial. Let this probability be \(q(\varepsilon,s)\). Decompose an independent Gaussian column \(a=z e_1+w e_2\) in an orthonormal basis with \(e_1=b/\sqrt s\). Then \(z,w\) are independent circular Gaussians of variance \(1/2\). For the Gram matrix of \([a,b]\), the determinant is \(s|w|^2\), whereas its largest eigenvalue is at most \(s+|z|^2+|w|^2\). Consequently, whenever \(s\ge2\varepsilon>0\), the event \(\lambda_{\min}\le\varepsilon\) implies
\[
|w|^2\le 2\varepsilon(1+|z|^2/s).
\]
Because \(\mathbb P(|w|^2\le u)=1-e^{-2u}\le2u\) and \(\mathbb E|z|^2=1/2\),
\[
q(\varepsilon,s)\le4\varepsilon\left(1+\frac1{2s}\right)
\quad\text{if }s\ge2\varepsilon,
\qquad q(\varepsilon,s)\le1\text{ otherwise}.
\]
The squared norm \(s\) has Gamma shape-two density \(4se^{-2s}\) on \((0,\infty)\). Conditional independence therefore gives
\[
\begin{aligned}
\mathbb P(L_j\le\varepsilon,L_{j+1}\le\varepsilon)
&=\mathbb E\big[q(\varepsilon,s)^2\big]\\
&\le\int_0^{2\varepsilon}4se^{-2s}\,ds
+16\varepsilon^2\int_{2\varepsilon}^\infty
4se^{-2s}\left(1+\frac1{2s}\right)^2\,ds\\
&=O\big(\varepsilon^2[1+|\log\varepsilon|]\big)
\qquad(\varepsilon\downarrow0).
\end{aligned}
\]
This bound holds for the two boundary-adjacent pairs as well: conditioning on their common vector, the other Gaussian vectors remain independent, and the swap preserves \(s\).

**4. Poisson approximation and sharp lower bound.** Fix \(t>0\), set \(\varepsilon=t/p\), and define \(I_j=\mathbf1_{\{L_j\le\varepsilon\}}\), so \(Z_{p,t}=\sum_j I_j\). For all sufficiently large \(p\), the cyclic neighborhoods \(\{j-1,j,j+1\}\) are a dependency graph, with marginal probability \(q_\varepsilon=1-e^{-4t/p}\). In the standard Arratia--Goldstein--Gordon two-moment Poisson bound, its first dependency sum is at most \(3p q_\varepsilon^2=O_t(p^{-1})\), its second is at most \(2p\,O(\varepsilon^2[1+|\log\varepsilon|])=O_t((\log p)/p)\), and the conditional dependence term is exactly zero because each indicator is independent of all indicators outside its cyclic neighborhood. Thus
\[
d_{\mathrm{TV}}\big(\mathcal L(Z_{p,t}),\mathrm{Poisson}(p q_\varepsilon)\big)
=O_t((\log p)/p).
\]
Since \(p q_\varepsilon=4t+O_t(p^{-1})\), the same estimate holds with mean \(4t\). The event \(pA_p>t\) is precisely \(Z_{p,t}=0\), proving the exponential survival limit and the stated fixed-\(t\) error. At \(t=0\), positivity holds almost surely and the survival probability is exactly one.

**5. Convergence of all positive moments.** Choose \(\lfloor p/2\rfloor\) pairwise nonadjacent block indices on the cyclic graph; the associated least eigenvalues are independent. For every \(u\ge0\), the single-block exact survival gives
\[
\mathbb P(pA_p>u)\le
\exp\!\left(-\frac{4\lfloor p/2\rfloor}{p}u\right)
\le e^{-4u/3}\qquad (p\ge3).
\]
Using \(\mathbb E[X^r]=r\int_0^\infty u^{r-1}\mathbb P(X>u)\,du\) for \(r>0\), the uniform integrable majorant and pointwise survival limit yield \(\Gamma(r+1)/4^r\) by dominated convergence. This completes the proof.

## Verification
The accompanying `CHECK.py` uses only Python's standard library. It directly constructs the complete cyclic Gabor frame operator for multiple small values of \(p\) and checks every entry against the proposed block decomposition, including the swapped boundary. Seeded finite simulations check representative one-block and global survival probabilities against their analytical targets. Running `python CHECK.py` gave `GAUSSIAN_GABOR_HARD_EDGE_CHECKS_PASSED 11241`. The simulations are diagnostics and do not establish the Poisson limit; the proof is the exact block analysis, Wishart law, neighboring-event estimate, and Poisson approximation bound.

## Relationship to prior work
Asipchuk, De Carli, and Rodriguez established subgroup-induced block equivalence for finite Gabor systems, furnishing the general structural setting for this exact two-translation specialization. Their work does not provide a random-window hard-edge law. Salanevich and Salanevich--Strachan analyze extreme frame bounds for structured random Gabor systems but do not give the present rate-four Poisson limit for a square, one-dependent Gaussian block family. Classical complex Wishart theory gives the single two-by-two eigenvalue distribution, but by itself does not describe the minimum across the dependent cyclic blocks. The logarithmic determinant of this same cyclic Gaussian model is a different global invariant: neither its mean/variance nor its central limit behavior implies the least-eigenvalue law here. A matching sliding-block result under alternate terminology has not been conclusively excluded.

## Limitations
The complex Gaussian distribution, its variance, and the specified even-modulation/two-translation geometry are essential to the exact rate four as stated. There is no claim for real Gaussian windows, non-Gaussian universality, fixed-norm conditioned windows, arbitrary frequency subsets, or the maximum eigenvalue. The Poisson approximation concerns threshold counts individually, not full point-process convergence. The argument uses a standard dependency-graph Poisson bound as a cited theorem. Publication priority has not been independently certified.

## References
1. O. Asipchuk, L. De Carli, L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139v1 (first posted 2026-05-15), https://arxiv.org/abs/2605.16139 .
2. P. Salanevich, N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325v1 (2025), https://arxiv.org/abs/2509.01325 .
3. P. Salanevich, *Extreme Singular Values of Random Time-Frequency Structured Matrices*, arXiv:1902.01062v1 (2019), https://arxiv.org/abs/1902.01062 .
4. R. Arratia, L. Goldstein, L. Gordon, *Two moments suffice for Poisson approximations: the Chen--Stein method*, Annals of Probability 17 (1989), 9--25, https://doi.org/10.1214/aop/1176991491 .
5. T. Wirtz, T. Guhr, *Distribution of the smallest eigenvalue in complex and real correlated Wishart ensembles*, Journal of Physics A 47 (2014), 075004, https://arxiv.org/abs/1310.2467 .
