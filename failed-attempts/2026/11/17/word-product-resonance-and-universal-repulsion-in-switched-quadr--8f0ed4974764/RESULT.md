# Word-product resonance and universal repulsion in switched quadratic population maps

## Finding

For \(t\in[-1,1]\), define the two-type quadratic stochastic map
\[
q_t(x)=x+t x(1-x),\qquad 0\le x\le1.
\]
For a word \(w=(t_1,\ldots,t_n)\) with \(n\ge1\), put \(Q_w=q_{t_n}\circ\cdots\circ q_{t_1}\), and define its endpoint products
\[
A_w=\prod_{j=1}^n(1+t_j),\qquad B_w=\prod_{j=1}^n(1-t_j).
\]
**Word-product resonance theorem.** If some \(t_j\ne0\), then \(Q_w\) has exactly one fixed point in \((0,1)\) if and only if
\[
A_w<1\quad\text{and}\quad B_w<1.
\]
Otherwise it has no fixed point in \((0,1)\). Whenever the fixed point exists, it is hyperbolically repelling, with \(Q_w'(x_*)>1\). The criterion depends only on the multiset of the coefficients, not their order; the location \(x_*\) can depend on the order. If every \(t_j=0\), \(Q_w\) is the identity and every point is neutrally fixed.

**Piecewise application.** Partition \((0,1)\) into finitely many intervals and assign one \(q_t\), \(t\in[-1,1]\), to each interval. Every interior periodic orbit of least period at least two that avoids partition boundaries at all its points is hyperbolically repelling. For any prescribed anchored branch itinerary, there is at most one such periodic point. In particular, there are no attracting regular interior cycles for any number of switching intervals or any admissible coefficient vector. This applies to the three-piece map of Abdurakhimova and Rozikov (2021), whose primary mathematical classification is different from the 2019 motivating source.

## Assumptions and scope

The word theorem concerns an exogenously specified finite sequence of maps acting on \((0,1)\), including the extreme coefficients \(t=\pm1\). No stochastic independence or global continuity of a piecewise selection is assumed. In the piecewise statement, a regular periodic orbit has all its coordinates in open partition interiors; hence its itinerary remains unchanged for sufficiently close initial conditions through its prescribed period. The theorem does not classify periodic orbits hitting a discontinuity, endpoints, or invariant nonperiodic sets; nor does it assert existence of an admissible orbit for every word satisfying the products. Instead, it gives an exact criterion for the *unrestricted composition* and a necessary criterion plus unique-location test for a *branch-constrained itinerary*.

## Proof

Write \(\sigma(z)=e^z/(1+e^z)\), \(\ell(x)=\log(x/(1-x))\), and \(G_t=\ell\circ q_t\circ\sigma\) on \(\mathbb R\). On \((0,1)\), the identities
\[
q_t(x)=x[1+t(1-x)],\qquad 1-q_t(x)=(1-x)(1-tx)
\]
show that both bracket factors are strictly positive even when \(t=\pm1\). Direct differentiation yields
\[
G_t'(\ell(x))
=\frac{1+t(1-2x)}{[1+t(1-x)](1-tx)}
=1+\frac{t^2x(1-x)}{[1+t(1-x)](1-tx)}.
\]
Thus \(G_t'\ge1\) on \(\mathbb R\), with strict inequality at every point if \(t\ne0\). For \(G_w=G_{t_n}\circ\cdots\circ G_{t_1}\), the chain rule implies \(G_w'(z)>1\) at every finite \(z\) whenever the word contains a nonzero coefficient. Consequently \(h_w(z)=G_w(z)-z\) is strictly increasing.

At the left endpoint, \(q_t(x)\sim (1+t)x\) when \(t>-1\), whereas \(q_{-1}(x)=x^2\). At the right endpoint, \(1-q_t(x)\sim(1-t)(1-x)\) when \(t<1\), whereas \(1-q_1(x)=(1-x)^2\). Composition of these positive monotone maps gives the extended endpoint limits
\[
\lim_{z\to-\infty} h_w(z)=\log A_w,
\qquad
\lim_{z\to+\infty} h_w(z)=-\log B_w,
\]
where \(\log0=-\infty\) and \(-\log0=+\infty\). These formulas also hold with extreme coefficients: the first map that has a zero endpoint derivative produces a higher-order zero, and subsequent maps cannot restore a first-order zero. Because \(h_w\) is strictly increasing and continuous, it has a unique zero exactly when its left limit is strictly negative and its right limit strictly positive. If either limit equals zero, strict increase excludes a finite zero on the corresponding side. This proves the necessary and sufficient product inequalities and uniqueness.

At a fixed point, the derivative in the original coordinate is the derivative in logit coordinates because the outer coordinate derivatives cancel:
\[
Q_w'(x_*)=G_w'(\ell(x_*))>1.
\]
For the piecewise application, a regular orbit of period \(n\ge2\) has a unique local word of coefficient choices. At least one coefficient in this word is nonzero, since otherwise each step fixes its state and its least period would be one. The return map agrees near the orbit with \(Q_w\); hence the strict multiplier and at-most-one-itinerary statements follow. A branch-constrained orbit must pass the additional interval-membership checks after calculating the unique unrestricted fixed point; product resonance alone does not guarantee those checks.

**Exact illustration.** Choose \(x_0=1/5\), \(x_1=17/50\), \(t_0=7/8\), and \(t_1=-350/561\). Then \(q_{t_0}(x_0)=x_1\), \(q_{t_1}(x_1)=x_0\), and the return multiplier equals \(27389/22440>1\). These points lie in the first and second intervals of the two-discontinuity construction with cuts at \(1/3\) and \(2/3\), using \(a=15/16\), \(b=211/1122\), and arbitrary \(c\in[0,1]\). This is a check of nonvacuity, not a claim of a new isolated orbit.

## Verification

The accompanying standalone file `checks/check.py` re-derives the logit derivative identity symbolically, checks the exact rational two-cycle and its multiplier, and verifies 776 finite rational word cases for positivity and noncontraction. Run `python checks/check.py` from the directory containing this file. The expected final output begins `SWITCHED_QUADRATIC_LOGIT_CHECK_OK`. The proof above, not the finite checks, establishes the theorem for all words and all permitted real parameters.

## Relationship to prior work

Rozikov and Usmonov's 2019 preprint (2020 journal version, primary MSC 37E05) introduces a particular one-cut, two-parameter switched quadratic population map and proves its periodic points repelling. That restricted qualitative repulsion assertion is **prior work** and is not being presented as new. The present theorem additionally treats arbitrary coefficient words and arbitrary finite cuts, including regimes with Euclidean branch derivatives below one, and gives an exact endpoint-product iff criterion plus itinerary uniqueness. Abdurakhimova and Rozikov's 2021 two-cut paper gives the three-coefficient family and analyzes parameter-dependent fixed/periodic behavior; its fully inspected preprint does not present the word-product criterion or the all-regular-periodic-orbits multiplier result. Its primary MSC is 92D25, so it is supporting context rather than the primary source determining this result's dynamical classification. General projective-metric expansion or distortion results might imply portions of the theorem; the exact mathematical implication and all-word criterion must be distinguished from restricted repulsion results.

## Limitations

Only smooth itinerary cycles are classified dynamically; boundary-hitting cycles are explicitly excluded and could behave differently. The uniqueness theorem for an unrestricted composition does not imply that its unique fixed point satisfies any specific partition itinerary. No statement of global attraction/chaos, entropy, or invariant-measure uniqueness is made. Prior publication priority is qualified by the inspected literature and searchable mathematical records; related newer same-family conjugacy work and general distortion results were not fully resolved. Independent mathematical audit has not been performed.

## References

1. U. A. Rozikov and J. B. Usmonov, *Dynamics of a Population with Two Equal Dominated Species*, arXiv:1909.07106, first submitted 2019-09-16; *Qualitative Theory of Dynamical Systems* 19 (2020), article 62, DOI:10.1007/s12346-020-00399-w, primary MSC 37E05. https://arxiv.org/abs/1909.07106
2. Sh. B. Abdurakhimova and U. A. Rozikov, *Dynamical system of a quadratic stochastic operator with two discontinuity points*, arXiv:2103.14834, first submitted 2021-03-27; *Mathematical Notes* 111 (2022), pp. 676–687. https://arxiv.org/abs/2103.14834
