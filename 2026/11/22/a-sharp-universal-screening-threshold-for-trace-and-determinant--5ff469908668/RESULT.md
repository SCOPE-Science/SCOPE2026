# A sharp universal screening threshold for trace- and determinant-optimal Nyström landmarks on paths

## Finding

Let \(P_n\) be the unit-conductance path with \(n\ge3\) vertices and let
\[
 A_\mu=\mu I+L(P_n),\qquad K_\mu=A_\mu^{-1},\qquad\mu>0.
\]
For a set \(S\subseteq\{1,\dots,n\}\) of exactly \(k\) noiseless landmarks, define
\[
 \widetilde K(S)=K_{:,S}K_{S,S}^{-1}K_{S,:},\quad
 E_\mu(S)=\operatorname{tr}(K_\mu-\widetilde K(S)),\quad
 D_\mu(S)=\det (K_\mu)_{S,S}.
\]
For every \(2\le k\le n\), the **complete set of maximizers** of \(D_\mu\), for every \(\mu>0\), consists of exactly those landmark sets containing both endpoints whose \(k-1\) interior gaps of unselected vertices differ in length by at most one.

For every \(\mu\ge\tfrac12\) and every \(2\le k\le n\), these are **also precisely all minimizers** of the Nyström trace error \(E_\mu\). The boundary is sharp uniformly over path lengths and budgets: for each \(0<\mu<\tfrac12\), some finite path (already with \(k=2\)) has strictly smaller trace error with a non-endpoint set than with the determinant-optimal endpoint pair.

More explicitly, write \(n-k=(k-1)q+r\), where \(0\le r<k-1\). Each jointly optimal set has \(r\) interior gaps of length \(q+1\) and the others of length \(q\); there are exactly \(\binom{k-1}{r}\) such sets. If \(F_0=1\), \(F_1=\mu+2\), and \(F_j=(\mu+2)F_{j-1}-F_{j-2}\), then in the joint-optimal region
\[
 E_\mu^*=r\frac{F_{q+1}'}{F_{q+1}}+(k-1-r)\frac{F_q'}{F_q},\qquad
 D_\mu^*=\frac{F_{q+1}^{r}F_q^{k-1-r}}{\det A_\mu}.
\]
Here prime denotes differentiation with respect to \(\mu\), and the empty complement at \(k=n\) has zero trace error.

## Assumptions and scope

All edges of \(P_n\) have conductance exactly one. The screening parameter \(\mu\) is strictly positive and is uniform at every vertex; the path Laplacian has free (degree-one) endpoints. Landmark observations are noiseless; every size-\(k\) subset is allowed. The trace objective is the nuclear-norm residual of the positive-semidefinite Nyström approximation, while the determinant objective measures the generalized variance (or Gaussian differential entropy) of the selected covariance principal minor. The two objectives are optimized separately over the same feasible subsets.

When \(k\ge2\), enumerate \(S=\{s_1<\cdots<s_k\}\). Define endpoint-tail lengths \(a=s_1-1\) and \(b=n-s_k\), and interior gap lengths \(\ell_j=s_{j+1}-s_j-1\), \(1\le j<k\). These are nonnegative integers satisfying \(a+b+\sum_j\ell_j=n-k\).

## Proof

**Step 1: Exact conditional block decomposition.** Put \(U=\{1,\ldots,n\}\setminus S\). The Schur complement of \(K_{S,S}\) in \(K=A_\mu^{-1}\) is \((A_{U,U})^{-1}\). Thus
\[
 E_\mu(S)=\operatorname{tr}(A_{U,U}^{-1}),\qquad
 D_\mu(S)=\frac{\det A_{U,U}}{\det A_\mu}
\]
by the complementary-minor determinant identity. The principal precision block \(A_{U,U}\) is the direct sum of two tails, whose exposed path endpoint has diagonal \(\mu+1\), and \(k-1\) interior blocks with diagonal \(\mu+2\) throughout; all nonzero off-diagonals are \(-1\).

Write \(F_j\) for the determinant of an interior block of length \(j\) (with \(F_0=1\)) and \(H_j\) for a tail determinant (with \(H_0=1\)). Set \(\theta=\operatorname{arcosh}(1+\mu/2)>0\) and \(c=1/\sqrt{\mu(\mu+4)}\). The continuant recurrence gives
\[
 F_j=\frac{\sinh((j+1)\theta)}{\sinh\theta},\qquad
 H_j=\frac{\cosh((j+\tfrac12)\theta)}{\cosh(\theta/2)}.
\]
The trace of an inverse block equals the derivative of the logarithm of its determinant. Define \(f(j)=F_j'/F_j\) and \(g(j)=H_j'/H_j\). Therefore
\[
 E_\mu(S)=g(a)+g(b)+\sum_{j=1}^{k-1}f(\ell_j),\qquad
 (\det A_\mu)D_\mu(S)=H_aH_b\prod_{j=1}^{k-1}F_{\ell_j}.
\]
In particular,
\[
 f(j)=c\big[(j+1)\coth((j+1)\theta)-\coth\theta\big],
\]
\[
 g(j)=c\big[(j+\tfrac12)\tanh((j+\tfrac12)\theta)-\tfrac12\tanh(\theta/2)\big].
\]

**Step 2: Determinant-optimal tails are empty at every screening strength.** For all integers \(a\ge1\), \(j\ge0\),
\[
 \frac{H_a}{H_{a-1}}<e^\theta<\frac{F_{j+1}}{F_j}.
\]
Both inequalities are immediate by writing \(\cosh x\) and \(\sinh x\) in exponential form. If the left tail is nonempty, move the leftmost landmark one vertex left: its tail decreases by one and the adjacent interior gap increases by one. The determinant strictly increases. Similarly remove the right tail. Hence every determinant maximizer contains both endpoints. Since \(x\mapsto\log\sinh(x\theta)\) is strictly concave for positive \(x\), the product of the interior continuants is strictly increased by balancing any two gap sizes differing by two or more. Conversely, every balanced profile has the same maximal product. This gives the entire determinant optimizer set and its count.

**Step 3: Trace-optimal tails are empty for \(\mu\ge\tfrac12\).** For every integer \(j\ge1\), the interior increment obeys
\[
 f(j)-f(j-1)<c.
\]
Indeed, its difference from \(c\) is twice \(c\) times the difference between consecutive values of the strictly decreasing function \(x/(e^{2\theta x}-1)\).

If \(\mu\ge\tfrac12\), then \(t=e^\theta\ge2\). For every integer \(a\ge1\),
\[
 g(a)-g(a-1)-c
 =2c\left(\frac{a-\tfrac12}{t^{2a-1}+1}-\frac{a+\tfrac12}{t^{2a+1}+1}\right)\ge0.
\]
After clearing the positive denominator, the sign assertion is precisely
\[
 t^{2a-1}\big[(a-\tfrac12)(t^2-1)-1\big]\ge1.
\]
For \(t\ge2\) it is equality only when \(a=1,t=2\) and is otherwise strict: at \(t=2,a=1\) both sides equal one, while for \(a\ge2\) the left side exceeds one and increases with \(t\). Thus shifting one vertex from any endpoint tail into the adjacent interior gap **strictly decreases** the trace error. All trace minimizers consequently contain both endpoints.

For interior gaps, the function \(x\mapsto x\coth(x\theta)\) has positive second derivative for \(x>0\):
\[
 \frac{d^2}{dx^2}[x\coth(\theta x)]
 =2\theta\,\operatorname{csch}^2(\theta x)
 [\theta x\coth(\theta x)-1]>0.
\]
The inequality \(z\coth z>1\) holds for every \(z>0\). Therefore \(f(j)\) is strictly discretely convex: transferring a vertex from a gap at least two larger than another strictly lowers the total error. Balanced interior gaps are precisely all trace minimizers, completing the agreement theorem and exact formulas.

**Step 4: Sharpness below the universal threshold.** For \(0<\mu<\tfrac12\), one has
\[
 g(1)=\frac1{\mu+1}<c,
 \qquad \lim_{j\to\infty}[f(j)-f(j-1)]=c.
\]
Choose \(n\) sufficiently large that \(f(n-2)-f(n-3)>g(1)\). The determinant optimizer for two landmarks is \(S=\{1,n\}\), with trace error \(f(n-2)\); the legal competitor \(S'=\{2,n\}\) has error \(g(1)+f(n-3)<f(n-2)\). Thus the determinant optimum cannot be trace optimal. No claim is made that \(S'\) is globally trace optimal for every such \(n\).

For an exact small witness, at \(n=6\), \(k=2\), and \(\mu=1/4\), the determinant optimizer is \(\{1,6\}\), while the unique trace minimizer is \(\{2,5\}\). Their trace errors are respectively \(8208/2929\) and \(176/65\), differing by \(18016/190385>0\).

## Verification

Run the accompanying standalone Python 3 script with `python verify_path_design.py`. It uses only the standard library and exact rational arithmetic. It directly checks the complementary-minor and Schur-complement identities for small path matrices, exhaustively compares all landmark subsets for \(3\le n\le11\) and several rational screening strengths, verifies all equality cases in the claimed regime, and checks the six-vertex exact counterexample. This finite verification does not certify the general theorem by enumeration; the proof above establishes all orders and real screening parameters.

## Relationship to prior work

Belabbas and Wolfe, *On Landmark Selection and Sampling in High-Dimensional Data Analysis* (public preprint 24 June 2009), define the Nyström subset-selection objective and give its general trace-residual characterization. They do not classify screened-path kernel optimizers or identify the sharp screening boundary derived here.

The 2010 Kriging-design study of Baldi Antognini and Zagoraiou is a particularly relevant comparison because it optimizes prediction and information gain for the one-dimensional stationary exponential-correlation model. That model has a different boundary precision from \(A_\mu\): with \(e^{-\theta}\) denoting the correlation between neighbors, its suitably rescaled endpoint diagonal is \(e^\theta\), rather than the Neumann value \(2\cosh\theta-1\), although its interior diagonal and off-diagonals can match. Hence its equispacing results do not automatically imply the present sharp boundary-dependent trace-versus-determinant statement. The complete 2010 text could not be obtained for a definitive comparison; its abstract and subsequent citations were examined.

Mukherjee’s 2001 thesis on optimal sampling of product-covariance processes provides general necessary-and-sufficient conditions for integrated mean-square path prediction, potentially relevant to this Green kernel. Its publicly accessible abstract does not specify a universal screened-Neumann threshold, and its gated complete text was not inspected. Such general criteria may offer another route to the present classification; their exact implication relationship remains a priority risk.

Related designs on cycles have no free-end tails, so their joint balancing optimality has no screening transition. This distinction also separates the result from earlier one-landmark half-line trace-gain thresholds: the present statement classifies *all* budgets of at least two on finite paths and simultaneously addresses determinant selection.

## Limitations

The exact universal threshold concerns *agreement of complete optimizer sets across every finite path and every budget at least two*. It does **not** classify every trace-optimal subset below \(\mu=1/2\), establish the first finite-size transition for each budget, cover singleton budgets, permit unequal vertex screening or edge weights, or treat noisy landmark measurements. It does not imply practical superiority of Nyström to direct tridiagonal solvers. Originality remains contingent on fuller comparisons with specialized spatial-design literature, particularly inaccessible complete versions of the 2001 product-covariance dissertation and the 2010 Kriging paper. No independent mathematical validation has been performed.

## References

1. M.-A. Belabbas and P. J. Wolfe, *On Landmark Selection and Sampling in High-Dimensional Data Analysis*, arXiv:0906.4582v1, first submitted 24 June 2009, https://arxiv.org/html/0906.4582v1 ; see Sections 3.2 and 4.1.
2. A. Baldi Antognini and M. Zagoraiou, *Exact Optimal Designs for Computer Experiments via Kriging Metamodelling*, Journal of Statistical Planning and Inference 140 (2010), 2607–2617, https://doi.org/10.1016/j.jspi.2010.03.027 (abstract and secondary descriptions inspected; full text not available).
3. B. Mukherjee, *Optimal Designs for Estimating the Path of a Stochastic Process*, Purdue University dissertation (2001), https://docs.lib.purdue.edu/dissertations/AAI3043760/ (abstract inspected; complete text access restricted).
4. K. Sikolya and S. Baran, *On the Optimal Designs for the Prediction of Complex Ornstein–Uhlenbeck Processes*, Communications in Statistics—Theory and Methods (2019), https://doi.org/10.1080/03610926.2019.1645855 (Sections 1, 4, 6 inspected for the different correlation/entropy design setting).
