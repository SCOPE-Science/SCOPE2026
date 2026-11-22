# Sharp perimeter profile for opposite unit-strutted legs of symmetric trapezoids

## Finding
Let \(T\) be a nondegenerate Euclidean isosceles trapezoid with parallel base lengths \(p\ge q>0\), equal nonparallel leg length \(a\), and height \(h>0\). We include rectangles when \(p=q\). A leg \(UV\) is **unit-strutted** if a point \(W\in T\) satisfies \(|W-U|=|W-V|=1\); the closed set \(T\) is used, so witnesses on the boundary, including vertices, are allowed.

Assume both legs are unit-strutted. For each fixed \(0<a<1\),
\[
\operatorname{per}(T)\ge 2+2a-a^2,
\]
with equality, up to Euclidean congruence, exactly when
\[
(p,q,h)=\left(1,1-a^2,a\sqrt{1-a^2/4}\right).
\]
In particular, if the sum of the lengths of the two opposite unit-strutted legs is at least \(1\), then
\[
\boxed{\operatorname{per}(T)\ge\frac{11}{4}.}
\]
This is sharp, and equality occurs only for \((p,q,a,h)=(1,3/4,1/2,\sqrt{15}/8)\). Consequently, the lower bound \(3\) known for **two adjacent** unit-strutted sides with combined length at least \(1\) does not extend to opposite legs even among symmetric convex quadrilaterals.

The following more precise description is also exact for \(0<a<1\): put \(\delta=(p-q)/2\) and \(S=p+q\). Then both legs admit unit struts if and only if
\[
0\le\delta\le\frac{a^2}{2},\qquad
S\ge\frac{2\sqrt{1-a^2/4}\,(a^2-2\delta^2)}{a\sqrt{a^2-\delta^2}}.
\]
The standing conditions \(p\ge q>0\) and \(h>0\) are understood. For \(1\le a\le2\), the elementary bound \(\operatorname{per}(T)\ge a+2\ge3\) holds; for \(a>2\), a unit strut is impossible.

## Assumptions and scope
Write the vertices counterclockwise as
\[
A=(-p/2,0),\quad B=(p/2,0),\quad C=(q/2,h),\quad D=(-q/2,h).
\]
Let \(\delta=(p-q)/2\ge0\). Then \(a^2=h^2+\delta^2\). All distances are ordinary Euclidean distances and the witness is permitted anywhere in the **closed** trapezoid. The sharp fixed-leg theorem is claimed only for \(0<a<1\); the global bound additionally assumes \(2a\ge1\). No assertion for arbitrary nonsymmetric quadrilaterals, different pairs of sides, or interior-only witnesses is intended.

## Proof
**1. The unique candidate for the right leg.** For \(0<a<1\), the two circles of radius \(1\) about \(B\) and \(C\) meet in exactly two points. Put \(s=\sqrt{1-a^2/4}>0\). The one to the interior side of the supporting line \(BC\) is
\[
W=\left(\frac{p+q}{4}-\frac{sh}{a},\quad\frac h2-\frac{s\delta}{a}\right).
\]
Indeed, the midpoint of \(BC\) is \(((p+q)/4,h/2)\), and the inward normal displacement has length \(s\); the other circle intersection lies outside the supporting half-plane. Reflection in the vertical axis exchanges the two legs, so both have unit struts exactly when \(W\in T\).

**2. Exact feasibility.** The point \(W\) automatically satisfies the upper and right supporting inequalities. Its lower-coordinate inequality \(W_y\ge0\) is equivalent, since both sides are nonnegative, to
\[
a^2(a^2-\delta^2)\ge4(1-a^2/4)\delta^2
\quad\Longleftrightarrow\quad \delta\le a^2/2.
\]
For the left side of \(T\), the supporting inequality is
\[
W_x\ge-p/2+(\delta/h)W_y.
\]
Substitution gives
\[
S\ge F_a(\delta):=
\frac{2s(a^2-2\delta^2)}{a\sqrt{a^2-\delta^2}}.
\]
Thus these two conditions, along with \(p\ge q>0\) and \(h>0\), are necessary and sufficient. Here \(\delta\le a^2/2<a\) implies the denominator is positive, while \(a^2-2\delta^2>0\).

**3. Exact fixed-leg lower bound.** On \(0<a<1\) and \(0\le\delta\le a^2/2\), both \(F_a(\delta)\) and \(2-a^2\) are positive. Their squared difference has the exact factorization
\[
\begin{aligned}
&a^2(a^2-\delta^2)\bigl(F_a(\delta)^2-(2-a^2)^2\bigr)\\
&=(a^4-4\delta^2)\bigl(3a^2-a^4-(4-a^2)\delta^2\bigr).
\end{aligned}
\]
The first factor is nonnegative. The second is strictly positive: \(\delta^2\le a^4/4\) gives
\[
3a^2-a^4-(4-a^2)\delta^2
\ge a^2\left(3-2a^2+\frac{a^4}{4}\right)>0.
\]
Hence \(F_a(\delta)\ge2-a^2\), with equality exactly when \(\delta=a^2/2\). Since \(\operatorname{per}(T)=S+2a\), the claimed lower bound follows.

At equality \(S=2-a^2\) and \(\delta=a^2/2\), so \(p=S/2+\delta=1\) and \(q=S/2-\delta=1-a^2>0\); the altitude is \(h=\sqrt{a^2-a^4/4}=a\sqrt{1-a^2/4}\). These data are feasible. Indeed, the right-leg witness is the opposite long-base vertex \(A\), the left-leg witness is \(B\), and the equal diagonals have squared length
\[
|AC|^2=|BD|^2=(1-a^2/2)^2+a^2(1-a^2/4)=1.
\]
This gives existence and uniqueness of the fixed-leg equality shape.

**4. Optimization and the remaining leg range.** When both legs have total length at least \(1\), \(a\ge1/2\). For \(1/2\le a<1\), the function \(2+2a-a^2\) is strictly increasing, and equals \(11/4\) only at \(a=1/2\). For \(a\ge1\), any unit-strut witness on a leg creates a contained Euclidean triangle with side lengths \(a,1,1\); perimeter is monotone under convex inclusion, so \(\operatorname{per}(T)\ge a+2\ge3>11/4\). For \(a=2\), the witness is the midpoint of the leg; the basic diameter bound \(\operatorname{per}(T)\ge2a=4=a+2\) replaces the nondegenerate triangle argument. Triangle inequality excludes \(a>2\). The unique global equality shape therefore has long base \(1\), short base \(3/4\), legs \(1/2\), and height \(\sqrt{15}/8\).

## Verification
The accompanying `verify.py` runs using Python 3 standard library only. It checks the exact bivariate polynomial identity in the proof by coefficient arithmetic, the nonnegative-factor inequalities on rational parameter grids, the exact squared diagonal lengths and sharp perimeter, and independently checks circle-intersection distances and polygon containment across numerical parameter samples. It passed **8,204 assertions** in the packaged form. These finite tests corroborate the algebra and boundary formulas; the argument above is the proof for all real parameters.

To reproduce: extract the `verify.py` file from this package unchanged and run `python3 verify.py`; no third-party modules or network are needed.

## Relationship to prior work
Nikonorov and Nikonorova, *Some extremal problems for polygons in the Euclidean plane*, arXiv:2209.05940 (first posted 2022-09-13), define unit-strutted sides through the existence of a point of the polygon at unit distance from both endpoints. Their Theorem 2 gives the perimeter-three bound for **two consecutive sides** whose combined length is at least one; their conjecture similarly retains consecutiveness. The present theorem locates the exact sharp contrasting bound for the two **opposite legs** in the symmetric-trapezoid class, with the full fixed-leg profile and equality cases. The original consecutive-side theorem does not cover the new hypothesis.

Nikitenko and Nikonorov, *The extreme polygons for the self Chebyshev radius of the boundary*, arXiv:2301.03218, solve an extremal problem constrained by a different global radius, not by specified unit struts on opposite sides. Nikonorov and Oskorbin, *One Application of Ptolemy's Theorem* (2025), simplify the proof of the original special-pentagon **adjacent-side** result but do not address the opposite-leg family. Other published trapezoid results on geometric dilation, perimeter depth, and convexification have different constraints and objectives; their conclusions do not imply this sharp perimeter statement.

## Limitations
This is a theorem about **isosceles** trapezoids only; it does not establish the optimum for arbitrary convex quadrilaterals or for all polygons. The unit-strut witness is allowed on the boundary; requiring a witness to lie strictly in the interior would change attainability. For fixed \(a\ge1\) the theorem gives the simpler perimeter bound \(a+2\), not a complete sharp profile. Earlier unpublished or unindexed geometry notes might contain an equivalent calculation, so historical priority remains subject to further independent literature review. Independent mathematical audit has not been performed.

## References
1. Yu. G. Nikonorov and O. Yu. Nikonorova, *Some extremal problems for polygons in the Euclidean plane*, arXiv:2209.05940 (2022), https://arxiv.org/html/2209.05940v2 ; initial public posting https://arxiv.org/abs/2209.05940 .
2. E. V. Nikitenko and Yu. G. Nikonorov, *The extreme polygons for the self Chebyshev radius of the boundary*, arXiv:2301.03218 (2023), https://arxiv.org/abs/2301.03218 .
3. Yu. G. Nikonorov and D. N. Oskorbin, *One Application of Ptolemy's Theorem*, Vladikavkaz Math. J. 27(4), 103–108 (2025), https://doi.org/10.46698/o1944-0990-7792-e .
