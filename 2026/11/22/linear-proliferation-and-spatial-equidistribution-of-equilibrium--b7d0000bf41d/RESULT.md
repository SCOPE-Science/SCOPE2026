# Linear proliferation and spatial equidistribution of equilibrium lines in a cosine–memristor map

## Finding

For fixed \(0<\mu\le1\) and fixed \(h\in\mathbb R\), the number of equilibrium **lines**, not the total number of equilibrium points, of the published three-dimensional cosine–memristor map grows linearly with its amplification parameter \(\gamma\to\infty\). Let
\[
L_\mu(t)=\log(3-4\mu t(1-t)),\qquad
\vartheta_\mu(t)=4\pi\mu t(1-t),\qquad k=\frac1{10}.
\]
There exist unique \(a_\mu<0<b_\mu<1/2\) such that
\[
a_\mu L_\mu(a_\mu)=-k,\qquad b_\mu L_\mu(b_\mu)=k.
\]
The distinct equilibrium-line count is
\[
N_{\mu,\gamma}
=\frac{\gamma}{\pi}\big(\vartheta_\mu(b_\mu)-\vartheta_\mu(a_\mu)\big)+O_\mu(1)
=4\mu\gamma\big[b_\mu(1-b_\mu)-a_\mu(1-a_\mu)\big]+O_\mu(1).
\]
If the lines have parameters \(p_1,\ldots,p_{N_{\mu,\gamma}}\), their empirical measure converges in Wasserstein-1 distance with error \(O_\mu(\gamma^{-1})\) to
\[
\rho_\mu(t)\,dt=
\frac{1-2t}{b_\mu(1-b_\mu)-a_\mu(1-a_\mu)}
\boldsymbol1_{(a_\mu,b_\mu)}(t)\,dt.
\]
For each fixed \(h\), at most \(O_{\mu,h}(1)\) lines fail to have both transverse Jacobian multipliers of modulus exceeding one **at every point** on the line. Their proportion is therefore \(O_{\mu,h}(\gamma^{-1})\). A neutral tangent multiplier remains exactly one.

## Assumptions and scope

The state space is \(\mathbb R^3\), amplification \(\gamma>0\), \(0<\mu\le1\), and \(h\in\mathbb R\) is fixed as \(\gamma\to\infty\). Write
\[
P_{\mu,\gamma}(t)=\frac{k\cos(\gamma\vartheta_\mu(t))}{L_\mu(t)},\qquad
T_{\mu,\gamma,h}(x,y,z)
=\big(P_{\mu,\gamma}(x)+h\sin z(x-y),
P_{\mu,\gamma}(y)-h\sin z(x-y),z+x-y\big).
\]
The logarithm is real and positive because \(3-4\mu t(1-t)\ge 2\) for all real \(t\). A line means a connected one-dimensional fixed set \(\{(p,p,z):z\in\mathbb R\}\). Constants in asymptotic bounds may depend on the displayed fixed parameters, but not on \(\gamma\), \(z\), or on a selected equilibrium root.

## Proof

**1. Reduction to a compact scalar equation.** The third fixed-point equation forces \(x=y=p\), and the first two then agree and give \(P_{\mu,\gamma}(p)=p\). Put \(g_\mu(t)=tL_\mu(t)/k\). Then the scalar equation is \(\cos(\gamma\vartheta_\mu(t))=g_\mu(t)\).

The derivative of \(g_\mu\), multiplied by \(k\), equals \(L_\mu+tL_\mu'\). It is positive when \(t<0\) because \(tL_\mu'(t)>0\), and for \(t\ge1/2\) because \(tL_\mu'(t)\ge0\). For \(0\le t\le1/2\),
\[
L_\mu(t)+tL_\mu'(t)
\ge\log2-\frac{4\mu t(1-2t)}{3-4\mu t(1-t)}
\ge\log2-\frac14>0.
\]
Thus \(g_\mu\) is strictly increasing on the real line. The bounds \(|g_\mu(t)|\ge|t|\log2/k\), together with \(g_\mu(0)=0\), give unique endpoints \(a_\mu<0<b_\mu<k/\log2<1/2\). The scalar roots lie exactly in \([a_\mu,b_\mu]\). On this compact interval,
\[
\vartheta_\mu'(t)=4\pi\mu(1-2t)>0,
\qquad g_\mu'(t)>0.
\]

**2. Quantization and uniform counting discrepancy.** On the closed root interval define \(u(t)=\arccos(g_\mu(t))\); this decreases continuously from \(\pi\) to \(0\). Every scalar root solves one of the two quantizations
\[
\gamma\vartheta_\mu(t)-u(t)=2\pi j,\quad\text{or}\quad
\gamma\vartheta_\mu(t)+u(t)=2\pi j,
\qquad j\in\mathbb Z.
\]
The minus-phase is strictly increasing, hence its number of intersections with the integer lattice over any prefix \([a_\mu,t]\) equals \(\gamma(\vartheta_\mu(t)-\vartheta_\mu(a_\mu))/(2\pi)+O(1)\), uniformly in that prefix.

For the plus-phase, \(-u'(t)=g_\mu'(t)/\sqrt{1-g_\mu(t)^2}\) is bounded on compact interior subintervals. Near the left endpoint it equals \(c_a(t-a_\mu)^{-1/2}(1+O(t-a_\mu))\), and near the right endpoint it equals \(c_b(b_\mu-t)^{-1/2}(1+O(b_\mu-t))\), for positive constants \(c_a,c_b\); these expansions follow by Taylor expansion of \(g_\mu\), using its strictly positive endpoint derivatives. Moreover, \(-u'\) is strictly decreasing sufficiently near the left endpoint and strictly increasing sufficiently near the right endpoint. Because \(\vartheta_\mu'\) is smooth and uniformly positive, for sufficiently large \(\gamma\) the derivative of the plus-phase has just two zeros, one within \(O_\mu(\gamma^{-2})\) of each endpoint; it is positive between them. Indeed the derivative of \(-u'\) has order \(\gamma^3\) at either crossing, dominating the \(O(\gamma)\) derivative of \(\gamma\vartheta_\mu'\). Each short turning segment contributes at most a fixed number of additional roots: its total phase variation is \(O(1)\). Consequently its number of intersections over **every** prefix is also \(\gamma(\vartheta_\mu(t)-\vartheta_\mu(a_\mu))/(2\pi)+O(1)\), uniformly in \(t\) and \(\gamma\). Endpoints common to both quantizations contribute at most two duplicate roots. Thus, uniformly for \(a_\mu\le t\le b_\mu\),
\[
\#\{p\le t:P_{\mu,\gamma}(p)=p\}
=\frac\gamma\pi\big(\vartheta_\mu(t)-\vartheta_\mu(a_\mu)\big)+O_\mu(1).
\]
Taking \(t=b_\mu\) proves the displayed root-count law. Normalization by \(N_{\mu,\gamma}\) gives a uniform distribution-function discrepancy \(O_\mu(\gamma^{-1})\) from the law with CDF \((\vartheta_\mu(t)-\vartheta_\mu(a_\mu))/(\vartheta_\mu(b_\mu)-\vartheta_\mu(a_\mu))\). Differentiating gives \(\rho_\mu\). In one dimension, Wasserstein-1 distance is the integral of the absolute CDF difference; the common compact support proves the claimed rate.

**3. Transverse multipliers and exceptional lines.** At an equilibrium \((p,p,z)\), the Jacobian is
\[
D T=\begin{pmatrix}
P'(p)+h\sin z&-h\sin z&0\\
-h\sin z&P'(p)+h\sin z&0\\
1&-1&1
\end{pmatrix}.
\]
Its eigenvalues are exactly \(1\), \(P'(p)\), and \(P'(p)+2h\sin z\). The scalar derivative satisfies
\[
P'(p)=-\frac{k\gamma\vartheta_\mu'(p)}{L_\mu(p)}\sin(\gamma\vartheta_\mu(p))
-\frac{pL_\mu'(p)}{L_\mu(p)}.
\]
The second term is uniformly bounded on \([a_\mu,b_\mu]\), and the first prefactor is bounded below by a positive constant times \(\gamma\). If some point of a line has a transverse multiplier of modulus at most one, then \(|P'(p)|\le1+2|h|\), whence \(|\sin(\gamma\vartheta_\mu(p))|=O_{\mu,h}(\gamma^{-1})\). At a scalar root, \(\cos(\gamma\vartheta_\mu(p))=g_\mu(p)\), so \(1-|g_\mu(p)|=O_{\mu,h}(\gamma^{-2})\). Strict positivity of \(g_\mu'\) implies that \(p\) lies within \(O_{\mu,h}(\gamma^{-2})\) of one of the two endpoints. The uniform prefix-count bound from step 2 shows only \(O_{\mu,h}(1)\) roots can lie in these two shrinking strips. Every other line has both transverse multipliers of modulus greater than one uniformly for all \(z\), and the remaining multiplier is exactly one.

## Verification

The self-contained script `check_equilibrium.py` evaluates both endpoint equations, numerically enumerates scalar roots for \(\mu\in\{0.1,0.5,1\}\) and \(\gamma\in\{3,11,29,80,151,400\}\), checks every enumerated root against the full three-dimensional map, verifies the Jacobian eigenvalue identity, and checks the count and empirical-distribution approximations. It uses only the Python standard library. Run `python check_equilibrium.py` alongside this document. This finite diagnostic is not a proof of the asymptotic estimates; the proof is analytical above.

## Relationship to prior work

Peng, Shi, Li, Xiang, Dai, and Li introduced the coupled three-dimensional map and examined simulated orbits, stability and an equilibrium calculation. The underlying one-dimensional cosine/logarithm amplifier was introduced by Mansouri and Wang. The present result resolves the global real equilibrium-line census as amplification grows and gives a limiting spatial law and an almost-everywhere-in-the-line-census transverse expansion statement. These are not consequences of the published numerical bifurcation plots or the displayed local linearization at a single candidate equilibrium. The usual elementary oscillatory-phase counting method is an ingredient, not an assertion of priority for the method itself.

## Limitations

The theorem is a fixed-\(\mu\), fixed-\(h\) high-amplification result, not uniform as \(\mu\downarrow0\), or when \(h\) grows with \(\gamma\). It counts equilibrium lines, not individual equilibrium points, and makes no claim that typical forward trajectories visit those lines, nor about a stationary chaotic measure or encryption security. An inaccessible earlier treatment of the scalar amplifier could in principle contain a partial or equivalent fixed-point count; the associated priority risk remains. All novel statements require independent examination before publication.

## References

1. S. Peng, H. Shi, R. Li, Q. Xiang, S. Dai, Y. Li, *Simulink Modeling and Analysis of a Three-Dimensional Discrete Memristor Map*, Symmetry 16 (2024), 990. https://doi.org/10.3390/sym16080990. First published 2024-08-05.
2. A. Mansouri, X. Wang, *A novel one-dimensional chaotic map generator and its application in a new index representation-based image encryption scheme*, Information Sciences (2021). https://doi.org/10.1016/j.ins.2021.02.022.
