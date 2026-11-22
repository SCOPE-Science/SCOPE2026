# Sharp finite-capture versus ballistic-escape boundary for critical affine resets of two linear centers

## Finding

Consider a planar hybrid system whose left and right half-planes carry arbitrary linear-center vector fields, with switching section \(\Sigma=\{x=0\}\) and the same affine reset \(\varphi(y)=ay+b\) at every section encounter. Suppose \(|a|=1\). For the complete section-return map \(P:\mathbb R\to\mathbb R\) defined by the flow-or-reset convention below, there is an explicit scalar \(\Delta\) with the following **sharp exhaustive dichotomy**.

* If \(\Delta\leq0\), **every** section point enters an exact periodic orbit after finitely many returns, of least period one or two.
* If \(\Delta>0\), **every** section orbit escapes, and after finitely many returns it follows an exact arithmetic progression \(P^{n+1}(y)-P^n(y)=\sigma\Delta\), where \(\sigma\in\{-1,1\}\) is explicitly determined by the right-hand center and reset sign.

In the fixed-point regime, every invariant Borel probability of \(P\) is a mixture of uniform probabilities on its one- and two-cycles; in the escape regime no invariant Borel probability exists. A simple parameter choice exhibits an entire interval of primitive two-cycles, showing that the period-two alternative is necessary. Statements concern section-return iterations; a zero-duration reset leg must not be reinterpreted as a positive-duration flow.

## Assumptions and scope

For \(i=1,2\), use the linear-center normal form
\[
X_i(x,y)=\left(-\beta_i x-\delta_i(4\beta_i^2+\omega_i^2)y+d_i,\quad
\delta_i x+\beta_i y+e_i\right),
\]
where \(\beta_i,d_i,e_i\in\mathbb R\), \(\delta_i\in\{-1,1\}\) and \(\omega_i\ne0\). The vector field \(X_1\) is followed only in \(x<0\), and \(X_2\) only in \(x>0\). At a section encounter, the orbit applies \(\varphi(y)=ay+b\) before trying the other half-plane; if the vector field points away from that half-plane, that flow leg has zero duration. This is the convention used for the return map of Llibre and Santana [1]. We include tangency values by the continuous formula.

Put
\[
h_i=\frac{\delta_i d_i}{4\beta_i^2+\omega_i^2},\qquad
s_1=-\delta_1,\qquad s_2=\delta_2,
\]
and define
\[
H=ah_2+b-h_1,\quad
t=as_1(ah_1+b-h_2),\quad
\sigma=as_2,\quad
\boxed{\Delta=t+\sigma H}.
\]
Here \(a,s_1,s_2,\sigma\in\{-1,1\}\). No boundedness or genericity assumptions on the center locations, reset translation, or initial section point are imposed. The flow parameters \(e_i\) affect flight times but not the section-height return formula.

## Proof

**1. Each half-flight is an exact fold.** The quadratic first integral
\[
I_i(x,y)=2e_i x-2d_i y+\delta_i x^2+2\beta_i xy
+\delta_i(4\beta_i^2+\omega_i^2)y^2
\]
has, on \(x=0\), two intersection heights \(y\) and \(2h_i-y\), counted with tangency multiplicity. The transverse component at the section is
\[
\dot x\big|_{x=0}=-\delta_i(4\beta_i^2+\omega_i^2)(y-h_i).
\]
Therefore a left half-flight is taken exactly when \(\delta_1(y-h_1)>0\); a right half-flight exactly when \(\delta_2(y-h_2)<0\). On the entry half-line, the next section crossing is \(2h_i-y\); otherwise the next leg is immediate and has unchanged height. Thus the two continuous half-flight maps are
\[
g_i(y)=h_i+s_i|y-h_i|,\qquad s_1=-\delta_1,\quad s_2=\delta_2.
\]
They are globally one-Lipschitz and piecewise isometric.

**2. An exact double-fold normal form.** Two alternating half-flights with the reset between and after them give
\[
P=\varphi\circ g_2\circ\varphi\circ g_1.
\]
Writing \(u=y-h_1\), direct substitution yields the exact conjugate
\[
\boxed{P(h_1+u)-h_1=Q(u):=H+\sigma\bigl||u|+t\bigr|.}
\]
Consequently \(Q\) is continuous, one-Lipschitz, and piecewise affine with slopes \(+1\) or \(-1\) on finitely many intervals. This formula is valid for every real \(u\), including folds.

**3. Sharp fixed-point/escape test.** Since \(Q\) is one-Lipschitz, \(Q(u)-u\) is continuous and nonincreasing. If \(\sigma=1\), its limit at \(u\to-\infty\) is \(+\infty\), while its limit at \(u\to+\infty\) is \(H+t=\Delta\). If \(\sigma=-1\), its limit at \(u\to+\infty\) is \(-\infty\), while its limit at \(u\to-\infty\) is \(H-t=-\Delta\). At \(\Delta=0\) the appropriate outer ray consists of exact fixed points. Hence a fixed point exists **if and only if** \(\Delta\le0\). If \(\Delta>0\), \(Q(u)-u\) has the strict sign \(\sigma\), so every orbit moves monotonically toward \(\sigma\infty\). A bounded monotone orbit would converge to a fixed point, which does not exist. In the eventual tail, direct evaluation of the double absolute value gives \(Q(u)=u+\sigma\Delta\), proving the exact eventual drift.

**4. Finite-time capture when a fixed point exists.** We use the following elementary lemma. If \(f:\mathbb R\to\mathbb R\) is continuous, one-Lipschitz and piecewise affine with slopes in \(\{-1,1\}\) on finitely many pieces, and \(f\) has a fixed point \(p\), then every forward orbit is eventually periodic with least period at most two. Indeed, \(r_n=|f^n(x)-p|\) is nonincreasing. Its limit is \(r\ge0\), so every accumulation point belongs to the at-most-two-point set \(\{p-r,p+r\}\). Continuity and forward invariance imply the limiting dynamics is a fixed point or a two-cycle (if both points recur, continuity forces their interchange). Along each residue class modulo its period \(q\in\{1,2\}\), the orbit tends to a corresponding point \(z\) fixed by \(f^q\). But \(f^q\) is again continuous, finitely piecewise affine with slopes \(\pm1\). In a sufficiently small neighborhood of \(z\), each adjacent affine piece passes through \((z,z)\), so \(|f^q(w)-z|=|w-z|\). A subsequence tending to \(z\) with this locally constant distance must attain \(z\) in finite time. That completes the lemma. For \(P\), nonexpansiveness relative to a fixed point gives boundedness for every initial condition, so the lemma applies.

**5. Invariant measures.** If \(\Delta>0\), every orbit eventually leaves every compact subset, whence invariance and dominated convergence force every finite invariant measure to vanish. If \(\Delta\le0\), every point is eventually periodic. Under any invariant probability, Poincaré recurrence holds almost everywhere, so almost every point is already periodic. The ergodic invariant probabilities are precisely the uniform orbit measures of one- and two-cycles; arbitrary invariant probabilities are their mixtures.

**6. Nontrivial two-cycles.** Take
\[
X_1=(-y,x),\qquad X_2=(y-\tfrac15,-x),
\qquad\varphi(y)=y+1.
\]
Here \(h_1=0\), \(s_1=-1\), \(h_2=\tfrac15\), \(s_2=-1\), and
\[
P(y)=\frac65-\left|\frac45-|y|\right|.
\]
On \([\frac45,\frac65]\), \(P(y)=2-y\). Every point in the open interval other than \(y=1\) lies on a primitive two-cycle. These are section-return cycles, including zero-duration right-hand legs, and do not contradict a restriction on *regular isolated* limit cycles.

## Verification

The standalone `CHECK.py` uses exact fractions to compare the raw composition of two half-flight folds and two resets against the double-absolute-value formula over a deterministic parameter grid. It also checks the claimed two-cycle example, the critical neutral case and exact escape translation. These are finite consistency tests; the universal assertions follow from the proof, not from enumeration. The symbolic reduction can be reconstructed directly from the four definitions in Section 2.

## Relationship to prior work

Llibre and Santana [1], Sections 2, 4–7, give the same hybrid two-center setup, a four-branch expression for its return map, results for regular limit cycles with affine resets when \(|a|\ne1\), and a chaos construction with a quadratic reset. The present claim concerns precisely the omitted critical affine case \(|a|=1\): it adds a parameter-space boundary \(\Delta=0\), a **global finite-time** return-orbit dichotomy and an exact ballistic escape velocity. These assertions do not follow from the paper's regular-cycle theorem alone. The argument does use the known elementary theory of nonexpansive interval maps, but the sharp double-fold reduction and boundary criterion are specific to this hybrid family.

Li and Liu [2] analyze impact limit cycles in related piecewise-linear hybrid systems. Their full text was not accessible in the present comparison, so priority cannot be completely resolved. Lawrence and Spingarn [3] study nonexpansive piecewise-isometric maps in a different fixed-point-iteration context; their abstract does not establish the present hybrid parameter criterion. The 2014 work on piecewise contractions [4] assumes strict branch contractions and is not a same-system result. Relevant published and indexed comparisons do not establish a dominating theorem for this precise affine-reset boundary, but lack of such evidence is not proof of absolute priority.

## Limitations

The theorem classifies **section returns**, not the physical-time distribution of flight lengths, Zeno accumulation, or arbitrary hybrid solution conventions. Critical folds are defined continuously, and the reset rule is the two-reset return construction above. No quantitative uniform upper bound on the number of transient returns is claimed; this can become arbitrarily large near \(\Delta=0\). Finite tests do not prove the full statement. The primary 2024 paper was inspected in its open full-text sections; one potentially related older hybrid-impact article and general historical literature remain incompletely accessible. Independent mathematical validation has not been performed.

## References

[1] J. Llibre and P. Santana, *Limit cycles and chaos in planar hybrid systems*, arXiv:2407.05151 (first posted 2024-07-06), https://arxiv.org/abs/2407.05151 ; later *Communications in Nonlinear Science and Numerical Simulation* **140** (2025), 108382.

[2] Z. Li and X. Liu, *Impact limit cycles in the planar piecewise linear hybrid systems*, *Communications in Nonlinear Science and Numerical Simulation* **119** (2023), 107074. DOI: https://doi.org/10.1016/j.cnsns.2022.107074.

[3] J. Lawrence and J. E. Spingarn, *On Fixed Points of Non-Expansive Piecewise Isometric Mappings*, *Proceedings of the London Mathematical Society* s3-55 (1987), 605–624. https://doi.org/10.1112/plms/s3-55.3.605.

[4] A. Nogueira, B. Pires and R. A. Rosales, *Asymptotically periodic piecewise contractions of the interval*, *Nonlinearity* **27** (2014), 1603. https://doi.org/10.1088/0951-7715/27/7/1603.
