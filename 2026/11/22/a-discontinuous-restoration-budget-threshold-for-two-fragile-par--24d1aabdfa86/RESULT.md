# A discontinuous restoration-budget threshold for two fragile parallel ecological corridors

## Finding

Consider two disjoint, two-link ecological corridors connecting permanently viable terminal habitats, each using its own independently viable intermediate habitat. Intermediate viability is \(s\in(0,1)\); investing nonnegative effort \(x\) in an edge independently makes that link operable with probability \(1-e^{-x}\). The total edge-investment budget is \(B>0\). Successful connectivity means at least one complete route is operable.

**Exact global allocation theorem.** Define
\[
B_c(s)=4\log\!\left(1+\sqrt{\frac{2}{1-s}}\right).
\]
Write the four edge efforts in route order as \((x_1,x_2,y_1,y_2)\), with nonnegative entries summing to \(B\). Every global maximizer of the probability of terminal connectivity is precisely one of the following:

- If \(0<B<B_c(s)\), the two optimal vectors are \((B/2,B/2,0,0)\) and \((0,0,B/2,B/2)\).
- If \(B=B_c(s)\), those two vectors and \((B/4,B/4,B/4,B/4)\) are the **only** three optimal vectors.
- If \(B>B_c(s)\), \((B/4,B/4,B/4,B/4)\) is the **unique** optimal vector.

No unequal positive allocation across the two routes is globally optimal, including at the threshold. Therefore the preferred allocation jumps directly from fully concentrating investment on one path to a symmetric four-link investment. In particular, the diversification transition is discontinuous in the optimal decision, not a continuous activation of the backup route. At \(s=1/2\), the threshold is \(B_c=4\log3\); at the threshold all three stated plans achieve exactly \(32/81\) connectivity probability.

**Sharp topological comparator.** If each of the two independent parallel paths instead requires just **one** investable link and independently survives its own intermediate gate with the same probability \(s\in(0,1)\), the unique optimum at every \(B>0\) invests \(B/2\) in each path. Thus a pair of serial investable links per route is the smallest common path length producing the stated concentration-to-diversification transition within this identical two-route family.

## Assumptions and scope

The graph has terminals \(a,z\), two distinct intermediate vertices \(v_1,v_2\), and edges \(a v_1, v_1 z, a v_2, v_2 z\). Terminals never fail. Intermediate viability indicators are mutually independent Bernoulli variables with probability \(s\), and are independent of the four Bernoulli edge-operability indicators. The edge-operability probability of an edge receiving effort \(x\ge0\) is exactly \(1-e^{-x}\). Neither site viability nor the edge-effort response is learned or updated by field observations. All efficiencies and unit effort prices are equal. The objective is a single static, unconditional probability that some complete source-to-destination path exists, not expected extinction time, electric resistance, long-run flow, or spectral metapopulation capacity.

The theorem quantifies over all \(s\in(0,1)\), all \(B>0\), and every nonnegative effort vector with sum exactly \(B\); no symmetric or equal-within-route allocation is assumed in advance. At \(s=1\), concentration remains optimal at every finite positive budget and the stated finite transition disappears. At \(s=0\), every allocation has zero success probability, so it is excluded.

## Proof

**1. Equalize investment inside each occupied route.** For a fixed route budget \(b=x_1+x_2\), the conditional two-edge path survival is
\[
(1-e^{-x_1})(1-e^{-x_2})
=1-e^{-x_1}-e^{-x_2}+e^{-b}.
\]
The arithmetic-geometric mean inequality gives \(e^{-x_1}+e^{-x_2}\ge2e^{-b/2}\), with equality only when \(x_1=x_2=b/2\). Multiplying by the positive viability factor \(s\), and noting that overall success is strictly increasing in either individual route-success probability unless it is already one (which never occurs for finite \(B\) and \(s<1\)), every global optimizer must equalize positive effort within each route. Zero-budget routes already have both edges at zero.

Thus, for \(b\in[0,B]\), put
\[
q_s(b)=s(1-e^{-b/2})^2,
\qquad R_s(b)=1-[1-q_s(b)][1-q_s(B-b)].\tag{1}
\]
The original four-dimensional problem is exactly equivalent to maximizing \(R_s(b)\) over the closed interval.

**2. Exclude all asymmetric interior maxima.** Since \(0\le q_s(b)<1\), define \(h_s(b)=-\log[1-q_s(b)]\). Then \(R_s(b)=1-e^{-H_s(b)}\), where \(H_s(b)=h_s(b)+h_s(B-b)\); maximizing either expression is equivalent. With \(u=e^{-b/2}\) and \(v=e^{-(B-b)/2}\), elementary differentiation gives
\[
h_s'(b)=\frac{s u(1-u)}{1-s(1-u)^2},
\]
\[
H_s'(b)=-\frac{s(u-v)\left[(1-s)(u+v-1)+suv\right]}
{[1-s(1-u)^2][1-s(1-v)^2]}.\tag{2}
\]
For \(0<b<B/2\), \(u>v>0\), and \(uv=e^{-B/2}\) is fixed. The sum \(u+v\) strictly decreases throughout this half-interval, because \((u+v)'=(v-u)/2<0\). The bracket
\[
K(b)=(1-s)(u+v-1)+s e^{-B/2}
\]
is therefore strictly decreasing. At \(b=0\) its value is \(e^{-B/2}>0\). Equation (2) shows that \(H_s'\) is initially negative and can only change sign from negative to positive on \((0,B/2)\), never in the opposite direction. Consequently, \(H_s\) cannot have any local maximum in that open half-interval; any interior critical point is a strict minimum. By reflection \(H_s(b)=H_s(B-b)\), every global maximizer of \(H_s\) is among \(b=0,B/2,B\), and every other point is strictly inferior to the larger of those candidate values. The same argument also covers the case where \(K\) does not cross zero.

**3. Compare the only candidates.** Set \(x=e^{-B/4}\in(0,1)\). Concentration gives \(R_C=s(1-x^2)^2\); a split between the two equalized routes gives \(R_E=1-[1-s(1-x)^2]^2\). Exact expansion yields
\[
R_E-R_C=s(1-x)^2\bigl[(1-s)(1-2x)-(1+s)x^2\bigr].\tag{3}
\]
The bracket \(G_s(x)=(1-s)(1-2x)-(1+s)x^2\) is strictly decreasing for \(x\ge0\); moreover \(G_s(0)=1-s>0\) and \(G_s(1)=-2<0\). Its sole positive root is
\[
x_c=\frac{\sqrt{1-s}}{\sqrt2+\sqrt{1-s}}=\frac{1}{1+\sqrt{2/(1-s)}}.\tag{4}
\]
As \(B\) increases, \(x=e^{-B/4}\) decreases strictly. Equations (3)–(4) show that concentration wins below \(B_c=-4\log x_c\), equal splitting wins above, and the two tie exactly at the indicated critical budget. The strict exclusion of all other \(b\) in step 2 proves the complete optimizer and tie classification, with no missing asymmetric cases. At \(s=1/2\), \(x_c=1/3\), and both candidates equal \(\frac12(1-1/9)^2=32/81\).

**4. Shortest-route contrast.** In the one-edge-per-route comparator, put \(q_1(b)=s(1-e^{-b})\) and \(h_1(b)=-\log(1-q_1(b))\). Direct differentiation gives
\[
h_1''(b)=-\frac{s(1-s)e^{-b}}{(1-s+s e^{-b})^2}<0.
\]
Thus \(h_1(b)+h_1(B-b)\) is strictly concave and symmetric, so its sole maximizer is \(b=B/2\). For \(s=1\), the bracket in (3) is strictly negative for every \(x>0\), proving concentration at all finite budgets. \(\square\)

## Verification

The standalone `verify.py` reproduces the exact symbolic identities in (2), (3) and (4), the rational critical example, and over 200,000 supplementary assertions at varied viability rates and budgets. It additionally tests arbitrary within-route splits and the one-edge-per-route comparator. Run `python verify.py` using Python 3.10+ and SymPy. Those finite tests confirm identities and sampled inequalities, but the proof's continuous-domain conclusions come from exact factorization and monotonicity, not the grid.

## Relationship to prior work

Jiang and colleagues (2024) explicitly motivate allocating scarce restoration resources while balancing habitat-patch stability against ecological network connectivity. Their open-access empirical landscape model uses node and edge removal, circuit-inspired network metrics, and spatial priorities rather than a two-route independent-reliability probability with investments in each link. Zeller and colleagues (2024) develop ecological-distance and resistant-kernel landscape connectivity metrics; they do not posit independent Bernoulli path operability or derive budget-switch thresholds. Saura and colleagues (2014) establish the ecological importance of viable stepping-stone habitats; their spatial dispersal analysis does not derive the present exact optimizer.

The mathematics is related to classical series–parallel system reliability and to optimization of sigmoidal resource-return functions. El-Neweihi, Proschan and Sethuraman (1986) study component permutations with fixed reliabilities, not four continuous edge investments and independently vulnerable intermediate sites. Vicentini (1970) studies general S-shaped returns, which may supply a general allocation framework; the accessible abstract alone cannot rule out broader coverage of the step excluding interior maxima. The exact formula for the viability-dependent jump and the one-edge contrast are asserted as a special structural classification, not as new general-purpose optimization calculus.

Three directly relevant published mathematical research results were inspected in complete scientific statements: one shows a stochastic extinction-time concentration/splitting transition for a three-patch Markov colonization chain; one compares Perron eigenvalues of alternative four-patch corridors; and another contrasts independent and fixed-number surviving links on eight-edge networks. None has this objective, independent stepping-stone survival factor, continuous four-edge effort law, or the exact transition \(B_c(s)\); qualitative analogies do not imply this theorem. The inspected sources are listed in the references and review. These comparisons do not establish exhaustive historical priority.

## Limitations

The theorem is a mathematical benchmark for a highly idealized, binary-connectivity, equal-price model. Habitat survival is independent between the two routes, link operability depends only on its own investment and is independent of intermediate viability, and no ecological response, dispersal behavior, path travel time, source dynamics, or spatial cost constraints are modeled. A different effort–reliability law, dependent failures, asymmetric route prices or imperfect terminal protection can change the conclusion. The threshold is not an empirical conservation budget or a field-deployment recommendation. Priority against all older reliability and S-shaped resource-allocation literature is not certified; a highly relevant 1970 report was accessible only at abstract level. No external independent scientific validation is claimed.

## References

1. Jiang, H., Peng, J., Liu, M., Dong, J., and Ma, C. (2024), *Integrating patch stability and network connectivity to optimize ecological security pattern*. Landscape Ecology 39, article 54. **First published 2024-02-21**. https://doi.org/10.1007/s10980-024-01852-w . Open full article: https://link.springer.com/article/10.1007/s10980-024-01852-w .
2. Zeller, K. A., Compton, B. W., Finn, S. P., and Palm, E. C. (2024), *Measuring ecological connectivity with ecological distance and dynamic resistant kernels*. Landscape Ecology 39, article 95. First published 2024-04-24. https://doi.org/10.1007/s10980-024-01890-4 .
3. Saura, S., Bodin, O., and Fortin, M.-J. (2014), *Stepping stones are crucial for species' long-distance dispersal and range expansion through habitat networks*. Journal of Applied Ecology 51, 171–182. First online 2013. https://doi.org/10.1111/1365-2664.12179 .
4. El-Neweihi, E., Proschan, F., and Sethuraman, J. (1986), *Optimal allocation of components in parallel–series and series–parallel systems*. Journal of Applied Probability 23, 770–777. https://doi.org/10.2307/3214014 .
5. Vicentini, F. M. (1970), *On the Resource Allocation Problem with S-Shaped Utility Functions*, Technical memorandum no. 201, Case Western Reserve University. https://commons.case.edu/wsom-ops-reports/370/ .
6. *A sharp colonization-budget switch between seed and community persistence on three habitats* (2026). Public research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-colonization-budget-switch-between-seed-and-community-pe--b1bf0ac4bb11 .
7. *A unique corridor-investment reversal in a four-patch landscape* (2026). Public research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-unique-corridor-investment-reversal-in-a-four-patch-landscape--56bee6769edb .
8. *A sharp eight-corridor split between independent and fixed-budget ecological connectivity rankings* (2026). Public research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-eight-corridor-split-between-independent-and-fixed-budge--a542bd2ea38a .
