# One activation window for a specialist pest detector: a sharp three-pest example

## Finding

In a fixed-budget, two-device Poisson surveillance model, **a detector specialized for exactly one pest can be optimal at positive effort only on a single interval of total budgets**, irrespective of the number of other pests. The interval may be empty, all positive budgets, one-sided, or strictly bounded. In particular, the specialized detector can be unused at small budgets, used at intermediate budgets, and abandoned again at large budgets. Three target pests are the sharp minimum for that two-transition pattern.

More precisely, for \(m\ge2\) pest species, a general detector G has known positive per-effort detection rates \(b_1,\ldots,b_m\) and a specialized detector S has positive rate \(a\) only for one target \(s\), with zero rate for every other pest. Let each pest have a positive missed-detection weight \(w_i\). If \(B>0\) is a common-cost, continuously divisible total surveillance budget and \(x\in[0,B]\) is allocated to S, expected weighted misses are

\[
L_B(x)=\sum_{i\ne s}w_i e^{-b_i(B-x)}+w_s e^{-b_s(B-x)-ax}.
\]

The minimizing \(x_B\) is unique. If \(a\le b_s\), then \(x_B=0\) for all \(B>0\). If \(a>b_s\), define

\[
H(B)=\sum_{i\ne s}w_i b_i e^{-(b_i-b_s)B}-w_s(a-b_s).
\]

Then exactly \(x_B>0\) when \(H(B)<0\). The positive-effort budget set \(\{B>0:x_B>0\}\) is an interval, and its membership changes at most twice. There cannot be two changes for \(m\le2\).

For the exact three-pest witness

\[
(b_1,b_2,b_3)=(2,3,4),\quad s=2,\quad a=4,\quad (w_1,w_2,w_3)=(1/2,8,2),
\]

we have \(H(B)=e^B-8+8e^{-B}\). There are precisely two positive switching budgets,

\[
B_- =\log(4-2\sqrt2)=0.158347183820\ldots,
\qquad
B_+=\log(4+2\sqrt2)=1.921094357859\ldots.
\]

The unique optimum is \(x_B=0\) for \(0<B\le B_-\) and \(B\ge B_+\), and satisfies \(0<x_B<B\) for \(B_-<B<B_+\). The specialized detector thus enters and later exits an optimal **mixed** program, despite all pest weights and capture rates remaining fixed.

## Assumptions and scope

Each pest is taken as present when calculating its conditional detection failure. Surveillance encounters for species \(i\) follow a Poisson process with exposure mean equal to its linear combination of efforts; therefore its nondetection probability is the exponential shown above. The weights \(w_i>0\) may combine pest prevalence and consequences of a missed introduction, but are fixed with the budget. Only the *expected weighted count of missed detections* is optimized; no claim is made about a fully time-dependent eradication-cost objective.

The two instruments have equal per-unit effort costs, no minimum setup requirement, calibrated constant rates, no interactions, and perfectly divisible effort. The general detector responds to all \(m\) species (\(b_i>0\)); the specialized detector responds only to species \(s\). The target's specialized rate \(a>0\) is finite. The theorem holds for every real \(B>0\), every integer \(m\ge2\), and all positive rates and weights satisfying these conditions.

## Proof

**1. Strictly convex optimization.** Differentiation gives

\[
L'_B(x)=\sum_{i\ne s}w_i b_i e^{-b_i(B-x)}
+w_s(b_s-a)e^{-b_sB-(a-b_s)x}
\]

and

\[
L''_B(x)=\sum_{i\ne s}w_i b_i^2e^{-b_i(B-x)}
+w_s(a-b_s)^2e^{-b_sB-(a-b_s)x}>0,
\]

because \(m\ge2\), each nonspecialist \(b_i>0\), and every \(w_i>0\). Thus the minimizer on \([0,B]\) is unique. Strict convexity shows \(x_B>0\) if and only if \(L'_B(0)<0\); when equality holds, the unique minimizer is the boundary \(x_B=0\). If \(a\le b_s\), every term in \(L'_B(x)\) is nonnegative and the nonspecialist terms are strictly positive, so \(x_B=0\).

**2. Connected activation budgets.** Now assume \(a>b_s\). An exact rearrangement gives \(L'_B(0)=e^{-b_sB}H(B)\). Also

\[
H''(B)=\sum_{i\ne s}w_i b_i(b_i-b_s)^2e^{-(b_i-b_s)B}\ge0.
\]

If some nonspecialist has \(b_i\ne b_s\), this is strictly positive at every \(B\), so \(H\) is strictly convex. Consequently the strict negative sublevel set of \(H\) is an interval and there are at most two distinct zeros. If every nonspecialist rate equals \(b_s\), \(H\) is constant, and the negative sublevel set is either empty or all positive budgets. These cases prove the interval and two-transition assertions without a generic-position assumption or an appeal to finite sampling of \(B\).

**3. Two-pest obstruction.** For \(m=2\), there is exactly one nonspecialist rate. Therefore \(H(B)=c e^{-dB}-k\) for constants \(c,k>0\) and real \(d\). This is monotone or constant on \((0,\infty)\). Its negative set cannot have two distinct finite boundary points. For one pest, an optimal choice between two fixed positive rates also cannot switch twice. Hence at least three pests are needed.

**4. Three-pest attainment and mixedness.** In the displayed example, \(L'_B(0)=e^{-2B}-8e^{-3B}+8e^{-4B}\), so \(H(B)=e^B-8+8e^{-B}\). Setting \(y=e^B>1\), the zero equation becomes \(y^2-8y+8=0\), whose roots \(4\pm2\sqrt2\) are both greater than one. Since \(H(0)=1>0\) and \(H\) is strictly convex, \(H<0\) exactly between the two roots. At the other endpoint of the allocation interval,

\[
L'_B(B)=9-8e^{-4B}>0
\quad(B>0).
\]

Thus in the activation window the derivative starts negative and ends positive, and strict convexity places the unique minimizer strictly between \(0\) and \(B\). Outside this window the unique minimizer is \(x_B=0\). This proves all inclusions, equalities, and sharpness claims.

## Verification

The standalone Python 3 script `checks/verify_specialist_window.py` computes the exact three-term coefficients using rational arithmetic, checks strict signs of the quadratic at rational values, verifies the two analytic switching budgets numerically, and independently solves the strictly convex allocation problem by derivative bisection. It also checks the first-order boundary test and global objective comparisons on randomized positive-rate multi-pest cases. Running the script without external dependencies produced 32,550 supplementary assertions and reported specialist allocations \(0\), approximately \(0.084712904316\), and \(0\) at budgets \(0.1\), \(1\), and \(3\), respectively.

These finite checks support implementation and the example; the unbounded-budget interval theorem and the three-pest minimality follow from the analytic proof, not from finite enumeration.

## Relationship to prior work

Nguyen et al. (2024) formulate multi-pest, multi-trap invasive-species surveillance, including generalized and specialized detectors (their Section “Multipest–Multitrap Design and Detection Probability,” particularly Equation 10), and optimize a broader discounted expected-cost model numerically. Their study motivates treating a specialized device as responding to only some pests, but does not state the one-interval activation theorem or sharp three-pest two-transition witness for the distinct fixed-budget weighted-miss objective here. Its more general ecological setting does **not** by itself establish a stronger optimization theorem for the constrained model specified above.

Moore and McCarthy (2016) use exponential Poisson nondetection and optimize surveillance effort over sites and times, not continuous allocation between a general detector and a single-target specialist. Kompas et al. (2019) analyze biosecurity budgets across different interventions; the publicly accessible abstract was examined, but its full article was not inspected here. Classical calculus and convex sublevel-set arguments are part of the proof and are not claimed as novel mathematics in isolation. The contribution is the exact specialist-use classification and sharp biologically interpretable minimal witness under the stated model. No empirical superiority or established historical firstness is asserted.

## Limitations

The two-transition claim concerns a fixed total budget varied across alternative plans, not time evolution within a single campaign. It does not carry over automatically to multiple specialized targets, setup charges, integer trap counts, stochastic and adaptive detection rates, interactions, correlated detection processes, or alternate nonlinear loss functions. Positive weights are known rather than estimated; the strict interval statement is an idealized structural result. Near a transition the benefit of the specialist can be arbitrarily small; the particular witness has a modest interior gain. The work is not field-calibrated and has not received an independent audit. Some older broad allocation literature was only available at abstract level; an undiscovered equivalent formulation remains possible.

## References

1. Nguyen, H.-T.-M., et al. (2024), “Optimal allocation of resources among general and species-specific tools for plant pest biosecurity surveillance,” *Ecological Applications*, e2955. First published 20 February 2024. https://doi.org/10.1002/eap.2955
2. Moore, A. L. and McCarthy, M. A. (2016), “Optimizing ecological survey effort over space and time,” *Methods in Ecology and Evolution* 7, 891–899. https://doi.org/10.1111/2041-210X.12564
3. Kompas, T., Chu, L., Van Ha, P. and Spring, D. (2019), “Budgeting and portfolio allocation for biosecurity measures,” *Australian Journal of Agricultural and Resource Economics* 63, 412–438. https://doi.org/10.1111/1467-8489.12305
