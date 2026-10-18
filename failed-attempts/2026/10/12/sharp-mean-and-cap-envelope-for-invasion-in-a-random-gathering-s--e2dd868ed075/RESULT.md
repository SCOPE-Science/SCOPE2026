# Sharp mean-and-cap envelope for invasion in a random-gathering SIR model

## Finding

Cortez's random-gathering SIR model has
\[
\mathcal R_0
=
\frac{\mu p}{\gamma}\,
\mathbb E[\Theta(\Theta-1)].
\]
Write
\[
C=\frac{\mu p}{\gamma}>0.
\]

Fix an integer gathering cap
\[
K\ge2
\]
and a mean gathering size
\[
m=\mathbb E[\Theta]\in(1,K].
\]
Assume, as allowed in the source, that
\[
\Theta\in\{0,1,\ldots,K\}.
\]
Let
\[
k=\lfloor m\rfloor,\qquad \delta=m-k\in[0,1).
\]

Then the complete attainable interval of reproduction numbers among all such gathering-size distributions is
\[
\boxed{
C\bigl(k(k-1)+2k\delta\bigr)
\le
\mathcal R_0
\le
C\,m(K-1)
}.
\]

The lower endpoint is attained by the least-dispersed integer law
\[
\mathbb P(\Theta=k)=1-\delta,
\qquad
\mathbb P(\Theta=k+1)=\delta.
\]
When \(m\) is an integer this reduces to the deterministic law
\[
\Theta\equiv m.
\]

The upper endpoint is attained by the maximally dispersed endpoint law
\[
\mathbb P(\Theta=K)=\frac mK,
\qquad
\mathbb P(\Theta=0)=1-\frac mK.
\]

Every value between the endpoints is attainable: any convex mixture of the two extremizing laws has the same mean \(m\), the same cap \(K\), and interpolates linearly between their factorial second moments.

This gives exact robust threshold tests. If
\[
C\,m(K-1)\le1,
\]
then every gathering-size law with that mean and cap satisfies
\[
\mathcal R_0\le1.
\]
If
\[
C\bigl(k(k-1)+2k\delta\bigr)>1,
\]
then every such law satisfies
\[
\mathcal R_0>1.
\]
If
\[
C\bigl(k(k-1)+2k\delta\bigr)<1<C\,m(K-1),
\]
then there are two laws with the same mean and the same legal cap for which one is subcritical and the other is supercritical.

A concrete certificate is
\[
K=10,\qquad m=3,\qquad C=\frac1{10}.
\]
The deterministic law
\[
\Theta\equiv3
\]
has
\[
\mathcal R_0=\frac35<1,
\]
whereas
\[
\mathbb P(\Theta=10)=\frac3{10},
\qquad
\mathbb P(\Theta=0)=\frac7{10}
\]
has the same mean and cap but
\[
\mathcal R_0=\frac{27}{10}>1.
\]

There is also no finite upper bound at fixed mean if no gathering cap is imposed. For any fixed
\[
m>1,
\]
letting
\[
\mathbb P(\Theta=L)=\frac mL,
\qquad
\mathbb P(\Theta=0)=1-\frac mL
\]
gives
\[
\mathcal R_0=Cm(L-1)\to\infty
\]
as the integer \(L\to\infty\).

## Assumptions and scope

The model is exactly the random-gathering SIR model of the source. Gatherings occur at rate \(\mu>0\), transmission succeeds independently with probability \(p>0\) per infectious contact, and infected individuals recover at rate \(\gamma>0\).

The source permits
\[
\Theta\in\{0,1,2,\ldots\}
\]
and explicitly discusses policies for which the distribution is supported on
\[
\{0,1,\ldots,K\}.
\]
The restriction
\[
m>1
\]
keeps the theorem within the source's nontrivial epidemic regime
\[
\mathbb P(\Theta\ge2)>0.
\]

The theorem is an extremal statement about the invasion number. It does not assert that real gathering-size distributions attain either extremizer, and it does not optimize social welfare or compliance responses to a legal cap.

## Proof

The source gives
\[
\mathcal R_0=C\,\mathbb E[\Theta(\Theta-1)].
\]
First,
\[
\mathbb E[\Theta(\Theta-1)]
=
\mathbb E[\Theta^2]-m
=
\operatorname{Var}(\Theta)+m^2-m.
\]
Thus, at fixed mean, \(\mathcal R_0\) is an affine increasing function of the gathering-size variance.

For the lower bound, put
\[
k=\lfloor m\rfloor.
\]
For every integer \(n\),
\[
(n-k)(n-k-1)\ge0.
\]
Expanding gives
\[
n(n-1)\ge2kn-k(k+1).
\]
Taking expectations yields
\[
\mathbb E[\Theta(\Theta-1)]
\ge
2km-k(k+1).
\]
Writing \(m=k+\delta\) gives
\[
2km-k(k+1)
=
k(k-1)+2k\delta.
\]
Equality in the pointwise inequality is possible only at
\[
n=k
\quad\text{or}\quad
n=k+1.
\]
The stated adjacent two-point distribution has mean \(m\), so it attains the lower bound.

For the upper bound, every integer
\[
0\le n\le K
\]
satisfies
\[
n(n-1)\le(K-1)n,
\]
because
\[
n(K-n)\ge0.
\]
Therefore
\[
\mathbb E[\Theta(\Theta-1)]
\le
(K-1)m.
\]
Equality is possible only at the endpoints
\[
n=0
\quad\text{or}\quad
n=K.
\]
The law with mass \(m/K\) at \(K\) and the remaining mass at zero has mean \(m\), so it attains the upper bound.

The set of probability laws with a fixed mean is convex, and the factorial moment is linear in the law. Convex mixtures of the lower and upper extremizers therefore realize every value in the displayed interval.

Finally, if no finite cap is imposed, for every integer \(L\ge m\) the two-point law
\[
\mathbb P(\Theta=L)=\frac mL,
\qquad
\mathbb P(\Theta=0)=1-\frac mL
\]
has mean \(m\) and
\[
\mathbb E[\Theta(\Theta-1)]
=
m(L-1).
\]
This diverges with \(L\), proving the unboundedness claim.

## Verification

The proof is exact and finite-dimensional.

The accompanying verifier checks the two pointwise inequalities for a range of integer caps, constructs both extremizing distributions using exact rational arithmetic, verifies their means and factorial moments, checks convex interpolation, and replays the explicit
\[
K=10,\quad m=3,\quad C=\frac1{10}
\]
threshold-separation certificate.

The computation is corroborative only; the universal bounds follow from the two pointwise integer inequalities proved above.

## Relationship to prior work

Cortez derives the general random-gathering force of infection
\[
B(i)=
\mathbb E\!\left[
\Theta\left(1-(1-pi)^{\Theta-1}\right)
\right]
\]
and the resulting reproduction number
\[
\mathcal R_0
=
\frac{\mu p}{\gamma}
\mathbb E[\Theta(\Theta-1)].
\]
The article explicitly notes that a gathering-size restriction can be represented by support on
\[
\{0,\ldots,K\},
\]
then analyzes fixed, binomial, Poisson, and logarithmic examples and observes quadratic growth with mean gathering size in those examples. It does not state the sharp fixed-mean, fixed-cap envelope above.

Boyer, Rumpler, Kissler, and Lipsitch independently model gathering-size restrictions and emphasize that the distribution of gathering sizes is a key determinant of intervention effects. Their model computes expected incident cases by averaging a size-dependent infection expression against the gathering-size distribution; for small transmission prevalence it has an approximately quadratic size law. This strongly motivates distribution-sensitive policy analysis, but it is a different model and does not give the exact factorial-moment invasion envelope for the Cortez SIR system.

Searches using the source title and identifier, factorial-second-moment terminology, variance formulations, fixed-mean gathering-size constraints, and sharp cap bounds did not locate a published statement of this exact classification.

## Limitations

The endpoint maximizer uses size-zero gatherings because the source explicitly permits \(\Theta=0\). If a separate application insists that every gathering be nonempty, the sharp upper extremizer and its formula change and should be recomputed under that additional support constraint.

The theorem concerns \(\mathcal R_0\), not the complete nonlinear epidemic trajectory. Two gathering laws with the same reproduction number can still produce different nonlinear incidence functions.

The unbounded fixed-mean statement assumes no finite cap. Real populations and venues necessarily impose physical bounds, so its role is to show that the mean alone is mathematically insufficient rather than to claim literal infinite gathering sizes.

The literature search cannot exclude an equivalent extremal-moment statement under substantially different terminology.

## References

1. R. Cortez, “SIR model with social gatherings,” Journal of Applied Probability 61 (2024), 667–684. arXiv:2203.08260. DOI: 10.1017/jpr.2023.65.
2. C. B. Boyer, E. Rumpler, S. M. Kissler, M. Lipsitch, “Infectious disease dynamics and restrictions on social gathering size,” Epidemics 40 (2022), 100620. DOI: 10.1016/j.epidem.2022.100620.
