# Universal even-moment intermittency of root-branch imbalance in a recursive tree with doublings

## Finding

Consider the continuous-time root-doubling recursive tree after its first root doubling, initialized with one root and two single-vertex daughter subtrees. Denote the two daughter-subtree sizes by \(X_t\) and \(Y_t\), and write \(S_t=X_t+Y_t\), \(\Delta_t=X_t-Y_t\). For every **fixed** integer \(r\geq1\),

\[
\lim_{t\to\infty}\frac{\mathbb E[|\Delta_t|^{2r}]}{\mathbb E[S_t^r]}
= a_r
:=2^r(2r-1)!!\,\mathrm B(2^r-r,r+1)
=\frac{2^r(2r-1)!!(2^r-r-1)!r!}{(2^r)!}.
\]

In addition, both moments grow at the same exponent:

\[
\lim_{t\to\infty}\frac{1}{t}\log \mathbb E[|\Delta_t|^{2r}]
=\lim_{t\to\infty}\frac{1}{t}\log \mathbb E[S_t^r]
=\lambda_r:=r+2^r-1.
\]

For \(r=1,2,3,4,5\), the universal ratios are \(1,1,3/7,1/13,5/899\). In particular, \(\mathbb E[\Delta_t^2]=3e^{2t}-4e^t+1\), \(\mathbb E[S_t^2]=12e^{5t}-9e^{2t}+1\), \(\mathbb E[\Delta_t^4]\sim12e^{5t}\), and \(\mathbb E[\Delta_t^6]\sim(792/35)e^{10t}\). Thus a perfectly symmetric duplication mechanism produces non-Gaussian, rapidly accelerating high-moment growth of the *difference* between its descendant populations.

## Assumptions and scope

The model is the continuous-time embedding of Björnberg and Mailler's root-doubling random recursive tree, not the distinct model permitting duplication at every vertex. After the initial doubling, each non-root vertex independently adds one child at rate one; the root independently rings at rate one and then replaces its two descendant subtrees by two identical copies of the entire pre-event tree. Therefore the branch sizes have transitions

\[
(X,Y)\mapsto(X+1,Y)\ \text{at rate }X,\qquad
(X,Y)\mapsto(X,Y+1)\ \text{at rate }Y,
\]
\[
(X,Y)\mapsto(1+X+Y,1+X+Y)\ \text{at rate }1,
\qquad (X_0,Y_0)=(1,1).
\]

The claims concern each fixed integer moment order as continuous time tends to infinity; they do not assert a common limiting distribution for an order that grows with time. The \(\mathrm B\) symbol is the ordinary Euler beta function. All moments are finite at every finite time.

## Proof

**1. Total-mass moments.** If \(S=X+Y\), then births occur at total rate \(S\), giving \(S\mapsto S+1\), and the root event gives \(S\mapsto2S+2\). Its generator on the monomial \(s^r\) is

\[
(\mathcal L s^r)(s)=s((s+1)^r-s^r)+(2s+2)^r-s^r
=\lambda_rs^r+\sum_{j=0}^{r-1}c_{r,j}s^j,
\]

where \(\lambda_r=r+2^r-1\), \(c_{r,0}=2^r\), and \(c_{r,j}=\binom r{j-1}+2^r\binom rj\) for \(1\le j<r\). All \(c_{r,j}\) are nonnegative. Writing \(M_r(t)=\mathbb E[S_t^r]\), induction on \(r\) using variation of constants and the strict inequalities \(\lambda_j<\lambda_r\) for \(j<r\) shows

\[
0<C_r:=\lim_{t\to\infty}e^{-\lambda_rt}M_r(t)<\infty,
\qquad M_r(t)\le K_r e^{\lambda_rt}
\]

for a finite \(K_r\). In particular \(C_1=3\), \(C_2=12\), and \(C_3=264/5\). The same leading asymptotic holds for \(\mathbb E[(S_t+1)^r]\), because the lower moments have strictly smaller exponents.

**2. Condition on the last root event.** Root rings form a rate-one Poisson process independent of all non-root clocks. If the last root ring before \(t\) occurred at \(s=t-u\), each daughter subtree at that ring had exactly \(N_s:=S_{s-}+1\) vertices. During the subsequent root-free time \(u\), the two daughter subtrees independently follow unit-rate Yule pure-birth processes started from \(N_s\) individuals. A Yule process started from one individual at time \(u\) is geometric on the positive integers, with mean \(e^u\) and variance \(e^u(e^u-1)\).

Let \(H_r(N,u)\) be the \(2r\)-th moment of the difference of two independent such Yule processes, each started from \(N\) individuals. By expressing the difference as a sum of \(N\) independent centered differences of geometric variables, the moment partition formula gives

\[
H_r(N,u)=(2r-1)!!\,[2e^u(e^u-1)]^rN^r+R_r(N,u),
\]
\[
|R_r(N,u)|\le K'_r(1+N^{r-1})e^{2ru}.
\]

Indeed, the unique terms of degree \(r\) in \(N\) pair all \(2r\) factors; every other contributing partition has at most \(r-1\) distinct summand labels. Geometric-variable moments of order at most \(2r\) are bounded by a constant times \(e^{2ru}\), uniformly for \(u\ge0\). This also handles \(r=1\) (when the remainder actually vanishes).

Poisson last-event decomposition, including the possibility of no root ring since initialization, is the exact identity

\[
\mathbb E[|\Delta_t|^{2r}]
=e^{-t}H_r(1,t)+\int_0^t e^{-u}\mathbb E[H_r(S_{t-u}+1,u)]\,du.
\]

The pre-event distribution in the integral is the unconditional tree distribution at deterministic time \(t-u\), because the root clock is independent of the non-root evolution.

**3. Extract the leading term.** The no-ring term is \(O(e^{(2r-1)t})\). By step 1, the remainder in the integral is bounded by a constant times

\[
\int_0^t e^{(2r-1)u}(1+e^{\lambda_{r-1}(t-u)})\,du
=O\!\left((1+t)e^{\max(2r-1,\lambda_{r-1})t}\right),
\]

with \(\lambda_0=0\). Since \(\lambda_r>\max(2r-1,\lambda_{r-1})\) for every \(r\ge1\), both contributions are negligible compared to \(e^{\lambda_rt}\). The leading term, divided by \(C_re^{\lambda_rt}\), converges by dominated convergence to

\[
(2r-1)!!\,2^r\int_0^\infty e^{-(\lambda_r+1)u}e^{ru}(e^u-1)^r\,du.
\]

Substituting \(w=e^{-u}\) changes this integral to

\[
(2r-1)!!\,2^r\int_0^1 w^{2^r-r-1}(1-w)^r\,dw
=2^r(2r-1)!!\,\mathrm B(2^r-r,r+1)=a_r.
\]

It is finite and strictly positive because \(2^r-r>0\). Hence \(\mathbb E|\Delta_t|^{2r}\sim a_r C_r e^{\lambda_rt}\) and the two claims follow.

## Verification

The companion `verify_moments.py` reconstructs the two-dimensional jump generator on monomials \(S^a\Delta^b\) using integer polynomial arithmetic, checks the low-order generator identities, then independently extracts the leading \(e^{\lambda_rt}\) coefficients in the triangular exact-moment system through \(r=6\). All 284 exact assertions pass under Python 3's standard library. Its values agree with the beta-function formula for each tested order. These are finite cross-checks; the proof above establishes all fixed orders.

Reproduction: run `python3 verify_moments.py` from the directory containing this file and the script.

## Relationship to prior work

Björnberg and Mailler define the tree, its continuous-time Poisson-clock embedding, total-size asymptotics at discrete growth steps, and height/degree laws. Their Section 4.3 explicitly identifies the independent root clock and the Yule interpretation of non-root growth. The new calculation instead concerns the two *whole root-daughter masses*, which are reset identically at every doubling, and obtains their antisymmetric even-moment growth at **every order**.

Classical Yule-process and geometric moment formulas supply inputs, not the Poisson-last-reset moment comparison. Related published work on leaf-count imbalance and on the total-size weak limit concerns different observables and does not, in its accessible descriptions, state the root-daughter moment ratio. An implication from a more general, unlocated branching-with-reset theorem is not excluded.

## Limitations

The result uses a continuous-time origin immediately after a doubling, not a fixed number of discrete attachment steps. The exponent is a moment exponent and does not assert a typical-path rate or a central limit theorem. No independence of daughter subtrees is claimed across different root doublings; independence is conditional on the last doubling and the shared pre-event tree. The all-order formula has been proved analytically, but independently audited mathematical verification has not occurred. Historical priority cannot be proved from literature searches.

## References

1. J. E. Björnberg and C. Mailler, *A random recursive tree model with doubling events*, arXiv:2501.18466, first public version 30 January 2025, especially Sections 1, 2, and 4.3. https://arxiv.org/html/2501.18466
2. S. Janson, *Random recursive trees and preferential attachment trees are random split trees*, arXiv:1706.05487 (2017). https://arxiv.org/abs/1706.05487
3. Standard unit-rate Yule pure-birth law: the geometric one-family distribution and independent-branching property, as also used in Section 4.3 of Reference 1.
