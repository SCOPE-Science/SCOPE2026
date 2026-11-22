# Exact odd area and robust sub-\(\pi\) certification for seven unit disks

## Finding

Let \(D_j\) be seven closed Euclidean unit disks centered at the following points, in the displayed order:
\[
 c_0=(0,0),\quad c_1=(\sqrt3/6,0),\quad c_2=(-\sqrt3/12,1/4),\quad c_3=(-\sqrt3/12,-1/4),
\]
\[
 c_4=(\sqrt3/24,1/8),\quad c_5=(-\sqrt3/12,0),\quad c_6=(\sqrt3/24,-1/8).
\]
Thus the six noncentral centers are the three vertices and three edge-midpoints of an equilateral triangle of side \(1/2\). Define \(\operatorname{OA}(D_0,\ldots,D_6)\) as the planar area covered by an odd number of the seven disks. Put
\[
\begin{aligned}
 \mathcal R={}&-\frac{3\sqrt{15}}4-\frac{3\sqrt{183}}{16}-\frac{\sqrt3}{16}
 +\frac{\sqrt{191}}{16}+\frac{\sqrt{47}}4+\frac{9\sqrt7}{8},\\
 \mathcal U={}&12\arcsin(\sqrt3/24)+24\arcsin(1/8)+12\arcsin(\sqrt3/12)\\
 &\quad-12\arcsin(\sqrt3/8)-12\arcsin(1/4).
\end{aligned}
\]
Then the **exact** odd area is
\[
 \boxed{\operatorname{OA}(D_0,\ldots,D_6)=\pi+\mathcal R+\mathcal U
 =3.1080916498782973699968\ldots.}
\]
In particular, the certified rational bounds
\[
 -0.033502<\mathcal R+\mathcal U<-0.033500
\]
prove the strict inequality \(\operatorname{OA}<\pi-67/2000\), with no numerical area integration needed.

This counterexample is stable under **arbitrary** simultaneous translations: if \(D_j'\) is the unit disk centered at \(c_j+h_j\), then
\[
 \boxed{\sum_{j=0}^6\|h_j\|<67/8000\quad\Longrightarrow\quad
 \operatorname{OA}(D_0',\ldots,D_6')<\pi.}
\]
The exact evaluation and the explicit guaranteed perturbation neighborhood are the findings; the seven-disk configuration and the existence of a sub-\(\pi\) example were already established by Steinerberger (2026).

## Assumptions and scope

All areas are ordinary two-dimensional Lebesgue areas. Membership on disk boundaries does not affect area. The seven centers and the unit radii are fixed exactly as above; the robustness conclusion permits each center to move independently. No claim is made that this arrangement is globally or locally area-minimizing, that seven is the smallest possible number of disks in a counterexample, or that the true robustness radius is optimal. The motivating source first appeared publicly on 6 June 2026.

## Proof

For each disk define \(z_j(\theta)=c_j+(\cos\theta,\sin\theta)\) and
\[
 \sigma_j(\theta)=(-1)^{\#\{k\ne j:\|z_j(\theta)-c_k\|<1\}}.
\]
The boundary of the odd-multiplicity region consists, up to finitely many intersections, of arcs on the seven unit circles. Its positively oriented Green area integral assigns sign \(\sigma_j\) to the counterclockwise traversal of the \(j\)th circle. Consequently,
\[
 2\operatorname{OA}=\sum_{j=0}^6 I_j,\qquad
 I_j=\int_0^{2\pi}\sigma_j(\theta)
 (1+c_{j,x}\cos\theta+c_{j,y}\sin\theta)\,d\theta. \tag{1}
\]
For centers \(c_j,c_k\) at distance \(d_{jk}<2\), the two circle intersections have angles
\[
 \theta_{jk}^{\pm}=\arg(c_k-c_j)\pm\arccos(d_{jk}/2)\pmod{2\pi}. \tag{2}
\]
All the angles \(\arg(c_k-c_j)\) are integer multiples of \(\pi/6\). Every \(d_{jk}/2\) belongs to the five-element set
\[
 \{\sqrt3/24,\ 1/8,\ \sqrt3/12,\ \sqrt3/8,\ 1/4\}.
\]
For a complete finite ordering check, name the five associated arccosines \(B_1,\ldots,B_5\) in that order and use the labels \(O,V_0,V_1,V_2,M_0,M_1,M_2\) for the sites above. The circle crossings, traversed counterclockwise from angle zero, occur in these exact orders; plus/minus refers to the sign in (2):

| Circle | Sign of \(\sigma(0)\) | Subsequent crossing order |
|---|---:|---|
| \(O\) | \(-1\) | \(M_2^+,V_1^-,V_0^+,M_1^-,M_0^+,V_2^-,V_1^+,M_2^-,M_1^+,V_0^-,V_2^+,M_0^-\) |
| \(V_0\) | \(+1\) | \(M_0^-,V_1^-,O^-,M_1^-,M_2^-,V_2^-,V_1^+,M_0^+,M_1^+,O^+,V_2^+,M_2^+\) |
| \(M_0\) | \(-1\) | \(V_0^+,V_1^-,M_1^-,O^-,V_2^-,M_2^-,V_1^+,V_0^-,M_1^+,V_2^+,O^+,M_2^+\) |

The crossings are all strict, so the parity sign reverses at each. The table follows from (2): substitute the exact centers, reduce the five possible half-angle terms to \(\pi/2-\arcsin(d_{jk}/2)\), and compare them using the elementary increasing series for \(\arcsin\). The accompanying rational-arithmetic checker independently verifies every ordering inequality, including the absence of coincident crossings.

Let \(F_j(\theta)=\theta+c_{j,x}\sin\theta-c_{j,y}\cos\theta\), a primitive for the integrand in (1) without the parity factor. If \(\Delta\sigma_j(\theta_*)\) is the sign jump at a crossing, the integral equals
\[
 I_j=2\pi\sigma_j(0)-\sum_{\theta_*}\Delta\sigma_j(\theta_*)F_j(\theta_*). \tag{3}
\]
Using the above table in (3) and simplifying the sine and cosine of (2) yields
\[
 I_O=10\pi-12B_1-12B_3,
\]
\[
 I_{V_0}=2\pi-8B_2-4B_3+4B_4+8B_5
 -\frac{\sqrt{15}}2-\frac{\sqrt{183}}{12}
 +\frac{\sqrt{47}}6+\frac{3\sqrt7}4,
\]
\[
 I_{M_0}=\frac{10\pi}3-4B_1-8B_2+4B_4
 -\frac{\sqrt{183}}{24}-\frac{\sqrt3}{24}+\frac{\sqrt{191}}{24}.
\]
Rotation by \(2\pi/3\) preserves the configuration. Hence \(2\operatorname{OA}=I_O+3I_{V_0}+3I_{M_0}\). Substitution of \(B_i=\pi/2-\arcsin(d_i/2)\) proves the stated closed formula.

For strictness, all square roots can be enclosed by rational intervals using integer square roots. For \(0\le x\le1/4\), the first \(N\) positive Taylor terms of \(\arcsin x\) give a lower bound, with remaining tail at most \(x^{2N+1}/(1-x^2)\). Ten terms, rational interval arithmetic and the classical alternating-arctangent series for \(\pi\) yield the stated rational interval. This is a finite exact certificate, not a statistical estimate.

Finally, for any vector \(h\), horizontal slicing in the direction of \(h\) proves \(|D\triangle(D+h)|\le4\|h\|\) for a unit disk \(D\): each one-dimensional interval changes by at most \(2\|h\|\), over a perpendicular span of length two. The symmetric difference of two parity unions is contained in the union of the seven corresponding disk symmetric differences. Thus
\[
 \bigl|\operatorname{OA}(D_0',\ldots,D_6')-\operatorname{OA}(D_0,\ldots,D_6)\bigr|
 \le4\sum_j\|h_j\|,
\]
which proves the stated open perturbation neighborhood.

## Verification

The standalone Python 3 file `odd_area_certificate.py` requires only the standard library. It constructs every circle-intersection angle from integer-coordinate differences, checks the complete strict angular orders using rational enclosures for \(\pi\), \(\arcsin\), and square roots, evaluates (1) via rational-interval Green integration, and independently evaluates the simplified formula. It proves \(-0.033502<\operatorname{OA}-\pi<-0.033500\). A separate midpoint polar integration, where all seven disk-exit radii are sorted on every ray, checks the same area numerically by a different geometric method. The polar integration corroborates the formula but is not used to certify the strict bound.

## Relationship to prior work

Steinerberger (2026) identified this very configuration and reported odd area approximately \(3.108\), giving a counterexample to the proposed universal bound \(\operatorname{OA}\ge\pi\). This finding **does not** re-claim the configuration or the counterexample. Its addition is the closed radical/inverse-trigonometric area identity, the reproducible rational strictness certificate and the explicit perturbation guarantee. Carmel and Pinchasi (2023) proved the lower bound for concyclic centers of radius at most one, which cannot apply here because the seven centers lie on three distinct radii. The broader odd-area and first-variation literature does not itself furnish the displayed exact evaluation.

## Limitations

Only the specified seven-disk benchmark is evaluated. The perturbation threshold is a conservative certified neighborhood, not an optimum. None of the inequalities determine the infimum odd area among all odd numbers of disks. The historical novelty comparison is to accessible sources and searches; a previous independently derived expression not indexed in those sources remains possible. Independent external mathematical validation has not been performed.

## References

1. S. Steinerberger, *A Remark on the Odd Area of Unit Disks*, arXiv:2606.08337, first posted 6 June 2026. https://arxiv.org/abs/2606.08337
2. A. Carmel and R. Pinchasi, *Some notes about the odd area of unit discs centered at points on a circle*, Australasian Journal of Combinatorics 87 (2023), 148–159. https://ajc.maths.uq.edu.au/pdf/87/ajc_v87_p148.pdf
3. R. Pinchasi, *On the odd area of the unit disc*, Israel Journal of Mathematics 256 (2023), 619–637. https://doi.org/10.1007/s11856-023-2518-4
4. A. Oren, I. Pak and R. Pinchasi, *On the Odd Area of Planar Sets*, Discrete & Computational Geometry 55 (2016), 715–724. https://www.math.ucla.edu/~pak/papers/odd_area.pdf
