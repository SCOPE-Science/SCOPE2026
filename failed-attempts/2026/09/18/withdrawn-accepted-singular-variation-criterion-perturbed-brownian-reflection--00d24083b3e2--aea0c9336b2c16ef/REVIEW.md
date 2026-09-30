# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The result starts from the standard two-dimensional orthant reduction used for the \(\nu<1/2\) case of Wang (2026). For
\[
R=\begin{pmatrix}1&\nu/(1-\nu)\\-1&1\end{pmatrix},
\]
the spectral radius of \(|I-R|\) is \(\sqrt{|\nu/(1-\nu)|}<1\) exactly for \(\nu<1/2\). The classical Skorokhod theorem therefore supplies a unique adapted solution for the continuous driver \((x+B-b,-B)\). Adding coordinates and applying the one-dimensional Skorokhod lemma recovers
\[
V/(1-\nu)=M(W)-x
\]
and the scalar regulator equation for \(W\).

The local-time defect calculation was checked directly. With \(X=W-b\ge0\),
\[
dX=dB+\nu\,dM+dK-db,\qquad \langle X\rangle_t=t.
\]
The occupation-density formula gives zero Lebesgue measure to \(\{X=0\}\) and makes the Brownian stochastic integral over that set vanish. Tanaka's formula then yields
\[
K-L^0(X)/2=A-\nu J
\]
with the two contact Stieltjes terms stated in `RESULT.md`.

The reduction to singular boundary variation is also exact. For
\(F=M(W)-b\ge0\), a continuous finite-variation process, the finite-variation Tanaka identity gives
\({\bf1}_{\{F=0\}}dF=0\), hence
\({\bf1}_{\{F=0\}}dM={\bf1}_{\{F=0\}}db\).
Because \(dM\) is supported on \(\{W=M\}\), any contribution of \(dM\) on
\(\{W=b\}\) lies at \(M=W=b\). Both relevant contact sets are Lebesgue-null,
so the absolutely continuous component of \(db\) contributes zero. This proves the locally absolutely continuous corollary.

For increasing \(b\), the two contact masses satisfy \(0\le J\le A\).
The equation \(K=L^0/2\) is therefore equivalent to \(A=\nu J\), which for
every \(\nu<1/2\) forces \(A=J=0\); conversely \(A=0\) gives the desired
local-time identity. Any solution of the original equation induces the same
orthant Skorokhod solution, so pathwise uniqueness follows from uniqueness of
the Skorokhod problem.

The example \(b_\alpha(t)=\min\{t^\alpha,1\}\) was checked separately:
it is absolutely continuous, globally \(\alpha\)-Hölder, has total variation
one, and violates the \(o(\sqrt h)\) upward-modulus condition for every
\(\alpha\le1/2\).

## Originality

Wang (2026), arXiv:2609.20491, is the closest source. It proves strong
existence and pathwise uniqueness under the upward-modulus condition
\(\omega^+_{b,T}(h)=o(\sqrt h)\), treats the \(\nu<1/2\) case through the
orthant Skorokhod problem, proves that a genuine solution with an increasing
boundary has \(db\)-null contact set, and constructs singular
\(\alpha\)-Hölder nonexistence examples for every \(\alpha<1/2\).

The present claim does not treat the orthant reduction, the spectral-radius
criterion, Tanaka's formula, or Wang's singular counterexamples as new. The
new statement is the combination into an exact regulator/local-time defect
identity for arbitrary continuous finite-variation boundaries in the
subcritical regime, the observation that the defect is supported entirely on
the singular Stieltjes component, the resulting iff contact criterion for
increasing boundaries, and the consequent well-posedness of every locally
absolutely continuous boundary without the Brownian-scale modulus assumption.

Targeted searches using the formulations "perturbed Brownian motion",
"time-dependent boundary", "absolutely continuous boundary", "singular
variation", "contact set", and "Skorokhod regulator local time" located
Wang's new paper and classical orthant/reflected-diffusion sources, but no
statement of this criterion or the locally absolutely continuous corollary.
The assessment is therefore **to the best of our knowledge**, not a claim of
exhaustive coverage.

The principal residual originality risk is that the corollary may be
extractable implicitly from standard reflected-semimartingale theory or from
an uninspected specialization of the older orthant literature. Williams
(1995) supplies the Skorokhod theorem used here, while Doney--Zhang (2005)
treat a related perturbed Skorokhod equation at a fixed reflecting level.
Neither inspected statement addresses the moving-boundary singular-variation
criterion. Because Wang's paper appeared only recently, later work may also
independently record the same observation.

## Value

The result changes the interpretation of the regularity threshold in the
new time-dependent-boundary problem. In the entire \(\nu<1/2\) regime,
absolute continuity of the boundary Stieltjes measure is sufficient even
when the boundary rises much faster than the Brownian \(\sqrt h\) scale.
The critical example \(b(t)=\min\{\sqrt t,1\}\) and all
\(b(t)=\min\{t^\alpha,1\}\), \(0<\alpha<1/2\), are therefore strongly
well posed although they fall outside Wang's positive theorem.

Combined with Wang's singular counterexamples, this gives a sharp
mechanistic distinction: for every fixed \(\alpha<1/2\), two increasing
globally \(\alpha\)-Hölder boundaries with the same total variation can have
opposite solvability behavior. Hölder exponent alone cannot classify the
problem; in the subcritical regime the obstruction is singular boundary
variation charged by the contact set.

## Limitations

The automatic well-posedness result is restricted to \(\nu<1/2\).
For \(\nu\ge1/2\), the associated regulator problem is not covered by the
subcritical spectral-radius theorem, so the defect identity by itself does
not establish existence.

For singular increasing boundaries, the iff condition still depends on the
contact set of the Skorokhod candidate and is therefore not an explicit
deterministic condition on \(b\) alone. Absolute continuity is sufficient,
not claimed necessary. The critical \(1/2\)-Hölder class is not fully
classified.
