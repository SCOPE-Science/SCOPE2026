# Fixed-mean renewal probing has three sharp optimal phases in a two-level quantum detector

## Finding
Fix a two-dimensional Hamiltonian with a nonzero transition matrix element between the prepared state and an orthogonal detected state. For independent, identically distributed **strictly positive** projective-measurement intervals with prescribed mean \(\mu>0\), the infimum of mean first-detection time is given exactly by a three-piece phase law.

Write the Hermitian Hamiltonian in the preparation/detection basis as
\[
H=\begin{pmatrix}h_0+d&v\\\overline v&h_0-d\end{pmatrix},\qquad
\Omega=\sqrt{d^2+|v|^2}>0,\qquad
\alpha=\frac{|v|^2}{\Omega^2}\in(0,1].
\]
Let \(x_c\) be the unique solution of \(\tan x=2x\) in \((\pi/4,\pi/2)\), and write \(m=\Omega\mu\). Then, over all renewal interval distributions \(\tau>0\) almost surely with \(\mathbb E\tau=\mu\),
\[
\boxed{\inf\mathbb E T_{\mathrm{det}}=\frac1{\alpha\Omega}\begin{cases}
\dfrac{x_c}{\sin^2x_c},&0<m\le x_c,\\[3pt]
\dfrac{m}{\sin^2m},&x_c\le m\le\pi/2,\\[3pt]
m,&m\ge\pi/2.
\end{cases}}
\]
The formulas agree at both phase boundaries. The first regime has a constant optimal infimum despite an arbitrarily high prescribed mean probing frequency; this infimum is **not attained** by any strictly positive-interval law when \(0<m<x_c\). For \(x_c\le m\le\pi/2\), the unique optimizer is deterministic probing at \(\tau=\mu\). For \(m>\pi/2\), the optimizers are exactly the interval distributions supported on the resonant set
\[
\left\{\frac{\pi/2+k\pi}{\Omega}:k=0,1,2,\ldots\right\}
\]
that have mean \(\mu\). Such laws always exist, and two adjacent resonant intervals suffice. At \(m=\pi/2\), the only optimizer is the deterministic first resonance.

If zero-length intervals are explicitly allowed, the infimum in the first regime is attained uniquely by the two-point distribution on \(\{0,x_c/\Omega\}\) with mass \(m/x_c\) at \(x_c/\Omega\); for \(m=x_c\), the deterministic law is optimal. Numerically,
\[
x_c=1.16556118520723\ldots,\qquad \frac{x_c}{\sin^2x_c}=1.38005013968930\ldots.
\]

## Assumptions and scope
The prepared state \(|0\rangle\) and detected state \(|1\rangle\) are orthonormal, and the Hamiltonian is time independent and Hermitian. A projective measurement of \(|1\rangle\langle1|\) is performed after each waiting interval. On failure, the state is projected onto \(|0\rangle\) and evolution continues; there is no additional physical reset. The waiting intervals are i.i.d., independent of measurement outcomes conditional on the evolved state, strictly positive almost surely, and have the exact finite prescribed mean \(\mu\). Detection ends the process. The nonzero coupling assumption \(v\ne0\) excludes permanently dark transitions. Units use \(\hbar=1\).

The theorem optimizes **elapsed first-detection time** among all such renewal laws, not the expected number of probes alone and not protocols subject to a minimum switching time, per-probe cost, adaptive feedback, interval correlations, or finite support constraints. Its first phase is a sharp unattained infimum for physical positive intervals; the zero-interval statement is a mathematical closure, not an assertion that coincident probes are experimentally free.

## Proof
**1. One attempt and renewal reduction.** Subtracting \(h_0I\), the traceless Hamiltonian obeys \((H-h_0I)^2=\Omega^2I\). Therefore
\[
e^{-iH\tau}=e^{-ih_0\tau}\left[\cos(\Omega\tau)I-\frac{i\sin(\Omega\tau)}{\Omega}(H-h_0I)\right],
\]
so the success probability of a probe after waiting \(\tau\) is exactly
\[
p(\tau)=|\langle1|e^{-iH\tau}|0\rangle|^2
=\alpha\sin^2(\Omega\tau).
\]
Every failed probe leaves the ray \(|0\rangle\), because the failure projector has rank one. Thus the experiment restarts in the same state after each failure. For a law \(P\) of \(\tau\), let \(\bar p=\alpha\mathbb E_P[\sin^2(\Omega\tau)]\). If \(\bar p=0\), detection never occurs and the mean is infinite. Otherwise the attempt index of the first success is geometric with success parameter \(\bar p\). Although interval length and success at a given attempt are correlated, the event of *reaching* that attempt depends only on previous attempts and is independent of its current interval. Tonelli's theorem therefore gives
\[
\mathbb ET_{\mathrm{det}}=\sum_{j\ge1}\mathbb E\left[\tau_j\mathbf1_{\{\text{attempt }j\text{ reached}\}}\right]
=\mu\sum_{j\ge1}(1-\bar p)^{j-1}
=\frac{\mu}{\alpha\mathbb E[\sin^2(\Omega\tau)]}.
\]
The remaining task is the fixed-mean extremum of the bounded oscillatory function \(f(x)=\sin^2x\) for \(x\ge0\).

**2. A sharp concave majorant.** For \(0<x<\pi/2\), the derivative of \(f(x)/x\) has the sign of \(2x\cos x-\sin x\). The function \(\tan x-2x\) first decreases and then increases, is negative at \(\pi/4\), and tends to positive infinity as \(x\uparrow\pi/2\). Hence its unique positive root \(x_c\) belongs to \((\pi/4,\pi/2)\), and \(f(x)/x\) is strictly increasing up to \(x_c\) and strictly decreasing thereafter on that half-period. Moreover, for \(x\ge\pi/2\),
\[
\frac{f(x)}x\le\frac1x\le\frac2\pi<\frac{f(x_c)}{x_c},
\]
so \(f(x_c)/x_c\) is the unique global maximum of \(f(x)/x\) on \((0,\infty)\).

Set \(s_c=f(x_c)/x_c=f'(x_c)\) and define
\[
G(x)=\begin{cases}
s_cx,&0\le x\le x_c,\\
\sin^2x,&x_c\le x\le\pi/2,\\
1,&x\ge\pi/2.
\end{cases}
\]
The equality of slopes at \(x_c\), the zero derivative of \(f\) at \(\pi/2\), and \(f''(x)=2\cos(2x)<0\) for \(x_c<x<\pi/2\) show that \(G\) is concave on the entire nonnegative half-line. It majorizes \(f\): on \((0,x_c)\) by the global maximum property of \(f(x)/x\), in the middle by equality, and beyond \(\pi/2\) by \(f\le1\). Therefore, with \(X=\Omega\tau\) and \(\mathbb EX=m\),
\[
\mathbb E f(X)\le\mathbb EG(X)\le G(\mathbb EX)=G(m).
\]
Substitution into the renewal identity yields the displayed three-piece lower bound.

**3. Sharpness and all equality cases.** When \(0<m<x_c\), the law with mass \(1-m/x_c\) at \(X=0\) and mass \(m/x_c\) at \(X=x_c\) has mean \(m\) and attains \(\mathbb Ef(X)=G(m)\). Within strictly positive laws, choose \(0<\varepsilon<m\) and put mass \((m-\varepsilon)/(x_c-\varepsilon)\) at \(X=x_c\) and the remaining mass at \(X=\varepsilon\). These strictly positive laws have mean \(m\) and approach the bound as \(\varepsilon\downarrow0\). Equality is impossible for a strictly positive law: the inequality \(f(x)\le s_cx\) is strict for all \(x>0\) except \(x=x_c\), forcing the entire law to be the point mass at \(x_c\), inconsistent with mean \(m<x_c\).

For \(x_c\le m\le\pi/2\), the point mass \(X=m\) attains the bound. It is the only optimizer: \(G\) is strictly concave on \((x_c,\pi/2)\), so Jensen equality at an interior mean forces a point mass; at the two endpoints, the linear and constant contact regions together with equality \(f=G\) leave only \(X=x_c\) and \(X=\pi/2\), respectively.

For \(m>\pi/2\), the upper bound is \(G(m)=1\). It is attained if and only if \(f(X)=1\) almost surely, equivalently \(X\in\{\pi/2+k\pi:k\ge0\}\) almost surely. Every \(m>\pi/2\) can be written as a convex combination of two consecutive values of this set, proving existence and characterizing all optimizers. This also proves the endpoint assertions, concluding the theorem.

## Verification
The analytical proof establishes the global bound and uniqueness, including unbounded-support waiting distributions. The standalone script `artifacts/verify.py` uses only the Python standard library. It independently checks the root and tangent identities, explicit optimizers across the three regimes, the concave majorant on sampled points and sampled fixed-mean two-point laws, direct matrix-propagator transition probabilities for nonzero detuning, and geometric-renewal expectations. On direct execution it reports 3061 successful diagnostic assertions. These finite tests do not substitute for the global concavity/Jensen proof.

As an illustrative resonant qubit with \(\alpha=\Omega=1\), a mean interval \(\mu=1/2\) has sharp infimum \(1.38005013968930\ldots\), versus \(2.17534264967002\ldots\) for deterministic probing at that mean; the strict-positive optimum is approached by a mixture of very short waits and waits near \(x_c\). At mean \(\mu=2\), the optimal resonant mixture gives detection mean exactly \(2\), whereas deterministic probing yields \(2/\sin^2(2)=2.41890087412608\ldots\).

## Relationship to prior work
Kulkarni and Majumdar (2023), first posted May 24, 2023, developed renewal formulas for arbitrary measurement-interval laws in a two-level projective detector; their equation (135) provides the general first-detection mean underlying step 1. They analyzed the Poissonian optimum and interval-law effects but not the exact mean-constrained optimization and its three optimizer phases. Kessler, Barkai and Ziegler (2020/2021) gave the mean-time/mean-attempt identity for i.i.d. quantum probing and compared fixed, gamma and exponential measurement laws, without a sharp optimization over all distributions at fixed mean.

A later public result, *Exact renewal-protocol optimum for first detection on the fully connected quantum model* (2026), proved the best mean first-detection time over **all** i.i.d. waiting laws when their mean is free to vary. Its scalar success function reduces to the same sinusoidal extremum and fixes the universal constant \(x_c/\sin^2x_c\). Thus that unconditional optimum and the low-mean limiting value are **prior coverage, not claimed as new**. The present claim is the complete *prescribed-mean* envelope, including the deterministic interval and resonant-mixture regimes, the two sharp transitions, all optimizer supports, and the nonattainment distinction for strictly positive waits. These constrained statements are not obtained merely by substituting the previously known unrestricted optimum.

## Limitations
The mean constraint is exact and does not impose a minimum gap between attempts. Under a fixed positive lower bound on every waiting interval, the small-mean regime changes; the result makes no claim for such a practical restriction. The zero-wait optimizer is a mathematical idealization. The rates and equality characterizations assume exact stationary Hamiltonian parameters and projective detection, not imperfect detectors, adaptive timing or multiple surviving states. General concave-envelope principles could lead to an equivalent theorem in unindexed optimal-renewal literature; this remains a priority risk despite the explicit comparisons. No experimental performance guarantee is claimed.

## References
1. M. Kulkarni and S. N. Majumdar, *First detection probability in quantum resetting via random projective measurements*, arXiv:2305.15123, initially posted 2023-05-24, especially Section 6, equation (135). https://arxiv.org/abs/2305.15123
2. D. A. Kessler, E. Barkai and K. Ziegler, *The first detection time of a quantum state under random probing*, arXiv:2012.01763, initially posted 2020-12-03; Physical Review A 103 (2021) 022222. https://arxiv.org/abs/2012.01763
3. *Exact renewal-protocol optimum for first detection on the fully connected quantum model*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-renewal-protocol-optimum-for-first-detection-on-the-fully--1683e0413749
4. MSC2020 classification: 81P15, quantum measurement theory, state operations and state preparations. https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=81P15
