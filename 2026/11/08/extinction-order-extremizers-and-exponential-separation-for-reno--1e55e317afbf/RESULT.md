# Extinction-order extremizers and exponential separation for renormalized partner-loss hazards

## Finding

**Theorem (single-focal-partner loss-order law).** A focal species has positive interaction strengths \(w_1,\ldots,w_m\) with \(m\ge2\) partner species and intrinsic dependence \(0<r<1\). All partner species are removed exactly once, sequentially, while this focal species is tested for extinction after each loss. Under the post-removal updating rule defined below, the survival probability after all partner losses is **strictly maximal** when losses occur in nondecreasing order of interaction strength, and **strictly minimal** in nonincreasing order, except for permutations among equal strengths.

For the natural family \(w_j=\lambda^{j-1}\), \(\lambda>1\), the best survival probability has a strictly positive limit as \(m\to\infty\), but the worst is exponentially small. More exactly, set \(B=1-r(1-\lambda^{-1})\in(0,1)\). Then

\[
S_m^{\uparrow}=\prod_{k=1}^{m}\left(1-\frac{r(\lambda-1)}{\lambda^k-1}\right)\longrightarrow
C_{\uparrow}=\prod_{k=1}^{\infty}\left(1-\frac{r(\lambda-1)}{\lambda^k-1}\right)>0,
\]

\[
S_m^{\downarrow}=\prod_{k=1}^{m}\left(1-\frac{r(\lambda-1)\lambda^{k-1}}{\lambda^k-1}\right)
=C_{\downarrow}B^m\bigl(1+O(\lambda^{-m})\bigr),
\]

with the explicit positive constant

\[
C_{\downarrow}=\prod_{k=1}^{\infty}\left(1-\frac{r(1-\lambda^{-1})}{B(\lambda^k-1)}\right)>0.
\]

In particular, \(S_m^{\uparrow}/S_m^{\downarrow}\sim (C_{\uparrow}/C_{\downarrow})B^{-m}\): extinction sequence can change survival by an exponentially growing factor in the number of partners. This is one structural theorem about the same single-focal stochastic rule, not a claim about unconstrained community-level cascades.

## Assumptions and scope

All weights are positive, the finite integer \(m\) is at least two, and \(r\) lies strictly between zero and one. The focal species begins extant. Its partner removals are externally fixed and sequential, every partner ultimately disappears, and focal extinction is irreversible. There is **no feedback** of focal disappearance onto partner removals or any other species. With \(\sigma\) a permutation of \(1,\ldots,m\), write the remaining pre-loss interaction total as

\[
W_t=\sum_{s=t}^{m}w_{\sigma(s)}>0.
\]

If the focal species remains extant before step \(t\), the conditional probability that it becomes extinct at that step is \(r w_{\sigma(t)}/W_t\); if it survives, the next \(W_t\) omits the removed partner. Thus conditional survival is \(1-rw_{\sigma(t)}/W_t>0\), and by the chain rule its final survival is

\[
S_\sigma(r;w_1,\ldots,w_m)=\prod_{t=1}^{m}\left(1-\frac{r w_{\sigma(t)}}{W_t}\right).
\]

Even when the final partner is removed the focal species has conditional survival probability \(1-r\), matching the non-unit intrinsic dependence in the motivating stochastic coextinction model. The model fixes strengths until partner removal and renormalizes them by the *current remaining total*.

## Proof

**1. Exact adjacent exchange.** Consider adjacent removals of weights \(a,b>0\), followed by a suffix of total remaining weight \(c\ge0\). Both orders begin with the same total \(T=a+b+c\); their subsequent suffix factors are identical. The two corresponding factors in the first order and reversed order are respectively

\[
F(a,b;c)=\left(1-\frac{ra}{T}\right)\left(1-\frac{rb}{b+c}\right),\qquad
F(b,a;c)=\left(1-\frac{rb}{T}\right)\left(1-\frac{ra}{a+c}\right).
\]

Direct common-denominator subtraction gives the **exact identity**

\[
F(a,b;c)-F(b,a;c)=
\frac{abr(a-b)(r-1)}{(a+c)(b+c)(a+b+c)}.
\]

All denominator factors and every other survival factor are positive. Since \(0<r<1\), if \(a>b\), swapping \(a,b\) into \(b,a\) strictly *increases* survival; if \(a<b\), the opposite swap strictly decreases it. Repeated adjacent exchanges (bubble sort) yield increasing and decreasing orders as the global maximum and minimum. A permutation not monotone in the required direction contains an adjacent unequal inversion; reversing it strictly improves the objective. Ties can be permuted freely and are the only source of equality among optimal orders.

**2. Geometric weights.** Put \(w_j=\lambda^{j-1}\), \(\lambda>1\). In ascending order, read the product factors in reverse: when the suffix contains the \(k\) largest weights, the removed weight as a fraction of the remaining total is \((\lambda-1)/(\lambda^k-1)\). This gives the displayed exact expression for \(S_m^{\uparrow}\). Its factor at \(k=1\) is \(1-r>0\); all later factors are positive and their decrements are summable because \((\lambda-1)/(\lambda^k-1)=O(\lambda^{-k})\). The standard logarithm criterion for positive infinite products then proves \(C_{\uparrow}>0\).

For descending order, the corresponding lost fractions are \((\lambda-1)\lambda^{k-1}/(\lambda^k-1)=(1-\lambda^{-1})(1+1/(\lambda^k-1))\). Therefore, for every \(k\ge1\),

\[
1-\frac{r(\lambda-1)\lambda^{k-1}}{\lambda^k-1}
=B\left(1-\frac{r(1-\lambda^{-1})}{B(\lambda^k-1)}\right).
\]

The normalized factor in parentheses is positive (because its product with \(B>0\) is an original positive survival factor) and differs from one by \(O(\lambda^{-k})\). Its infinite product converges to a strictly positive \(C_{\downarrow}\), with relative tail error \(O(\lambda^{-m})\), proving the claimed exponential asymptotic. Combining the two limits proves the exponential ratio.

**3. Why updating matters.** If instead the numerator were divided by a fixed original interaction total \(W=\sum_jw_j\) at *every* step, the final survival would be \(\prod_j(1-rw_j/W)\), which is invariant under loss permutation. Thus dynamic renormalization is necessary for the ordering phenomenon under this focal model. For equal weights the order is immaterial and the exact survival is

\[
S_m=\prod_{k=1}^{m}(1-r/k)=\frac{\Gamma(m+1-r)}{\Gamma(1-r)\Gamma(m+1)}
\sim\frac{m^{-r}}{\Gamma(1-r)};
\]

this polynomial-scale decay differs from the extreme geometric-weight ordering. These cases fix both a mathematical boundary and an interpretable scale for the theorem.

## Verification

Run `python3 checker.py` using only the Python standard library. The checker independently enumerates distinct removal permutations for several integer, tied, and geometric weight families; it compares exact rational values with both sorted orders, checks the adjacent exchange identity for exact rational parameters, verifies both geometric finite-product identities, and tests their asymptotic constants numerically. It returned 144 exact adjacent-exchange comparisons, 36,522 exact permutation comparisons, 144 geometric identity checks, and 54 geometric asymptotic comparisons. The general-order theorem is proved above; no finite enumeration is used to infer arbitrary-order validity.

## Relationship to prior work

Vieira and Almeida-Neto (first publicly released 28 November 2014, [1]) introduced the stochastic coextinction rule \(P_{ij}=R_i d_{ij}\), where \(d_{ij}\) is proportional to interaction strength among surviving partners and is updated after partner losses. This theorem analyzes the **exogenously specified single-focal no-feedback subcase** of that rule. The source's full nine-page article describes simulation cascades and empirical connectance effects, not a universal pairwise order exchange or a positive-versus-exponential asymptotic at fixed intrinsic dependence.

Memmott, Waser, and Price [2] studied random and degree-ordered pollinator extinctions under topological partner-loss rules; their loss-on-last-partner mechanism does not imply the conditional-hazard identity. Traveset, Tur, and Eguíluz [3] compared three removal scenarios and analytically averaged plant survival under random removal, whereas the result here optimizes **each entire prescribed permutation** and quantifies an infinite-size separation. Bane, Pocock, and James [4] examined differing knockout models and order-dependent network robustness, rather than this exact one-focal weight-renormalized product. These comparisons distinguish the theorem from established qualitative removal-order sensitivity; they are not a claim of historical uniqueness.

## Limitations

The theorem does not establish optimal controls for real ecosystems, stochastic primary-loss timings, fully coupled community cascades, adaptive interaction rewiring, simultaneous removals, unknown weights, or feedback of focal extinction on other taxa. The geometric example uses increasingly heterogeneous interaction strengths as \(m\) grows; it is a structural limit rather than a calibrated ecological forecast. Earlier work on arbitrary conditional-product ordering could still cover this mathematical special case, and independent literature review is outstanding. All survival assertions require \(0<r<1\); at \(r=1\) the final loss forces extinction under every order, so the strict and positive-limit conclusions do not apply.

## References

1. Vieira, M. C., and Almeida-Neto, M. (2014 first online; journal 2015), *A simple stochastic model for complex coextinctions in mutualistic networks: robustness decreases with connectance*, Ecology Letters. https://doi.org/10.1111/ele.12394.
2. Memmott, J., Waser, N. M., and Price, M. V. (2004), *Tolerance of pollination networks to species extinctions*, Proceedings of the Royal Society B. https://doi.org/10.1098/rspb.2004.2909.
3. Traveset, A., Tur, C., and Eguíluz, V. M. (2017), *Plant survival and keystone pollinator species in stochastic coextinction models: role of intrinsic dependence on animal-pollination*, Scientific Reports. https://doi.org/10.1038/s41598-017-07037-7.
4. Bane, M. S., Pocock, M. J. O., and James, R. (2018), *Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness*, Ecology and Evolution. https://doi.org/10.1002/ece3.4529.
