# Exact Hausdorff convergence of all convex binary cyclotomic domains

## Finding

Put \(Q=[-1,1]^2\). For a positive-definite homogeneous binary cyclotomic form \(\Phi_m\) of even degree, write \(\mathcal O_m=\{(x,y)\in\mathbb R^2:\Phi_m(x,y)\le1\}\). Distance throughout is Euclidean, and \(d_H\) denotes the (two-sided) Euclidean Hausdorff distance between compact sets. The full class of convex \(\mathcal O_m\), classified by Fouvry and Waldschmidt, has the following exact metric profile:

\[
 d_H(\mathcal O_m,Q)=
 \begin{cases}
 \sqrt2\bigl(1-p^{-1/(p-1)}\bigr),&m=p\text{ or }m=2p,\quad p\text{ odd prime},\\
 \sqrt2\bigl(1-2^{-1/2^{k-1}}\bigr),&m=2^k,\quad k\ge2.
 \end{cases}
\]

More generally, for **every odd integer** \(s\ge3\), put \(F_s(x,y)=\sum_{j=0}^{s-1}x^{s-1-j}y^j\) and \(B_s=\{F_s\le1\}\). Then \(d_H(B_s,Q)=\sqrt2\bigl(1-s^{-1/(s-1)}\bigr)\). In particular, the two arithmetic subsequences of convex cyclotomic domains obey different sharp rates:

\[
 d_H(\mathcal O_p,Q)\sim\frac{\sqrt2\log p}{p},\qquad
 d_H(\mathcal O_{2^k},Q)\sim\frac{2\sqrt2\log2}{2^k}.
\]

## Assumptions and scope

All integers \(p\) are odd primes, \(k\ge2\) is an integer, and \(s\ge3\) is odd. The squares and distances use the standard Euclidean norm, with **no** rescaling of the cyclotomic form. The result concerns only the convex cases \(m\ge3\), not the generally nonconvex domains for composite indices excluded by the classification. For \(x=y\), the divided difference \((x^s-y^s)/(x-y)\) is interpreted continuously as \(s x^{s-1}\).

## Proof

**1. The divided-power body is compact and convex.** Put \(n=s-1\), which is even and at least two. The integral identity

\[
 F_s(x,y)=s\int_0^1\bigl(tx+(1-t)y\bigr)^n\,dt
\]

shows that \(F_s\ge0\), with equality only at \((0,0)\), and that \(F_s\) is convex, because every integrand is a convex function of \((x,y)\). Homogeneity then makes \(B_s\) compact. It is invariant under simultaneously changing both signs and under exchanging the two coordinates.

**2. Exact distance from the square to the divided-power body.** On the diagonal, \(F_s(t,t)=s t^n\). Set \(a=s^{-1/n}\), so \(B_s\cap\{x=y\}=\{(t,t):|t|\le a\}\). If a point of \(B_s\) realizes the distance from the square corner \((1,1)\), averaging it with its coordinate swap gives another point in \(B_s\) that is no farther from \((1,1)\). Thus a closest point lies on the diagonal, and

\[
 \operatorname{dist}((1,1),B_s)=\sqrt2(1-a)=:\delta_s.
\]

The same holds at \((-1,-1)\). At both remaining corners the distance is zero, since \(F_s(1,-1)=F_s(-1,1)=1\). The distance to a closed convex set is convex. Every point of \(Q\) is a convex combination of its four vertices; hence

\[
 \sup_{q\in Q}\operatorname{dist}(q,B_s)=\delta_s.
\]

**3. Outward excess is strictly smaller.** For \((x,y)\in B_s\) with \(xy\ge0\), put \(u=\max(|x|,|y|)\). The positive sum defining \(F_s\) gives \(F_s(x,y)\ge u^n\), hence \(|x|,|y|\le1\): such a point already belongs to \(Q\). If \(xy<0\), put \(u=\max(|x|,|y|)\) and \(v=\min(|x|,|y|)\). Then

\[
 F_s(x,y)=\frac{u^s+v^s}{u+v}\le1.
\]

It follows that \(u^s\le u+v\le2u\), so \(u\le2^{1/n}\). Also \(u>1\) and \(v>1\) cannot both hold, since then \(u^s+v^s>u+v\). Therefore at most one coordinate leaves \([-1,1]\), with total Euclidean outward distance bounded by

\[
 \sup_{z\in B_s}\operatorname{dist}(z,Q)\le2^{1/n}-1.
\]

This bound is always strictly less than \(\delta_s\). Indeed let \(h(t)=\sqrt2(1-3^{-t})-(2^t-1)\) for \(0\le t\le\tfrac12\). Direct differentiation gives \(h''(t)<0\), while \(h(0)=0\) and \(h(1/2)=1-\sqrt{2/3}>0\). Concavity implies \(h(t)>0\) for \(0<t\le\tfrac12\). Taking \(t=1/n\) and using \(s\ge3\) yields

\[
 2^{1/n}-1<\sqrt2(1-3^{-1/n})\le\sqrt2(1-s^{-1/n})=\delta_s.
\]

The larger of the two directed Hausdorff distances is therefore \(\delta_s\), establishing the general odd-\(s\) formula.

**4. Cyclotomic identifications.** For odd prime \(p\), \(\Phi_p(x,y)=F_p(x,y)\), and \(\Phi_{2p}(x,y)=F_p(x,-y)\). Reflection in the coordinate axis preserves both Euclidean distance and \(Q\), so the same formula holds for both indices. For \(m=2^k\), set \(n=2^{k-1}\); the cyclotomic form equals \(x^n+y^n\). Its domain is a convex subset of \(Q\). Coordinate sign symmetries and interchange show that the nearest point to \((1,1)\) lies at \((2^{-1/n},2^{-1/n})\). Thus its corner distance is \(\sqrt2(1-2^{-1/n})\). Convexity of the distance function and symmetry of the four corners give the exact two-sided Hausdorff distance. The stated asymptotic rates follow from \(1-e^{-u}\sim u\) as \(u\downarrow0\).

## Verification

The standalone `verify.py` is included. It uses exact rational arithmetic to check the divided-power lower Euclidean bound, both outward coordinate constraints, and 5,625 rational grid instances across nine odd degrees. It also checks 25 symbolic homogenized cyclotomic identities and 500 high-precision-free floating-point scalar comparisons, which only corroborate the analytic inequality. Execute with `python3 verify.py` from the directory containing the file; the run produced:

```text
VERIFY_OK exact_grid_points=5625 cyclotomic_identities=25 scalar_comparisons=500 rational_exact=yes
```

The unlimited-degree conclusion is proved above, not inferred from these finite checks.

## Relationship to prior work

Fouvry and Waldschmidt, *On the convexity of the fundamental domain of binary cyclotomic forms* (arXiv:2610.37735v1, first posted 2026-10-27), classify the convex indices and prove convexity of the divided-power body in Lemma 3.1. Their stated results give convexity, not the exact distance from the fixed square. Their earlier paper, *Sur la représentation des entiers par les formes cyclotomiques de grand degré* (arXiv:1909.01892v1), Theorem 1.5, gives inner and outer squares of side lengths \(2\pm m^{-1+\varepsilon}\) for all sufficiently large cyclotomic indices, implying convergence with a non-sharp rate. The present exact Hausdorff formula and constants do not follow from that estimate. The proof uses the new classification to organize all cases and sharpens the quantitative picture within them.

## Limitations

The result does not classify Hausdorff distances of nonconvex cyclotomic domains, and it does not determine surface areas, lattice-point errors, or optimal ellipsoidal approximations. Prior formulations outside the inspected works could contain an equivalent sharp metric statement; literature searches alone cannot establish global priority. The verification script is a finite corroboration, not independent proof or an external audit.

## References

1. É. Fouvry and M. Waldschmidt, *On the convexity of the fundamental domain of binary cyclotomic forms*, arXiv:2610.37735v1 (2026-10-27), Sections 1, 3 and 5; https://arxiv.org/abs/2610.37735.
2. É. Fouvry and M. Waldschmidt, *Sur la représentation des entiers par les formes cyclotomiques de grand degré*, arXiv:1909.01892v1 (2019-09-04), Theorem 1.5 and Section 6; https://arxiv.org/abs/1909.01892.
