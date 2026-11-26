# Pointwise entry scale and mean dilation of Reeve tetrahedra

## Finding
For an integer \(q\ge1\), let \(R_q=\operatorname{conv}\{(0,0,0),(1,0,0),(0,1,0),(1,1,q)\}\). For each real point \(p=(x,y,z)\), define \(\tau_q(p)=\inf\{t\ge0:p\in tR_q+\mathbb Z^3\}\). Write \(\{h\}=h-\lfloor h\rfloor\), \(w=\{z\}/q\), \(u=\{x-w\}\), and \(v=\{y-w\}\). Then
\[
\tau_q(p)=w+\max(u,v)+q^{-1}\{q\min(u,v)\}.
\tag{1}
\]
The covering radius is \(1+2/q\) (a supremum, never a pointwise value). The mean of \(\tau_q\) over the unit torus is \(2/3+1/q-1/(6q^2)\). At a uniform torus point it couples to the maximum of two independent unit uniforms with nonnegative error less than \(2/q\), giving a limit with cumulative distribution \(s^2\) for \(0\le s\le1\).

## Proof
Relative to an integer translate, the three coefficients of the nonzero vertices must be nonnegative and sum to at most \(t\). The height of the apical coefficient forces it to be \(w+j/q\) with integer \(j\ge0\). At this height the smallest first two coefficients are \(\{u-j/q\}\) and \(\{v-j/q\}\), obtained by choosing the largest admissible integer translate in each horizontal coordinate. The candidate scale thus increases by one when \(j\) is increased by \(q\). For \(0\le j<q\) it is
\[
 w+u+v-j/q+\mathbf 1_{u<j/q}+\mathbf 1_{v<j/q}.
\]
If \(j/q>\min(u,v)\), this is strictly larger than the value at zero, since \(j/q<1\). Otherwise both indicators vanish and the largest feasible \(j\), namely \(\lfloor q\min(u,v)\rfloor\), is optimal. The exact minimum is attained, including at integer or grid boundaries, and simplifies to (1).

Modulo the lattice, \((w,u,v)\) ranges over the product \([0,1/q)\times[0,1)^2\). The three summands in (1) are respectively less than \(1/q,1,1/q\). These bounds are approached simultaneously by taking \(w\uparrow 1/q\), \(\max(u,v)\uparrow 1\), and \(\min(u,v)\uparrow 1/q\) from below, including when \(q=1\). Attainment of the entry minimum and nesting of the dilates give the covering radius as the supremum of (1).

Under uniform torus measure \(u,v\) are independent unit uniforms, independent of uniform \(w\) on \([0,1/q)\): conditional on \(z\), the horizontal transformation is a torus translation. Thus \(\mathbb Ew=1/(2q)\) and \(\mathbb E\max(u,v)=2/3\). The minimum has density \(2(1-a)\) on \([0,1]\). Dividing into its \(q\) fractional-part intervals gives
\[
\mathbb E\{q\min(u,v)\}=\frac{2}{q}\sum_{j=0}^{q-1}\int_0^1 h\bigl(1-(j+h)/q\bigr)\,dh=\frac{3q-1}{6q}.
\]
This yields the mean. Subtracting \(\max(u,v)\) from (1) gives the deterministic coupling bound.

## Relation to prior work and scope
The earlier *Cubic overlap spectrum of minimal Reeve-prism lattice coverings* (Resultary, 25 October 2026, Finding equation (2) and proof, [record](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-cubic-overlap-spectrum-of-minimal-reeve-prism-lattice-coverings--144458c7c9ab)) already determines the unscaled uncovered fraction for \(q\ge2\). Indeed, for interior horizontal coordinates exactly one horizontal translate has a nonempty vertical fiber. Each fiber of \(R_q\) is an interval; adding the unit vertical segment increases its vertical translate count by exactly one. Thus the earlier thickened body's singly covered set agrees almost everywhere with the tetrahedron's uncovered set. At \(q=1\) the unscaled covered fraction is the simplex volume \(1/6\), since its interior embeds in the unit cube. This unit-scale statistic is not part of the present finding.

Lian and Xue, [arXiv:2606.14584v1](https://arxiv.org/abs/2606.14584), §4.2, give vertical fibers and study inclusion-minimal covering by the thickened body. The inspected statements at unit scale do not give the all-dilations entry law, its supremum or mean. Codenotti–Santos–Schymura, [arXiv:1903.02866v2](https://arxiv.org/abs/1903.02866), use the same lattice covering radius but their non-hollow simplex hypotheses do not apply. Codenotti–Freyer–Krivokuća, [arXiv:2606.14442v1](https://arxiv.org/abs/2606.14442), give, in particular, covering-radius inequalities for planar Minkowski sums. These comparisons are bounded; historical priority is not certified. The result is only for this three-dimensional family and the standard integer lattice.

## Verification
The proof handles all real points. A separate bounded finite check directly enumerated candidate integer translates and their feasible barycentric sums on a rational grid at heights \(1,2,3,6\); all 864 exact comparisons agreed with (1). Details of the enumeration are in `VERIFICATION.md`. A finite grid alone is not a proof.
