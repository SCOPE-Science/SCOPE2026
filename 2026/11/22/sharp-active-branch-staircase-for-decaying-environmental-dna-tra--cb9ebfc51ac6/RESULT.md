# Sharp active-branch staircase for decaying environmental-DNA transport

## Finding

**Theorem.** Let \(n\ge 2\) be an integer, \(a>0\), and let \(p=(p_1,\ldots,p_n)\) range over all nonnegative flow shares satisfying \(\sum_{i=1}^{n}p_i=1\). Define the dimensionless downstream recovered-flux factor

\[
F_a(p)=\sum_{i:p_i>0}\exp(-a/p_i),
\]

where a zero-flow branch has zero downstream contribution. Then

\[
\max_{p_i\ge0,\,\sum p_i=1}F_a(p)=\max_{1\le k\le n}\bigl(k\exp(-ak)\bigr).
\]

**All** global optimizers have precisely \(k\) positive components, each exactly \(1/k\), and the other components zero, where \(k\) maximizes the displayed expression; conversely every such allocation is optimal. The sharp switching parameters are

\[
a_j=\log\frac{j+1}{j},\qquad 1\le j<n.
\]

For \(0<a<a_{n-1}\), all \(n\) branches are active. As \(a\) increases, the optimal active count decreases consecutively through every integer to one, with the transition from \(j+1\) to \(j\) precisely at \(a=a_j\). At each threshold, **only** the adjacent support sizes \(j\) and \(j+1\) tie; there are no other optimal allocations. In particular, for three channels the two transitions are \(a=\log(3/2)\) and \(a=\log 2\).

## Assumptions and scope

Consider \(n\) geometrically identical, independent parallel flumes or controlled river-like reaches converging into a perfectly mixed outlet, each of length \(\ell>0\) and constant wetted cross section \(A_c>0\). The controlled total discharge is \(Q>0\), and channel \(i\) receives discharge \(Qp_i\). In an active channel the mean velocity is \(v_i=Qp_i/A_c\). An upstream inlet delivers a *flow-independent* tracer/eDNA mass flux \(S>0\) in every active channel. Tracer transport is purely advective with common first-order decay rate \(\lambda>0\), and there is no internal exchange or additional input; inactive branches deliver no tracer to the outlet. No biological claim is made about the fate of input material in an inactive branch.

Travel time is \(\ell/v_i\), and recovered outlet mass flux from channel \(i\) is \(S\exp[-\lambda\ell/v_i]\). Taking \(a=\lambda\ell A_c/Q\) yields the theorem's objective. As the downstream mixed discharge is fixed at \(Q\), maximizing its tracer concentration \((S/Q)F_a(p)\) is equivalent to maximizing recovered mass flux. This is a *counterfactual flow-control model*, not a proposed redistribution of water among natural tributaries, whose morphology, biological shedding, and discharge-dependent width/depth need not satisfy these hypotheses.

## Proof

**Step 1: Exact two-branch optimizer.** For any \(b>0\), define \(g_b(0)=0\), \(g_b(x)=\exp(-b/x)\) for \(x>0\), and \(G_b(x)=g_b(x)+g_b(1-x)\). We prove that its global maxima on \([0,1]\) occur **only** at \(x=0,1/2,1\). Symmetry lets us examine \(0<x<1/2\). Put \(u=\log((1-x)/x)>0\). Direct differentiation gives

\[
\operatorname{sgn}G_b'(x)=\operatorname{sgn}\left(\frac{u}{\sinh u}-b\right).
\]

Indeed the ratio of the two positive derivative summands is \(\exp[2(u-b\sinh u)]\). The function \(u/\sinh u\) is strictly decreasing on \((0,\infty)\): its derivative has the sign of \(\sinh u-u\cosh u<0\), since \(u\cosh u-\sinh u\) vanishes at zero and has derivative \(u\sinh u>0\). Its limits are \(1\) at zero and \(0\) at infinity. For \(0<b<1\), \(G_b'\) changes from negative to positive exactly once on \((0,1/2)\), giving only a strict local minimum there; for \(b\ge1\), it stays negative there. By reflection there are no noncentral interior maxima. The only candidates are endpoints, with value \(e^{-b}\), and the center, with value \(2e^{-2b}\). Thus a pair is optimized only by equal splitting, by completely concentrating the flow, or by both at \(b=\log2\).

**Step 2: Every global optimum has equal active flows.** The simplex is compact and \(g_a\) is continuous at zero, so a maximizer exists. Suppose two active components of a maximizing vector are unequal, with sum \(t>0\). Holding every other component fixed, write this pair as \((tx,t(1-x))\) with \(0<x<1\), \(x\ne1/2\). Its contribution is \(G_{a/t}(x)\), strictly below the pair maximum by Step 1, which contradicts global optimality. Consequently all positive shares are identical: if there are \(k\), each is \(1/k\). Conversely every such vector is feasible.

**Step 3: Sharp phase staircase and all equality cases.** The value for an equal positive \(k\)-support is \(V_k(a)=ke^{-ak}\), and

\[
\frac{V_{k+1}(a)}{V_k(a)}=\frac{k+1}{k}e^{-a}.
\]

This is greater than, equal to, or less than one as \(a\) is below, equal to, or above \(a_k=\log((k+1)/k)\). The numbers \(a_1>a_2>\cdots>a_{n-1}>0\) decrease strictly, hence the \(V_k\) increase then decrease as \(k\) grows, with a unique largest index except for a single adjacent tie at a threshold. Steps 1–2 exclude every other optimizer, proving all claims and sharpness for every \(n\ge2\).

## Verification

The self-contained Python 3 script `verify.py` uses only the standard library; execute `python3 verify.py` from a directory containing the extracted script. It checks algebraic candidate relations and all adjacent ties, directly tests the curvature formula and the strict monotonicity entering Step 1, and performs dense finite-grid plus reproducible randomized tests over various support sizes and decay parameters. The observed run completed 141230 assertions. These finite checks are consistency diagnostics and are **not** a substitute for Steps 1–3, which prove the statement for every real \(a>0\) and all integer \(n\ge2\).

## Relationship to prior work

Carraro, Blackman and Altermatt (2023), in their eDITH formulation (Methods, equation (1)), relate river eDNA concentration to source flux, flow dilution and exponential attenuation determined by path travel time; this supplies the motivating transport structure. Carraro, Stauffer and Altermatt (2020) analyze **optimal sampling-location design** in river networks with modeled discharge, rather than a controlled allocation of total discharge among identical channels. Udell and Boyd (2014) establish the general nonlinear optimization context for separable sigmoidal utilities and algorithmic bounds; the general framework covers this optimization *form* but does not itself state the exact all-size equal-support classification and logarithmic critical values shown here. The theorem is an explicit specialization with a stronger structural conclusion, not an assertion that sigmoidal optimization itself is new. Earlier resource-allocation theory may contain equivalent results; historical priority has not been independently established.

## Limitations

The assumptions of identical geometric reaches, fixed total discharge, unchanged cross sections, equal inlet mass flux per active branch, constant first-order decay, and complete outlet mixing are essential. Fixed upstream **concentration** instead of fixed tracer-source flux yields a different objective. Natural river cross section, flow velocity, shedding, hydrological connectivity, temperature, deposition/resuspension and sampling sensitivity often vary with flow; a zero-flow reach may not be operationally attainable. This result is a precisely defined laboratory benchmark only, not a field-management prescription or a prediction of taxon presence. The statement concerns the mathematical maximizers of a static model, not dynamic stability or adaptive routing.

## References

- Carraro, L., Blackman, R. C. and Altermatt, F. (2023), “Modelling environmental DNA transport in rivers reveals highly resolved spatio-temporal biodiversity patterns,” *Scientific Reports* 13:8854, published 31 May 2023. DOI: https://doi.org/10.1038/s41598-023-35614-6; open full-text copy https://www.nature.com/articles/s41598-023-35614-6.pdf.
- Carraro, L., Stauffer, J. B. and Altermatt, F. (2020), “How to design optimal eDNA sampling strategies for biomonitoring in river networks,” *Environmental DNA*, first published 20 September 2020, DOI: https://doi.org/10.1002/edn3.137.
- Udell, M. and Boyd, S. (2014), “Maximizing a Sum of Sigmoids,” https://web.stanford.edu/~boyd/papers/pdf/max_sum_sigmoids.pdf.
- Vicentini, A. (1970), “On the Resource Allocation Problem with S-Shaped Utility Functions,” record https://commons.case.edu/wsom-ops-reports/370/; full text not inspected in this review.
