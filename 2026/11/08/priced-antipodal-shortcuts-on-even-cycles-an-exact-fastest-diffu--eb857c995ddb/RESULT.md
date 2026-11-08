# Priced antipodal shortcuts on even cycles: an exact fastest-diffusion transition and a fourfold vanishing-budget gain

## Finding

**Theorem.** Fix an integer \(m\ge 4\), a positive budget \(B\), and a positive antipodal-edge price \(c\). Let \(G_m\) have vertices \(j\in\mathbb Z/(2m)\mathbb Z\), the \(2m\) cycle edges \(\{j,j+1\}\), and the \(m\) antipodal edges \(\{j,j+m\}\) for \(0\le j<m\). The edges have independent nonnegative conductances; cycle-edge price is one, and antipodal-edge price is \(c\). Maximize the second eigenvalue \(\lambda_2\) of the ordinary symmetric weighted graph Laplacian under total expense at most \(B\).

Set
\[
D_m=4\sin^2\left(\frac{\pi}{2m}\right),\quad
A_m=4\sin^2\left(\frac{\pi}{m}\right),\quad
c_m^*=\frac4{D_m}=\csc^2\left(\frac{\pi}{2m}\right).
\]
For \(m\ge4\), \(0<D_m<A_m\). Every global optimum assigns a common conductance \(a\) to all \(2m\) cycle edges and a common conductance \(b\) to all \(m\) antipodal edges. The complete classification is:

* If \(0<c<c_m^*\), the optimum is unique and
\[
a=\frac{2B}{m[4+c(A_m-D_m)]},\qquad
b=\frac{B(A_m-D_m)}{m[4+c(A_m-D_m)]},\qquad
\lambda_2^*=\frac{2A_mB}{m[4+c(A_m-D_m)]}.
\]
In this regime the ratio \(b/a=(A_m-D_m)/2\) is independent of \(c\).
* If \(c=c_m^*\), the entire optimal set is the one-dimensional closed segment
\[
0\le b\le \frac{BD_m(A_m-D_m)}{4mA_m},\qquad
a=\frac{B-mcb}{2m},\qquad
\lambda_2^*=\frac{D_mB}{2m}.
\]
* If \(c>c_m^*\), the unique optimum is \(a=B/(2m)\), \(b=0\), with \(\lambda_2^*=D_mB/(2m)\).

In particular, all globally optimal designs fund antipodal shortcuts if \(c<c_m^*\), none fund them if \(c>c_m^*\), and both support patterns are optimal at equality. For any fixed \(c>0\) and \(B>0\), as \(m\to\infty\) the optimally spent *fraction of the budget* on antipodal edges and the spectral-gap improvement over the best design forbidding those edges satisfy
\[
\frac{mc b}{B}\sim\frac{3c\pi^2}{4m^2},\qquad
\frac{\lambda_2^*}{D_mB/(2m)}\longrightarrow4.
\]
Also \(b/a\sim3\pi^2/(2m^2)\) and \(c_m^*=4m^2/\pi^2+1/3+O(m^{-2})\). Thus an asymptotically vanishing investment fraction quadruples the leading diffusion rate.

## Assumptions and scope

All graphs are undirected and have \(2m\) distinct vertices, where \(m\ge4\). All cycle and opposite-pair conductances may be independently chosen in \([0,\infty)\). The graph Laplacian is \(L=\sum_{\{i,j\}} w_{ij}(e_i-e_j)(e_i-e_j)^\top\) with its eigenvalues in increasing order, including multiplicity. No stochastic one-step normalization or intermediate Runge–Kutta stages are involved. The budget is \(\sum_{j=0}^{2m-1}a_j+c\sum_{j=0}^{m-1}b_j\le B\). The objective is \(\lambda_2(L)\), the continuous-time decay exponent for zero-mean states. At an optimum the budget is tight, because scaling a positive-gap feasible design upward increases \(\lambda_2\).

## Proof

**1. A universal two-mode upper bound.** Put \(\theta=\pi/m\), and define the average cycle and antipodal conductances
\[
\bar a=\frac1{2m}\sum_{j=0}^{2m-1}a_j,\qquad
\bar b=\frac1m\sum_{j=0}^{m-1}b_j.
\]
The vectors \(u^{(k)}_j=\cos(k\theta j)/\sqrt m\) and \(v^{(k)}_j=\sin(k\theta j)/\sqrt m\) are orthonormal, orthogonal to constants, for \(k=1,2\) and \(m\ge4\). Each pair has mean Rayleigh quotient equal to half the trace of the Laplacian on its span. For \(k=1\), every cycle edge contributes squared sine-plus-cosine difference \(D_m/m\) and every antipodal edge contributes \(4/m\). Thus the mean is \(D_m\bar a+2\bar b\). For \(k=2\), antipodal differences vanish, and the cycle-edge difference sum is \(A_m/m\), so the mean is \(A_m\bar a\). As \(\lambda_2\) cannot exceed either mean,
\[
\lambda_2(L)\le\min\{D_m\bar a+2\bar b,\ A_m\bar a\}.
\tag{1}
\]
The average rates obey \(2m\bar a+mc\bar b\le B\).

**2. Attainment for equal edge-class conductances.** When \(a_j=a\) and \(b_j=b\), the Fourier vectors \(\exp(i\pi kj/m)\) diagonalize the Laplacian, with eigenvalues
\[
\lambda_k=4a\sin^2\left(\frac{\pi k}{2m}\right)+2b\,\mathbf1_{\{k\text{ odd}\}},\qquad 0\le k<2m.
\]
The smallest positive even-frequency eigenvalue is \(A_ma\), and the smallest odd-frequency eigenvalue is \(D_ma+2b\). Therefore
\[
\lambda_2(L)=\min\{D_ma+2b,A_ma\}.
\tag{2}
\]
Consequently the right-hand side of (1), optimized over nonnegative average rates, is the true unrestricted optimum: imposing equal edge rates loses nothing *at the level of the optimal value*.

**3. Solve the scalar allocation exactly.** Full budget gives \(a=(B-mcb)/(2m)\), \(0\le b\le B/(mc)\). The two lines in (2) become
\[
F_{\rm odd}(b)=\frac{D_mB}{2m}+\left(2-\frac{D_mc}{2}\right)b,
\qquad
F_{\rm even}(b)=\frac{A_mB}{2m}-\frac{A_mc}{2}b.
\]
They cross at
\[
b_0=\frac{B(A_m-D_m)}{m[4+c(A_m-D_m)]},\quad
 a_0=\frac{2B}{m[4+c(A_m-D_m)]}.
\]
Here \(b_0>0\) and \(b_0<B/(mc)\). The even line decreases strictly. The odd line increases, is constant, or decreases according as \(c\) is below, equal to, or above \(4/D_m\). The maximum of their minimum is therefore attained uniquely at their crossing if \(c<4/D_m\), at every \(0\le b\le b_0\) if equality holds, and uniquely at \(b=0\) if \(c>4/D_m\). Substitution yields all stated rates and optimal eigenvalues.

**4. Rigidity: no asymmetric optima.** Let an arbitrary independently weighted design attain the unrestricted optimal value \(\Lambda\). Its mean rates achieve the scalar optimum, and in each of the three price regimes the first Fourier-pair upper bound in (1) equals \(\Lambda\). On the mean-zero subspace \(L-\Lambda I\) is positive semidefinite. Both vectors \(u^{(1)}\) and \(v^{(1)}\) have Rayleigh quotients at least \(\Lambda\), yet their average is exactly \(\Lambda\), hence each has Rayleigh quotient exactly \(\Lambda\). Positive semidefiniteness forces both to be eigenvectors with eigenvalue \(\Lambda\).

Write \(z_j=e^{i\theta j}\) and \(b_{j\bmod m}\) for the opposite-pair conductance at vertex \(j\). The two real eigenvector equations imply \(Lz=\Lambda z\). After dividing its component equation by \(z_j\),
\[
a_{j-1}(1-e^{-i\theta})+a_j(1-e^{i\theta})+2b_{j\bmod m}=\Lambda.
\tag{3}
\]
The imaginary part of (3) is \(\sin\theta\,(a_{j-1}-a_j)=0\). Since \(\sin\theta>0\), all \(2m\) cycle rates coincide. Its real part then forces all \(m\) antipodal rates to coincide as well. Hence (2)–(3) classify *every* optimum, not just invariant optima.

**5. Large-size effect.** Taylor expansion gives \(D_m=\pi^2/m^2+O(m^{-4})\) and \(A_m=4\pi^2/m^2+O(m^{-4})\). For fixed \(c>0\), the critical price \(4/D_m\) diverges, so the positive-chord case applies for sufficiently large \(m\). Its exact chord spending fraction is
\[
\eta_m=\frac{mc b_0}{B}=\frac{c(A_m-D_m)}{4+c(A_m-D_m)},
\]
which equals \(3c\pi^2/(4m^2)+O(m^{-4})\). The exact rate ratio to the cycle-only optimum is \(4A_m/[D_m(4+c(A_m-D_m))]\), converging to \(4\). The remaining asymptotics follow by the same expansions.

## Verification

Run `python3 verify.py` from the directory containing the attached verifier. The code uses only Python's standard library. It checks exact rational eigenvectors and budget identities in the excluded six-vertex boundary case, verifies general spectra using an independently implemented Jacobi diagonalization across several prices and sizes, tests independently weighted competitors against both Rayleigh bounds, and evaluates the asymptotic formulas. The delivered replay produced `VERIFY_OK 641`. The universal argument is the preceding proof; no finite battery of numerical tests certifies an infinite statement.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006) formulate continuous-time fastest mixing under priced linear edge budgets, including semidefinite duality, and solve the uniform-price cycle instance. The present result is a *specific closed-form classification* for a cycle augmented by an entire antipodal matching, including uniqueness of all unconstrained edge-wise optima and the critical price segment. Boyd, Diaconis, Parrilo and Xiao (2009) develop graph-automorphism and block-diagonalization methods for the discrete-time stochastic fastest-mixing problem; their inspected cases include cycles, wheels and complete multipartite graphs but not this priced continuous-time family. Shakeri and collaborators (2015) optimize one-to-one *interlayer* weights with fixed layer Laplacians, whereas the present problem funds both edge classes jointly on a Möbius ladder with a common budget.

The six-vertex realization \(G_3\cong K_{3,3}\) is covered by the matching-price optimization on balanced complete bipartite graphs. That case is deliberately excluded here by the condition \(m\ge4\). Other closely related priced-wheel and exceptional-cycle-edge optimizations change the graph and cost structure; none directly implies the full all-size antipodal-matching classification or its vanishing-budget fourfold gain. These comparisons do not establish absolute publication priority; see the limitations.

## Limitations

This theorem concerns even cycles of length at least eight with exactly the specified opposite-vertex matching, constant price within each edge orbit, and nonnegative freely selected undirected conductances. It makes no assertion for arbitrary sets of shortcuts, heterogeneous prices within an orbit, or discrete-time stochastic fastest mixing. The six-vertex case is intentionally excluded as already covered by a complete-bipartite matching-price classification. Literature checks included targeted records and primary texts, not a proof that no unindexed equivalent result exists.

## References

1. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699. DOI: 10.1137/S0036144504443821. First day-verified electronic publication: 2006-11-02. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM J. Optimization 20 (2009), 792–819. arXiv:0709.0955 (first posted 2007-09-06); https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
3. H. Shakeri, N. Albin, F. Darabi Sahneh, P. Poggi-Corradini, C. Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785 (first posted 2015-10-22). https://arxiv.org/abs/1510.06785.
