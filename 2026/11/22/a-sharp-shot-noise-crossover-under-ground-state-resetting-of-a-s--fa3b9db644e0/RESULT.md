# A sharp shot-noise crossover under ground-state resetting of a shelved three-level emitter

## Finding

An incoherently pumped three-level emitter has a sharp, radiative-decay-independent threshold for the *sign* of long-time photon-count noise under independent stochastic re-preparation of the ground state. Let \(p,\gamma,s,u>0\) respectively denote pumping, counted emission, shelving, and natural dark-state recovery rates. Independent complete Poisson re-preparation of the ground state occurs at rate \(r\geq0\). Define
\[
q=u+r,\qquad H(r)=q(\gamma+p+s+r)+ps.
\]
Then the stationary emission count rate and asymptotic photon Fano factor are exactly
\[
\boxed{J(r)=\frac{\gamma p q}{H(r)},\qquad
F(r)=1+\frac{2\gamma p\bigl(ps-q^2\bigr)}{H(r)^2}.}
\]
Here \(J(r)=\lim_{t\to\infty}\mathbb E N_t/t\) and \(F(r)=\lim_{t\to\infty}\operatorname{Var}(N_t)/\mathbb E N_t\). If \(ps>u^2\), there is exactly one nonnegative reset-rate crossing, at the strictly positive rate
\[
\boxed{r_*=\sqrt{ps}-u,}
\]
with \(F(r)>1\) for \(0\leq r<r_*\), \(F(r_*)=1\), and \(F(r)<1\) for \(r>r_*\). When \(ps=u^2\), equality holds only at \(r=0\) and strict sub-Poisson noise holds for all \(r>0\). When \(ps<u^2\), strict sub-Poisson noise holds for every \(r\geq0\). The sign boundary does not depend on \(\gamma\), although \(F\) and \(J\) do.

The equality \(F(r_*)=1\) is *not* Poissonian photon emission. In the strictly crossing case, set \(q_* = \sqrt{ps}\) and \(H_*=H(r_*)\). The third asymptotic normalized photon-count cumulant obeys the strict exact identity
\[
\boxed{\lim_{t\to\infty}\frac{\kappa_3(N_t)}{\mathbb E N_t}
=1-\frac{6\gamma^2p^2q_*^2}{H_*^3}<1.}
\]
For example, when \(p=\gamma=s=1\) and \(u=1/5\), the unique crossing is \(r_*=4/5\); the Fano factor changes from \(7/4\) at zero resetting to \(1\) at the crossing, while the normalized third count cumulant at the crossing is \(1-125/2304\). [The exact last rational is independently checked in the bundled checker.]

## Assumptions and scope

The state space is \(\{G,E,D\}\). State transitions are \(G\xrightarrow{p}E\), \(E\xrightarrow{\gamma}G\), \(E\xrightarrow{s}D\), and \(D\xrightarrow{u}G\). Only the \(E\xrightarrow{\gamma}G\) transition increments \(N_t\). A separate memoryless clock of intensity \(r\) returns any state to \(G\); if already in \(G\), the preparation is a null state transition. Reset events do not count as photons and do not alter the underlying radiative jump rates. All four intrinsic rates are strictly positive and the reset rate is finite and nonnegative. The stationary finite-state process is ergodic. Counts are ideal, with no dark detector counts, dead time, missed photons, coherent driving, or reset energy accounting. This is a classical-population sector of a three-level open-quantum-system jump model, not a statement about coherently driven emitters.

## Proof

1. Each recorded emission returns the state to \(G\); independent memoryless clock increments and the strong Markov property imply that consecutive inter-emission waiting times \(T\) are independent and identically distributed. The residual initial interval under stationary initialization does not affect asymptotic count cumulants. Between emissions, form the transient generator (with counted jumps removed), in the state order \((G,E,D)\):
\[
A=\begin{pmatrix}
 p&-p&0\\
 -r&\gamma+s+r&-s\\
 -(u+r)&0&u+r
\end{pmatrix}.
\]
The Laplace transform of the waiting-time density is \(\widehat f(z)=\gamma[(A+zI)^{-1}]_{GE}\), i.e.
\[
\widehat f(z)=\frac{\gamma p(q+z)}
{z^3+(\gamma+p+s+u+2r)z^2+(\gamma p+H(r))z+\gamma p q}.
\]
The expression has \(\widehat f(0)=1\) and exponentially decaying waiting-time tails for all stated rates.

2. Differentiate at zero to calculate \(\mu=\mathbb E T=H/(\gamma p q)\) and \(\sigma^2=\mathbb E T^2-\mu^2\). Renewal-reward counting identities give \(J=\mu^{-1}\) and \(F=\sigma^2/\mu^2\). Clearing the positive denominator in the differentiated rational transform yields exactly
\[
F-1=\frac{2\gamma p\bigl(ps-(u+r)^2\bigr)}{H^2}.
\]
Since \(\gamma,p,H>0\) and \(u+r\) strictly increases with \(r\), the sign classifications and unique crossing follow without numerical root searches. In the strong-reset limit \(r\to\infty\), \(F(r)=1-2\gamma p/r^2+O(r^{-3})\) and \(J(r)\sim\gamma p/r\).

3. For a renewal process with waiting-time third cumulant \(\kappa_3(T)\), the long-time normalized third counting cumulant is
\[
S_3=\frac{3\sigma^4}{\mu^4}-\frac{\kappa_3(T)}{\mu^3}.
\]
This follows by differentiating three times the implicit scaled-cumulant-generating equation \(e^k\widehat f(\lambda(k))=1\) at \(k=0\). Differentiate the rational \(\widehat f\), impose \(q^2=ps\), and simplify:
\[
S_3-1=-\frac{6\gamma^2p^2q^2}{H^3}.
\]
Every factor is strictly positive apart from the minus sign, proving \(S_3<1\) at the shot-noise crossing. Further, \(\lim_{z\to\infty}z\widehat f(z)=0\), so the inter-emission density satisfies \(f(0)=0\); an exponential waiting law would have \(f(0)>0\). Thus the photon process is not Poisson at any finite rate even if its Fano factor happens to equal one.

## Verification

The self-contained script `check.py` evaluates the resolvent and waiting-time derivatives symbolically, proves exact cancellation of both Fano and third-count-cumulant identities, and checks nine rational parameter combinations independently by differentiating the characteristic polynomial of the photon-count tilted generator. Run `python check.py` with SymPy installed. These finite test cases support the proof but do not replace the symbolic identities and strict inequalities. The source result has been checked with the checker extracted from its final serialized package.

## Relationship to prior work

Fei Liu's 2023 work develops counting statistics for quantum-jump processes subject to stochastic resetting, including general tilted constructions and coherent two-level examples; those constructions are not claimed as new here. Lachman and coauthors' 2024 work provides the same *reset-free* incoherent three-level shelving population model and analyzes finite-time photon coincidence observables. Its Appendix B explicitly contains the rates and photon correlation functions used as the physical starting point. This finding adds an independent reset clock, a complete all-rate sign boundary for long-time count Fano noise, and a strict third-count-cumulant distinction at the apparent Poisson crossing. General renewal identities are standard. The explicit crossing has not been located in the inspected sources, but a more general uninspected counting formula might imply it after specialization; publication priority remains subject to independent literature review.

## Limitations

This is a model-specific ideal asymptotic-count theorem. The word Poissonian at the threshold refers only to equality of asymptotic variance and mean, not a Poisson point process. No claim is made about finite-time Fano factors, an optimal reset rate for useful photon brightness, quantum-coherent lambda systems, detector imperfections, or the thermodynamic cost of re-preparation. The general reset-counting framework precedes this special calculation. An independent scientific audit has not been performed.

## References

- Fei Liu, *Semi-Markov Processes in Open Quantum Systems. II. Counting Statistics with Resetting*, arXiv:2308.02214, first posted 4 August 2023. https://arxiv.org/abs/2308.02214
- Lukáš Lachman, Ilya P. Radko, Maxime Bergamin, Ulrik L. Andersen, Alexander Huck, and Radim Filip, *Experimental certification of level dynamics in single-photon emitters*, Physical Review Research 6, 033254 (2024), Appendix B, especially equations (B11)–(B17). https://doi.org/10.1103/PhysRevResearch.6.033254
