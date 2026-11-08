# A one-switch sign law for paired coextinction during fixed-count pollinator loss

## Finding

Consider two plant species whose nonempty sets of pollinator partners are \(A\) and \(B\), within a finite pool of \(n\) distinct pollinators. Remove exactly \(r\) pollinators uniformly without replacement. Each plant remains viable precisely when at least one of its original partners survives. Put \(a=|A|\), \(b=|B|\), \(c=|A\cap B|\), and \(u=a+b-c\). Let \(S_A(r),S_B(r)\in\{0,1\}\) denote plant-survival indicators. For \(s\in\{0,\ldots,n\}\), set

\[
q_s(r)=\begin{cases}\binom{r}{s}/\binom{n}{s},&r\ge s,\\0,&r<s.\end{cases}
\]

Then at every integer \(0\le r\le n\),

\[
\boxed{\operatorname{Cov}(S_A(r),S_B(r))=q_u(r)-q_a(r)q_b(r).}
\]

The covariance has a complete sign classification:

1. **Nested partners.** If \(A\subseteq B\) or \(B\subseteq A\), covariance is nonnegative for every stage, and strictly positive whenever \(u\le r<n\). (The strict interval is empty if \(u=n\).)
2. **Incomparable partners with no excess intersection.** Suppose neither partner set contains the other, equivalently \(c<\min(a,b)\). If \(nc\le ab\), covariance is nonpositive at every stage; it is strictly negative for \(\max(a,b)\le r\le n-2\), and at \(r=n-1\) is strictly negative if \(nc<ab\) and zero if \(nc=ab\).
3. **Incomparable partners with excess intersection.** If \(0<c<\min(a,b)\) and \(nc>ab\), covariance is strictly negative at \(r=\max(a,b)\), strictly positive at \(r=n-1\), and its signs on \(\max(a,b)\le r<n\) follow a single nondecreasing sequence: a nonempty negative phase, at most one zero stage, then a nonempty positive phase. There can be no return to negative covariance.

At the penultimate stage, the exact boundary is

\[
\boxed{\operatorname{Cov}(S_A(n-1),S_B(n-1))=\frac{nc-ab}{n^2}.}
\]

The threshold \(nc>ab\) is the same as \(c>ab/n\): the actual shared-pollinator count must exceed the mean overlap of two independently randomized sets of sizes \(a,b\). It determines whether positive fixed-stage covariance is *ever possible* for incomparable species; the switch location within the removal sequence depends on all four parameters.

## Assumptions and scope

Here \(n\ge2\) is an integer, \(A,B\) are arbitrary nonempty subsets of a fixed \(n\)-element pollinator pool, and \(r=0,1,\ldots,n\). This is the binary static-knockout model with no interaction rewiring, no variable pollination efficiency, no reproduction after pollinator loss, and uniformly random *fixed-count* removal. Removing the first \(r\) pollinators of a uniformly random permutation is equivalent. Plants are modeled as disappearing only when their last pollinator disappears. Both plant indicators are deterministic functions of the same random removed subset. The theorem does not apply to weighted/remodeled interactions, nonuniform removal sequences, or arbitrary correlated primary extinctions.

For \(r<\max(a,b)\), both plant-extinction indicators cannot simultaneously be one, and the covariance is zero. At \(r=n\) both plants have disappeared and the covariance is zero. All other strict claims refer to the specified integer stage ranges, including empty-range conventions.

## Proof

Write \(R_r\) for the uniformly sampled set of \(r\) removed pollinators, and \(E_A=\mathbf1\{A\subseteq R_r\}\), \(E_B=\mathbf1\{B\subseteq R_r\}\) for plant-extinction indicators. Then \(S_A=1-E_A\) and \(S_B=1-E_B\), so their covariance equals \(\operatorname{Cov}(E_A,E_B)\). Any fixed \(s\)-subset lies in \(R_r\) with probability \(q_s(r)\), and both extinction events occur exactly when \(A\cup B\subseteq R_r\). This proves the boxed formula.

For nested sets, assume without loss \(A\subseteq B\), so \(u=b\). The covariance equals \(q_b(r)(1-q_a(r))\), which is nonnegative; if \(b\le r<n\), then \(q_b(r)>0\) and \(q_a(r)<1\), proving strict positivity.

Now assume the sets are incomparable, \(c<\min(a,b)\). Then \(u>\max(a,b)\), and for every \(\max(a,b)\le r<u\), the covariance is \(-q_a(r)q_b(r)<0\). For \(u\le r\le n\), all three \(q\)'s are positive. Define

\[
H_r=\frac{q_u(r)}{q_a(r)q_b(r)}.
\]

The sign of covariance is the sign of \(H_r-1\), and \(H_n=1\). A direct cancellation of binomial factors gives, for \(u\le r<n\),

\[
\frac{H_{r+1}}{H_r}=\frac{(r+1-a)(r+1-b)}{(r+1)(r+1-u)},\qquad
\frac{H_{r+1}}{H_r}-1=\frac{ab-c(r+1)}{(r+1)(r+1-u)}.
\]

The denominators are strictly positive. If \(nc\le ab\), every successive ratio is at least one, hence \(H_r\le H_n=1\) throughout. All ratios are strictly greater than one except possibly the final ratio when \(nc=ab\). This yields strict negativity through \(n-2\) and the asserted penultimate equality or strictness.

If \(nc>ab\), the ratios are first greater than one, possibly once equal to one, then less than one (some phases can be empty). Thus \((H_r)_{r=u}^n\) is unimodal. At the penultimate stage, using \(q_s(n-1)=(n-s)/n\), we have

\[
q_u(n-1)-q_a(n-1)q_b(n-1)=\frac{nc-ab}{n^2}>0.
\]

Consequently \(H_{n-1}>1\), whereas \(H_n=1\). On the nonincreasing tail of the unimodal sequence all earlier terms are at least \(H_n\), strictly above it for \(r<n\) after the maximum; on the preceding nondecreasing segment \(H_r-1\) can cross zero at most once. Combined with the negative phase \(\max(a,b)\le r<u\), this proves the one-switch sign pattern, including the possibility of a single exact zero at an integer stage. The formula at \(n-1\) also holds in the nested and disjoint cases and completes the classification.

## Verification

Run `python3 checker.py` using only the Python standard library. The checker independently enumerates all removed subsets for representative canonical overlap patterns; separately it evaluates the binomial formula across all permissible set-size triples and stages with \(2\le n\le12\). It tests strict boundary signs and the monotone sign pattern, and verifies an exact example distinguishing stage covariance from rank covariance. The replay output is:

```
PASS exact-cardinality stage checks=17743; phase cases=1650;
PASS independent subset-enumeration comparisons=1737; distinct rank example=PASS
```

As a small explicit witness, \(n=12\), \(a=b=3\), \(c=1\) gives \(\operatorname{Cov}(S_A(6),S_B(6))=-1/1452\) and \(\operatorname{Cov}(S_A(7),S_B(7))=7/5808\). Hence two species sharing a pollinator are negatively associated midway through removal but positively associated one removal later.

For \(n=26\), \(a=b=5\), \(c=1\), the fixed-stage covariance at \(r=25\) is \(1/676>0\), whereas the covariance of their *extinction ranks* in a random permutation is \(-9/220<0\). The latter rank identity is an earlier, distinct result, not established here. This example shows that an integrated rank-covariance sign does not determine the stage-resolved sign.

## Relationship to prior work

Memmott, Waser and Price (first online 6 December 2004) used random removal without replacement and loss of the last pollinator in a static binary plant–pollinator network, reporting simulated mean robustness of networks. Kaiser-Bunbury and colleagues (2010) examined robustness with interaction strengths and possible rewiring. Bane, Pocock and James (2018) studied distributions of whole-network robustness and dependencies on network structure. These works motivate the quantity, but their inspected full text does not give an arbitrary-overlap pairwise covariance sign phase diagram over every removal count. Negative association of multivariate-hypergeometric variables, developed by Joag-Dev and Proschan (1983), applies to functions of disjoint coordinate sets; for overlapping partner sets the sign need not be negative. The elementary hypergeometric inclusion formula alone specifies the covariance but does not by itself state its global phase classification.

The previously derived covariance of *two extinction ranks* under random removal is not a stronger version of the result: it concerns different random variables, and the \(n=26\) example above exhibits opposite signs. No claim is made that a generic set-system/probability theorem outside the inspected literature could not contain an equivalent formulation.

## Limitations

This is an exact theorem for a static, binary, uniform-removal null model, not an ecological prediction for arbitrary disturbed communities. It is not a theorem for unequal pollinator extinction probabilities, species-specific coextinction probabilities, adaptive switching, recovery, or extinction cascades that feed back into the pollinator guild. A covariance sign says nothing about causal ecological interaction or statistical significance. It also does not determine the full distribution of the number of surviving plants, although it supplies exact contributions to its variance. General hypergeometric dependence literature may contain related reformulations; historical priority is provisional and independent examination remains outstanding.

## References

- Memmott, J., Waser, N. M., and Price, M. V. (2004). *Tolerance of pollination networks to species extinctions*. Proceedings of the Royal Society B 271, 2605–2611. First public online 2004-12-06. DOI: 10.1098/rspb.2004.2909. Lawful author PDF: https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf
- Kaiser-Bunbury, C. N., Muff, S., Memmott, J., Müller, C. B., and Caflisch, A. (2010). *The robustness of pollination networks to the loss of species and interactions: a quantitative approach incorporating pollinator behaviour*. Ecology Letters 13, 442–452. DOI: 10.1111/j.1461-0248.2009.01437.x. Lawful author PDF: https://www.biochem-caflisch.uzh.ch/sites/default/files/publist/pdfs/smuff10.pdf
- Bane, M. S., Pocock, M. J. O., and James, R. (2018). *Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness*. Ecology and Evolution 8, 10794–10804. DOI: 10.1002/ece3.4529. Open PDF: https://nora.nerc.ac.uk/id/eprint/521791/1/N521791JA.pdf
- Joag-Dev, K., and Proschan, F. (1983). *Negative association of random variables with applications*. Annals of Statistics 11, 286–295. DOI: 10.1214/aos/1176346079.
