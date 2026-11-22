# The sharp one-tangent local-oracle constant on rolling-ball convex sets

## Finding

**Theorem (sharp universal quadratic constant for the one-tangent repair).** Let \(d\ge2\), \(\rho>0\), and let \(K\subset\mathbb R^d\) be a nonempty compact convex body satisfying the interior rolling-ball property: for every \(q\in\partial K\) and outward supporting unit normal \(n\),
\[
B(q-\rho n,\rho)\subseteq K.
\]
For every \(x\in K\), \(s>0\), and \(c\in\mathbb R^d\), let \(\widehat p\) be the *exact one-tangent oracle output* defined below, with the standard tangent-ball projection repair. Then \(\widehat p\in K\cap B(x,s)\) and
\[
0\le \langle c,\widehat p\rangle-\min_{z\in K\cap B(x,s)}\langle c,z\rangle
\le \|c\|\bigl(\sqrt{\rho^2+s^2}-\rho\bigr)
\le \frac{\|c\|s^2}{2\rho}.
\]
The coefficient \(1/(2\rho)\) is the smallest possible *uniform quadratic coefficient* for this specified algorithm, even if the convex body is restricted to a Euclidean disk in dimension two. This improves the coefficient \(2/\rho\) in the cited one-tangent oracle lemma by a factor of four, without changing the oracle or its assumptions.

## Assumptions and scope

All balls are closed Euclidean balls. The supporting unit normal satisfies \(\langle n,z-q\rangle\le0\) for all \(z\in K\). When \(c=0\), the oracle returns \(x\), and the statement is immediate. For \(c\ne0\), put \(d_0=-c/\|c\|\) and \(y=x+s d_0\). If \(y\in K\), return \(\widehat p=y\). Otherwise obtain the last feasible point \(q=x+\tau d_0\) on \([x,y]\), where \(0\le\tau<s\), together with any outward supporting unit normal \(n\) at \(q\). Choose any minimizer
\[
p\in\arg\min\{\langle c,z\rangle:\ z\in B(x,s),\ \langle n,z-q\rangle\le0\},
\]
and return
\[
\widehat p=\operatorname{proj}_{B(q-\rho n,\rho)}(p).
\]
The bound holds for all minimizer choices in the degenerate case where the tangential component of \(c\) vanishes, and for every choice of a valid supporting normal. It requires exact tangent and projection operations; it is not a statement about inexact membership-oracle implementations.

## Proof

**1. Geometry of the relaxed minimizer.** Assume \(y\notin K\). Since \(x\in K\) and \(n\) supports \(K\) at \(q\),
\[
a:=\langle n,d_0\rangle\ge0,\qquad 0\le a\le1.
\]
If \(\tau>0\), this follows from \(\langle n,x-q\rangle=-\tau a\le0\). If \(\tau=0\) and \(a<0\), then for every sufficiently small \(t>0\) the point \(q+t d_0\) belongs to \(B(q-\rho n,\rho)\), because its squared distance to that ball center is \(\rho^2+2\rho t a+t^2<\rho^2\). This contradicts the choice of \(q\) as the last feasible point of the outward ray. Therefore \(a\ge0\) for every valid normal.

The unconstrained maximizer of \(\langle d_0,z\rangle\) on \(B(x,s)\) is \(y\), which lies on or beyond the supporting plane: \(\langle n,y-q\rangle=(s-\tau)a\ge0\). Thus the relaxed minimizer is on that plane. Write \(b=\sqrt{1-a^2}\). If \(b>0\), choose \(u=(d_0-an)/b\). Since \(x=q-\tau(an+bu)\), the planar-slice ball calculation gives
\[
p=q+t u,\qquad t=\sqrt{s^2-\tau^2a^2}-\tau b.
\]
The relation \(\tau\le s\) gives \(0\le t\le s\). If \(b=0\), every relaxed minimizer lies in the supporting plane and satisfies \(\|p-q\|^2\le s^2-\tau^2\le s^2\). Hence in every case
\[
\langle n,p-q\rangle=0,\qquad \|p-q\|\le s,\qquad \langle d_0,p-q\rangle\ge0.
\]
The last inequality holds trivially for \(b=0\), and equals \(bt\ge0\) otherwise.

**2. Repair stays feasible and local.** Write \(v=p-q\), \(L=\sqrt{\rho^2+\|v\|^2}\), and \(\theta=1-\rho/L\). Since \(v\perp n\), the exact ball projection is
\[
\widehat p-p=-\theta(v+\rho n).
\]
The point \(\widehat p\) lies in the interior tangent ball, hence in \(K\). As \(q\) itself is in that tangent ball, nonexpansivity of Euclidean projection gives \(\|\widehat p-q\|\le\|p-q\|\). Also
\[
\langle q-x,\widehat p-p\rangle
=-\tau\theta\bigl(\langle d_0,v\rangle+\rho a\bigr)\le0.
\]
Consequently
\[
\|\widehat p-x\|^2-\|p-x\|^2
=\|\widehat p-q\|^2-\|p-q\|^2+2\langle q-x,\widehat p-p\rangle\le0,
\]
so \(\widehat p\in B(x,s)\).

**3. Improved loss bound.** Every member of \(K\cap B(x,s)\) is feasible for the supporting-halfspace relaxation, so
\[
\langle c,p\rangle\le\min_{z\in K\cap B(x,s)}\langle c,z\rangle.
\]
The correction norm equals the exact tangent-ball distance
\[
\|\widehat p-p\|=L-\rho=\sqrt{\rho^2+\|v\|^2}-\rho.
\]
Using the Cauchy--Schwarz inequality and \(\|v\|\le s\), the objective loss is at most \(\|c\|(\sqrt{\rho^2+s^2}-\rho)\), and rationalization gives the asserted quadratic bound.

**4. Sharpness.** In dimension two choose \(K=B(0,\rho)\), \(x=\rho e_1\), \(s=\rho\varepsilon\), and
\[
d_\varepsilon=(\sqrt{1-\varepsilon^6},\varepsilon^3),\qquad c=-d_\varepsilon,
\]
for \(0<\varepsilon<1/2\). The ray immediately leaves the disk, so \(q=x\), \(n=e_1\). Since the tangential component is strictly positive, the relaxed minimizer is unique:
\[
p=x+s e_2,\qquad
\widehat p=\frac{\rho(e_1+\varepsilon e_2)}{\sqrt{1+\varepsilon^2}}.
\]
The full-disk support point \(z_\star=\rho d_\varepsilon\) belongs to \(B(x,s)\), because \(\|z_\star-x\|^2=2\rho^2(1-\sqrt{1-\varepsilon^6})\le2\rho^2\varepsilon^6<\rho^2\varepsilon^2\). It is therefore the exact local minimizer for \(c=-d_\varepsilon\). The loss is exactly
\[
\rho\left[1-\frac{\sqrt{1-\varepsilon^6}+\varepsilon^4}{\sqrt{1+\varepsilon^2}}\right].
\]
Division by \(s^2/(2\rho)=\rho\varepsilon^2/2\) and passage to \(\varepsilon\downarrow0\) give limit \(1\). No smaller universal quadratic coefficient is possible. The positive tangential component ensures that this is not an artefact of a nonunique relaxed minimizer.

## Verification

A standalone standard-library Python script, `verify.py`, reproduces the disk oracle and compares its output with the exact planar disk-cap optimum for 3,000 deterministic random test instances, including varied scales and directions. It also checks the explicit sharpness family across seven positive radii. The script passes in the packaged form. These finite tests corroborate the geometry but do not replace the proof for all dimensions, all admissible bodies, and arbitrarily small radii.

## Relationship to prior work

Hazan's *A Linearly Convergent Projection-Free Algorithm for Smooth Convex Sets*, arXiv:2608.04321v2, Section 2.2 and Lemma 2.3, introduces exactly this supporting-halfspace and interior-tangent-ball repair and proves the bound with quadratic coefficient \(2/\rho\), using \(\|p-q\|\le2s\). The present result establishes the stronger structural fact \(\|p-q\|\le s\) and makes the resulting coefficient \(1/(2\rho)\) sharp for the specified method.

Levy and Krause (2019) use related tangent-plane repair for *approximate projection* in online learning, not the same local-linear-minimization oracle with an optimal quadratic coefficient. Kolzenburg and Richtárik, arXiv:2611.11354v1, study a short-step Broximal method that assumes an *exact* local linear oracle, so its analysis does not subsume this error bound for a particular *approximate* oracle. The general local-LMO projection interpretation of Richtárik and Mahran, arXiv:2609.33383, concerns the exact local oracle, with no matching sharp bound identified from accessible material. Searches of published mathematical research records did not identify a statement implying the sharp constant. This is a best-knowledge claim, not an exhaustive historical-priority certificate.

## Limitations

The constant is sharp only as a uniform quadratic bound for this exact one-tangent, tangent-ball-projection oracle; alternative oracles may achieve better performance. The stronger radius-dependent majorant is not claimed to be pointwise optimal at every fixed positive radius. The result does not improve the asymptotic order of the outer convergence theorem and does not analyze errors from approximate tangents, finite-precision arithmetic or membership queries.

## References

- E. Hazan, *A Linearly Convergent Projection-Free Algorithm for Smooth Convex Sets*, arXiv:2608.04321v2, https://arxiv.org/abs/2608.04321 (first public version: 2026-08-05 UTC).
- K. Y. Levy and A. Krause, *Projection Free Online Learning over Smooth Sets*, AISTATS 2019, PMLR 89, https://proceedings.mlr.press/v89/levy19a.html.
- J. N. Kolzenburg and P. Richtárik, *An Adaptive Short-Step Variant of BroxGD with Linear Convergence under Quadratic Growth*, arXiv:2611.11354v1, https://arxiv.org/abs/2611.11354.
- P. Richtárik and A. Mahran, *Local LMO is Secretly a Projection Method!*, arXiv:2609.33383, https://arxiv.org/abs/2609.33383.
