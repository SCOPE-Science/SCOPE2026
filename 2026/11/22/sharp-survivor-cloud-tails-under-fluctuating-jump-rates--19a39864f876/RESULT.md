# Sharp survivor-cloud tails under fluctuating jump rates

## Finding

Fix an integer \(m\ge 1\), a refresh period \(\tau>0\), and a time \(t>0\). A symmetric nearest-neighbor lattice walk starts at \(m\), jumps at a conditionally Poisson rate that is redrawn independently at times \(0,\tau,2\tau,\ldots\), and is absorbed on hitting the origin. Suppose the common strictly positive, almost surely finite rate \(\Lambda\) obeys
\[
\Pr(\Lambda>z)\sim C z^{-\alpha}\quad (z\to\infty),\qquad 0<\alpha<1,\quad C>0.
\]
Let \(\ell_j(t)\) be the positive lengths of the finitely many intersections of \([0,t]\) with the successive refresh intervals, and define
\[
C_t=C\sum_j\ell_j(t)^\alpha,\qquad
B_t=\frac{2^{\alpha+1}\alpha m C_t\Gamma(\alpha+\tfrac12)}{\sqrt\pi}.
\]
For \(X_t\), the position of the particle while alive, and \(T\), its absorption time, one has the sharp *unconditioned survivor-cloud* equivalent
\[
\Pr(X_t>h,\ T>t)\sim B_t h^{-(2\alpha+1)}\qquad (h\to\infty\text{ through integers}).
\]
Consequently, for every real \(q>0\),
\[
\mathbb E[X_t^q\mid T>t]<\infty\quad\Longleftrightarrow\quad q<2\alpha+1,
\]
and for every \(t>0\) the exactly conserved unconditioned survivor first moment is
\[
\mathbb E[X_t;T>t]=m.
\]
The conditional tail coefficient is \(B_t/\Pr(T>t)\); no unexplained conditioning factor is hidden in the displayed equivalent.

In the independent-rate Mittag--Leffler family with \(\mathbb E e^{-s\Lambda}=(1+s^\alpha)^{-1}\), the known first-passage transition is \(\mathbb E T<\infty\) exactly when \(\alpha<1/2\). Combining it with the new survivor moment cutoff shows that **there is no \(0<\alpha<1\) for which both \(\mathbb E T\) and \(\mathbb E[X_t^2\mid T>t]\) are finite**. At the boundary \(\alpha=1/2\), both diverge; below it only the mean first-passage time is finite, while above it only the conditional second spatial moment is finite.

## Assumptions and scope

A single jump is \(+1\) or \(-1\) with probability \(1/2\), independently of clocks and previous jumps. Conditional on the sampled rate history, jump times constitute an inhomogeneous Poisson process with intensity equal to the current rate; rates are *not* redrawn at each jump. The particle is killed upon its first visit to site zero and thereafter makes no further observations. The observation time is fixed, finite, and positive; it is not a large-time or joint large-space/large-time limit. The upper-tail variable \(h\) tends to infinity through the integers. The rate tail is an asymptotic equivalent, not merely an upper or lower power bound. No rate-density assumption, finite mean rate, or finite rate variance is used. The mean-first-passage complementarity assertion is restricted to the specified Mittag--Leffler family, as explicitly stated.

## Proof

**1. The integrated rate and a one-large-rate tail.** Let \(A_t=\int_0^t\lambda_s\,ds=\sum_j\ell_j(t)\Lambda_j\). For each fixed \(t\), the sum has finitely many independent summands, with regularly varying tails \(\Pr(\ell_j\Lambda_j>z)\sim C\ell_j^\alpha z^{-\alpha}\). The finite-sum, one-large-jump argument gives
\[
\Pr(A_t>z)\sim C_t z^{-\alpha}.
\]
Indeed, the probability of two separate summands both exceeding a fixed positive fraction of \(z\) is \(O(z^{-2\alpha})\), while the event that all are below that fraction and their sum exceeds \(z\) can be bounded by first taking the fraction small, then sending it to zero; equivalently one may use the elementary finite-convolution subexponential law for regularly varying variables. Karamata's Laplace-tail identity therefore gives
\[
1-\mathbb E e^{-sA_t}\sim C_t\Gamma(1-\alpha)s^\alpha\quad(s\downarrow0).
\]

**2. A sharp local tail for the free subordinated walk.** Let \(W_n\) be an unrestricted symmetric integer walk from zero, and let \(N_t\mid A_t\) be Poisson with mean \(A_t\). Set \(f_t(k)=\Pr(W_{N_t}=k)\). Its exact characteristic function is
\[
\widehat f_t(\theta)=\mathbb E\exp[-A_t(1-\cos\theta)]
=1-C_t\Gamma(1-\alpha)2^{-\alpha}|\theta|^{2\alpha}+o(|\theta|^{2\alpha}).
\]
For every deterministic \(a>0\), the Poissonized nearest-neighbor heat kernel is \(e^{-a}I_{|k|}(a)\), which is decreasing as an integer function of \(|k|\ge0\) (standard modified-Bessel order inequality, also obtainable from the one-dimensional nearest-neighbor heat-kernel comparison). Thus \(f_t(k)\) is symmetric and eventually monotone in positive \(k\). The monotone lattice Fourier Tauberian theorem, for exponent \(\beta\in(0,2)\), states that a symmetric eventually monotone lattice probability mass with \(1-\widehat f(\theta)\sim c|\theta|^\beta\) has local equivalent
\[
f(k)\sim \frac{c\,\Gamma(\beta+1)\sin(\pi\beta/2)}{\pi}\,k^{-\beta-1}.
\]
This is the monotone-density converse of the Abelian identity obtained by replacing \(\sum_{k\ge1}k^{-1-\beta}(1-\cos k\theta)\) by its Riemann integral. The identity \(\int_0^\infty(1-\cos u)u^{-1-\beta}du=\pi/[2\Gamma(1+\beta)\sin(\pi\beta/2)]\) fixes the normalization. Apply the theorem with \(\beta=2\alpha\) and simplify with the gamma reflection and duplication identities to obtain
\[
f_t(k)\sim K_t k^{-(2\alpha+1)},\qquad
K_t=\frac{\alpha 2^\alpha C_t\Gamma(\alpha+\tfrac12)}{\sqrt\pi}.
\]
This also admits a direct check: mix the large-time Poissonized Gaussian kernel \((2\pi a)^{-1/2}\exp[-k^2/(2a)]\) against the rescaled Pareto-tail measure \(\alpha C_t a^{-\alpha-1}da\). The resulting gamma integral yields the same \(K_t\). This is a proof of an infinite-lattice equivalent, not a conclusion from finite numerical enumeration.

**3. Reflection and the precise boundary prefactor.** The killed walk's exact image formula, for every integer \(j\ge1\), is
\[
\Pr(X_t=j,T>t)=f_t(j-m)-f_t(j+m).
\]
For any integer \(h\ge m\), summing *before* approximating the two close terms telescopes exactly:
\[
\Pr(X_t>h,T>t)=\sum_{k=h-m+1}^{h+m} f_t(k).
\]
There are exactly \(2m\) terms. The free local equivalent is uniform over this fixed-width window, whence the stated coefficient \(B_t=2mK_t\). Directly subtracting two leading approximations without this telescoping step would not justify the coefficient.

**4. Sharp moment cutoff and conservation.** Since \(\Pr(T>t)>0\) (there is a positive chance of making no jump by \(t\)), division by survival preserves the exact positive tail exponent and coefficient. For a nonnegative variable \(Y\), \(\mathbb E Y^q=q\int_0^\infty x^{q-1}\Pr(Y>x)dx\) for \(q>0\), including extended values. The survivor-tail equivalent therefore gives finiteness exactly for \(q<2\alpha+1\), with logarithmic divergence at equality. For each fixed discrete step count \(n\), the nonnegative walk absorbed at zero is an integrable stopped martingale with \(\mathbb E[X_n;T_{\rm step}>n]=m\). Conditioning on the independent Poisson event count \(N_t\) and summing its probabilities proves the exact equality \(\mathbb E[X_t;T>t]=m\), even though \(\mathbb EN_t\) may be infinite. As an independent check of the second-moment boundary, in deterministic operational time \(a\) the killed walk generator applied to the square function equals one at every strictly positive site. Thus \(M_2(a)=m^2+\int_0^a S_{\mathrm{op}}(u)\,du\), where \(S_{\mathrm{op}}(a)\sim m\sqrt{2/(\pi a)}\). Consequently \(M_2(a)\sim 2m\sqrt{2/\pi}\sqrt a\), and mixing over \(A_t\) makes the second moment finite exactly when \(\mathbb E\sqrt{A_t}<\infty\), i.e. precisely when \(\alpha>1/2\). This checks the moment transition independently of the local-tail calculation. Finally, the cited first-passage result for independent Mittag--Leffler rates supplies \(\mathbb ET<\infty\) iff \(\alpha<1/2\); intersecting this condition with \(\mathbb E[X_t^2\mid T>t]<\infty\) iff \(\alpha>1/2\) gives the incompatibility claim.

## Verification

The companion script `verification.py` checks the exact stopped-walk first moment for all discrete step counts through 20 at three positive starting positions; independently integrates the free one-period Pareto-mixture heat kernel \(\mathbb E[e^{-\Lambda}I_{|k|}(\Lambda)]\) at three large lattice sites and two tail exponents; and checks the *exact reflected finite-window sum* against the asserted survivor-tail prefactor. It does not claim that these finite checks prove the infinite limit. The analytic proof above is the certification basis. Execute `python verification.py` with Python, NumPy, and SciPy installed.

## Relationship to prior work

Levit and Reuveni (2026, arXiv:2609.26925), including its supporting information, introduce the periodically refreshed Mittag--Leffler rate family for half-line first passage, derive the general killed propagator and survival transform, and prove the mean-first-passage boundary at \(\alpha=1/2\). These are **prior results**, not part of the new claim. Arutkin and Reuveni (2024) introduce the general doubly stochastic continuous-time random-walk framework, give an unrestricted propagator transform and discuss free-position moments. The current theorem extracts a **sharp fixed-time, far-survivor-position asymptotic with its boundary factor**, establishes its universal finite-moment cutoff under *general* regularly varying rate tails, and connects that cutoff to the known mean-first-passage phase diagram. These conclusions are not explicitly stated by the cited general transform formulas. They do follow by combining those formulas with the additional monotone Fourier Tauberian and reflected-window analysis proved here; that relationship limits the novelty to the new asymptotic consequences, not the underlying exact propagator.

The nearest indexed results concern the first-passage-time distribution at large starting distance, mean first-passage integrability at marginal rate tails, and two-particle joint survival under shared stochastic clocks. None of those statements supplies the fixed-observation survivor-cloud tail and its incompatibility with finite mean first passage.

## Limitations

The tail applies for a fixed observation time and fixed finite starting distance; no uniformity as time, starting distance or refresh period vary is asserted. Rates are iid across deterministic refresh intervals and heavy-tailed with a pure regularly varying equivalent; slowly varying factors other than a constant would change the normalization. The comparison with finite mean first passage uses the specific Mittag--Leffler family, not every possible distribution satisfying the generic rate-tail assumption. The proof concerns symmetric unit jumps and absorption at zero, not drift, arbitrary long jumps, finite intervals, or reactive (partially absorbing) targets. Numerical tests are supplementary only. The result has undergone self-review, not independent audit.

## References

1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean* (2026), arXiv:2609.26925, initial public version 2026-09-22. https://arxiv.org/abs/2609.26925
2. M. Arutkin and S. Reuveni, *Doubly stochastic continuous time random walk*, Physical Review Research **6**, L012033 (2024), DOI:10.1103/PhysRevResearch.6.L012033; first preprint arXiv:2302.07041. https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.6.L012033
3. N. H. Bingham, C. M. Goldie, and J. L. Teugels, *Regular Variation*, Cambridge University Press (1987), standard regular-variation and Tauberian background.
4. W. Feller, *An Introduction to Probability Theory and Its Applications*, Vol. II, Wiley (1971), standard reflection and Fourier/Tauberian background.
