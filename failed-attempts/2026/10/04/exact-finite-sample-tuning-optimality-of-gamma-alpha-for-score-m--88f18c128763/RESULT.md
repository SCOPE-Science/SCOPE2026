# Exact finite-sample tuning optimality of \(\gamma=\alpha\) for SCoRE-MDR

## Finding

Fix a nominal marginal deployment risk level \(\alpha\in(0,1)\). In the SCoRE-MDR construction of Bai and Jin, let
\[
\psi_\gamma=\mathbf{1}\{E_{\gamma,n+1}\ge 1/\alpha\}\,,\qquad \gamma\in(0,1),
\]
be the deploy/abstain decision based on their risk-adjusted e-value. Then, for every realized calibration sample, every realized calibration-risk vector in \([0,1]^n\), and every realized test score,
\[
\boxed{\psi_\gamma\le \psi_\alpha\quad\text{for every }\gamma\in(0,1).}
\]
Thus the recommended choice \(\gamma=\alpha\) is not merely asymptotically power-optimal: it is pointwise finite-sample optimal over the full tuning family. Consequently, for every nonnegative deployment reward \(r\),
\[
\mathbb E[r\psi_\gamma]\le \mathbb E[r\psi_\alpha]
\]
whenever the expectations exist.

The same pathwise dominance holds for the known-covariate-shift weighted SCoRE-MDR construction in the paper. The dominance is sharp in the family: for every \(\gamma\ne\alpha\), there are admissible finite samples on which \(\psi_\alpha=1\) and \(\psi_\gamma=0\).

## Assumptions and scope

The unweighted statement uses exactly the SCoRE-MDR e-value and threshold rule in Bai and Jin, with calibration risks in \([0,1]\), a score function independent of the held-out calibration/test labels as required by their setup, and nominal decision threshold \(1/\alpha\). No distributional assumption is needed for the pointwise comparison itself. Exchangeability is needed for the paper's finite-sample MDR validity of each member of the family.

For the weighted extension, the importance weights are the positive known covariate-shift weights used in the paper's weighted MDR construction. Again, the dominance argument is deterministic conditional on the realized data and weights; the shift assumptions are needed for the corresponding risk-control validity, not for the ordering of decisions.

The result concerns the MDR tuning parameter \(\gamma\). It does not claim an analogous ordering for the paper's SDR/e-BH procedure, whose coupled selection rule is structurally different.

## Proof

Write
\[
Q=\frac{1+\sum_{i=1}^n L_i\mathbf{1}\{s(X_i)\le s(X_{n+1})\}}{n+1}.
\]
Bai and Jin's Proposition 4.4 gives the exact finite-sample decision rule. If \(\gamma\le\alpha\), then
\[
\psi_\gamma=\mathbf{1}\{Q\le\gamma\}.
\]
Therefore \(\psi_\gamma\le\mathbf{1}\{Q\le\alpha\}=\psi_\alpha\).

Now let \(\gamma>\alpha\). Proposition 4.4 states that \(\psi_\gamma=1\) only if both \(Q\le\gamma\) and
\[
\frac{\ell+\sum_{i=1}^n L_i\mathbf{1}\{s(X_i)\le t\}}{n+1}
\notin(\alpha,\gamma]
\]
for every score threshold \(t\) in the pooled score set and every \(\ell\in[0,1]\). Choose specifically \(t=s(X_{n+1})\) and \(\ell=1\). The displayed quantity is then exactly \(Q\). Hence \(\psi_\gamma=1\) implies
\[
Q\le\gamma\quad\text{and}\quad Q\notin(\alpha,\gamma],
\]
which forces \(Q\le\alpha\). Proposition 4.4 at \(\gamma=\alpha\) then yields \(\psi_\alpha=1\). Thus \(\psi_\gamma\le\psi_\alpha\) also for \(\gamma>\alpha\).

Multiplying the pointwise inequality by any nonnegative reward \(r\) and taking expectations gives the finite-sample reward dominance.

For the weighted construction, the proof of the paper's weighted analogue replaces \(Q\) by
\[
Q_w=\frac{w_{n+1}+\sum_{i=1}^n w_iL_i\mathbf{1}\{s(X_i)\le s(X_{n+1})\}}{\sum_{i=1}^n w_i+w_{n+1}}.
\]
Its extra condition for \(\gamma>\alpha\) again quantifies over all thresholds and \(\ell\in[0,1]\). Taking \(t=s(X_{n+1})\) and \(\ell=1\) makes that quantity equal \(Q_w\), so the identical implication proves weighted pointwise dominance.

Sharpness is constructive. If \(\gamma<\alpha\), choose \(n\) large enough that \(1/(n+1)<\alpha\), choose \(q\in(\max\{\gamma,1/(n+1)\},\alpha]\), put all calibration scores below the test score, and choose calibration risks summing to \((n+1)q-1\). Then \(Q=q\), so \(\psi_\alpha=1\) but \(\psi_\gamma=0\).

If \(\gamma>\alpha\), choose \(n\) so that \(1/(n+1)\le\alpha\). Put the test score below all positive-risk calibration scores, so \(Q=1/(n+1)\le\alpha\). Choose the calibration risks so that at a larger calibration-score threshold the quantity with \(\ell=1\) equals some \(q\in(\alpha,\gamma]\). Then \(\psi_\alpha=1\), while the extra condition for \(\gamma>\alpha\) fails, so \(\psi_\gamma=0\).

## Verification

The argument is an exact consequence of the decision characterization in Proposition 4.4 and its weighted analogue. The standalone script `artifacts/verify.py` checks the implication algebra on deterministic random finite samples and constructs strict witnesses on both sides of \(\alpha\). Running

`python artifacts/verify.py`

prints `VERIFY_OK`.

The computation is supplementary: the theorem follows from substituting \(t=s(X_{n+1})\) and \(\ell=1\) into the paper's exact finite-sample characterization.

## Relationship to prior work

Bai and Jin introduce SCoRE and prove finite-sample MDR validity for every fixed \(\gamma\). Their Proposition 4.4 gives the two exact decision regimes used above. Their Remark 4.5 explicitly notes that \(\gamma<\alpha\) selects no more often than \(\gamma=\alpha\), while for \(\gamma>\alpha\) it emphasizes an extra condition and asymptotically vanishing power. Their Theorem 4.6 further states that \(\gamma=\alpha\) is asymptotically power-optimal for a fixed score. The pointwise finite-sample dominance for all \(\gamma>\alpha\), and therefore the finite-sample reward-optimality over the entire tuning family, is not stated there.

The original conformal risk control framework of Angelopoulos, Bates, Fisch, Lei, and Schuster controls monotone expected losses but does not contain the SCoRE risk-adjusted e-value tuning family. Xu, Guo, and Wei's selective conformal risk control uses a distinct two-stage selective calibration framework and likewise does not imply this \(\gamma\)-ordering.

Targeted published-finding and scholarly searches did not locate an equivalent finite-sample pointwise dominance theorem. This supports non-coverage by the checked sources but is not a claim of exhaustive historical priority.

## Limitations

The theorem orders only the one-parameter SCoRE-MDR family generated by varying \(\gamma\) while holding the score, data, nominal level, and construction fixed. It does not compare different score functions, alternative e-values, randomized procedures, or SDR rules. Pointwise deployment dominance does not mean that deploying more is always preferable under every downstream utility model; the reward corollary assumes nonnegative reward for deployment. Literature searches cannot rule out equivalent observations in unindexed notes, code comments, or unpublished work.

## References

1. T. Bai and Y. Jin, “Conformal Selective Prediction with General Risk Control,” arXiv:2603.24704, first submitted 25 March 2026. https://arxiv.org/abs/2603.24704
2. A. N. Angelopoulos, S. Bates, A. Fisch, L. Lei, and T. Schuster, “Conformal Risk Control,” ICLR 2024; arXiv:2208.02814. https://arxiv.org/abs/2208.02814
3. Y. Xu, W. Guo, and Z. Wei, “Selective Conformal Risk Control,” arXiv:2512.12844, first submitted 14 December 2025. https://arxiv.org/abs/2512.12844
