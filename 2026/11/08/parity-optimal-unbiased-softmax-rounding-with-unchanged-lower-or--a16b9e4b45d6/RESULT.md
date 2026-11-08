# Parity-optimal unbiased softmax rounding with unchanged lower-order moments

## Finding

**Theorem (sharp all-order cross-entropy coupling).** Fix integers \(K\ge n\ge3\). For the first \(n\) class logits choose arbitrary lower values \(a_i\in\mathbb R\), strictly positive bin widths \(d_i>0\), and stochastic-round-up probabilities \(p_i\in(0,1)\). Other class logits \(c_{n+1},\ldots,c_K\in\mathbb R\) are deterministic. Let the rounded logits be \(z_i=a_i+d_i B_i\), where \(B_i\in\{0,1\}\), and require every proper subcollection of \((B_1,\ldots,B_n)\) to have the independent Bernoulli law with its prescribed probabilities. In particular, every one-coordinate rounding is unbiased and all pairwise covariances agree with independent rounding.

Write \(q_b=\prod_{i=1}^n p_i^{b_i}(1-p_i)^{1-b_i}\) for \(b\in\{0,1\}^n\), and define
\[
\alpha=\min_{b:n-|b|\ \mathrm{even}}q_b,\qquad
\beta=\min_{b:n-|b|\ \mathrm{odd}}q_b,
\qquad |b|=\sum_{i=1}^n b_i.
\]
Every admissible joint law is uniquely of the form
\[
\Pr_\theta(B=b)=q_b+(-1)^{n-|b|}\theta,\qquad -\alpha\le\theta\le\beta.
\]
For every possible true class \(y\in\{1,\ldots,K\}\), define the cross-entropy
\[
\mathcal L_y(z)=\log\biggl(\sum_{i=1}^K e^{z_i}\biggr)-z_y,
\]
and let \(R_y(\theta)=\mathbb E_\theta\mathcal L_y(z)\). Then, with \(F(x)=\log(\sum_{i=1}^n e^{a_i+x_i}+\sum_{j=n+1}^K e^{c_j})\),
\[
R_y(\theta)=R_y(0)+\theta\,\Delta_n,\quad
\Delta_n=\int_0^{d_1}\cdots\int_0^{d_n}
(-1)^{n-1}(n-1)!\prod_{i=1}^n \pi_i(x)\,dx_n\cdots dx_1,
\]
where \(\pi_i(x)=e^{a_i+x_i}/(\sum_{k=1}^n e^{a_k+x_k}+\sum_{j=n+1}^K e^{c_j})\). Therefore \(\Delta_n\) has the **strict** sign \((-1)^{n-1}\), independent of the logits, the label, or the bin widths. The **unique** minimizer of expected cross-entropy among all such moment-preserving joint laws is
\[
\theta_*=\begin{cases}-\alpha,&n\text{ odd},\\ \beta,&n\text{ even}.
\end{cases}
\qquad
R_y(0)-R_y(\theta_*)=
\begin{cases}\alpha\Delta_n,&n\text{ odd},\\-\beta\Delta_n,&n\text{ even}.
\end{cases}
\]
The gain is strictly positive for every \(n\ge3\). The optimizing joint distribution is **the same for every class label**.

**Fair-grid corollary.** When all \(p_i=1/2\), the unique optimum is the uniform law on the even-parity vertices \(\{b:\sum_i b_i\text{ is even}\}\), assigning probability \(2^{1-n}\) to each such vertex and zero to all others, for **every** \(n\ge3\). For \(K=n\), \(a_i=0\), and \(d_i=h>0\), the gain over independent rounding is exactly
\[
G_n(h)=2^{-n}\bigg|\sum_{k=0}^n(-1)^{n-k}\binom nk\log(k e^h+n-k)\bigg|
=\frac{h}{2^n}+O(1)\quad(h\to\infty).
\]
In the minimal nontrivial case \(n=3\),
\[
G_3(h)=\frac18\bigl(h+3\log(2+e^h)-3\log(1+2e^h)\bigr)
=\frac h8-\frac{3\log2}{8}+o(1).
\]
For \(h=4\), the exact formula gives \(G_3(4)\approx0.2501423668659\) nats per prediction, although all means and covariances of the rounded logits are exactly unchanged. This is a property of coupled **output-logit rounding**, not an assertion about floating-point operations within a multistep computation.

## Assumptions and scope

The bin widths are strictly positive, and every marginal is strictly between zero and one. The coupling design preserves all joint sublaws of at most \(n-1\) rounding decisions; no constraints on sequential conditional distributions are assumed. The loss is the exact natural-log softmax cross-entropy at fixed deterministic input logits and a fixed label. There is no assumption that these couplings can be substituted for independent random draws in a floating-point reduction while preserving a martingale-difference property. The class set may contain arbitrary additional unrounded logits. The statement includes the entire admissible coupling polytope, not merely symmetric or exchangeable laws.

## Proof

**1. Feasible laws.** For each proper subset \(S\subsetneq\{1,\ldots,n\}\), require \(\mathbb E\prod_{i\in S}B_i=\prod_{i\in S}p_i\), with the empty-product equation normalizing total mass. Möbius inversion, or induction on the Boolean lattice, shows that the nullspace of these \(2^n-1\) linearly independent equations on the \(2^n\) atom probabilities has basis \(((-1)^{n-|b|})_b\). Thus every solution equals \(q_b+(-1)^{n-|b|}\theta\). Nonnegativity on the two alternating parity classes is exactly the pair of bounds \(-\alpha\le\theta\le\beta\). Since every \(q_b>0\), the independent law \(\theta=0\) lies strictly inside that interval. This characterization of the \((n-1)\)-wise-independent Bernoulli family is classical and is not claimed as new; see Natarajan, Ramachandra, and Tan (2022), Section 2.

**2. Loss is affine in the sole interaction coordinate.** Let \(f(b)=F(d_1b_1,\ldots,d_nb_n)\). Because the marginal distribution of each \(B_i\) is fixed, \(\mathbb E_\theta z_y\) is independent of \(\theta\), whether \(y\le n\) or \(y>n\). Consequently,
\[
R_y(\theta)-R_y(0)=\theta\sum_{b\in\{0,1\}^n}(-1)^{n-|b|}f(b)=\theta\Delta_n.
\]
The coefficient is the full mixed forward difference of \(F\) across the bin rectangle. Repeated application of the fundamental theorem of calculus expresses it as the integral of \(\partial_1\cdots\partial_nF\) over that rectangle.

**3. Strict derivative sign.** Put \(\pi_i(x)=\partial_iF(x)\). For distinct indices \(i\ne j\), the exact softmax derivative is \(\partial_j\pi_i=-\pi_i\pi_j\). Induction gives, for any \(r\) distinct coordinates,
\[
\partial_{i_1}\cdots\partial_{i_r}F(x)
=(-1)^{r-1}(r-1)!\prod_{s=1}^r\pi_{i_s}(x).
\]
Indeed differentiation of the product with respect to an unused coordinate multiplies it by \(-r\pi_{i_{r+1}}\). Every softmax probability is strictly positive, as is the integration rectangle's volume, so \((-1)^{n-1}\Delta_n>0\). An affine function with nonzero slope on a closed interval has the unique endpoint minimizer written above. This proves simultaneously the sharp optimum and the label independence.

**4. Fair-grid parity and asymptotics.** At \(p_i=1/2\), all \(q_b=2^{-n}\), so \(\alpha=\beta=2^{-n}\). If \(n\) is odd the optimum removes atoms with \(n-|b|\) even, precisely odd-weight atoms; if \(n\) is even it removes atoms with \(n-|b|\) odd, again precisely odd-weight atoms. In both cases the survivors are the even-parity vertices with weights \(2^{1-n}\). For common bin width \(h\), the mixed difference groups by the number \(k\) of rounded-up coordinates and equals the stated binomial sum. Its term at \(k=0\) is \((-1)^n\log n\); for \(k\ge1\), \(\log(k e^h+n-k)=h+\log k+O(e^{-h})\). As \(\sum_{k=1}^n(-1)^{n-k}\binom nk=(-1)^{n+1}\), one obtains \(\Delta_n=(-1)^{n+1}h+O(1)\). The exact \(n=3\) simplification follows by substituting \(k=0,1,2,3\). No numerical experiment is used to justify these universal or asymptotic claims.

## Verification

Run the standalone `checker.py` from a directory containing Python and, for the optional linear-programming comparison, NumPy and SciPy. The verifier tests 400 randomly generated three-coordinate cases against the sharp formulas, 512 exact-rational marginal vectors, 100 independent linear-programming optimizations on all eight atoms, 240 randomized cases with three to six coordinates checking every proper-subset product moment, and symbolic-asymptotic numerical comparisons for three through seven coordinates. At package review the checker printed `PASS 4283 checks` and `scipy LP cross-checks: 100`. These finite checks test the implementation and sample cases; the proof above establishes the statements for every allowed integer \(n\) and every allowed input.

## Relationship to prior work

Chatelain and de Oliveira Castro, *Stochastic Rounding in Low-Precision Transformer Inference: A Variable-Precision Emulation Study of a Small GPT-2* (arXiv:2610.01889; first public October 1, 2026), analyze second-order drift and a Fisher-weighted variance penalty for logit softmax loss, with fresh random draws in elementary operations. The exact coupling optimization here asks a different, one-shot output-logit question and proves an effect invisible to any expectation depending only on means and covariances. The prior manuscript's conditional mean-independence assumptions for successive operations must not be transferred to this coupling.

Natarajan, Ramachandra, and Tan, *Probability bounds for n random events under (n−1)-wise independence* (arXiv:2211.01596, 2022), characterize the one-dimensional feasible law and bounds, including Bernstein parity constructions; **that probability-theoretic component is prior work**. The new mathematical object evaluated here is the exact softmax cross-entropy over this family: its all-order mixed derivative's strict global sign proves a label-universal parity optimum and exact risk gap. Ramachandra and Natarajan, *Tight Probability Bounds with Pairwise Independence* (SIAM Journal on Discrete Mathematics 37, 2023) give general event-probability envelopes, not this softmax optimization. Blanchard, Higham, and Higham (2021) analyze numerical evaluation errors of log-sum-exp/softmax, a different question.

## Limitations

This is an oracle coupling-design theorem for a single simultaneous quantization of logit values, not a method for preserving the conditional-unbiasedness requirements of a sequence of floating-point operations. Its exact objective is cross-entropy for fixed true class, not top-1 accuracy or perplexity averaged over a trained model's data distribution. It allows full \((n-1)\)-wise independence (stronger than pairwise independence when \(n>3\)); with only pairwise independence in dimension four or higher the optimal-law classification may differ. Large-bin-width asymptotics are mathematical benchmarks, not evidence that such bins are typical of production precision. Equivalent unindexed results specializing known multiway-dependence formulas to log-sum-exp remain a historical-priority risk. Independent validation is not claimed.

## References

1. Y. Chatelain and P. de Oliveira Castro, *Stochastic Rounding in Low-Precision Transformer Inference: A Variable-Precision Emulation Study of a Small GPT-2*, arXiv:2610.01889 (October 1, 2026), https://arxiv.org/abs/2610.01889 .
2. K. Natarajan, A. Kodagehalli Ramachandra, and C. Tan, *Probability bounds for n random events under (n−1)-wise independence*, arXiv:2211.01596 (November 3, 2022), https://arxiv.org/abs/2211.01596 .
3. A. K. Ramachandra and K. Natarajan, *Tight Probability Bounds with Pairwise Independence*, SIAM J. Discrete Math. 37 (2023), 516–555, https://doi.org/10.1137/21M1408294 .
4. P. Blanchard, D. J. Higham, and N. J. Higham, *Accurately Computing the Log-Sum-Exp and Softmax Functions*, IMA J. Numer. Anal. 41 (2021), 2311–2330, https://eprints.maths.manchester.ac.uk/2765/ .
