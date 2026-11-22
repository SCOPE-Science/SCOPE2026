# Sharp complex convergence disk and exact radial envelopes for the Newton–sine map

## Finding

Let \(N(z)=z-\tan z\) be Newton's map of \(\sin z\), defined away from the poles of \(\tan z\), and let \(R\) be the unique number in \((0,\pi/2)\) satisfying \(\tan R=2R\). Numerically, \(R=1.1655611852072113068\ldots\). Put \(A(t)=\tan t-t\) for \(0\le t<\pi/2\). For every real \(0\le r\le R\) and integer \(n\ge0\),

\[
\max_{|z|\le r}|N^{\circ n}(z)|=A^{\circ n}(r),
\]

where \(A^{\circ 0}(r)=r\), and every maximum is attained at \(z=r\) and \(z=-r\). In particular, for every \(0<r<R\), every orbit initially in the complex closed disk \(|z|\le r\) converges to zero uniformly; indeed, with \(q_r=A(r)/r<1\),

\[
|N^{\circ n}(z)|\le r\,q_r^{(3^n-1)/2}\qquad (|z|\le r,\ n\ge0).
\]

The open disk \(\{|z|<R\}\) is the **largest open Euclidean disk centered at zero entirely contained in the immediate attracting basin of zero**. Its circle of radius \(R\) meets the complement of that immediate basin at exactly two points, \(z=\pm R\), which form a repelling two-cycle. The same statements hold after translation to every sine root \(k\pi\), \(k\in\mathbb Z\).

## Assumptions and scope

All maps act on the complex plane and are iterated only where their meromorphic compositions are defined. The attracting basin of \(k\pi\) comprises the points with globally defined forward orbits converging to \(k\pi\); its immediate basin means the connected component containing \(k\pi\). This theorem concerns **centered Euclidean disks**, not all possible disks or a complete description of the basin's fractal boundary. The formula for iterated maxima is asserted only for \(0\le r\le R\), where the radial envelope stays in its analytic range. The closed critical disk itself is **not** a subset of the basin because of the two boundary points.

## Proof

1. **A positive-coefficient majorant.** Write \(\tan z=\sum_{j\ge0}c_j z^{2j+1}\) in its disk of convergence \(|z|<\pi/2\). The identity \((\tan z)'=1+\tan^2 z\) yields \(c_0=1\) and
   \[
   (2j+1)c_j=\sum_{\ell=0}^{j-1}c_\ell c_{j-1-\ell}\quad(j\ge1).
   \]
   Therefore \(c_j>0\) for every \(j\). In particular,
   \[
   N(z)=-\sum_{j\ge1}c_j z^{2j+1},\qquad
   |N(z)|\le\sum_{j\ge1}c_j|z|^{2j+1}=A(|z|).
   \]
   On each circle of radius \(0<t<\pi/2\), equality holds precisely at the two real points \(\pm t\): equality of the nonzero cubic and quintic summands forces \(z^2\) to be positive real. In particular, \(A(t)\) is the **exact** one-step radial maximum, not merely a bound.

2. **Unique threshold.** Positivity of the coefficients of \(A(t)/t=\sum_{j\ge1}c_jt^{2j}\) makes this function continuous and strictly increasing for \(0<t<\pi/2\); its endpoint limits are zero and infinity. Thus \(A(R)=R\) has exactly one positive solution, equivalently \(\tan R=2R\). For \(0<t<R\), \(0<A(t)<t\). The map \(A\) is increasing, and its positive iterates from any \(r<R\) decrease to a nonnegative fixed point of \(A\) in \([0,r]\); that fixed point must be zero.

3. **Exact iterated maxima.** If \(|z|\le r\le R\), repeated application of the majorant, monotonicity of \(A\) and invariance of \([0,R]\) gives \(|N^{\circ n}(z)|\le A^{\circ n}(r)\). For each real \(0\le t\le R\), \(N(t)=-A(t)\) and \(N(-t)=A(t)\). Thus the two initial states \(z=\pm r\) alternate in sign while their magnitudes follow the scalar recurrence \(r_{n+1}=A(r_n)\), proving equality at every time. For \(0<r<R\), positivity of the coefficients also makes \(A(t)/t^3\) increasing. Hence, for \(0<t\le r\), \(A(t)\le(A(r)/r^3)t^3\). Iteration gives
   \[
   A^{\circ n}(r)\le r\bigl(A(r)/r\bigr)^{(3^n-1)/2},
   \]
   proving uniform convergence with the displayed cubic-order worst-case bound.

4. **The exact first-contact circle.** The disk \(|z|<R\) is invariant under \(N\) and every point in it converges to zero. Since it is connected and contains zero, it lies inside the immediate basin. At \(z=R\), \(N(R)=-R\), and oddness implies \(N(-R)=R\); neither point converges to zero. For every other point of the circle \(|z|=R\), strictness of the complex majorant implies \(|N(z)|<R\), so that point enters the invariant disk in one step and converges to zero. Openness of the basin and contact with the connected invariant disk show that such a point belongs to the **same immediate component**. Thus the critical circle has precisely the two stated exceptional points, and no centered open disk of greater radius is contained in the basin. Finally, \(N'(z)=-\tan^2 z\), so each multiplier at \(\pm R\) has modulus \(4R^2>1\), and the two-cycle's return multiplier is \(16R^4>1\).

5. **Other roots.** The identity \(\tan(z+k\pi)=\tan z\) gives \(N(k\pi+z)=k\pi+N(z)\) for every integer \(k\), transferring the whole statement.

## Verification

The analytic proof is independent of numerical testing. The optional standard-library Python program `check.py` confirms the first 13 positive rational Taylor coefficients, brackets the critical root, tests the modulus majorant on finitely many nonreal circles, tests exact radial iterates at real extremizers, and samples points on the critical circle. Run using `python3 check.py`. The observed output was `PASS: 991 numerical majorant/orbit checks; 13 exact tangent coefficients; R=1.165561185207211`. These checks provide regression evidence only; they are neither a proof of the complex inequalities nor an exhaustive dynamical census.

## Relationship to prior work

Cloutier, Dwyer, Barnard, Stone and Williams (2024), Section 2.3.1, establish the real-axis boundary two-cycle \(\pm R\). Their Section 2.3.5 states that the entire complex disk of that radius **appears numerically** to be contained in the immediate basin, leaving that complex inclusion unproved in the inspected text. The present theorem proves this inclusion, sharpness, the exact contact set of the critical circle, and all-time extremal radial envelopes. Bray, Dwyer, Barnard and Williams (2020) introduce the Newton–sine map for comparison but focus their disk estimates on the distinct Newton map of \(\tan z\), namely \(z-\sin z\cos z\). A public 2019 discussion derives the same real critical number but does not treat the complex disk. General positive-coefficient majorization underlies the proof; it does not itself constitute a previously verified specialized sine-Newton basin theorem.

## Limitations

This is not a global classification of all Fatou components, poles and their preimages, or every periodic orbit. It does not show that the immediate basin is a disk: outside the maximal **centered** disk the basin can still extend in some directions. The exact threshold and rates are for an undamped Newton step for \(\sin z\), not for Newton's method for \(\tan z\). Existing unindexed or differently phrased literature could contain the complex disk statement; independent mathematical and priority audits have not been performed.

## References

1. A. Cloutier, J. Dwyer, R. W. Barnard, W. D. Stone, G. B. Williams, *Dynamics of Iterations of the Newton Map of sin(z)*, Symmetry **16** (2024), 162, published January 30, 2024. https://doi.org/10.3390/sym16020162 . Sections 2.3.1 and 2.3.5.
2. K. Bray, J. Dwyer, R. W. Barnard, G. B. Williams, *Fixed Points, Symmetries, and Bounds for Basins of Attraction of Complex Trigonometric Functions*, International Journal of Mathematics and Mathematical Sciences (2020), Article 1853467, first published April 23, 2020. https://doi.org/10.1155/2020/1853467 . Section 2.1 and the distinct tangent-Newton basin theorem.
3. *Newton's method, find the initial value which will produce a periodic cycle when we start the iteration from this value*, Mathematics Stack Exchange, October 4, 2019, https://math.stackexchange.com/questions/3379990/ . Real-axis critical-value precursor, not a complex-disk proof.
