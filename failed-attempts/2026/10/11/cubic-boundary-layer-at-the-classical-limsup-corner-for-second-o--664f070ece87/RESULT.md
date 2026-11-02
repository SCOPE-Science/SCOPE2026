# Cubic boundary layer at the classical limsup corner for second-order delay oscillation
## Finding
Consider the normalized second-order delay equation
\[
x''(t)=x(\tau(t)),
\]
where \(\tau\) is nondecreasing, \(\tau(t)\le t\), and \(\tau(t)\to\infty\). Put
\[
a=\liminf_{t\to\infty}(t-\tau(t)),\qquad
b=\limsup_{t\to\infty}(t-\tau(t)).
\]
For the sharp boundary \(b=\beta(a)\) introduced for this problem in arXiv:2609.31732v1, the classical corner \(a=0\), \(\beta(0)=\sqrt2\), has cubic rather than linear or quadratic contact:
\[
\beta(a)=\sqrt2-\frac{a^3}{3}-\frac{\sqrt2}{24}a^4+O(a^5)
\qquad (a\downarrow0).
\]
In particular,
\[
\beta'(0)=\beta''(0)=0,\qquad \beta'''(0)=-2,
\qquad
\lim_{a\downarrow0}\frac{\sqrt2-\beta(a)}{a^3}=\frac13.
\]

This coefficient gives a sharp boundary-layer selection rule. For any fixed real \(\kappa\) and any family
\[
b(a)=\sqrt2-\kappa a^3+o(a^3),
\]
one has, for all sufficiently small positive \(a\),

- if \(\kappa<1/3\), then \(b(a)>\beta(a)\), so the source's sharp theorem excludes an eventually positive decreasing solution;
- if \(\kappa>1/3\), then \(b(a)<\beta(a)\), and the source's sharpness construction supplies a nondecreasing delay with these limiting delay data and a strictly positive decreasing solution.

Thus \(1/3\) is the exact cubic-scale transition coefficient near the classical \(\limsup\) corner.

## Assumptions and scope
The statement uses the normalized problem and the same monotonicity assumptions on \(\tau\) as arXiv:2609.31732v1. Only the limit \(a\downarrow0\) is considered. The coefficient \(\kappa\) in the scaled family is fixed, and the conclusion for \(\kappa>1/3\) invokes the source's existence theorem for data satisfying \(a\le b\le\beta(a)\); this inequality is automatic for sufficiently small positive \(a\) in the displayed scaling.

The source describes the small-\(a\) branch by two positive spectral coordinates \(r=r(a)\) and \(s=s(a)\) satisfying
\[
r^2=e^{ar},\qquad s^2=e^{-as},
\]
and, with
\[
d=\frac1s-\frac1r,
\]
gives the explicit boundary formula
\[
\beta(a)=2a-2d+\sqrt{2d^2+\frac4{rs}-2}
\]
on a neighborhood of \(a=0\).

## Proof
The spectral equations can be solved on their principal analytic branches by
\[
r(a)=-\frac{2}{a}W_0\!\left(-\frac a2\right),
\qquad
s(a)=\frac{2}{a}W_0\!\left(\frac a2\right),
\]
where \(W_0\) is the principal Lambert \(W\) function. Since \(W_0\) is analytic at \(0\), its Taylor series gives
\[
r(a)=1+\frac a2+\frac{3a^2}{8}+\frac{a^3}{3}
+\frac{125a^4}{384}+O(a^5),
\]
\[
s(a)=1-\frac a2+\frac{3a^2}{8}-\frac{a^3}{3}
+\frac{125a^4}{384}+O(a^5).
\]
Series inversion and multiplication then yield
\[
d=a+\frac{a^3}{6}+O(a^5),
\qquad
rs=1+\frac{a^2}{2}+\frac{11a^4}{24}+O(a^6),
\]
and hence
\[
\frac1{rs}=1-\frac{a^2}{2}-\frac{5a^4}{24}+O(a^6).
\]
Therefore
\[
2a-2d=-\frac{a^3}{3}+O(a^5)
\]
and
\[
2d^2+\frac4{rs}-2
=2-\frac{a^4}{6}+O(a^6).
\]
Taking the positive square root,
\[
\sqrt{2d^2+\frac4{rs}-2}
=\sqrt2-\frac{\sqrt2}{24}a^4+O(a^6).
\]
Substitution into the source formula proves
\[
\beta(a)=\sqrt2-\frac{a^3}{3}-\frac{\sqrt2}{24}a^4+O(a^5).
\]

For
\[
b(a)=\sqrt2-\kappa a^3+o(a^3),
\]
subtracting the boundary expansion gives
\[
b(a)-\beta(a)=\left(\frac13-\kappa\right)a^3+o(a^3).
\]
Its sign is therefore positive for fixed \(\kappa<1/3\) and negative for fixed \(\kappa>1/3\). The two alternatives now follow directly from the necessity and sharpness parts of the source theorem.

## Verification
The algebraic series identities needed above are independently replayed by `verify_series.py` using exact rational arithmetic. The script verifies the defining spectral equations through the required order and recomputes
\[
d=a+\frac{a^3}{6}+O(a^5),\qquad
\frac1{rs}=1-\frac{a^2}{2}-\frac{5a^4}{24}+O(a^6),
\]
as well as
\[
2d^2+\frac4{rs}-2=2-\frac{a^4}{6}+O(a^6).
\]
The proof itself is analytic and does not infer an infinite statement from finite numerical sampling.

## Relationship to prior work
arXiv:2609.31732v1 establishes the sharp boundary \(b\le\beta(a)\), proves \(\beta(0)=\sqrt2\), gives the small-\(a\) explicit formula used here, and proves sharpness by constructing a positive decreasing solution for every admissible pair below the boundary. It states continuity and strict monotonicity of \(\beta\), but the endpoint cubic contact and the scaled coefficient \(1/3\) are not stated there.

Pituk, I. P. Stavroulakis, and J. I. Stavroulakis obtained explicit Lambert-\(W\) formulas for a different, first-order monotone-delay oscillation-bound problem. That work motivates the spectral parameterization but does not imply the second-order boundary expansion above. Earlier surveys and second-order oscillation criteria use different coefficient-weighted or sign conventions and do not provide this sharp \((a,b)\) boundary.

## Limitations
This is a local result at \(a=0\). It does not describe the interior branch transition of \(\beta\), the endpoint \(a=2/e\), or nonmonotone delay arguments. At the critical cubic scaling \(\kappa=1/3\), the cubic term alone is inconclusive; the displayed quartic term or finer information about \(b(a)\) must be used. The literature search cannot exclude an equivalent unpublished or differently indexed endpoint calculation.

## References
1. J. I. Stavroulakis, *Oscillation of Second-Order Delay Equations with Positive Feedback*, arXiv:2609.31732v1, 2026.
2. M. Pituk, I. P. Stavroulakis, and J. I. Stavroulakis, *Explicit values of the oscillation bounds for linear delay differential equations with monotone argument*, Communications in Contemporary Mathematics 25 (2023), 2150087, DOI: 10.1142/S0219199721500875.
