# Sharp FIR-length stabilization and optimal contraction in a filtered Hénon map

## Finding

**Theorem.** Fix an integer \(n\ge 2\), \(\alpha>0\), \(0\le\beta<1\), and a positive filter gain \(G\). Consider the \(n\)-dimensional real delay map determined by
\[
 u_{t+1}=\alpha-\left(\sum_{j=0}^{n-1}c_j u_{t-j}\right)^2+\beta u_{t-1},\qquad \sum_{j=0}^{n-1}c_j=G.
\]
The positive stationary state is a **hyperbolic sink for some strictly positive filter taps** if and only if
\[
 \boxed{0<G<G_n^*,\qquad G_n^*=\sqrt{\frac{4^n-(1-\beta)^2}{4\alpha}}.}
\]
For \(G\ge G_n^*\), no choice of real taps with sum \(G\), even signed ones, makes the positive stationary state a hyperbolic sink. For \(G>G_n^*\), it has an eigenvalue of modulus strictly greater than one.

In the high-feedback regime \(\Delta>1\), with
\[
 \Delta=(1-\beta)^2+4\alpha G^2,\qquad
 r=\Delta^{1/(2n)}-1>0,\qquad a=\sqrt\Delta-(1-\beta),
\]
the sharp optimal spectral radius of the derivative at the positive fixed point is
\[
 \boxed{\inf_{\sum c_j=G}\rho(D F|_{p_+})=r.}
\]
The minimizer is **unique**, has all taps strictly positive, and is explicitly
\[
 \boxed{c_j=\frac{G}{a}\left[\binom{n}{j+1}r^{j+1}+\beta\,\mathbf 1_{\{j=1\}}\right],\quad j=0,\ldots,n-1.}
\]
Its characteristic polynomial is exactly \((z+r)^n\). The infimum is therefore attained, including when optimizing over arbitrary signed real taps. At \(G=G_n^*\), exactly this filter has every multiplier in the closed unit disk; all are the neutral multiplier \(-1\). Every other filter at that gain has a multiplier outside the closed unit disk.

The negative stationary state has a real multiplier greater than one for **every** real tap vector with positive sum \(G\).

For the original numerical parameters \(\alpha=7/5\), \(\beta=3/10\), the sharp gain is
\[
 \boxed{G_n^*=\sqrt{\frac5{28}\left(4^n-\frac{49}{100}\right)}}.
\]
Thus the maximal locally stabilizable gain grows asymptotically like \(2^n/(2\sqrt\alpha)\) with filter length, whereas for any fixed high-feedback gain the optimal radius satisfies \(r\sim(\log\sqrt\Delta)/n\).

## Assumptions and scope

The state is the real delay vector \((u_t,u_{t-1},\ldots,u_{t-n+1})\in\mathbb R^n\); no clipping, numerical rounding, or external forcing is assumed. A hyperbolic sink means that every eigenvalue of its \(n\)-dimensional Jacobian has modulus strictly below one, which implies exponential attraction in a neighborhood. Admissible positive-tap filters satisfy \(c_j>0\) for all \(j\). The impossibility part allows arbitrary signed real taps with the same total \(G>0\). The high-feedback optimal-radius assertion assumes \(\Delta>1\); the remaining small-gain region is covered by an existence argument, not by an asserted spectral optimum. None of these claims concerns global attraction, chaos, spectral bandwidth, robustness to parameter error, or practical security.

## Proof

**1. Stationary branches.** Both equilibria have all delay coordinates equal to \(p\), where
\[
 G^2p^2+(1-\beta)p-\alpha=0,\qquad
 p_\pm=\frac{-(1-\beta)\pm\sqrt\Delta}{2G^2}.
\]
Thus \(p_+>0>p_-\). With \(w_j=c_j/G\), \(\sum w_j=1\), and \(a=2G^2p_+=\sqrt\Delta-(1-\beta)>0\), the exact linearized scalar recurrence about \(p_+\) is
\[
 e_{t+1}=-a\sum_{j=0}^{n-1}w_j e_{t-j}+\beta e_{t-1}.
\]
Its companion-matrix characteristic polynomial, including the \(n=2\) case, is
\[
 P_+(z)=z^n+a\sum_{j=0}^{n-1}w_jz^{n-1-j}-\beta z^{n-2},
 \qquad P_+(1)=1+a-\beta=\sqrt\Delta.
\]
All coefficient identities hold for signed taps as well.

**2. Universal radius obstruction.** Let \(\lambda_1,\ldots,\lambda_n\) be its complex roots, with \(\rho=\max|\lambda_j|\). By factorization and the triangle inequality,
\[
 \sqrt\Delta=|P_+(1)|=\prod_{j=1}^n|1-\lambda_j|
 \le\prod_{j=1}^n(1+|\lambda_j|)\le(1+\rho)^n.
\]
Consequently \(\rho\ge\Delta^{1/(2n)}-1\). Whenever \(\sqrt\Delta\ge2^n\), the derivative cannot be Schur stable, irrespective of the signs of the taps. For \(\sqrt\Delta>2^n\), some multiplier necessarily has modulus greater than one. Equality throughout the product inequalities when \(\Delta>1\) requires every multiplier to equal the same negative real number \(-r\), where \(r=\Delta^{1/(2n)}-1\).

**3. Unique exact root-placement filter.** For \(\Delta>1\), define the taps in the finding. Their normalized weights satisfy
\[
 a\sum_{j=0}^{n-1}w_j=(1+r)^n-1+\beta
 =\sqrt\Delta-1+\beta=a.
\]
All weights are strictly positive since \(r>0\). Coefficient comparison gives the exact identity
\[
 z^n+a\sum_{j=0}^{n-1}w_jz^{n-1-j}-\beta z^{n-2}=(z+r)^n.
\]
It attains the universal radius bound. If another filter attains the same radius, equality in Step 2 forces all its roots to be \(-r\); equality of monic polynomials then fixes every coefficient and hence every tap. This proves existence and uniqueness of the optimum. It is stable exactly when \(r<1\), equivalently \(\sqrt\Delta<2^n\).

**4. The small-feedback gap.** If \(0<G\) and \(\sqrt\Delta\le1\), then \(0<a\le\beta\) and \(0\le\beta<1\). Allow temporarily \(w_1=1\) and all other weights zero. Its characteristic polynomial is
\[
 P_+(z)=z^{n-2}\bigl(z^2+a-\beta\bigr)
 =z^{n-2}\bigl(z^2+\sqrt\Delta-1\bigr).
\]
Since \(-1<\sqrt\Delta-1\le0\), all roots have modulus strictly less than one. Schur stability is open in the coefficients, so an arbitrarily small perturbation into the interior of the positive weight simplex gives \(w_j>0\) for every \(j\), including the first and last taps, without losing stability. Together with Step 3, this covers every \(0<G<G_n^*\).

**5. The sharp endpoint and the other equilibrium.** At \(\sqrt\Delta=2^n\), the binomial construction has \(r=1\) and \(P_+(z)=(z+1)^n\), while any other filter would violate the equality conditions of Step 2 if its roots all lay in the closed unit disk. For the negative branch, its polynomial has
\[
 P_-(1)=1-\beta+2G^2p_-=-\sqrt\Delta<0.
\]
Because \(P_-(z)\to+\infty\) for real \(z\to+\infty\), the intermediate value theorem supplies a real zero strictly greater than one. Finally \(\sqrt\Delta<2^n\) is algebraically equivalent to \(G<G_n^*\), completing the classification.

## Verification

The accompanying `verify.py` independently constructs the delay Jacobian for several lengths and checks that its characteristic polynomial matches the scalar recurrence; it also verifies the binomial coefficient identities with exact rational symbolic arithmetic, checks normalization and positivity of the proposed taps, and compares the finite-degree spectra numerically for selected gains. It returned `FIR_HENON_POLYNOMIAL_VERIFY_OK` when executed with SymPy and NumPy. The proof above, rather than floating-point root tests, establishes the quantified all-length and all-gain assertions. Multiple-root eigenvalue calculations can be ill-conditioned numerically, which is why the certificate checks the polynomial identities exactly.

## Relationship to prior work

Borges and Eisencraft, *A filtered Hénon map*, arXiv:2211.16964 (first publicly posted 2022-11-23), studied a two-tap feedback Hénon model and presented fixed-point stability plots and Lyapunov numerics. Borges, Silva and Eisencraft, *Chaotic properties of an FIR filtered Hénon map*, first publicly posted in its 2023-06-21 SSRN version, considered arbitrary FIR lengths, computed stationary branches and Jacobian matrices, and studied selected filter zero patterns numerically. Its accessible later arXiv manuscript (2401.10281) does not state the all-tap optimal spectral radius, unique binomial root-placement law, or exact gain frontier for all lengths. The fixed-point equation and companion linearization are taken as starting points, not claimed as new; the root-product inequality is elementary, while its sharp positive-tap realization yields the new optimal-design conclusion.

## Limitations

This is a local hyperbolic-stability theorem. At the sharp gain boundary the repeated multiplier \(-1\) precludes a hyperbolic sink but does not by itself classify nonlinear attraction or repulsion. The optimum concerns unconstrained positive taps with fixed sum, not a prescribed frequency response. The earlier SSRN full-text file could not be accessed for a same-version comparison; the later full manuscript was inspected. General root-placement and robust-filter literature beyond the indexed and directly inspected sources remains a publication-priority risk. The finite checker is diagnostic and is not an independent mathematical audit.

## References

1. V. S. Borges and M. Eisencraft, *A filtered Hénon map*, arXiv:2211.16964, first public 2022-11-23. https://arxiv.org/html/2211.16964v1
2. V. S. Borges, M. T. M. Silva and M. Eisencraft, *Chaotic Properties of an FIR Filtered Hénon Map*, SSRN:4487008, first public 2023-06-21. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4487008
3. Same authors, *Chaotic properties of an FIR filtered Hénon map*, arXiv:2401.10281, first arXiv version 2024-01-12; full text used for detailed equation and appendix comparison. https://arxiv.org/abs/2401.10281
