# Exact endpoint decorrelation for the peak/valley dynamics of open meandric walks

## Finding

Consider the peak/valley walk dynamics introduced in the work of Wei [1], with the terminal free-end flip specified below. The stationary normalized endpoint autocorrelation of a walk of \(m\) increments has the exact expression

\[
C_m(t)=\sum_{k=1}^{m}\frac{r_{m,k}^{\,t}}{2m^2\sin^2(\theta_{m,k}/2)},\qquad
\theta_{m,k}=\frac{(k-\tfrac12)\pi}{m},\quad
r_{m,k}=1-\frac{1-\cos\theta_{m,k}}{m}.
\]

Its exact integrated value and cubic-time scaling profile are

\[
\sum_{t=0}^{\infty}C_m(t)=\frac{m(2m^2+1)}{3},\qquad
C_m(\lfloor sm^3\rfloor)\longrightarrow
F(s):=\sum_{k=1}^{\infty}\frac{2e^{-\pi^2(k-1/2)^2s/2}}{\pi^2(k-1/2)^2},\quad s\ge0.
\]

Every nontrivial fixed-correlation threshold is therefore crossed on the exact cubic time scale. In the original notation of a \(2n\)-step walk, the scale is \((2n)^3\). Numerically, the thresholds for correlation \(1/2\) and \(0.05\) have asymptotic times approximately \(3.14769183238n^3\) and \(18.0641180277n^3\), respectively, where \(n\) is half the number of increments.

## Assumptions and scope

Fix an integer \(m\ge1\). Initially each of the two walks has independent equiprobable increments in \(\{-1,+1\}\). For each update choose the top or bottom walk with probability \(1/2\), and independently choose an index \(j\) uniformly in \(\{1,\ldots,m\}\). If \(j<m\), exchange increments \(j\) and \(j+1\): this changes the path only when its vertex at \(j\) is a peak or valley. If \(j=m\), reverse increment \(m\); this is a flip of the free terminal vertex. All choices are independent across updates. This finite-state symmetric chain preserves the product uniform law. Let \(Y_t\) be the sum of the increments of the top walk after \(t\) updates and define \(C_m(t)=\mathbb E[Y_0Y_t]/m\), for every integer \(t\ge0\).

The end flip is essential: with only interior swaps the endpoint never changes. The numerical implementation accompanying [1] samples also an inert position \(j=0\); that variant is explicitly covered below. No claim is made about the crossing-event covariance or the full-map mixing time.

## Proof

**1. One-walk linear reduction.** Write the top increments as \(\varepsilon_i(t)\), \(1\le i\le m\). The bottom-walk updates leave them unchanged. For any fixed current configuration, averaging the next top update gives

\[
\mathbb E[\varepsilon(t+1)\mid\varepsilon(t)]
=\left(I-\frac{L_m}{2m}\right)\varepsilon(t)=P_m\varepsilon(t),
\]

where \(L_m\) is the symmetric tridiagonal matrix whose quadratic form is

\[
\langle x,L_mx\rangle=\sum_{j=1}^{m-1}(x_j-x_{j+1})^2+2x_m^2.
\]

For \(m\ge2\), its diagonal is \(1,2,\ldots,2,3\) and all adjacent off-diagonals are \(-1\); for \(m=1\), \(L_1=[2]\). Indeed an interior update exchanges two signs, and an end update reverses the last sign, causing the coefficient \(2\) in the terminal term. By iterated conditional expectation, \(\mathbb E[\varepsilon(t)\mid\varepsilon(0)]=P_m^t\varepsilon(0)\). The initial covariance matrix is the identity because the signs are independent and centered. Consequently

\[
C_m(t)=\frac1m\mathbf1^{\mathsf T}P_m^t\mathbf1.
\]

This is exact for all \(m\ge1\) and integer \(t\ge0\), with no independence assumption at later times.

**2. Exact half-integer spectral expansion.** For \(k=1,\ldots,m\) set \(\theta_{m,k}=(k-\tfrac12)\pi/m\) and \(v^{(k)}_j=\cos((j-\tfrac12)\theta_{m,k})\). The difference equation \((L_mv)_j=(2-2\cos\theta_{m,k})v_j\) follows from the ghost-site conditions \(v_0=v_1\) and \(v_{m+1}=-v_m\): the right condition holds since \(\cos(m\theta_{m,k})=0\). The modes are orthogonal, each with squared norm \(m/2\), and their coordinate sums obey

\[
\sum_{j=1}^m v^{(k)}_j=\frac{\sin(m\theta_{m,k})}{2\sin(\theta_{m,k}/2)}.
\]

Their squared projections of \(\mathbf1/\sqrt m\) are \(1/(2m^2\sin^2(\theta_{m,k}/2))\); inserting the eigenvalues of \(P_m\) yields the stated spectral formula. All bases \(r_{m,k}\) lie in \([0,1)\) (the zero mode occurs only at \(m=1\)), and the positive weights sum exactly to one by orthogonality.

**3. Integrated correlation.** As \(I-P_m=L_m/(2m)\) and \(L_m\) is positive definite,

\[
\sum_{t\ge0}C_m(t)=2\mathbf1^{\mathsf T}L_m^{-1}\mathbf1.
\]

A direct substitution shows that \(x_j=(m^2-j(j-1))/2\) is the unique solution of \(L_mx=\mathbf1\), including the \(m=1\) boundary case. Summing this vector gives \(\sum_j x_j=(2m^3+m)/6\); the exact cubic polynomial follows.

**4. Sharp scaling and thresholds.** For every fixed \(k\), as \(m\to\infty\),

\[
\frac{1}{2m^2\sin^2(\theta_{m,k}/2)}\to\frac{2}{\pi^2(k-1/2)^2},\quad
m^3(1-r_{m,k})\to\frac{\pi^2}{2}(k-1/2)^2.
\]

The weights are uniformly bounded by \(1/[2(k-\tfrac12)^2]\), using \(\sin u\ge2u/\pi\) for \(0\le u\le\pi/2\). This summable majorant proves convergence for every sequence \(t_m/m^3\to s\in[0,\infty)\), including \(s=0\), by dominated convergence, and the weights sum to one at \(s=0\). The resulting function \(F\) is continuous, strictly decreasing on \([0,\infty)\), with \(F(0)=1\) and \(F(s)\downarrow0\). Since each finite \(C_m\) is nonincreasing, the first threshold crossing at any fixed \(\eta\in(0,1)\) divided by \(m^3\) converges to the unique root \(F(s_\eta)=\eta\). In particular, the endpoint-decorrelation exponent in [1, Conjecture 4] is \(3\), whereas the crossing-decorrelation exponent is not addressed.

**5. Additional inert index used by the accompanying code.** If each update chooses uniformly from \(\{0,1,\ldots,m\}\), with index \(0\) inert, the same reasoning gives \(P_{m,\mathrm{inert}}=I-L_m/[2(m+1)]\). Thus replace the denominator \(m\) by \(m+1\) only in the spectral eigenvalue base (not in mode weights). The exact integrated value is then \((m+1)(2m^2+1)/3\), and the same limiting \(F(s)\) holds because \((m+1)/m\to1\).

## Verification

The standalone file `verify_meandric_endpoint.py` uses Python's exact rational arithmetic to construct the entire Markov transition kernel for all \(2^m\) sign configurations at \(m=1,\ldots,6\), for both sampling conventions. It independently compares finite-state autocorrelations with the linear recurrence and the spectral formula through thirteen updates; it checks the discrete Green function through \(m=100\) and verifies eigenvector identities and normalization. The actual completed run reported `VERIFY_OK checks=21378`. Finite-state diagnostics corroborate the derivation but do not establish the infinite-volume limit; the proof is the preceding analytic argument. Reproduce with `python3 verify_meandric_endpoint.py` in a standard Python 3 installation.

## Relationship to prior work

Wei [1] introduces exactly the walk peak/valley/free-terminal dynamics and conjectures distinct polynomial decorrelation exponents for walk endpoints and crossings. The present result settles the endpoint component: the scale exponent is exactly \(3\), with a full limiting crossover profile, exact finite-\(m\) formula and integrated correlation. Neither the conjecture nor its numerical fits provide an exact endpoint formula.

The reduction to the symmetric exclusion process with a reservoir at one end is standard. Santos and Schütz [2] analyze open exclusion processes, especially equal-time correlations during relaxation of a *semi-infinite* system. Their full paper establishes general Fourier/Bethe machinery; it does not state the exact **discrete-time**, finite-\(m\), stationary endpoint series, its integrated cubic polynomial, or the decay thresholds for Wei's dynamics. The more recent finite-reservoir hydrodynamic study [3] has different reservoir dynamics and observables. Thus the new content is the explicit resolution of a specific recent quantitative question using classical exclusion spectral methods, not a claim to have introduced exclusion processes or spectral diagonalization.

## Limitations

The claim concerns stationary endpoint autocorrelation of one encoded walk, not top/bottom crossing probabilities, a mixing-time upper bound for all observables, or any independence assertion about limiting geometries. Its proof assumes symmetric independent initial walk increments and the stated terminal flip; a dynamics omitting terminal flips conserves the endpoint and has a different answer. The finite-\(m\) constants depend on whether an inert index is sampled. The scaling statement is pointwise along all time sequences with finite nonnegative scaled limit, not uniform in unbounded scaled time. Full historical priority against all possible reformulations of exclusion-chain Green functions cannot be guaranteed.

## References

[1] David J. Wei, *Uniform meandric systems as percolation on planar maps: conjectures and a numerical study*, arXiv:2610.03730v1, first public submission 2026-09-09, Sections 4–6 and Appendix A. https://arxiv.org/abs/2610.03730 . Accompanying public code: https://github.com/davidw289/Meandric-System-Numerical-Analysis .

[2] J. E. Santos and G. M. Schütz, *Exact time-dependent correlation functions for the symmetric exclusion process with open boundary*, Physical Review E 64 (2001), 036107. https://doi.org/10.1103/PhysRevE.64.036107 . Author-available full text: https://juser.fz-juelich.de/record/46852/files/96.pdf .

[3] M. Franco, T. Franco and P. Gonçalves, *Finite reservoirs lead to Wentzell boundary conditions for independent random walks and exclusion process*, arXiv:2604.02579 (2026). https://arxiv.org/abs/2604.02579 .
