# Exact arithmetic rank loss and one-snapshot recovery on even cycle graphs

## Finding

Let \(m\ge2\), let \(C_{2m}\) be the undirected cycle with vertices \(\mathbb Z/(2m)\mathbb Z\), and let \(U f(x)=(f(x-1)+f(x+1))/2\). Let \(T=\phi(U)\) be any spectral function whose \(m+1\) values \(\phi(\cos(\pi k/m))\), \(0\le k\le m\), are pairwise distinct. For a separation \(1\le h<2m\) and an integer \(t\ge1\), observe a signal \(f\in\mathbb C^{2m}\) at two fixed sites through
\[
\mathcal O_{t,h} f=\big((T^j f)(0),(T^j f)(h)\big)_{j=0}^{t-1}.
\]
Put \(g=\gcd(h,m)\). At the information-theoretic critical horizon and at one further snapshot, the **exact ranks** are
\[
\boxed{\operatorname{rank}\mathcal O_{m,h}=2m-g+1-\mathbf1_{\{2\mid h/g\}},\qquad
\operatorname{rank}\mathcal O_{m+1,h}=2m-g+1.}
\]
The rank has already saturated at \(m+1\): this second formula holds with \(m+1\) replaced by every \(t\ge m+1\). Thus the unobservable subspace at arbitrarily many times has dimension **exactly** \(g-1\); in addition, a single recoverable direction is missing at the critical horizon precisely when \(h/g\) is even.

Consequently, complete recovery of every signal is possible if and only if \(\gcd(h,m)=1\). Its minimum number of simultaneous two-site snapshots is precisely \(m\) when \(h\) is odd and \(m+1\) when \(h\) is even. For even \(m\), all \(2\varphi(m)\) fully observable separations use the first horizon. For odd \(m\), exactly \(\varphi(m)\) fully observable separations use each of the two horizons. The assertions apply to normalized adjacency, normalized graph Laplacian and any nondegenerate discrete heat step.

## Assumptions and scope

The cycle has even order at least four, distinct observation vertices, and an arbitrary complex initial signal. The standard Fourier characters on \(\mathbb Z/(2m)\mathbb Z\) form an orthonormal basis for counting measure. The spectral function may be complex-valued, but its values on the **distinct** cycle eigenspaces must be pairwise distinct. In particular, \(T=U\), \(T=I-U\), and \(T=e^{-\tau(I-U)}\) for \(\tau>0\) satisfy this assumption. The time index \(j\) is a nonnegative integer; each snapshot supplies two separate complex scalar measurements. The rank formulas do not assert uniform noise stability or characterize all intermediate horizons below \(m\).

## Proof

Write \(N=2m\), \(\omega=e^{2\pi i/N}\), and Fourier characters \(e_k(x)=N^{-1/2}\omega^{kx}\). The eigenvalue of \(U\) at \(e_k\) is \(\cos(\pi k/m)\), hence the \(m+1\) distinct spectral shells are indexed by \(k=0,1,\ldots,m\); the interior shell \(1\le k\le m-1\) is spanned by \(e_k,e_{-k}\), while the first and last shells each have dimension one.

**Spatial visibility.** On an interior shell the two sensor evaluations are, in the ordered character basis,
\[
\frac1{\sqrt N}\begin{pmatrix}1&1\\ \omega^{kh}&\omega^{-kh}\end{pmatrix}.
\]
Its determinant vanishes exactly when \(\sin(\pi kh/m)=0\), equivalently \(m\mid kh\). Writing \(g=\gcd(h,m)\), the interior shells with this property are precisely
\[
k_j=jm/g,\qquad 1\le j\le g-1.
\]
Each such shell contributes exactly one invisible direction for every time, and all other interior shells are fully visible from the two locations. The endpoint characters are individually visible. Hence the full spatially visible Fourier space has dimension \(2m-(g-1)=2m-g+1\). This proves an upper bound on the rank of every time observation, and identifies the entire permanent kernel explicitly.

**Vandermonde demixing.** Denote by \(a_k\) and \(b_k\) the value at the two sensors of the component of \(f\) in shell \(k\). The entire observation record is the pair of vectors \(V_t a,V_t b\), where
\[
(V_t)_{j,k}=\lambda_k^j,\qquad \lambda_k=\phi(\cos(\pi k/m)),\quad 0\le j<t,\ 0\le k\le m.
\]
Because the \(\lambda_k\) are pairwise distinct, \(V_{m+1}\) is invertible. Thus the \((m+1)\)-snapshot record recovers every observable shell value. It has rank \(2m-g+1\), as does every later record.

**Exact critical-horizon defect.** The rectangular \(m\)-by-\((m+1)\) Vandermonde matrix \(V_m\) has a one-dimensional kernel spanned by a vector \(v=(v_0,\ldots,v_m)\) with **every coordinate nonzero**: any \(m\) of its columns are independent by the square Vandermonde determinant. A vector in the kernel of the two-record observation map must therefore have shell values \(a=\alpha v\), \(b=\beta v\) for some scalars \(\alpha,\beta\).

For the constrained shells \(k_j=jm/g\), \(0\le j\le g\), where \(k_0=0\) and \(k_g=m\) denote the endpoints, the two sensor values obey
\[
b_{k_j}=(-1)^{(h/g)j}a_{k_j}.
\]
For the interior constrained shells this follows from \(\omega^{kh}=(-1)^{kh/m}\); at the endpoints it follows directly from the constant and alternating characters. As \(v_{k_j}\ne0\), the constraints on a record-kernel vector reduce to
\[
\beta=(-1)^{(h/g)j}\alpha\quad\text{for every }0\le j\le g.
\]
The \(j=0\) constraint gives \(\beta=\alpha\). If \(h/g\) is odd, the \(j=1\) constraint gives \(\beta=-\alpha\), so only the zero vector remains. If \(h/g\) is even, all constraints agree, leaving exactly one dimension of record-kernel vectors **inside the visible shell space**. Subtracting this transient defect from the visible-space dimension proves the critical-horizon rank formula.

**Horizon and census.** Fewer than \(m\) snapshots yield at most \(2(m-1)<2m\) measurements, so full recovery is impossible then. When \(g=1\), the two rank formulas show that \(m\) snapshots suffice for odd \(h\), whereas even \(h\) requires exactly \(m+1\). For \(g>1\), the \(g-1\) invisible eigenvectors prevent recovery at any horizon. There are exactly two offsets modulo \(2m\) above each residue coprime to \(m\), giving \(2\varphi(m)\) fully observable offsets. If \(m\) is even both lifts are odd. If \(m\) is odd the two lifts have opposite parity, giving \(\varphi(m)\) offsets at each horizon.

## Verification

The dependency-free Python program `CHECK.py` uses exact rational Gaussian elimination on the integer-site matrices generated by \(U\), and tests the critical and saturated rank formulas for every half-order \(2\le m\le11\) and every nonzero separation \(h\). It checks \(120\) distinct parameter pairs without numerical tolerances and also independently reproduces the earlier critical-horizon determinant test in \(80\) cases. Run `python CHECK.py`; its final line is `CHECK_OK exact_ranks= 120`. The finite checks are only corroboration: the Vandermonde and spatial-shell argument above proves the statements for every \(m\).

## Relationship to prior work

Bulai, Cabrelli, Cordero, Molter and Saliani (2026) develop graph Paley–Wiener dynamical sampling, including finite-graph experiments on paths. Aldroubi and collaborators (2026) survey general eigenmode-observation criteria. Those works motivate the graph harmonic frame setting, but their inspected accessible material does not give the two critical-horizon rank formulas on even cycles. Previous exact cycle results identify invertibility and even-cycle information determinants at the dimensionally minimal horizon, and optimal demixed low-pass spatial conditioning; a zero determinant alone does **not** determine the exact rank or whether one further snapshot repairs the failure.

The earlier cycle-observability analysis of Parlangeli and Notarstefano (2011) provides a related arithmetic criterion for two observation sites. Its displayed coprimality condition involving the **full** cycle order is not adopted as a premise here; the present direct Fourier calculation distinguishes the half-order and the transient one-snapshot defect. For example, on the six-cycle, separation two gives rank five at three snapshots but full rank six at four snapshots, so full-order coprimality is not necessary for this stated two-sensor evolution. This comparison is made at the level of concrete operators and eigenspaces, not by title similarity.

## Limitations

The result concerns exact linear recoverability, not condition numbers or noise amplification. It requires every pair of distinct cycle eigenvalue shells to receive distinct evolution multipliers; non-injective spectral filters can have additional defects. The motivating 2026 finite-graph paper was available in bibliographic and abstract form only, not as inspectable complete primary text; an equivalent calculation in its uninspected sections cannot be excluded. The older cycle-observability formula should be reconciled carefully with its full set of conventions before drawing historical priority conclusions. No independent mathematical audit or complete publication-priority certification is claimed.

## References

1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472 (first publicly posted 21 September 2026), https://arxiv.org/abs/2609.25472.
2. A. Aldroubi, C. Cabrelli, I. Krishtal, U. Molter, *Dynamical Sampling: A Survey*, La Matematica 5, article 37 (2026), DOI:10.1007/s44007-026-00215-y.
3. G. Parlangeli, G. Notarstefano, *On the Reachability and Observability of Path and Cycle Graphs*, arXiv:1109.3556 (first publicly posted 16 September 2011), DOI:10.1109/TAC.2011.2168912.
