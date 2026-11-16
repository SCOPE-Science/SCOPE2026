# Sharp theta-function conditioning threshold for circular Fock kernels

## Finding
In the analytic Bargmann–Fock space with kernel \(K(z,w)=e^{z\overline w}\), fix an integer \(n\ge2\) and a squared radius \(t>0\). Let \(z_j=\sqrt t\,e^{2\pi i j/n}\), \(j=0,\ldots,n-1\), and let \(G_n(t)\) be the Gram matrix of the unit-normalized evaluation kernels at these points. Write \(\kappa_n(t)=\lambda_{\max}(G_n(t))/\lambda_{\min}(G_n(t))\), the **squared** spectral condition number. Then:

1. \(\kappa_n(t)\) is continuous and **strictly decreasing** from infinity to one as \(t\) runs from zero to infinity. Thus, for every \(C>1\), there is a unique critical squared radius \(t_n(C)>0\) with \(\kappa_n(t_n(C))=C\).
2. For every fixed \(\alpha>0\),
\[
\lim_{n\to\infty}\kappa_n(\alpha n^2)=\frac{\vartheta_3(0,e^{-2\pi^2\alpha})}{\vartheta_4(0,e^{-2\pi^2\alpha})}=:\mathcal R(\alpha),
\]
where \(\vartheta_3(0,q)=1+2\sum_{k\ge1}q^{k^2}\) and \(\vartheta_4(0,q)=1+2\sum_{k\ge1}(-1)^kq^{k^2}\). In particular \(\mathcal R\) strictly decreases from infinity to one.
3. Consequently, for every prescribed \(C>1\), the unique \(\alpha_C>0\) solving \(\mathcal R(\alpha_C)=C\) gives the **sharp radius threshold**
\[
\lim_{n\to\infty}\frac{t_n(C)}{n^2}=\alpha_C,\qquad\lim_{n\to\infty}\frac{\sqrt{t_n(C)}}n=\sqrt{\alpha_C}.
\]
For instance, \(\alpha_2\) is approximately \(0.0906930202\). Each finite \(n\) threshold is exact by its monotone defining equation; no finite-\(n\) closed form is asserted.

## Assumptions and scope
The Fock norm is \(\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\). Unit-normalized kernel vectors are \(k_w(z)=e^{z\bar w-|w|^2/2}\). Matrix entries are \(G_{j\ell}=\langle k_{z_\ell},k_{z_j}\rangle\), with eigenvalues independent of matrix-convention conjugation. The number of nodes \(n\) varies while the exact prescribed squared condition ratio \(C\) stays fixed. This is conditioning of a finite Riesz family in the **full** Fock space, not a sampling frame for the entire infinite-dimensional Fock space. The area parameter in the Fock kernel is exactly one; for \(e^{\beta z\bar w}\), replace \(t\) by \(\beta t\).

## Proof
**(1) Exact spectrum and strict mixing.** Set \(\zeta=e^{2\pi i/n}\). The Gram matrix is circulant, with entries \(e^{t(\zeta^{j-\ell}-1)}\). Fourier diagonalization and the exponential series give its eigenvalues (up to reindexing)
\[
\lambda_{n,j}(t)=n e^{-t}\sum_{q=0}^{\infty}\frac{t^{j+qn}}{(j+qn)!}=n p_{n,j}(t),\quad 0\le j<n.
\]
The \(p_{n,j}(t)\) are strictly positive and constitute the residue distribution \(\mathbb P\{N_t\equiv j\pmod n\}\) for a Poisson random variable \(N_t\) of mean \(t\). This spectral formula is known in the coherent-state literature and is not claimed as new.

For every \(s>0\), independent Poisson increments give the circular convolution identity \(p_n(t+s)=p_n(t)*p_n(s)\). Every coordinate of \(p_n(s)\) is positive. Since \(p_n(t)\) is nonconstant for finite \(t>0\) (its nontrivial first Fourier coefficient is \(e^{t(\zeta-1)}\ne0\)), strict averaging implies
\[
\max_jp_{n,j}(t+s)<\max_jp_{n,j}(t),\qquad\min_jp_{n,j}(t+s)>\min_jp_{n,j}(t).
\]
Hence their ratio strictly decreases. As \(t\downarrow0\), the maximum tends to one and the minimum to zero; as \(t\to\infty\), the nontrivial Fourier coefficients \(e^{t(\zeta^k-1)}\) vanish, so all probabilities tend to \(1/n\). Continuity gives existence and uniqueness of \(t_n(C)\).

**(2) Uniform modular central limit with drifting phase.** Fourier inversion gives
\[
n p_{n,j}(t)=\sum_{\ell=0}^{n-1}\exp\!\big(t(e^{2\pi i\ell/n}-1)-2\pi i\ell j/n\big).
\]
For \(t=\alpha n^2\) and fixed signed index \(k\in\mathbb Z\), Taylor expansion gives
\[
\exp\!\big(t(e^{2\pi ik/n}-1)-2\pi ikj/n\big)=e^{-2\pi^2\alpha k^2+2\pi ik(\alpha n^2-j)/n}(1+O_{\alpha,k}(n^{-1})).
\]
For signed indices \(|k|\le n/2\), the modulus is at most \(e^{-8\alpha k^2}\), using \(1-\cos(2\pi k/n)\ge8k^2/n^2\). Dominated convergence in the discrete Fourier series, with finite fixed-frequency truncation before taking limits, yields **uniformly in \(j\)**
\[
n p_{n,j}(\alpha n^2)=H_\alpha((j-\alpha n^2)/n)+o(1),\quad H_\alpha(x)=\sum_{k\in\mathbb Z}e^{-2\pi^2\alpha k^2}e^{2\pi ikx}.
\]
The modular phase \((j-\alpha n^2)/n\) may depend on \(n\); uniform convergence, not a fixed-phase limit, is essential. As the phase grid has mesh \(1/n\), the largest and smallest of these sampled values tend to the continuous maximum and minimum of \(H_\alpha\).

**(3) Exact theta extrema and threshold.** For \(q=e^{-2\pi^2\alpha}\), the Jacobi product identity gives
\[
H_\alpha(x)=\prod_{m\ge1}(1-q^{2m})\big(1+2q^{2m-1}\cos(2\pi x)+q^{4m-2}\big).
\]
Each positive factor is strictly increasing in \(\cos(2\pi x)\), so \(H_\alpha\) has its unique maximum at integral \(x\), and unique minimum at half-integral \(x\), modulo integers. They are exactly \(\vartheta_3(0,q)\) and \(\vartheta_4(0,q)\); positivity of the latter follows from the product. This proves the displayed ratio limit.

The functions \(H_\alpha\) are the strictly positive wrapped Gaussian heat kernels, satisfying \(H_{\alpha+s}=H_\alpha*H_s\) with normalized circle convolution. Positive convolution strictly decreases the maximum and increases the minimum of the nonconstant continuous function \(H_\alpha\). Thus \(\mathcal R\) strictly decreases. As \(\alpha\to\infty\), the Fourier expansion tends uniformly to one. As \(\alpha\downarrow0\), the wrapped-Gaussian representation
\[
H_\alpha(x)=(2\pi\alpha)^{-1/2}\sum_{k\in\mathbb Z}e^{-(x+k)^2/(2\alpha)}
\]
shows \(H_\alpha(0)/H_\alpha(1/2)\to\infty\). Thus every \(C>1\) defines a unique \(\alpha_C\). For \(\alpha_-<\alpha_C<\alpha_+\), the ratio limit gives \(\kappa_n(\alpha_-n^2)>C>\kappa_n(\alpha_+n^2)\) for all sufficiently large \(n\). Finite-\(n\) strict monotonicity forces \(\alpha_-n^2<t_n(C)<\alpha_+n^2\). Let both brackets approach \(\alpha_C\) to prove the sharp limit.

## Verification
`CHECK.py` independently computes finite circular Gram eigenvalues by dense Hermitian diagonalization and residue Poisson summation, compares the theta crossover at multiple sizes, checks sampled monotonicity, and locates \(\alpha_2\). It passed 48 finite checks in the stated environment with NumPy/SciPy. Finite tests do not prove uniform convergence, strict monotonicity for every real parameter, or the infinite-dimensional definition of the Fock space; those facts are proved above.

## Relationship to prior work
Horoshko, De Bièvre, Kolobov, and Patera (2016), equations (5)–(9), already give the **exact Poisson-residue Gram eigenvalues** for circular coherent states; these are expressly prior. De Bie, De Martino, and Diki (2025) give the analytic Gaussian Fock kernel as the base of their polyanalytic Gaussian-RBF construction. Gröchenig and Ortega-Cerdà (2022) study polynomial Fock sampling and interpolation inequalities with a different sampling regime. The present finite-orbit theorem concerns the previously unidentified strictly monotone squared-condition profile and its sharp **growing-orbit, radius-squared \(n^2\), theta-function threshold**. The finite spectrum by itself does not state this asymptotic or prove that its phase-shifted extremal samples converge uniformly. The derivation uses additional modular local-limit and heat-kernel monotonicity arguments.

## Limitations
The claim is restricted to equally spaced points on a circle, the classical analytic Gaussian Fock space, and a fixed target squared-condition ratio \(C>1\). It does not address optimal arrangements among all sets of \(n\) Fock nodes, variable \(C\), relative-error estimates in \(n\), or non-Gaussian Fock weights. An older equivalent theta crossover under quantum-coherent-state or random-walk terminology is a publication-priority risk; no independent audit has occurred.

## References
1. H. De Bie, A. De Martino, and K. Diki, *Polyanalytic Gaussian Radial Basis Function Kernel and Itô-Hermite Polynomials*, arXiv:2510.14639, first publicly posted 2025-10-16; Section 2.1 for the analytic Fock kernel.
2. D. B. Horoshko, S. De Bièvre, M. I. Kolobov, and G. Patera, *Entanglement of quantum circular states of light*, arXiv:1602.07852 (2016); Section II.A, equations (5)–(9).
3. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz–Zygmund inequalities for polynomials in Fock space*, Math. Z. 302 (2022), 1409–1428; doi:10.1007/s00209-022-03087-4.
4. Standard Jacobi triple-product identity and Poisson summation formula, with the theta normalizations explicitly defined above.
