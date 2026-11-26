# Sharp moment cutoffs for the first Gaussian-sketched CUR pivot

## Finding

The first partially pivoted LU step on the transpose of a Gaussian sketch is unaffected by all but one sketch measurement. This has a precise statistical cost for rank-one cross approximation: its error-moment cutoff remains one even if arbitrarily many Gaussian sketch rows are available, while first-step column-pivoted QR improves the cutoff to the full number of sketch rows.

Let \(I_z(a,b)=B(a,b)^{-1}\int_0^z t^{a-1}(1-t)^{b-1}\,dt\). For the exact normalized spectral errors \(E_{\mathrm{LU}}\) and \(E_{\mathrm{CPQR}}\), and any real \(q>0\),
\[
\mathbb E E_{\mathrm{LU}}^q=1+(\kappa^q-1)\frac2\pi\arctan\frac1\kappa,
\qquad
\mathbb E E_{\mathrm{CPQR}}^q=1+(\kappa^q-1)I_{1/(1+\kappa^2)}(s/2,s/2).
\]
Writing \(c_s=2\Gamma(s)/(s\Gamma(s/2)^2)\), the exact large-condition-number phase diagram is
\[
\lim_{\kappa\to\infty}\mathbb E E_{\mathrm{LU}}^q=
\begin{cases}1&q<1,\\1+2/\pi&q=1,\\+\infty&q>1,\end{cases}\quad
\lim_{\kappa\to\infty}\mathbb E E_{\mathrm{CPQR}}^q=
\begin{cases}1&q<s,\\1+c_s&q=s,\\+\infty&q>s.\end{cases}
\]
In the supercritical regimes the differences from 1 are asymptotic to \((2/\pi)\kappa^{q-1}\) and \(c_s\kappa^{q-s}\), respectively. In particular, for every \(s\ge2\), the expected LU approximation error approaches \(1+2/\pi\), whereas the expected CPQR approximation error approaches 1; both errors nevertheless tend to 1 in probability.

## Assumptions and scope

Fix any integer \(s\ge2\), and any real \(\kappa>1\). Let \(A_\kappa=\operatorname{diag}(\kappa,1)\in\mathbb R^{2\times2}\) and \(S=(S_{ij})\in\mathbb R^{s\times2}\) have independent \(N(0,1)\) entries. Put \(Y=SA_\kappa\). The **LU rule** selects the original column index represented by the first row pivot in standard partial-pivoting elimination of \(Y^\mathsf T\in\mathbb R^{2\times s}\), without prior column permutation. The **CPQR rule** selects the index of the largest Euclidean-norm column of \(Y\), equivalently the first column pivot of ordinary column-pivoted QR applied to \(Y\). Each selected index \(j\in\{1,2\}\) determines the unique nonzero row \(i=j\) of the selected column of \(A_\kappa\). Set
\[
\widehat A_j=A_\kappa(:,j)\,[A_\kappa(j,j)]^{-1}A_\kappa(j,:),\qquad
E_j=\frac{\lVert A_\kappa-\widehat A_j\rVert_2}{\sigma_2(A_\kappa)}.
\]
The draws have no pivot ties with probability one; statements are in exact arithmetic. We do not claim anything about non-Gaussian sparse-sign embeddings, multi-column LU pivots, repeated CUR updates, or downstream Krylov iterations.

## Proof

**Cross-approximation loss.** Direct multiplication gives \(\widehat A_1=\operatorname{diag}(\kappa,0)\) and \(\widehat A_2=\operatorname{diag}(0,1)\). Since \(\sigma_2(A_\kappa)=1\), the normalized error is \(E_1=1\) or \(E_2=\kappa\). If \(p\) is the probability of choosing index 2, then \(\mathbb E E^q=1+(\kappa^q-1)p\), for every \(q>0\).

**Why the first LU pivot is oversampling-blind.** The first column of \(Y^\mathsf T\) is \((\kappa S_{11},S_{12})^\mathsf T\). By definition, the first row-partial-pivot picks the row having larger absolute entry in this column; hence the weak original column is selected precisely on \(\{|S_{12}|>\kappa|S_{11}|\}\), irrespective of the remaining \(s-1\) rows of \(S\). The independent standard normal ratio \(S_{12}/S_{11}\) has the standard Cauchy distribution. Its two-sided tail is \(p_{\rm LU}=(2/\pi)\arctan(1/\kappa)\), proving the first moment identity.

**The CPQR alternative.** CPQR compares \(\kappa\|S_{:,1}\|_2\) with \(\|S_{:,2}\|_2\). Independent random variables \(V=\|S_{:,1}\|_2^2\) and \(W=\|S_{:,2}\|_2^2\) each have a chi-squared distribution with \(s\) degrees of freedom. Thus \(Z=V/(V+W)\) has a beta distribution with parameters \((s/2,s/2)\). The weak-column event \(\kappa^2 V<W\) is exactly \(Z<1/(1+\kappa^2)\). It has probability \(p_{\rm CPQR}=I_{1/(1+\kappa^2)}(s/2,s/2)\). This gives the second identity.

**Sharp asymptotics and all boundary cases.** The arctangent expansion gives \(p_{\rm LU}\sim (2/\pi)\kappa^{-1}\). Let \(a=s/2>0\) and \(z=(1+\kappa^2)^{-1}\). Since \((1-t)^{a-1}=1+O(t)\) as \(t\downarrow0\), the beta integral gives
\[
I_z(a,a)=\frac{z^a}{a B(a,a)}(1+O(z))
=\frac{2\Gamma(s)}{s\Gamma(s/2)^2}\kappa^{-s}(1+O(\kappa^{-2})).
\]
Multiplying either probability by \(\kappa^q-1\) proves all three regimes, including the finite nonzero critical limits and sharp diverging powers. Both failure probabilities tend to zero, yielding convergence of each error to 1 in probability. Finally, if \(s=1\) is allowed, the beta half-half CDF reduces to the same Cauchy tail, so the distinct cutoffs require at least two sketch rows. \(\square\)

## Verification

The standalone `verify.py` checks the cross approximation for both column choices, independent first-pivot logic, analytic Cauchy formula, exact even-sketch beta-binomial CDFs, and numerical asymptotic constants. This finite checker is supplementary; the proof above covers every integer \(s\ge2\), every \(\kappa>1\), and every real \(q>0\). For example, at \(s=2\), \(p_{\rm CPQR}=1/(1+\kappa^2)\); with \(\kappa=100\), the mean LU relative error is about 1.63023 and the mean CPQR relative error about 1.00990.

## Relationship to prior work

Pritchard, Park, Nakatsukasa, and Martinsson introduce IterativeCUR using recycled sketches and LU-pivot-based row/column choices. Huh, Cartis, and Nakatsukasa subsequently describe an adaptive LSQR method and an appendix algorithm that chooses columns using row-partial-pivoted LU of \((SA)^\mathsf T\), while also discussing CPQR alternatives. Their principal algorithms typically use sparse-sign rather than dense Gaussian sketches and grow ranks adaptively. The present result isolates the first pivot in the mathematically standard Gaussian sketch specialization and calculates its exact statistical approximation-loss spectrum, as distinct from these papers' overall algorithm guarantees. Related analyses of rank-adaptive randomized pivoting and complete-pivot ACA concern different selection rules and do not imply the stated Cauchy-versus-beta cutoff comparison. These comparisons are not a proof of worldwide novelty.

## Limitations

The matrix is a two-mode diagonal model, and the analyzed output is a rank-one cross approximation using its correspondingly selected row, not a stabilized pseudoinverse CUR implementation over multiple ranks. The first pivot of partial LU is considered with the sketch-row order fixed; randomized reordering or alternative norm-based selection may change the conclusion. In the motivating implementations sparse-sign sketches are the default. This calculation does not establish failure or success of a complete adaptive LSQR solver, nor finite-precision behavior. An older, unindexed moment comparison for these exact pivot laws could exist.

## References

- Nathaniel Pritchard, Taejun Park, Yuji Nakatsukasa, Per-Gunnar Martinsson. *IterativeCUR: Large Rank-Adaptive Approximation From a Small Recycled Sketch*. arXiv:2509.21963 (initial public version 2025-09-26), https://arxiv.org/abs/2509.21963 .
- Jung Eun Huh, Coralia Cartis, Yuji Nakatsukasa. *Adaptive LSQR Preconditioning from One Small Sketch*. arXiv:2604.05065 (initial public version 2026-04-06), Appendix B.1, Algorithms 4, 6 and 7, https://arxiv.org/html/2604.05065v1 .
