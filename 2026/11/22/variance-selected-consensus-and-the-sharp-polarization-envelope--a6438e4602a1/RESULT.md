# Variance-selected consensus and the sharp polarization envelope in neutral fast-assortative imitation

## Finding

Consider the noise-free, zero-selection fast-assortative imitation equation on the continuous cooperation interval \([0,1]\). For **every** nontrivial initial probability measure \(\mu_0\), not just an initial two-cluster population, the final consensus is selected by its first two moments:

\[
\boxed{L=\sqrt{\frac{q_0+m_0^2}{2}}=\sqrt{m_0^2+\frac{v_0}{2}}},
\qquad
m_0=\int x\,d\mu_0,\quad q_0=\int x^2\,d\mu_0,\quad v_0=q_0-m_0^2.
\]

The quantity \(q(t)+m(t)^2\) is conserved for the entire transport evolution. For a prescribed initial mean \(0<m_0<1\), the consensus satisfies the **sharp universal envelope**

\[
\boxed{m_0\le L\le \sqrt{\frac{m_0(1+m_0)}{2}}}.
\]

The lower equality holds precisely for the homogeneous initial law \(\delta_{m_0}\); the upper equality holds precisely for the polarized Bernoulli law \((1-m_0)\delta_0+m_0\delta_1\). Every genuinely dispersed initial law strictly raises the final mean relative to its starting value. Initial laws with equal first and second moments have exactly the same consensus, irrespective of skewness, modality, or the number of distinct strategies.

## Assumptions and scope

The model is the fast-network deterministic mean-field transport equation of Russell, Nugent and Bara (2026), with interaction weights proportional to the sum of the participants' cooperation levels, pairwise Fermi-imitation selection intensity \(\beta=0\), and zero added noise. The state \(\mu_t\) is any probability measure supported in \([0,1]\), and the transport equation is

\[
\partial_t\mu_t+\partial_x(V_t\mu_t)=0,\qquad
V_t(x)=\frac{q(t)-x^2}{2(x+m(t))},
\]

where \(m(t)=\int x\,d\mu_t(x)\) and \(q(t)=\int x^2\,d\mu_t(x)\). For \(m_0>0\) the denominator is positive for all future times. The degenerate state \(\mu_0=\delta_0\) is constant under the defining microscopic update and is included separately, with \(L=0\). There is no restriction to atomically supported, absolutely continuous, or two-cluster initial data.

The same identities and final consensus formula hold for any fixed finite number \(N\ge1\) of deterministic agents with \(x_i\in[0,1]\), provided the degree normalization is the **complete fast-network sum including self-weight**, exactly as in the model's microscopic equation:

\[
\dot x_i=\frac{1}{N}\sum_{j=1}^N\frac{(x_i+x_j)(x_j-x_i)}{2(x_i+m)}
=\frac{q-x_i^2}{2(x_i+m)},
\quad m=N^{-1}\sum_i x_i,\quad q=N^{-1}\sum_i x_i^2.
\]

The finite-agent result concerns this deterministic system; it does not assert stochastic fixation or an arbitrary fixed-graph update rule.

## Proof

**1. Well-defined evolution and moment equations.** For \(m_0>0\), the original transport equation is well posed on \([0,1]\) and its velocity is bounded and locally Lipschitz because \(m(t)>0\). Its values on the boundary point inward, so mass cannot leave \([0,1]\). Write

\[
v=q-m^2\ge0,\qquad G(t)=\int_{[0,1]}\frac{d\mu_t(x)}{x+m(t)}.
\]

The exact algebraic decomposition

\[
V_t(x)=\frac{v(t)}{2(x+m(t))}-\frac{x-m(t)}{2}
\]

permits differentiation of the first two moments using the weak transport equation. Since the average of \(x-m\) vanishes and \(\int x/(x+m)\,d\mu=1-mG\), one obtains

\[
\dot m=\frac{vG}{2},\qquad
\dot q=-mvG,\qquad
\dot v=-2mvG.
\]

Consequently

\[
\frac{d}{dt}(q+m^2)=0.
\]

The same calculation follows by averaging \(\dot x_i\) and \(2x_i\dot x_i\) in any finite complete fast-network system stated above. The neutral dynamics therefore have an exact quadratic integral for arbitrary distributions, not just two masses.

**2. Convergence and exact selector.** Since \(\dot m\ge0\), \(m(t)\ge m_0>0\). Because \(x+m(t)\le2\) throughout the allowed state interval, \(G(t)\ge1/2\). Thus

\[
0\le v(t)\le v_0e^{-m_0t}.
\]

The bounded increasing mean has a limit \(L\in[0,1]\), and the vanishing variance gives \(q(t)\to L^2\). Conservation now forces \(2L^2=q_0+m_0^2\), giving the positive-root formula. More strongly, \(\int(x-L)^2d\mu_t=v(t)+(m(t)-L)^2\to0\), hence \(\mu_t\) converges to \(\delta_L\) in quadratic Wasserstein distance. If \(v_0>0\), then \(\dot m>0\) at all finite times and \(L>m_0\).

**3. Sharp extremal initial laws.** For a probability law on \([0,1]\), Jensen's inequality and \(x^2\le x\) give \(m_0^2\le q_0\le m_0\). The first equality characterizes point masses; the second characterizes laws supported on \(\{0,1\}\). Substitution into the exact consensus selector yields the stated sharp inequalities, with precisely the advertised equality cases at every prescribed interior mean.

## Verification

The standalone `verify.py` uses Python 3 standard-library exact fractions to check all moment-derivative identities on 1,400 independently generated rational configurations of one through fourteen strategy classes, including boundaries and repeated values. Eight separate deterministic trajectories are integrated with fourth-order Runge–Kutta and checked for agreement with the predicted invariant and consensus limit, including polarized, multimodal, uniform-grid, and already homogeneous configurations. The checker reports 1,400 exact-rational passes and eight numerical passes. Its numerical tests corroborate but do **not** replace the symbolic moment proof.

For the continuum uniform law, \(m_0=1/2\), \(q_0=1/3\), and the exact answer is \(L=\sqrt{7/24}=0.540061724867\ldots\), strictly above the starting mean. For the extremal fixed-mean law with \(m_0=1/3\), the exact maximal consensus is \(L=\sqrt2/3\).

Run from the extracted package with `python3 verify.py`. No external libraries or data files are required.

## Relationship to prior work

Russell, Nugent and Bara (2026), Equation (6), establish the fast-assortative transport equation and prove eventual Dirac consensus for general initial data (Theorem 3.2). Their Proposition 3.4 and Appendix B determine the neutral consensus for the **specific two-cluster mixture of pure cooperators and defectors**, \((1-p)\delta_0+p\delta_1\), as \(\sqrt{p(1+p)/2}\). Their auxiliary two-cluster quadratic invariant is the restriction of the general invariant proved here. In contrast, the result here determines the consensus for **every** probability law and identifies the sharp fixed-mean extremizers; it neither renames their binary mixture formula as new nor reclaims their convergence theorem.

Hendrickx and Olshevsky (2016) study convergence under symmetric continuum opinion interactions. That result concerns symmetric effective interactions and does not supply this selector for degree-normalized, state-dependent (generally asymmetric) update rates. Brede (2019) studies opinion influence and adaptive rewiring with bounded confidence, a different model without the specified quadratic moment identity. These related sources provide context, not proof of historical uniqueness.

## Limitations

The selection law requires exactly zero Fermi selection and zero noise, plus instantaneous fast assortative network equilibration and the stated degree normalization. It does not apply to arbitrary static networks, nonzero selection, finite network adaptation speed, or stochastic interaction events. This is a mathematical outcome of a mean-field/coordinated deterministic learning rule, not a prediction of how actual people behave. Although the two-cluster special case was known, the all-law extension and extremal interpretation have not received independent scientific validation; unlocated earlier equivalent formulations remain possible.

## References

1. B. Russell, A. Nugent and J. Bara, *Mean-field imitation dynamics on fast assortative networks*, arXiv:2606.11892v1 (first posted 2026-06-10). https://arxiv.org/abs/2606.11892 . Full author-posted text also accessible via https://www.researchgate.net/publication/406910216_Mean-field_imitation_dynamics_on_fast_assortative_networks .
2. J. M. Hendrickx and A. Olshevsky, *On Symmetric Continuum Opinion Dynamics*, SIAM Journal on Control and Optimization 54 (2016), 2893–2918, arXiv:1311.0355. https://arxiv.org/abs/1311.0355 .
3. M. Brede, *How Does Active Participation Affect Consensus: Adaptive Network Model of Opinion Dynamics and Influence Maximizing Rewiring*, Complexity (2019), Article 1486909. https://doi.org/10.1155/2019/1486909 .
