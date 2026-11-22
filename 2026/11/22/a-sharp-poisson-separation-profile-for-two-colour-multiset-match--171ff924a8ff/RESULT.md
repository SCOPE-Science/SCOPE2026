# A sharp Poisson-separation profile for two-colour multiset matches

## Finding

Let \(a_n,b_n\) be positive integers with \(a_n+b_n=n\to\infty\) and \(a_n/n\to c\in(0,1)\). Choose uniformly one of the \(\binom n{a_n}\) words containing \(a_n\) copies of the first symbol and \(b_n\) copies of the second. Let \(W_n\) count positions agreeing with the sorted two-block word, and let \(Z_n\) be Poisson with the exact mean \(\lambda_n=(a_n^2+b_n^2)/n\) of \(W_n\). Define
\[
h=c^2+(1-c)^2,\qquad v=4c^2(1-c)^2,
\qquad t=\sqrt{\frac{2vh}{h-v}\log\!\left(2\sqrt{h/v}\right)}.
\]
Here \(0<v<h\), and \(\Phi\) and \(\overline\Phi=1-\Phi\) denote the standard normal distribution and survival functions.

**Theorem (sharp whole-law separation).** For every such sequence,
\[
\boxed{\lim_{n\to\infty}d_{\mathrm{TV}}\bigl(\mathcal L(W_n),\mathcal L(Z_n)\bigr)
=D(c):=\frac12+\overline\Phi(t/\sqrt h)-2\overline\Phi(t/\sqrt v).}
\]
The function \(D(c)\) is symmetric about \(1/2\), strictly decreasing on \((0,1/2]\), strictly increasing on \([1/2,1)\), and tends to \(1\) as \(c\to0\) or \(c\to1\). In particular the following **universal sharp non-Poisson obstruction** holds:
\[
\boxed{D(c)\ge D(1/2)=0.533230687960\ldots,}
\]
with equality only for the balanced proportion \(c=1/2\).

The mismatch persists even after enforcing the correct parity. Put \(Z_n^\circ\stackrel d=Z_n\mid\{Z_n\equiv n\pmod2\}\), and define
\[
s=\sqrt{\frac{vh}{h-v}\log(h/v)}.
\]
Then
\[
\boxed{\lim_{n\to\infty}d_{\mathrm{TV}}\bigl(\mathcal L(W_n),\mathcal L(Z_n^\circ)\bigr)
=R(c):=2\bigl[\Phi(s/\sqrt v)-\Phi(s/\sqrt h)\bigr].}
\]
Here \(R(c)\ge R(1/2)=0.166064074983\ldots\), again with equality only for \(c=1/2\). Thus the failure has **two distinct causes**: an exactly forbidden parity class and a genuine Gaussian variance mismatch that survives parity correction.

## Assumptions and scope

The two symbols are distinguishable, but their repeated copies are not. All distinct multiset arrangements are equiprobable. A fixed position compares the new word with the original sorted word, not with individually labelled copies. Total variation is \(d_{\mathrm{TV}}(P,Q)=\tfrac12\sum_{j\ge0}|P\{j\}-Q\{j\}|\). The regime requires both multiplicities to be asymptotically positive proportions; no uniformity is claimed when \(a_n/n\) approaches either endpoint. The Poisson law has the **exact**, not just asymptotic, matching mean, and the parity-conditioned law is well-defined for all \(n\ge2\).

## Proof

**1. Exact hypergeometric reduction.** Write \(a=a_n\), \(b=n-a\). If \(X\) counts first-symbol occurrences among the first \(a\) positions, sampling those positions without replacement gives
\[
\Pr(X=x)=\frac{\binom ax\binom b{a-x}}{\binom na},\qquad
\max(0,a-b)\le x\le a.
\]
There are \(a-X\) first-symbol occurrences in the last \(b\) positions, so precisely \(b-a+X\) second-symbol occurrences there. Consequently
\[
W=b-a+2X,\qquad W\equiv n\pmod2,
\]
\[
\mathbb EW=\lambda_n=\frac{a^2+b^2}{n},\qquad
\operatorname{Var}(W)=\frac{4a^2b^2}{n^2(n-1)}.
\]
Both the parity constraint and the reduced asymptotic variance are exact consequences of the two-by-two count conservation law.

**2. Local limits at their respective lattice spans.** Let \(\phi_q(x)=(2\pi q)^{-1/2}\exp(-x^2/(2q))\) for \(q>0\), and let \(x_{n,j}=(j-\lambda_n)/\sqrt n\). Expanding the three factorials in the hypergeometric mass from Step 1 by Stirling's formula, uniformly for \(|x_{n,j}|\le A\) with any fixed finite \(A\), gives
\[
\Pr(W_n=j)=\frac2{\sqrt n}\bigl[\phi_v(x_{n,j})+o(1)\bigr],
\quad j\equiv n\pmod2.
\]
Indeed \(\operatorname{Var}(X_n)/n\to c^2(1-c)^2=v/4\), the first derivative of the log mass vanishes at the mean to first order, and its second-order Taylor term is \(-x_{n,j}^2/(2v)\); the normalization prefactor is the span-two local normal prefactor above. For other \(j\), the probability is exactly zero. Separately, Stirling's formula for the Poisson mass, using \(\lambda_n/n\to h\), yields uniformly on the same compact windows
\[
\Pr(Z_n=j)=\frac1{\sqrt n}\bigl[\phi_h(x_{n,j})+o(1)\bigr].
\]
Both centered variables divided by \(\sqrt n\) are tight: their variances divided by \(n\) converge respectively to \(v\) and \(h\), so Chebyshev bounds tails outside \(|x_{n,j}|\le A\) by \(O(A^{-2})\). The local approximations may therefore be summed as Riemann sums without unproved tail interchange.

**3. Unconditioned total-variation limit.** Each parity lattice has mesh \(2/\sqrt n\) in centered coordinates. On the attainable parity, the absolute mass difference gives \(\tfrac14\int_{\mathbb R}|2\phi_v(x)-\phi_h(x)|\,dx\) in the limiting total variation; on the opposite parity, the Poisson mass contributes \(1/4\), because \(\Pr(Z_n\equiv n\pmod2)=[1+(-1)^n e^{-2\lambda_n}]/2\to1/2\). Thus
\[
D(c)=\frac14\left(1+\int_{\mathbb R}|2\phi_v(x)-\phi_h(x)|\,dx\right).
\]
Since \(v<h\), the two functions \(2\phi_v\) and \(\phi_h\) intersect exactly at \(\pm t\), with \(2\phi_v>\phi_h\) strictly between the intersections; solving their equality gives the stated value of \(t\). Integrating the positive and negative regions and using \(\int(2\phi_v-\phi_h)=1\) yields
\[
D(c)=\frac12+\overline\Phi(t/\sqrt h)-2\overline\Phi(t/\sqrt v).
\]

**4. Parity-conditioned limit.** The Poisson probability of the attainable parity tends to \(1/2\), so on that parity its conditioned mass is \((2/\sqrt n)[\phi_h(x_{n,j})+o(1)]\), uniformly in compact windows. Tightness still holds after conditioning, because the conditioning probability is bounded away from zero. Accordingly
\[
R(c)=\frac12\int_{\mathbb R}|\phi_v(x)-\phi_h(x)|\,dx.
\]
The normal densities intersect at \(\pm s\), where \(s^2=vh\log(h/v)/(h-v)\). Integrating gives the displayed formula for \(R(c)\).

**5. Sharpness over all macroscopic proportions.** Put \(u=c(1-c)\in(0,1/4]\). Then \(v/h=4u^2/(1-2u)\), strictly increasing in \(u\), with maximum \(1/2\) exactly at \(c=1/2\). Scale the normal densities to set \(h=1\), write \(r=v/h\), and note that
\[
D=\frac14\left(1+\|2\phi_r-\phi_1\|_{L^1}\right),
\qquad R=\frac12\|\phi_r-\phi_1\|_{L^1}.
\]
For \(0<r_1<r_2<1\), take \(\alpha=(1-r_2)/(1-r_1)\in(0,1)\). The Ornstein–Uhlenbeck Gaussian kernel \(x\mapsto\sqrt\alpha\,x+\sqrt{1-\alpha}\,G\), where \(G\) is standard normal, sends \(N(0,r_1)\) to \(N(0,r_2)\) and fixes \(N(0,1)\). A Markov kernel contracts the total-variation norm of every finite signed measure. Here contraction is **strict** for both signed differences: their densities have nonempty positive and negative regions, and the Gaussian kernel has a strictly positive density everywhere, producing strict cancellation. Hence both \(D\) and \(R\) decrease strictly as \(r\) increases. Both achieve unique minima at \(c=1/2\), with the stated constants. As \(r\downarrow0\), the narrow normal becomes asymptotically singular relative to \(N(0,1)\), giving \(D\to1\). Symmetry under swapping the two symbols completes the proof.

## Verification

The standalone standard-library program `check.py` enumerates all distinct binary words of lengths \(2\) through \(11\), checks their agreement-count probabilities against the exact hypergeometric formula, and independently checks exact means and variances via rational arithmetic. It performs 660 exact assertions. It also evaluates the exact finite-sample total-variation sums at several sizes and compares their convergence to both analytic profile functions; these numerical diagnostics are not used as proofs of the limits. Run `python3 check.py` beside this file; its expected output is reproduced in `CHECK_LOG.txt`.

## Relationship to prior work

Stark's 2026 investigation of fixed points of random multiset permutations gives the model, the general mean/variance and finite Poisson-approximation bounds. It discusses both bounded expected counts and regimes where the mean is proportional to the word length, but does not give a sharp full-distribution total-variation limit in the macroscopic two-symbol regime. A published exact-support classification establishes the two-symbol parity constraint for every finite multiplicity profile; the constraint alone gives only a limiting total-variation lower bound of \(1/2\), while the present result computes the strictly larger gap and the surviving parity-conditioned gap, including sharp minima over all proportions. A separate published Poisson–Charlier result treats one repeated symbol of order \(\sqrt n\) and all remaining symbols distinct, a regime with bounded mean and vanishing Poisson error, and does not imply the two-macroscopic-block profile. The hypergeometric and Poisson local Gaussian approximations themselves are classical; the contribution is their precise lattice-sensitive total-variation comparison, the closed profile and its sharp composition optimization in this natural multiset model.

## Limitations

The result is asymptotic for fixed interior limiting proportions. It does not give an explicit finite-size rate, a full multicolour profile or a uniform two-symbol endpoint regime. It does not establish novelty against all historical work: a yet-unlocated general lattice local-limit comparison could subsume the profile after specialization. No independent mathematical validation has occurred.

## References

1. Dudley Stark, *Poisson approximations of the number of fixed points in random multiset permutations*, arXiv:2608.00710, first publicly submitted 2026-08-01, https://arxiv.org/abs/2608.00710 .
2. *Exact fixed-point support and constructive mismatch spectrum for multiset permutations*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-fixed-point-support-and-constructive-mismatch-spectrum-for--3698ed40fe98 .
3. *Sharp Poisson approximation for one square-root multiset block*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-poisson-approximation-for-one-square-root-multiset-block--b21e06270e4c .
4. A. D. Barbour, L. Holst and S. Janson, *Poisson Approximation*, Clarendon Press, Oxford, 1992 (general approximation background).
