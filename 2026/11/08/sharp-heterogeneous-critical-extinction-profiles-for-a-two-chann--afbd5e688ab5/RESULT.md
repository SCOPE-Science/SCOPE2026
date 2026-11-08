# Sharp heterogeneous critical-extinction profiles for a two-channel aerosol–droplet SIS hypergraph model

## Finding
For a connected finite dyadic–environment hypergraph under the Nguyen–Porter individual-level deterministic mean-field closure, the precise spatial profile of critical epidemic extinction is given by the Perron eigenvector of an **effective node transmission matrix** and an explicit cubic coefficient. The profile is valid from every nonzero initial infection or environmental contamination state, not only symmetric initial conditions.

Let \(u>0\) satisfy \(Mu=\gamma u\), where
\[
M=\beta_d A+\frac{\beta_e\sigma}{\delta}BB^\top,
\qquad \rho(M)=\gamma.
\]
Put \(q=B^\top u\) and
\[
W=\sum_{i=1}^n u_i^2+\frac{\beta_e\sigma}{\delta^2}\sum_{h=1}^m q_h^2,
\qquad
K=\frac{\gamma\sum_i u_i^3+(\beta_e\sigma^2/\delta^2)\sum_h q_h^3}{W}.
\]
Then every nonzero trajectory of the specified model satisfies
\[
\boxed{\lim_{s\to\infty} s x_i(s)=\frac{u_i}{K},\qquad
\lim_{s\to\infty}s y_h(s)=\frac{\sigma q_h}{\delta K}.}
\]
Thus all vertex and environment compartments decay at rate \(1/s\) with a topology-dependent, explicitly computable, nonzero profile. Changing the scale of \(u\) changes \(K\) by the same factor and leaves these limits invariant.

## Assumptions and scope
Let \(n\ge3\) and \(m\ge1\). Let \(A\in\{0,1\}^{n\times n}\) be a symmetric, zero-diagonal adjacency matrix of dyadic contacts. Let \(B\in\{0,1\}^{n\times m}\) be a node–environment incidence matrix whose columns have at least three ones. Assume that the union of dyadic edges and the incidence links is connected, including every environment vertex. The five rates \(\beta_d,\beta_e,\sigma,\gamma,\delta\) are strictly positive. This ensures irreducibility of the node–environment linearized flow. The exact spectral condition \(\rho(M)=\gamma\) is imposed.

On the invariant cube \([0,1]^{n+m}\) consider
\[
\begin{aligned}
\dot x_i&=(\beta_d(Ax)_i+\beta_e(By)_i)(1-x_i)-\gamma x_i,\\
\dot y_h&=\sigma\arctan((B^\top x)_h)(1-y_h)-\delta y_h.
\end{aligned}
\]
This is the individual-level deterministic mean-field approximation (3.1) of the motivating paper for its specified \(g(z)=\arctan z\), specialized to uniform rates. It is not an exact moment equation of the original stochastic hypergraph process.

## Proof
**Step 1: positivity and the critical Perron pair.** Each coordinate is inward-pointing at zero and strictly inward at one, hence the cube is forward invariant. Since the directed graph of the nonnegative cross-derivatives is strongly connected, every nonzero initial condition enters the strictly positive cube for every positive time. Let
\[
L=\begin{pmatrix}\beta_d A-\gamma I&\beta_e B\\\sigma B^\top&-\delta I\end{pmatrix},\qquad
v=\binom{u}{(\sigma/\delta)q},\quad
w=\frac1W\binom{u}{(\beta_e/\delta)q}.
\]
The equality \(Mu=\gamma u\) gives \(Lv=0\), \(w^\top L=0\), \(w^\top v=1\). These are strictly positive vectors. Irreducible Metzler Perron–Frobenius theory implies that zero is the simple spectral bound of \(L\) and its other eigenvalues have strictly negative real part.

**Step 2: global critical extinction.** Write \(z=(x,y)\), \(\dot z=Lz-Q(z)\), with
\[
Q_i=x_i[\beta_d(Ax)_i+\beta_e(By)_i],\quad
Q_{n+h}=\sigma[r_h-\arctan r_h+\arctan(r_h)y_h],\quad r=B^\top x.
\]
Both blocks are nonnegative on the invariant cube, and \(Q(z)=O(\|z\|^2)\) near zero. The positive weighted mass \(a(s)=w^\top z(s)\) satisfies \(a'=-w^\top Q(z)\le0\). The cube is compact. For any nonzero state, strong positivity makes every \(x_i\) and every \(y_h\) positive at any later time, at which point \(w^\top Q>0\). Hence the largest invariant subset of \(\{z:w^\top Q(z)=0\}\) is the origin. LaSalle's principle yields \(z(s)\to0\) globally for every nonzero initial state.

**Step 3: alignment with the null eigenvector.** Normalize as above and set \(P=vw^\top\), \(r_\perp=(I-P)z\). Let \(c>0\) be the spectral gap of \(L\) on \(\ker w^\top\). Variation of constants gives
\[
\|r_\perp(s)\|\le C e^{-cs}+C\int_0^s e^{-c(s-\tau)}a(\tau)^2\,d\tau.
\]
Strict positivity of \(w\) bounds each coordinate by a constant times \(a\), so \(\|Q(z)\|\le C a^2\). Therefore \(-C a^2\le a'\le0\) and \(a(s)\ge c_0/(1+s)\). Given any sufficiently late \(T\), \(0\le-a'/a\le C a(T)\) on \([T,\infty)\); choosing \(T\) with \(2Ca(T)<c\) bounds the recent-time convolution by \(O(a(s)^2)\), while the initial part decays exponentially. Consequently \(r_\perp(s)=O(a(s)^2)\), and \(z(s)=a(s)v+o(a(s))\).

**Step 4: the exact quadratic coefficient.** Since \(\arctan t=t+O(t^3)\), the quadratic part of \(Q\) at \(v\) has vertex components \(v_i(\beta_d(Av_x)_i+\beta_e(Bv_y)_i)=\gamma u_i^2\) and environment components \(\sigma q_h v_{y,h}=(\sigma^2/\delta)q_h^2\). Taking its scalar product with \(w\) gives precisely
\[
w^\top Q_2(v)=\frac{\gamma\sum_i u_i^3+(\beta_e\sigma^2/\delta^2)\sum_h q_h^3}{W}=K>0.
\]
Thus \(a'=-K a^2+o(a^2)\), which implies \((1/a)'=K+o(1)\), \(s a(s)\to1/K\), and the displayed coordinate limits follow from alignment.

## Verification
The standalone `check.py` included in this package verifies 30 heterogeneous connected node–environment networks numerically at their exact spectral thresholds, checking the left/right zero eigenvectors, their normalization, and the full nonlinear quadratic coefficient. A rational three-person example is checked separately: for the triangle dyadic graph and its single three-person environment, with \((\beta_d,\beta_e,\sigma,\gamma,\delta)=(1/4,1/6,1,1,1)\), choose \(u=(1,1,1)\). Then \(q=3\), \(W=9/2\), \(K=5/3\), and the limits are \(3/5\) for each person and \(9/5\) for the environment. Numerical integrations to times \(10^3,10^4,10^5\) approach those exact coefficients. These computations check instances and identities; the proof above establishes the infinite-time and arbitrary-topology quantifiers.

## Relationship to prior work
Nguyen and Porter (2026) introduce the individual-level node/environment closure (3.1) and establish local invasion-threshold results on complete uniform hypergraphs (Theorem 3.1) and a homogeneous regular-hypergraph threshold (Theorem 3.3). Neither theorem asserts the global spatial critical profile proved here. The networked SIWS work of Paré et al. (2021) establishes general threshold-based global stability for a related linear-infrastructure model, so global extinction alone is not claimed as novel. The distinct contribution here is the exact \(1/s\) coefficient for the arctan-saturating hyperedge state model on arbitrary connected incidence structures, including nonsymmetric initial conditions and an explicit left/right Perron reduction. Classical positive-system and spectral-gap arguments supply part of the method.

## Limitations
The theorem concerns the deterministic mean-field approximation, not extinction-time distributions of the finite stochastic SIS process. It requires fixed connected topology, strictly positive rates, and exactly the critical spectral surface; it does not claim uniform estimates near criticality, or the same coefficient for a contamination kernel with nonzero second derivative. The mathematical model should not be interpreted as an epidemiological forecast without parameter calibration.

## References
- T. D. Nguyen and M. A. Porter, *A disease-spread model on hypergraphs with distinct droplet and aerosol transmission modes*, arXiv:2601.03563v1 (first public January 7, 2026), https://arxiv.org/pdf/2601.03563.
- P. E. Paré et al., *Multi-Layer SIS Model with an Infrastructure Network*, arXiv:2109.09493v1 (2021), https://arxiv.org/pdf/2109.09493.
- A. Khanafer, T. Başar and B. Gharesifard, *Stability of Epidemic Models over Directed Graphs: A Positive Systems Approach*, arXiv:1407.6076 (2014), https://arxiv.org/abs/1407.6076.
