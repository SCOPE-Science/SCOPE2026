# Half-order price scaling for antipodal rung deletion on Möbius ladders

## Finding

For every integer \(n\ge2\), form the Möbius ladder by taking the cycle on \(2n\) vertices \(0,\ldots,2n-1\) and adding the \(n\) antipodal edges \(\{j,j+n\}\), \(0\le j<n\). Each rim edge has unit price and each antipodal rung has unit price \(c>0\). Independently choose nonnegative conductances on all \(3n\) edges under the exact budget \(B>0\). For \(p>0\), minimize the inverse Laplacian spectral moment
\[
\Phi_p(L)=\sum_{k=2}^{2n}\lambda_k(L)^{-p}.
\]
A disconnected network has infinite objective. At \(p=0\), use \(\Phi_0=-\sum_{k=2}^{2n}\log\lambda_k(L)\), the determinant endpoint. The determinant-only result at \(p=0\) was previously established; the contribution here is the positive-order price threshold and its three-regime scaling.

**Unique unrestricted optimum and exact support rule.** There is one global minimizer among all independently adjustable edge conductances. It gives a common rim conductance \(a>0\) and common rung conductance \(b\ge0\). Put
\[
\mu_k=4\sin^2\!\left(\frac{\pi k}{2n}\right),\qquad k=1,\ldots,2n-1.
\]
Define
\[
C_{n,p}=\frac{4\displaystyle\sum_{\substack{1\le k<2n\\ k\ \mathrm{odd}}}\mu_k^{-(p+1)}}{\displaystyle\sum_{k=1}^{2n-1}\mu_k^{-p}},\qquad p>0,
\]
and at the determinant endpoint \(C_{n,0}=4\sum_{k\ \mathrm{odd}}\mu_k^{-1}/(2n-1)\). Then
\[
\boxed{\ b=0\quad\Longleftrightarrow\quad c\ge C_{n,p}.\ }
\]
If \(0<c<C_{n,p}\), every rim and rung receives positive conductance. The optimum is characterized exactly as the unique minimum of the following scalar objective over \(r=b/a\ge0\):
\[
\begin{aligned}
 a&=\frac{B}{n(2+cr)},&b&=ra,\\
 \Phi_p(r)&=\left(\frac{n(2+cr)}B\right)^p
 \left[\sum_{\substack{1\le k<2n\\k\ \mathrm{even}}}\mu_k^{-p}
 +\sum_{\substack{1\le k<2n\\k\ \mathrm{odd}}}(\mu_k+2r)^{-p}\right],\quad p>0.
\end{aligned}
\]
For \(p=0\), substitute the negative sum of logarithms of the nonzero eigenvalues \(a\mu_k\) for even \(k\) and \(a(\mu_k+2r)\) for odd \(k\). The unique interior optimum is equivalently the unique budget-feasible positive stationary point of this scalar objective.

**Exact endpoints and a sharp half-order transition.** The determinant threshold (already known) and the inverse-trace threshold are respectively
\[
\boxed{\ C_{n,0}=\frac{n^2}{2n-1},\qquad
C_{n,1}=\frac{n^2(n^2+2)}{4n^2-1}.\ }
\]
For each *fixed* real \(p\ge0\), as \(n\to\infty\), the entire price frontier has three regimes:
\[
\boxed{
C_{n,p}\sim
\begin{cases}
\displaystyle\frac{4(1-2^{-2p-2})\zeta(2p+2)}{\pi^{2p+2}I_p}\,n^{2p+1},&0\le p<\tfrac12,\\[6pt]
\displaystyle\frac{7\zeta(3)}{2\pi^2}\,\frac{n^2}{\log n},&p=\tfrac12,\\[6pt]
\displaystyle\frac{4(1-2^{-2p-2})\zeta(2p+2)}{\pi^2\zeta(2p)}\,n^2,&p>\tfrac12,
\end{cases}}
\]
where \(\zeta\) is the Riemann zeta function and
\[
I_p=\frac{4^{-p}\Gamma(\tfrac12-p)}{\sqrt\pi\,\Gamma(1-p)}\qquad(0\le p<\tfrac12).
\]
In particular, the price needed to delete every expensive antipodal rung grows linearly at determinant order, quadratically at inverse-trace order, and has a logarithmically corrected quadratic critical law at half order. For each fixed \(n\), the high-spectral-order limit is
\[
\lim_{p\to\infty}C_{n,p}=\csc^2\!\left(\frac\pi{2n}\right).
\]
The limits in the last display and the fixed-order asymptotics concern different limit procedures; no uniform-in-order error bound is asserted.

## Assumptions and scope

The graph is undirected, simple, and connected before any conductance is removed; only the specified rim and opposite-vertex edges may receive conductance. Prices are uniform *within* each of the two edge classes and strictly positive, and there are no capacities or integrality restrictions. The budget is spent exactly. The term \(\Phi_p\) always uses the positive eigenvalues on the mean-zero subspace; zero conductances that disconnect the graph give infinite cost. All uniqueness and optimal-support claims apply to the full independent-edge allocation, not merely the rotationally symmetric family.

## Proof

**1. Unique global optimizer and symmetry.** On the mean-zero subspace, a connected weighted graph Laplacian is positive definite. The spectral trace \(\operatorname{tr}(X^{-p})\) is strictly convex in a positive-definite symmetric matrix \(X\) for every \(p>0\): its second directional derivative in an eigenbasis is a positive sum of squared matrix entries, with diagonal coefficients \(p(p+1)\lambda^{-p-2}>0\) and off-diagonal coefficients equal to positive divided differences of the derivative of \(x^{-p}\). The same holds for \(-\log\det X\) at \(p=0\). The map from independent edge conductances to the restricted Laplacian is injective, since its off-diagonal entries, in the original vertex basis, recover every individual simple-graph edge weight. Consequently the objective is strictly convex in all \(3n\) conductances whenever connected. It diverges on the disconnected boundary, so a unique minimum exists in the compact budget simplex.

Rotating the vertex labels preserves the prices and both edge classes. By uniqueness, the global optimizer is invariant under all rotations and therefore has common rim conductance \(a\) and common rung conductance \(b\). Necessarily \(a>0\), because rungs alone form \(n\) disconnected pairs. The budget becomes \(2na+ncb=B\). Thus the entire unrestricted problem is exactly the scalar family above, after setting \(r=b/a\).

**2. Fourier eigenvalues.** On a Fourier mode \(v_j=\exp(\pi i k j/n)\), the cycle Laplacian contributes \(a\mu_k\). The antipodal matching contributes \(b(1-(-1)^k)\), giving
\[
\lambda_k=a\left(\mu_k+2r\mathbf1_{k\ \mathrm{odd}}\right),\qquad k=0,\ldots,2n-1.
\]
The mode \(k=0\) is the sole zero eigenvalue because \(a>0\). Substituting \(a=B/[n(2+cr)]\) yields the stated exact objectives.

**3. Threshold and all boundary cases.** For \(p>0\), differentiate the scalar objective at \(r=0\); its derivative has the sign of
\[
\frac c2\sum_{k=1}^{2n-1}\mu_k^{-p}
 -2\sum_{k\ \mathrm{odd}}\mu_k^{-(p+1)}.
\]
For \(p=0\), the analogous sign expression is \(c(2n-1)/2-2\sum_{k\ \mathrm{odd}}\mu_k^{-1}\). The coordinate \(r\) is monotone in the affine rung conductance \(b\in[0,B/(nc))\). Strict convexity along that actual affine budget segment makes a nonnegative right derivative at zero necessary and sufficient for the unique minimum to be \(b=0\). If negative, the minimum is interior: the other boundary \(a=0\) is disconnected and its objective diverges. Equality belongs to the zero-rung phase; no multiple optimum is introduced. This proves the exact price rule.

**4. Rational special cases.** The classical finite trigonometric sums
\[
\sum_{k=1}^{m-1}\csc^2(\pi k/m)=\frac{m^2-1}{3},\qquad
\sum_{k=1}^{m-1}\csc^4(\pi k/m)=\frac{m^4+10m^2-11}{45}
\]
follow, for example, by differentiating the cotangent multiplication identity. Subtracting the even-index sums of length \(n\) from the full length-\(2n\) sums gives
\[
\sum_{k\ \mathrm{odd}}\mu_k^{-1}=\frac{n^2}{4},\qquad
\sum_{k\ \mathrm{odd}}\mu_k^{-2}=\frac{n^2(n^2+2)}{48},\qquad
\sum_{k=1}^{2n-1}\mu_k^{-1}=\frac{4n^2-1}{12}.
\]
The two rational thresholds follow immediately. These formulae are independent of the budget \(B\).

**5. Three asymptotic price regimes.** Let \(S_{n,p}=\sum_{k=1}^{2n-1}\mu_k^{-p}\) and \(T_{n,p}=\sum_{k\ \mathrm{odd}}\mu_k^{-(p+1)}\). Since \(\mu_k\sim(\pi k/n)^2\) for fixed positive \(k\), and the spectrum is symmetric under \(k\mapsto2n-k\), dominated convergence after scaling by \(n^{2p+2}\) yields, for every fixed \(p\ge0\),
\[
T_{n,p}\sim\frac{2n^{2p+2}}{\pi^{2p+2}}\bigl(1-2^{-2p-2}\bigr)\zeta(2p+2).
\]
To justify domination, for \(1\le k\le n\), the inequalities \(2k/n\le2\sin(\pi k/(2n))\le\pi k/n\) bound the scaled summands by a multiple of \(k^{-2p-2}\), which is summable.

For \(0\le p<1/2\), the endpoint singularities of \((2-2\cos\theta)^{-p}\) are integrable. Riemann-sum convergence with a vanishing endpoint cutoff gives
\[
S_{n,p}\sim2n I_p,
\]
with the stated beta-integral value of \(I_p\). At \(p=1/2\), the two harmonic endpoint sums give \(S_{n,1/2}\sim(2n/\pi)\log n\). For fixed \(p>1/2\), the same dominated-convergence argument as for \(T_{n,p}\) yields \(S_{n,p}\sim2n^{2p}\zeta(2p)/\pi^{2p}\). Insert these three estimates into \(C_{n,p}=4T_{n,p}/S_{n,p}\). Finally, for fixed \(n\), the two modes \(k=1,2n-1\) uniquely have the smallest positive eigenvalue \(\mu_1\), and both are odd; consequently the threshold ratio tends to \(4/\mu_1=\csc^2(\pi/(2n))\) as \(p\to\infty\).

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It computes exact rational Moore–Penrose inverses for unweighted cycles with \(2n\) vertices for \(2\le n\le9\), independently recovering the sums and the inverse-trace threshold. It applies actual weighted Laplacians to complex Fourier eigenvectors for finite graph sizes, tests the interior and deleted-rung phases on both sides of the threshold, and checks numerical convergence in all asymptotic regimes. On this record it passed **15,506 finite assertions**. Finite tests do not establish universal uniqueness or infinite-size limits; the proof is analytical in the preceding steps.

## Relationship to prior work

Bailey and Cameron (2011) compare A- and D-optimality on fixed unweighted block-design graphs, including a Möbius ladder, and present general \(\Phi_p\) criteria. Their comparison does not optimize continuously chosen conductances at heterogeneous rim/rung prices. Ghosh, Boyd and Saberi (2006/2008) establish the general convex framework for total-effective-resistance allocation, but the inspected material does not provide this antipodal matching price frontier. Azimi and Farrokhi (2023) determine fixed-weight resistance and inverse-Laplacian quantities on ladders and Möbius ladders, not unrestricted price-dependent optimizers. The previously published Möbius-ladder D-optimal allocation result (published-finding corpus, 2026) already proves the exact \(p=0\) rung-deletion threshold; the present theorem **does not claim the determinant endpoint as new**. Its contribution is the positive real-order threshold and the sharp \(p=1/2\) boundary separating two price-scaling exponents, including the logarithmic law and explicit constants. General graph-design convexity, Fourier diagonalization, and standard zeta-sum asymptotics are antecedents, not asserted innovations.

## Limitations

Only the specified Möbius-ladder family with price-homogeneous edge classes is treated. The threshold is exact for each finite graph and real order, but the large-graph asymptotics hold for fixed order and give no simultaneous uniform bound as order varies with size. No formula in radicals is asserted for the interior optimum for arbitrary real order. The determinant endpoint is previously known, and generic one-dimensional spectral-density reasoning partly motivates the half-order boundary; the new assertion is the **exact priced Möbius-ladder design classification and its derived quantitative boundary**, not the general existence of spectral-density thresholds. An undiscovered equivalent specialized treatment remains possible; there has been no independent mathematical validation.

## References

1. R. A. Bailey and P. J. Cameron, *Using graphs to find the best block designs*, arXiv:1111.3768v1, first public 2011-11-16, especially Section 3.3 and the discussion of spectral criteria: https://arxiv.org/abs/1111.3768.
2. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS, July 2006; expanded SIAM Review 50 (2008), 37–66, DOI 10.1137/050645452: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.
3. A. Azimi and M. Farrokhi D. G., *Explicit formulas for matrices associated to ladder, circular ladder, and Mobius ladder graphs*, arXiv:2306.10497v1, first public 2023-06-18, especially Section 5: https://arxiv.org/html/2306.10497v1.
4. *Sharp rung-deletion prices and critical-scale D-optimality on Möbius ladders*, published-finding corpus 2026/10/18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-rung-deletion-prices-and-critical-scale-d-optimality-on-m--00e372929d94 (determinant case recovered here, not claimed new).
