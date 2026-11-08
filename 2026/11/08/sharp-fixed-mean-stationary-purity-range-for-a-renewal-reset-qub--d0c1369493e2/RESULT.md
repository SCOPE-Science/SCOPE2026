# Sharp fixed-mean stationary purity range for a renewal-reset qubit

## Finding

Fix an energy-gap angular frequency \(\Omega>0\), an i.i.d. strictly positive reset-interarrival time \(T\) with finite prescribed mean \(\mu>0\), and a qubit Hamiltonian \(H=\hbar\Omega\lvert1\rangle\langle1\rvert\). At each reset the qubit is re-prepared in the same density matrix
\[
\rho_0=\begin{pmatrix}p&c\\\overline c&1-p\end{pmatrix},\qquad
0<p<1,\qquad 0<|c|^2\le p(1-p).
\]
The renewal clock is initialized in its stationary version; the reported state is the ensemble-averaged qubit state at a time sampled from this stationary clock, **not** the phase-dependent limit of a clock started at a reset instant. Define \(m=\Omega\mu\), \(P_0=p^2+(1-p)^2\), and
\[
G(m)=\begin{cases}2\sin(m/2),&0<m\le\pi,\\2,&m\ge\pi.\end{cases}
\]
Then the exact set of attainable stationary ensemble purities \(\operatorname{tr}(\rho_*^2)\), over all such interarrival laws with mean \(\mu\), is
\[
\boxed{\begin{cases}
(P_0,\,P_0+2|c|^2G(m)^2/m^2],&0<m<2\pi,\\
[P_0,\,P_0+2|c|^2G(m)^2/m^2],&m\ge2\pi.
\end{cases}}
\]
The upper endpoint is attained uniquely by deterministic interarrivals \(T=\mu\) when \(m\le\pi\). When \(m>\pi\), it is attained **exactly** by laws supported on odd half-turn periods \(\Omega T\in\{(2k+1)\pi:k=0,1,\ldots\}\) with mean \(m\). The lower endpoint is attained if and only if \(m\ge2\pi\), by laws supported on full-turn periods \(\Omega T\in\{2k\pi:k=1,2,\ldots\}\) with mean \(m\). These support characterizations include all equality cases and permit two-point extremizers at each attainable endpoint.

## Assumptions and scope

The qubit evolves unitarily between reset events, with no additional dissipation. Each reset instantaneously replaces its density operator by the fixed coherent \(\rho_0\); reset intervals are i.i.d., positive almost surely, and have finite positive mean. No density, nonlattice condition, variance assumption, or upper bound on reset intervals is imposed. The stationary renewal clock is obtained by length-biasing renewal intervals and sampling a uniform location inside the selected interval. This construction exists for every positive integrable interarrival law; for a deterministic interval law it randomizes the clock phase. The purity is the purity of the **averaged** stationary density operator; averaging the purities of single pure-state trajectories would give a different observable.

The thresholds \(m=\pi\) and \(m=2\pi\) refer respectively to the first half-turn and full-turn time of the Hamiltonian gap. The boundary cases are included in the displayed intervals and equality conditions.

## Proof

**Stationary renewal representation.** For any nonnegative measurable \(f\), the renewal reward identity for the stationary clock gives
\[
\mathbb E f(A)=\frac1\mu\mathbb E\int_0^T f(s)\,ds
=\frac1\mu\int_0^\infty f(s)\Pr(T>s)\,ds,
\]
where \(A\) is the stationary elapsed time since the most recent reset. The formula extends to complex bounded \(f\) by absolute integrability. Under \(H\), the off-diagonal element of the state aged \(s\) is \(ce^{i\Omega s}\). Hence
\[
\rho_*=\begin{pmatrix}p&c\chi\\\overline{c\chi}&1-p\end{pmatrix},\qquad
\chi=\frac1\mu\mathbb E\int_0^T e^{i\Omega s}\,ds
=\frac{\mathbb E[e^{iX}]-1}{im},\quad X=\Omega T>0,\quad \mathbb E X=m.
\]
Consequently
\[
\operatorname{tr}(\rho_*^2)=P_0+2|c|^2\frac{|1-\mathbb E[e^{iX}]|^2}{m^2}.
\]
These identities also prove that the stationary density matrix is well defined without a finite second interarrival moment.

**Sharp upper bound.** Define the scalar function on \([0,\infty)\)
\[
g(x)=\begin{cases}2\sin(x/2),&0\le x\le\pi,\\2,&x\ge\pi.\end{cases}
\]
The function is globally concave: on \((0,\pi)\) its second derivative is \(-\tfrac12\sin(x/2)<0\), its left derivative at \(\pi\) is zero, and it is constant thereafter. Moreover \(|1-e^{ix}|=2|\sin(x/2)|\le g(x)\) for every \(x\ge0\). Thus the triangle inequality and Jensen inequality yield
\[
|1-\mathbb E[e^{iX}]|\le\mathbb E|1-e^{iX}|\le\mathbb E g(X)\le g(\mathbb E X)=G(m).
\]
For \(0<m<\pi\), equality in Jensen requires \(X=m\) almost surely: strict concavity applies below \(\pi\), and mixing any point below \(\pi\) with a larger one also makes Jensen strict. At \(m=\pi\), equality forces \(|1-e^{iX}|=2\) almost surely, hence \(X\) is an odd positive multiple of \(\pi\); the mean \(\pi\) forces \(X=\pi\). When \(m>\pi\), equality forces \(|1-e^{iX}|=2\) almost surely, equivalently \(X\in\{\pi,3\pi,5\pi,\ldots\}\). Conversely all such laws have \(e^{iX}=-1\) almost surely, so they saturate the bound. Their convex hull of possible means is \([\pi,\infty)\). In particular, for \(m>\pi\), choose adjacent odd multiples \(a\le m\le b=a+2\pi\) with weights \((b-m)/(2\pi)\) at \(a\) and \((m-a)/(2\pi)\) at \(b\). This proves both sharpness and exhaustive upper equality cases.

**Lower endpoint and attainment.** The general lower bound is \(\operatorname{tr}(\rho_*^2)\ge P_0\). Because \(c\ne0\), equality holds precisely when \(\mathbb E e^{iX}=1\). The nonnegative random variable \(1-\cos X\) then has zero mean, so \(X\in\{2\pi,4\pi,6\pi,\ldots\}\) almost surely (strict positivity excludes zero). Such a law has mean at least \(2\pi\). Conversely every \(m\ge2\pi\) is a convex combination of two adjacent positive full-turn values and hence attains the lower endpoint. When \(0<m<2\pi\), choose \(0<\varepsilon<m\) and the two-point law supported on \(\{\varepsilon,2\pi\}\), with weight \((m-\varepsilon)/(2\pi-\varepsilon)\) at \(2\pi\). Its mean is exactly \(m\), and \(\mathbb E e^{iX}\to1\) as \(\varepsilon\downarrow0\). The lower endpoint is therefore a strict, approachable infimum in this regime.

**No gaps in the attainable set.** Probability distributions with a fixed mean form a convex set. The map from a reset law to \(\mathbb E e^{iX}\) is affine, and purity is continuous along each convex interpolation. Interpolating a maximizing law with an exact minimizing law (when \(m\ge2\pi\)) or with a sequence approaching the minimum (when \(m<2\pi\)) attains every intermediate purity by the intermediate value theorem. This proves the stated complete intervals.

## Verification

Run `python3 verify_qubit_purity.py` with Python 3 and NumPy installed. Its checks independently compute the purity from finite-support renewal occupation integrals and Fourier transforms, verify all explicit equality constructions and nonattainment approximations, and compare random positive finite-support laws at fixed means against the sharp bounds. The checker is a finite diagnostic, not the proof of global optimality; global quantifiers, unbounded supports, and equality cases are proved by the concavity and nonnegativity arguments above.

For example, for a coherent equatorial pure reset state \(p=1/2\), \(|c|=1/2\), at \(m=\pi\) the maximal purity is \(\tfrac12+2/\pi^2\). At \(m=2\pi\), the full-turn reset protocol has the exactly dephased purity \(1/2\), while the optimal odd-half-turn mixture has purity \(\tfrac12+1/(2\pi^2)\).

## Relationship to prior work

Sevilla and Valdés-Hernández derived the general renewal formulation of a resetting quantum density operator, the stationary coherence factor, and the stationary purity functional (their stationary-density Eq. (27) and purity Eq. (42)). Those equations are taken as known background; they do not state a fixed-mean optimization over all renewal laws or its attained/unattained extremizers. The present theorem applies an explicit global concave envelope to classify the attainable purity values, both threshold transitions, and every equality law under the fixed-mean constraint. A previously established stationary quantum renewal comparison for integer-shape Erlang clocks determines when purity is above or below reset-state fidelity; it does not optimize purity over arbitrary laws at a fixed mean, so its result neither supplies the two thresholds nor implies the extremizer classification here.

Wald, Yao, Platini, Hooley and Carollo study a *discrete-time gate process*, correlations and resonances, including deterministic resetting that fails to converge from a fixed initial phase. Their problem is not the stationary-phase-sampled continuous-time qubit with arbitrarily distributed positive renewal intervals and a fixed mean. Rose, Touchette, Lesanovsky and Garrahan treat state-independent *Poissonian* resetting in quantum Markov dynamics, a restricted reset-law class which cannot furnish the distribution-free optimum.

## Limitations

The theorem concerns ensemble stationary purity of a two-level unitary system only; it does not optimize convergence rates from a fixed reset phase, energetic reset costs, time-dependent gates, multi-gap many-level systems, or first-detection time. A deterministic renewal clock initialized at a reset event does not generally converge in time to the phase-stationary mixed state: the stationary-clock initialization is essential. It does not establish originality against every unindexed paper or general convex-geometric theorem. No independent scientific audit is claimed.

## References

1. F. J. Sevilla and A. Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting*, arXiv:2209.05643 (first posted 2022-09-12), especially Secs. 2.1, 3.1, 3.3, and 4. https://arxiv.org/abs/2209.05643
2. S. Wald, L. H. Yao, T. Platini, C. Hooley and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497 (first posted 2024-10-15), Quantum 9, 1742 (2025), especially Secs. 2 and 4. https://arxiv.org/abs/2410.11497
3. D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, Phys. Rev. E 98, 022129 (2018). https://doi.org/10.1103/PhysRevE.98.022129
