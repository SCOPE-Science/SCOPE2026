# A sharp momentum crossover between periodic and Bernoulli gradient delivery

## Finding

Fix an integer \(m\ge2\), let \(0\le\beta<1\), and consider the scalar heavy-ball recursion
\[
x_{k+1}=(1+\beta-\tau\xi_k)x_k-\beta x_{k-1},\qquad\tau>0.
\]
Here a unit-curvature gradient is delivered at active steps \(\xi_k=1\), and no gradient is delivered at inactive steps \(\xi_k=0\). Compare two delivery processes with exactly the same average active fraction \(1/m\): (P) exactly one active step every \(m\) iterations, repeated periodically, with any fixed phase; and (B) independent Bernoulli active indicators with probability \(1/m\).

For any deterministic initial pair, periodic delivery converges to zero geometrically exactly when
\[
0<\tau<C_{\rm per}(m,\beta):=\frac{2(1-\beta)(1+\beta^m)}{1-\beta^m}.
\]
Bernoulli delivery converges to zero in mean square for **every** deterministic initial pair exactly when
\[
0<\tau<C_{\rm iid}(m,\beta):=\frac{2(1-\beta^2)}{1+\beta-2\beta/m}.
\]
Both endpoints are excluded, including when \(\beta=0\). For each \(m\ge2\) there is a unique \(b_m\in(0,1)\) satisfying
\[
m b_m^{m-1}+(m-1)b_m^m=1.
\]
For \(0<\beta<b_m\), Bernoulli delivery admits **strictly larger** active-step strengths than periodic delivery; for \(b_m<\beta<1\), periodic delivery admits **strictly larger** strengths. Both ceilings agree at \(\beta=0\) and at \(\beta=b_m\). The crossover values increase strictly with \(m\), satisfy \(b_2=\sqrt2-1\) and \(b_3=1/2\), and obey the sharp long-period boundary-layer law
\[
b_m=1-\frac{\log(2m)}m+O\!\left(\frac{(\log m)^2}{m^2}\right)\qquad(m\to\infty).
\]
In particular, the correlation structure of the delivery schedule can reverse which sampling mechanism permits the larger heavy-ball step even when its mean delivery frequency is unchanged.

## Assumptions and scope

The recursion is applied to the scalar strictly convex quadratic \(f(x)=x^2/2\), using raw Polyak heavy-ball momentum. Under (B), the gradient oracle may equivalently be written as the unbiased estimator \(m\xi_k x_k\) with nominal step \(\tau/m\). Under (P), the same gradient strength is supplied once per fixed block of length \(m\), so the average gradient strength is matched but individual periodic updates need not be conditionally unbiased. Momentum continues to operate in steps when the gradient is absent. No momentum state is reset at block boundaries. For (P), convergence means convergence of all iterates for every pair of real initial values; for (B), convergence means \(\mathbb E(x_k^2+x_{k-1}^2)\to0\) for every real deterministic initial pair, and indicators are independent of the current iterate history. The claims apply to fixed \(m\), fixed parameters and exact arithmetic. The stability *ceiling* is a supremum and never a stable positive endpoint.

## Proof

**Periodic stability.** Put
\[
A_0=\begin{pmatrix}1+\beta&-\beta\\1&0\end{pmatrix},\qquad
A_1=\begin{pmatrix}1+\beta-\tau&-\beta\\1&0\end{pmatrix}.
\]
The inactive matrix has eigenvalues \(1\) and \(\beta\), and direct induction gives
\[
(A_0^{m-1})_{11}=\frac{1-\beta^m}{1-\beta}.
\]
A monodromy matrix is \(P=A_0^{m-1}A_1\) (a different periodic phase changes the cyclic order of factors, not its trace and determinant). Consequently
\[
\det P=\beta^m,\qquad
\operatorname{tr}P=1+\beta^m-\tau\frac{1-\beta^m}{1-\beta}.
\]
The strict second-degree Jury criterion for two eigenvalues in the open unit disk is \(1-\det P>0\) and \(1\pm\operatorname{tr}P+\det P>0\). Here \(0\le\beta^m<1\); the minus-trace inequality holds for every \(\tau>0\), and the plus-trace inequality is exactly \(\tau<C_{\rm per}\). The within-cycle matrices are bounded, so the same condition ensures convergence of every intermediate iterate. At the upper endpoint the monodromy has eigenvalue \(-1\), and at \(\tau=0\) it has eigenvalue \(1\), so these endpoints are genuinely excluded. The same computation works at \(\beta=0\) without a separate argument.

**Bernoulli mean-square stability.** Write \(p=1/m\), \(a=1+\beta-p\tau\), and \(v=p(1-p)\tau^2\). Independence gives the *exact* map on second moments \(\big(\mathbb E x_k^2,\mathbb E[x_kx_{k-1}],\mathbb E x_{k-1}^2\big)\):
\[
T=\begin{pmatrix}a^2+v&-2\beta a&\beta^2\\a&-\beta&0\\1&0&0\end{pmatrix}.
\]
Direct expansion yields
\[
\det(I-T)=p\tau\left(2(1-\beta^2)-\tau(1+\beta-2p\beta)\right).
\]
For \(0<\beta<1\) consider the real symmetric matrix
\[
H=\begin{pmatrix}1&-\beta a/(1+\beta)\\-\beta a/(1+\beta)&\beta^2\end{pmatrix}.
\]
Its determinant equals \(\beta^2p\tau[2(1+\beta)-p\tau]/(1+\beta)^2\). Within the proposed stability interval we have \(0<p\tau<2(1+\beta)\), because \(p<1\); thus \(H\) is positive definite. For \(A_{\xi}=\left(\begin{smallmatrix}1+\beta-\tau\xi&-\beta\\1&0\end{smallmatrix}\right)\), an exact identity is
\[
\mathbb E(A_{\xi}^{\mathsf T}HA_{\xi})-H
=-D\begin{pmatrix}1&0\\0&0\end{pmatrix},
\quad D=p\tau\left[2(1-\beta)-\frac{\tau(1+\beta-2p\beta)}{1+\beta}\right].
\]
The quantity \(D\) is strictly positive exactly when \(0<\tau<C_{\rm iid}\). Summation of the energy identity shows that \(\sum_k\mathbb E x_k^2<\infty\), hence \(\mathbb E(x_k^2+x_{k-1}^2)\to0\). For \(\beta=0\), this assertion follows directly from the exact scalar factor \(\mathbb E(1-\tau\xi)^2=1-2p\tau+p\tau^2<1\), equivalent to \(0<\tau<2\).

Conversely, at the proposed upper endpoint, \(\det(I-T)=0\), so \(T\) has an eigenvalue \(1\). Above it, \(\det(I-T)<0\) while \(\det(\lambda I-T)\to+\infty\) as \(\lambda\to+\infty\), so \(T\) has a real eigenvalue greater than \(1\). In either case, \(T^k\) cannot tend to zero. The deterministic initial covariance vectors from pairs \((1,0),(0,1),(1,1)\) span the three-dimensional real second-moment space; if every deterministic start decayed in mean square, each spanning moment sequence would decay and thus \(T^k\to0\), a contradiction. The lower endpoint \(\tau=0\) retains a constant solution. This establishes the necessary and sufficient strict interval for all \(0\le\beta<1\).

**Exact crossover and monotonicity in \(m\).** Subtraction and algebraic factorization give
\[
C_{\rm per}-C_{\rm iid}
=\frac{4\beta(1-\beta)\,[m\beta^{m-1}+(m-1)\beta^m-1]}{m(1-\beta^m)(1+\beta-2\beta/m)}.
\]
Every denominator and the prefactor outside brackets are positive for \(0<\beta<1\). The bracket \(F_m(\beta)\) is strictly increasing on \((0,1)\), beginning at \(-1\) and ending at \(2m-2>0\), so it has precisely one root \(b_m\). The explicit values for \(m=2,3\) follow from factoring the respective cubics/quadratics. To show strict monotonicity, Bernoulli's inequality gives \((1-1/m)^{m-1}\ge1/m\), hence
\[
F_m(1-1/m)>0\quad\Longrightarrow\quad b_m<1-1/m.
\]
The difference of the unshifted polynomials \(G_j(z)=jz^{j-1}+(j-1)z^j\) is
\[
G_{m+1}(z)-G_m(z)=z^{m-1}[mz^2+2z-m].
\]
The quadratic is increasing and negative at \(z=1-1/m\), hence it is negative at \(b_m\). Therefore \(G_{m+1}(b_m)<G_m(b_m)=1\), and strict increase of \(G_{m+1}\) forces \(b_{m+1}>b_m\).

Finally, for every fixed \(z<1\), \(G_m(z)\to0\); thus \(b_m\uparrow1\). The defining equation can be rewritten exactly as
\[
b_m^m=\frac{1}{m/b_m+m-1}.
\]
It implies \(\log b_m=-\log(m/b_m+m-1)/m\). A preliminary bound from this identity gives \(1-b_m=O(\log m/m)\), so the logarithm in the numerator is \(\log(2m)+O(\log m/m)\). Exponentiating and expanding yields the asserted uniform scalar boundary-layer expansion \(1-b_m=\log(2m)/m+O((\log m)^2/m^2)\). Every limit keeps \(m\) integer and \(\beta\) in the stated domain.

## Verification

The standalone `verify.py`, runnable with Python 3 and SymPy, independently expands the monodromy trace/determinant for \(2\le m\le15\), the covariance determinant and Lyapunov drift identities, the first two exact crossover roots, and many rational sign and Schur-boundary comparisons. The accompanying `verification_output.txt` is an actual execution record; the script terminates with `VERIFY_OK` and 166 checks. These are finite corroborations, not an infinite proof. The all-parameter proof is the matrix and monotonicity argument above. As a concrete example at \(m=3,\beta=1/4\), the two ceilings are \(65/42\) and \(45/26\) respectively, favoring Bernoulli updates, whereas at \(m=3,\beta=3/4\) the ceilings are \(91/74\) and \(7/10\), favoring periodic updates.

## Relationship to prior work

Bollapragada, Chen and Ward (arXiv:2206.07553, public first version 2022-06-15) study stochastic minibatch heavy-ball convergence in quadratic optimization and transfer-matrix concentration; their analyzed independent minibatch construction does not yield the explicit exact periodic-versus-Bernoulli scalar threshold or its unique crossover for every \(m\). Qiu and Milzarek (arXiv:2404.18452, original public version 2024-04-29; later expanded with Ma) study random reshuffling with momentum in nonconvex optimization through complexity and asymptotic convergence; that work does not identify this fixed-frequency sharp stability-ceiling reversal. Tran, Tran-Dinh and Nguyen (arXiv:2403.03180, 2024-03-05) study a different shuffling-momentum recursion with an epoch anchor and convergence-rate guarantees; their exact algorithm does not give the present raw heavy-ball stability comparison. Exact scalar Bernoulli-erasure heavy-ball mean-square stability criteria already exist, as do exact periodic two-component heavy-ball phase diagrams. Neither *ingredient alone* is claimed new. The narrowly assessed contribution is their matched-frequency **comparison**, its unique \(m\)-dependent phase boundary and the increasing logarithmic boundary-layer law for general periods. Jury stability theory, Lyapunov identities, and scalar random-coefficient second-moment recursion are classical tools rather than claimed original methodology.

## Limitations

The theorem concerns only one scalar positive-curvature quadratic, fixed raw heavy-ball momentum, all-initialization deterministic stability versus all-initialization iid **mean-square** stability, and schedules with exactly matched long-run active frequency. The two stability notions are not identical probabilistic pathwise criteria. Larger step ceilings are not guarantees of faster within-region contraction, better finite-time error, lower wall-clock cost, or lower numerical sensitivity. No optimality among all schedules with the same average fraction is asserted, nor any extension to variable momentum, random correlated erasures, adaptive sampling, noncommuting Hessians, or higher-dimensional objectives. Classical switched-system theory may contain an unlocated equivalent specialization; exact priority therefore requires external verification.

## References

1. R. Bollapragada, T. Chen and R. Ward, *On the fast convergence of minibatch heavy ball momentum*, arXiv:2206.07553, originally posted 2022-06-15, https://arxiv.org/abs/2206.07553.
2. J. Qiu and A. Milzarek, *Random Reshuffling with Momentum for Nonconvex Problems: Iteration Complexity and Last Iterate Convergence*, arXiv:2404.18452, original 2024-04-29, https://arxiv.org/abs/2404.18452; subsequent revised manuscript with B. Ma.
3. I. S. Stamatiou, *A note on Asymptotic mean-square stability of stochastic linear two-step methods for SDEs*, arXiv:1704.08515, 2017-04-27, https://arxiv.org/abs/1704.08515.
4. R. Kidambi, P. Netrapalli, P. Jain and S. M. Kakade, *On the insufficiency of existing momentum schemes for stochastic optimization*, arXiv:1803.05591, original 2018-03-15, https://arxiv.org/abs/1803.05591.
5. T. H. Tran, Q. Tran-Dinh and L. M. Nguyen, *Shuffling Momentum Gradient Algorithm for Convex Optimization*, arXiv:2403.03180, original 2024-03-05, https://arxiv.org/abs/2403.03180.
