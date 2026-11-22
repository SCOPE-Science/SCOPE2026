# Strong Rayleigh persistence in a lossy coupon collection process

## Finding
Fix an integer \(n\ge1\). At each integer time \(t\ge0\), one label is drawn uniformly from \([n]\) and added to the currently retained set. Independently, every retained label, including the newly drawn one, is then deleted with the same deterministic time-dependent probability \(p_t\in[0,1]\). Start from the empty set and observe the set \(S_t\) **after deletion**. Put \(K_t=|S_t|\).

For **every** deterministic loss schedule \((p_t)_{t\ge0}\) and every finite \(t\ge0\), the full \(n\)-dimensional occupancy indicator law of \(S_t\) is **strongly Rayleigh**. Equivalently, its count probability-generating polynomial \(F_t(z)=\mathbb E[z^{K_t}]\) has only real nonpositive zeros. Therefore there exist parameters \(\theta_{1,t},\ldots,\theta_{n,t}\in[0,1]\) such that
\[
K_t\ \stackrel{\mathrm d}=\ \sum_{j=1}^{n} B_{j,t},\qquad
 B_{j,t}\text{ independent Bernoulli}(\theta_{j,t}).
\]
This representation describes the **count law only**; the physical coupon indicators are generally dependent. For constant \(p_t=p\in(0,1)\), the unique stationary retained-subset law is also strongly Rayleigh, and its stationary count is Poisson-binomial.

A recurrence furnishing a direct constructive proof is
\[
F_0(z)=1,\qquad
F_{t+1}(z)=x_t\left[F_t(x_t)+\frac{1-x_t}{n}F_t'(x_t)\right],
\quad x_t=p_t+(1-p_t)z.
\]

## Assumptions and scope
The sample labels are independent and uniform on the same fixed alphabet \([n]\), and each loss occurs after its round's sample. Within a round deletion indicators are mutually independent and independent of past draws, past losses, and the new draw. The scalar loss probability may change deterministically in arbitrary fashion between rounds, including the endpoint values zero and one, but does not depend on coupon label or trajectory. The initial collection is empty. Strongly Rayleigh means that the multiaffine occupancy generating polynomial has no zero when every complex variable has strictly positive imaginary part.

## Proof
**1. Exact polynomial evolution.** Condition on \(K_t=k\). The new draw is absent from the current set with probability \((n-k)/n\) and already present otherwise. Before deletion the count is accordingly \(k+1\) or \(k\). With retention probability \(q_t=1-p_t\), a single present coupon survives with generating polynomial \(x_t=p_t+q_tz\). Since deletions are independent, the conditional generating polynomial after deletion is
\[
\frac{k}{n}x_t^k+\frac{n-k}{n}x_t^{k+1}.
\]
Average over \(K_t\). The identities \(\mathbb E[K_tx^{K_t}]=xF_t'(x)\) and \(\mathbb E[(n-K_t)x^{K_t}]=nF_t(x)-xF_t'(x)\) yield precisely
\[
F_{t+1}(z)=x_t\left[F_t(x_t)+\frac{1-x_t}{n}F_t'(x_t)\right].
\]
Every \(F_t\) is a probability-generating polynomial of degree at most \(n\), with nonnegative coefficients and \(F_t(1)=1\).

**2. Nonpositive-root preservation.** For a nonzero degree-\(k\) real polynomial \(F\), with \(0\le k\le n\) and all roots \(r_1,\ldots,r_k\) real and nonpositive, consider
\[
H(x)=nF(x)+(1-x)F'(x).
\]
Suppose first that the roots are distinct. On every interval \((r_i,r_{i+1})\), the quotient
\[
\frac{H(x)}{F(x)}=n+(1-x)\sum_{i=1}^k\frac{1}{x-r_i}
\]
continuously passes from \(+\infty\) to \(-\infty\), because \(1-x>0\) at each nonpositive root. Thus \(H\) has at least one root in each of the \(k-1\) internal intervals. If \(k<n\), the same quotient approaches \(n-k>0\) as \(x\to-\infty\) and approaches \(-\infty\) as \(x\uparrow r_1\). It therefore has an additional root to the left of \(r_1\). Since \(\deg H=k\) when \(k<n\) and \(\deg H=k-1\) when \(k=n\), these are all of its roots. Each is nonpositive. For \(k=0\), \(H=nF\) is a positive constant.

For repeated roots, approximate \(F\) coefficientwise by products with distinct nonpositive roots; the corresponding polynomials \(H\) converge coefficientwise. Real-rootedness is closed under nonzero polynomial limits, while the coefficient formula
\[
[x^j]H=(n-j)[x^j]F+(j+1)[x^{j+1}]F\ge0
\]
ensures no positive root in the limit. Consequently \(H\), including the repeated-root case, has only nonpositive real zeros.

The next generating polynomial is \(F_{t+1}(z)=x_tH(x_t)/n\). If \(0\le p_t<1\), the affine map \(z\mapsto x_t\) sends each nonpositive root of \(xH(x)\) to a nonpositive real root of the new polynomial. If \(p_t=1\), then \(x_t=1\) and \(F_{t+1}(z)=F_t(1)=1\). Starting from \(F_0=1\), induction establishes the real-nonpositive-root assertion for all finite times and arbitrary deterministic loss schedules.

**3. Poisson-binomial count law and strong Rayleigh property.** The real-nonpositive-root factorization and \(F_t(1)=1\) give
\[
F_t(z)=\prod_{j=1}^n(1-\theta_{j,t}+\theta_{j,t}z),
\qquad \theta_{j,t}\in[0,1],
\]
where constant factors correspond to zero parameters. Hence \(K_t\) has the stated independent-Bernoulli-sum *distribution*.

By permutation invariance of the entire process, the law of \(S_t\) is exchangeable. Its multiaffine generating polynomial is the symmetric polarization
\[
G_t(z_1,\ldots,z_n)=\sum_{k=0}^n\frac{\Pr(K_t=k)}{\binom nk}
\sum_{\substack{A\subseteq[n]\\|A|=k}}\prod_{i\in A}z_i.
\]
Borcea–Brändén–Liggett's exchangeable characterization (Theorem 3.8) or the Grace–Walsh–Szegő polarization theorem shows that \(G_t\) is stable if and only if its diagonal specialization \(G_t(z,\ldots,z)=F_t(z)\) is real-rooted. Thus the entire vector is strongly Rayleigh, a strictly stronger structural property than negative association.

**4. Stationarity under constant loss.** For fixed \(0<p<1\), independent losses give positive probability of clearing every currently held coupon; from the empty collection any subset can be built by drawing its elements successively, retaining them and deleting the unwanted element as required. Hence the finite Markov chain is irreducible. It is aperiodic because the empty state has positive one-step self-transition probability. It has a unique stationary distribution and its time-\(t\) law converges to it from the empty state. Probability polynomials converge coefficientwise. Stability and real-rootedness are closed under such limits because \(F_t(1)=1\); the same two conclusions therefore hold at equilibrium.

## Verification
The standalone `checker.py` implements the generating-polynomial recursion with exact rational coefficients and **independently** evolves the complete \(2^n\)-state subset Markov chain using exact fractions, including changing loss probabilities and endpoint cases. It also checks exchangeability of every state probability and uses exact symbolic root counting. Executing `python checker.py` with Python 3 and SymPy passed **3,960 exact assertions** over \(1\le n\le6\), four nonconstant loss schedules per size, and up to seven steps per schedule. The finite checks are diagnostics; Steps 1–4 above are the proof for all dimensions and time horizons.

## Relationship to prior work
Cruciani and Dudeja (2026) introduced the post-loss careless collector, prove **negative association of the occupancy indicators** (Lemma 13), and analyze concentration and completion times. Their inspected full text does not assert a Poisson-binomial count law or strong Rayleigh property. Long (2026) studies stationary-entry fluxes and the high-tail hitting time of this same model under a fixed loss probability; the full text does not state the time-dependent real-rootedness theorem.

A separate previously recorded study proves exact stationary subset inclusion probabilities and strictly negative pairwise correlations for this model; these results do not themselves give the asserted finite-time strong Rayleigh property. A different prior study proves strong Rayleigh and Poisson-binomial laws for **never-seen coupons under independent uniform group drawings**, a no-forgetting situation, not the repeated global losses here. Borcea, Brändén and Liggett (2009) supply the general characterization of exchangeable strongly Rayleigh measures and the polarization theorem; these are used as established tools rather than claimed as new mathematics. The model-specific polar-derivative evolution and its arbitrary-time-loss consequence are the point of the finding.

## Limitations
This theorem requires uniform label sampling, deletion independence, equal within-round loss probabilities across coupon types, and the empty or stationary starting state as specified. It does not establish strong Rayleigh behavior under nonuniform sampling or label-dependent losses. The Bernoulli parameters are specified implicitly by the generating polynomial, not by elementary formulas in general. The claim does not assert a new general theorem about polar derivatives or independently sampled Bernoulli coordinate indicators. Classical real-rootedness-preserving operator literature might yield an equivalent special case not explicitly identified, so mathematical priority still requires external assessment.

## References
1. E. Cruciani and A. Dudeja, *The Careless Coupon Collector's Problem*, arXiv:2602.20705v1, first public version 2026-02-24, https://arxiv.org/abs/2602.20705.
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511v1, first public version 2026-05-14, https://arxiv.org/abs/2605.14511.
3. J. Borcea, P. Brändén and T. M. Liggett, *Negative Dependence and the Geometry of Polynomials*, arXiv:0707.2340, *J. Amer. Math. Soc.* 22 (2009), 521–567, https://arxiv.org/abs/0707.2340.
4. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485, https://arxiv.org/abs/2202.07485.
