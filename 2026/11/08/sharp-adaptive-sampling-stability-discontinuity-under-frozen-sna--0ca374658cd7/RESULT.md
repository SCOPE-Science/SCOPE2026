# Sharp adaptive-sampling stability discontinuity under frozen-snapshot Kaczmarz batches

## Finding

For a fixed integer number \(m\ge2\) of orthonormal equations, any integer batch size \(T\ge1\), relaxation \(\beta>0\), and residual-power exponent \(\ell\ge0\), consider the frozen-snapshot, independent-with-replacement Kaczmarz process defined below. The following distinctions are sharp for convergence from **every** deterministic initial state:

1. For exactly uniform sampling (\(\ell=0\)), mean-square convergence occurs if and only if
   \[
   \beta\left(1+\frac{T-1}{m}\right)<2.
   \]
   In this case the expected squared error after \(k\) batches is exactly \(q_0^k\|x^{(0)}\|_2^2\), where
   \[
   q_0=1-\frac{\beta T}{m}\left[2-\beta\left(1+\frac{T-1}{m}\right)\right].
   \]
2. For every \(\ell>0\), convergence in mean square and almost surely from every initial state occurs if and only if \(\beta T<2\). In the convergent range, a common bound for every positive exponent is
   \[
   \mathbb E\|x^{(k)}\|_2^2\le
   \left(1-\frac{\beta T(2-\beta T)}m\right)^k\|x^{(0)}\|_2^2.
   \]
3. At \(\ell>0\) and \(\beta T=2\), a nonzero coordinate-axis start has a period-two sign orbit. At \(\ell>0\) and \(\beta T>2\), **every** nonzero initial state, even one with all coordinates nonzero, has strictly positive probability of an exponentially divergent trajectory; its expected squared error tends to infinity.

Thus the universal safe batch size can jump discontinuously at zero adaptive exponent. For example, with \(m=4\), \(T=3\), and \(\beta=1\), uniform sampling has exact mean-square factor \(5/8\), while every \(\ell>0\) has positive-probability divergence from every nonzero initial vector. The theorem is a complete classification for the specified frozen-snapshot model, not a claim about every asynchronous schedule.

## Assumptions and scope

Take the consistent linear system \(Ax=b\) with \(A=I_m\), \(b=0\), and error \(x^{(k)}\in\mathbb R^m\) after \(k\) completed batches. At a nonzero state \(x\), define selection probabilities
\[
p_i(x)=\begin{cases}
1/m,&\ell=0,\\
|x_i|^\ell/\sum_{j=1}^m|x_j|^\ell,&\ell>0.
\end{cases}
\]
The zero-exponent rule is uniform **including** currently satisfied equations; for a positive exponent, zero-residual equations have zero probability. Conditional on \(x\), draw \(T\) independent indices with replacement using this one unchanged probability vector, and let \(N_i\) be their multiplicities. All workers use the same frozen value of \(x\) for both selection and the correction; their accumulated row updates yield
\[
x_i^{(k+1)}=(1-\beta N_i)x_i^{(k)}.
\]
At \(x=0\), the state is absorbing. Draws in later batches are fresh and conditionally independent given the then-current state. Arithmetic is exact; no duplicate suppression, reread, coordinate lock, implicit relaxation, or decreasing gain is permitted. The batch is a specific consistent-snapshot interleaving of multiple row-action corrections.

For any nonzero state set
\[
U(x)=\sum_{i=1}^mp_i(x)x_i^2,\qquad
V(x)=\sum_{i=1}^mp_i(x)\bigl(1+(T-1)p_i(x)\bigr)x_i^2.
\]
Both quantities are strictly positive. The exact single-batch strict expected-descent criterion is \(0<\beta<2U(x)/V(x)\).

## Proof

**Exact conditional moment.** The counts are multinomial, so their binomial marginals satisfy
\[
\mathbb E[N_i\mid x]=Tp_i,\quad
\mathbb E[N_i^2\mid x]=Tp_i+T(T-1)p_i^2.
\]
Expand the squared update coordinate by coordinate and sum to obtain, without independence assumptions on distinct counts,
\[
\mathbb E[\|x^{(k+1)}\|_2^2\mid x^{(k)}=x]
=\|x\|_2^2-\beta T\{2U(x)-\beta V(x)\}.
\]
Since \(U,V>0\) at a nonzero state, this identity proves the asserted exact one-step criterion.

**Uniform branch.** If \(\ell=0\), then \(p_i=1/m\) for all coordinates, so \(U=\|x\|_2^2/m\) and \(V=(1+(T-1)/m)U\). Substitution gives conditional expectation \(q_0\|x\|_2^2\), hence the precise \(k\)-batch expression by the tower property. For \(\beta>0\) and nonzero initial data it tends to zero exactly when the stated strict inequality holds; at equality it stays constant, and when the inequality reverses it grows exponentially. The factor \(q_0\) is nonnegative because it is an expectation of squares divided by \(\|x\|_2^2\).

**Adaptive sufficiency.** For \(\ell>0\), order the values \(x_i^2\) increasingly. Their weights \(|x_i|^\ell\) have the same order. The pairwise-sum form of Chebyshev's sum inequality gives
\[
m\sum_i|x_i|^\ell x_i^2
-\left(\sum_i|x_i|^\ell\right)\left(\sum_i x_i^2\right)
=\sum_{i<j}(|x_i|^\ell-|x_j|^\ell)(x_i^2-x_j^2)\ge0.
\]
Dividing by the positive sum of weights yields \(U(x)\ge\|x\|_2^2/m\). Also \(1+(T-1)p_i\le T\). If \(0<\beta T<2\), the conditional moment identity consequently gives
\[
\mathbb E[\|x^{(k+1)}\|_2^2\mid x]
\le\|x\|_2^2-\beta T(2-\beta T)U(x)
\le q_\ell\|x\|_2^2,
\quad q_\ell=1-\frac{\beta T(2-\beta T)}m\in(0,1).
\]
Iterating proves mean-square geometric convergence. For each \(\varepsilon>0\), Markov's inequality implies \(\sum_k\Pr(\|x^{(k)}\|_2>\varepsilon)<\infty\); Borel–Cantelli applied to a countable sequence of positive \(\varepsilon\)'s proves almost-sure convergence.

**Critical equality.** For \(\ell>0\), choose \(x^{(0)}=a e_i\) with \(a\ne0\). At every batch \(p_i=1\), all \(T\) selections equal \(i\), and the update is multiplication by \(1-\beta T=-1\) when \(\beta T=2\). Thus the orbit does not approach zero. This is enough to rule out universal convergence at equality.

**Supercritical positive-probability escape.** Suppose \(\ell>0\), \(\beta T>2\), and let \(i\) be any coordinate with \(x_i^{(0)}\ne0\). Set \(R=\beta T-1>1\) and \(C=\sum_{j\ne i}|x_j^{(0)}/x_i^{(0)}|^\ell\ge0\). On the event that **all** workers choose coordinate \(i\) in **every** batch, induction gives \(x_i^{(k)}=(1-\beta T)^k x_i^{(0)}\), while all other coordinates remain at their initial values. Conditional on the first \(k\) such batches, the probability that the next one also selects only \(i\) is \([1+C R^{-\ell k}]^{-T}\). Therefore the infinite event has the exact probability
\[
\Pr(E_i)=\prod_{k=0}^\infty[1+C R^{-\ell k}]^{-T}
\ge\exp\left(-\frac{TC}{1-R^{-\ell}}\right)>0,
\]
using \(\log(1+t)\le t\). On this event \(\|x^{(k)}\|_2^2\ge R^{2k}|x_i^{(0)}|^2\). Consequently
\[
\mathbb E\|x^{(k)}\|_2^2\ge\Pr(E_i)R^{2k}|x_i^{(0)}|^2\longrightarrow\infty.
\]
This applies to every nonzero start, including dense starts, and completes the classification.

## Verification

The accompanying standalone `CHECK.py` requires only Python 3's standard library. Execute `python CHECK.py` in a directory containing the extracted file. It enumerates finite independently drawn batches using rational arithmetic and compares their exact second moments against the theorem's formula, checks the uniform and adaptive contractions, and numerically checks the infinite-collision product lower bound. The packaged test completed **7,816 assertions**. Finite enumeration and floating-point product checks are corroborative; the proof above establishes the infinite-horizon statements.

## Relationship to prior work

Coleman's *Adaptive Row Selection Meets Asynchrony in Randomized Kaczmarz* (2026) defines power-weighted row sampling and consistent-snapshot updates and reports measured concurrency-dependent stability cliffs, but does not derive the orthonormal, fully simultaneous batch classification above. His earlier *Residual-Weighted Randomized Jacobi* (2026) analyzes synchronous progress and asynchronous delay bounds and observes self-reinforcing frozen-value collisions, including concentrated single-coordinate experiments; those qualitative and conditional bounds do not give the sharp every-positive-exponent, every-nonzero-start positive-probability theorem here. Richtárik and Takáč (2015) analyze parallel coordinate sampling while discarding duplicate simultaneous block choices in the relevant construction. Lopes, Santos and Silva (2026) allow repeated coordinate selections but scale the local model curvature to preserve expected descent and use group-structured rather than current residual-power probabilities. Neither update rule implies this theorem. The exact binomial moment identity is elementary; the new content of the combined classification is the sharp discontinuity and the all-dense-start positive-probability escape under adaptive feedback.

## Limitations

The theorem applies to identity/orthonormal equations, an exactly frozen residual shared by every worker per batch, independent sampling with replacement, constant relaxation, and exact arithmetic. It does **not** characterize partial overlap, live/inconsistent reads, hardware scheduling distributions, row coupling, momentum, or practical wall-clock behavior. A positive-probability divergence event may have very small probability; the theorem is a universal stability classification, not a prediction that typical adaptive runs fail. Nonconvergence at the critical parameter is demonstrated by a coordinate-axis start; no classification of every other critical orbit is claimed.

## References

- E. Coleman (2026), *Adaptive Row Selection Meets Asynchrony in Randomized Kaczmarz*, arXiv:2607.08313, first posted 9 July 2026. https://arxiv.org/abs/2607.08313
- E. Coleman (2026), *Residual-Weighted Randomized Jacobi: Sharpened Bounds via Residual Concentration and Asynchronous Extension*, arXiv:2606.01232, first posted 31 May 2026. https://arxiv.org/abs/2606.01232
- P. Richtárik and M. Takáč (2015), *Parallel coordinate descent methods for big data optimization*, Mathematical Programming 156, 433–484 (2016), first published 12 April 2015. https://doi.org/10.1007/s10107-015-0901-6
- R. Lopes, S. A. Santos and P. J. S. Silva (2026), *Parallel block coordinate descent methods with identification strategies*, Computational Optimization and Applications 94, 475–508. https://doi.org/10.1007/s10589-026-00773-5
