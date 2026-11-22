# Four habitats are the sharp onset of unequal reliability investment on a path

## Finding

Consider a path of \(n\in\{2,3,4\}\) equally valued habitat patches. For each edge \(i\), a nonnegative restoration investment \(x_i\) gives independent operational probability \(p_i=1-e^{-x_i}\). All patches themselves remain available. Under the exact budget \(\sum_i x_i=B>0\), maximize the expected number of unordered patch pairs connected by operational paths:

\[
\mathcal C_n(x)=\sum_{1\le i<j\le n}\prod_{k=i}^{j-1}(1-e^{-x_k}).
\]

For \(n=2\) the only edge gets the entire budget, and for \(n=3\) the unique global optimum divides it equally between the two edges. **Four patches are the smallest path for which equal investment is not optimal**: for every \(B>0\), the four-patch path has a unique global optimum of the form \((a_B,b_B,a_B)\), with \(0<a_B<b_B\).

Put \(R=e^{-B}\), and let \(u_B\) denote the unique solution in \((\sqrt R,1)\) of

\[
R=\frac{u_B^3(3-u_B)}{2(2-u_B)}.
\]

Then the exact optimal amounts are

\[
a_B=-\log u_B,\qquad b_B=B-2a_B.
\]

The central-edge premium \(\delta(B)=b_B-a_B\) is strictly increasing in \(B\) and satisfies the sharp bounds

\[
0<\delta(B)=\log\frac{2(2-u_B)}{3-u_B}<\log\frac43.
\]

At small and large budgets respectively,

\[
a_B\sim\frac{2B}{7},\quad b_B\sim\frac{3B}{7}\quad(B\downarrow0),
\]

\[
a_B=\frac{B-\log(4/3)}{3}+o(1),\quad b_B=\frac{B+2\log(4/3)}{3}+o(1)\quad(B\to\infty).
\]

All uniqueness and inequalities refer to every feasible nonnegative real allocation, not only symmetric allocations. For the exactly solvable budget \(B=\log(48/5)\), the unique optimum is \((\log 2,\log(12/5),\log2)\) and has \(\mathcal C_4=37/16\).

## Assumptions and scope

The patches are arranged in a simple, unbranched path. Each patch has unit value, every patch remains extant, and a pair is connected precisely when every edge on its unique path operates. Operational edge events are independent, with no common-cause failures. Effort is continuously divisible, costs are equal per unit of \(x_i\), and every edge follows the same exponential response \(1-e^{-x_i}\). The score counts six unordered pairs for four patches, including pairs directly linked by one edge; it is not the probability that the entire path is simultaneously connected. Equivalently, for unit patch weights, maximizing this score maximizes the probability-of-connectivity index and the equivalent-connected-area index up to a fixed positive affine or monotone rescaling.

No statement concerns arbitrary graphs, unequal habitat weights, price heterogeneity, nonlinear ecological responses other than the one specified, stochastic recolonization, or correlated failures.

## Proof

**1. Two and three patches.** For two patches there is one edge and the claim is immediate. For three patches, put \(u=e^{-x_1}\), \(v=e^{-x_2}\), so \(uv=R=e^{-B}\). The sum of the three pair-connectivity probabilities is

\[
(1-u)+(1-v)+(1-u)(1-v)=3-2(u+v)+R.
\]

At fixed product \(uv=R\), AM--GM gives \(u+v\ge2\sqrt R\), with equality only at \(u=v=\sqrt R\), hence the unique optimum is \(x_1=x_2=B/2\).

**2. Equality of the two outer edge investments on the four-patch path.** Write \(u=e^{-x_1}\), \(v=e^{-x_2}\), \(w=e^{-x_3}\). Summing all six pair-connection probabilities and expanding gives

\[
\mathcal C_4=6-3u-4v-3w+2uv+2vw+uw-uvw.
\]

For a fixed central investment \(x_2\) and fixed outer total \(x_1+x_3=B-x_2\), the product \(uw=e^{-(B-x_2)}\) is fixed. Grouping the expression yields

\[
\mathcal C_4=6-4v+uw-uvw-(3-2v)(u+w).
\]

Since \(3-2v\ge1>0\), maximizing \(\mathcal C_4\) is strictly equivalent to minimizing \(u+w\) at fixed product. By AM--GM the unique optimum has \(u=w\), including the degenerate zero-outer-budget case. Therefore **every** global optimizer, not merely some optimizer, is symmetric on the two outer edges.

**3. Exact scalar global maximum.** Let \(x_1=x_3=a\), \(x_2=B-2a\), \(0\le a\le B/2\), set \(u=e^{-a}\in[\sqrt R,1]\), and hence \(v=R/u^2\). Substitution gives

\[
F_R(u)=6-R-6u+u^2+\frac{4R}{u}-\frac{4R}{u^2}.
\]

Differentiation gives

\[
F_R'(u)=\frac{2}{u^3}\left[2R(2-u)-u^3(3-u)\right].
\]

Put \(H(u)=u^3(3-u)/[2(2-u)]\). On \((0,1]\), \(H\) is strictly increasing because

\[
\frac{H'(u)}{H(u)}=\frac3u+\frac{1}{(3-u)(2-u)}>0.
\]

At the left endpoint \(u=\sqrt R\in(0,1)\), the strict inequality \(u(3-u)<2(2-u)\) implies \(H(u)<u^2=R\). At the right endpoint, \(H(1)=1>R\). Thus there is exactly one \(u_B\in(\sqrt R,1)\) with \(H(u_B)=R\), and \(F_R'\) changes sign from positive to negative there. This is the unique scalar global maximum. Step 2 promotes it to the unique global maximum among all three-dimensional allocations, and its interior location ensures \(a_B>0\), \(b_B>0\).

**4. Central premium and sharp endpoints.** Since \(R=H(u_B)\),

\[
b_B-a_B=\log\frac{u_B^3}{R}=\log\frac{2(2-u_B)}{3-u_B}.
\]

For \(0<u_B<1\), the logarithm is strictly between \(0\) and \(\log(4/3)\). Its derivative with respect to \(u_B\) is \(-2/[(4-2u_B)(3-u_B)]<0\). Since \(R=e^{-B}\) decreases strictly with \(B\) and \(H\) increases strictly, \(u_B\) decreases strictly with \(B\), proving that the central premium increases strictly.

As \(B\downarrow0\), \(u_B\to1\). Since \(H'(1)=7/2\), the identity \(H(u_B)=e^{-B}\) implies \(u_B=1-2B/7+O(B^2)\), whence \(a_B=2B/7+O(B^2)\) and \(b_B=3B/7+O(B^2)\). As \(B\to\infty\), \(u_B\to0\), and \(H(u_B)\sim3u_B^3/4\). Thus \(u_B\sim(4R/3)^{1/3}\), giving the stated large-budget expansions. In particular both inequalities for the premium are sharp as limiting bounds.

For the exact example \(u_B=1/2\), substitution into \(H\) gives \(R=5/48\). The three investments are \((\log2,\log(12/5),\log2)\), edge passage probabilities are \((1/2,7/12,1/2)\), and the six path products sum to \(37/16\).

## Verification

The proof above is an analytic, all-budget argument and does not require numerical optimization. Run the included Python 3 standard-library checker from its own extracted directory:

```text
python3 checker.py
```

It independently calculates the six-pair score in two ways, compares the exact optimizer with random feasible allocations over a range of budgets, checks all inequality directions and monotonicity, verifies the three-patch equality property, and tests both asymptotic formulas. The recorded execution completed with `PASS 40071 supplementary assertions`. Finite checks do not establish an infinite assertion; the analytic proof provides the global conclusion.

## Relationship to prior work

The equal-patch all-pairs objective is a specialization of the established probability-of-connectivity / equivalent-connected-area landscape indices. Hamonic, Albert, Couëtoux and Vaxès formulate budgeted ecological connectivity improvement through **discrete sets of corridor upgrades**, not a continuously divisible exponential investment law or the unique four-patch optimizer above. Their earliest located open preprint is arXiv:2109.06622, version 1 released 14 September 2021; the later journal version is DOI 10.1002/net.22131.

Kettelle (1962) analyzes optimal continuously exponential stage reliabilities for a **serial whole-system** availability objective and its sum-of-unavailabilities approximation. That objective is \(\prod_i p_i\) for a serial chain, whereas the present six-pair objective includes individual, two-edge, and three-edge path products with different coefficients. Kettelle's allocation therefore does not imply the strict central premium or minimal four-patch onset. General network reliability allocation and habitat-corridor models motivate the question, but the exact four-path claim was not identified in the inspected sources. This is a statement of investigated coverage, not a claim of comprehensive historical priority.

## Limitations

Uniform link-cost and response assumptions are strong. The score is a surrogate for landscape connectivity, not a population-persistence or conservation-outcome prediction. A path with three edges is the smallest path showing strict unequal investment under this particular objective; this is not a universal lower bound over all networks. Only up to four habitat patches are classified exactly here. Literature search cannot exclude uncatalogued earlier formulations; a 2006 general reliability-allocation paper was available in abstract but not in its complete primary article for comparison.

## References

1. F. Hamonic, C. Albert, B. Couëtoux and Y. Vaxès, *Optimizing the ecological connectivity of landscapes with generalized flow models and preprocessing*, arXiv:2109.06622 (version 1, 2021-09-14), https://arxiv.org/abs/2109.06622. Journal version: *Networks* 81 (2023), 278–293, https://doi.org/10.1002/net.22131.
2. J. D. Kettelle, *Least-Cost Allocations of Reliability Investment*, *Operations Research* 10 (1962), 249–265, https://doi.org/10.1287/opre.10.2.249.
3. J. E. Falk, N. D. Singpurwalla and Y. Y. Vladimirsky, *Reliability Allocation for Networks and Systems*, *SIAM Review* 48 (2006), 43–65, https://doi.org/10.1137/S0036144503434493 (abstract inspected; full article not read).
