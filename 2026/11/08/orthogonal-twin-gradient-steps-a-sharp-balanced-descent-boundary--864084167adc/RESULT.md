# Orthogonal twin-gradient steps: a sharp balanced-descent boundary and unbounded unbalanced ascent

## Finding

Consider minimizing the squared distance between two gradient rays on a symmetric positive-definite (SPD) quadratic. Even when their normalized descent directions are exactly orthogonal and the two rays meet, contraction of their separation does not imply objective descent. Two sharp conclusions hold.

**Balanced-data frontier.** For every common damping \(0<\eta\le1\), among all real SPD quadratic forms whose spectral condition number is at most \(\kappa\ge1\), the distance-minimizing paired step is objective-nonincreasing at **both** endpoints whenever their initial objective values agree and their normalized negative gradient directions are orthogonal, if and only if
\[
\kappa\le\frac4\eta-1.
\]
The boundary is attained; beyond it, a two-dimensional example strictly increases both objective values. In particular the undamped threshold is \(\kappa=3\).

**Unbalanced-data obstruction.** For every \(\kappa>1\) and every fixed \(0<\eta\le1\), there is a family of planar SPD quadratics with condition number exactly \(\kappa\), pairs of starting points with orthogonal normalized negative gradients and strictly positive distance-minimizing step lengths, such that the two rays meet exactly while the ratio of the first endpoint's new objective to its original objective tends to infinity. At \(\kappa=1\), every such orthogonal meeting pair instead contracts each objective by the factor \((1-\eta)^2\). Thus positive fixed damping based only on the angle cannot ensure per-path objective descent as soon as the quadratic is anisotropic.

## Assumptions and scope

Let \(A\in\mathbb R^{2\times2}\) be SPD and \(f(u)=\frac12u^{\mathsf T}Au\), with minimizer at the origin. Let \(x,z\in\mathbb R^2\) have nonzero gradients; their normalized **negative** gradients are
\[
p=-Ax/\|Ax\|_2,\qquad q=-Az/\|Az\|_2,\qquad p^{\mathsf T}q=0.
\]
Choose \(\alpha,\beta\ge0\) to globally minimize \(\frac12\|(x+\alpha p)-(z+\beta q)\|_2^2\), then set \(x^+=x+\eta\alpha p\) and \(z^+=z+\eta\beta q\). Only this paired minimization step is studied, not optional switching or line-search components of a full hybrid optimizer. For the balanced pairs and the explicit unbalanced family below, the constrained minimizer is interior and the undamped rays meet exactly. A general pair may instead have an active nonnegativity constraint. Condition number means \(\kappa_2(A)=\lambda_{\max}(A)/\lambda_{\min}(A)\).

## Proof

Choose the orthonormal basis whose vectors point along \(Ax\) and \(Az\), respectively, and work in its coordinates. Write
\[
B=A^{-1}=\begin{pmatrix}a&c\\c&d\end{pmatrix},\quad
 a>0,\ d>0,\ ad>c^2,\qquad
Ax=Ue_1,\ Az=Ve_2,\quad U,V>0.
\]
Thus \(x=(aU,cU)\), \(z=(cV,dV)\), and the two descent rays are \(x-\alpha e_1\) and \(z-\beta e_2\). Their uniquely minimizing nonnegative step lengths are
\[
\alpha=aU-cV,\qquad \beta=dV-cU,
\]
whenever these are positive. At such lengths the two undamped rays meet, so their damped separation equals \((1-\eta)(x-z)\). In the constructions below, positivity is explicit. For a general orthogonal-gradient pair with \(c>0\), one or both lengths may instead be clipped to zero; the balanced case remains interior, as shown next.

Suppose \(f(x)=f(z)>0\). Since \(f(x)=aU^2/2\) and \(f(z)=dV^2/2\), this is equivalent to \(aU^2=dV^2\). Set \(r=-c/\sqrt{ad}\), so \(-1<r<1\) and \(V/U=\sqrt{a/d}\). Therefore
\[
\alpha=aU(1+r)>0,\qquad \beta=dV(1+r)>0.
\]
A direct quadratic expansion, using \(Ax=Ue_1\) and the \((1,1)\)-entry \(d/(ad-c^2)=1/[a(1-r^2)]\) of \(A\), gives
\[
\frac{f(x^+)}{f(x)}
=1-2\eta(1+r)+\eta^2\frac{(1+r)^2}{1-r^2}
=1-2\eta(1+r)+\eta^2\frac{1+r}{1-r}.
\]
The same expression holds for \(f(z^+)/f(z)\). Denoting it by \(R\),
\[
R-1=\eta(1+r)\left(\frac\eta{1-r}-2\right).
\]
Consequently both new objectives strictly increase precisely when \(r>1-\eta/2\), remain unchanged at equality, and otherwise decrease.

To optimize this criterion over a spectral condition class, put \(\kappa=\kappa_2(A)=\kappa_2(B)\). The determinant and trace of \(B\) imply
\[
\frac{ad-c^2}{(a+d)^2}=\frac{\kappa}{(\kappa+1)^2}.
\]
By \((a+d)^2\ge4ad\),
\[
1-r^2=\frac{ad-c^2}{ad}
\ge\frac{4\kappa}{(\kappa+1)^2},\qquad
r\le |r|\le\frac{\kappa-1}{\kappa+1}.
\]
Equality is achieved with \(a=d=1\) and \(c=-r\). Hence universal nonincrease at both balanced starts is equivalent to
\[
\frac{\kappa-1}{\kappa+1}\le1-\frac\eta2,
\]
which simplifies to \(\kappa\le4/\eta-1\). Necessity, including the strict ascent beyond this boundary, follows by taking \(B=\begin{psmallmatrix}1&-r\\-r&1\end{psmallmatrix}\), \(r=(\kappa-1)/(\kappa+1)\), \(U=V=1\).

For the unbalanced obstruction, fix any \(\kappa>1\), \(\eta>0\), and the same \(B\) with \(r=(\kappa-1)/(\kappa+1)\). Let \(Ax=e_1\), \(Az=Me_2\), where \(M>0\) varies. Then
\[
x=(1,-r),\qquad z=(-rM,M),\quad
\alpha=1+rM>0,\quad\beta=M+r>0,
\]
and the undamped rays meet at \((-rM,-r)\). Meanwhile \(f(x)=1/2\) and exact expansion gives
\[
\frac{f(x^+)}{f(x)}
=1-2\eta(1+rM)+\frac{\eta^2(1+rM)^2}{1-r^2}.
\]
The leading coefficient in \(M^2\) is \(\eta^2r^2/(1-r^2)>0\), proving divergence to infinity with \(\kappa\) and \(\eta\) fixed. The distance after damping is exactly \((1-\eta)\|x-z\|_2\). If \(\kappa=1\), \(A\) is a positive scalar multiple of the identity, and an orthogonal-gradient pair lies on the two coordinate axes; the rays then meet at the origin, giving \(x^+=(1-\eta)x\), \(z^+=(1-\eta)z\), and objective ratio \((1-\eta)^2\) on each path. This proves both assertions.

## Verification

The included `VERIFY.py` uses standard-library exact rational arithmetic to check the two-step geometry, each balanced ratio formula, positivity of the step lengths, the sharp condition-number boundary and unbalanced high-contrast families. It reports `VERIFY_OK 688 exact-rational checks` on successful completion. The finite checks are diagnostics; the universal quantifiers and divergent limit follow from the preceding exact proof. To reproduce, run `python3 VERIFY.py` in the directory containing this document and the script.

## Relationship to prior work

De Magistris, Hochstenbach and Toraldo introduce the Twin gradient distance-minimization step, characterize its angle geometry, and use safeguards and complementary steps. Their guarantee of decreasing inter-path distance is not a guarantee of decreasing objective values. The present result isolates the **orthogonal**, exactly meeting, simultaneously balanced case and determines its sharp objective condition-number boundary, then demonstrates unbounded objective ascent without balanced energies. It does **not** assert failure of their safeguarded full algorithm. A related speed-up scheme with partially overlapping authors optimizes a different direction selection. Classical single-path line-search and two-mode steepest-descent objective factors concern a different update rule and do not directly imply the paired distance minimizer formulas here.

## Limitations

The result is confined to two-dimensional real SPD quadratics, normalized negative-gradient rays, an exact constrained distance-minimizing paired step, and constant common damping. The balanced result quantifies both endpoints jointly; the unbalanced result forces unbounded amplification of one endpoint, not necessarily of both. No numerical stability guarantee is given for finite precision. No convergence or divergence assertion is made about a hybrid algorithm equipped with switching, admissibility tests or line searches. Related historical descent analyses may contain equivalent statements under other names; no claim of exhaustive literature coverage or independent verification is made.

## References

1. A. De Magistris, M. E. Hochstenbach and G. Toraldo, *A Twin gradient method for unconstrained optimization*, arXiv:2607.11575, first public version July 13, 2026, https://arxiv.org/abs/2607.11575. Main algorithm and its geometric analysis, inspected in the open preprint.
2. A. De Magistris, S. Crisci, V. De Simone and G. Toraldo, *A speed up strategy for gradient methods*, Computational Optimization and Applications (2026), https://doi.org/10.1007/s10589-026-00778-0. Related but different optimization procedure.
3. J. van Lith, P. C. Hansen and M. E. Hochstenbach, *A twin error gauge for Kaczmarz's iterations*, arXiv:1906.07470, https://arxiv.org/abs/1906.07470. Terminological and geometric predecessor with a different stopping-rule objective.
