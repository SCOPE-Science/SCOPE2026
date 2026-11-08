# Detuning-blind third click cumulant and a sharp fourth-order sign boundary in monitored qubits

## Finding
Consider continuous projective monitoring of a coherently driven qubit, specified in **Assumptions and scope**. Let \(N_t\) count detector clicks up to time \(t\), and let \(K_j\) denote the asymptotic cumulant rate
\[
K_j=\lim_{t\to\infty}\frac{\operatorname{cum}_j(N_t)}{t},\qquad j=1,2,3,4.
\]
For all \(g>0\), \(\gamma>0\), and real \(\Delta\), these limits exist and are
\[
\begin{aligned}
K_1&=\frac{\gamma}{2},\\
K_2&=\frac{\gamma(4\Delta^2+8g^2+\gamma^2)}{16g^2},\\
K_3&=\frac{\gamma(4g^2+3\gamma^2)}{8g^2},\\
K_4&=\frac{\gamma}{1024}P\left(\frac{\gamma^2}{g^2},\frac{\Delta^2}{g^2}\right),
\end{aligned}
\]
where
\[
P(u,v)=512+1600u+48u^2-3u^3+(256-36u^2)v-(768+144u)v^2-192v^3.
\]
In particular, \(K_3\) is **independent of detuning**, although \(K_2\) strictly increases with \(|\Delta|\). The asymptotic Fano factor is
\[
\frac{K_2}{K_1}=1+\frac{\gamma^2+4\Delta^2}{8g^2}>1.
\]
The fourth cumulant has the following **complete sign classification**. Let \(u_*\) be the unique positive real solution of
\[
512+1600u+48u^2-3u^3=0,
\]
so \(u_*=32.54744306049\ldots\). For each \(0<u<u_*\), there is exactly one \(v_*(u)>0\) satisfying \(P(u,v_*(u))=0\), and
\[
\begin{cases}
K_4>0,&0\le v<v_*(u),\\
K_4=0,&v=v_*(u),\\
K_4<0,&v>v_*(u).
\end{cases}
\]
For \(u=u_*\), the only nonnegative zero occurs at \(v=0\), with \(K_4<0\) at \(v>0\). For \(u>u_*\), \(K_4<0\) for every \(v\ge0\). Here \(u=\gamma^2/g^2\) and \(v=\Delta^2/g^2\). Thus a positive-to-negative fourth-order counting-noise transition occurs without any corresponding zero in the variance or third cumulant. The sign concerns the *cumulant per unit time*, not the uncentered fourth moment.

## Assumptions and scope
Fix \(g,\gamma>0\), \(\Delta\in\mathbb R\), and the computational basis \(\{|0\rangle,|1\rangle\}\). Set \(\hbar=1\), let
\[
H=g\sigma_x+\frac{\Delta}{2}\sigma_z,
\qquad P_1=|1\rangle\langle1|,
\qquad L=\sqrt\gamma\,P_1.
\]
Between clicks, a trajectory follows the no-click effective Hamiltonian \(H_{\mathrm{eff}}=H-i\gamma P_1/2\); at each click its state is projected to \(|1\rangle\). Its instantaneous click intensity is \(\gamma\langle\psi|P_1|\psi\rangle\). The initial state can be any normalized pure qubit state (or any density operator); it changes transient count statistics but not these positive-time asymptotic cumulant rates. There is only this one monitored channel; no independent spontaneous-emission channel or unmonitored dephasing is included. The full four-dimensional Bloch dynamics, not a restricted great-circle approximation, is used when \(\Delta\ne0\).

Write \(\operatorname{cum}_j\) for ordinary, not factorial, cumulants. At finite times \(N_t\) is not assumed Poisson, and the claims concern the \(t\to\infty\) limits at fixed nonzero \(g,\gamma\) and fixed \(\Delta\). Do not interchange this limit with \(g\to0\) or \(\gamma\to0\).

## Proof
**1. Exact regeneration and no-click resolvent.** Every click replaces the normalized state by \(|1\rangle\). Hence, after the first click, inter-click times are independent with a common law \(\tau\). For an unnormalized density matrix evolving under the no-click generator
\[
\mathcal L_0\rho=-i[H,\rho]-\frac\gamma2\{P_1,\rho\},
\]
write \(p_0=\rho_{00}\), \(p_1=\rho_{11}\), \(x=\operatorname{Re}\rho_{01}\), and \(y=\operatorname{Im}\rho_{01}\). In this order, the generator is
\[
A_0=\begin{pmatrix}
0&0&0&-2g\\
0&-\gamma&0&2g\\
0&0&-\gamma/2&\Delta\\
g&-g&-\Delta&-\gamma/2
\end{pmatrix}.
\]
The post-click initial vector is \(e=(0,1,0,0)^{\mathsf T}\). The waiting-time density is \(f(t)=\gamma(e^{tA_0}e)_2\), indexed from \(p_0\) as the first coordinate. It is a probability density: the no-click survival probability is \(\operatorname{tr}(e^{t\mathcal L_0}P_1)\); its derivative is \(-f(t)\). Moreover it decays exponentially. Indeed, if a no-click solution failed to decay, it would possess a nondecaying eigendirection annihilated by \(P_1\), while \(g>0\) makes the kernel of \(P_1\) noninvariant under \(H\). The finite-dimensional dissipative semigroup therefore has strictly negative spectral abscissa. Thus \(\tau\) has moments of every order and a positive exponential moment.

Put \(M(s)=(s+\gamma/2)^2+\Delta^2\). Inverting \(sI-A_0\), for \(s\ge0\), gives
\[
\widehat f(s)=\gamma[(sI-A_0)^{-1}e]_2
=\frac{\gamma[sM(s)+g^2(\gamma+2s)]}{s(s+\gamma)M(s)+g^2(\gamma+2s)^2}.
\tag{1}
\]
At \(s=0\) the numerator and denominator both equal \(g^2\gamma^2\), so \(\widehat f(0)=1\). As an independent representation, the tilted counting generator \(A_q=A_0+\gamma e^q E_{22}\), where \(E_{22}\) projects onto the \(p_1\) coordinate, has characteristic equation
\[
\det(sI-A_q)=s(s+\gamma)M(s)+g^2(\gamma+2s)^2
-e^q\gamma[sM(s)+g^2(\gamma+2s)]=0.
\tag{2}
\]
Here and below the matrix \(E_{22}\) indexes its diagonal coordinate from one.

**2. Why the long-time cumulants exist.** The positive exponential moment and continuous, nonlattice waiting law imply an analytic renewal pole near \(q=0\). Equivalently, the unique real eigenvalue \(s(q)\) near zero of \(A_q\), with \(s(0)=0\), is analytic: at \(q=0\), the stationary unconditional Lindblad generator is primitive because \(g>0\) mixes the measurement eigenspaces; it has a simple eigenvalue zero and all other eigenvalues strictly in the left half-plane. Consequently, for each fixed \(j\le4\), the long-time cumulant rate is \(K_j=s^{(j)}(0)\). The initial state affects only the prefactor in the corresponding tilted semigroup, and so does not affect \(K_j\).

Equation (2), or the renewal identity, is equivalent near zero to
\[
q=\log\frac{s(s+\gamma)M(s)+g^2(\gamma+2s)^2}
{\gamma[sM(s)+g^2(\gamma+2s)]}.
\tag{3}
\]
Its derivative with respect to \(s\) at zero equals \(2/\gamma>0\), guaranteeing a unique analytic inverse \(s=s(q)\) there.

**3. Exact cumulants.** Expand the right side of (3) as \(q=a_1s+a_2s^2+a_3s^3+a_4s^4+O(s^5)\). Direct differentiation yields
\[
\begin{aligned}
a_1&=2/\gamma,\\
a_2&=-\frac{4\Delta^2+8g^2+\gamma^2}{4g^2\gamma^2},\\
a_3&=\frac{48\Delta^4+192\Delta^2g^2+24\Delta^2\gamma^2+128g^4+3\gamma^4}{48g^4\gamma^3},\\
a_4&=-\frac{64\Delta^6+416\Delta^4g^2+48\Delta^4\gamma^2+768\Delta^2g^4+80\Delta^2g^2\gamma^2+12\Delta^2\gamma^4+256g^6-6g^2\gamma^4+\gamma^6}{64g^6\gamma^4}.
\end{aligned}
\]
Series reversion \(s(q)=c_1q+c_2q^2+c_3q^3+c_4q^4+O(q^5)\) gives
\[
\begin{aligned}
c_1&=a_1^{-1},\\
c_2&=-a_2c_1^2/a_1,\\
c_3&=-(2a_2c_1c_2+a_3c_1^3)/a_1,\\
c_4&=-[a_2(c_2^2+2c_1c_3)+3a_3c_1^2c_2+a_4c_1^4]/a_1.
\end{aligned}
\]
Using \(K_j=j!c_j\) and simplifying yields exactly the four expressions in **Finding**, including cancellation of every detuning term from \(K_3\).

**4. The sign classification.** Write \(u=\gamma^2/g^2>0\) and \(v=\Delta^2/g^2\ge0\). Then \(K_4=\gamma P(u,v)/1024\). The polynomial \(P(u,0)=512+1600u+48u^2-3u^3\) has exactly one positive root by Descartes' rule of signs, and changes from positive to negative at that root. For each fixed \(u>0\),
\[
\frac{\partial^2P}{\partial v^2}(u,v)=-2(768+144u)-1152v<0,
\qquad \lim_{v\to\infty}P(u,v)=-\infty.
\]
If \(0<u<u_*\), \(P(u,0)>0\), so strict concavity ensures a unique positive crossing: the derivative decreases strictly and, after any initial increase, the function decreases strictly to \(-\infty\). If \(u\ge u_*\), \(P(u,0)\le0\) and \(\partial_vP(u,0)=256-36u^2<0\) (since \(u_*>8/3\)); the negative second derivative then gives \(P(u,v)<0\) for all \(v>0\). This proves every assertion and the equality cases.

## Verification
Run `python3 checker.py` next to this document. Its standard-library `Fraction` calculations check the inverse power-series coefficients and all four displayed cumulants at 100 rational parameter triples; an independently assembled four-by-four tilted generator is checked against the exact characteristic polynomial at 800 parameter/spectral points. A second independent rational linear solve checks the resolvent (1) at 200 positive Laplace arguments, and examples are checked on both sides of the fourth-cumulant boundary. Exact arithmetic makes these finite algebraic tests reproducible. The infinite-time assertion, analyticity, and full sign classification come from the proof above, **not** from finite testing. The checker reports its actual counts.

## Relationship to prior work
Dubey, Chetrite, and Dhar (arXiv:2210.15188, first submitted 27 October 2022) study the continuous probe-monitoring protocol with \(\Delta=0\), obtain its full finite-time click-count transform and mean, and analyze dynamical transitions. Their source already covers the resonant process, and any cumulant obtained solely by differentiation of that resonant transform is not claimed separately as new. The present claim concerns the *detuned* Hamiltonian, which moves trajectories off the single-angle state manifold, and a complete, two-parameter sign classification of the fourth count cumulant together with the detuning cancellation in the third.

Landi, Kewming, Mitchison, and Potts (arXiv:2303.04270, first submitted 7 March 2023) explain tilted-Lindbladian and renewal techniques for current fluctuations. Those general tools are used here and are not newly introduced. Their illustrative dephased qubit uses a different diffusive unraveling and does not give the detuned \(\sqrt\gamma P_1\) click-count cumulant phase boundary displayed above. The sign change is a model-specific result, not a claimed new general fluctuation theorem.

## Limitations
The model assumes ideal unit-efficiency projection upon each counted jump and no independent unmonitored jump channels. It applies to fixed finite positive \(g,\gamma\) and real \(\Delta\); it does not assert a uniform approximation when \(g\to0\), nor a finite-time cumulant sign law. The Gaussian central limit for long counts is compatible with a negative fourth cumulant rate. The novelty assessment is limited by the possibility of unlocated implicit treatment in the broad full-counting-statistics literature and is not an independent priority certificate. No experiment is claimed.

## References
1. V. Dubey, R. Chetrite, A. Dhar, *Quantum resetting in continuous measurement induced dynamics of a qubit*, arXiv:2210.15188 (first posted 2022-10-27), https://arxiv.org/abs/2210.15188 .
2. G. T. Landi, M. J. Kewming, M. T. Mitchison, P. P. Potts, *Current fluctuations in open quantum systems: Bridging the gap between quantum continuous measurements and full counting statistics*, arXiv:2303.04270 (first posted 2023-03-07), https://arxiv.org/abs/2303.04270 .
