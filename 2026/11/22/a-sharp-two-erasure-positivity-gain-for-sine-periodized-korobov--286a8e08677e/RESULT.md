# A sharp two-erasure positivity gain for sine-periodized Korobov quadrature

## Finding

Consider the unmodified optimal first-order periodic Korobov quadrature rule of Bartel–Gilbert–Griebel–Kuo–Sloan with the nonnegative periodization density \(\mu(t)=\frac{\pi}{2}|\sin(2\pi t)|\). For each **even** integer \(N\ge 8\), start with the complete grid \(\{j/N:0\le j<N\}\) and delete **both** grid sites at the density zeros \(0\) and \(1/2\). Denote the remaining \(N-2\) nodes by \(X_N\). For \(\gamma>0\), use the *unmodified unconstrained kernel-optimal weights* \(w^{(N)}(\gamma)=G_{N,\gamma}^{-1}b_{N,\gamma}\), defined precisely below.

For every sufficiently large even \(N\), there is a finite positive threshold \(\Gamma_N^{\rm erase}\) with the sharp sign classification
\[
\begin{array}{ll}
0<\gamma<\Gamma_N^{\rm erase}:&\text{every weight is strictly positive},\\
\gamma=\Gamma_N^{\rm erase}:&\text{exactly the four sites }1/N,\ 1-1/N,\ 1/2-1/N,\ 1/2+1/N\text{ have zero weight},\\
\gamma>\Gamma_N^{\rm erase}:&\text{at least one weight is strictly negative}.
\end{array}
\]
The threshold has the **sharp two-term large-grid asymptotic**
\[
\boxed{\Gamma_N^{\rm erase}=\frac73 N+\frac{49\pi^2}{27}+O(N^{-1}).}
\]
By contrast, for the *complete* grid the established threshold is \(\Gamma_N^{\rm full}=N+\pi^2/3+O(N^{-1})\). Therefore deleting the two zero-density sites—rather than adding nodes—raises the admissible kernel-parameter scale by the exact asymptotic factor \(7/3\):
\[
\boxed{\lim_{N\to\infty,\ 2\mid N}\frac{\Gamma_N^{\rm erase}}{\Gamma_N^{\rm full}}=\frac73.}
\]
The claim is about the sign of *unconstrained optimal weights*, not positivity after clipping or renormalization, and the kernel parameter is allowed to grow with \(N\). For each fixed \(\gamma\), both designs eventually have positive weights.

More generally, for **any** circular grid with at least two distinct nodes, a nonnegative probability density \(\nu\) and the same first-order kernel, the optimal weights have an exact local-hat formula and a single scalar positivity test given in the proof. For the specified two-erasure design, the resulting finite-\(N\) threshold is explicit in one-dimensional integrals:
\[
\Gamma_N^{\rm erase}
=\frac{q_N}{2\pi^2 B_N-(\pi^2/3)q_N T_N},\qquad
T_N=\frac{N+12}{N^3},
\]
where \(q_N\) and \(B_N\) are exactly defined below; this formula holds whenever its denominator is positive, in particular for all sufficiently large even \(N\).

## Assumptions and scope

Work on the periodic circle \(\mathbb T=\mathbb R/\mathbb Z\). For \(\gamma>0\), the first-order Korobov reproducing kernel and its norm are
\[
K_\gamma(s,t)=1+\gamma\sum_{m\in\mathbb Z\setminus\{0\}}\frac{e^{2\pi i m(s-t)}}{m^2}
=1+2\pi^2\gamma B_2(\{s-t\}),\quad B_2(u)=u^2-u+\frac16,
\]
\[
\|f\|_\gamma^2=\left|\int_0^1f(t)\,dt\right|^2+
\frac1{4\pi^2\gamma}\int_0^1|f'(t)|^2\,dt.
\]
For any distinct ordered nodes \(0\le x_1<\cdots<x_m<1\), put \(x_{m+1}=x_1+1\) and interpret all intervals periodically. Let \(G_{ij}=K_\gamma(x_i,x_j)\) and \(b_i=\int_0^1K_\gamma(x_i,t)\nu(t)\,dt\). Every Fourier coefficient of the kernel is positive, hence \(G\) is strictly positive definite and \(w=G^{-1}b\) is uniquely defined. No postprocessing of \(w\) is allowed.

Let \(h_i=x_{i+1}-x_i>0\), with circular indexing, and let \(\phi_i\) be the piecewise-linear periodic cardinal hat equal to one at \(x_i\), zero at all other nodes and affine on every gap. Define the positive piecewise quadratic bubble \(Q(t)=(t-x_i)(x_{i+1}-t)\) for \(t\in[x_i,x_{i+1}]\), and
\[
a_i=\frac{h_{i-1}+h_i}{2},\quad t_i=\int_0^1\phi_i(t)\nu(t)\,dt,
\quad B=\int_0^1Q(t)\nu(t)\,dt,\quad T=\sum_i h_i^3.
\]
For the two-erasure grid \(X_N\), these become \(a_{N,i},t_{N,i},B_N,T_N\), with \(q_N=\min_i(t_{N,i}/a_{N,i})\). Since \(\mu>0\) away from two isolated points, every \(t_{N,i}\) and \(B_N\) is positive.

## Proof

**1. Exact interpolation formula on an arbitrary circular mesh.** The kernel interpolant of real nodal values \(v_i\) is the unique periodic interpolant \(S_v\) minimizing \(\|\cdot\|_\gamma\). Write \(L_v=\sum_i v_i\phi_i\) for its piecewise-affine interpolant and \(\bar S=\int_0^1S_v\). Variations vanishing at every node give the Euler–Lagrange equation \(S_v''=4\pi^2\gamma\bar S\) on every open gap: this follows directly from the displayed RKHS norm by integration by parts. Since \(Q''=-2\) on each gap, every solution with the prescribed nodal values has the form
\[
S_v(t)=L_v(t)-2\pi^2\gamma\bar S Q(t).
\]
The equality \(\int_0^1Q=T/6\), and \(\int_0^1L_v=\sum_i a_i v_i\), give
\[
\bar S=\frac{\sum_i a_iv_i}{1+\frac{\pi^2\gamma}{3}T},\qquad
S_v(t)=L_v(t)-\frac{2\pi^2\gamma Q(t)}{1+\frac{\pi^2\gamma}{3}T}\sum_i a_i v_i.
\]
This periodic function is continuous, interpolates the data and satisfies the variational equation; strict convexity of the norm yields uniqueness. Integrating it against \(\nu\), and independently using the kernel-interpolant identity \(S_v=\sum_i (G^{-1}v)_iK_\gamma(x_i,\cdot)\), proves the exact **unconstrained optimal-weight identity**
\[
\boxed{w_i=t_i-a_i c_\gamma,\quad c_\gamma=\frac{2\pi^2\gamma B}{1+(\pi^2\gamma/3)T}.}
\]
In particular, all optimal weights are nonnegative if and only if \(c_\gamma\le q:=\min_i t_i/a_i\). The scalar \(c_\gamma\) increases strictly with \(\gamma\), from zero toward \(6B/T\). If \(2\pi^2 B-(\pi^2/3)qT>0\), the unique crossing is at
\[
\Gamma=\frac{q}{2\pi^2 B-(\pi^2/3)qT}.
\]
Otherwise every positive parameter yields nonnegative weights. These formulas require no uniform mesh assumption.

**2. The two-erasure geometry.** Set \(h=1/N\). Erasing the sites \(0\) and \(1/2\) leaves two gaps of length \(2h\) (across the two zeros) and \(N-4\) gaps of length \(h\). Therefore
\[
T_N=2(2h)^3+(N-4)h^3=h^2+12h^3.
\]
The four remaining nodes closest to density zeros are \(h,1-h,1/2-h,1/2+h\). At the node \(h\), the hat is \((t+h)/(2h)\) on \([-h,h]\), and \((2h-t)/h\) on \([h,2h]\). Locally, \(\mu(t)=\pi^2|t|+O(|t|^3)\). Thus its hat mass is
\[
t_h=\pi^2h^2\left[\int_{-1}^1\frac{|u|(u+1)}2\,du+
\int_1^2u(2-u)\,du\right]+O(h^4)
=\frac76\pi^2h^2+O(h^4).
\]
The neighboring-gap area is \(a_h=3h/2\), so
\[
\frac{t_h}{a_h}=\frac79\pi^2h+O(h^3).
\]
Periodicity, reflection and half-periodicity give the same ratio at the other three indicated nodes. Every other retained node has two adjacent ordinary gaps and its hat support lies within one smooth half-period of \(\mu\). Direct tent convolution gives the exact expression
\[
\frac{t_j}{a_j}=\mu(x_j)\left(\frac{\sin(\pi h)}{\pi h}\right)^2
\]
for those nodes. Their nearest possible distance from a zero is \(2h\), so the minimum over this remaining set is \(2\pi^2h+O(h^3)\) as \(h\downarrow0\). Therefore, for all sufficiently large even \(N\), **exactly** the four nearest nodes attain
\[
q_N=\frac79\pi^2h+O(h^3).
\]

**3. Bubble-mass asymptotic with boundary checks.** For each ordinary gap, a second-order Taylor expansion about its midpoint and symmetry of \((t-x_i)(x_{i+1}-t)\) imply that its contribution to \(B_N\) differs from \(\frac{h^2}{6}\) times the density integral over that gap by at most \(O(h^5)\). The second derivative of \(\mu\) is uniformly bounded on any ordinary gap that avoids the density zeros. There are \(N-4\) such gaps. On each doubled gap the density is \(O(h)\), the bubble is \(O(h^2)\) and the length is \(O(h)\); its contribution and the corresponding \(\frac{h^2}{6}\)-weighted density integral are both \(O(h^4)\). Because \(\int_0^1\mu=1\), summing yields
\[
B_N=\frac{h^2}{6}+O(h^4).
\]
The two nondifferentiable zeros have thus been handled directly rather than subjected to a smooth Taylor expansion.

**4. Sharp crossing and both asymptotic coefficients.** Substituting the preceding expansions into the exact scalar crossing yields
\[
2\pi^2B_N-\frac{\pi^2}3q_NT_N
=\frac{\pi^2}{3}h^2-\frac{7\pi^4}{27}h^3+O(h^4)>0
\]
for all sufficiently small \(h\). The unique finite threshold therefore exists and equals
\[
\Gamma_N^{\rm erase}
=\frac{\frac79\pi^2h+O(h^3)}{\frac{\pi^2}{3}h^2-\frac{7\pi^4}{27}h^3+O(h^4)}
=\frac73h^{-1}+\frac{49\pi^2}{27}+O(h).
\]
The strict localization in Step 2 shows that precisely the four nearest-node weights reach zero simultaneously at equality. Monotonicity of \(c_\gamma\) proves strict positivity below and a negative weight above. The complete-grid threshold \(N+\pi^2/3+O(N^{-1})\) is a previously established comparison, and the ratio limit follows. \(\square\)

## Verification

The standalone \(\texttt{verify.py}\) uses two independent routes to evaluate finite-grid weights: (i) the local-hat/bubble formula derived here and (ii) solving the original dense positive-definite Gram system using separately integrated kernel means. It checks the exact gap-cube identity, sign behavior on both sides of the crossing, the four limiting minimal-hat sites, and the two-term asymptotic at increasing even grid sizes. A run returned \(\texttt{VERIFY_OK 74 checks}\). This test suite uses \(\texttt{numpy}\) and \(\texttt{scipy}\), with \(\texttt{python verify.py}\) in the extracted file directory. The finite checks support but do **not** establish the infinite-\(N\) assertion; Steps 1–4 are its proof.

## Relationship to prior work

Bartel et al. (2026) define exactly the sine-periodization measure, Korobov-kernel interpolation and (full or subsampled) optimal kernel quadrature weights, and identify asymptotic positivity in their multivariate setting as unresolved. Published analyses of the **complete** one-dimensional equispaced grid already determine its sharp \(N+\pi^2/3+O(N^{-1})\) threshold, its constant-function bias, and higher-order full-grid asymptotic positivity. Those results are comparison baselines, not claimed anew. They do not calculate the Gram inverse on the *erased* design or imply the new \(7/3\) factor by restriction: deleting nodes changes every optimal coefficient. The closest general Bayesian quadrature positivity analysis (Karvonen–Kanagawa–Särkkä, 2019) studies general positivity/stability criteria, rather than this two-erasure Korobov setting. Novak–Zhang (2016) derive weighted \(H^1\) optimal quadrature errors for arbitrary nodes under different norms/conditions; the present quantitative deletion law and mean-penalized periodic kernel parameter are not established in their inspected text.

## Limitations

The sharp deletion factor is proven only for the **one-dimensional first-order kernel** with exact sine-periodization density and the specified antipodal pair of erasures, in the large-even-\(N\) regime. The result does not classify arbitrary erasure patterns, random subsampling, multidimensional lattices, higher-order kernels, rounded floating-point coefficients or practical error improvements for a particular integrand. It concerns weight positivity, not monotonic improvement in quadrature accuracy; deleting points could worsen approximation quality. General kernel interpolation and spline variational principles are established background. The overlap search and available source inspection support an original *specific asymptotic classification* but cannot certify absolute historical priority.

## References

- F. Bartel, A. D. Gilbert, M. Griebel, F. Y. Kuo and I. H. Sloan, *A higher order lattice-based method for high-dimensional numerical integration using periodization*, arXiv:2610.01113v1 (2026-10-01), https://arxiv.org/html/2610.01113v1 .
- *Sharp positivity threshold for sine-periodized Korobov quadrature*, published result (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-positivity-threshold-for-sine-periodized-korobov-quadratur--f2630b796e0e .
- *Quantified asymptotic positivity for higher-order periodized Korobov quadrature*, published result (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-quantified-asymptotic-positivity-for-higher-order-periodized-kor--feb80935de99 .
- T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, Statistics and Computing 29 (2019), 1317–1333, https://doi.org/10.1007/s11222-019-09901-0 .
- E. Novak and S. Zhang, *Optimal Quadrature Formulas for the Sobolev Space H1*, arXiv:1609.01146v1 (2016), https://arxiv.org/pdf/1609.01146 .
