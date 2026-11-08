# Sharp Bernoulli stale-gradient stability and a pathwise-versus-mean-square split

## Finding

Consider gradient descent on the one-dimensional strongly convex quadratic \(f(x)=\lambda x^2/2\), where \(\lambda>0\). At each update, independently use either the current gradient or a one-iterate-stale gradient. Write \(h=\eta\lambda>0\), and let \(p\in[0,1]\) be the probability of using the stale gradient. Then, for **every** deterministic initial pair \((x_{-1},x_0)\),
\[
\mathbb E[x_n^2]\longrightarrow 0\quad(n\to\infty)
\quad\Longleftrightarrow\quad
h+ph^2<2.
\]
The exact sharp stepsize ceiling, including both deterministic endpoints, is
\[
h_c(p)=\frac{4}{1+\sqrt{1+8p}},\qquad 0<h<h_c(p).
\]
For \(h=h_c(p)\) some deterministic starting pair has a nonvanishing second moment; for \(h>h_c(p)\) some deterministic starting pair is mean-square unstable.

More sharply, choose \(h=3/2\), \(p=1/4\). Every deterministic initial pair yields an **almost-surely exponentially decaying augmented state**, whereas with \((x_{-1},x_0)=(0,1)\) the expected squared iterate grows exponentially. Thus almost-sure optimization success need not control the expected quadratic loss for a randomly stale gradient method.

## Assumptions and scope

Let \((D_n)_{n\ge0}\) be independent, identically distributed, independent of the deterministic initial pair, with \(\Pr(D_n=1)=p\) and \(\Pr(D_n=0)=1-p\). The exact recursion is
\[
x_{n+1}=x_n-hx_{n-D_n},\qquad n\ge0.
\]
No additive oracle noise, adaptively selected delays, or multidimensional coupling is allowed. Mean-square stability means convergence of \(\mathbb E[x_n^2]\) to zero for every real deterministic initial pair; the theorem also gives exponential decay when the inequality is strict. The nonconvergence statement is existential over deterministic initial pairs. The almost-sure example uses exactly the same random-delay recursion without altering its sampling law.

## Proof

**1. The closed covariance recurrence.** Set \(a_n=\mathbb E[x_n^2]\), \(b_n=\mathbb E[x_nx_{n-1}]\), \(c_n=\mathbb E[x_{n-1}^2]\), and \(v_n=(a_n,b_n,c_n)^{\mathsf T}\). Conditioning on the fresh delay, and using its independence of preceding states, yields \(v_{n+1}=T(p,h)v_n\), with
\[
T(p,h)=
\begin{pmatrix}
1-2(1-p)h+(1-p)h^2&-2ph&ph^2\\
1-(1-p)h&-ph&0\\
1&0&0
\end{pmatrix}.
\]
This is the coordinate matrix of the positive map
\[
\Phi(X)=(1-p)A_0XA_0^{\mathsf T}+pA_1XA_1^{\mathsf T},
\]
where \(A_0=\begin{pmatrix}1-h&0\\1&0\end{pmatrix}\), \(A_1=\begin{pmatrix}1&-h\\1&0\end{pmatrix}\), and \(X\) is a real symmetric \(2\times2\) matrix. Positivity here means \(X\succeq0\) implies \(\Phi(X)\succeq0\); the matrix \(T\) itself need not be entrywise nonnegative.

**2. The sharp mean-square boundary.** A finite-dimensional positive linear map on the cone of positive-semidefinite matrices has a real nonnegative eigenvalue equal to its spectral radius, with a nonzero positive-semidefinite eigenmatrix. Consequently, \(\rho(T)=1\) forces \(1\) to be an eigenvalue of \(T\). Direct expansion gives
\[
\det(I-T(p,h))=h(2-h-ph^2).
\]
At \(h=0\), the simple Perron eigenvalue equals \(1\) and the other two eigenvalues are zero. The derivative of that simple eigenvalue with respect to \(h\) at zero equals \(-2\), independently of \(p\): the right eigenvector is \((1,1,1)^{\mathsf T}\), the normalized left eigenvector is \((1,0,0)^{\mathsf T}\), and their derivative pairing is \(-2\). Thus \(\rho(T)<1\) for all sufficiently small positive \(h\). By continuity, it cannot subsequently reach \(1\) before the **unique** positive zero of \(2-h-ph^2\); otherwise the determinant would vanish earlier. This proves \(\rho(T)<1\) throughout \(0<h<h_c(p)\).

At \(h=h_c(p)\), the positive map has spectral radius at least \(1\), because its matrix has eigenvalue \(1\). For \(h>h_c(p)\), the determinant \(\det(I-T)\) is negative. A real matrix whose eigenvalues lie strictly inside the unit disk has strictly positive \(\det(I-T)\): positive factors arise from real eigenvalues and conjugate-pair products \(|1-z|^2\). Hence \(\rho(T)>1\) for all larger \(h\). The endpoints \(p=0,1\) are covered by these arguments, without divisions by \(p\).

Covariance iteration converges geometrically for every initial rank-one positive-semidefinite matrix precisely when \(\rho(T)<1\). Necessity follows because rank-one real symmetric matrices span the symmetric matrices: if all deterministic initial pairs had vanishing second moment, Cauchy--Schwarz would make every covariance entry vanish, so the powers of \(T\) would converge to zero on a spanning set, forcing \(\rho(T)<1\). This establishes all quantifiers of the first assertion and its critical boundary.

**3. A pathwise-stable, mean-square-unstable witness.** Set \(p=1/4\), \(h=3/2\). In state coordinates \(y_n=(x_n,x_{n-1})^{\mathsf T}\), the independent update matrices are
\[
A_0=\begin{pmatrix}-1/2&0\\1&0\end{pmatrix},\qquad
A_1=\begin{pmatrix}1&-3/2\\1&0\end{pmatrix},
\]
with probabilities \(3/4\) and \(1/4\), respectively. In the weighted maximum norm \(\|(u,v)\|_*:=\max\{|u|,|v|/2\}\), their induced operator norms are **exactly** \(1/2\) and \(4\). For any fixed starting state,
\[
\|y_n\|_*\le\|y_0\|_*\,(1/2)^{N_0(n)}4^{N_1(n)},
\]
where \(N_j(n)\) counts the first \(n\) draws of outcome \(j\). The strong law of large numbers gives
\[
\limsup_{n\to\infty}\frac1n\log\|y_n\|_*
\le\frac34\log(1/2)+\frac14\log4=-\frac14\log2<0
\]
almost surely, with the zero state understood separately. Thus every deterministic initial pair converges exponentially to zero almost surely.

Yet \(h+ph^2=33/16>2\). For the specific initial pair \((x_{-1},x_0)=(0,1)\), the exact covariance matrix and generating function are
\[
T=\begin{pmatrix}7/16&-3/4&9/16\\-1/8&-3/8&0\\1&0&0\end{pmatrix},\quad
\sum_{n\ge0}\mathbb E[x_n^2]z^n
=\frac{1+3z/8}{1-z/16-105z^2/128-27z^3/128}.
\]
The characteristic polynomial \(128t^3-8t^2-105t-27\) has one root \(\rho\in(1,9/8)\), one root in \((-1,-1/2)\), and one in \((-1/2,0)\), by explicit endpoint signs. The positive root is therefore uniquely dominant in modulus. The generating function's numerator does not vanish at its positive pole \(z=1/\rho\); the pole is simple and its coefficient is \(C=N(r)/(-rQ'(r))>0\) when \(r=1/\rho\), \(N(z)=1+3z/8\), and \(Q(z)=1-z/16-105z^2/128-27z^3/128\). Consequently \(\mathbb E[x_n^2]\sim C\rho^n\). This proves divergent expected loss on the same almost-surely convergent pathwise experiment.

## Verification

`verify.py` uses SymPy exact symbolic and rational arithmetic to check the covariance map identity, determinant factorization, witness characteristic polynomial and generating function, root-bracketing signs, weighted operator norms, and exact path enumeration for all binary delay histories up to ten updates. The output is in `verification_output.txt`. This finite enumeration independently checks the formulae; it is not substituted for the real-parameter proof above. To replay, install the exact dependency listed in `requirements.txt` and run `python verify.py` in the extracted folder.

## Relationship to prior work

Arjevani, Shamir, and Srebro (first public 2018) study convergence of quadratic gradient descent with a **fixed** number of stale iterations and provide finite-time complexity bounds; this is a different delay law and does not give the sharp iid Bernoulli threshold. Lale, Teke, Hassibi, and Anandkumar (2021) provide the positive-covariance-operator perspective for random asynchronous linear systems, including numerical random-delay stability diagrams; their exact analytic formulae specialize to random *updates without delay*, and they explicitly leave the general randomly delayed closed-form analysis for future work. Mulayoff and Michaeli (2024) derive exact mean-square thresholds for random minibatch current-gradient SGD, which has neither the delayed state nor the two-step moment evolution here.

The positive-map spectral-radius criterion is established background, not claimed as new. The contribution assessed here is its **explicit sharp two-point staleness boundary for all delay probabilities**, together with the concrete simultaneous almost-sure exponential convergence and exponential growth of expected loss. It may be expressible using earlier random-switching recurrence or Markov-jump results under other terminology; no general novelty assertion is made beyond the compared sources.

## Limitations

The model is scalar, noiseless except for iid delay selection, and uses a constant positive stepsize. The theorem does not cover correlated or unbounded delays, changing steps, multiple coordinates, additive noise, or nonlinear losses. No claim is made that a typical trajectory exhibits the mean-square divergence; the witness shows the contrary. A more comprehensive survey of older stochastic difference-equation and random-matrix-product literature could uncover an equivalent special-case statement. Independent validation has not been performed.

## References

1. Y. Arjevani, O. Shamir, N. Srebro, *A Tight Convergence Analysis for Stochastic Gradient Descent with Delayed Updates*, arXiv:1806.10188 (first public 2018-06-26), https://arxiv.org/abs/1806.10188 .
2. S. Lale, O. Teke, B. Hassibi, A. Anandkumar, *Stability and Identification of Random Asynchronous Linear Time-Invariant Systems*, Proceedings of Machine Learning Research **144** (2021), https://proceedings.mlr.press/v144/lale21a.html .
3. R. Mulayoff, T. Michaeli, *Exact Mean Square Linear Stability Analysis for SGD*, arXiv:2306.07850 (first public 2023-06-13), https://arxiv.org/abs/2306.07850 .
4. S. U. Stich and S. P. Karimireddy, *The Error-Feedback Framework: Better Rates for SGD with Delayed Gradients and Compressed Communication*, arXiv:1909.05350 (2019), https://arxiv.org/abs/1909.05350 .
