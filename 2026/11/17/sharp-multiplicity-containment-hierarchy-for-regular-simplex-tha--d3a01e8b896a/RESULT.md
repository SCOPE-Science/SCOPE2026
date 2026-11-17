# Sharp multiplicity containment hierarchy for regular-simplex Thales balls

## Finding
Let \(d\ge2\), and let \(P\subset\mathbb R^d\) be a regular \(d\)-simplex whose vertices \(v_0,\ldots,v_d\) lie on the unit sphere about its centroid, chosen as the origin. For each vertex let \(D_i\) be the **closed Thales ball** with diameter from the origin to \(v_i\), and, for \(1\le m\le d+1\), put
\[
U_m=\{x\in\mathbb R^d:\#\{i:x\in D_i\}\ge m\}.
\]
Let \(\gamma_P(x)=\inf\{\lambda\ge0:x\in\lambda P\}\) be the centroidal Minkowski gauge of the simplex. Then for every integer \(1\le m\le d\),
\[
\boxed{\max_{x\in U_m}\gamma_P(x)
 =\Lambda_{d,m}:=\frac{1+\sqrt{d(d+1-m)/m}}{2}.}
\]
The equality set consists of exactly \((d+1)\binom dm\) points, indexed by a distinguished vertex \(k\) and an \(m\)-element subset \(I\subset\{0,\ldots,d\}\setminus\{k\}\), explicitly described below. Moreover \(U_{d+1}=\{0\}\).

In particular, \(U_m\subseteq P\) **if and only if** \(m\ge d\). Thus at least \(d\) of the \(d+1\) Thales balls can overlap only inside the simplex, while every lower positive multiplicity has points outside it. For fixed \(m\), \(\Lambda_{d,m}\sim d/(2\sqrt m)\) as \(d\to\infty\).

## Assumptions and scope
The dimension is a positive integer \(d\ge2\), and all balls, the simplex, and its homothetic copies are closed. Unit circumradius and centroid at the origin are normalization choices: the dimensionless containment factors and counts remain unchanged under translations and similarities. The asserted equality count is for distinct **points in Euclidean space**, not labeled representations. The multiplicity counts ball membership including boundaries.

The normalized regular-simplex relations are
\[
\|v_i\|=1,\qquad \langle v_i,v_j\rangle=-1/d\quad(i\ne j),
\qquad\sum_{i=0}^d v_i=0.
\]
For \(x\ne0\), let \(x=ru\) with \(r>0\), \(\|u\|=1\), and write \(a_i(u)=\langle u,v_i\rangle\). Let \(a_{[1]}(u)\ge\cdots\ge a_{[d+1]}(u)\) denote the descending order statistics.

## Proof
**1. Radial membership and simplex gauge.** Completing the square shows
\[
 x\in D_i\quad\Longleftrightarrow\quad \|x\|^2\le\langle x,v_i\rangle.
\]
For \(x=ru\) with \(r>0\), this becomes \(r\le a_i(u)\), so \(ru\in U_m\) exactly when \(0<r\le a_{[m]}(u)\). The simplex facets are
\[
P=\{x:\langle x,v_i\rangle\ge-1/d\quad\forall i\},
\]
whence \(\gamma_P(ru)=dr(-a_{[d+1]}(u))\); the last parenthesis is strictly positive for every unit \(u\), since the sum of the \(a_i\) is zero and the vectors span the space. Thus for \(m\le d\), whenever \(a_{[m]}(u)>0\), the best point of that ray lies at \(r=a_{[m]}(u)\).

**2. A universal bound.** Select the indices \(I\) of the largest \(m\) inner products, and an index \(k\notin I\) of the smallest one. Put
\[
s_I=\frac1m\sum_{i\in I}v_i,\qquad t_k=-v_k,
\qquad \alpha_m=\|s_I\|=\sqrt{\frac{d+1-m}{dm}}.
\]
Then \(\|t_k\|=1\) and \(\langle s_I,t_k\rangle=1/d\). Since the mean of the top \(m\) inner products is no less than their minimum,
\[
0<a_{[m]}(u)\le \langle u,s_I\rangle,
\qquad -a_{[d+1]}(u)=\langle u,t_k\rangle>0.
\]
For any vectors \(s,t\) and unit vector \(u\),
\[
\langle u,s\rangle\langle u,t\rangle\le
 \frac{\|s\|\|t\|+\langle s,t\rangle}{2}.
\]
Indeed, this is the largest eigenvalue of the symmetric rank-two form \((st^{\mathsf T}+ts^{\mathsf T})/2\); alternatively it follows from the difference-of-squares identity applied to the unit-normalized \(s,t\). Consequently
\[
\gamma_P(ru)\le d\,a_{[m]}(u)(-a_{[d+1]}(u))
\le\frac d2\left(\alpha_m+\frac1d\right)=\Lambda_{d,m}.
\]
The zero vector also obeys the bound.

**3. Sharpness and all equality cases.** Conversely choose any index \(k\), any \(I\) of size \(m\) avoiding \(k\), and let
\[
w_{I,k}=\frac{s_I}{\alpha_m}-v_k,
\qquad u_{I,k}=\frac{w_{I,k}}{\|w_{I,k}\|},
\qquad r_{I,k}=\langle u_{I,k},s_I\rangle,
\qquad x_{I,k}=r_{I,k}u_{I,k}.
\]
Writing \(L=\|w_{I,k}\|=\sqrt{2+2/(d\alpha_m)}\), direct products give
\[
\langle u_{I,k},v_i\rangle=\frac{\alpha_m+1/d}{L}\quad(i\in I),
\qquad
\langle u_{I,k},v_k\rangle=-\frac{1+1/(d\alpha_m)}{L},
\]
and, for \(j\notin I\cup\{k\}\),
\[
\langle u_{I,k},v_j\rangle=\frac{1/d-1/(d\alpha_m)}{L}.
\]
Because \(0<\alpha_m\le1\), exactly the \(m\) indices in \(I\) attain the largest inner product, and \(k\) uniquely attains the smallest. Hence \(x_{I,k}\) belongs to **exactly \(m\)** Thales balls, and both inequalities in Step 2 are equalities: \(\gamma_P(x_{I,k})=\Lambda_{d,m}\).

Conversely, if \(x\in U_m\) attains the upper bound, the radial inequality must be an equality, all top \(m\) inner products must equal their mean, and the rank-two quadratic-form bound must be sharp. Since \(\langle s_I,t_k\rangle=1/d>0\), the positive eigendirection is uniquely \(s_I/\alpha_m+t_k\) up to a positive scalar; the negative eigendirection cannot satisfy the positive inner products. Thus \(x=x_{I,k}\). At this point the \(m\) largest values and the unique smallest value have exactly the index structure displayed above, so different pairs \((I,k)\) produce different points. There are exactly \((d+1)\binom dm\).

**4. Containment threshold and highest multiplicity.** The formula gives \(\Lambda_{d,m}>1\) precisely for \(m<d\), and \(\Lambda_{d,d}=1\). Since \(P=\{x:\gamma_P(x)\le1\}\), \(U_m\subseteq P\) precisely when \(m\ge d\). For \(m<d\), decreasing the positive radial coordinate of a maximizer slightly preserves membership strictly in all \(m\) chosen balls and keeps \(\gamma_P>1\), so the exterior overlap has nonempty interior. Finally if \(x=ru\ne0\) belonged to all \(d+1\) balls, then \(a_i(u)\ge r>0\) for every \(i\), contradicting \(\sum_i a_i(u)=0\). The origin belongs to all balls, so \(U_{d+1}=\{0\}\).

## Verification
The proof is exact and uses no computationally inferred step. The companion standard-library verifier `check_hierarchy.py` independently constructs coordinates for each simplex, checks the equality points directly against ball membership and the simplex gauge, checks their distinctness, and probes random directions for violations of the sharp bound. The numeric checks illustrate and stress-test the proof but do not constitute its all-dimensional justification. Run with `python3 check_hierarchy.py` from the same directory.

## Relationship to prior work
Polyanskii [1, Sections 1 and 4] surveys the geometric-graph problem of common intersections of diameter balls and uses regular simplices as canonical Euclidean extremal configurations. It does not analyze the radial extent of multiplicity layers of the centroid-to-vertex star. Pirahmad, Polyanskii, and Vasilevskii [2] prove intersection results for diametral balls induced by matchings and cycles, not the centroidal gauge of such layers. Pavlík [3, Theorem 5.1 and Corollary 5.3] proves that diameter balls cover arbitrary polytopes and their power diagram gives a subordinate tiling, but does not provide the **external spatial extent of every multiplicity layer**, the multiplicity containment threshold, or its equality counts. A planar overlap-containment statement for regular polygons includes the \(d=2,m=2\) special case; no new priority is claimed for that case alone.

## Limitations
This result concerns regular simplices with the source point at their centroid and balls determined by the source-to-vertex diameters. It does not classify arbitrary simplices, off-center sources, local overlap volumes, or the shapes of the full higher-dimensional multiplicity regions. The novelty comparison is based on identified public literature and accessible summaries of neighboring results; it is not a guarantee of historical priority. 

## References
[1] Alexander Polyanskii, *No-dimensional Tverberg-type problems*, arXiv:2506.13451v1, first posted June 16, 2025, https://arxiv.org/abs/2506.13451 (in particular Sections 1 and 4).

[2] Olimjoni Pirahmad, Alexandr Polyanskii, Alexey Vasilevskii, *Intersecting diametral balls induced by a geometric graph*, arXiv:2108.09795, first posted August 22, 2021, https://arxiv.org/abs/2108.09795 (in particular Section 1 and Theorems 1–4).

[3] Jan Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1, first posted November 10, 2026, https://arxiv.org/abs/2611.14277 (in particular Section 5).
