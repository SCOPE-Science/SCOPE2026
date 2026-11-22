# Complete positive spectrum and sharp modal relaxation for an expanding conditioned moving average

## Finding
Let \(a>0\), \(\theta>1\), \(q=1/\theta\), and \(c=a/(1+a)\). For independent innovations uniform on \([-a,1]\), impose the persistence inequalities \(X_{j+1}>\theta X_j\). Let \(T\) be the one-step killed transition operator on \(L^2([-a,1],dx)\):
\[
(Tf)(x)=\frac1{1+a}\int_{-a}^{1}{\bf1}_{\{y>\theta x\}}f(y)\,dy.
\]
Let \(E(q,z)=\sum_{k\ge0}q^{k(k-1)/2}z^k/k!\), and enumerate the strictly positive roots of \(E(q,-z)\) by \(0<z_1(q)<z_2(q)<\cdots\). The complete nonzero spectrum of \(T\), including algebraic multiplicities, is
\[
\sigma(T)\setminus\{0\}=\left\{\frac{c}{z_j(q)}:j=1,2,\ldots\right\}.
\]
Every listed eigenvalue is real, strictly positive, and algebraically simple. In particular there are no negative or nonreal nonzero eigenvalues.

On the effective conditioned state space \(\Omega=[-a,0)\), let \(h>0\) be the principal right eigenfunction of the restricted killed operator, and define the Doob transition \(Qf=h^{-1}T(hf)/(c/z_1(q))\), restricting its integrals to \(\Omega\). On \(\mathcal H=L^2(\Omega,h(x)^2dx)\), \(Q\) is compact, with its complete nonzero spectrum \(\{z_1(q)/z_j(q):j\ge1\}\). If \(\Pi\) denotes the rank-one Riesz projection for its stationary eigenvalue \(1\), then its *sharp spectral modal relaxation rate* is
\[
\lim_{n\to\infty}\|Q^n-\Pi\|_{\mathcal H\to\mathcal H}^{1/n}
=\frac{z_1(q)}{z_2(q)}.
\]
This is an operator-norm statement in the specified weighted Hilbert space, **not** a uniform total-variation mixing claim. The rate does not depend on \(a\), and as \(\theta\to\infty\),
\[
\frac{z_1(1/\theta)}{z_2(1/\theta)}\sim\frac1{2\theta}.
\]
The nonzero eigenvalues also obey the absolutely convergent power-sum identities
\[
\sum_j\lambda_j=c,\qquad \sum_j\lambda_j^2=c^2(1-q),\qquad
\sum_j\lambda_j^3=c^3(1-\tfrac32q+\tfrac12q^3).
\]

## Assumptions and scope
The inequalities are strict; replacing them by weak inequalities changes no law for continuous innovations. The parameter range is exactly \(a>0\) and \(\theta>1\), with \(q\in(0,1)\); no assertion is made at \(\theta=1\), for negative coupling, or for other innovation laws. Spectra are of bounded operators on the specified real/complex \(L^2\) spaces (interpreted over \(\mathbb C\) for spectral theory). The existence and positivity of \(h\) on \(\Omega\) and the nontrivial conditioned chain are supplied by the stated 2026 primary paper. The strict negative-to-negative transition kernel is used for the Doob chain; the killed operator on the entire innovation interval is retained for the full-spectrum assertion.

## Proof
**1. Triangular reduction.** Split \(L^2([-a,1])=L^2([-a,0])\oplus L^2([0,1])\). From a positive state no permitted next state is negative, so the killed operator is block upper triangular. Its positive-to-positive block \(V\) has kernel supported on \(y>\theta x>x\). Its \(n\)-step kernel is bounded by the ordinary strict-order simplex kernel, so \(\|V^n\|\le C^n/n!\), hence \(\sigma(V)=\{0\}\). Under \(x=-au\), \(y=-av\), the negative-to-negative block is unitarily equivalent (up to the harmless unitary normalization factor) to \(cK_q\) on \(L^2(0,1)\), where
\[
(K_qf)(u)=\int_0^{\min(u/q,1)}f(v)\,dv.
\]
The integral kernel is square-integrable, so \(K_q\) is compact. Block triangular spectral equivalence gives \(\sigma(T)\setminus\{0\}=c(\sigma(K_q)\setminus\{0\})\), with algebraic multiplicity conserved for nonzero eigenvalues.

**2. Determinantal discretization.** Set \(u_i=(i-1/2)/N\), and define the finite-rank midpoint-grid operator \(K_{q,N}\) with matrix entries \(A_{ij}=N^{-1}{\bf1}_{\{u_j<u_i/q\}}\). Regard it as a piecewise constant kernel on \([0,1]^2\). The discontinuity curve has area zero, and the grids converge to it in \(L^2\); hence \(\|K_{q,N}-K_q\|_{op}\to0\).

For a principal submatrix indexed by \(u_{i_1}<\cdots<u_{i_k}\), remove the factor \(N^{-1}\) from each row. Its \(j\)-th row contains a prefix of ones, and all entries on and below the diagonal are one. Successive row subtraction (from bottom to top) shows its determinant is **exactly one** if \(u_{i_j}\le q u_{i_{j+1}}\) for every \(j<k\), and is **zero** otherwise. Strict-versus-weak equality at finitely many grid points has no effect on the limit. Thus the coefficient of \((-z)^k\) in \(\det(I-zA_N)\) tends to the ordered-region volume
\[
\int_{0<u_1<qu_2<\cdots<qu_k<1}du_1\cdots du_k
=\frac{q^{k(k-1)/2}}{k!}.
\]
The equality follows by substituting \(u_j=q^{k-j}t_j\), transforming the region to \(0<t_1<\cdots<t_k<1\). Every finite coefficient is bounded in absolute value by \(\binom NkN^{-k}\le 1/k!\). Consequently, by dominated convergence of the polynomial series, \(\det(I-zA_N)\to E(q,-z)\) uniformly on compact complex sets.

**3. Identification of the entire nonzero spectrum.** Compact-operator norm convergence of \(K_{q,N}\) and uniform convergence of their determinant polynomials imply, through isolated-eigenvalue spectral perturbation and Hurwitz/Rouché's theorem, that reciprocal nonzero eigenvalues (with algebraic multiplicities) are exactly the zeros of \(E(q,-z)\). Indeed any isolated nonzero eigenvalue must arise as a limit of approximate eigenvalues, and every finite nonzero zero of the limiting determinant attracts the same number of zeros of the approximants. The deformed-exponential zero theorem (Morris et al., with the gap completed by Iserles, as documented by Wang–Zhang) gives infinitely many *simple negative real zeros* of \(E(q,z)\) and no other zeros for \(0<q<1\). Therefore the complete nonzero spectrum of \(K_q\) consists of the simple positives \(1/z_j(q)\).

**4. Conditioning and exact modal rate.** On \(\Omega\) use \(h\) and \(\lambda_1=c/z_1(q)\) from Aurzada–Worf. Multiplication \(Uf=hf\) is unitary from \(\mathcal H=L^2(\Omega,h^2dx)\) onto \(L^2(\Omega,dx)\) (\(h>0\) almost everywhere); it satisfies \(UQU^{-1}=T_{--}/\lambda_1\). Hence the eigenvalues of \(Q\) are precisely \(z_1/z_j\), all simple. Removing its rank-one Riesz projection \(\Pi\) leaves compact operator \(Q-\Pi\) with spectral radius \(z_1/z_2\). Since \(Q^n-\Pi=(Q-\Pi)^n\), Gelfand's formula proves the displayed root-norm limit.

**5. Critical scaling and power sums.** As \(q\downarrow0\), \(E(q,-z)=1-z+qz^2/2+O(q^3)\) uniformly for bounded \(z\), so its first root tends to one. For \(z=w/q\), \(qE(q,-w/q)=-w+w^2/2+q(1-w^3/6)+O(q^3)\) locally uniformly in \(w\); a Rouché argument near \(w=2\) produces a root \(z\sim2/q\). This is the **second** root: uniformly for \(B\le z\le(2-\varepsilon)/q\), the higher terms give \(E(q,-z)=1-z+qz^2/2+O(qz)\); choosing fixed large \(B\), then small \(q\), makes this expression negative, and the bounded interval contains only the first root. Hence \(z_2\sim 2/q\) and \(z_1/z_2\sim q/2\). Finally the classical large-index zero asymptotics imply \(\sum_j z_j^{-1}<\infty\), and the genus-zero factorization \(E(q,-z)=\prod_j(1-z/z_j)\) is legitimate. Comparing the first three coefficients and applying Newton identities proves the three stated eigenvalue power sums. These are sums of eigenvalues; no unsupported claim about operator trace class is needed.

## Verification
The accompanying `check.py` uses rational arithmetic to verify the principal-minor identity exhaustively for four rational dilation parameters, grid widths two through eight, and all tested principal sizes through five. It also checks the first three Newton power sums symbolically at those parameters, and independently compares the first two positive deformed-exponential roots against finite-grid matrix eigenvalues at three real parameters and three mesh sizes each. It reports 1,847 passing finite checks. These calculations do not establish the infinite zero theorem, compact spectral convergence, or the asymptotic rate: those are proved in the argument above or explicitly credited to prior literature.

At \(q=1/2\), numerical roots are approximately \(1.4880785456\) and \(4.8811408949\), giving modal ratio \(0.3048628543\). At \(q=1/4\) the ratio is approximately \(0.1367306010\), and at \(q=1/10\) approximately \(0.0517414581\). These are illustrations, not defining data.

## Relationship to prior work
Aurzada–Worf (2026, arXiv:2611.16041v1, Theorem 1.1(B)) construct the conditioned chain, determine its positive eigenfunction and **principal** eigenvalue as the inverse smallest deformed-exponential zero, and give stationary laws. Those results are explicitly used, not claimed as new. Aurzada–Raschel (2025) compute the entire **scalar persistence generating function**, including the expanding parameter range by duality, and therefore already expose the same deformed-exponential denominator and its candidate poles. The present claim is strictly the operator-level identification of **all** nonzero modes, simplicity, and the sharp weighted-Hilbert-space relaxation factor. No novelty is asserted for the deformed-exponential roots themselves: their reality, simplicity, and asymptotics are classical and are cited from Wang–Zhang and earlier authors.

The distinction from the scalar generating function is material: its poles identify only eigenmodes actually visible to a particular initial-observation pairing, whereas this result establishes exhaustiveness of the spectrum on the full state space and hence a worst-mode operator-norm rate. Similar-sounding results for the \(\theta=-1\) or non-expanding regimes involve different kernels and do not imply this spectrum. A historical paper could still have made the full operator connection implicitly; no claim of exhaustive historical uniqueness is made.

## Limitations
The assertion concerns \(\theta>1\) and \(a>0\) only, with the conditioned operator acting on the strictly negative effective state space. The sharp relaxation is in the special weighted \(L^2\) space and after removing the spectral projection; it does not assert a uniform total-variation bound. Existence of the conditioned kernel, the principal eigenfunction, and the real-simple-zero theorem are external established inputs. The checker provides finite consistency checks, not a proof. Independent external validation and historical priority adjudication have not occurred.

## References
- Frank Aurzada and Virginia Worf, *MA(1) processes with uniform innovations conditioned to stay positive in the expanding regime*, arXiv:2611.16041v1 (first publicly submitted 2026-11-11), https://arxiv.org/abs/2611.16041.
- Frank Aurzada and Kilian Raschel, *Persistence probabilities for MA(1) sequences with uniform innovations*, manuscript dated 2025-07-02, https://viasm.edu.vn/Cms_Data/Contents/viasm/Media/tienanpham2025/Persistence_MA_1_.pdf.
- Liuquan Wang and Cheng Zhang, *Zeros of the deformed exponential function*, arXiv:1709.04357 (2017), https://arxiv.org/abs/1709.04357. See its introduction for the Morris–Feldstein–Bowen and Iserles zero results and its large-index asymptotics.
- Frank Aurzada and Virginia Worf, *MA(1) processes with uniform innovations conditioned to stay positive in the non-expanding regime*, arXiv:2606.01832 (2026), https://arxiv.org/abs/2606.01832.
