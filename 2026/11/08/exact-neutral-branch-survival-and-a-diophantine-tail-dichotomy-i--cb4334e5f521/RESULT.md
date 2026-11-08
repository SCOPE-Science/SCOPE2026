# Exact neutral-branch survival and a Diophantine tail dichotomy in a planar discontinuous map

## Finding

For a uniform initial condition in the two-step neutral-branch parallelogram of a planar three-branch stock-market map at its center bifurcation, the exact distribution of the first neutral-branch departure is determined by the gap lengths of a circle-rotation orbit. The residual probability of never departing is positive. After subtracting this atom, the remaining tail decays on the scale \(N^{-2}\) uniformly in time **if and only if** the rotation number has bounded continued-fraction coefficients. Unbounded coefficients give arbitrarily large normalized excursions. The exact rational-angle survival law and its dense arithmetic parameter discontinuities follow from the same formula.

## Assumptions and scope

Let \(0<c<4\), \(h>0\), \(d>h\), and \(\ell(x,y)=x-y\). At the center parameter \(b=1\) use the three-part map
\[
T(z)=\begin{cases}Jz+(d,0),&\ell(z)>h,\\Jz,&|\ell(z)|\le h,\\Jz-(d,0),&\ell(z)<-h,\end{cases}
\qquad J=\begin{pmatrix}2-c&-1\\1&0\end{pmatrix}.
\]
These are the model's middle and outer affine branches at the neutral center boundary; the outer translations play no role before the first departure. Define \(\theta=\arccos(1-c/2)\in(0,\pi)\) and \(\alpha=\theta/\pi\in(0,1)\). For each integer \(N\ge2\), define the convex survivor set
\[
K_N=\bigcap_{j=0}^{N-1}\{z\in\mathbb R^2:|\ell J^jz|\le h}.
\]
The starting law is normalized planar Lebesgue measure on \(K_2\), which has area \(4h^2/c\). For \(z\in K_2\) set \(L(z)=\min\{j\ge2:|\ell T^j(z)|>h}\), interpreted as \(\infty\) if there is no such index. This is the FIRST middle-branch departure time; no return-time or post-departure behavior is claimed. Boundary points have zero initial probability.

For any \(N\ge2\), let \(\phi_1<\cdots<\phi_s\) be the distinct elements of \(\{j\alpha\pmod1:0\le j<N}\), listed in \([0,1)\). Let \(g_i=\phi_{i+1}-\phi_i\) for \(i<s\) and \(g_s=1+\phi_1-\phi_s\). Every \(g_i>0\), and \(\sum g_i=1\).

## Proof

**1. Exact geometry of the neutral branch.** Write \(a=\cos\theta=1-c/2\), and introduce
\[
Q(x,y)=x^2-2axy+y^2.
\]
Direct multiplication shows \(Q(Jz)=Q(z)\). Its determinant is \(\sin^2\theta>0\); the change of coordinates from \(Q\) to a Euclidean squared norm has absolute area Jacobian \(\sin\theta\). The covector \(\ell\) has dual \(Q\)-norm squared \(2/(1+a)\), so \(|\ell(z)|\le h\) becomes a Euclidean strip between tangent lines at distance
\[
R=h\sqrt{(1+a)/2}=\frac h2\sqrt{4-c}
\]
from the origin. Iterating \(J\) rotates the strip normals by \(\theta\), up to orientation; using both sides of each strip includes their antipodes. Thus \(K_N\) becomes the intersection of strips tangent to a disk of radius \(R\), with normal directions at angles \(\pi\phi_i\) and \(\pi(1+\phi_i)\).

For a centered polygon tangential to a disk of radius \(R\) with consecutive outward-normal gaps \(\delta_j\in(0,\pi)\), the two half-edge lengths at a vertex are \(R\tan(\delta_j/2)\), hence its perimeter is \(2R\sum_j\tan(\delta_j/2)\) and area is \(R^2\sum_j\tan(\delta_j/2)\). Each circle gap \(g_i\) contributes twice with angular width \(\pi g_i\). Pulling back by the area Jacobian therefore gives the exact formula
\[
A_N:=\operatorname{area}(K_N)=\frac{2R^2}{\sin\theta}\sum_{i=1}^s\tan\frac{\pi g_i}2
=h^2\sqrt{\frac{4-c}c}\sum_{i=1}^s\tan\frac{\pi g_i}2.
\]
For \(N=2\), the two strips are linearly independent and \(A_2=4h^2/c\). Every orbit in \(K_2\) follows the middle branch until departure, so \(\Pr(L\ge N)=A_N/A_2\), giving
\[
\boxed{\Pr(L\ge N)=\frac{\sin\theta}2\sum_{i=1}^s\tan\frac{\pi g_i}2.}
\]
The first-departure mass at finite \(n\ge2\) is the difference of these probabilities at \(n\) and \(n+1\).

**2. Eternal survivors and rational resonances.** If \(\alpha\) is irrational, the strip normals are dense. The nested intersection \(K_\infty=\bigcap_NK_N\) is exactly \(\{Q(z)\le R^2}\), an ellipse of area \(\pi R^2/\sin\theta\). Consequently,
\[
\boxed{p_\infty:=\Pr(L=\infty)=\frac{\pi\sin\theta}4.}
\]
Every new irrational direction strictly cuts the previous tangential polygon, so each finite departure mass is strictly positive.

If \(\alpha=p/q\) in lowest terms, the distinct unoriented normals number exactly \(q\), equally spaced on a circle of length \(\pi\), so \(K_N=K_q\) for all \(N\ge q\). All its gaps are \(1/q\), giving
\[
\boxed{p_\infty=\frac{q\sin\theta}2\tan\frac{\pi}{2q}.}
\]
The cuts are strict at each \(2\le N<q\). The ratio of this rational mass to the continuously varying irrational-angle baseline is
\[
\frac{2q}\pi\tan\frac{\pi}{2q}
=1+\frac{\pi^2}{12q^2}+O(q^{-4}).
\]
As rational angles approach an irrational angle, their reduced denominators necessarily diverge. Thus the mass function is continuous at irrational angles, but has a positive discontinuity at each rational angle, despite the density of rational angles.

**3. Arithmetic classification of the excess survival tail.** Suppose \(\alpha\) is irrational. Set \(f(t)=\tan(\pi t/2)-\pi t/2\) for \(0<t<1\). Using \(\sum g_i=1\) gives the exact positive excess
\[
D_N:=A_N-\operatorname{area}(K_\infty)
=\frac{2R^2}{\sin\theta}\sum_{i=1}^N f(g_i).
\]
The Taylor expansion of tangent has positive coefficients on \((0,\pi/2)\); therefore
\[
f(t)\ge\frac{\pi^3}{24}t^3\qquad(0<t<1).
\]
Jensen's inequality yields \(\sum g_i^3\ge N^-2\). Consequently \(D_N\ge (\pi^3R^2/(12\sin\theta))N^-2\) for all \(N\ge2\). This lower bound is universal.

For the upper bound when partial quotients are bounded by \(B\), let \(p_k/q_k\) be consecutive convergents of the irrational \(\alpha\), choosing \(q_k\le N<q_{k+1}\). Their standard inequalities are \(|\alpha-p_k/q_k|<1/(q_kq_{k+1})\) and \(q_{k+1}\le(B+1)q_k\). The first \(q_k\) distinct fractional orbit points differ from the uniform grid \(\{j p_k/q_k\pmod1:0\le j<q_k}\) by at most \(1/q_{k+1}\). Hence their largest circular gap is at most \(1/q_k+2/q_{k+1}\le3(B+1)/N\). Adding further orbit points cannot increase any gap. For large \(N\), all gaps are below \(1/2\); on this interval \(f(t)\le C t^3\) for an absolute constant \(C\). Thus
\[
D_N\le\frac{2R^2C}{\sin\theta}\sum_i g_i^3
\le\frac{2R^2C}{\sin\theta}(\max_i g_i)^2
=O_{B,c,h}(N^{-2}).
\]
This proves the matching quadratic estimate for bounded type.

Conversely, suppose the partial quotients are unbounded. Select a sequence of convergents for which \(q_{k+1}/q_k\to\infty\). Put \(N_k=\lfloor q_{k+1}/4\rfloor\), so \(N_k\ge q_k\) eventually. Every orbit point \(\{j\alpha}\), \(j<N_k\), lies within circular distance \(1/(4q_k)\) of the grid point \(\{jp_k/q_k}\), since \(j|\alpha-p_k/q_k|\le1/(4q_k)\). All \(q_k\) grid neighborhoods contain at least one of the first \(q_k\) orbit points, and successive neighborhoods are separated by gaps of length at least \(1/(2q_k)\). Thus at least \(q_k\) distinct circular gaps satisfy this lower bound, whence
\[
\sum_i g_i^3\ge\frac1{8q_k^2},\qquad
N_k^2D_{N_k}\ge C_{c,h}\left(\frac{q_{k+1}}{q_k}\right)^2\longrightarrow\infty.
\]
Here \(C_{c,h}>0\) depends only on the fixed map parameters; floor effects vanish along the selected sequence. Since \(\Pr(L\ge N)-p_\infty=D_N/A_2\), the same exact bounded-type if-and-only-if and unbounded-type limsup conclusions hold for the probability tail. This completes the proof.

## Verification

The accompanying standalone script `check_center_survival.py` clips finite intersections of half-planes directly, computes their areas by the shoelace formula, and compares against the independently evaluated circular-gap formula. It also checks exact rational specializations, rational stabilization, and initial-state normalization. Running `python3 check_center_survival.py` produced `PASS 207 supporting exact and numerical comparisons`. The proof of the infinite-time Diophantine dichotomy is analytic; finite tests do not certify it.

## Relationship to prior work

Gardini, Radi, Schmitt, Sushko and Westerhoff (2023) introduce this three-branch market map and describe the invariant polygon/ellipse on its center-bifurcation line, with rational/irrational rotation types. The exact finite-horizon neutral-branch survival function and its continued-fraction characterization of the approach to the eternal-survival atom are not stated in the inspected paper. Sushko and Gardini's earlier chapter treats the related two-branch center bifurcation, with invariant polygons and ellipses but without the precise survival statistic or sharp Diophantine equivalence proved here. The polygonal gap computation is elementary convex geometry; its dynamical identification and the arithmetic characterization of escape frequencies are the substantive claims, not a claim to have discovered the polygon/ellipse distinction.

## Limitations

The starting law is uniform on \(K_2\), not the full phase plane or an invariant probability distribution. The stopping event is departure from the middle branch, not divergence and not first return after departure. The parameter is exactly \(b=1\); the theorem does not assert stability for \(b\ne1\). The universal \(N^{-2}\) lower bound for irrational angles does not imply a two-sided bound for unbounded partial quotients. The theorem does not claim a limiting coefficient for bounded-type rotations. Published analogues of irrational-rotation polygon approximation may yield alternative proofs; an exhaustive priority determination has not been performed.

## References

1. L. Gardini, D. Radi, N. Schmitt, I. Sushko, F. Westerhoff, "A 2D piecewise-linear discontinuous map arising in stock market modeling: Two overlapping period-adding bifurcation structures," *Chaos, Solitons & Fractals* **176** (2023), article 114143, DOI: 10.1016/j.chaos.2023.114143. Lawful full text: https://fis.uni-bamberg.de/bitstreams/f7cf86a1-3705-49f7-aba3-a1829808b077/download. First online: 2023-10-12.
2. I. Sushko and L. Gardini, "Center Bifurcation for a Two-Dimensional Piecewise Linear Map," chapter (2006), publicly available author's manuscript: https://www.mdef.it/public/fileadmin/whoiswho/gardini/Publications/Contributions_in_Multiauthor_Books_and_Proceedings/Ch2-SG-06.pdf.
3. Elementary continued-fraction convergent inequalities and the geometry of tangential polygons are invoked with complete arguments in the proof, without reliance on unpublished certificates.
