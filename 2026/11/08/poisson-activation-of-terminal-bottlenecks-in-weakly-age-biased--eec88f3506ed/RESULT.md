# Poisson activation of terminal bottlenecks in weakly age-biased recursive trees

## Finding

Fix an integer \(m\ge1\). Start with vertex \(v_0\). At each integer time \(t\ge1\), attach the new vertex \(v_t\) by \(m\) independently drawn edges to earlier vertices; for \(0\le k<t\), each edge chooses \(v_k\) with probability proportional to \(e^{\beta k}\), where \(\beta>0\). Parallel edges are retained when \(m>1\).

Let \(A_j\) denote the event that all \(m\) parents of \(v_{j+1}\) equal \(v_j\) and no future edge has a parent in \(\{v_0,\dots,v_j\}\). Define

\[
r=e^{-\beta},\qquad
\rho_\beta=\left[(1-r)\prod_{h=1}^\infty(1-r^h)\right]^m,
\qquad
\Xi_\beta=\sum_{j\ge0}\mathbf1_{A_j}\delta_{\rho_\beta(j+1)}.
\]

**Theorem.** For each fixed positive integer \(m\), as \(\beta\downarrow0\), \(\Xi_\beta\) converges in distribution, in the vague topology for locally finite counting measures on \([0,\infty)\), to the homogeneous Poisson point process with intensity one. The first terminal bottleneck index \(J_\beta=\min\{j+1:A_j\}\) is almost surely finite and satisfies

\[
\rho_\beta J_\beta\ \Longrightarrow\ \operatorname{Exp}(1).
\]

The exact one-point probabilities and the activation scale are

\[
\Pr(A_j)=\left[(1-r)\prod_{h=1}^{j}(1-r^h)\right]^m,
\qquad
\rho_\beta=(2\pi\beta)^{m/2}
\exp\!\left(-\frac{m\pi^2}{6\beta}\right)(1+O_m(\beta)).
\]

The \(m=1\) model is precisely the young-vertex-favoring case of the exponentially preferential recursive tree of Aguech–Mahmoud–Mohamed–Yang (2025). The extension to fixed \(m>1\) allows parallel parents.

## Assumptions and scope

Birth times are \(0,1,2,\ldots\); all parent choices are mutually independent. The integer \(m\ge1\) is fixed while \(\beta\downarrow0\); the theorem does not cover growing \(m\), degree-biased choices or different edge-weight kernels. The bottleneck event uses *all subsequent births*: a finite-time edge count does not certify the infinite-horizon condition. Convergence refers to the unconditioned random infinite graph, not its walk or a conditional environment. The first index uses the right endpoint \(j+1\).

## Proof

**1. Exact finite-start cut probabilities.** At time \(t\), the backward lag \(L=t-k\) of a selected parent has law

\[
\Pr(L=\ell)=\frac{(1-r)r^{\ell-1}}{1-r^t},\qquad1\le\ell\le t.
\]

For the cut at \(j\), the first requisite lag is one at \(t=j+1\). At subsequent time \(t=j+1+h\), \(h\ge1\), the required lag is at most \(h\), with probability \((1-r^h)/(1-r^{j+1+h})\). Taking independent choices and telescoping the infinite products gives

\[
\begin{aligned}
\Pr(A_j)^{1/m}
&=\frac{1-r}{1-r^{j+1}}\prod_{h=1}^\infty\frac{1-r^h}{1-r^{j+1+h}}\\
&=(1-r)\prod_{h=1}^{j}(1-r^h)=:b_j^{1/m}.
\end{aligned}
\]

In particular, \(b_j\downarrow\rho_\beta\) as \(j\to\infty\). The same computation gives exact probabilities for finite truncations; no interchange of random sums is needed.

**2. Stationary lag coupling.** Extend the parent choices to independent geometric lag variables \(G_{t,a}\) (\(t\in\mathbb Z\), \(1\le a\le m\)) with \(\Pr(G=\ell)=(1-r)r^{\ell-1}\). A finite-start lag is a geometric variable conditioned on \(G\le t\). Couple these choices so they agree whenever \(G\le t\), resampling conditionally on the other outcome. The probability that any choice differs at \(t\ge K\) is at most

\[
m\sum_{t\ge K}r^t=\frac{mr^K}{1-r}.
\]

Choose the integer \(K=\lceil\beta^{-2}\rceil\). This mismatch bound tends to zero. The infinite-stationary bottleneck \(B_j\), defined by the same lag inequalities, has intensity exactly \(\rho_\beta\). Events \(A_j\) and \(B_j\) agree for every \(j\ge K\) on the coupling-success event.

**3. Finite dependence and exact pair law.** Write \(B_j^{(K)}\) for the event restricted to births \(j+1,\ldots,j+K\). This indicator depends only on the \(mK\) lag variables in that interval, so disjoint windows at distance at least \(K\) are independent. Let

\[
\rho_{\beta,K}=\Pr(B_j^{(K)})
=\left[(1-r)\prod_{h=1}^{K-1}(1-r^h)\right]^m.
\]

If \(1\le d<K\), the conditions from the later cut are stricter wherever its window overlaps the earlier window. The earlier cut adds only its first \(d\) birth constraints, all independent of the later window. Consequently the exact joint probability is

\[
\Pr(B_j^{(K)}\cap B_{j+d}^{(K)})
=\rho_{\beta,K}\,b_{d-1}.
\]

The relative truncation error obeys

\[
0\le\frac{\rho_{\beta,K}}{\rho_\beta}-1
\le \exp\!\left(O_m\!\left(\frac{r^K}{1-r}\right)\right)-1=o(1).
\]

**4. Anti-clustering.** For \(d\ge0\), \(b_d=(1-r)^m\prod_{h=1}^{d}(1-r^h)^m\). Set \(D=\lfloor\beta^{-1/2}\rfloor\). When \(h\le D\), \(1-e^{-\beta h}\le\beta h\le\sqrt\beta\), hence \(b_d\le\beta^m(\sqrt\beta)^{md}\) for \(d\le D\). For \(D<d<K\), monotonicity yields \(b_d\le\beta^m(\sqrt\beta)^{mD}\). Because \(K=O(\beta^{-2})\), it follows that

\[
\sum_{d=0}^{K-1}b_d=O_m(\beta^m)\longrightarrow0.
\]

**5. Poisson approximation.** On any bounded rescaled interval of length \(H\), the number of candidate sites is at most \(H/\rho_\beta+2\). The usual dependency-neighborhood Poisson point-process estimate (equivalently, the marked Stein–Chen bound applied to finitely many disjoint test intervals) has error controlled by

\[
\begin{aligned}
S_1&\le C_H(\rho_\beta^{-1}+1)K\rho_{\beta,K}^2=O_H(K\rho_\beta)=o(1),\\
S_2&\le C_H(\rho_\beta^{-1}+1)\rho_{\beta,K}\sum_{d=0}^{K-1}b_d=O_{H,m}(\beta^m)=o(1).
\end{aligned}
\]

Therefore the stationary truncated cut process converges jointly on disjoint bounded test intervals to independent Poisson counts with means equal to interval lengths. The locations sit on a mesh of size \(\rho_\beta\), which tends to zero; this yields convergence of locally finite counting measures. The expected number of discarded early finite-start cuts is at most

\[
\sum_{j<K}b_j=O_m(\beta^m),
\]

and the coupling and truncation errors in a bounded rescaled interval are bounded respectively by \(mr^K/(1-r)\) and \((H/\rho_\beta+2)(\rho_{\beta,K}-\rho_\beta)=o(1)\). Thus the original process \(\Xi_\beta\) has the same Poisson limit.

**6. First cut and scale.** The convergence on \([0,H]\) gives \(\Pr(\rho_\beta J_\beta>H)\to e^{-H}\). Taking all fixed \(H>0\) yields the exponential limit. For fixed \(\beta>0\), the stationary geometric lag process is ergodic and \(\Pr(B_j)=\rho_\beta>0\), so infinitely many \(B_j\) occur almost surely; the finite-start coupling differs from it only at finitely many sufficiently late births almost surely, proving existence of \(J_\beta\). Finally, the classical Dedekind product asymptotic is

\[
\prod_{h\ge1}(1-e^{-\beta h})
=\sqrt{\frac{2\pi}{\beta}}\exp\!\left(-\frac{\pi^2}{6\beta}+\frac\beta{24}\right)
\bigl(1+O(e^{-4\pi^2/\beta})\bigr).
\]

Together with \(1-e^{-\beta}=\beta(1+O(\beta))\), this gives the stated essential-exponential activation scale.

## Verification

The standalone standard-library checker `verify.py` exercises the exact finite-horizon original-law formula against exhaustive enumerations, exact rational pair probabilities for overlapping truncated windows, and small-parameter product and anti-clustering estimates. Execute `python3 verify.py`. These finite checks do not certify the infinite weak limit; that follows from the analytical steps above.

## Relationship to prior work

Aguech, Mahmoud, Mohamed and Yang (2025) introduce the same exponentially preferential recursive tree when \(m=1\), but their limit theorems concern the outdegree of selected vertices. Tang, Wang and Wu (preprint dated November 2, 2026) formulate the terminal bottlenecks and fixed-parameter renewal structure for the \(m\)-edge growth model, proving recurrence and infinite collisions; those bottlenecks, their existence, and renewal are **not** claimed as new here. The claim concerns the nontrivial \(\beta\downarrow0\) **Poisson point-process scaling**, exact essential-exponential intensity and exponential first-cut activation. Classical Stein–Chen approximation supplies the probability approximation method, not the model-specific estimates.

## Limitations

Historical priority cannot be guaranteed by search alone. A sufficiently general existing rare-event renewal/point-process theorem might imply the Poisson limit after verifying its hypotheses. The result fixes \(m\), applies only to independent exponential-age parent selection and describes infinite-horizon terminal cuts, not the random-walk limiting motion, finite-volume mixing or large-\(m\) regime. Verification code checks only finite identities and quantitative surrogates; independent expert review has not occurred.

## References

1. R. Aguech, H. Mahmoud, H. Mohamed, Z. Yang, *Exponentially preferential trees*, Network Science **13** (2025), e5, first published April 14, 2025, https://doi.org/10.1017/nws.2025.3.
2. J. Tang, F. Wang, X.-Y. Wu, *Random Walk on age-preferential random growth processes*, arXiv:2611.02329, first posted November 2, 2026, https://arxiv.org/abs/2611.02329. Cited as later comparative literature, not as an eligible starting source.
3. R. Arratia, L. Goldstein, L. Gordon, *Two moments suffice for Poisson approximations: the Chen–Stein method*, Annals of Probability **17** (1989), 9–25, https://projecteuclid.org/euclid.aop/1176991491.
4. L. H. Y. Chen, A. Xia, *Stein's method, Palm theory and Poisson process approximation*, Annals of Probability **32** (2004), 2545–2569, https://arxiv.org/abs/math/0410169.
