# Gaussian-optimal Crofton ball sections of higher-dimensional spherical tori

## Finding
Fix an integer \(d\ge3\) and a real \(R>1\). The unit-minor-radius spherical torus is the compact solid
\[
T_{d,R}=\{(x,z)\in\mathbb R^{d-1}\times\mathbb R:(\|x\|-R)^2+z^2\le1\}.
\]
Its boundary is diffeomorphic to \(S^{d-2}\times S^1\). Sample an unoriented affine hyperplane from Euclidean-motion-invariant hyperplane measure, conditional on intersecting the *interior* of this solid. Away from a null family of tangencies and topology transitions, precisely three intrinsic section homeomorphism types occur:
\[
\begin{array}{c|c}
\text{type}&\text{homeomorphism}\\
\text{outer-only}&S^{d-3}\times D^2\\
\text{ball}&D^{d-1}\\
\text{shell}&S^{d-2}\times[0,1]
\end{array}
\]
Here \(S^0\times D^2\) means two disjoint planar disks, recovering the classical three-dimensional classification. In dimensions \(d\ge4\) all generic cuts are connected; in \(d\ge5\) they are all simply connected, although the outer-only and shell types remain noncontractible.

Let \(B\in[0,\pi/2]\) have density proportional to \(\sin^{d-2}B\), write \(X=\sin B\), and set
\[
\mu_d=\mathbb E X=\frac{\Gamma(d/2)^2}{\Gamma((d-1)/2)\Gamma((d+1)/2)},\qquad Z_d(R)=1+R\mu_d.
\]
The exact conditional probabilities are
\[
\boxed{\begin{aligned}
P_{\rm outer}(d,R)&=\frac{\mathbb E(RX-1)_+}{Z_d(R)},\\
P_{\rm ball}(d,R)&=\frac{2\mathbb E\min(RX,1)}{Z_d(R)},\\
P_{\rm shell}(d,R)&=\frac{\mathbb E(1-RX)_+}{Z_d(R)}.
\end{aligned}}
\]
These are exhaustive and strictly positive for \(R>1\).

For each \(d\ge3\), the ball probability has a **unique global maximizing radius ratio** \(R_d\in(1,\infty)\). Put \(q=\Phi^{-1}(3/4)\), with \(\Phi\) and \(\varphi\) the standard-normal cdf and density. Then
\[
\boxed{\begin{aligned}
\lim_{d\to\infty}d(R_d-1)&=\frac{q^2}{2}=0.227468211559786\ldots,\\
\lim_{d\to\infty}d\left(1-P_{\rm ball}(d,R_d)\right)&=q\varphi(q)=0.214337041127870\ldots.
\end{aligned}}
\]
In particular, the radius maximizing the chance of a contractible affine cut approaches the horn-torus boundary at the exact order \(d^{-1}\), and the *best possible non-ball probability* has sharp order \(d^{-1}\).

## Assumptions and scope
The ambient dimension is any integer \(d\ge3\); minor radius is normalized to one, and \(R>1\) ensures the tube misses the rotational axis. The sampling law on unoriented hyperplanes \(H_{n,t}=\{u:\langle n,u\rangle=t\}\) is the unique invariant measure, proportional to spherical normal measure \(dn\) times Lebesgue offset measure \(dt\), conditioned on positive \((d-1)\)-dimensional section volume. It is not the law of hyperplanes through the origin. Equalities and topological classifications ignore a zero-measure family of tangent hyperplanes and threshold offsets. The ball and shell refer to the entire solid section, not the intersection of its boundary with the hyperplane. All asymptotics are for \(d\to\infty\) with the minor radius fixed to one.

## Proof
**1. A meridian disk and its axis contacts.** Write \(k=d-2\). Rotational invariance reduces a normal to \((\sin\beta,0,\ldots,0,\cos\beta)\), for \(\beta\in(0,\pi/2)\). Its hyperplane can be parametrized as
\[
(x_1,y,z)=(t\sin\beta+s\cos\beta,\ y,\ t\cos\beta-s\sin\beta),\qquad y\in\mathbb R^k.
\]
Set \(u=\|y\|\ge0\). At each fixed \(s\), the solid inequality gives a closed interval of allowed \(u\), possibly empty, because
\[
R-\sqrt{1-z^2}\le\sqrt{x_1^2+u^2}\le R+\sqrt{1-z^2}
\]
whenever \(|z|\le1\); the lower bound is positive since \(R>1\). The projection onto the \((x_1,z)\)-plane is the convex stadium \([-R,R]\times\{0\}+D^2\), so the allowed \(s\) form a single interval. Its radius endpoints vary continuously; therefore the resulting meridian region \(U\subset\{(s,u):u\ge0\}\) is a topological closed disk. Its contact with the boundary axis \(u=0\) is the intersection of the meridian line with the two disjoint unit disks centered at \((\pm R,0)\). Consequently, for generic \((\beta,t)\), the contact set consists of exactly \(j=0,1,\) or \(2\) closed boundary intervals. A standard planar straightening of a disk with \(j\) marked disjoint boundary intervals reduces rotation about \(u=0\) to the corresponding product/handle model: with no axis contact one obtains \(D^2\times S^{k-1}\); with one contact one obtains \(D^{k+1}\); with two contacts one obtains \(S^k\times[0,1]\). Explicitly, in the last two cases the \(S^{k-1}\) fibers collapse at the marked boundary arcs, yielding respectively a sphere-cap closure and a double sphere-cap closure. This proves the three asserted section homeomorphisms. It also shows why dimension three is the only disconnected case: there \(S^{k-1}=S^0\).

**2. Exact Crofton law.** By symmetry take \(t\ge0\), and put \(c=R\sin\beta\). The two meridian disks' signed center offsets from the hyperplane are \(t\mp c\). The whole solid is hit for \(0\le t<1+c\). Both disks are hit for \(0\le t<(1-c)_+\), and neither disk is hit for \(0\le t<(c-1)_+\); all other hitting offsets meet exactly one. Thus their conditional-offset lengths for nonnegative \(t\), in the order outer-only, ball, shell, are
\[
(c-1)_+,\quad 2\min(c,1),\quad (1-c)_+,
\]
whose sum is \(1+c\) in either case. A uniform normal has inclination density
\[
f_d(\beta)=\frac{2\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}\sin^{d-2}\beta
\quad(0\le\beta\le\pi/2).
\]
Integrating lengths over normals and dividing by \(\mathbb E(1+RX)=1+R\mu_d\) proves the three formulas. The moment \(\mu_d\) follows by beta integration. Every event has positive probability because \(X\) has positive density throughout \((0,1)\) and \(R>1\).

**3. Unique finite-dimensional optimizer.** Define \(N_d(R)=\mathbb E\min(RX,1)\). For \(R>1\), differentiation under the integral gives
\[
N_d'(R)=\mathbb E[X\mathbf1_{\{X<1/R\}}]>0,\qquad
N_d''(R)=-\frac{f_X(1/R)}{R^3}<0,
\]
where \(f_X\) is the strictly positive density of \(X\) on \((0,1)\). The sign of the derivative of \(P_{\rm ball}=2N_d/(1+R\mu_d)\) is that of
\[
G_d(R)=N_d'(R)(1+R\mu_d)-\mu_dN_d(R).
\]
It is strictly decreasing, since \(G_d'(R)=N_d''(R)(1+R\mu_d)<0\). At \(R\downarrow1\), \(N_d=\mu_d\) and \(N_d'=\mu_d\), giving \(G_d(1+)=\mu_d>0\). At \(R\to\infty\), \(N_d\to1\), \(N_d'\to0\), and \(G_d\to-\mu_d<0\). Hence there is precisely one critical point, and it is the strict global maximum. Comparing its objective value to the limit at \(R\downarrow1\), and using \(N_d\le1\), yields the useful global bound
\[
1<R_d\le\mu_d^{-2}.
\]

**4. Gaussian boundary layer.** For a uniform unit normal, \(Y_d=\sqrt d\,|n_z|\) converges in distribution to \(|Z|\), where \(Z\) is standard normal; moreover its fixed moments converge and remain uniformly bounded. Here \(X=\sqrt{1-n_z^2}\), so
\[
\mu_d=1-\frac1{2d}+O(d^{-2}),\qquad d(X-1)\ \Longrightarrow\ -\frac{Z^2}{2}
\]
with uniform integrability for the positive parts below. Fix \(\lambda\ge0\), set \(R=1+\lambda/d\), and write
\[
A(\lambda)=\mathbb E\bigl(\lambda-Z^2/2\bigr)_+.
\]
Dominated convergence (uniformly for \(\lambda\) in compact intervals by the Lipschitz property of the positive part) gives
\[
\begin{aligned}
d\,P_{\rm outer}(d,1+\lambda/d)&\longrightarrow A(\lambda)/2,\\
d\,P_{\rm shell}(d,1+\lambda/d)&\longrightarrow\bigl(A(\lambda)-\lambda+1/2\bigr)/2,\\
d\,[1-P_{\rm ball}(d,1+\lambda/d)]&\longrightarrow F(\lambda):=A(\lambda)-\lambda/2+1/4.
\end{aligned}
\]
The second relation uses \(\mathbb E(Z^2)=1\); the third follows by summing the other two. The finite-radius bound from step 3 and \(d(\mu_d^{-2}-1)\to1\) ensure that \(d(R_d-1)\) stays in a fixed compact interval. Thus compact-uniform convergence lets us pass the finite-dimensional minimizers to minimizers of \(F\).

With \(h=\sqrt{2\lambda}\) and \(\Phi,\varphi\) the standard-normal functions, direct integration yields
\[
A(\lambda)=(2\lambda-1)(\Phi(h)-1/2)+h\varphi(h),\quad
F'(\lambda)=2\Phi(\sqrt{2\lambda})-\tfrac32.
\]
The derivative is strictly increasing from \(-1/2\) to \(+1/2\). Therefore the **unique** minimizer is \(\lambda_*=q^2/2\), \(q=\Phi^{-1}(3/4)\). Substitution simplifies the minimum to \(F(\lambda_*)=q\varphi(q)\). Uniqueness and compactness prove both displayed limits at \(R_d\).

## Verification
Run `python3 check_tube.py` with Python 3, NumPy and SciPy. The checker uses beta-normalized one-dimensional quadrature, direct differentiation of the exact probability expression, nine-dimensional sweeps of the optimizer equation, four independent importance-weighted Gaussian-normal/offset Monte Carlo draws of 240,000 hyperplanes each, and the known three-dimensional circular-meridian formula as a cross-check. It passed 106 deterministic finite assertions and recovered \(d(R_d-1)\to0.227468\ldots\) and \(d(1-P_{\rm ball}^{\max})\to0.214337\ldots\). For example, \(R_4=1.078309203655\ldots\) gives \(P_{\rm ball}=0.929987889303\ldots\), whereas \(R_{200}=1.001143708345\ldots\) gives \(0.998922934916\ldots\). Finite tests corroborate but do not establish the topology for all hyperplanes or the limits for infinitely many dimensions; the proof above supplies those conclusions.

## Relationship to prior work
Peng Peng, *Existence of rotationally symmetric embedded f-minimal tori*, first posted 2026-05-06, produces a recently studied class of Euclidean-embedded rotational hypersurfaces of the same \(S^1\times S^{d-2}\) topological type. The present canonical circular-profile tube is **not** asserted to be any of Peng's \(f\)-minimal examples: the new question concerns affine-section topology under motion-invariant sampling. Moroni's toric-section exposition concerns three-dimensional intersection curves and classical quartics. A published three-dimensional convex-meridian Crofton law already includes the dimension-three circular-profile probability formulas as a special case; the present novelty claim concerns the dimensional change in generic section topology, the all-dimensional unique optimizer, and the sharp Gaussian optimization window and constant. A separate known study of centered circular-torus sections concerns their sectional area and a Villarceau logarithmic cusp, not the all-offset, all-dimension optimal ball probability here.

## Limitations
No formula is asserted for an arbitrary generating profile, a noncircular rotational hypersurface, or the \(f\)-minimal tori themselves. The exact probabilities rely on conditioning the motion-invariant **affine-hyperplane** measure on intersecting the solid. They do not apply to uniform central planes or surface-only intersections. The limiting constants concern the optimizer within this one-parameter circular-profile family; there is no claim of optimality among all rotational solids or all toroidal embeddings. The dimensional limit is first order and not a uniform finite-dimension error estimate. Historical overlap with unindexed higher-dimensional stereology literature remains possible. No independent mathematical audit has been performed.

## References
1. Peng Peng, *Existence of rotationally symmetric embedded f-minimal tori*, arXiv:2605.05022, first posted 2026-05-06, https://arxiv.org/abs/2605.05022 (full text https://arxiv.org/html/2605.05022v3).
2. Luca Moroni, *The toric sections: a simple introduction*, arXiv:1708.00803, first posted 2017-08-01, https://arxiv.org/abs/1708.00803; expository full text https://www.lucamoroni.it/toric-sections/.
3. *A three-topology Crofton law and inverse support tomography for convex-meridian toroids*, published research record 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-three-topology-crofton-law-and-inverse-support-tomography-for--8cf34e87984a.
4. *Logarithmic area cusp and Haar topology law at the Villarceau transition*, published research record 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-logarithmic-area-cusp-and-haar-topology-law-at-the-villarceau-tr--3f2e0b5e194a.
