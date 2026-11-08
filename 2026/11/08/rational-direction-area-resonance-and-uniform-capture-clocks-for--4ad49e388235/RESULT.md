# Rational-direction area resonance and uniform capture clocks for a one-sided two-square flow

## Finding

The two-square, one-sided-barrier flow of Beck, Chen, and Yang has an explicit rational-direction recurrent-area law and, below a rational denominator threshold, an exactly uniform transient capture-time distribution. These results concern the same noninvertible barrier mechanism as the previously studied irrational-direction model.

**Theorem (rational resonance and capture).** Fix a circle interval \(B=(a,a+b)\subset\mathbb R/\mathbb Z\), with \(0\le a<a+b\le1\) and \(0<b<1\). For \(\alpha=p/q>0\) in lowest terms, with positive coprime integers \(p,q\), define the discrete unit-horizontal-advance return map on \(X=[0,1)\times(\mathbb R/\mathbb Z)\times\{0,1\}\) by

\[
F_\alpha(r,u,s)=\bigl(r,u+\alpha\pmod1,\sigma(s,u+\alpha)\bigr),\qquad
\sigma(s,v)=\begin{cases}0,&s=1\text{ or }v\in B,\\1,&s=0\text{ and }v\notin B.\end{cases}
\]

Here \(r\) is fractional horizontal position, \(u\) is vertical phase relative to the horizontal passage coordinate, and \(s\) selects one of the two squares. The area measure is Lebesgue in \(r,u\), summed over both sheets, of total mass \(2\). Barrier-endpoint conventions are immaterial to all area statements.

For every integer \(n\ge1\), with \(|\cdot|\) denoting length modulo \(1\),

\[
\operatorname{area}(F_\alpha^n X)=2-\left|\bigcup_{j=0}^{n-1}(B+j\alpha)\right|.
\]

In particular, the recurrent/nonwandering region, up to a null boundary set, has area

\[
\boxed{\operatorname{area}(\mathcal R_\alpha)=2-\min\{1,qb\}},\qquad
\boxed{\operatorname{area}(\mathcal W_\alpha)=\min\{1,qb\}}.
\]

Every point of the recurrent region outside barrier-boundary orbits is periodic under the unit-advance map, of period dividing \(2q\). Every transient point joins the recurrent periodic region after at most \(q\) advances.

When \(qb<1\), let \(\tau\in\{1,\ldots,q\}\) be the first passage count when a transient orbit joins the recurrent periodic region. The exact unnormalized area at each capture time is

\[
\boxed{\operatorname{area}\{x\in\mathcal W_\alpha:\tau(x)=j\}=b\quad(1\le j\le q)},
\]

and hence under normalized area conditioned on the transient region,

\[
\boxed{\mathbb P(\tau=j\mid\mathcal W_\alpha)=1/q\quad(1\le j\le q)}.
\]

Consequently, \(\operatorname{area}(F_\alpha^n X)=2-nb\) for \(0\le n\le q\), and equals \(2-qb\) thereafter. The area excess over the irrational-direction recurrent area of \(1\) is precisely \((1-qb)_+\). Thus rational directions with denominator \(q<1/b\) are exactly the resonant directions having recurrent area greater than \(1\).

## Assumptions and scope

The model is the two adjacent unit squares with horizontal identifications, vertical coordinate modulo \(1\), and a one-sided barrier on the vertical seam between the squares. Motion is to the right at positive slope \(\alpha\). On hitting the barrier from the left, the orbit restarts at the left outer edge at the same height; if the barrier is missed, the orbit passes to the right-hand square. Passing the far-right edge returns to the left square. This is the usual two-square construction with a noninvertible seam. The horizontal unit-advance map is a Poincaré description, with vertical phase \(u=y-\alpha r\pmod1\) at fractional horizontal coordinate \(r\), and it preserves planar area elements before sheets coalesce. For \(\alpha=p/q\), the base phase has exact period \(q\). All topological periodicity/nonwandering descriptions are asserted away from the finite union of barrier-endpoint orbit lines, which has area zero; area identities hold independently of endpoint conventions.

The integer \(n\) denotes horizontal unit crossings, not Euclidean arclength or arbitrary continuous time. The capture clock refers to joining the invariant set of periodic points, not simply the first crossing of the seam. The interval \(B\) can be translated within the seam with no change to any formula.

## Proof

**Step 1: One-step reduction.** At the next vertical seam, the phase increases by \(\alpha\) modulo \(1\). A right-square start necessarily wraps to sheet \(0\); a left-square start goes to sheet \(1\) if the barrier is missed and instead restarts on sheet \(0\) when the barrier is hit. This is exactly the formula for \(F_\alpha\). For any fixed phase \(v\notin B\), its sheet map \(s\mapsto1-s\) is a bijection of \(\{0,1\}\). For \(v\in B\), both sheet labels map to \(0\). Thus barrier encounters coalesce the two possible sheet histories, and later evolution cannot separate them.

**Step 2: Every finite-time image.** Fix target phase \(u\) and a number \(n\ge1\). Because the base rotation is bijective, it has exactly one phase ancestor \(u-n\alpha\). If the intervening phases \(u-(n-1)\alpha,\ldots,u\) avoid \(B\), both original sheet choices survive and yield the two distinct target sheet labels. If any of these phases visits \(B\), the two histories coalesce and the target phase has exactly one sheet label in the image. The subset of target phases with an encounter is \(\bigcup_{j=0}^{n-1}(B+j\alpha)\), as can be seen by writing the earliest target-backward position as \(u-j\alpha\in B\). Each phase fiber contributes either area \(2\) or area \(1\) per unit \(r\), proving the finite-time image formula.

**Step 3: The periodic recurrent set.** The base rotation has period \(q\), so the sets of phases visited over any full block of \(q\) steps coincide. Let \(U=\bigcup_{j=0}^{q-1}(B+j\alpha)\). At a phase outside \(U\), both sheet labels are possible, and no barrier is visited in either direction of the phase cycle. Therefore the return after \(q\) steps either preserves each sheet or exchanges the pair, and every such point has period dividing \(2q\). At a phase in \(U\), at least one barrier encounter occurs in each cycle of \(q\) steps. The composition of its sheet maps over that cycle is a constant map; it has precisely one fixed sheet label, and any initial label is mapped to it. This unique label is periodic with period dividing \(q\). Hence every point of the stable image \(F_\alpha^q X\), away from boundary orbits, is periodic, and each point not in that image joins it by step \(q\).

A periodic point is nonwandering. Conversely, a point outside the stable image and off its boundary has an open neighborhood disjoint from the stable image. All sufficiently long images of that neighborhood lie in the stable image, so it is wandering. Thus recurrent and transient regions agree with the stable image and its complement up to a null boundary set.

**Step 4: Arithmetic union measure.** Since \(p\) and \(q\) are coprime, the set of shifts \(j\alpha\pmod1\) is the equally spaced grid \(\{0,1/q,\ldots,(q-1)/q\}\). The translated intervals have uniform starting-point gaps \(1/q\). If \(b\le1/q\), they are disjoint up to endpoints and their union has length \(qb\). If \(b\ge1/q\), adjacent intervals overlap or touch and cover the circle, so the union length is \(1\). This proves the two area formulas and identifies the rational denominator resonance criterion.

**Step 5: Uniform capture clocks.** Assume \(qb<1\). The sets \(B-j\alpha\) for \(j=1,\ldots,q\) are disjoint modulo endpoints and each has phase length \(b\). Every phase in their union supports precisely one periodic sheet and one transient sheet. For transient initial phase \(u\), the first coalescence occurs exactly at the first \(j\) such that \(u+j\alpha\in B\); before that encounter the sheet update is a bijective toggle, so the transient and periodic sheet histories remain distinct, and after it they coincide forever. Consequently \(\tau=j\) holds on one sheet over \(B-j\alpha\), of area exactly \(b\). The transient region has total area \(qb\), so conditioning gives the discrete uniform distribution. For \(0\le n\le q\), the \(n\) shifted barrier intervals have disjoint interiors and total length \(nb\), yielding the finite-time image-volume law. For \(n\ge q\), the phase union has stabilized.

**Step 6: Comparison with irrational directions.** The irrational-direction recurrent area \(1\) is Theorem 1 of the cited originating paper. The rational formula differs by \(1-\min\{1,qb\}=(1-qb)_+\). This comparison uses the originating theorem rather than attempting a new proof for irrational directions. No statement of continuous parameter continuity is implied; the rational resonance depends on reduced denominator.

## Verification

The standalone exact-rational checker `checker.py` independently evaluates the phase interval decomposition using `fractions.Fraction` and confirms the periodic and transient sheet classification, arithmetic union measure, finite-time coalescence, and conditional hitting-time weights. It passed \(2444\) rational-angle/barrier combinations and \(57908\) exact rational phase strata. The tested denominators range from \(1\) to \(18\), including rational slopes above \(1\), barrier translations, both disjoint and overlapping regimes. All universal claims follow from the preceding proof; the finite checker is independent stress testing, not an exhaustive infinite certificate.

## Relationship to prior work

Beck, Chen, and Yang [1] formulate the noninvertible two-square one-sided-barrier model and establish its recurrent area \(1\) for **irrational** slopes. The present statement changes the slope arithmetic and computes the complete rational recurrent-area spectrum plus the exact first-capture distribution, which are not consequences of the irrational theorem alone. Beck, Chen, and Yang [2] examine symmetric, invertible two-circle gates and rotation arithmetic, rather than the coalescing one-way barrier used here. General elementary circle-rotation facts, including the rational grid and disjoint translates, are standard and not claimed as novel by themselves; the contribution is their exact dynamical manifestation as area resonance and uniform capture in this dissipative flow.

## Limitations

The theorem is restricted to a **single connected barrier interval** and to the special two-square mechanism; arbitrary collections of barrier intervals and other square-tiled surfaces require separate analysis. The area and almost-everywhere classifications exclude finitely many barrier-endpoint orbit lines where endpoint conventions may alter pointwise classifications. Time counts horizontal unit advances. An equivalent formulation in unindexed literature remains possible. No independent mathematical audit has been performed.

## References

[1] J. Beck, W. W. L. Chen, and Y. Yang, *Irreversible and dissipative systems*, arXiv:2404.00078, first publicly posted 2024-03-29; Section 2 and Theorem 1. https://arxiv.org/abs/2404.00078

[2] J. Beck, W. W. L. Chen, and Y. Yang, *New Kronecker-Weyl type equidistribution results and diophantine approximation*, arXiv:2106.14001, first publicly posted 2021-06-26; two-circle symmetric-gate model. https://arxiv.org/abs/2106.14001
