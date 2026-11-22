# Reversibility and a three-band minor sign law for geometric-minification count chains

## Finding

**Theorem.** Consider the stationary geometric NonLINAR(1) model of Barreto-Souza, Ndreca, Silva and Silva. For any positive finite thinning mean \(\alpha\) and marginal mean \(\mu\), let
\[
q=\frac{\alpha}{1+\alpha},\qquad r=\frac{\mu}{1+\mu},\qquad K=\frac{1-r}{1-qr}.
\]
Writing \(J_{ij}=\Pr(X_0=i,X_1=j)\) and
\[
D_{ij}=J_{ij}J_{i+1,j+1}-J_{i+1,j}J_{i,j+1},\qquad i,j\in\mathbb Z_{\ge0},
\]
the exact **complete adjacent-minor sign diagram** is
\[
\operatorname{sgn}(D_{ij})=
\begin{cases}1,&i=j,\\-1,&|i-j|=1,\\0,&|i-j|\ge2.\end{cases}
\]
The chain is nevertheless time-reversible, stochastically monotone, and positively quadrant dependent at every lag. At lag one the positive quadrant dependence is strict at all positive-integer thresholds. In particular its one-step probability kernel is **never TP2** (and does not have globally likelihood-ratio-monotone rows), for any \(\alpha,\mu>0\).

The structural mechanism is the independent one-step representation
\[
(X_0,X_1)\overset{d}=(W+E_0,W+E_1),
\]
where \(W\) is geometric on nonnegative integers with tail parameter \(qr\), \(E_0,E_1\) are iid, mutually independent of \(W\), and
\[
\Pr(E=0)=K,\qquad \Pr(E=n)=K(1-q)r^n\quad(n\ge1).
\]
This is an identity **for the consecutive stationary pair**, not a representation of an entire path using one fixed shared variable.

## Assumptions and scope

Fix \(0<q,r<1\). Let \(Z_t\) be iid with \(\Pr(Z_t=k)=(1-q)q^k\) for \(k\ge0\); let \(E_t\) be iid with the mass function above, independent of the past and of all \(Z_t\). Define
\[
X_{t+1}=\min\{X_t,Z_{t+1}\}+E_{t+1},\qquad
\Pr(X_0=k)=(1-r)r^k.
\]
Equivalently \(q=\alpha/(1+\alpha)\) and \(r=\mu/(1+\mu)\), where the two original model means are strictly positive and finite. The innovation distribution is normalized because
\(K[1+(1-q)r/(1-r)]=1\). This parameterization is exactly the stationary geometric special case in Definition 3 and equation (11) of the source paper. All assertions concern this stationary homogeneous model, not its nonstationary or zero-modified-marginal variants.

Here TP2 means that every \(2\times2\) determinant of a strictly positive pair-mass array is nonnegative; checking adjacent determinants is sufficient for such an array. Stochastic monotonicity means that \(x\mapsto\Pr(X_m\ge b\mid X_0=x)\) is nondecreasing, for each \(m\ge1\) and \(b\ge0\). Positive quadrant dependence means \(\Pr(X_0\ge a,X_m\ge b)\ge\Pr(X_0\ge a)\Pr(X_m\ge b)\).

## Proof

**Step 1: the generating function and independent shared-shock pair.** For every \(x\ge0\), direct geometric summation gives
\[
\mathbb E[t^{\min(x,Z)}]
=\frac{(1-q)+q(1-t)(qt)^x}{1-qt}.
\]
The innovation and stationary-marginal generating functions are
\[
B(z)=\frac{K(1-qr z)}{1-rz},\qquad
G(z)=\frac{1-r}{1-rz}.
\]
The first expression is precisely the algebraic form of the original innovation generating function, not a new marginal. For \(s,t\in[0,1]\), conditioning first on \(X_0\) and then on \(E_1\) gives
\[
F(s,t)=\mathbb E[s^{X_0}t^{X_1}]
=\frac{B(t)}{1-qt}\bigl[(1-q)G(s)+q(1-t)G(sqt)\bigr].
\]
Cancellation yields the exact factorization
\[
F(s,t)=B(s)B(t)\frac{1-qr}{1-qr st}.
\]
The last factor is the pgf of a nonnegative geometric \(W\) when both arguments are multiplied by \(W\), proving the pair representation. Taking either argument as \(1\) gives \(G\), verifying stationarity directly. Symmetry in \(s,t\) gives \(J_{ij}=J_{ji}\), hence \(\pi_iP_{ij}=\pi_jP_{ji}\) for \(\pi_i=(1-r)r^i\) and transition \(P_{ij}\). Detailed balance yields time reversibility of every finite stationary path.

**Step 2: exact neighboring-minor signs.** Put \(w_k=(1-qr)(qr)^k\) and \(e_0=K\), \(e_n=K(1-q)r^n\) for \(n\ge1\). The factorization implies
\[
J_{ij}=\sum_{k=0}^{\min(i,j)}w_ke_{i-k}e_{j-k}.
\]
For all \(j>i\), each summand has \(e_{j+1-k}=r e_{j-k}\), so \(J_{i,j+1}=rJ_{ij}\). At the diagonal the sole extra term gives
\[
\delta_i:=J_{ii}-\frac{J_{i,i+1}}{r}=w_iK^2q>0.
\]
Thus for \(j\ge i+2\), the four entries of the adjacent determinant obey the same column ratio \(r\), whence \(D_{ij}=0\). For \(j=i+1\), substituting the off-diagonal ratios gives
\[
D_{i,i+1}=-rJ_{i,i+1}\delta_{i+1}<0.
\]
Symmetry supplies the transposed signs. Finally \(J\) is a Gram matrix: define \(f_i(k)=\sqrt{w_k}\,e_{i-k}\) if \(0\le k\le i\), and zero otherwise, so \(J_{ij}=\langle f_i,f_j\rangle\). The vectors \(f_i\) and \(f_{i+1}\) are linearly independent because the latter alone has positive coordinate \(i+1\). Strict Cauchy–Schwarz therefore gives
\(D_{ii}=\|f_i\|^2\|f_{i+1}\|^2-\langle f_i,f_{i+1}\rangle^2>0\).
This establishes all indices, not just a finite numerical sample. In particular
\[
D_{0,0}=\frac{qr(1-r)^4}{(1-qr)^2}>0,\qquad
D_{0,1}=-\frac{q^2(1-q)r^3(1-r)^4}{(1-qr)^2}<0.
\]
Since multiplying each row by the strictly positive \(1/\pi_i\) preserves determinant signs, the transition kernel also fails TP2 at the same adjacent indices.

**Step 3: positive quadrant dependence and stochastic monotonicity.** In the independent-shock pair, for thresholds \(a,b\ge0\), both functions \(w\mapsto\Pr(E\ge a-w)\) and \(w\mapsto\Pr(E\ge b-w)\) are nondecreasing. The covariance inequality for two monotone functions of one variable proves nonnegative quadrant dependence. For \(a,b\ge1\) it is strict: both functions are below one at \(w=0\), equal one when \(w\ge\max(a,b)\), and \(W\) assigns strictly positive probability to both regions. For arbitrary lag \(m\ge1\), couple two chains starting from ordered states using identical independent future \((Z_t,E_t)\). The map \(x\mapsto\min(x,Z)+E\) preserves order pathwise. Thus the \(m\)-step transition kernel is stochastically monotone, and \(\operatorname{Cov}(1_{\{X_0\ge a\}},\mathbb E[1_{\{X_m\ge b\}}\mid X_0])\ge0\) proves positive quadrant dependence at every lag.

## Verification

The standalone `checks/check.py` performs symbolic generating-function factorization, symmetry, marginalization and the first two exact determinant formulas, as well as rational one-step transition checks and the entire \(12\times12\) adjacent sign grid at a nonboundary rational parameter pair. Run from the extracted package directory using `python checks/check.py` with Python 3 and SymPy. Its execution returned `PASS: PGF identities, symmetry, marginals, signed minors and transitions`. The infinite-index and all-parameter results are established by the preceding analytic proof, **not** by the finite grid.

## Relationship to prior work

Barreto-Souza, Ndreca, Silva and Silva (2023), Definition 3 and equations (7)–(11), introduce precisely this stationary model, give its innovation law and derive a general consecutive-pair generating function (Proposition 7). Those formulas are **prior art**, and the factored generating function here is obtained from them by algebra. The additional statements are the independent common-shock interpretation, full stationary-path reversibility, the strict three-band signed-minor classification and the precise contrast between positive quadrant dependence, stochastic monotonicity and failure of TP2 for every interior parameter.

Littlejohn (1992) studies reversibility in other discrete minification/first-order-autoregression constructions, and Littlejohn (1996) studies reversible relationships of geometric-tailed models. Their abstracts indicate relevant background; their full results were not accessible for complete historical implication comparison. The claim does **not** assert that reversibility itself, geometric shared-shock distributions, or the general theory of TP2 and stochastic ordering originated here. A search of related published mathematical findings did not identify the joint theorem; absence of a match is not proof of novelty.

## Limitations

No assertion is made for \(q=0,1\), \(r=0,1\), nonstationary extensions, or models with nongeometric stationary marginals. The common-shock decomposition holds for each consecutive pair, not one global latent variable across all times. The proof establishes ordinary positive quadrant dependence, not TP2 or monotone likelihood-ratio dependence; indeed it explicitly refutes the latter. Historical priority remains qualified by inaccessible older full texts, and there has been no independent validation.

## References

1. W. Barreto-Souza, S. Ndreca, R. B. Silva, and R. W. C. Silva, “Non-linear INAR(1) processes under an alternative geometric thinning operator,” *TEST* 32 (2023), 695–725. First publicly available 25 February 2023. https://doi.org/10.1007/s11749-023-00849-y . Open-access full text: https://link.springer.com/article/10.1007/s11749-023-00849-y .
2. R. P. Littlejohn, “Discrete minification processes and reversibility,” *Journal of Applied Probability* 29 (1992), 82–91. https://doi.org/10.2307/3214793 . Publisher abstract inspected; full text unavailable.
3. R. P. Littlejohn, “A reversibility relationship for two Markovian time series models with stationary geometric tailed distribution,” *Stochastic Processes and their Applications* 64 (1996), 127–133. Relevant bibliographic/abstract information inspected; full text unavailable.
