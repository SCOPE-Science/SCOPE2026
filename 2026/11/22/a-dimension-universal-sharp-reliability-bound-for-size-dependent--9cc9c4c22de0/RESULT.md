# A dimension-universal sharp reliability bound for size-dependent fragment survival

## Finding

Dividing a finite supply of living material into many independently surviving fragments creates two competing effects: more attempts to retain the same donor lineage, and lower survival probability for each smaller fragment. Under the explicit inverse-length survival law below, these effects define one preferred fragment size independent of the total material budget. A sharp reliability envelope holds against **every finite, possibly unequal partition**; a two-integer rule computes the optimum **within equal-sized partitions**.

For \(d,b,V>0\), define \(L(z)=-\log(1-e^{-z})\). There exists exactly one \(z_d\in(0,d)\) such that

\[
 dL(z_d)=\frac{z_d}{e^{z_d}-1}.
\]

Put \(v_*=(b/z_d)^d\) and \(C_d=z_d^dL(z_d)\). If \(P\) is the probability of at least one survivor from any admissible finite partition, then

\[
 P\le 1-\exp\!\left(-\frac{V}{b^d}C_d\right).
\]

This bound is attained by a finite partition **if and only if** \(V/v_*\) is a positive integer, in which case every fragment has size \(v_*\); no other partition attains equality. If only equal fragment sizes are permitted, their best integer count can be found by testing at most the two integers bracketing \(V/v_*\), each clipped below at one. The location \(z_d\) is strictly increasing with \(d\). Notably, \(z_1=\log 2\), and \(z_2\approx1.830300860680\), so in two-dimensional area units the preferred area is \(v_*\approx0.298507352140b^2\), with individual survival approximately \(0.160365312899\) at that area.

## Assumptions and scope

Fix a real dimension exponent \(d>0\), a vulnerability length \(b>0\), and total usable material \(V>0\). Admissible decisions consist of an arbitrary positive integer \(n\) and positive real pieces \(v_1,\ldots,v_n\) whose sum is \(V\). A fragment of size \(v\) survives a specified outcome horizon with probability

\[
 p(v)=\exp\left(-\frac{b}{v^{1/d}}\right).
\]

Survival events of distinct fragments are independent. The goal is to maximize the probability that **at least one** fragment survives, not expected surviving area or expected growth. The case \(d=2\) models a postulated edge-to-area mortality penalty for geometrically similar planar coral microfragments, since characteristic inverse length scales with inverse square root of area. No derivation from measured coral mortality, independence test, or species-level calibration is claimed. Other positive exponents are treated mathematically.

## Proof

**Step 1: complementary-failure information.** Since \(0<p(v)<1\), the probability that all fragments fail is

\[
 1-P=\prod_{j=1}^{n}\left(1-e^{-b/v_j^{1/d}}\right).
\]

Thus the additive log-failure reduction is \(-\log(1-P)=\sum_{j=1}^nL(z_j)\), where \(z_j=b/v_j^{1/d}\). Let \(h_d(z)=z^dL(z)\). As \(v_j=(b/z_j)^d\),

\[
 \frac{L(z_j)}{v_j}=\frac{h_d(z_j)}{b^d}.
\]

**Step 2: unique maximum of information per material.** The function \(L\) is strictly positive, satisfies \(L'(z)=-1/(e^z-1)\), and obeys

\[
 0<L(z)<\frac1{e^z-1}\qquad(z>0).
\]

The last inequality follows termwise from the absolutely convergent series \(L(z)=\sum_{m\ge1}e^{-mz}/m\) and \((e^z-1)^{-1}=\sum_{m\ge1}e^{-mz}\); strictness comes from terms \(m\ge2\). Differentiation gives

\[
 h_d'(z)=z^{d-1}Q_d(z),\qquad
 Q_d(z)=dL(z)-\frac{z}{e^z-1},
\]

and

\[
 Q_d'(z)=\frac1{e^z-1}
 \left(\frac{z}{1-e^{-z}}-(d+1)\right).
\]

The function \(z/(1-e^{-z})\) is strictly increasing, because its derivative is positive by \(e^z>1+z\). For \(0<z\le d\),

\[
 \frac{z}{1-e^{-z}}\le\frac{d}{1-e^{-d}}<d+1,
\]

where the final strict inequality is equivalent to \(e^d>1+d\). Consequently, \(Q_d'<0\) throughout \((0,d)\). Moreover \(Q_d(z)\to+\infty\) as \(z\downarrow0\), whereas \(Q_d(d)<0\) by \(L(d)<(e^d-1)^{-1}\). Thus it has precisely one root \(z_d\in(0,d)\). For every \(z\ge d\), the series inequality yields \(Q_d(z)<(d-z)/(e^z-1)\le0\). Therefore \(h_d\) increases strictly up to \(z_d\) and decreases strictly afterward. The endpoint limits are zero: \(z^dL(z)\to0\) as \(z\downarrow0\), and \(z^dL(z)\to0\) as \(z\to\infty\). This proves existence, global uniqueness and strictness of the optimum.

**Step 3: sharp arbitrary-partition bound and equality.** Each summand obeys

\[
 L(z_j)=\frac{v_j}{b^d}h_d(z_j)
 \le \frac{v_j}{b^d}h_d(z_d).
\]

Summing and using \(\sum_jv_j=V\) gives

\[
 -\log(1-P)\le\frac{V}{b^d}C_d.
\]

Exponentiating establishes the claimed bound. Because all \(v_j\) are positive and \(h_d\) has a unique maximizer, equality in the sum occurs exactly when every \(z_j=z_d\), equivalently \(v_j=v_*\). Total size then requires \(n=V/v_*\) to be a positive integer. Conversely that equal partition attains equality, proving sharpness and the complete equality characterization.

**Step 4: exact integer rule for equal partitions.** With \(n\) equal fragments, their total log-failure reduction is

\[
 H(n)=nL\!\left(b(n/V)^{1/d}\right).
\]

For real \(t>0\), set \(z=b(t/V)^{1/d}\). Then \(H(t)=(V/b^d)h_d(z)\), strictly increasing until \(t_*=V/v_*\) and strictly decreasing thereafter. Over integers \(n\ge1\), compare the two neighbors \(\max(1,\lfloor t_*\rfloor)\) and \(\max(1,\lceil t_*\rceil)\); no other integer can win. Either or both may be optimal depending on equality of the two objective values. This integer statement concerns equal-size partitions only.

**Step 5: dimensional monotonicity and a special case.** If \(d_2>d_1>0\), then \(Q_{d_2}(z)=Q_{d_1}(z)+(d_2-d_1)L(z)>Q_{d_1}(z)\) for all \(z>0\). At \(z=z_{d_1}\), the left side is positive, so its unique zero lies at a larger \(z\): \(z_{d_2}>z_{d_1}\). With \(d=1\), substituting \(z=\log2\) into \(L(z)=z/(e^z-1)\) verifies \(z_1=\log2\) by uniqueness.

## Verification

The proof is analytic and does not depend on numerical experiments. From the enclosed standalone `verify.py`, run `python3 verify.py` with a standard-library Python interpreter. The script independently evaluates the defining root by bisection, checks numerical signs, verifies bound/equality on sampled partitions, and compares the two-candidate equal-fragment rule with a finite enumeration. It reports 43,789 supplemental assertions and the illustrative dimension-one, -two, and -three constants. Such finite checks do not prove uniqueness for all real \(d\) or the inequality for all possible partitions; Steps 1–5 supply that proof.

For example, at \(d=2\), \(b=V=1\), the equal-partition continuous optimum count is about \(3.35000124\), so the optimal count among equal-sized partitions is selected by comparing three and four. Three gives survival approximately \(0.44239811\), and four about \(0.44102685\). The universal arbitrary-partition bound is about \(0.4432\). No global optimum over unequal partitions is asserted when the equality condition \(V/v_*\in\mathbb N\) fails.

## Relationship to prior work

Schlecker et al. (2022) report experimental tradeoffs among coral microfragment size, growth and immune investment, while Knapp et al. (2022) directly assess size-dependent coral survival and outplanting. Neither supplies the postulated independent inverse-length mortality law, the dimension-dependent critical equation, the global probability-of-any-survivor envelope, or its equality condition. These ecological papers motivate the decision question rather than validate the survival formula.

Pichugin, Peña, Rainey and Traulsen (2017), and Pichugin and Traulsen (2020), mathematically optimize evolutionary multicellular fragmentation strategies by long-run population growth and fragmentation costs. Their model state, objective and mortality mechanism differ: maximizing a population projection matrix growth rate is not maximizing at-least-one-fragment survival for a fixed total tissue budget. The familiar general technique of bounding total benefit by a maximal benefit-per-unit-size ratio underlies Step 3; the contribution here is the exact dimension-universal strict shape, unique constant, equality characterization and finite-size rule for the specified biological reliability functional. No claim of a first-ever resource-allocation inequality is made.

## Limitations

The survival law is stipulated, not estimated from the cited field studies. Spatially correlated mortality, disease propagation, tissue damage during cutting, minimum viable fragment size, changing shape, nursery labor, growth, genetic diversity, and placement costs are excluded. Actual coral survivorship may lack monotonic dependence on size, and species and sites vary. The sharp envelope is attained for special material budgets but need not be attainable for any fixed generic budget; the two-neighbor integer rule does **not** solve the unequal-partition optimization problem in those cases. Broader priority in classical allocation theory cannot be ruled out without further independent review; no field recommendation or independent validation is asserted.

## References

1. Schlecker, L., Page, C., Matz, M., and Wright, R. M. (2022). *Mechanisms and potential immune tradeoffs of accelerated coral growth induced by microfragmentation*. PeerJ 10:e13158. First published March 29, 2022. https://doi.org/10.7717/peerj.13158 . Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC8973463/ .
2. Knapp, I. S. S., et al. (2022). *Coral micro-fragmentation assays for optimizing active reef restoration efforts*. PeerJ 10:e13653. First published July 18, 2022. https://doi.org/10.7717/peerj.13653 . Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC9302430/ .
3. Pichugin, Y., Peña, J., Rainey, P. B., and Traulsen, A. (2017). *Fragmentation modes and the evolution of life cycles*. PLOS Computational Biology 13:e1005860. https://doi.org/10.1371/journal.pcbi.1005860 . Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC5718564/ .
4. Pichugin, Y., and Traulsen, A. (2020). *Evolution of multicellular life cycles under costly fragmentation*. PLOS Computational Biology 16:e1008406. https://doi.org/10.1371/journal.pcbi.1008406 . Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC7714367/ .
5. Sam, S. Q., Ng, C. S. L., and Kikuzawa, Y. P. (2021). *Influence of fragment size on post transplantation growth and survival of domed scleractinian corals*. Marine Biology Research 17. https://doi.org/10.1080/17451000.2021.1957934 . Abstract and accessible bibliographic material consulted; full text not established as inspected.
