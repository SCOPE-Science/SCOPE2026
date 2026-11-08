# Sharp rate–noise Pareto frontier for two-row Markov Kaczmarz

## Finding
Let \(0<c<1\) be the absolute inner product of two independent unit row normals, and let \(v_1,v_2>0\) be independent fresh-observation noise variances. In a stationary two-state Markov choice of these rows, put \(\alpha=\Pr(I_{n+1}=2\mid I_n=1)\in(0,1]\), \(\beta=\Pr(I_{n+1}=1\mid I_n=2)\in(0,1]\), and \(p=\beta/(\alpha+\beta)\). The stationary expected squared error is
\[
R(p)=\frac{v_1+v_2+2c^2[pv_1+(1-p)v_2]}{1+c^2}.
\]
It depends on row frequencies, but **not** on switching persistence. The exact asymptotic worst-case synchronized mean-square contraction factor is
\[
\lambda(\alpha,\beta)=\frac{2-\alpha-\beta+\sqrt{(\alpha-\beta)^2+4\alpha\beta c^4}}2.
\]
For fixed \(p\), the fastest chain has \(\max(\alpha,\beta)=1\): every visit to the less-frequent row is followed by an immediate switch. In particular, independent row choices with the same \(p\) and the same stationary risk generally converge more slowly.

More sharply, let \(r\) be a prescribed upper bound on this factor. No admissible policy meets \(r<c^2\). For \(c^2\le r<1\), define
\[
z_r=\frac{r^2-c^4}{2r-r^2-c^4}.
\]
The **sharp minimum stationary error at rate cap \(r\)** is
\[
\boxed{R_{\min}(r)=v_1+v_2-\frac{c^2|v_1-v_2|}{1+c^2}\,z_r.}
\]
For \(v_1<v_2\), the unique optimizer (including its transitions) chooses \(p=(1+z_r)/2\), \(\alpha=(1-p)/p\), \(\beta=1\); for \(v_2<v_1\), interchange the row labels. At \(r=c^2\) this gives perfect alternation \(\alpha=\beta=1\). If \(v_1=v_2\), the stationary error is invariant under every policy and the optimizer is not unique.

## Assumptions and scope
The problem is real and two-dimensional. Let \(u_1,u_2\in\mathbb R^2\) be unit vectors with \(0<|u_1^{\mathsf T}u_2|=c<1\). With the consistent exact right-hand side subtracted, update
\[
X_{n+1}=(I-u_{I_{n+1}}u_{I_{n+1}}^{\mathsf T})X_n+\epsilon_{I_{n+1},n+1}u_{I_{n+1}}.
\]
The row-index process is an exogenous stationary irreducible two-state Markov chain with strictly positive \(\alpha,\beta\le1\). The innovations are centered, independent across updates, independent of row choices and past states, with finite positive conditional variances \(\operatorname{Var}(\epsilon_{i,n})=v_i\); Gaussianity is **not** assumed. The unique stationary joint law of row and error has finite second moments. At \(\alpha=\beta=1\), row indices are periodic: the invariant joint law still exists and is unique, but distributional convergence from a fixed row phase need not hold. Contraction is defined from synchronized runs sharing the same row path and innovations, not from an unrelated-noise difference.

## Proof
Choose unit tangents \(w_i\perp u_i\). Let \(S_i=\mathbb E[XX^{\mathsf T}\mid I=i]\) under the invariant law, and put \(q_i=w_i^{\mathsf T}S_iw_i\). Because the current projection annihilates the normal component of the previous error and adds independent centered normal noise,
\[
S_i=q_iw_iw_i^{\mathsf T}+v_iu_iu_i^{\mathsf T}.
\]
The two-state Markov chain is reversible; its backward transition probabilities equal its forward transition probabilities. Thus
\[
q_1=(1-\alpha)q_1+\alpha[c^2q_2+(1-c^2)v_2],
\quad q_2=(1-\beta)q_2+\beta[c^2q_1+(1-c^2)v_1].
\]
Positivity of \(\alpha,\beta\) gives \(q_1=c^2q_2+(1-c^2)v_2\) and \(q_2=c^2q_1+(1-c^2)v_1\), hence
\[
q_1=\frac{v_2+c^2v_1}{1+c^2},\qquad
q_2=\frac{v_1+c^2v_2}{1+c^2}.
\]
Taking \(p\operatorname{tr}(S_1)+(1-p)\operatorname{tr}(S_2)\) proves the risk formula. Existence and uniqueness follow by coupling solutions using the same bi-infinite stationary row chain and noises: the norm of the difference cannot increase, and each row switch multiplies its post-projection magnitude by \(c\); since the finite-state chain switches infinitely often with a geometric tail for switch gaps, the infinite backward sum of injected noises converges in \(L^2\). This argument also works at perfect alternation.

For two synchronously driven errors \(Y_n\), define \(t_{i,n}=\mathbb E[\|Y_n\|^2\mathbf1_{\{I_n=i\}}]\). After one projection the difference lies along the selected tangent. Same-row repetition leaves its magnitude unchanged; switching rows multiplies squared magnitude by \(c^2\). Therefore
\[
\begin{pmatrix}t_{1,n+1}\\t_{2,n+1}\end{pmatrix}
=\begin{pmatrix}1-\alpha&\beta c^2\\\alpha c^2&1-\beta\end{pmatrix}
\begin{pmatrix}t_{1,n}\\t_{2,n}\end{pmatrix}.
\]
Its Perron eigenvalue is the stated \(\lambda\) and is the sharp asymptotic squared-error contraction factor. Sharpness is realized by nonzero initial tangent discrepancies with positive mass in each row phase. Write \(k=\alpha+\beta\), \(\alpha=(1-p)k\), \(\beta=pk\). Then
\[
\lambda=1-\frac{k}{2}\left[1-\sqrt{1-4p(1-p)(1-c^4)}\right].
\]
For fixed \(p\) the bracket is strictly positive, and \(0<k\le1/\max(p,1-p)\). Hence the unique fastest transition choice is \(k=1/\max(p,1-p)\). If \(z=|2p-1|\), its rate simplifies to
\[
\lambda_{\rm best}(z)=\frac{z+\sqrt{c^4+(1-c^4)z^2}}{1+z}.
\]
This function is strictly increasing from \(c^2\) to \(1\) as \(z\) increases from zero to one. A convenient proof uses its positive-root relation
\[
(1+z)\lambda_{\rm best}^2-2z\lambda_{\rm best}-c^4(1-z)=0:
\]
implicit differentiation gives \(\lambda_{\rm best}'=(2\lambda_{\rm best}-\lambda_{\rm best}^2-c^4)/[2(1+z)\lambda_{\rm best}-2z]>0\), because the positive-root derivative denominator is positive and the numerator equals \(2c^2(1-c^2)\) at \(z=0\) and remains positive for \(c^2\le\lambda_{\rm best}<1\). Solving the same identity at \(\lambda_{\rm best}=r\) gives \(z=z_r\). The rate cap is feasible precisely for \(|2p-1|\le z_r\); since \(R(p)\) is strictly affine when \(v_1\ne v_2\), its minimum is attained by the largest permitted frequency of the lower-noise row. At that endpoint, to meet the cap requires \(k\) to be maximal. This proves the closed form and uniqueness; equal noise variances give constant risk.

## Verification
A standalone standard-Python verifier, \(\texttt{verification/verify_markov.py}\), checks the conditional stationary-covariance equations, exact transfer-matrix identities and examples for 4,500 rational parameter tuples, alongside floating-point checks of the sharp Pareto transformation. These finite checks supplement but do not replace the analytic proof. For unit row normals \((1,0)\) and \((3/5,4/5)\), noise variances \((1,4)\), and stationary first-row probability \(3/4\), optimal transitions \((\alpha,\beta)=(1/3,1)\) give \(R=313/68\) and factor \((25+2\sqrt{217})/75\approx0.726158\). Independent draws with the same stationary frequency and risk have factor \((25+\sqrt{217})/50\approx0.794618\).

## Relationship to prior work
Patel, Jahangoshahi and Maldonado (2019, arXiv:1904.11919) develop convergence theory for randomized iterative linear solvers under dependent and other sampling schemes, including Kaczmarz. The present result treats the exact two-row Markov stationary **fresh-noise** law and a sharp joint policy optimization, not general noiseless convergence bounds. Bergou et al. (2023, arXiv:2308.16904) analyze RK with noisy coefficients and right-hand sides; their noise models and guarantees do not state the present stationary Markov two-row rate–risk frontier. Agaskar, Wang and Lu (2014) give exact IID randomized-Kaczmarz MSE and sampling analysis for the noise-free case. Prior noisy-Kaczmarz and sampling literature is substantial, and previously unknown equivalent specializations may exist.

## Limitations
The result requires exactly two nonorthogonal spanning rows in two dimensions, an exogenous stationary two-state Markov selection rule, unrelaxed projections, and independent fresh finite-variance innovations. It does not extend without further proof to adaptive selection, more rows, memory-dependent noise, relaxation or least-squares noise fixed across iterations. At perfect alternation the row chain is periodic. The reported rate is mean-square synchronous error contraction; no almost-sure rate, mixing time or optimality under more general sampling schemes is claimed. The asymptotic limiting minimum at \(r=1\) is not attained among irreducible chains.

## References
1. V. Patel, M. Jahangoshahi and D. A. Maldonado, *An Implicit Representation and Iterative Solution of Randomly Sketched Linear Systems*, arXiv:1904.11919, first public 2019-04-26. https://arxiv.org/abs/1904.11919
2. E. H. Bergou et al., *A Note on Randomized Kaczmarz Algorithm for Solving Doubly-Noisy Linear Systems*, arXiv:2308.16904, first public 2023-08-31. https://arxiv.org/abs/2308.16904
3. A. Agaskar, C. Wang and Y. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, IEEE GlobalSIP (2014). https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b
