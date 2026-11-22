# Maximal disconnected mobility-instability windows in an ecological cooperation network

## Finding

For every integer \(m\ge1\), a fixed network with \(m+1\) habitats and a fixed two-strategy ecological public-goods game can undergo exactly \(2m\) alternating transitions between local exponential stability and linear instability of its homogeneous positive coexistence state as **only one scalar common mobility level** rises. The \(m\) instability windows are disconnected. This attains the universal sharp upper bound of \(m\) windows for two species with positive diagonal diffusion on an undirected connected \((m+1)\)-node graph.

The ecological game parameters and ratio of defectors' to cooperators' mobility are fixed for the entire family. Only the number and fixed conductances of habitat corridors change between the networks in the family; **within each network, not a single corridor or kinetic parameter changes during a mobility sweep**. All corridor weights are positive and sum to one.

## Assumptions and scope

Define the local strategy densities \(u,v>0\), available ecological space \(z=1-u-v>0\), group size \(N=30\), game multiplier \(r=4\), baseline births \(b=1\), and death rate \(d=13/10\). Set

\[
S(z)=\sum_{j=0}^{29}z^j,\quad F(z)=1+3z^{29}-\frac{2}{15}S(z),\quad H(z)=\frac{4}{1-z}\left(1-\frac{S(z)}{30}\right).
\]

The local expected fitnesses are \(f_D=uH(z)\) and \(f_C=uH(z)-F(z)\), and the reaction functions are

\[
G_C(u,v)=u\{z[uH(z)-F(z)+1]-13/10\},\quad
G_D(u,v)=v\{z[uH(z)+1]-13/10\}.
\]

For every \(m\ge1\), let \(R=10(m+1)\) and consider the star with one center and leaves \(j=1,\ldots,m\), whose undirected spoke conductances are

\[
w_j=\frac{R^{j-1}}{\sum_{i=0}^{m-1}R^i}\quad(j=1,\ldots,m).
\]

With the **positive** weighted graph Laplacian \(\mathcal L\) (diagonal is weighted degree, off-diagonal is minus conductance), the ecological equations are

\[
\dot u_i=G_C(u_i,v_i)-\varepsilon(\mathcal L u)_i,\qquad
\dot v_i=G_D(u_i,v_i)-20\varepsilon(\mathcal L v)_i,
\]

for arbitrary \(\varepsilon>0\). This is the symmetric weighted-corridor extension of the unweighted simple-network diffusion model of Roy et al.; weighted corridors are an explicit extension, not a purported assumption of the original article. The homogeneous positive equilibrium exists independently of \(\varepsilon\).

## Proof

**1. Certified positive coexistence and local reaction stability.** Define \(z_*\) as the zero of \(F\) in the rational interval

\[
\frac{87766779091483}{10^{14}}<z_*<\frac{87766779091485}{10^{14}}.
\]

Direct exact-rational endpoint evaluations give \(F(z_{\rm left})>0>F(z_{\rm right})\), and interval evaluation gives \(F'<0\) throughout the interval. Put

\[
u_* =\frac{(13/10)/z_*-1}{H(z_*)},\qquad v_*=1-z_*-u_*.
\]

Exact rational interval arithmetic yields \(u_*\in(0.02007837048979,0.02007837048981)\), \(v_*\in(0.10225383859534,0.10225383859538)\), and hence a strictly interior zero of both reactions. For brevity write \(H_*=H(z_*)\), \(H'_* = H'(z_*)\), \(F'_* = F'(z_*)\), and

\[
A=-\frac{d}{z_*}+z_*H_*-z_*u_*H'_*,\qquad B=-\frac{d}{z_*}-z_*u_*H'_*.
\]

Differentiating the reactions at \((u_*,v_*)\), with \(\partial_u z=\partial_v z=-1\), gives the local Jacobian

\[
J=\begin{pmatrix}
 u_*(A+z_*F'_*)&u_*(B+z_*F'_*)\\
 v_*A&v_*B
\end{pmatrix}.
\]

The included dependency-free exact-rational checker verifies

\[
\begin{aligned}
&J_{11}\in(0.2453,0.2454),\quad J_{12}\in(-0.1771,-0.1769),\\
&J_{21}\in(1.7639,1.7642),\quad J_{22}\in(-0.3869,-0.3867),\\
&\operatorname{tr}J<0,\qquad \det J>0.
\end{aligned}
\]

Thus \((u_*,v_*)\) is linearly exponentially stable without spatial coupling.

**2. Two fixed instability thresholds for every graph mode.** For each nonzero positive eigenvalue \(\lambda\) of \(\mathcal L\), the linearized mode is \(J-x\operatorname{diag}(1,20)\), with \(x=\varepsilon\lambda\). Its trace is \(\operatorname{tr}J-21x<0\), and its determinant is

\[
p(x)=20x^2-(J_{22}+20J_{11})x+\det J.
\]

The exact rational certificate proves

\[
p(0.069)>0,\quad p(0.070)<0,\quad p(0.156)<0,\quad p(0.157)>0.
\]

Therefore this quadratic has precisely two distinct positive roots \(\alpha\in(0.069,0.070)\), \(\beta\in(0.156,0.157)\). Since the trace is negative for every \(x\ge0\), the mode is linearly exponentially unstable exactly when \(\alpha<x<\beta\), stable outside the closed interval, and has a zero eigenvalue at the two endpoints. In particular \(\beta/\alpha<157/69<3\).

**3. Spectral separation on one weighted star.** Order the positive spoke weights as \(w_1<\cdots<w_m\) (for \(m=1\), there is one weight). Let \(D=\operatorname{diag}(w_1,\ldots,w_m)\). A weighted incidence matrix \(Q\) of the star has \(QQ^\top=\mathcal L\) and

\[
Q^\top Q=D^{1/2}(I+\boldsymbol 1\boldsymbol 1^\top)D^{1/2}.
\]

Its eigenvalues are exactly the \(m\) positive eigenvalues \(\lambda_1\le\cdots\le\lambda_m\) of \(\mathcal L\). As \(I\preceq I+\boldsymbol 1\boldsymbol 1^\top\preceq(m+1)I\), the min-max principle gives

\[
w_j\le\lambda_j\le(m+1)w_j\quad(j=1,\ldots,m).
\]

Consequently \(\lambda_{j+1}/\lambda_j\ge w_{j+1}/((m+1)w_j)=10\). This also proves all positive eigenvalues are distinct. The instability interval of mode \(j\) as \(\varepsilon\) varies is exactly

\[
I_j=\left(\frac\alpha{\lambda_j},\frac\beta{\lambda_j}\right).
\]

For adjacent modes, \(\beta/\lambda_{j+1}<\alpha/\lambda_j\) because \(\lambda_{j+1}/\lambda_j\ge10>\beta/\alpha\). Thus all \(m\) intervals are pairwise disjoint and separated by nonempty intervals of full linear exponential stability. The spatially uniform mode corresponds to eigenvalue zero and remains linearly stable for every \(\varepsilon>0\). We have therefore exhibited exactly \(m\) disconnected strict linear-instability windows, hence \(2m\) threshold crossings.

**4. Optimal number of windows.** For an arbitrary fixed, connected undirected \((m+1)\)-node weighted graph, the positive Laplacian spectrum has at most \(m\) distinct values. For *any* fixed two-species reaction Jacobian with \(\operatorname{tr}J<0\), \(\det J>0\) and positive diagonal diffusion ratio \(\kappa\), each mode has strictly negative trace for all \(\varepsilon>0\), while its determinant is an upward quadratic in \(\varepsilon\) with positive value at zero. Hence the set on which that mode is strictly unstable is either empty or one open interval. The union of at most \(m\) intervals has at most \(m\) connected components. The star realizes equality.

## Verification

Run `python3 verify.py` using Python standard library only. It applies exact rational interval arithmetic to the displayed high-degree polynomial, bracket for the unique root in the small rational interval, state positivity, all four Jacobian entries, trace/determinant, and signs of the modal determinant at four rational endpoints. The universal star spectral min-max argument and maximal-component bound are proofs above, not inferred from finite simulation. The checker additionally certifies \(\beta/\alpha<157/69<3\).

## Relationship to prior work

Roy et al. introduce the ecological public-goods reactions, diffusion with fixed relative strategy mobility, and modal dispersion relation; their Appendix E explicitly discusses the finite range of unstable graph modes and spectral suppression. The present result uses those facts, without re-claiming them, and adds an exact **maximal-disconnected-window theorem for one fixed graph when the common mobility level alone varies**, a normalized positive-conductance star family attaining the theoretical maximum for every habitat count, and an exact-rational viable ecological calibration.

Hütt, Armbruster, and Lesne (2022) connect network spectra to Turing-pattern sensitivity under network perturbations, and Yang et al. (2022) investigate predator-prey Turing stability on diffusion graphs. Those related methods do not in their inspected relevant sections establish the fixed-graph maximal-window star construction. This literature comparison does not constitute a universal novelty certificate.

## Limitations

The theorem concerns the **linearized** homogeneous equilibrium. In instability windows the homogeneous state is linearly unstable, but emergence, existence, shape, and attraction of nonlinear cooperation-rich patterns are not established. At the finitely many threshold values a zero eigenvalue prevents classification as exponentially stable or unstable by this argument. The construction relies on increasingly heterogeneous *weighted* corridor conductances and unbounded mobility sweep; the originating article explicitly uses unweighted simple graphs. Historical priority against every possible general spectral-mode theorem is not independently established.

## References

1. S. Roy, M. S. Anwar, T. Carletti, M. Perc, D. Ghosh, *Diffusion-induced instabilities promote cooperation in eco-evolutionary networks*, PNAS **123** (2026), e2530131123, DOI: https://doi.org/10.1073/pnas.2530131123. Earliest verified public article date: 2026-07-08. Open full text: https://arxiv.org/abs/2607.15989 (posted 2026-07-17).
2. M.-T. Hütt, D. Armbruster, A. Lesne, *Predictable topological sensitivity of Turing patterns on graphs*, Physical Review E **105** (2022), 014304, https://doi.org/10.1103/PhysRevE.105.014304.
3. W. Yang, Q. Zheng, J. Shen, Q. Hu, *Pattern Dynamics in a Predator-Prey Model with Diffusion Network*, Complexity (2022), 9055480, https://doi.org/10.1155/2022/9055480.
