# Uniform logarithmic correction at the critical exclusion boundary of a two-sex quadratic map

## Finding

In the deterministic quadratic population evolution
\[
(x,y)\mapsto\bigl(x+a(1-x)y,\;y[x+b(1-x)]\bigr),\qquad 0<a,b<1,
\]
consider trajectories whose conserved invariant leaf approaches the nonhyperbolic corner \((1,0)\) at rate \(N^{-1}\). The leading-order population crossover on this scale is already known from an earlier initial-ensemble scaling analysis. The present theorem identifies **both universal logarithmic corrections** in reciprocal coordinates, uniformly along the macroscopic observation interval. In particular the finite-generation deviation from the continuum crossover is of exact order \(\log N\) for the reciprocal states, not just an unquantified remainder.

Write \(\gamma=1-b\). Choose any fixed \(0<r<\min\{1,a/\gamma\}\), \(R>0\) and \(0<\delta\le1\). For each sufficiently large integer \(N\), any \(|\tau|\le R\), initialize
\[
x_0=1-r,\qquad y_0=\frac{\gamma}{a}\left(r+\frac{\tau}{N}\right).
\]
This is a valid interior state for all sufficiently large \(N\). Define
\[
A_\tau(t)=\int_0^t\gamma e^{\gamma\tau s}\,ds
=\begin{cases}(e^{\gamma\tau t}-1)/\tau,&\tau\ne0,\\\gamma t,&\tau=0.\end{cases}
\]
For \(m=\lfloor Nt\rfloor\), uniformly for \(\delta\le t\le1\) and \(|\tau|\le R\),
\[
\boxed{\frac{1}{1-x_m}=N A_\tau(t)+\gamma e^{\gamma\tau t}\log N+O_{a,b,r,R,\delta}(1),}
\]
\[
\boxed{\frac{\gamma}{a y_m}=N A_{-\tau}(t)+\gamma e^{-\gamma\tau t}\log N+O_{a,b,r,R,\delta}(1).}
\]
The coefficients of \(\log N\) are positive for all allowed parameters. At the exactly critical leaf \(\tau=0\), both formulas reduce to \(\gamma Nt+\gamma\log N+O(1)\). The new second-order terms determine the precise finite-generation bias of the previously established first-order extinction-selection crossover.

## Assumptions and scope

Here time \(k\) counts discrete generations. The spatial domain is the full square \([0,1]^2\), but the assertion concerns the specified interior family, with \(a,b,r\) fixed while \(\tau\) may vary in a bounded interval and \(t\) in \([\delta,1]\). No uniformity as \(t\downarrow0\), as \(a,b\) approach a boundary, or for larger detunings is asserted. The source invariant leaf is
\[
\frac{x_k}{a}+\frac{y_k}{\gamma}=\frac{x_0}{a}+\frac{y_0}{\gamma}.
\]
The map has two intersecting equilibrium edges, meeting at the nonhyperbolic corner \((1,0)\). The two reciprocal observables quantify proximity to these faces while the conserved leaf offset is \(\tau/N\).

## Proof

**Step 1: symmetric competitive form and exact offset.** Put \(z_k=1-x_k\) and \(u_k=a y_k/\gamma\). The defining polynomial map becomes exactly
\[
 z_{k+1}=z_k(1-\gamma u_k),\qquad u_{k+1}=u_k(1-\gamma z_k).
\]
Consequently \(u_{k+1}-z_{k+1}=u_k-z_k=\tau/N\) for every \(k\). In particular both positive coordinates decrease. The admissibility condition ensures \(0<z_0,u_0<1\) and all iterates are positive; \(0<\gamma<1\). Thus \(u_k=z_k+\tau/N\) and the first scalar coordinate obeys
\[
z_{k+1}=z_k\bigl(1-\gamma z_k-\gamma\tau/N\bigr).
\]
The second coordinate satisfies the same scalar recurrence with detuning \(-\tau\), starting from \(u_0=r+\tau/N\).

**Step 2: reciprocal recurrence.** For either scalar coordinate write \(v_k>0\), detuning \(\sigma\in[-R,R]\), \(w_k=1/v_k\), \(s_N=1-\gamma\sigma/N\). For sufficiently large \(N\), \(s_N>0\) and
\[
w_{k+1}=\frac{w_k}{s_N}+\frac{\gamma}{s_N^2}+\frac{\gamma^2}{s_N^3 w_k}\frac{1}{1-\gamma/(s_Nw_k)}.\tag{1}
\]
This is an **identity**, not an Euler approximation. All denominators are uniformly bounded away from zero because \(v_k\le\max\{r,r+R/N\}\), \(0<\gamma<1\), and \(N\) is large. In particular the last term is bounded in absolute value by \(C/w_k\). Also \(s_N^{-1}=1+O(1/N)\), uniformly in detuning.

**Step 3: uniform growth estimates.** The positive forcing \(\gamma/s_N^2\) in (1), together with \(s_N^{-1}\ge1-C/N\), implies by variation of constants
\[
c(k+1)\le w_k\le C(k+1),\qquad 0\le k\le N,
\]
where constants may depend on the fixed parameter bounds but not on \(N,\sigma,k\). For the upper bound use (1), the positive initial lower bound and discrete Gronwall; the lower bound follows by summing forcing with weights no smaller than \((1-C/N)^N\). Subtracting the constant increment \(\gamma\) in (1) now gives
\[
w_k=\gamma k+O\left(1+\frac{k^2}{N}+\log(k+1)\right),\qquad 0\le k\le N.\tag{2}
\]
For \(k\ge1\), (2) and the growth bound imply
\[
\frac1{w_k}=\frac1{\gamma k}+O\left(\frac1N+\frac{1+\log(k+1)}{k^2}\right).\tag{3}
\]
All estimates are uniform over the detuning interval and remain valid for both initial reciprocals, which stay uniformly bounded.

**Step 4: leading term and logarithmic correction.** Apply variation of constants to (1) with \(h_N=s_N^{-1}\). The constant forcing and initial term produce
\[
h_N^m w_0+\frac{\gamma}{s_N^2}\sum_{j=0}^{m-1}h_N^j
=N A_\sigma(t)+O(1),\qquad m=\lfloor Nt\rfloor,\tag{4}
\]
uniformly for \(0\le t\le1\), by \(h_N^j=e^{\gamma\sigma j/N}+O(N^{-1})\). For the nonlinear forcing, (3) gives
\[
\sum_{j=1}^{m-1}h_N^{m-1-j}\frac1{w_j}
=\frac{e^{\gamma\sigma t}}\gamma\log N+O(1),\qquad \delta\le t\le1.\tag{5}
\]
Indeed the total error replacing \(1/w_j\) by \(1/(\gamma j)\) is bounded by (3); replacing the weights by the common factor \(e^{\gamma\sigma t}\) incurs \(O(\sum_{j\le m}j/(Nj))=O(1)\); and \(\log m=\log N+O_\delta(1)\). The denominator correction in (1) contributes an absolutely summable \(O(1/w_j^2)\) error, and \(s_N^{-3}=1+O(N^{-1})\). Inserting (4) and (5) into (1) yields
\[
w_m=N A_\sigma(t)+\gamma e^{\gamma\sigma t}\log N+O(1).
\]
First choose \(\sigma=\tau\) and \(v=z\); then choose \(\sigma=-\tau\) and \(v=u\). The original-coordinate formulas follow because \(w_z=1/(1-x)\) and \(w_u=\gamma/(a y)\). The \(O(1)\) constant is uniform as claimed.

## Verification

The included standalone `critical_window_check.py` tests conservation of \(u_k-z_k\) over 7,500 updates and compares the theoretically predicted coefficient \(\gamma e^{\gamma\tau t}\) with numerical differences of reciprocal residuals at two sizes (30 parameter-time combinations). It reports `BIPOP_RECIPROCAL_LOG_WINDOW_OK exact_symmetry=7500 cases=30`. To replay, execute `python3 critical_window_check.py` with the standard Python library. These finite checks support the derivation but cannot prove the asymptotics. The proof above supplies the infinite-\(N\) argument.

## Relationship to prior work

Boxonov, *On dynamical systems of quadratic stochastic operators constructed for bisexual populations*, arXiv:2303.03884v1, §3, defines the same operator in (3.6), identifies its invariant linear leaves in Lemma 1, and proves qualitative convergence in Theorem 2. An existing first-order critical-invariant-layer ensemble result for this same model yields the \(t=1\) crossover coordinates \(1/A_{\pm\tau}(1)\) after inversion. Neither qualitative endpoint convergence nor that first-order profile yields the **two nonzero logarithmic coefficients with a bounded remainder**, uniformly over detuning and physical discrete-time observation windows. General logistic parabolic recurrences motivate the reciprocal method but are not claimed new. Stronger general discrete Riccati asymptotics could potentially imply the coefficients by specialization and remain a priority risk.

## Limitations

Only fixed interior base points \(r\), bounded detunings, and observation times bounded below are covered. No whole-square ensemble density, higher-order constant, non-autonomous switching, or claim of independent validation is established. Publication novelty remains provisional relative to specialized recurrence-asymptotic literature. The source is mathematically classed as a dynamics preprint and the present theorem belongs to MSC2020 37N25, although the originating paper also emphasizes biological modeling.

## References

1. Z. S. Boxonov, *On dynamical systems of quadratic stochastic operators constructed for bisexual populations*, arXiv:2303.03884v1, first posted 2023-03-07. https://arxiv.org/abs/2303.03884
2. Z. S. Boxonov, *On Dynamical Systems of Quadratic Stochastic Operators Constructed for Bisexual Populations*, *Mathematical Notes* 114 (2023), 1134–1150. DOI: 10.1134/S0001434623110469.
