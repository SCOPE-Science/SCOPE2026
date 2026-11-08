# Microscopic recurrence switch and linear moment escape in a position-feedback random walk

## Finding

Fix the minimal spatial threshold \(\ell=1\) in the position-dependent-step random walk of Lima and Curado [1]. For every positive integer rule parameter \(r\), its **exact discrete** Markov chain on \(\mathbb Z\) has a unique stationary distribution and is uniformly geometrically ergodic. Nevertheless, the stationary absolute first moment is infinite, and the finite-time expected absolute position grows linearly.

The family has a sharp **integer recurrence switch** at \(r=2\): only \(r=1\) admits recurrent visits to the physical origin. For \(r\ge2\), the origin is transient and the stationary measure has no mass in the central three-site region. Explicitly, with \(a_k=3\cdot2^k-1\) for \(k\ge0\),

\[
\begin{aligned}
\pi_1(0)&=\pi_1(1)=\pi_1(-1)=\frac15,\\
\pi_1(+a_k)&=\pi_1(-a_k)=\frac{1}{5\cdot2^{k+1}},\\
\pi_1(x)&=0\quad\text{otherwise}.
\end{aligned}
\]

For each integer \(r\ge2\), with \(b_{r,k}=r(2^{k+1}-1)\),

\[
\pi_r(+b_{r,k})=\pi_r(-b_{r,k})=2^{-k-2},
\qquad \pi_r(x)=0\quad\text{otherwise}.
\]

For every initial site \(x\in\mathbb Z\), convergence in total variation is bounded by

\[
\begin{aligned}
\|P_1^t(x,\cdot)-\pi_1\|_{\rm TV}&\le(15/16)^{\lfloor t/4\rfloor},\\
\|P_r^t(x,\cdot)-\pi_r\|_{\rm TV}&\le(7/8)^{\lfloor t/5\rfloor},\quad r\ge2.
\end{aligned}
\]

The discrete stationary tails are *not* asymptotic to a single constant times the reciprocal of distance. In fact,

\[
\begin{aligned}
\liminf_{z\to\infty}z\,\pi_1(|X|>z)&=3/5,
&\limsup_{z\to\infty}z\,\pi_1(|X|>z)&=6/5,\\
\liminf_{z\to\infty}z\,\pi_r(|X|>z)&=r,
&\limsup_{z\to\infty}z\,\pi_r(|X|>z)&=2r\quad(r\ge2).
\end{aligned}
\]

For all positive \(p\), \(\mathbb E_{\pi_r}|X|^p<\infty\) if and only if \(p<1\). In contrast, for each deterministic finite starting site \(x\),

\[
\begin{aligned}
\mathbb E_x|X_t|&=\frac35t+O_x(1), &&r=1,\\
\mathbb E_x|X_t|&=rt+O_x(1), &&r\ge2.
\end{aligned}
\]

The second relation is the exact identity \(\mathbb E_x|X_t|=|x|+rt\) for every \(|x|\ge2\) and \(r\ge2\). Thus strong convergence in distribution and divergence of first moments coexist without conflict.

## Assumptions and scope

Let \((\sigma_t)_{t\ge0}\) be independent, equiprobable signs, and let \(X_0=x\in\mathbb Z\) be deterministic. Set \(\ell=1\), choose integer \(r\ge1\), and use the **exact prepoint lattice rule** [1], in units of the elementary spatial step,

\[
X_{t+1}=X_t+\sigma_t s_r(X_t),\qquad
s_r(n)=\begin{cases}1,&|n|\le1,\\ |n|+r,&|n|\ge2.\end{cases}
\]

No continuum or small-jump approximation is used. The statements hold for each nonnegative integer \(t\); all stationary distributions are probability measures on the integers. The parameter \(r\) is discrete; the origin-recurrence switch is not a continuous-parameter thermodynamic phase transition.

## Proof

**1. Exact transition graph.** If \(n\ge2\), the two possible successors are \(-r\) and \(2n+r\). If \(n\le-2\), they are \(+r\) and \(2n-r\). At the center, \(0\mapsto\{\pm1\}\), \(+1\mapsto\{0,2\}\), and \(-1\mapsto\{0,-2\}\), all choices having probability \(1/2\). Every exterior excursion therefore resets in one direction to the opposite-sign site of magnitude \(r\), or doubles its magnitude after an affine shift in the other direction.

**2. Communicating support and stationary mass at \(r=1\).** The central set \(\{0,\pm1\}\) communicates with the two excursion ladders \(\{\pm a_k:k\ge0\}\), since \(+1\mapsto+2\), \(-1\mapsto-2\), and each outer reset returns to the opposite site \(\mp1\). Each ladder grows by \(a_{k+1}=2a_k+1\). This is a closed irreducible class \(C_1\). At any site outside it, each successive exterior step has probability \(1/2\) of jumping into \(\{\pm1\}\); the probability of never doing so vanishes. Hence no other closed recurrent class exists.

The displayed mass has total one: the center contributes \(3/5\) and the two ladders together contribute \(\sum_{k\ge0}2/(5\cdot2^{k+1})=2/5\). The incoming mass to \(0\) is half the mass at each of \(\pm1\), totaling \(1/5\). The incoming mass to either site \(\pm1\) is half the mass at \(0\) plus half the total mass on the opposite excursion ladder, again \(1/5\). The site \(\pm a_0\) receives half of \(\pi_1(\pm1)\), and every \(\pm a_k\), \(k\ge1\), receives half the mass at its same-sign predecessor. These identities prove invariance.

**3. Communicating support and stationary mass at \(r\ge2\).** The exterior region \(\{|n|\ge2\}\) is forward invariant; in particular no exterior path can revisit \(0\) or \(\pm1\). From any exterior site, the first reset lands on \(\pm r\), almost surely in finite time, since the probability of avoiding a reset for \(m\) steps is \(2^{-m}\). Starting in the center, the finite simple-walk segment reaches \(\pm2\) almost surely, after which the same argument applies. The unique closed class is therefore \(C_r=\{\pm b_{r,k}:k\ge0\}\), with \(b_{r,k+1}=2b_{r,k}+r\). At each seed \(\pm r\), total influx is one half of the mass on the opposite-sign ladder, hence \(1/4\). At higher levels the same-sign predecessor contributes half its mass. The displayed \(\pi_r\) satisfies these equations and has mass \(2\sum_{k\ge0}2^{-k-2}=1\). The origin has no invariant mass for \(r\ge2\). Starting at \(0\), each departure from the center has probability \(1/2\) of escaping to \(\pm2\) before returning; hence the number of visits to \(0\), counting the initial visit, has mean \(2\). For \(r=1\), recurrence of \(0\) and Kac's formula give mean first return time \(5\).

**4. Uniform mixing, including arbitrary sites outside the support.** For \(r=1\), every site reaches \(0\) in four moves along a particular allowed path, each of probability \(2^{-4}\). The paths are

- \(0\to1\to0\to1\to0\);
- \(+1\to+2\to+5\to-1\to0\) and its reflection;
- for all \(n\ge2\), \(n\to-1\to-2\to+1\to0\), and its reflection for \(n\le-2\).

Consequently \(P_1^4(x,\{0\})\ge1/16\) for every integer \(x\). For \(r\ge2\), from every integer \(x\) the probability of being in \(C_r\) after three moves is at least \(1/4\). From any \(y\in C_r\), the two-step choices inward-inward and outward-inward reach the two seed sites \(+r,-r\), each with probability \(1/4\). It follows that \(P_r^5(x,\{+r\})\ge1/16\) and \(P_r^5(x,\{-r\})\ge1/16\). These are global Doeblin minorizations: respectively \(P_1^4\ge(1/16)\delta_0\) and \(P_r^5\ge(1/8)(\delta_{+r}+\delta_{-r})/2\). The standard contraction argument gives the two stated total-variation bounds, existence of a unique invariant law, and convergence independent of the initial site.

**5. Exact discrete tails and moment cutoff.** The level-tail sums are geometric:

\[
\pi_1(|X|\ge a_k)=\tfrac25 2^{-k},\qquad
\pi_r(|X|\ge b_{r,k})=2^{-k}\quad(r\ge2).
\]

For \(a_k\le z<a_{k+1}\), the strict r=1 tail is \((2/5)2^{-(k+1)}\); for \(b_{r,k}\le z<b_{r,k+1}\), the strict tail for \(r\ge2\) is \(2^{-(k+1)}\). Multiplication by \(z\) at the two ends of successive gaps proves all four liminf/limsup formulas. The stationary \(p\)-th absolute moment is a geometric series with term size comparable to \(2^{(p-1)k}\). Therefore it is finite exactly when \(p<1\).

**6. Linear escape of finite-time absolute moments.** Directly conditioning on \(X_t=n\) yields

\[
\mathbb E\bigl[|X_{t+1}|-|X_t|\mid X_t=n\bigr]
=\begin{cases}1,&n=0,\\0,&|n|=1,\\r,&|n|\ge2.\end{cases}
\]

For \(r=1\), this is \(1-\mathbf1_{\{|n|=1\}}\). The mixing bound implies \(\Pr_x(|X_t|=1)=2/5+O((15/16)^{\lfloor t/4\rfloor})\), with error uniformly bounded for each starting site. Summing the conditional drift gives \(\mathbb E_x|X_t|=(3/5)t+O_x(1)\). For \(r\ge2\), every path beginning with \(|x|\ge2\) remains exterior, so the conditional drift is always \(r\), proving the exact identity. From central starting sites the time spent in \(\{0,\pm1\}\) has a geometric tail, because within three steps there is probability at least \(1/4\) of entering the absorbing exterior class; its finite expected occupation contributes only a bounded correction. Thus \(\mathbb E_x|X_t|=rt+O_x(1)\) for all integer starts.

## Verification

The standalone file `verify.py` uses Python's exact `Fraction` arithmetic. It checks the transition kernel, prescribed stationary masses and incoming flux at thousands of integer sites, verifies the finite-step Doeblin minorization for many initial states, and compares finite-time first moments with the exact conditional-drift identities. Run `python3 verify.py` alongside this file. These finite checks do not establish the infinite-support claims; the proof above does.

## Relationship to prior work

Lima and Curado [1], whose first public version is dated May 21, 2026, introduce this microscopic walk and study large-threshold numerical simulations together with a smooth continuum stationary density. Their work supplies the update rule and the heavy-tail motivation. The present finding isolates the previously untreated minimal lattice threshold and determines its **exact discrete recurrent support, origin occupation, mixing and moment dynamics**; it does not present the continuum equation or the heavy-tail phenomenon itself as new.

The geometric ladder for \(r\ge2\), after the affine change \(1+|X|/r\), is a standard multiplicative-reset process. Montero and Villarroel [2] and Zanette and Manrubia [3] already derive geometric stationary laws and moment cutoffs for generic reset processes. These generic results directly explain the positive-\(r\) exterior ladder; no novelty is claimed for geometric resetting in isolation. In the original walk the central three-site motion survives only at \(r=1\), where it changes the support, stationary weights, origin recurrence and finite-time moment slope. The complete threshold-specific classification and its all-initial-state uniform mixing bounds require the additional central-state transition analysis given here.

## Limitations

The result concerns only the exact microscopic regime \(\ell=1\), not arbitrary positive thresholds \(\ell>1\) or a continuum scaling limit. The reset-like transitions are deterministic consequences of the original position-dependent step and should not be confused with an externally imposed resetting mechanism. The parameter switch occurs between two integer values and is not a thermodynamic singularity. Universal stationary moment divergence is consistent with geometric total-variation mixing because the observable \(|X|\) is unbounded; no convergence of its expectation is asserted. A wider generic renewal theorem may subsume the central-state derivation after an appropriate state augmentation; the specific lattice classification has been compared with the primary sources listed below but has not undergone independent verification.

## References

1. H. S. Lima and E. M. F. Curado, *Emergent heavy-tailed distributions from a Markovian random walk*, arXiv:2605.22933v1 (first public May 21, 2026), https://arxiv.org/abs/2605.22933 ; *Physical Review E* **114**, 034114 (2026), https://doi.org/10.1103/f1bd-1242 .
2. M. Montero and J. Villarroel, *Directed random walk with random restarts: The Sisyphus random walk*, *Physical Review E* **94**, 032132 (2016), https://doi.org/10.1103/PhysRevE.94.032132 , open full text https://diposit.ub.edu/bitstreams/557f3158-02eb-4d2f-b9a9-d3b31fd07fa6/download .
3. D. H. Zanette and S. Manrubia, *Fat tails and black swans: Exact results for multiplicative processes with resets*, *Chaos* **30**, 033104 (2020), https://doi.org/10.1063/1.5141837 , open preprint arXiv:2105.11679v1, https://arxiv.org/abs/2105.11679 .
