# An exponentially small inradius gap between prism and Möbius Laplacian simplices

## Finding

For each integer \(m\ge3\), consider two simple cubic graphs on \(2m\) vertices. The prism \(P_m=C_m\square K_2\) has two length-\(m\) cycles joined by corresponding rungs. The Möbius ladder \(M_{2m}\) has a length-\(2m\) cycle and chords joining opposite vertices. For any connected graph \(G\) on \(N\) vertices, write \(L_G\) for its unweighted graph Laplacian and consider the **canonical full-Laplacian Euclidean realization**
\[
T_G=\operatorname{conv}\{L_Ge_i:1\le i\le N\}\subset\{x\in\mathbb R^N:\mathbf1^{\mathsf T}x=0\}.
\]
The metric here is inherited from \(\mathbb R^N\); it is not the standard metric on an arbitrary lattice-basis representation of the simplex.

Set
\[
q=2-\sqrt3,\qquad h=q^m,\qquad S_m=\frac{(m^2-1)(m^2+11)}{720}.
\]
Define the positive real numbers
\[
A_m=S_m+\frac{m}{6\sqrt3}\frac{1+h}{1-h}+\frac{m^2h}{6(1-h)^2},
\]
\[
B_m=S_m+\frac{m}{6\sqrt3}\frac{1-h}{1+h}-\frac{m^2h}{6(1+h)^2}.
\]
Then both \((2m-1)\)-simplices have unique origin-centered inspheres and circumspheres. Their shared circumradius is \(\sqrt{12}\), while their **exact inradii** are
\[
r(P_m)=\frac1{\sqrt{2m A_m}},\qquad r(M_{2m})=\frac1{\sqrt{2m B_m}}.
\]
The spectral reciprocal-square traces obey the strict, explicitly positive gap
\[
\boxed{A_m-B_m=\frac{mh}{3}\left(\frac{2}{\sqrt3(1-h^2)}+\frac{m(1+h^2)}{(1-h^2)^2}\right)>0.}
\]
Therefore \(r(P_m)<r(M_{2m})\) for every \(m\ge3\), even though the two simplices have the same number of vertices, dimension, graph degree and circumradius. The precise asymptotics are
\[
r(P_m)\sim r(M_{2m})\sim6\sqrt{10}\,m^{-5/2},\qquad
\frac{r(M_{2m})}{r(P_m)}-1\sim\frac{120}{m^2}(2-\sqrt3)^m.
\]
In particular,
\[
r(M_{2m})-r(P_m)\sim720\sqrt{10}\,m^{-9/2}(2-\sqrt3)^m.
\]

## Assumptions and scope

All graphs are finite, simple, connected and unweighted. For \(M_{2m}\), label vertices by \(j\in\mathbb Z/(2m)\) and use edges from \(j\) to \(j+1\) and to \(j+m\); each opposite chord is included once. For \(P_m\), label vertices by \((j,\varepsilon)\) with \(j\in\mathbb Z/m\) and \(\varepsilon\in\{0,1\}\) and use rim and rung edges. The claim begins at \(m=3\) to avoid multigraph conventions for cycles of length two. All distances, radii, and polar normals are intrinsic to the specified Euclidean hyperplane of dimension \(2m-1\). This statement does not address arbitrary lattice-equivalent coordinates or weighted graphs.

## Proof

**1. Universal metric lemma, included for completeness.** Let a connected, vertex-transitive \(k\)-regular graph \(G\) have \(N\) vertices. Because \(L_G\) has kernel \(\operatorname{span}\{\mathbf1\}\) and rank \(N-1\), its \(N\) columns form the vertices of an \((N-1)\)-simplex whose barycenter is zero. Every vertex has norm \(\sqrt{k(k+1)}\). Their mean is zero, hence for any proposed circumball center \(z\) the average squared vertex distance is \(k(k+1)+\|z\|^2\). This forces the unique minimum enclosing sphere to be centered at zero, with radius \(\sqrt{k(k+1)}\).

For \(x\in\mathbf1^\perp\), the barycentric coordinate opposite column \(L_Ge_i\) is exactly \(N^{-1}+(L_G^+x)_i\), since \(L_G L_G^+x=x\) and these coordinates sum to one. Thus the facet halfspace is
\[
\langle L_G^+e_i,x\rangle\ge-\frac1N.
\]
Vertex transitivity makes all \(\|L_G^+e_i\|\) equal, so their squares are \(N^{-1}\operatorname{tr}((L_G^+)^2)\). Each facet is at distance
\[
\left(N\operatorname{tr}((L_G^+)^2)\right)^{-1/2}
\]
from the origin. A ball of that radius is contained in every facet halfspace. Conversely, if a center \(z\) supports a ball of at least that radius, all its barycentric coordinates must be at least \(1/N\); summing them shows every coordinate equals \(1/N\), and then \(L_G^+z=0\), yielding \(z=0\). This proves the radius is optimal, the center unique, and every facet tangent. This general lemma is independently known and is not proposed as a new result.

**2. Two graph spectra.** Diagonalizing the cyclic shift and the involution between the two layers of \(P_m\), the nonzero Laplacian eigenvalues split into
\[
\left\{2-2\cos\frac{2\pi j}{m}:1\le j<m\right\}
\quad\text{and}\quad
\left\{4-2\cos\frac{2\pi j}{m}:0\le j<m\right\}.
\]
On \(M_{2m}\), Fourier mode \(k\) on the length-\(2m\) cycle has Laplacian eigenvalue \(3-2\cos(\pi k/m)-(-1)^k\), since the chord sends it to \((-1)^k\) times itself. Its even and odd modes consequently give precisely the same first band and the *half-shifted* second band
\[
\left\{4-2\cos\frac{(2j+1)\pi}{m}:0\le j<m\right\}.
\]
In particular \(\operatorname{tr}((L_G^+)^2)\) for these graphs equals the sum of the squared reciprocals of the two nonzero spectral bands.

**3. Common first band.** The classical cotangent identity
\[
\sum_{j=0}^{m-1}\csc^2\left(x+\frac{\pi j}{m}\right)=m^2\csc^2(mx)
\]
implies \(\sum_{j=1}^{m-1}\csc^2(\pi j/m)=(m^2-1)/3\). Comparing the coefficients of \(x^2\) on both sides, using \(\csc^2x=x^{-2}+1/3+x^2/15+O(x^4)\) and \((\csc^2y)''=6\csc^4y-4\csc^2y\), gives
\[
\sum_{j=1}^{m-1}\csc^4(\pi j/m)=\frac{(m^2-1)(m^2+11)}{45}.
\]
Since \(2-2\cos(2\pi j/m)=4\sin^2(\pi j/m)\), the reciprocal-square trace of the common first band is exactly \(S_m\).

**4. Periodic versus antiperiodic second bands.** The Fourier series of the positive analytic function \(f(\theta)=(4-2\cos\theta)^{-2}\) is
\[
f(\theta)=\frac1{6\sqrt3}+\frac12\sum_{k=1}^{\infty}\left(\frac{k}{3}+\frac{2}{3\sqrt3}\right)q^k\cos(k\theta),\qquad q=2-\sqrt3.
\]
For instance, differentiate the absolutely convergent expansion of \((a-\cos\theta)^{-1}\) with respect to \(a\) at \(a=2\), then divide by four. Sampling at \(\theta=2\pi j/m\) selects frequencies divisible by \(m\); sampling at \(\theta=(2j+1)\pi/m\) multiplies the selected term at frequency \(\ell m\) by \((-1)^\ell\). Consequently
\[
\sum_{j=0}^{m-1} f(2\pi j/m)
=\frac{m}{6\sqrt3}\frac{1+h}{1-h}+\frac{m^2h}{6(1-h)^2},
\]
\[
\sum_{j=0}^{m-1} f((2j+1)\pi/m)
=\frac{m}{6\sqrt3}\frac{1-h}{1+h}-\frac{m^2h}{6(1+h)^2}.
\]
Subtracting gives
\[
\frac m2\sum_{\ell\ge1}\bigl(1-(-1)^\ell\bigr)\left(\frac{\ell m}{3}+\frac{2}{3\sqrt3}\right)h^\ell
=\frac{mh}{3}\left(\frac{2}{\sqrt3(1-h^2)}+\frac{m(1+h^2)}{(1-h^2)^2}\right),
\]
which is strictly positive. Combining with the metric lemma proves all exact formulas and the strict inequality.

**5. Sharp asymptotics.** Because \(0<q<1\), both reciprocal-square traces have leading term \(S_m\sim m^4/720\) and their difference satisfies \(A_m-B_m\sim m^2q^m/3\). Therefore \(r(P_m),r(M_{2m})\sim(2m\cdot m^4/720)^{-1/2}=6\sqrt{10}\,m^{-5/2}\). Expanding \(\sqrt{A_m/B_m}-1\) at one gives the asserted relative gap \(120q^m/m^2\), and multiplication gives the asserted absolute gap. All limits are along integers \(m\to\infty\).

## Verification

A standalone Python 3 checker accompanies this result. It constructs both adjacency-defined integer Laplacians, computes the Moore–Penrose inverses through the exact rational identity \(L^+=(L+J/N)^{-1}-J/N\), verifies \(LL^+=I-J/N\), and compares independently obtained rational reciprocal-square traces to the closed radical formulas using 65-digit decimal arithmetic for all integers \(3\le m\le10\). It also checks the sign and exact difference formulas over \(3\le m<50\), without treating these finite tests as proof for all \(m\). For example at \(m=3\), the exact reciprocal-trace difference is \(2/25\). The analytic spectral calculation supplies the all-integer proof.

## Relationship to prior work

Braun and Meyer introduced graph Laplacian simplices and studied their Ehrhart and lattice structure [1]. The general relation between the intrinsic Euclidean inradius of a vertex-transitive graph's Laplacian simplex and its Laplacian reciprocal-square trace is a previously established result [4]; the proof above recalls it only to isolate the new specialization. Lin defined the biharmonic index \(BH(G)=N\sum_{\lambda>0}\lambda^{-2}\) [2], precisely the reciprocal squared radius here. Azimi and Farrokhi gave full explicit Moore–Penrose inverse matrices for both circular and Möbius ladders, as well as their Kirchhoff indices and spanning-tree counts [3]. Those pseudoinverse identities are stronger entrywise data, but the inspected statements do not evaluate and compare their Frobenius squares or prove the strict insphere order and its sharp exponential gap. The present contribution is **the exact two-family metric comparison, its positive finite-size identity and its sharp decay law**, not the graph constructions, the general spectral-radius correspondence, or an independently new inverse matrix.

## Limitations

The conclusion is for the intrinsic full-Laplacian metric only; basis-dependent lattice simplex coordinates generally change Euclidean radii. The comparison is between precisely these two cubic graph families and does not state an order among all cubic graphs. Earlier inversion formulas contain sufficient data from which the new identities could in principle be calculated; an unlocated previous squared-Frobenius comparison or biharmonic-index specialization could alter historical priority. The finite checker corroborates the analytical argument but does not independently certify its proof or exhaust the literature.

## References

[1] B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085 (initial public version 2017-06-21), https://arxiv.org/abs/1706.07085.

[2] Z. Lin, *The biharmonic index of connected graphs*, arXiv:2110.09931 (initial public version 2021-10-18); AIMS Mathematics 7 (2022), 6050–6065, https://doi.org/10.3934/math.2022337.

[3] A. Azimi and M. Farrokhi Derakhshandeh Ghouchan, *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*, arXiv:2306.10497 (initial public version 2023-06-18), https://arxiv.org/abs/2306.10497. In particular, Corollaries 4.7 and 5.4.

[4] *Vertex-transitive Laplacian simplices have spectral inradii and degree-controlled circumradii*, 2026 mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-vertex-transitive-laplacian-simplices-have-spectral-inradii-and--841b23980b76. Its general metric lemma is acknowledged and reconstructed here.
