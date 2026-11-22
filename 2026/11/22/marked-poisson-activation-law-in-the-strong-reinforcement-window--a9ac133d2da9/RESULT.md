# Marked Poisson activation law in the strong-reinforcement window for preferential-attachment trees

## Finding

Consider a linear preferential-attachment rooted tree with attachment weight \(1+a\deg^+(v)\). The **first child of each nonroot vertex** is an activation. At the arrival of vertex \(t+1\), write \(Z_t=j\) if the newborn vertex chooses an as-yet-childless parent with birth index \(j\), and write \(Z_t=0\) if no such activation occurs. Thus \(t\in\{2,\ldots,n-1\}\) and any positive \(Z_t\) belongs to \(\{2,\ldots,t\}\).

**Finite-sample marked-history coupling.** For all integers \(n\ge2\) and all real \(a\ge1\), let \((Y_t)_{t=2}^{n-1}\) be independent random variables with
\[
\Pr(Y_t=0)=1-\frac1a,\qquad
\Pr(Y_t=j)=\frac{1}{a(t-1)}\quad(2\le j\le t).
\]
Then, for the complete labelled activation history,
\[
\boxed{\quad d_{\mathrm{TV}}\bigl(\mathcal L((Z_t)_{t=2}^{n-1}),\mathcal L((Y_t)_{t=2}^{n-1})\bigr)
\le \frac{2(n-2)}{a^2}.\quad}
\]
This bound controls all joint first-parent events, including their original birth labels, rather than only the number of activated vertices.

**Two-dimensional critical limit.** For each \(n\), sample a fresh tree with constant attachment parameter \(a_n\ge1\) throughout its growth. If \(n/a_n\to\lambda\in[0,\infty)\), then the finite point measure
\[
\Xi_n=\sum_{t=2}^{n-1}\mathbf 1_{\{Z_t\ne0\}}\,\delta_{(t/n,\,Z_t/t)}
\]
converges in distribution (weak convergence of finite point measures on the unit square) to a homogeneous Poisson point process with intensity \(\lambda\,du\,dw\). In particular, the number of nonroot vertices that acquire children converges to \(\operatorname{Poisson}(\lambda)\), and
\[
\Pr(\text{the resulting tree is a rooted star})\longrightarrow e^{-\lambda}.
\]
For \(\lambda=0\) the point process is empty. No claim is made for \(n/a_n\to\infty\).

## Assumptions and scope

The tree starts with the singleton vertex \(1\). At each integer \(t\ge1\), vertex \(t+1\) is attached to an existing vertex \(v\) with probability proportional to \(1+a\deg^+_{T_t}(v)\), where \(\deg^+\) counts children relative to the root. The same real \(a\) is used at all steps for a given finite tree; in the critical triangular array it may depend on the final order \(n\). The root gains its first child deterministically when vertex \(2\) is added; we count only subsequent, nonroot activations. Total variation means \(\sup_B|\Pr(U\in B)-\Pr(V\in B)|\) on the indicated finite history space.

## Proof

**1. Exact one-step marked probabilities.** At the moment immediately before vertex \(t+1\) arrives, the total attachment weight is \(D_t=t+a(t-1)\). Let \(A_t\) be the set of vertices already having a child, including root \(1\), and put \(H_t=|A_t|\). Every \(j\in\{2,\ldots,t\}\setminus A_t\) has attachment weight one, so conditional on the entire tree,
\[
\Pr(Z_t=j\mid T_t)=\frac1{D_t}
\quad\text{for }j\notin A_t,\qquad
\Pr(Z_t=0\mid T_t)=1-\frac{t-H_t}{D_t}.
\]
The activated set evolves by adding \(j\) when \(Z_t=j\), and it starts at \(A_2=\{1\}\). Therefore this kernel specifies the exact joint law of all \(Z_t\) without needing the degree allocation among already activated vertices.

**2. Exact thinning of independent marked trials.** Independently for each \(t\), generate \(Y_t\) with the law above and an additional independent uniform \([0,1]\) coin. If \(Y_t=j>0\) and \(j\notin A_t\), accept the mark as \(Z_t=j\) with probability
\[
\theta_t=\frac{a(t-1)}{t+a(t-1)}\le1.
\]
Otherwise set \(Z_t=0\). By multiplication, an eligible \(j\) is activated with conditional probability \(\frac{1}{a(t-1)}\theta_t=1/D_t\). Hence this construction gives the exact marked activation history while satisfying \(Z_t\ne0\Rightarrow Z_t=Y_t\). The two histories can differ only upon rejection of a positive trial.

**3. Uniform rejection bound.** The conditional probability of rejection at time \(t\), given the previously constructed activated set, is
\[
\frac1a-\frac{t-H_t}{D_t}
=\frac{t+a(H_t-1)}{aD_t}.
\]
Every prior activation must have arisen from a prior positive independent trial. Consequently
\[
H_t-1\le\sum_{s=2}^{t-1}\mathbf1_{\{Y_s\ne0\}},
\qquad \mathbb E(H_t-1)\le\frac{t-2}{a}.
\]
Because \(D_t\ge a(t-1)\) and \(t+(t-2)=2(t-1)\), the expected rejection probability at each \(t\ge2\) is at most \(2/a^2\). A union bound over \(n-2\) trials therefore bounds the probability of any mismatch by \(2(n-2)/a^2\). The standard coupling inequality proves the total-variation assertion.

**4. Marked Poisson convergence.** Define the independent reference point measure \(\widetilde\Xi_n\) by replacing \(Z_t\) with \(Y_t\) in the definition of \(\Xi_n\). The coupling gives \(\Pr(\Xi_n\ne\widetilde\Xi_n)\le2(n-2)/a_n^2\), which tends to zero whenever \(n/a_n\) has a finite limit (then \(a_n\to\infty\)). For every continuous nonnegative function \(f\) on \([0,1]^2\), independence yields
\[
\mathbb E e^{-\langle f,\widetilde\Xi_n\rangle}
=\prod_{t=2}^{n-1}\left[1-\frac{1}{a_n}
\left(1-\frac{1}{t-1}\sum_{j=2}^{t}e^{-f(t/n,j/t)}\right)\right].
\]
For \(t/n\) bounded away from zero, the interior average converges uniformly to \(\int_0^1 e^{-f(t/n,w)}dw\). The contribution of \(t/n\) near zero is bounded by its relative interval length. Taking logarithms, using \(n/a_n\to\lambda\) and \(n/a_n^2\to0\), gives
\[
\exp\left[-\lambda\int_0^1\int_0^1
(1-e^{-f(u,w)})\,dw\,du\right],
\]
the Laplace functional of the stated Poisson point process. This proves weak convergence of finite point measures. Its total point count is Poisson with mean \(\lambda\). The event that the growing tree is a rooted star is exactly the event that there is no nonroot activation; by the coupling its probability differs from \((1-1/a_n)^{n-2}\) by at most \(2(n-2)/a_n^2\), giving the final limit.

## Verification

Run `python3 checker.py` using only the Python standard library. The script exhaustively computes exact rational probabilities of both unmarked activation-indicator histories and **complete birth-labelled activation histories** for multiple finite orders and attachment parameters. It checks normalization, eligibility, the star-event product and the marked/unmarked total-variation bounds. The finite checks supplement the analytic proof; they neither certify nor enumerate the infinite limit. A captured run is recorded in `checker_output.txt`.

## Relationship to prior work

Angel, Goldschmidt and Michaeli (arXiv:2611.18353v1, 2026) define the same affine outdegree attachment model, but their main theorem concerns random-walk cover times with \(a\) **fixed** as the tree size increases. They do not state a strongly reinforced triangular-array, birth-label-marked Poisson activation law. Seelbach Benkner and Wagner (2022) give fixed-parameter increasing-tree fringe-count results, not a marked activation-history approximation with parameter growing on the tree-size scale. Published work on rare innovations in reinforced random recursive forests obtains Poisson component-size laws under a different copy/innovation construction; those laws do not, from the inspected descriptions, directly identify the joint first-parent activation times and original parent birth labels in this attachment model. The connection nevertheless creates a residual priority risk and merits specialist checking.

## Limitations

The claim concerns first-time *nonroot* parent activations, not the full tree shape, its root-degree deficit, or random-walk cover time. The finite bound is informative in the critical regime \(a_n\asymp n\), not for fixed \(a\). No distributional statement is asserted when \(n/a_n\) diverges. Existing published formulas from other reinforced/recursive models may imply aspects of the limit after reductions not identified in the inspected source material. No independent verification has been performed.

## References

1. O. Angel, C. Goldschmidt and P. Michaeli, *Cover times of random recursive trees and linear preferential attachment trees*, arXiv:2611.18353v1, first public 2026-11-13, https://arxiv.org/html/2611.18353v1.
2. L. Seelbach Benkner and S. Wagner, *Distinct Fringe Subtrees in Random Trees*, Algorithmica 84 (2022), 3686–3728, https://link.springer.com/article/10.1007/s00453-022-01013-y.
3. C. Holmgren and S. Janson, *Fringe trees, Crump–Mode–Jagers branching processes and m-ary search trees*, Probability Surveys 14 (2017), 53–154, https://doi.org/10.1214/16-PS272.
