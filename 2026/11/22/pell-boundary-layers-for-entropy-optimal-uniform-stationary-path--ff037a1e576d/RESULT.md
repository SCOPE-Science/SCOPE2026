# Exact surface entropy and a full-length error bound for uniform-stationary path walks

## Finding

Let \(H_n\) be the maximum stationary entropy rate of a symmetric stochastic matrix on the \(n\)-vertex path, with all self-loops permitted and no entries permitted beyond nearest neighbors. The stationary distribution is uniform, and logarithms are natural. Put \(\vartheta=2-\sqrt3\). Then
\[
\boxed{n(\log 3-H_n)=-4\log(3\vartheta)+O(\vartheta^n).}
\]
The positive constant is the total entropy cost of the two ends. The error has the full path length in its exponent, with no factor of \(n\). The key step is a cancellation of the leading interaction between the two endpoint profiles in the stochasticity residual; summing this residual controls the *total*, not just the per-site, entropy error.

## Assumptions and scope

Here \(n\ge2\), and \(H(P)=-n^{-1}\sum_{i,j}P_{ij}\log P_{ij}\), with \(0\log 0=0\). The maximization is over all symmetric stochastic matrices with the stated support, including matrices with zeros on permitted entries. No optimization over the stationary law or spectral mixing criterion is meant. The result does not assert that the error bound is sharp.

## Proof

**Finite optimization.** The feasible polytope is compact and the entropy is strictly concave on it. Giving each edge a small positive weight and assigning the remaining row mass to holding produces an interior comparison point. If the maximizer had a permitted zero, interpolation toward that point would have positive infinite one-sided derivative of entropy. Write the positive optimal diagonal and edge entries as \(d_i\) and \(e_i=P_{i,i+1}\). Since \(d_i=1-e_{i-1}-e_i\), with \(e_0=e_n=0\), differentiation in \(e_i\) gives \(e_i^2=d_id_{i+1}\). Thus with \(v_i=\sqrt{d_i}\), \(v_0=v_{n+1}=0\), the entries are \(P_{ij}=v_iv_j\) on the support and
\[
v_i(v_{i-1}+v_i+v_{i+1})=1.
\]
As each \(v_j\le1\), the row equation yields \(v_i\ge\sqrt2-1\). Stochasticity and symmetry give \(H_n=-2n^{-1}\sum_i\log v_i\). For \(w_i=\sqrt3v_i\) this is
\[
n(\log3-H_n)=2\sum_{i=1}^n\log w_i.
\]

**One-wall input.** Write \(r=-\vartheta\), so \(r+r^{-1}=-4\). The single-wall profile used below is the strong negative-coupling specialization of Bouttier–Di Francesco–Guitter [1, Eqs. (4.3), (4.5), (4.10)]:
\[
t_k=f(r^k),\qquad f(z)=\frac{(1-z)(1-r^3z)}{(1-rz)(1-r^2z)},\qquad k\ge0.
\]
For a direct check, put \(\kappa=-(1-r)(1-r^2)\); then \(f(z)-1=\kappa z/((1-rz)(1-r^2z))\). Clearing denominators in \(f(z/r)+f(z)+f(rz)=3/f(z)\) and cancelling the factor \(\kappa z\) gives a quadratic polynomial identity: the coefficients on the left for the sum of the three deviations from 1 are \(r^{-1}+1+r\), \(-(1+2r+2r^2+r^3)\), and \(r^2+r^3+r^4\). These are exactly the coefficients of \(-3(1-rz)(1-r^2z)\), by \(r^2+4r+1=0\). Applying the identity at \(z=r^k\) gives \(t_k(t_{k-1}+t_k+t_{k+1})=3\) for \(k\ge1\). Here \(t_0=0\), each \(t_k>0\) for \(k\ge1\), and
\[
t_k=1+\kappa r^k+O(\vartheta^{2k}).
\]
The bound holds with a single constant for all \(k\ge0\), by enlarging it for \(k=0\).

**Two-wall residual.** Put \(a_i=t_i\), \(b_i=t_{n+1-i}\) for \(0\le i\le n+1\), and \(\widetilde w_i=a_ib_i\). For any interior index \(i\), write \(A_d=a_i a_{i+d}\), \(B_d=b_i b_{i+d}\) for \(d=-1,0,1\). The two half-line row sums are each 3, including at the adjacent wall, and \(\widetilde w_0=\widetilde w_{n+1}=0\). Hence its row residual is exactly
\[
\widetilde w_i(\widetilde w_{i-1}+\widetilde w_i+\widetilde w_{i+1})-3
=\sum_{d=-1}^1(A_d-1)(B_d-1).
\]
Uniformly for the three values of \(d\),
\[
\begin{aligned}
A_d-1&=\kappa r^i(1+r^d)+O(\vartheta^{2i}),\\
B_d-1&=\kappa r^{n+1-i}(1+r^{-d})+O(\vartheta^{2(n+1-i)}).
\end{aligned}
\]
The leading cross term sums to zero, since
\[
\sum_{d=-1}^1(1+r^d)(1+r^{-d})=8+2(r+r^{-1})=0.
\]
The residual in row \(i\) is therefore \(O(\vartheta^{n+1}(\vartheta^i+\vartheta^{n+1-i}))\). Summing its absolute value over the path gives \(O(\vartheta^n)\), by two geometric sums.

**Stability and the entropy sum.** For log-coordinates \(y_i\) of the positive entries define
\[
G_i(y)=e^{2y_i}+\sum_{j\sim i}e^{y_i+y_j}-3,
\]
where the sum is over neighbors in the finite path. Compare \(y_i=\log w_i\) with \(\widetilde y_i=\log\widetilde w_i\). The Jacobian is symmetric and its diagonal dominance margin in row \(i\) is \(2e^{2y_i}\). Both comparison vectors have a uniform lower bound in log-coordinates, since \(v_i\ge\sqrt2-1\) and the positive \(t_k\) tend to 1. The Jacobian averaged along the segment between the vectors is symmetric with a uniform positive diagonal dominance margin. Solving against a maximum absolute component bounds its inverse in the maximum norm by the reciprocal of that margin; by symmetry the same bound applies in the sum norm. The residual estimate consequently gives
\[
\sum_{i=1}^n|\log w_i-\log\widetilde w_i|=O(\vartheta^n).
\]
Finally \(\sum_{i=1}^n\log\widetilde w_i=2\sum_{k=1}^n\log t_k\). The product of the one-wall factors telescopes:
\[
\prod_{k=1}^n t_k
=\frac{(1-r)(1-r^{n+3})}{(1-r^{n+1})(1-r^3)}
=\frac{1}{3\vartheta}\bigl(1+O(\vartheta^n)\bigr),
\]
using \(1+r+r^2=-3r\). This proves the stated constant and error; positivity follows from \(3\vartheta<1\).

## Relationship to prior work

General maximum-entropy reconstruction with a fixed stationary law gives the finite score equations directly [3, §3]. The one-wall factorization is likewise not a novelty claim: in [1] take \(g=-s^2\), \(s\to\infty\), with \(R=1+3gR^2\) on its positive branch. The characteristic equation tends to \(r+r^{-1}=-4\), and the factorization at its modulus-less-than-one root is the profile above. The one-wall constant is then an elementary telescoping product; to identify it with the finite-path entropy cost one still needs finite-path control.

The same authors give a two-wall theta-function solution of the corresponding dilute tree recurrence [2, §6, Eqs. (6.1), (6.5)–(6.6)]. This is closely related: rescaling \(R_j=v_{j+1}/s\) for \(g=-s^2\) yields the entropy scaling equations at \(s\to\infty\). The elliptic formula with its finite-size normalization suggests an alternative method, but its displayed real-coupling parameter choices and continuum limit do not supply that negative-coupling branch limit and its uniform entropy error estimate. The result here is the quantitative entropy asymptotic by cancellation and summable error, not a new solution of the single- or two-wall tree recurrence.

## Reproducibility and limitations

The proof uses a polynomial identity, exact cancellation, a geometric sum, and a dimension-independent inverse bound. Finite numerical examples are not needed for the remainder estimate. Only the path with uniform stationary weights and holding at every site is treated.

## References

1. J. Bouttier, P. Di Francesco, E. Guitter, *Geodesic Distance in Planar Graphs*, Nucl. Phys. B **663** (2003), 535–567. https://arxiv.org/abs/cond-mat/0303272
2. J. Bouttier, P. Di Francesco, E. Guitter, *Random trees between two walls: Exact partition function*, J. Phys. A **36** (2003), 12349–12366. https://arxiv.org/abs/cond-mat/0306602v2
3. P. Bolzern, P. Colaneri, G. De Nicolao, *Maximum entropy reconstruction of discrete-time Markov chains under partial information*. https://arxiv.org/abs/2611.02982
