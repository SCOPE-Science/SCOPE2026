# Equidihedral ridge curvature and parity cancellation for Van Kampen–Flores polytopes

## Finding and scope

Let \(n\ge4\), \(H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}\) with its inherited Euclidean metric, \(\delta_i=e_i-\mathbf 1/n\), and \(\Omega_n=\operatorname{conv}\{\pm\delta_i:1\le i\le n\}\subset H_n\). Its intrinsic dimension is \(d=n-1\). Every ridge of \(\Omega_n\) is an \((n-3)\)-simplex, and all the ridges are congruent and have the same exterior dihedral angle. Their number \(r_n\) and exterior angle \(\alpha_n\) are
\[
 r_n=\begin{cases}
 \frac12\binom{n}{n/2}(n/2)^2,&n\text{ even},\\
 \frac12 n(n-1)\binom{n-1}{(n-1)/2},&n\text{ odd},
 \end{cases}
 \qquad
 \alpha_n=\begin{cases}
 \arccos(1-4/n),&n\text{ even},\\
 \arccos(1-1/(n-1)),&n\text{ odd}.
 \end{cases}
\]
The interior angle is \(\pi-\alpha_n\). Put \(\varepsilon_n=0\) for even \(n\) and \(\varepsilon_n=1\) for odd \(n\). The volume of each ridge \(F\) and the codimension-two intrinsic volume are
\[
 \mathcal H^{n-3}(F)=\frac{1}{(n-3)!}\sqrt{\frac{2(n-2)+\varepsilon_n}{n}},\qquad
 V_{n-3}(\Omega_n)=\frac{r_n\alpha_n}{2\pi(n-3)!}\sqrt{\frac{2(n-2)+\varepsilon_n}{n}}.
\]
In the classical Steiner normalization \(\operatorname{Vol}_d(K+tB_d)=\sum_{j=0}^d\kappa_{d-j}V_j(K)t^{d-j}\), the coefficient of \(t^2\) is \(\pi V_{d-2}(K)\). Both parity subsequences have the same leading normalized curvature:
\[
 \lim_{n\to\infty}\frac{(n-3)!\,V_{n-3}(\Omega_n)}{2^n n}=\frac{1}{4\pi}\sqrt{\frac{2}{\pi}}.
\]
The result concerns this Euclidean realization, not arbitrary affine deformations, irregular generators or other Bier spheres. It gives a leading equivalent, not a remainder estimate.

## Proof

**Polar edges and ridge count.** The signed vectors span \(H_n\), so the origin is interior relative to \(H_n\). Since \(\langle x,\delta_i\rangle=x_i\) for \(x\in H_n\), the polar is \(Q_n=H_n\cap[-1,1]^n\). A point in the relative interior of a polar edge has exactly \(n-2\) fixed saturated cube coordinates: with at least one free coordinate, the active coordinate constraints are independent on \(H_n\), and two free coordinates leave dimension one. Conversely, fix \(n-2\) coordinates to chosen signs. The two free coordinates \((x,y)\) then satisfy \(x+y=S\) in \([-1,1]^2\), where \(S\) is minus the sum of the chosen signs. Every nondegenerate segment so obtained is an edge, uniquely specified by its fixed coordinates and their signs.

In even order the only possibility is \(S=0\), with free-coordinate endpoints \((1,-1)\) and \((-1,1)\). Thus the number of edges is \(\binom n2\binom{n-2}{(n-2)/2}\), equal to the even formula for \(r_n\). In odd order the possibilities are \(S=\pm1\), with endpoints \((0,S)\) and \((S,0)\). **The nonzero entry keeps its sign when exchanged with the zero.** This gives \(2\binom n2\binom{n-2}{(n-3)/2}\) edges, equal to the odd formula for \(r_n\). Polarity pairs these edges with the ridges of \(\Omega_n\).

**Dihedral angles.** If \(u,v\) are adjacent polar vertices, the corresponding primal facets have outward normals \(u,v\), respectively. In even order the squared norms of these normals are both \(n\), and \(\|u-v\|^2=8\). In odd order both squared norms are \(n-1\), and \(\|u-v\|^2=2\). The identity for \(\langle u,v\rangle\) in terms of these squared norms gives the two displayed cosines of the angles between the outward unit normals.

**Congruence and volumes.** The dual ridge consists of the convex hull of the signed \(\delta_i\) at the \(N=n-2\) fixed coordinate positions, with sign vector \(s\in\{-1,1\}^N\). Their signs are balanced for even \(n\) and differ in count by one for odd \(n\), so coordinate permutations and global negation carry any ridge into any other ridge at fixed \(n\). Their vertex Gram matrix is \(G=I_N-ss^{\mathsf T}/n\), positive definite since \(N<n\). Hence the vertices are affinely independent, and their squared simplex volume multiplied by \(((N-1)!)^2\) is \(\det(G)\mathbf 1^{\mathsf T}G^{-1}\mathbf 1\). For example, this identity follows by taking the determinant after changing the vertex list to the first vertex and its \(N-1\) difference vectors, and using the corresponding cofactor for the difference Gram matrix. Here \(\det(G)=2/n\), \(G^{-1}=I_N+ss^{\mathsf T}/2\), and \((\sum_i s_i)^2=\varepsilon_n\). This gives the stated simplex volume.

**Intrinsic volume and limit.** A ridge's planar normal cone has aperture \(\alpha_n\), giving external angle \(\alpha_n/(2\pi)\). The polyhedral face formula therefore gives \(V_{d-2}\) as \(r_n\) times the common ridge volume times \(\alpha_n/(2\pi)\). At \(n=4\), this counts twelve unit edges with right exterior angles, so \(V_1=3\). Stirling's estimate gives \(r_n\sim (1/8)2^nn^{3/2}\sqrt{2/\pi}\) for even \(n\) and \(r_n\sim(1/4)2^nn^{3/2}\sqrt{2/\pi}\) for odd \(n\). Meanwhile \(\alpha_n\sim2\sqrt{2/n}\) for even \(n\) and \(\alpha_n\sim\sqrt{2/n}\) for odd \(n\), by the expansion of \(\arccos(1-x)\) at \(x=0\). The factor \(\sqrt{[2(n-2)+\varepsilon_n]/n}\) tends to \(\sqrt2\), producing the common limit.

## Verification and relationship to prior work

The companion `check.py` in the source package enumerates shared saturated coordinate constraints for \(n=4,\ldots,8\) and computes the corresponding Gram volumes and exterior angles. It already uses the shared-constraint test rather than a sign-change rule and needs no change. The checks are finite corroboration only. The complete parity-dependent classification follows from the two-coordinate segment argument above.

Jevtić and Živaljević, *Bier spheres of extremal volume and generalized permutohedra* ([arXiv:2108.00618](https://arxiv.org/abs/2108.00618)), identify the body and its polar median-hypersimplex realization. Jevtić, Timotijević and Živaljević, *Polytopal Bier spheres and Kantorovich–Rubinstein polytopes of weighted cycles* ([arXiv:1812.00397](https://arxiv.org/abs/1812.00397)), develop related opposite-simplex hulls. The claim here is the Euclidean ridge geometry and the resulting exact codimension-two intrinsic volume and parity-independent leading constant, not the polar model or the general intrinsic-volume face formula. Covariance of the same body and intrinsic volumes of ordinary hypersimplices are different invariants; the latter cannot be transferred to the polar by polarity alone.
