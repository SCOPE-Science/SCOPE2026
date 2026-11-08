# Sharp identifiability and noisy recovery of rotational switching itineraries

## Finding

Let \(p\ge5\) be an integer, \(2\le\ell\le p-2\), and \(1\le m<p\) with \(\gcd(m,p)=1\). Define the cyclic binary rotational word
\[
 w_i=\mathbf1_{\{im\bmod p<\ell\}},\qquad i\in\mathbb Z/p\mathbb Z.
\]
Let \(L=\min(\ell,p-\ell)\), \(r=\min(m,p-m)\), and let \(T\) denote the number of unequal adjacent pairs in the cyclic word. Then
\[
 T=2\min(L,r). \tag{1}
\]
Distinct values of \(r\) give distinct cyclic words up to rotation of their indices; hence the family has exactly \(\varphi(p)/2\) such necklaces. In particular, for odd prime \(p\), an observed adjacent-switch frequency distinguishes all necklaces at a fixed occupancy \(\ell\) **if and only if** \(\ell=(p-1)/2\) or \(\ell=(p+1)/2\). In other occupancies, the switch statistic identifies every \(r<L\), while precisely \((p+1)/2-L\) distinct necklaces have the same saturated count \(T=2L\).

For odd prime \(p\ge7\) and either balanced occupancy, suppose each independent trial selects a uniformly random index \(i\in\mathbb Z/p\mathbb Z\), obtains the adjacent pair \((w_i,w_{i+1})\), flips the two bits independently with a known probability \(\varepsilon\in[0,1/2]\), and records only whether the noisy pair differs. Write \(\kappa=(1-2\varepsilon)^2\) and \(\eta=2\varepsilon(1-\varepsilon)\). Then the observations are independent Bernoulli variables with parameter
\[
 Q_r=\eta+\frac{2\kappa r}{p}. \tag{2}
\]
For \(\varepsilon<1/2\), rounding \(p(\widehat Q-\eta)/(2\kappa)\) to the nearest allowed integer \(r\in\{1,\ldots,(p-1)/2\}\) recovers the necklace with failure probability at most
\[
 2\exp\left(-\frac{2N\kappa^2}{p^2}\right). \tag{3}
\]
Conversely, **every** procedure that uses only these \(N\) noisy adjacent-disagreement observations and has error at most \(\delta<1/4\) for every necklace must have
\[
 N\ \ge\ \frac{3p^2}{64\kappa^2}\log\frac{1}{4\delta}. \tag{4}
\]
Thus this observation model has minimax sample complexity of order \(p^2(1-2\varepsilon)^{-4}\log(1/\delta)\), up to absolute factors. At \(\varepsilon=1/2\), all distributions coincide, making recovery impossible.

## Assumptions and scope

All words are *cyclic* length-\(p\) sequences; index rotations are identified, but reversal of time is not regarded as an additional symmetry. The coprimality assumption makes the rotational orbit primitive. The observations in (2)–(4) are independent *phase-resampled experiments*, not successive overlapping observations from one trajectory. The probability of independent label flips is known, and only the noisy disagreement bit is retained. There is no claim of equivalent recovery rates for one continuously sampled orbit, unknown noise level, or arbitrary symbolic dynamics.

The object is precisely the rotational switching itinerary defined by Simpson (2023), Definition 3.3. That source proves such itineraries for periodic orbits on degree-one invariant circles meeting a switching manifold twice. Nothing here asserts that every parameter triple occurs in an arbitrary fixed piecewise-linear map.

## Proof

**1. Circular overlap identity.** Write \(I=\{0,1,\ldots,\ell-1\}\subset\mathbb Z/p\mathbb Z\), and define the time-lag correlation
\[
 C_m(t)=\sum_{i=0}^{p-1}w_iw_{i+t}.
\]
As multiplication by \(m\) permutes the residues, with \(s=tm\bmod p\) chosen in \(\{0,\ldots,p-1\}\), the size of \(I\cap(I-s)\) is
\[
 C_m(t)=g_\ell(s):=\max(\ell-s,0)+\max(\ell-(p-s),0). \tag{5}
\]
The two terms count nonwrapping and wrapping intersections; they are disjoint because \(\ell<p\). In particular \(C_m(0)=\ell\). Since each \(w_i\) is binary, the cyclic switch count is
\[
 T=\sum_i(w_i-w_{i+1})^2=2\ell-2C_m(1).
\]
Direct inspection of (5), distinguishing \(s\le\ell\), \(s\ge p-\ell\), and the central region, yields
\[
 \ell-g_\ell(s)=\min\{s,p-s,\ell,p-\ell\}.
\]
Substitute \(s=m\) and divide by two to establish (1).

**2. Exact cyclic identification.** Because \(2\le\ell\le p-2\), equation (5) gives \(g_\ell(1)=g_\ell(p-1)=\ell-1\), while for every \(s\in\{2,\ldots,p-2\}\), \(g_\ell(s)\le\ell-2\): if just one interval-overlap term is positive it is at most \(\ell-2\), and if both are positive their sum is \(2\ell-p\le\ell-2\). Consequently, for nonzero time lags, the two and only two maximizers of \(C_m(t)\) are
\[
 t\equiv m^{-1}\quad\hbox{or}\quad t\equiv-m^{-1}\pmod p. \tag{6}
\]
Cyclic index rotation does not change \(C_m\). If two words have the same necklace, (6) forces \(m'\equiv \pm m\pmod p\). Conversely, replacement of \(m\) by \(-m\) sends the occupied residue interval \(I\) to \(-I=I-(\ell-1)\); multiplication by \(m^{-1}\) transfers this residue translation to an index translation. Thus \(w(\ell,m,p)\) and \(w(\ell,p-m,p)\) are cyclic shifts. Their full period is \(p\), since any nontrivial index period \(t\) would give \(C_m(t)=C_m(0)=\ell\), impossible by (5). Therefore there are exactly \(\varphi(p)/2\) necklaces, parameterized by admissible \(r\).

For odd prime \(p\), every integer \(1\le r\le(p-1)/2\) is admissible. Equation (1) is strictly increasing until \(r=L\) and remains constant thereafter. The number of saturated parameters is \((p+1)/2-L\); it equals one exactly for the two balanced occupancies. This proves the sharp deterministic identification threshold and ambiguity count. For general composite \(p\), the saturated count is exactly \(\#\{r\in[L,\lfloor p/2\rfloor]:\gcd(r,p)=1\}\).

**3. Observation channel and upper bound.** Let \(D=\mathbf1_{\{w_i\ne w_{i+1}\}}\), so uniformly random \(i\) gives \(\Pr(D=1)=T/p=2r/p\) in the balanced, prime case. Independently flipping the two bits reverses their parity with probability \(\eta=2\varepsilon(1-\varepsilon)\), so the final disagreement bit has probability \(\eta+(1-2\eta)\Pr(D=1)\). The identity \(1-2\eta=\kappa\) proves (2). Independent fresh phases and fresh flips make the trials independent. If nearest-integer rounding is wrong, \(|\widehat Q-Q_r|\ge\kappa/p\), because neighboring parameters in (2) are separated by \(2\kappa/p\). Hoeffding's Bernoulli concentration inequality gives (3), including clipped endpoint rounding.

**4. Information-theoretic lower bound.** Choose \(r_0=\lfloor p/4\rfloor\) and \(r_1=r_0+1\). For every odd prime \(p\ge7\), both are admissible and their Bernoulli parameters differ by \(\Delta=2\kappa/p\). The parameter \(Q_{r_1}\) belongs to \([1/4,3/4]\), as it is the convex combination of \(2r_1/p\in[1/4,3/4]\) and \(1/2\). The elementary bound \(D_{\rm KL}(\operatorname{Ber}(u)\|\operatorname{Ber}(v))\le(u-v)^2/[v(1-v)]\), obtained from \(\log z\le z-1\), therefore gives
\[
 D_{\rm KL}(\operatorname{Ber}(Q_{r_0})\|\operatorname{Ber}(Q_{r_1}))\le \frac{64\kappa^2}{3p^2}. \tag{7}
\]
For any two distributions \(P,Q\), let \(H=\sum_x\sqrt{P(x)Q(x)}\). Jensen's inequality gives \(H\ge\exp[-D_{\rm KL}(P\|Q)/2]\). By Cauchy–Schwarz, \(\|P-Q\|_{\rm TV}\le\sqrt{1-H^2}\), and hence the maximal error probability in testing the two laws is at least \((1-\|P-Q\|_{\rm TV})/2\ge H^2/4\ge\exp[-D_{\rm KL}(P\|Q)]/4\). The divergence for \(N\) independent samples is \(N\) times (7). A uniform error upper bound \(\delta\) implies (4). In addition, Pinsker's inequality and the same pair of hypotheses give \(\|P^N-Q^N\|_{\rm TV}\le\sqrt{ND_{\rm KL}(P\|Q)/2}\). Since a maximal testing error of at most \(\delta\) requires \(\|P^N-Q^N\|_{\rm TV}\ge1-2\delta\), we also have \(N\ge 3p^2(1-2\delta)^2/(32\kappa^2)\). Together, this and (4) establish the stated minimax order uniformly for \(0<\delta<1/4\). When \(\kappa=0\), equation (2) is independent of \(r\), proving the impossibility assertion.

## Verification

`check.py` (Python 3.10+, standard library only) exhaustively checks the switch formula for all \(5\le p<90\), every occupancy \(2\le\ell\le p-2\), and every coprime multiplier \(m\). It checks circular-correlation maxima and necklace classes for \(5\le p<34\), and checks the exact rational noise channel on selected prime orders and rational noise parameters. The checker outputs three PASS counts and uses no numerical tolerance. These are finite corroborations, not substitutes for Steps 1–4, which cover all stated parameters.

## Relationship to prior work

Simpson (2023), especially Definition 3.3 and Theorem 3.4, supplies the rotational words and their dynamical provenance, and proves border-collision statements rather than the present switch-statistic inverse problem. Frid and Jamet (2013) enumerate binary rotation words broadly; their enumerations do not imply the exact quotient-class fibers of one adjacent-switch statistic at fixed occupancy or the noisy-observation minimax bounds. Berstel and Vuillon (2001) recode rotations with Sturmian words but do not determine this inverse statistical threshold. The interval-overlap and concentration methods used in the proof are standard; the contribution claimed is their sharp joint application to the restricted dynamical family and observation experiment, not novelty of those elementary tools.

## Limitations

The inversion recovers \(m\) only up to reflection \(m\leftrightarrow p-m\); this is mathematically unavoidable because these multipliers describe the same cyclic word. Observing just neighboring disagreement does not identify phase, nor does it distinguish saturated unbalanced parameters. No physical-noise model for a fixed piecewise-linear system is asserted. The sample-complexity result requires independent uniform phase resampling, known independent bit-flip noise, odd prime period, and balanced occupancy. Publication priority cannot be certified from a bounded literature search; older equivalent rotation-word identities, especially in non-indexed symbolic dynamics literature, remain possible.

## References

1. D. J. W. Simpson, *The necessity of the sausage-string structure for mode-locking regions of piecewise-linear maps*, arXiv:2312.03887v1, first posted 2023-12-06; Definition 3.3, Lemma 3.1, Theorem 3.4. https://arxiv.org/abs/2312.03887
2. A. E. Frid and D. Jamet, *The number of binary rotation words*, arXiv:1302.3722, first posted 2013-02-15. https://arxiv.org/abs/1302.3722
3. J. Berstel and L. Vuillon, *Coding rotations on intervals*, arXiv:math/0106217, first posted 2001-06-26. https://arxiv.org/abs/math/0106217
4. W. Hoeffding, *Probability inequalities for sums of bounded random variables*, Journal of the American Statistical Association 58 (1963), 13–30. The concentration inequality is used as a standard lemma, not claimed as a new result.
