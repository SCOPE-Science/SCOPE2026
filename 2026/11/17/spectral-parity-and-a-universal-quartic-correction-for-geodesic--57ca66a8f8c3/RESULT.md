# Spectral parity and a universal quartic correction for geodesic polygons on thin flat Klein bottles

## Finding
Let \(K_{a,b}\) be the smooth rectangular flat Klein bottle obtained from the Euclidean plane by the isometries
\[
A(x,y)=(x+a,-y),\qquad B(x,y)=(x,y+b),\qquad a,b>0.
\]
Choose \(n\ge4\) points independently and uniformly by Riemannian area, connect them in their sampled cyclic order by almost surely unique minimizing geodesics, and close the loop. Write \(p_n(a,b)\) for the probability that this closed piecewise-geodesic loop reverses orientation. The loop need not be embedded.

Define the spectral numbers
\[
 c_j=\sum_{k\in\mathbb Z}\left[\frac{2(-1)^k}{(2k+1)\pi}\right]^j,\qquad j\ge2.
\]
These series converge absolutely. Every fixed polygon size \(n\ge4\) has the sharp thin-bottle expansion
\[
\boxed{p_n(a,b)=\frac{1-c_n}{2}+\frac{n c_{n-2}}{360}\left(\frac ba\right)^4+O_n\!\left((b/a)^6\right),\qquad a/b\longrightarrow\infty.}
\]
In particular **every polygon size has a strictly positive first finite-width correction, of order four rather than order two**. For odd \(j\), write \(\beta(j)=\sum_{r\ge0}(-1)^r/(2r+1)^j\) and, for even \(j\), use the Riemann zeta function. Then
\[
 c_j=2(2/\pi)^j\begin{cases}
 (1-2^{-j})\zeta(j),&j\text{ even},\\
 \beta(j),&j\text{ odd}.
 \end{cases}
\]
Thus the leading probabilities for four, five and six vertices and their first corrections are
\[
\begin{aligned}
p_4(a,b)&=\frac13+\frac1{90}(b/a)^4+O((b/a)^6),\\
p_5(a,b)&=\frac{19}{48}+\frac1{144}(b/a)^4+O((b/a)^6),\\
p_6(a,b)&=\frac{13}{30}+\frac1{180}(b/a)^4+O((b/a)^6).
\end{aligned}
\]
The limiting probability tends to \(1/2\) as the number of vertices grows, with the exact leading bias \(1/2-p_n^{(0)}=(2/\pi)^n[1+O(3^{-n})]\), where \(p_n^{(0)}=(1-c_n)/2\). The large-vertex statement applies to the **thin-bottle limit first**; the \(O_n\) in the aspect-ratio expansion is not uniform in \(n\).

## Assumptions and scope
The model is the intrinsic quotient metric of the Euclidean plane. Points are independent and uniform in the fundamental rectangle \([0,a)\times[0,b)\), representing a surface of area \(ab\). Shortest geodesics are almost surely unique, as the equal-length locus of distinct covering images has measure zero. The orientation character of the **closed loop** is invariant under changes of endpoint lifts; an isolated open geodesic has no lift-independent orientation character. All assertions hold for every fixed integer \(n\ge4\), with \(a/b\to\infty\) and \(b>0\) otherwise arbitrary. No embeddedness assumption is imposed.

## Proof
**1. Exact parity of each minimizing edge.** For horizontal representatives \(x_i\in[0,a)\) and vertical representatives \(y_i\in[0,b)\), let \(d_b(t)=\min_{m\in\mathbb Z}|t-mb|\). The nearest covering images from orientation-preserving and orientation-reversing deck transformations have squared lengths
\[
 L_{ij,+}^2=|x_i-x_j|^2+d_b(y_i-y_j)^2,\qquad
 L_{ij,-}^2=(a-|x_i-x_j|)^2+d_b(y_i+y_j)^2.
\]
This follows by separately minimizing over even and odd powers of the horizontal glide reflection, and then minimizing vertical translations. Ties form a null set. Introduce normalized \(X_i=x_i/a\), \(Y_i=y_i/b\) and the threshold perturbations
\[
 u_{ij}=\frac{d_b(y_i+y_j)^2-d_b(y_i-y_j)^2}{2a^2},\qquad
 |u_{ij}|\le\delta:=\frac{b^2}{8a^2}.
\]
An edge uses an orientation-reversing deck image exactly when \(|X_i-X_j|>1/2+u_{ij}\). Put \(K_u(x,z)=1-2\mathbf1_{\{|x-z|>1/2+u\}}\). The orientation sign of the polygon is the product of the edge signs. Every change of a vertex lift flips two adjacent edge signs and hence preserves this product. Thus
\[
1-2p_n(a,b)=\mathbb E\prod_{j=1}^{n}K_{u_{j,j+1}}(X_j,X_{j+1}),\quad X_{n+1}=X_1.
\tag{1}
\]

**2. The exact limiting spectral law.** Let \(T\) act on \(L^2([0,1])\) by the symmetric kernel \(K_0(x,z)\). The functions \(\varphi_k(x)=e^{i(2k+1)\pi x}\), \(k\in\mathbb Z\), form a complete orthonormal basis. Direct integration across the two threshold intervals gives
\[
T\varphi_k=\lambda_k\varphi_k,\qquad
 \lambda_k=\frac{2(-1)^k}{(2k+1)\pi}.
\]
As \(T\) is Hilbert–Schmidt, \(T^n\) is trace class for \(n\ge2\). The cyclic kernel integral is \(\operatorname{tr}(T^n)=c_n\). For fixed \(n\), dominated convergence in (1), or the explicit bounded interface perturbations below, yields \(\lim_{a/b\to\infty}(1-2p_n)=c_n\). Pairing the frequencies \(k\) and \(-k-1\) evaluates \(c_n\) by the zeta/beta formulas displayed above. In particular, the first listed values follow from \(c_2=1\), \(c_3=1/2\), \(c_4=1/3\), \(c_5=5/24\) and \(c_6=2/15\). The remaining eigenvalues are at most one third the leading eigenvalue in magnitude, giving the stated \(O(3^{-n})\) bias.

**3. The independent vertical moment.** For \(s,t\) independent uniform modulo \(b\), write \(z(s,t)=d_b(s+t)^2-d_b(s-t)^2\). The absolutely convergent Fourier expansion
\[
 d_b(t)^2=\frac{b^2}{12}+\frac{b^2}{\pi^2}\sum_{m\ge1}\frac{(-1)^m}{m^2}\cos(2\pi mt/b)
\]
shows that \(\mathbb E[z(s,t)\mid s]=0\). Orthogonality of the sine functions in
\[
 z(s,t)=-\frac{2b^2}{\pi^2}\sum_{m\ge1}\frac{(-1)^m}{m^2}\sin(2\pi ms/b)\sin(2\pi mt/b)
\]
gives \(\mathbb Ez^2=b^4/90\). Consequently
\[
 \mathbb Eu_{ij}=0,\qquad\mathbb Eu_{ij}^2=\frac{b^4}{360a^4},\qquad
 \mathbb E[u_{ij}u_{kl}]=0\quad\text{when }\{i,j\}\ne\{k,l\}
\tag{2}
\]
for edges of a simple cyclic polygon of length at least four. For edges sharing a vertex, the last identity follows by conditioning on the shared vertical coordinate and integrating the two independent other coordinates; disjoint edges are independent.

**4. Single-interface quadratic coefficient.** Keep all but one edge at threshold \(1/2\), and let \(C_n(h)\) be the signed cyclic integral with that one edge's threshold changed to \(h\). Spectral expansion and elementary integration give
\[
 C_n'(h)=4(1-h)\sum_{k\in\mathbb Z}\lambda_k^{n-1}\cos((2k+1)\pi h).
\]
The sums defining the first two derivatives converge absolutely for \(n\ge4\). At \(h=1/2\), the first derivative vanishes term by term. Differentiating again and using \(\lambda_k=2\sin((2k+1)\pi/2)/[(2k+1)\pi]\), we obtain
\[
 C_n'(1/2)=0,\qquad C_n''(1/2)=-4\sum_{k\in\mathbb Z}\lambda_k^{n-2}=-4c_{n-2}.
\tag{3}
\]
The kernel of \(T^2\) is Lipschitz (integrate the product of two bounded step kernels with moving intervals). Subsequent kernel compositions preserve this regularity. Equivalently, the Fourier expressions above have a locally Lipschitz second derivative at \(h=1/2\) for \(n\ge4\). Therefore a one-edge change by \(u\) contributes \(-2c_{n-2}u^2+O_n(|u|^3)\) to the signed integral.

**5. Interaction terms and error control.** Expand the product in (1) as the unperturbed product plus terms with one, two, or at least three changed edge kernels. For the three-or-more-edge terms, each difference kernel is bounded by \(2\) and is supported on a band \(||X_i-X_{i+1}|-1/2|\le\delta\). Any three distinct edges of a simple cyclic graph with \(n\ge4\) form a forest; eliminating leaves successively shows the probability of all three bands is \(O_n(\delta^3)\). Thus their total contribution is \(O_n(\delta^3)\).

For two distinct edges, the relevant difference forms are linearly independent. Integrating their two small bands, with the other step kernels fixed, has expansion \(A_{ij}u_i u_j+O_n(\delta^3)\), where \(A_{ij}\) is independent of the vertical coordinates. A possible third jump contributes only \(O_n(\delta^3)\): any three edge-difference bands form a forest and hence have the preceding volume bound. Averaging the leading double-edge term eliminates it by the last identity in (2). The one-edge terms contribute \(n(-2c_{n-2})b^4/(360a^4)\), by (2) and (3). Hence
\[
 1-2p_n(a,b)=c_n-\frac{n c_{n-2}}{180}(b/a)^4+O_n((b/a)^6).
\]
Rearranging proves the theorem. Positivity of \(c_{n-2}\) follows from its explicit zeta/beta representation; consequently the quartic coefficient is never zero. The error constants depend on \(n\), not on the overall similarity scale.

## Verification
The standalone `verify.py`, requiring only the Python standard library, independently checks nearest-deck-image parity against direct deck enumeration; checks known trace coefficients and the quadratic one-edge derivative using thousands of Fourier modes; and compares direct uniformly sampled polygons with the asymptotic formulas for four, five and six vertices and multiple aspect ratios. Invoke `python3 verify.py` in the directory containing the script. It reports `KLEIN_ALL_POLYGON_PARITY_QUARTIC_OK` on completion. Simulations are finite corroboration, not a proof of an infinite limit.

## Relationship to prior work
The geometric setting of flat Klein-bottle geodesics is classical; the early work of Matveev and the later conformal geometry of El Mir and Yassine provide context for the quotients and their geodesic structure. A published result titled *Quartic orientation-reversal cusp for random shortest-geodesic triangles on thin flat Klein bottles* already gives the three-vertex quartic coefficient \(1/120\). That triangle case is **excluded from the new-claim range**. A published *Exact two-point squared geodesic distance on rectangular flat Klein bottles* provides an exact unmarked random pair-distance representation but not closed-polygon orientation statistics. The earlier *Exact homotopy spectrum of random shortest-geodesic polygons on the round projective plane* and its higher-dimensional extension obtain spectral homotopy laws for projective spaces, not finite-width Klein-bottle polygons. *Sharp asymptotic contractibility rates for random minimizing geodesic polygons on flat two-tori* studies a different, translation-valued homotopy invariant of orientable surfaces. Those methods motivate the spectral comparison but do not supply the present all-size quartic correction. This statement concerns an explicit asymptotic theorem for every \(n\ge4\), not priority over the known three-vertex case or basic Fourier methods.

## Limitations
The expansion holds for each fixed polygon size as \(a/b\to\infty\); it is not uniform in the polygon size. No exact all-aspect probability is claimed, and no claim is made for a nonrectangular metric or nonuniform sampling. The parity of the full closed loop is intrinsic, whereas an individual edge parity depends on representatives. Historical priority remains provisional: general discussions of random winding on circles could contain the limiting constants; the finite-width coefficients are the specific newly assessed contribution. No independent mathematical or historical audit has been performed.

## References
- V. S. Matveev, *Quadratically integrable geodesic flows on the torus and on the Klein bottle*, arXiv:solv-int/9712019, initially posted 1997-12-23, https://arxiv.org/abs/solv-int/9712019.
- C. El Mir and Z. Yassine, *Conformal geometric inequalities on the Klein bottle*, arXiv:1209.6202, initially posted 2012-09-27, https://arxiv.org/abs/1209.6202.
- D. M. Davis and D. Recio-Mitter, *The geodesic complexity of n-dimensional Klein bottles*, arXiv:1912.07411, initially posted 2019-12-16, https://arxiv.org/abs/1912.07411.
- O. Glorieux and A. Yarmola, *Random triangles on flat tori*, arXiv:2003.08190, initially posted 2020-03-18, https://arxiv.org/abs/2003.08190.
- Published scientific records (2026): *Quartic orientation-reversal cusp for random shortest-geodesic triangles on thin flat Klein bottles*; *Exact two-point squared geodesic distance on rectangular flat Klein bottles*; *Exact homotopy spectrum of random shortest-geodesic polygons on the round projective plane*; *Sharp spectral homotopy law for random geodesic polygons in real projective spaces*; *Sharp asymptotic contractibility rates for random minimizing geodesic polygons on flat two-tori*.
