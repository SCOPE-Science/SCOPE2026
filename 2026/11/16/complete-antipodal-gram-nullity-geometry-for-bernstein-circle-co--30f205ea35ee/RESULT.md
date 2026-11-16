# Complete antipodal Gram-nullity geometry for Bernstein circle covariances

## Finding

Let \(n\ge1\) be an integer and let \(f:[0,\pi]\to\mathbb R\) be a continuous isotropic positive-semidefinite circle kernel, written in its absolutely convergent cosine expansion
\[
f(x)=c_0+\sum_{m\ge1}c_m\cos(mx),\qquad c_0,c_m\ge0,\quad \sum_{m\ge1}c_m<\infty.
\]
Let \(Q_n=B_nf\) be the ordinary degree-\(n\) Bernstein polynomial on \([0,\pi]\), based on nodes \(j\pi/n\). Set
\[
O_n=\sum_{\substack{m\ge1\\m\text{ odd}}}c_m[1-\cos(m\pi/n)],\quad
E_n=\sum_{\substack{m\ge2\\m\text{ even}}}c_m[1-\cos(m\pi/n)],\quad
C_n=c_0+\sum_{j\ge1}c_{2nj}.
\]
All three quantities are nonnegative. For an arbitrary finite set \(S=\{e^{i\theta_1},\ldots,e^{i\theta_N}\}\) of **distinct** circle points, let \(p(S)\) count the antipodal pairs of points actually contained in \(S\), and let \(G_n(S)=[Q_n(d(\theta_j,\theta_k))]_{j,k=1}^{N}\), where \(d\) is circular geodesic distance in \([0,\pi]\). Then the exact complex nullity of this matrix is
\[
\dim\ker G_n(S)=
\begin{cases}
0,&O_n>0,\ E_n>0,\\
p(S),&O_n=0,\ E_n>0,\\
p(S),&O_n>0,\ E_n=0,\ C_n=0,\\
\max\{p(S)-1,0\},&O_n>0,\ E_n=0,\ C_n>0,\\
N-1,&O_n=E_n=0,\ C_n>0,\\
N,&O_n=E_n=C_n=0.
\end{cases}
\]
Consequently, \(Q_n\) is strictly positive definite on **every** set of distinct circle points if and only if \(O_nE_n>0\). At \(n=1\), this never occurs. At every \(n\ge2\), the degree-\(n\) Bernstein image of the finite-rank kernel \(\cos x+\cos(2x)\) is strictly positive definite on all finite distinct sets.

The exact mechanism is the following Fourier-tail law. With \(a_k=\frac2\pi\int_0^\pi Q_n(x)\cos(kx)\,dx\), for \(s\in\{0,1\}\) and positive \(k\to\infty\) along \(k\equiv s\pmod2\),
\[
 a_k=\frac{4n}{\pi^2 k^2}
 \sum_{\substack{m\ge1\\m\equiv s\ (\mathrm{mod}\ 2)}}c_m[1-\cos(m\pi/n)]
 +O_{f,n}(k^{-4}).
\]
If the corresponding leading sum vanishes, **every** positive-degree cosine coefficient of that parity vanishes identically. Otherwise, all sufficiently large coefficients of that parity are positive.

As an exact sampling-design corollary, for \(n=2\), \(f_\varepsilon(x)=1+\cos x+\varepsilon\cos(2x)\), \(\varepsilon>0\), and \(S_\delta=\{1,-1,e^{i\delta},-e^{i\delta}\}\), \(0<\delta<\pi\), write \(u=\delta/\pi\), \(D=1-2u\). The **complete** Gram spectrum is
\[
\operatorname{spec} G_2(S_\delta)=
\big\{4+2\varepsilon(1+D^2),\ 2\varepsilon(1-D^2),\ 4u,\ 4(1-u)\big\}.
\]
Among this entire antipodal-four-site family, the orthogonal-pair arrangement \(\delta=\pi/2\) uniquely maximizes the smallest eigenvalue and uniquely minimizes spectral condition number. The sharp values are, respectively,
\[
\max_{0<\delta<\pi}\lambda_{\min}=2\min\{\varepsilon,1\},\qquad
\min_{0<\delta<\pi}\frac{\lambda_{\max}}{\lambda_{\min}}=
\frac{2+\varepsilon}{\min\{\varepsilon,1\}}.
\]

## Assumptions and scope

The original kernel is real, continuous, isotropic, and positive semidefinite on the unit circle; its nonnegative cosine series and convergence are hypotheses. The input may have finite Fourier rank, may be identically zero, and need not itself be strictly positive definite. \(n\) is a positive integer, \(N\ge1\), the nodes are pairwise distinct, and Gram nullity is over \(\mathbb C\). Repeated nodes are excluded because they create trivial additional dependencies. All asymptotics fix \(f,n\) and let the integer Fourier index tend to infinity along the specified parity.

## Proof

**Step 1 (positive spectral coefficients and aliases).** The Bernstein positivity theorem of Otten–Nguyen–Watts proves that \(Q_n\) has nonnegative cosine coefficients \(a_k\), including the constant coefficient; we use that established theorem rather than reproving its general basis-positivity argument. For each integer \(m\ge1\), write \(R_{n,m}=B_n[\cos(mx)]\). Reflection of Bernstein nodes gives \(R_{n,m}(\pi-x)=(-1)^mR_{n,m}(x)\), and the first endpoint slope is
\[
R'_{n,m}(0)=\frac n\pi[\cos(m\pi/n)-1].
\]
If \(m\) is a positive multiple of \(2n\), then all sampled values are one and \(R_{n,m}\equiv1\). Otherwise the slope is strictly negative. Reflection forces \(R_{n,m}\) to have only positive-degree cosine frequencies of parity \(m\); odd \(m\) has no constant coefficient. Thus \(Q_n\) splits into a constant plus the two disjoint parity channels encoded by \(O_n,E_n\).

**Step 2 (tail constant and eventual full parity).** Twice integrating the cosine coefficient of the degree-\(n\) polynomial \(Q_n\) by parts, and integrating the remaining polynomial term again, gives
\[
 a_k=\frac2{\pi k^2}\big[(-1)^kQ'_n(\pi)-Q'_n(0)\big]+O_{f,n}(k^{-4}).
\]
The two endpoint derivatives from the sampling formula are
\[
 Q'_n(0)=\frac n\pi\big[f(\pi/n)-f(0)\big],\qquad
 Q'_n(\pi)=\frac n\pi\big[f(\pi)-f(\pi-\pi/n)\big].
\]
Insert the absolutely convergent cosine expansion, use \(\cos(m\pi)=(-1)^m\), and separate the parity \(k\equiv m\pmod 2\). This yields the stated \(4n/\pi^2\) constant with an \(O(k^{-4})\) remainder. If a sum is positive, its matching-parity coefficients are positive for every sufficiently large index. If it is zero, nonnegativity of each summand forces the corresponding sampled modes to be constant aliases (even \(m\equiv0\pmod{2n}\)) or absent (odd), so the entire positive-degree parity vanishes.

**Step 3 (exact finite nullspaces).** By the Bochner–Schoenberg Fourier expansion, for any coefficient vector \(z=(z_j)\in\mathbb C^N\),
\[
 z^*G_n(S)z=\frac{a_0}{2}\big|\sum_j z_j\big|^2+
 \frac12\sum_{k\ge1}a_k\Big(\big|\sum_j z_je^{ik\theta_j}\big|^2+\big|\sum_j z_je^{-ik\theta_j}\big|^2\Big).
\]
(The conjugate or sign convention for \(z\) is immaterial to the nullspace descriptions.) A vector lies in the kernel exactly when it annihilates every positive Fourier mode. In a parity channel with a full positive tail, all sufficiently large positive indices of that parity are positive; grouping the points by \(e^{2i\theta_j}\) and taking consecutive indices within that parity gives a finite Vandermonde matrix with distinct nonzero bases. Hence all group sums must vanish. An unpaired point has coefficient zero. A true antipodal pair has equal coefficients in the odd channel and opposite coefficients in the even channel.

If both channels occur, these relations force every coefficient to zero. If only the even channel occurs, each antipodal pair contributes the free difference vector \(e_{\theta}-e_{\theta+\pi}\), so nullity is \(p(S)\). If only the odd channel occurs, each pair contributes its sum vector \(e_{\theta}+e_{\theta+\pi}\); its coefficients are unrestricted when \(C_n=0\), and satisfy one independent total-sum condition when \(C_n>0\) and at least one pair is present. This yields the two odd-only cases. If neither channel occurs, \(Q_n\equiv C_n\), whose Gram rank is one when \(C_n>0\), zero otherwise. These are all cases, and exhibit actual bases for all asserted nullspaces.

**Step 4 (sharp four-site design).** Here \(Q_2(x)=2-2x/\pi+\varepsilon(1-2x/\pi)^2\). Ordering the nodes as \((0,\pi,\delta,\delta+\pi)\), its Gram matrix is diagonalized by the four orthogonal sign vectors \((1,1,1,1)\), \((1,1,-1,-1)\), \((1,-1,1,-1)\), and \((1,-1,-1,1)\). Their eigenvalues are the four values displayed above. The first is always the largest. The minimum of the other three is
\[
\lambda_{\min}=\min\{2\varepsilon(1-D^2),\,2(1-|D|)\}.
\]
Each term is strictly smaller when \(0<|D|<1\) than at \(D=0\), while the largest eigenvalue increases with \(D^2\). Therefore both optimality claims are strict and the displayed optimal values follow.

## Verification

`CHECK.py` runs exact SymPy coefficient, reflection, endpoint-derivative, parity, matrix-rank and four-site eigenvector tests for small degrees and aliases. The saved-script execution passed 1128 exact finite checks. These checks are not used as an infinite-degree proof. All universal claims follow from the cited positivity theorem, the endpoint calculation, and the finite Vandermonde argument above. The spectral optimization is an exact four-by-four diagonalization, not a numerical search.

## Relationship to prior work

Otten, Nguyen and Watts (arXiv:2608.04836v1, first public August 5, 2026) prove that Bernstein operators preserve **positive semidefiniteness** on the circle, including a basis coefficient formula, parity reflection, and \(O(k^{-2})\) tails. Their result and its endpoint lemma are indispensable inputs and are not claimed as new. The additional theorem here is the **exact nullity of every finite Bernstein covariance Gram matrix in terms of antipodal incidence**, with a sharp four-site condition-number design consequence. Classical circle strict-positive-definiteness criteria by Menegatto and Sun address Fourier supports in general, not this explicit node-by-node nullity law for Bernstein images.

## Limitations

The kernel must be a Bernstein polynomial sampled on the standard equispaced geodesic grid; other node choices are not classified. The method uses the previously published general Bernstein positive-semidefinite preservation theorem. Although no matching nullity classification was found in inspected sources, a condensed version may be considered a corollary of known endpoint and Fourier-support results; publication priority is provisional. The four-site optimization applies only to the displayed two-harmonic input and antipodal-pair designs, not all possible four-site configurations. No independent mathematical audit has been performed.

## References

1. M. Otten, N. Nguyen, T. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, arXiv:2608.04836v1 (2026-08-05), https://arxiv.org/abs/2608.04836.
2. V. A. Menegatto, *Strictly positive definite kernels on the circle*, Rocky Mountain J. Math. (1999), DOI:10.1216/RMJM/1181072211.
3. X. Sun, *Strictly positive definite functions on the unit circle*, Math. Comp. 74 (2005), 709–721, DOI:10.1090/S0025-5718-04-01668-0.
4. J. C. Guella, V. A. Menegatto, A. P. Peron, *Strictly positive definite kernels on a product of circles*, arXiv:1505.01169 (2015).
