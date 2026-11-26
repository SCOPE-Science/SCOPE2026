# Sharp rate–noise Pareto frontier for two-row Markov Kaczmarz

## Finding

Let \(u_1,u_2\in\mathbb R^2\) be unit row normals with \(0<c=|u_1^{\mathsf T}u_2|<1\). At each update use a fresh centered observation error, drawn from a fixed law for the chosen row, of variance \(v_i>0\). Choose the rows with an exogenous stationary two-state Markov chain having switch probabilities \(\alpha=\Pr(I_{n+1}=2\mid I_n=1)\) and \(\beta=\Pr(I_{n+1}=1\mid I_n=2)\) in \((0,1]\). Put \(p=\beta/(\alpha+\beta)\). The unique stationary joint law of the row and error has finite second moments, and its expected squared error is
\[
R(p)=\frac{v_1+v_2+2c^2[pv_1+(1-p)v_2]}{1+c^2}.
\]
Thus the risk depends on row frequencies, not on switching persistence at fixed frequencies. The exact asymptotic worst-case synchronized mean-square contraction factor is
\[
\lambda(\alpha,\beta)=\frac{2-\alpha-\beta+\sqrt{(\alpha-\beta)^2+4\alpha\beta c^4}}{2}.
\]
For fixed \(p\), the fastest transition choice is unique and has \(\max(\alpha,\beta)=1\). Every visit to the less-frequent row is followed by an immediate switch. Independent choices with the same \(p\) have the same risk but strictly slower contraction for \(0<p<1\).

There is no feasible policy at a rate cap \(r<c^2\). For \(c^2\le r<1\), set
\[
z_r=\frac{r^2-c^4}{2r-r^2-c^4}.
\]
The minimum risk among policies with \(\lambda\le r\) is
\[
R_{\min}(r)=v_1+v_2-\frac{c^2|v_1-v_2|}{1+c^2}\,z_r.
\]
If \(v_1<v_2\), the unique optimizer chooses \(p=(1+z_r)/2\), \(\alpha=(1-p)/p\), and \(\beta=1\); if \(v_2<v_1\), interchange the labels. If \(v_1=v_2\), every feasible policy minimizes the risk. In particular, the optimizer at \(r=c^2\) is uniquely \(\alpha=\beta=1\) even when the variances are equal; for \(c^2<r<1\) and equal variances there are infinitely many optimizers.

## Assumptions and scope

With the consistent exact right-hand side subtracted, write \(P_i=I-u_iu_i^{\mathsf T}\) and update
\[
X_{n+1}=P_{I_{n+1}}X_n+\epsilon_{I_{n+1},n+1}u_{I_{n+1}}.
\]
The row chain is exogenous, stationary and irreducible. Conditional on the row path, innovations at distinct updates have independent row-specific laws; the law for each given row is independent of the update index and of past errors, centered, and of finite variance \(v_i\). Gaussianity is not assumed. Time-independent laws, not just time-independent variances, are imposed for stationarity of the joint law. The contraction factor concerns two runs sharing the row path and innovations, with initial discrepancies of finite second moment and exogenous future row transitions. At perfect alternation a fixed row phase need not converge in distribution to the invariant joint law.

## Proof

Choose unit vectors \(w_i\perp u_i\), so \(P_i=w_iw_i^{\mathsf T}\) and \(|w_1^{\mathsf T}w_2|=c\). Repeating a projection on a tangent discrepancy preserves its magnitude; switching multiplies that magnitude by \(c\). In particular, for any \(\ell\) row transitions the expected value of \(c^{2N_\ell}\), with \(N_\ell\) the number of switches, is bounded by \(\theta^\ell\), uniformly over the starting row, where \(\theta=1-(1-c^2)\min(\alpha,\beta)<1\). This follows by conditioning successively on the current row, since each conditional expected factor is at most \(\theta\).

Take a bi-infinite stationary row path and draw innovations with the stipulated conditional laws. At time \(n\) sum the contributions of innovations at times \(n-j\), \(j\ge0\), after their \(j\) subsequent projections. The expected squared norm of the term with \(j\ge1\) is at most \(\max_i v_i\,\theta^{j-1}\): the first projection has norm at most one, then all further projections act on a tangent vector. Given the row path, terms from different innovations have zero cross moments. The sum converges in \(L^2\), is stationary by shift invariance of the driving laws, and satisfies the recursion. To see uniqueness, couple any two invariant initial laws by giving them the same initial row (with its stationary marginal), common future rows, and common future innovations. Switches occur infinitely often almost surely, so their difference tends to zero almost surely, irrespective of the initial error norms. Testing with bounded Lipschitz functions of the row and error shows that the two invariant laws coincide. This construction and argument also apply at alternation.

Let \(S_i=\mathbb E[XX^{\mathsf T}\mid I=i]\) in stationarity, and write \(q_i=w_i^{\mathsf T}S_iw_i\). The last update eliminates the previous normal component and adds independent centered noise along \(u_i\), so
\[
S_i=q_iw_iw_i^{\mathsf T}+v_iu_iu_i^{\mathsf T}.
\]
The backward transitions equal the forward transitions by two-state detailed balance. Using \(|w_1^{\mathsf T}u_2|^2=|w_2^{\mathsf T}u_1|^2=1-c^2\) and canceling the positive switch probabilities from the two stationary recursions gives
\[
q_1=c^2q_2+(1-c^2)v_2,\qquad q_2=c^2q_1+(1-c^2)v_1.
\]
Consequently \(q_1=(v_2+c^2v_1)/(1+c^2)\) and \(q_2=(v_1+c^2v_2)/(1+c^2)\); averaging the two traces with weights \(p,1-p\) gives \(R(p)\).

For a synchronized discrepancy \(Y_n\), let \(t_{i,n}=\mathbb E[\|Y_n\|^2\mathbf1_{\{I_n=i\}}]\). After the first projection, the tangent rule gives
\[
\binom{t_{1,n+1}}{t_{2,n+1}}=M\binom{t_{1,n}}{t_{2,n}},\qquad
M=\begin{pmatrix}1-\alpha&\beta c^2\\ \alpha c^2&1-\beta\end{pmatrix}.
\]
The positive Perron root of this irreducible matrix is the stated \(\lambda\). A positive left Perron vector makes the left-weighted energy exactly proportional to \(\lambda^n\) on any nonzero nonnegative initial energy vector. Its weighted and unweighted energies differ by fixed positive multiplicative bounds, so \(\lambda\) is the sharp asymptotic factor even if the other eigenvalue is \(-\lambda\) at alternation.

Put \(k=\alpha+\beta\), so \(\alpha=(1-p)k\), \(\beta=pk\), and
\[
\lambda=1-\frac{k}{2}\bigl[1-\sqrt{1-4p(1-p)(1-c^4)}\,\bigr].
\]
The bracket is positive and \(0<k\le 1/\max(p,1-p)\), proving the unique best choice at fixed \(p\); iid picks have \(k=1\), strictly below that maximum. If \(z=|2p-1|\), the best rate at fixed frequency is
\[
L(z)=\frac{z+\sqrt{c^4+(1-c^4)z^2}}{1+z}.
\]
It is the positive root of \((1+z)L^2-2zL-c^4(1-z)=0\). It satisfies \(c^2\le L(z)<1\) for \(0\le z<1\): the quadratic is nonpositive at \(c^2\) and positive at 1. Implicit differentiation gives
\[
L'(z)=\frac{2L-L^2-c^4}{2(1+z)L-2z}>0,
\]
since the numerator is at least \(2c^2(1-c^2)\) and the denominator equals twice the positive square root in the expression for \(L\). Thus \(L\) increases from \(c^2\) toward 1. Solving \(L(z)=r\) gives \(z_r\), so a frequency is feasible precisely when \(|2p-1|\le z_r\). With unequal variances the affine risk fixes the extreme frequency toward the lower-noise row, and there the rate cap forces the best transition choice. With equal variances the risk is constant on all feasible policies. At the minimum rate, monotonicity forces \(p=1/2\) and the unique maximal \(k=2\), while for \(r>c^2\) an interval of \(k\) near 2 is feasible at \(p=1/2\). This proves the optimizer claims.

## Verification

The accompanying standard-Python verifier `verification/verify_markov.py` checks stationary-covariance identities and transfer-matrix invariants for 4,500 rational parameter tuples; its spectral-rate and rate-cap comparisons use floating point. Those tests supplement the analytic proof, which also resolves the optimizer multiplicity at the minimum cap. For row normals \((1,0)\), \((3/5,4/5)\), variances \((1,4)\) and first-row frequency \(3/4\), optimized transitions \((\alpha,\beta)=(1/3,1)\) yield risk \(313/68\) and contraction factor \((25+2\sqrt{217})/75\). Independent choices have the same risk and factor \((25+\sqrt{217})/50\).

## Relationship to prior work

Patel, Jahangoshahi and Maldonado treat randomized linear solvers under dependent and other sampling schemes, including Kaczmarz. Bergou et al. analyze randomized Kaczmarz on systems with noisy coefficients and right-hand sides; Wang, Agaskar and Lu give exact lifted MSE formulas for a noise vector fixed across row visits. Agaskar, Wang and Lu optimize independent row sampling in the noise-free setting. Matrix second-moment recursions and Perron-root rates themselves are standard.

*Exact noise-memory risk and optimal refresh allocation for two-row cyclic Kaczmarz* (Resultary record `bb27287bed96`) includes the fully refreshed complete-sweep risk at perfect alternation, corresponding to the row-2 conditional risk here. It optimizes a refresh budget while keeping the row policy cyclic. *Gaussianity is exactly a nonorthogonality-graph compatibility condition for noisy randomized Kaczmarz* (Resultary record `525a6be445a9`) provides stationary covariance relations for iid row picks with fresh Gaussian noise. The distinct conclusion here is that persistence cancels from stationary risk throughout the two-state Markov family, allowing exact rate-constrained optimization of the transition probabilities rather than the refresh probabilities or only the stationary frequencies.

## Limitations

The result uses two nonorthogonal spanning rows in two dimensions, unrelaxed projections, and exogenous row choices with fresh innovations. It is not an optimality claim over adaptive or general memory-dependent sampling, more rows, relaxed projections, or reused noisy observations. The rate is for synchronized mean squares, not an almost-sure rate or a mixing-time estimate. At rate caps at least 1 all admissible policies are feasible: when the variances differ the limiting risk infimum as \(r\uparrow1\) is not attained by an irreducible chain; when they are equal all policies attain the constant risk.

## References

1. V. Patel, M. Jahangoshahi and D. A. Maldonado, *An Implicit Representation and Iterative Solution of Randomly Sketched Linear Systems*, arXiv:1904.11919. https://arxiv.org/abs/1904.11919
2. E. H. Bergou et al., *A Note on Randomized Kaczmarz Algorithm for Solving Doubly-Noisy Linear Systems*, arXiv:2308.16904. https://arxiv.org/abs/2308.16904
3. A. Agaskar, C. Wang and Y. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, IEEE GlobalSIP (2014). https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b
4. C. Wang, A. Agaskar and Y. Lu, *Randomized Kaczmarz Algorithm for Inconsistent Linear Systems: An Exact MSE Analysis*, arXiv:1502.00190. https://arxiv.org/abs/1502.00190
