# Exact classification of two-cycles of the positive Laplace chainability map

## Finding
Let \(F\) be the positive-half-line chainability operation defined by the negative logarithmic derivative of a Laplace transform. All of its genuine two-cycles, not merely an example family, are the following ordered pairs or their reversals:
\[
\mu_{a,t}=a\sum_{j=0}^{\infty}t^j\delta_{ja},\qquad
\nu_{a,t}=a\sum_{j=1}^{\infty}t^j\delta_{ja},\qquad a,t>0.
\]
Specifically, if \(\mu\ne0\) is a positive Borel measure on \([0,\infty)\) whose Laplace transform is finite on a right half-line, and \(F^2(\mu)=\mu\) is defined, then either
\[
\mu=F(\mu)=e^{-\gamma x}\,dx\quad\text{for a unique }\gamma\in\mathbb R,
\]
or \((\mu,F(\mu))=(\mu_{a,t},\nu_{a,t})\) or \((\nu_{a,t},\mu_{a,t})\) for unique \(a,t>0\). Conversely, every stated measure and pair is valid. These two-cycles are strictly nonconstant and satisfy \(\mu_{a,t}-\nu_{a,t}=a\delta_0\).

An exact probability-level consequence is that if both members of a cycle are probability measures, the cycle is the unit-mean exponential fixed point. More explicitly, **every probability measure** satisfying \(F^2(\mu)=\mu\) is exactly one of
\[
\begin{aligned}
& e^{-x}\,dx;\\
& a\sum_{j=0}^{\infty}(1-a)^j\delta_{ja},\quad 0<a<1;\\
& a\sum_{j=1}^{\infty}(1+a)^{-j}\delta_{ja},\quad a>0.
\end{aligned}
\]
The latter two families have non-probability chain partners of masses \(1-a\) and \(1+a\), respectively. This is a classification of *exact* two-cycles; the general classification of longer periodic or eventually periodic chains is not asserted.

## Assumptions and scope
For a positive, nonzero Borel measure \(\mu\) on \([0,\infty)\), write
\[
q_\mu(z)=\int_{[0,\infty)}e^{-zx}\,\mu(dx),\qquad z>z_\mu,
\]
where the abscissa \(z_\mu\) is finite or \(-\infty\). The chainability map \(F\), as in Grabchak (2026), is defined when there is a positive Borel measure \(\nu\) with the **same** abscissa of Laplace convergence and
\[
q_\nu(z)=-\frac{d}{dz}\log q_\mu(z).
\]
Then \(F(\mu)=\nu\), uniquely by Laplace-transform uniqueness. We require \(F(\mu)\) to be nonzero and in the domain of \(F\), with \(F(F(\mu))=\mu\). The measures may have infinite unweighted total mass, but all exponentially tilted measures at admissible \(z\) are finite. The series in the theorem converge on the common half-line \(z>\log(t)/a\); the fixed-point density has convergence half-line \(z>-\gamma\).

## Proof
Write \(q=q_\mu\) and \(r=q_{F(\mu)}\), defined and strictly positive on the common Laplace convergence half-line. The two-cycle hypothesis gives the simultaneous differential identities
\[
q'=-qr,\qquad r'=-rq.
\]
Consequently \((q-r)'=0\), so \(q-r=c\) for one constant \(c\in\mathbb R\). Uniqueness of the Laplace transform also identifies the signed measure relation \(\mu-F(\mu)=c\delta_0\). This identity is a **necessary condition for every exact two-cycle**, rather than an imposed shift ansatz.

If \(c=0\), the equations reduce to \(q'=-q^2\). All positive solutions are \(q(z)=1/(z+\gamma)\) on \(z>-\gamma\), with \(\gamma\in\mathbb R\). Uniqueness of Laplace transforms gives the density \(e^{-\gamma x}\), and direct differentiation verifies it is fixed by \(F\).

If \(c=a>0\), eliminate \(r=q-a\) to obtain \(q'=-q(q-a)\). Every positive solution has the form
\[
q(z)=\frac{a}{1-t e^{-az}},\qquad
r(z)=\frac{at e^{-az}}{1-t e^{-az}}
\]
for an integration constant \(t\). The strict positivity of \(r\) for all sufficiently large real \(z\) forces \(t>0\); the possibility \(t=0\) would give \(r\equiv0\), outside the domain of a two-cycle. On \(z>\log(t)/a\), expand the positive geometric series:
\[
q(z)=a\sum_{j\ge0} t^j e^{-jaz},\qquad
r(z)=a\sum_{j\ge1} t^j e^{-jaz}.
\]
Thus \(\mu=\mu_{a,t}\) and \(F(\mu)=\nu_{a,t}\) by Laplace uniqueness. If \(c=-a<0\), exchange \(q\) and \(r\) and apply the preceding argument. There are no other cases.

For the converse, on the common half-line use the two displayed rational transforms and differentiate to check exactly
\[
-\frac{q'}q=r,\qquad-\frac{r'}r=q.
\]
Both are transforms of the stated positive measures; their convergence abscissae coincide, so they satisfy the full definition of \(F\) in both directions.

Finally, the two total masses, when finite, are \(a/(1-t)\) and \(at/(1-t)\), for \(0<t<1\). Their difference is \(a>0\), so they cannot both equal one; the only probability fixed point occurs at \(\gamma=1\). Requiring \(\mu_{a,t}\) to have mass one forces \(t=1-a\), with \(0<a<1\). Requiring \(\nu_{a,t}\) to have mass one forces \(t=(1+a)^{-1}\), with \(a>0\), proving the two probability families. For \(t\ge1\), the measures have infinite total mass and cannot be probabilities; this does not affect their validity as positive Laplace-finite measures.

## Verification
The decisive identities are analytical: the equal derivatives force a transform difference constant, and a solvable first-order Riccati equation determines every possible positive Laplace transform. Positivity of both transforms removes the inadmissible integration-constant signs; exact geometric expansions and Laplace uniqueness finish the classification. The converse checks both derivatives and the equality of Laplace abscissae, not just a formal recurrence.

The accompanying `verify.py` checks the rational differential identities and finite truncation-tail formulas using exact rational arithmetic over a range of test parameters. These checks are independent consistency diagnostics; finite tests are not the proof of the universal classification.

To reproduce, run `python3 verify.py` using Python 3 without third-party packages.

## Relationship to prior work
Grabchak (2026), Section 3, defines the positive chainability map, classifies a **different** functional relation \(F(\mu)=\lambda^{-1}\mu*\delta_b\) (Theorem 1), and explicitly constructs eventually alternating geometric examples (Corollary 2). The present statement proves the missing converse: **every** measure satisfying the unconstrained exact-cycle identity \(F^2(\mu)=\mu\) belongs to the exponential/geometric families. The necessary zero-atom difference and the exact list of probability initial measures do not follow from an example construction alone. The previously published fixed-point classification is retained as prior work, not claimed as new.

Bar-Lev and Letac (2025) and Bar-Lev (2023) discuss chainability using the **second** logarithmic derivative on real-line measures, rather than this **first** logarithmic derivative on the positive half-line. Their framework is related but a same-map implication is not established by the material inspected. Other fixed-point results for equilibrium transforms concern distinct operations.

## Limitations
The classification is for exact period dividing two, not a theorem about all longer periods, transient behavior, attraction or eventual periodicity. General measures can be sigma-finite rather than probabilities. The converse may be implicit in older work on transform differential equations not located by the literature search; complete historical priority is not certified. The 2025 related paper was available only in abstract form during this comparison, so its full text was not ruled out. No independent audit has been performed.

## References
1. M. Grabchak, “On Size-Biased Distributions and the Chainability of Positive Infinitely Divisible Distributions,” arXiv:2611.11109v1, first publicly posted 8 November 2026, especially Sections 2–3, Theorem 1 and Corollary 2. https://arxiv.org/html/2611.11109v1
2. S. K. Bar-Lev and G. Letac, “Chainability of infinitely divisible measures,” *Statistics & Probability Letters* **216** (2025), 110256. DOI:10.1016/j.spl.2024.110256.
3. S. K. Bar-Lev, “The Exponential Dispersion Model Generated by the Landau Distribution—A Comprehensive Review and Further Developments,” *Mathematics* **11** (2023), 4343, Section 4.7. https://doi.org/10.3390/math11204343
