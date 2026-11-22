# A universal activation jump and later effort reversal for mixed one- and two-visit pollination

## Finding

Consider a fixed total mean of productive visits \(B>0\) split between one flower requiring at least one visit and another requiring at least two visits. The second fruit has relative value \(v\in(0,1]\). Write \(y\in[0,B]\) for the mean visits assigned to the two-visit flower and \(B-y\) for the one-visit flower. Under the stated independent-Poisson model, the expected weighted fruit count is
\[
F_{B,v}(y)=1-e^{-(B-y)}+v\bigl[1-(1+y)e^{-y}\bigr].
\]

Define \(u\) as the unique root in \((1/2,1)\) of
\[
H(u)=1-(1+2u)e^{-u}+u e^{-2u}=0,
\]
and set
\[
B_c(v)=2u-\log(vu),\qquad B_s(v)=2/v.
\]
Then \(B_c(v)<B_s(v)\) and **all** global maximizers are classified as follows:

1. For \(0<B<B_c(v)\), the unique maximizer is \(y=0\) (all effort to the one-visit flower).
2. For \(B=B_c(v)\), exactly two allocations maximize: \(y=0\) and \(y=u\).
3. For \(B>B_c(v)\), the unique maximizer is \(y=y_+(B,v)>u\), the larger positive solution of
   \[
   B=2y-\log(vy).
   \]
   On this active branch, \(y_+<B/2\) for \(B_c(v)<B<2/v\), \(y_+=B/2\) at \(B=2/v\), and \(y_+>B/2\) for \(B>2/v\).

In particular, the active optimizer jumps by the **same nonzero amount** \(u=0.842568964351706\ldots\) for every relative value \(v\in(0,1]\), while the budget threshold shifts exactly by \(-\log v\). For the equal-value case, \(B_c(1)=1.856437692011840\ldots\) and the allocation reaches equality at \(B=2\). The newly active hard flower eventually receives more visit effort than the easier flower even though its fruit value is no larger.

## Assumptions and scope

One flower requires at least one productive pollinator visit to count as a viable fruit; the other requires at least two. Their visit counts have Poisson marginals with nonnegative respective means \(B-y\) and \(y\). Their weighted expected fruit output is additive; independence of the two counts suffices but is not required for this expectation. The first fruit has value one and the second value \(v\in(0,1]\). Total expected productive visits \(B>0\) can be allocated continuously without travel, handling, interference, or flowers' additional resource constraints. A successful visit is treated as a unit event; the model does not assert that any particular crop follows these exact threshold laws.

The assertion concerns global optimization of expected fruit count, not the probability of producing any fruit, realized visitor scheduling, or optimization over a variable number of flowers. All quantified parameters are real in the stated ranges.

## Proof

**Step 1 (stationary-point geometry).** Differentiation gives
\[
\frac{\partial F_{B,v}}{\partial y}=vy e^{-y}-e^{-B+y}
=e^{-B+y}\bigl(vy e^{B-2y}-1\bigr).
\]
The factor \(y e^{-2y}\) increases on \((0,1/2)\) and decreases on \((1/2,\infty)\). Also \(\partial_yF_{B,v}(0)=-e^{-B}<0\) and \(\partial_yF_{B,v}(B)=vB e^{-B}-1<0\), since \(0<v\le1\) and \(B e^{-B}\le1/e\). For
\[
B\le B_0(v):=1+\log(2/v),
\]
the derivative is never positive, so \(y=0\) is uniquely optimal. For \(B>B_0(v)\), there are exactly two interior stationary points: \(y_-<1/2<y_+\), with derivative signs negative, positive, negative; the smaller is a strict local minimum, the larger a strict local maximum. Indeed the stationary equation is \(B=b_v(y):=2y-\log(vy)\), whose minimum occurs at \(y=1/2\); the upper root lies below \(B\), because \(B-y=y-\log(vy)\ge1\) follows from \(\log(vy)\le\log y\le y-1\). Thus global maximizers can only be \(0\) or \(y_+\). Moreover \(b_v'(y)=2-1/y>0\) on \((1/2,\infty)\), so \(y_+\) grows strictly with \(B\).

**Step 2 (unique global switch).** At a stationary point \(y>0\), \(e^{-B}=vy e^{-2y}\). Direct subtraction yields the exact identity
\[
F_{B,v}(y)-F_{B,v}(0)
=v\left[1-(1+2y)e^{-y}+y e^{-2y}\right]=vH(y).
\]
Its derivative is
\[
H'(y)=(2y-1)e^{-y}(1-e^{-y}),
\]
strictly positive for \(y>1/2\). Elementary inequalities give \(H(1/2)<0<H(1)\), so a unique root \(u\in(1/2,1)\) exists. The strictly increasing upper stationary branch crosses this root at the single budget \(B=b_v(u)=B_c(v)\). The sign of \(H(y_+)\) is negative, zero, or positive before, at, or after this crossing. Combining this comparison with Step 1 proves the three global-optimum cases and the absence of any unlisted optimizer. Since \(u\) is independent of \(v\), the entry jump is universal, and \(B_c(v)=B_c(1)-\log v\).

**Step 3 (effort inversion).** On the active branch,
\[
(B-y_+)-y_+=-\log(vy_+).
\]
Consequently the hard flower receives less, equal, or more effort than half the budget as \(vy_+\) is less than, equal to, or greater than one. Since \(1/v\ge1>u\) and \(b_v\) is strictly increasing above \(1/2\), the unique equal-effort budget is
\[
b_v(1/v)=2/v,
\]
strictly after \(B_c(v)\). This proves the stated classification. For any fixed \(v>0\), substitution in the stationary equation further gives
\[
y_+(B,v)=\frac B2+\frac12\log(vB/2)+O_v\left(\frac{\log B}{B}\right),\qquad B\to\infty,
\]
showing the logarithmically growing relative visit advantage of the higher-threshold flower.

## Verification

The companion standalone \(\texttt{verify.py}\) recomputes the unique root by bisection and compares the proposed optimizers with 75,621 deterministic finite diagnostic tests, including boundaries, values close to the switching budget, unequal values, and independent budget scans. It returned `PASS numerical diagnostic assertions: 75621`. These computations check implementation and representative cases; the global assertions follow from the analytic derivative and comparison arguments above, not from grid coverage.

## Relationship to prior work

Cane and Schiffhauer (2003) provide direct evidence for threshold and saturation effects in pollen-dose versus fruit-set curves, not a theorem on optimally splitting Poisson visit means between different threshold types. Stavert and colleagues (2020) empirically study multiple visits and report that a single visit did not initiate fruiting in their apple experiment; their analysis is neither a fixed-budget allocation problem nor a mathematical derivation of the jump \(u\). Wesselingh (2007) discusses pollen limitation and competition for reproductive resources, not this specific global optimization.

General sigmoid-response resource-allocation research, including Alban and colleagues (2021/2022), is a genuine adjacent mathematical literature: smooth nonconcave returns can generate concentrated allocations. The particular heterogeneous Poisson one-versus-two tail objective, value-independent jump, and subsequent exact balance threshold are not identified in the *accessible* material; the full text of the general sigmoid paper could not be examined and historical priority therefore remains provisional. Closely related published homogeneous Poisson-quorum allocation results and Hill-response active-set staircases use different objective families and do not, from their statements, imply this mixed-threshold phase diagram. No claim of generic novelty for nonconcave optimization, fixed-total Poisson allocation, or the use of first-order conditions is made.

## Limitations

This is an idealized two-flower benchmark with independent-Poisson-type marginal arrivals, deterministic success after exactly one versus two visits, and continuously redirectable mean effort. It does not account for visit dependence, pollen incompatibility or dose variability, resource-limited fruit abortion, more than two flowers, or species-specific field parameterization. The universal activation amount is measured in **expected productive visits**, not literal fractional visits to an individual flower. Broad historical priority has not been independently established. Numerical diagnostics provide no infinite-domain certification; the proof is analytic.

## References

- Cane, J. H. and Schiffhauer, D. (2003). *Dose-response relationships between pollination and fruiting refine pollinator comparisons for cranberry*. American Journal of Botany 90, 1425–1432. https://doi.org/10.3732/ajb.90.10.1425 (published online 2003-10-01).
- Wesselingh, R. A. (2007). *Pollen limitation meets resource allocation: towards a comprehensive methodology*. New Phytologist 174, 26–37. https://doi.org/10.1111/j.1469-8137.2007.01997.x.
- Stavert, J. R., Bailey, C., Kirkland, L. and Rader, R. (2020). *Pollen tube growth from multiple pollinator visits more accurately quantifies pollinator performance and plant reproduction*. Scientific Reports 10, 16958. https://doi.org/10.1038/s41598-020-73637-5.
- Alban, A., Blaettchen, P., de Vries, H. and Van Wassenhove, L. N. (2021/2022). *Resource Allocation with Sigmoidal Demands: Mobile Healthcare Units and Service Adoption*. Manufacturing & Service Operations Management 24, 2944–2961. https://doi.org/10.1287/msom.2021.1020. Only available metadata and abstract were inspectable.
