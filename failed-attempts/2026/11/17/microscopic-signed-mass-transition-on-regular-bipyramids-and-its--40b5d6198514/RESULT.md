# Microscopic signed-mass transition on regular bipyramids and its circle-plus-poles limit

## Finding

For each integer \(n\ge3\) and real height \(h>0\), let \(X_{n,h}\subset\mathbb R^3\) consist of the \(n\) equatorial points
\[
p_j=(\cos(2\pi j/n),\sin(2\pi j/n),0),\quad j=0,\ldots,n-1,
\]
and the two apices \(q_\pm=(0,0,\pm h)\). Every point is an exposed vertex of the convex bipyramid. Distances throughout are **ambient Euclidean chord lengths**, not surface-geodesic distances. Define
\[
s_n=\frac2n\cot\frac{\pi}{2n},\qquad T=\sqrt{1+h^2},\qquad d_n=2T-h-s_n.
\]
The microscopic weighting assigns the same coefficient \(a_{n,h}\) to each equatorial point and the same coefficient \(b_{n,h}\) to each apex, with
\[
\boxed{a_{n,h}=\frac{T-h}{n d_n}>0,\qquad
b_{n,h}=\frac{T-s_n}{2d_n},\qquad
E_{n,h}=\frac{T^2-hs_n}{d_n}.}
\]
Here \(na_{n,h}+2b_{n,h}=1\) and \(E_{n,h}\) is the exact maximal signed distance energy of a mass-one measure on the finite set; equivalently, it is the initial slope of its magnitude function. The denominator \(d_n\) is strictly positive for all allowed parameters. Setting
\[
\boxed{h_n=\sqrt{\frac4{n^2}\cot^2\frac{\pi}{2n}-1},}
\]
each apex coefficient is negative for \(0<h<h_n\), zero at \(h=h_n\), and positive for \(h>h_n\). The thresholds increase strictly with \(n\), starting at \(h_3=1/\sqrt3\), and
\[
\boxed{h_\infty=\sqrt{16/\pi^2-1},\qquad
h_\infty-h_n=\frac{4}{3h_\infty n^2}+O(n^{-4}).}
\]
The entire sign transition occurs **without any loss of exposed vertices or change of bipyramid face lattice**.

There is a compact counterpart. Let \(K_h\) be the union of the unit equatorial circle and the two apices \(q_\pm\), and let \(\sigma\) be normalized uniform arclength measure on that circle. Among **all finite signed Borel measures of total mass one** on \(K_h\), the distance energy
\[
I(\mu)=\iint_{K_h\times K_h}\|x-y\|_2\,d\mu(x)\,d\mu(y)
\]
has the unique maximizer
\[
\boxed{\mu_h=A_h\sigma+B_h(\delta_{q_+}+\delta_{q_-}),\quad
A_h=\frac{T-h}{2T-h-4/\pi},\quad
B_h=\frac{T-4/\pi}{2(2T-h-4/\pi)}.}
\]
Its maximum equals \(\bigl(T^2-4h/\pi\bigr)/(2T-h-4/\pi)\). The polar masses switch sign exactly at \(h=h_\infty\). If \(\mu_{n,h}\) denotes the finite microscopic measure on \(X_{n,h}\), then for every fixed \(h>0\), \(\mu_{n,h}\Rightarrow\mu_h\) weakly on \(K_h\) as \(n\to\infty\), with all the orbit-total coefficient errors of order \(O_h(n^{-2})\).

## Assumptions and scope

For any finite Euclidean set \(X=\{x_1,\ldots,x_m\}\) of pairwise distinct points, write \(D_{ij}=\|x_i-x_j\|_2\), \(Z_t=(e^{-tD_{ij}})_{ij}\) for \(t>0\), and \(w(t)=Z_t^{-1}{\bf1}\). Its microscopic weighting is \(\lim_{t\downarrow0}w(t)\), with total mass one, whenever this exists. In the present family it does exist uniquely. The signed distance energy of any finite mass-one vector \(z\) is \(z^TDz\), without restrictions on signs. For compact \(K_h\), maximization is specifically over finite signed Borel measures (finite total variation), not arbitrary distributions. All limits \(n\to\infty\) are over integers, with fixed \(h\) for the weak convergence assertion.

## Proof

**1. Strict negative type and the microscopic-energy principle.** For any compact Euclidean set and every nonzero finite signed Borel measure \(\xi\) supported on it with total mass zero, one has \(I(\xi)<0\). Indeed,
\[
\|x-y\|_2=\frac1{2\sqrt\pi}\int_0^\infty
(1-e^{-t\|x-y\|_2^2})t^{-3/2}\,dt,
\]
so, since \(\xi(K)=0\),
\[
I(\xi)=-\frac1{2\sqrt\pi}\int_0^\infty
\iint e^{-t\|x-y\|_2^2}\,d\xi(x)d\xi(y)\,t^{-3/2}dt<0.
\]
The integrals can be interchanged by compact support and finite variation, with cancellation at zero. Strict positivity of the inner Gaussian quadratic form for nonzero finite signed \(\xi\) follows from its strictly positive Fourier density and uniqueness of the Fourier transform of a finite measure. Thus, if a mass-one signed measure \(\mu\) has constant distance potential \(x\mapsto\int\|x-y\|_2d\mu(y)\) on its support set, then for every different mass-one measure \(\nu\), the cross term vanishes in \(I(\nu)-I(\mu)=I(\nu-\mu)+2I(\mu,\nu-\mu)\), giving strictly \(I(\nu)<I(\mu)\). Uniqueness follows. For finite Euclidean sets, the unique constant-potential mass-one vector is the microscopic weighting by the general existence theorem for finite strictly negative-type spaces [1, Theorem 4.11]; equivalently this follows from \(Z_t={\bf1}{\bf1}^T-tD+O(t^2)\) and inversion on the zero-sum subspace. The initial derivative of magnitude equals its maximizing energy by [1, Theorem 5.11].

**2. Symmetric finite stationarity.** The sum of chord distances from any equatorial vertex to the other equatorial vertices is
\[
\sum_{k=1}^{n-1}2\sin(\pi k/n)=2\cot(\pi/(2n))=n s_n.
\]
Each equatorial-to-apex distance is \(T\), and the distance between the apices is \(2h\). By rotational and reflection invariance and uniqueness, the coefficients of the constant-potential mass-one measure are \(a\) on the equator and \(b\) at each apex. Potential equality and mass normalization are precisely
\[
n s_n a+2Tb=nTa+2hb,\qquad na+2b=1.
\]
Writing \(A=na\), the equations become \((s_n-T)A+2(T-h)b=0\) and \(A+2b=1\), yielding \(A=(T-h)/d_n\), \(b=(T-s_n)/(2d_n)\). Their common potential equals
\[
s_nA+2Tb=\frac{T^2-hs_n}{d_n}.
\]
By step 1 this measure is uniquely maximizing and has exactly the microscopic coefficients stated.

**3. No denominator degeneracy, and the exact sign boundary.** For \(h>0\), the function \(2\sqrt{1+h^2}-h\) has global minimum \(\sqrt3\), attained at \(h=1/\sqrt3\). On the other hand, with \(x=\pi/(2n)>0\),
\[
s_n=\frac4\pi x\cot x<\frac4\pi<\sqrt3.
\]
Hence \(d_n>0\) uniformly. Also \(T-h=1/(T+h)>0\). The sequence \(s_n\) increases strictly because \(x\cot x\) decreases strictly on \((0,\pi/2)\): its derivative is \((\sin x\cos x-x)/\sin^2x<0\). Since \(s_3=2/\sqrt3>1\), the equation \(T=s_n\) has the unique positive solution \(h_n=\sqrt{s_n^2-1}\) and gives the complete sign classification. Every equatorial point is exposed by its radial linear functional, and each apex by an upward or downward vertical functional, for all \(h>0\); no face-lattice transition accompanies the weight sign change.

**4. Rate of approach of the critical heights.** The standard cotangent expansion gives
\[
s_n=\frac4\pi-\frac\pi{3n^2}+O(n^{-4}).
\]
The smooth map \(s\mapsto\sqrt{s^2-1}\), evaluated at \(s=4/\pi\), therefore gives
\[
h_\infty-h_n=\frac{(4/\pi)}{h_\infty}\frac\pi{3n^2}+O(n^{-4})
=\frac4{3h_\infty n^2}+O(n^{-4}).
\]

**5. The compact circle-and-poles maximizer.** The mean chord distance from any unit-circle point to \(\sigma\) is
\[
\frac1{2\pi}\int_0^{2\pi}2\left|\sin(\theta/2)\right|\,d\theta=\frac4\pi=:s.
\]
The two orbit potentials for \(\mu=A\sigma+b(\delta_{q_+}+\delta_{q_-})\) are \(sA+2Tb\) on the circle and \(TA+2hb\) at either pole. Solving \(sA+2Tb=TA+2hb\) together with \(A+2b=1\) gives the displayed \(A_h,B_h\). The same lower bound \(2T-h\ge\sqrt3>4/\pi\) makes these coefficients defined for all \(h>0\). The potential is constant everywhere on \(K_h\); the strict negative-type argument of step 1 proves unique optimality over **all** finite signed Borel mass-one measures, not only symmetric measures. The energy is this common potential, yielding the stated closed form. Its pole coefficient changes sign at \(T=4/\pi\), i.e. \(h=h_\infty\).

**6. Discrete-to-compact convergence.** The discrete equatorial uniform measures \(\sigma_n=n^{-1}\sum_{j=0}^{n-1}\delta_{p_j}\) converge weakly to \(\sigma\). The finite optimizer can be written \(\mu_{n,h}=A_{n,h}\sigma_n+b_{n,h}(\delta_{q_+}+\delta_{q_-})\), where \(A_{n,h}=(T-h)/(2T-h-s_n)\). Since \(s_n-s=O(n^{-2})\) and the denominator stays positive, \(A_{n,h}-A_h=O_h(n^{-2})\), \(b_{n,h}-B_h=O_h(n^{-2})\), and the finite maximal energies differ from the compact maximum by \(O_h(n^{-2})\). These assertions imply weak convergence. No rate for the weak convergence of the equatorial empirical measures against arbitrary continuous test functions is claimed.

## Verification

The standalone `verify.py` requires Python 3 and NumPy; run `python verify.py`. It independently builds full Euclidean distance matrices (rather than the two-orbit reduction), solves the mass-one linear system, checks energy and constant potential, numerically tests the strict negative-type quadratic form, validates the threshold ordering, and compares the compact-circle potential with high-resolution circular quadrature. At last execution it passed **2,158 assertions** on multiple heights and \(3\le n\le25\), with additional asymptotic checks through \(n=10{,}000\). The script is finite corroboration only: strict negative type, the sharp threshold, uniqueness on the compact set, and convergence are proved analytically above.

## Relationship to prior work

Roff and Willerton [1] introduced microscopic weighting and proved existence and its distance-energy interpretation for finite strictly negative-type metric spaces; this general theorem is **used**, not claimed here. Nickolas and Wolf [2] studied the maximal signed distance energy of general compact quasihypermetric spaces and the criterion of constant-potential measures; those general results likewise precede this calculation. The present specific contribution is the complete, all-height microscopic weighting of exposed-vertex regular bipyramids, a sharp integer-parameter boundary and its rate, and the explicitly computed **compact circle-with-two-poles signed energy maximizer** linked to the finite measures.

An earlier result on **planar staggered pairs of regular polygons** [3] already demonstrated negative microscopic mass on exposed vertices, so that phenomenon itself is **not** claimed to be new. Its two-dimensional two-ring chord matrix does not have the pole-to-pole distance \(2h\) or the same compact circle-plus-two-poles limit, and its threshold is instead a radius condition. Geodesic distance distributions on bipyramid surfaces are also different objects from ambient chord-distance energy. Searches and material comparisons found no exact existing statement implying this complete formula or compact limit, but mathematical priority is not established exhaustively.

## Limitations

The finite formula assumes equally spaced equatorial vertices, equal and opposite apex heights, and the ambient Euclidean chord metric. The compact optimization is restricted to **finite signed Borel measures**, not distributions of arbitrary order, and does not assert global microscopic-magnitude theory for arbitrary compact sets. The threshold does not imply that all microscopic weights on arbitrary convex polytope vertices are positive or negative. General negative masses at exposed vertices are already known [3]. Neither the finite numerical tests nor the absence of an equivalent record proves historical novelty; no independent audit was performed.

## References

[1] E. Roff and S. Willerton, *The microscopic weighting on a metric space*, arXiv:2607.05349, first publicly posted July 6, 2026; complete HTML revision inspected at https://arxiv.org/html/2607.05349v2 (Sections 4–6).

[2] P. Nickolas and R. Wolf, *Distance Geometry in Quasihypermetric Spaces. III*, arXiv:0809.0746, September 4, 2008; complete text at https://arxiv.org/abs/0809.0746 (Sections 3–5).

[3] *Negative microscopic weights at exposed vertices of staggered regular polygons*, publicly indexed research result, November 1, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-negative-microscopic-weights-at-exposed-vertices-of-staggered-re--9ce6bbdc7f59, full `RESULT.md` inspected.
