# Almost-sure finite absorption and a sharp mean-square dropout transition for error-feedback gradient descent

## Finding

For the scalar quadratic \(f(x)=x^2/2\), run ordinary error-feedback gradient descent at its exact-gradient unit step with independent all-or-nothing Bernoulli compression. Starting at \(x_0\ne0\) and zero error memory, the state \((x_k,e_k)\) reaches \((0,0)\) in finite time almost surely for every transmission probability \(0<p\le1\). Nevertheless, when \(0<p<2/3\), its deterministic-iteration mean-square objective error grows geometrically; at \(p=2/3\) its expected squared error converges to \((2/5)x_0^2\), not to zero; and only for \(2/3<p\le1\) does it converge geometrically to zero in mean square.

More precisely, for \(0<p<1\), put \(q=1-p\), \(a_k=\mathbb E[x_k^2]/x_0^2\), and
\[
W_p(z)=\frac{pqz^2(1+qz)}{(1-qz)^3}.
\]
There is a unique \(r_p\in(0,1/q)\) with \(W_p(r_p)=1\), and
\[
a_k\sim\frac{r_p^{-k}}{r_p(1-qr_p)W_p'(r_p)}.
\]
The base \(r_p^{-1}\) is greater than, equal to, or less than one according as \(p<2/3\), \(p=2/3\), or \(p>2/3\). In particular, this characterizes the exact deterministic-iteration mean-square threshold; the almost-sure absorption statement by itself gives no mean-square guarantee.

## Assumptions and scope

Take \(f:\mathbb R\to\mathbb R\), \(f(x)=x^2/2\), with exact gradient \(\nabla f(x)=x\), deterministic \(x_0\ne0\), memory \(e_0=0\), fixed step \(\eta=1\), and independent Bernoulli variables \(\xi_k\in\{0,1\}\) with \(\Pr(\xi_k=1)=p\). The on/off compressor is \(\mathcal C_p(v)=\xi_kv\), which satisfies the standard mean-square contraction identity \(\mathbb E|\mathcal C_p(v)-v|^2=(1-p)v^2\). Define the (unscaled) classical error-feedback updates
\[
u_k=x_k+e_k,\qquad x_{k+1}=x_k-\mathcal C_p(u_k),\qquad e_{k+1}=u_k-\mathcal C_p(u_k).
\]
All random choices are independent of the past. A zero state is absorbing. Mean-square error means \(\mathbb E[x_k^2]\) after exactly \(k\) attempted updates, not after a fixed number of transmitted messages. This is a fixed-stepsize, noiseless-gradient, one-dimensional special model; the result does not assert general error-feedback divergence.

## Proof

**Absorption on every sample path with a consecutive success.** When \(\xi_k=0\), the state update is \((x,e)\mapsto(x,x+e)\); when \(\xi_k=1\), it is \((x,e)\mapsto(-e,0)\). Thus two consecutive successful transmissions give \((x,e)\mapsto(-e,0)\mapsto(0,0)\), irrespective of the incoming state. Disjoint two-step blocks have probability \(p^2\) of being consecutive successes, independently. Hence the absorption time \(\tau\) obeys \(\Pr(\tau>2m)\le(1-p^2)^m\). For every \(p>0\), \(\tau<\infty\) almost surely.

**Renewal recurrence.** At any successful transmission, the memory resets to zero. If the first success occurs at attempted update \(t\), then the preceding \(t-1\) failures leave \(x\) fixed and raise memory to \((t-1)x\). The transmission maps \(x\) to \(-(t-1)x\). For \(t=1\) it therefore maps \(x\) to zero. If there is no success in the first \(k\) attempts, \(x_k=x_0\). Conditioning on this disjoint partition and using an independent continuation after each first success yields, for every integer \(k\ge0\),
\[
a_0=1,\qquad a_k=q^k+\sum_{t=2}^{k}pq^{t-1}(t-1)^2a_{k-t}\quad(k\ge1).
\]
The generating functions of the no-success term and nonzero renewal kernel are respectively \((1-qz)^{-1}\) and
\[
\sum_{t=2}^{\infty}pq^{t-1}(t-1)^2z^t=\frac{pqz^2(1+qz)}{(1-qz)^3}=W_p(z).
\]
Therefore, initially as formal power series and as analytic functions near zero,
\[
A_p(z):=\sum_{k=0}^{\infty}a_kz^k=\frac{1}{(1-qz)(1-W_p(z))}=\frac{(1-qz)^2}{(1-qz)^3-pqz^2(1+qz)}.
\]
Equivalently, \(a_0=1\), \(a_1=a_2=q\), and
\[
a_k=3qa_{k-1}-q(3q-p)a_{k-2}+q^2a_{k-3}\qquad(k\ge3).
\]

**The unique dominant pole and sharp regimes.** For \(0<p<1\), every coefficient of \(W_p\) at degrees \(2,3,4,\ldots\) is positive. Consequently \(W_p(z)\) is strictly increasing on \((0,1/q)\), starts at zero, and diverges at \(1/q\). Its unique positive level-one root is \(r_p\). For any complex \(z\) with \(|z|<r_p\), \(|W_p(z)|\le W_p(|z|)<1\). At \(|z|=r_p\), equality \(W_p(z)=1\) forces all nonzero summands to have the same argument; because both degrees \(2\) and \(3\) occur, this forces \(z=r_p\). Thus \(r_p\) is the sole pole of minimum modulus and is simple because \(W_p'(r_p)>0\). The rational generating function has the local decomposition
\[
A_p(z)=\frac{C_p}{1-z/r_p}+\text{a rational function analytic on a larger disk},\quad C_p=\frac{1}{r_p(1-qr_p)W_p'(r_p)}>0.
\]
Cauchy's coefficient formula gives \(a_k=C_pr_p^{-k}+O_p(s_p^{-k})\) for some \(s_p>r_p\). Direct evaluation gives
\[
W_p(1)=\frac{(1-p)(2-p)}{p^2},\qquad W_p(1)-1=\frac{2-3p}{p^2}.
\]
Since \(W_p\) increases, \(r_p<1\), \(r_p=1\), or \(r_p>1\) exactly when \(p<2/3\), \(p=2/3\), or \(p>2/3\). These are respectively exponential mean-square divergence, a positive limiting mean square, and geometric mean-square convergence. At \(p=2/3\), \(q=1/3\), factorization gives
\[
A_{2/3}(z)=\frac{(1-z/3)^2}{(1-z)(1+z^2/9)}.
\]
The pole at one has coefficient \((1-1/3)^2/(1+1/9)=2/5\); the remaining poles have modulus three. Therefore \(a_k\to2/5\). Finally, at \(p=1\) the first transmission is certain and \(x_k=e_k=0\) for all \(k\ge1\).

**Communication-epoch interpretation.** If \(T\) is geometric with \(\Pr(T=t)=pq^{t-1}\), the multiplier from one successful transmission to the next is \(-(T-1)\), with squared expectation
\[
\mathbb E[(T-1)^2]=\frac{(1-p)(2-p)}{p^2}.
\]
This renewal-epoch multiplier crosses one at the same sharp threshold, but the generating-function argument above is needed to establish the stated rates for deterministic iteration counts.

## Verification

The accompanying standard-library program `verify.py` enumerates every possible Bernoulli trace through 12 steps at five rational probabilities, reconstructs the state directly, and compares exact rational second moments with the renewal and cubic recurrences through 15 steps. It also checks the two-consecutive-transmissions absorption identity, the critical generating-function factorization, the limit \(2/5\), and an isolating interval for the growth rate at \(p=1/2\). The script reports 951 exact-rational assertions. These finite checks corroborate, but do not substitute for, the full positive-coefficient/generating-function proof above.

## Relationship to prior work

Classical error-feedback gradient descent and error-compensated sparsification are defined and analyzed in [1] and [2]. The closely relevant compression/delay analysis [3, Section 5] explicitly defines the same all-or-nothing Bernoulli compressor and gives sufficient step-size convergence bounds; its bounds do not state the exact unit-step, scalar, deterministic-iteration mean-square threshold or its coexistence with finite-time sample-path absorption. The later Markovian EF21 update [4] uses a different error mechanism, so its rates do not directly imply this specific renewal law. This result is an exact classification of a canonical special case, not an improvement of those works' general convergence theorems.

## Limitations

The phase transition is proved only for the classical error-memory recursion, scalar quadratic curvature one, unit learning rate, independent binary on/off compression, exact gradients and zero initial memory. No statement is made about other curvature/step-size combinations, unbiased rescaled compressors, minibatches, noisy gradients, finite-precision arithmetic, wall-clock time, or general multidimensional objective classes. Literature overlap was checked against the cited primary texts and an indexed set of published findings, but an equivalent specialized analysis not found in those sources remains possible. The result has not received independent audit.

## References

1. S. U. Stich, J.-B. Cordonnier, M. Jaggi, *Sparsified SGD with Memory*, 2018, arXiv:1809.07599 (initial public posting 2018-09-20). https://arxiv.org/abs/1809.07599
2. S. P. Karimireddy et al., *Error Feedback Fixes SignSGD and other Gradient Compression Schemes*, 2019, arXiv:1901.09847. https://arxiv.org/abs/1901.09847
3. S. U. Stich, S. P. Karimireddy, *The Error-Feedback Framework: SGD with Delayed Gradients*, 2019 preprint, arXiv:1909.05350, especially Section 5. https://arxiv.org/abs/1909.05350
4. P. Richtárik et al., *EF21: A New, Simpler, Theoretically Better, and Practically Faster Error Feedback*, 2021, arXiv:2106.05203. https://arxiv.org/abs/2106.05203
