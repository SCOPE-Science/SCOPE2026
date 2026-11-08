# The radix-parity boundary for quasi-random Lie splitting

## Finding

For the two-operator radical-inverse ordering of Li, Liu and Wan [1], the arithmetic parity of the radix exactly determines whether its logarithmic convergence loss is necessary. Fix an integer radix \(R\geq 2\) and set \(\xi_j=+1\) when the radical-inverse point \(\varphi_R(j)\) belongs to \([1/2,1)\), and \(\xi_j=-1\) otherwise. Write \(S_n=\sum_{j=1}^{n}\xi_j\), with \(S_0=0\).

**Radix dichotomy.** If \(R\) is even, \(\xi_j\) is exactly periodic with period \(R\), has zero mean over each period, and \(\sup_{n\geq0}|S_n|<\infty\). Consequently, for any two bounded linear evolution generators and any fixed finite time horizon, the prescribed two-operator quasi-random Lie scheme has uniform global error \(O(\tau^2)\), without a logarithm. For \(R=2\), each pair of its consecutive steps is exactly a symmetric Strang composition over time \(2\tau\).

If \(R=2m+1\) is odd, the indices
\[
N_k=m\frac{R^k-1}{R-1}-1,\qquad k\geq2,
\]
satisfy the **exact** discrepancy identity
\[
S_{N_k}=1-mk.
\]
For every odd \(R\), a fixed real three-dimensional, two-generator initial-value problem has, at the terminal time \(T>0\) and step sizes \(\tau_k=T/N_k\), the exact numerical error
\[
\bigl\|u_{N_k}-u(T)\bigr\|_2
=\frac{\tau_k^2}{2}(mk-1)
=\Theta_R\!\bigl(\tau_k^2\log(1/\tau_k)\bigr).
\]
Thus the source's \(O(\tau^2(1+\log N))\) bound is attained in order for odd radices but improves to genuine second order for all even radices in the two-operator bounded-linear class.

## Assumptions and scope

Let \(X\) be any real or complex Banach space, \(A,B\in\mathcal L(X)\), \(u_0\in X\), and \(T>0\). The exact solution is \(u(t)=e^{t(A+B)}u_0\). For each \(N\geq1\), put \(\tau=T/N\). The radical-inverse function is defined by the **finite** base-\(R\) expansion \(n=\sum_{j\geq0}a_jR^j\) and
\[
\varphi_R(n)=\sum_{j\geq0}\frac{a_j}{R^{j+1}},\qquad n\geq0.
\]
At step \(n\geq1\) the numerical method takes the factor
\[
L_n=\begin{cases}
e^{\tau A}e^{\tau B},&\varphi_R(n)\geq1/2,\\
e^{\tau B}e^{\tau A},&\varphi_R(n)<1/2,
\end{cases}\qquad u_n=L_nL_{n-1}\cdots L_1u_0.
\]
This is the source's two-operator point-to-permutation rule: the rightmost exponential acts first. There is no assumption that \(A\) and \(B\) commute. Error constants may depend on \(R,T,\|A\|,\|B\|,\|u_0\|\), but not on \(N\). All claims concern this two-operator construction and exact subflows.

## Proof

**1. Even-radix cancellation.** Write \(R=2m\). In the radical-inverse sum, the leading term \(a_0/R\) differs by at most \((R-1)\sum_{j\geq1}R^{-j-1}=1/R\) from the complete value, with strict inequality for finite expansions. Therefore \(\varphi_R(n)<1/2\) if \(n\bmod R<m\), and \(\varphi_R(n)\geq1/2\) otherwise. Hence \(\xi_n\) depends only on \(n\bmod R\), exactly \(m\) signs in each period are positive, and \(|S_n|\leq R\) for every \(n\) (the bound is deliberately nonoptimal). For \(R=2\), \(\xi_{2j-1}=+1\), \(\xi_{2j}=-1\). Thus each two-step propagator is
\[
L_{2j}L_{2j-1}=e^{\tau B}e^{2\tau A}e^{\tau B},
\]
which is the usual symmetric Strang step of length \(2\tau\).

**2. Convergence without the logarithm.** Put \(E=e^{\tau(A+B)}\), \(C=[A,B]\). Uniform Taylor expansion of the bounded exponentials gives
\[
L_j-E=\frac{\tau^2}{2}\xi_jC+R_j,
\qquad \|R_j\|\leq c_0\tau^3
\]
for sufficiently small \(\tau\), independently of \(j\). For any \(1\leq n\leq N\), the exact product-telescoping identity gives
\[
L_n\cdots L_1-E^n=\frac{\tau^2}{2}\sum_{j=1}^n\xi_jW_{n,j}+\sum_{j=1}^n L_n\cdots L_{j+1}R_jE^{j-1},
\]
where \(W_{n,j}=L_n\cdots L_{j+1}CE^{j-1}\). Boundedness of the generators and \(n\tau\leq T\) imply constants \(c_1,c_2\), independent of \(n,j,N\), with
\[
\|W_{n,j}\|\leq c_1,
\qquad
\|W_{n,j+1}-W_{n,j}\|\leq c_2\tau.
\]
The second estimate follows by factoring the difference into a bounded product times \(CE-L_{j+1}C\), which is \(O(\tau)\). Abel summation, with \(S_j=\sum_{i=1}^j\xi_i\), yields
\[
\sum_{j=1}^n\xi_jW_{n,j}
=S_nW_{n,n}+\sum_{j=1}^{n-1}S_j(W_{n,j}-W_{n,j+1}).
\]
For even \(R\), its norm is at most \(R(c_1+c_2T)\). The summed Taylor remainder is bounded by \(c_3n\tau^3\leq c_3T\tau^2\). Multiplying the product estimate by \(u_0\) establishes
\[
\max_{0\leq n\leq N}\|u_n-e^{n\tau(A+B)}u_0\|\leq C\tau^2.
\]
No infinite-dimensional commutator identities beyond boundedness are required.

**3. Exact odd-radix imbalance.** Let \(R=2m+1\), and define \(\eta(n)=+1\) if \(\varphi_R(n)<1/2\), or \(-1\) otherwise, including \(\eta(0)=+1\). Since \(\varphi_R(Rq+j)=j/R+\varphi_R(q)/R\), digit comparison gives
\[
\eta(Rq+j)=\begin{cases}
+1,&0\leq j<m,\\
\eta(q),&j=m,\\
-1,&m<j<R.
\end{cases}
\]
The center digit is the only recursive case, and the other \(2m\) digits cancel in pairs. For \(F(N)=\sum_{n=0}^{N-1}\eta(n)\), this proves \(F(RN)=F(N)\) and \(F(RN+m)=F(N)+m\) for every \(N\geq0\). Starting with \(M_0=0\) and \(M_k=RM_{k-1}+m\), we obtain \(M_k=m(R^k-1)/(R-1)\) and \(F(M_k)=mk\). As \(\xi_n=-\eta(n)\) for \(n\geq1\), the integer \(N_k=M_k-1\) satisfies
\[
S_{N_k}= -\bigl(F(M_k)-\eta(0)\bigr)=1-mk.
\]
Since \(N_k\asymp_R R^k\), these exact partial sums have logarithmic magnitude.

**4. An exact sharpness witness.** In \(\mathbb R^3\) let \(A=E_{12}\), \(B=E_{23}\), \(D=E_{13}\) in matrix-unit notation and \(u_0=e_3\). Direct matrix multiplication gives \(A^2=B^2=BA=0\), \(AB=D\), \((A+B)^2=D\), and \(D(A+B)=(A+B)D=D^2=0\). Hence, for either sign,
\[
L_j=\exp\!\left(\tau(A+B)+\frac{\tau^2\xi_j}{2}D\right).
\]
All matrices in these exponents commute. Consequently
\[
L_N\cdots L_1
=\exp\!\left(N\tau(A+B)+\frac{\tau^2S_N}{2}D\right),
\]
and because \(De_3=e_1\), the difference from the exact solution is precisely \((\tau^2S_N/2)e_1\). Its Euclidean norm is \(\tau^2|S_N|/2\), for every \(N\) and every \(\tau>0\). Substituting \(N=N_k\) from step 3 and \(\tau_k=T/N_k\) proves the claimed sharp odd-radix logarithmic loss.

## Verification

The included standard-library `verify.py` performs exact rational checks of the radical-inverse digits, all tested even-radix sign periods and prefix bounds, the odd-radix recursive block identity, the explicit logarithmic subsequence, and the exact three-by-three error coefficient. It is runnable using `python verify.py`. These finite diagnostics are not used to infer an infinite result: all universal claims follow from the analytic arguments above.

## Relationship to prior work

Li, Liu and Wan [1, §§2–4] define the radical-inverse ordering and prove the general \(O(\tau^2(1+\log N))\) estimate by pairwise cancellation and Abel summation. Their theorem applies to many operators; the present result restricts to exactly two and determines the sharp distinction between odd and even driver radices, including a matching lower-bound instance in the odd case. The local commutator expansion and the generic logarithmic upper bound are credited to [1], not new here. The base-two two-step identity is an instance of classical Strang composition [2]. General van der Corput discrepancy theory [3] concerns uniform interval discrepancy, which can grow logarithmically even when the specific half-interval sign imbalance is bounded; its standard bounds do not directly give this radix-dependent operator-splitting sharpness statement.

## Limitations

This result does not claim a parity dichotomy for three or more split operators or arbitrary point-to-permutation decoders. The logarithmic lower bound is a particular bounded, nonnormal three-by-three matrix example and a sparse sequence of time-step counts, not a lower bound for all bounded generators. It assumes exact subflows and fixed finite terminal time, not spatial discretization, rounding errors, nonlinear PDEs, or unbounded generators. Historical priority for equivalent unpublished or unindexed formulations is not established by the accessible source search; the classic building blocks themselves are not claimed as new.

## References

[1] Lei Li, Yunxiao Liu, Chenchen Wan, *Quasi-random splitting method for accurate and efficient multiphysics simulation*, arXiv:2603.27654 (first submitted 29 March 2026; revised 19 October 2026), https://arxiv.org/html/2603.27654v2.

[2] Gilbert Strang, *On the construction and comparison of difference schemes*, SIAM Journal on Numerical Analysis **5** (1968), 506–517; cited in [1, References].

[3] Josef Dick and Friedrich Pillichshammer, *Digital Nets and Sequences: Discrepancy Theory and Quasi–Monte Carlo Integration*, Cambridge University Press, 2010; cited in [1, References].
