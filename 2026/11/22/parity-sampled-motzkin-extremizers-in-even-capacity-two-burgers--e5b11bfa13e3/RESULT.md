# Parity-sampled Motzkin extremizers in even capacity-two Burgers traffic

## Finding

Let \(n\ge4\) be even. Consider the capacity-two Burgers traffic map on an indexed cyclic ring with site occupancies \(x_i\in\{0,1,2\}\):
\[
 F(x)_i=x_i+\min(x_{i-1},2-x_i)-\min(x_i,2-x_{i+1}).
\]
Indices are modulo \(n\); total occupancy \(N=\sum_i x_i\) is conserved. Let \(\tau(x)\) be the first time the trajectory enters its eventual temporal cycle (so a periodic initial state has \(\tau=0\)). The sharp universal entry time is \(n/2-1\); the classical asymptotic traffic-phase description is credited below.

**New near-critical extremizer census.** At **each** of the two nearest-neighbour densities \(N=n-1\) and \(N=n+1\), exactly
\[
 \boxed{E_{n,n-1}=E_{n,n+1}=2nM_{n-3}}
\]
labelled initial configurations require the full \(n/2-1\) updates to become periodic. Here \(M_k\) is the Motzkin number,
\[
 M_k=\sum_{j=0}^{\lfloor k/2\rfloor}\binom{k}{2j}\frac{1}{j+1}\binom{2j}{j}.
\]
The first counts **in either density sector** for \(n=4,6,8,10,12\) are \(8,48,336,2540,20040\). Under independent uniformly chosen initial symbols conditioned on total occupancy \(n\pm1\),
\[
 \boxed{\lim_{\substack{n\to\infty\\2\mid n}}\Pr\{\tau=n/2-1\mid N=n\pm1\}=\frac29.}
\]
Thus a positive proportion of states one particle away from the critical sector remain maximally delayed as the ring grows. The combined unconditional probability of maximum-delay states **in these two specified mass sectors** is asymptotic to \(2\sqrt3/(9\sqrt{\pi n})\); this is not a claim about all density sectors.

## Assumptions and scope

Only deterministic synchronous cyclic rings of **even** size \(n\ge4\) and capacity exactly two are involved. The exact extremizer count is made at the two individual conserved masses \(n-1\) and \(n+1\); the count of maximizers at mass \(n\) is not claimed. All ring sites are labelled. Complementing each symbol by \(2-x_i\) exchanges the two masses and preserves entry time. \(M_k\) is the standard Motzkin excursion number. This is one claim: a sharp density-resolved last-entry census and its limiting conditional probability.

## Proof

**1. Flux, height, and latest update.** Define \(J_i=\min(x_i,2-x_{i+1})\). Take a quasi-periodic lift \(h\) with \(h_i-h_{i-1}=x_i-1\), and \(h_{i+n}=h_i+d\), where \(d=N-n\). The flux identity
\[
 J_i=1+h_i-\max(h_{i-1},h_{i+1})
\]
shows that the density update is induced exactly by \(h_i(t+1)=\max(h_{i-1}(t),h_{i+1}(t))-1\). Its iterates have the explicit max-plus formula
\[
 h_i(t)=\max_{0\le j\le t}h_{i-t+2j}(0)-t.
\]
Put \(W_i(t)=h_i(t)+t\). The terminal *free* language is \(L_n=\{x:x_i+x_{i+1}\le2\text{ for all }i\}\), equivalently \(W_{i+1}(t)\le W_{i-1}(t)\) for all \(i\). The congested language is \(H_n=\{x:x_i+x_{i+1}\ge2\text{ for all }i\}\). On \(L_n\) the update is one rigid right shift; on \(H_n\) one rigid left shift. Thus both are periodic, and the classical height argument shows every state reaches their union. At time \(t=n/2-1\), each max window contains all \(n/2\) points of one parity class. Shifting a window by two replaces \(h_j\) by \(h_{j+n}=h_j+d\): the maxima are nonincreasing if \(d\le0\), nondecreasing if \(d\ge0\), proving \(\tau\le n/2-1\).

**2. An exact exceptional-peak criterion at mass \(n-1\).** Write \(n=2m\ge4\), take \(d=-1\), and inspect \(t=m-2\). Each max window now contains \(m-1\) consecutive points of a parity class. Moving the window forward by two drops \(h_{k+2}\) and appends \(h_{k+n}=h_k-1\). It increases strictly at some site if and only if there exists an index \(k\) for which
\[
 \boxed{h_k\ge h_{k+2j}+2\quad\text{for every }1\le j\le m-1.}\tag{*}
\]
For \(d=-1\), the congested language is impossible by conservation, so an increase of at least one such window is exactly the condition for the state at time \(m-2\) to remain transient. Consequently, \(\tau=m-1\) if and only if there exists such an *exceptional parity peak*. All comparisons are in the quasi-periodic lift on indices \(k,k+2,\ldots,k+n-2\), with no modulo-induced loss of the drift.

There is **at most one exceptional peak per word**, not merely one per parity class. Indeed if \(k\) satisfies (*), its lifted heights at every position \(k+1,\ldots,k+n-1\) are strictly below \(h_k\): the even offsets are at most \(h_k-2\), and an odd-offset height is at most one larger than either adjacent even-offset height (both adjacent values bound the odd site, with at least one among the strict low heights). Suppose a second peak lay at \(k<\ell<k+n\). Then \(h_\ell\le h_k-1\), yet the second peak would force \(h_{k+n}<h_\ell\), because \(k+n\) lies strictly between \(\ell\) and \(\ell+n\). But \(h_{k+n}=h_k-1\ge h_\ell\), contradiction. Thus a state can be counted exactly once by marking its exceptional peak.

**3. Rooted parity-sampled Motzkin count.** Fix the unique exceptional index \(k\), write \(a_j=x_{k+j}-1\in\{-1,0,1\}\) and \(S_r=\sum_{j=1}^r a_j=h_{k+r}-h_k\). The full drift is \(S_n=-1\), while (*) says \(S_{2j}\le-2\) for \(1\le j\le m-1\). Necessarily \(a_1=a_2=-1\), and, just before the final two steps, \(S_{n-2}=-2\) or \(-3\). In the first case the final two increments sum to \(+1\) and admit two ordered choices; in the second they sum to \(+2\) and admit one choice.

Delete the first two increments, negate the remaining intermediate increments, and sample their partial sums **after each pair**. This is a nonnegative walk of \(L=m-2\) two-step units over elementary increments \(-1,0,1\), constrained to be nonnegative at even instants but allowed to visit \(-1\) at intervening odd instants. If \(T\) is the standard infinite tridiagonal Motzkin transfer on heights \(0,1,2,\ldots\) (each of horizontal, up and down steps has unit weight, but down from zero is forbidden), the paired transfer is exactly
\[
 K=T^2+e_0e_0^{\mathsf T}.
\]
The extra \(e_0e_0^{\mathsf T}\) counts the additional \(0\to-1\to0\) excursion whose intermediate height is negative. The final-step multiplicities make the number of rooted exception words
\[
 Q_L=2(K^L)_{0,0}+(K^L)_{0,1}.
\]
We now show *for all* \(L\ge0\), not merely by finite computation, that
\[
 Q_L=2M_{2L+1}.
\]
Let \(E(z)=\sum_{L\ge0}M_{2L}z^L\) and \(O(z)=\sum_{L\ge0}M_{2L+1}z^L\). The Motzkin generating function \(\mathcal M(u)=E(u^2)+uO(u^2)\) satisfies \(\mathcal M=1+u\mathcal M+u^2\mathcal M^2\). Taking the odd part gives
\[
 O=E+2zEO.\tag{1}
\]
As a formal power series, \(G=(I-zT^2)^{-1}\) has \(G_{00}=E\), and \(G_{01}=O-E\) since \(Te_0=e_0+e_1\). The rank-one resolvent identity for \(K=T^2+e_0e_0^{\mathsf T}\) then yields
\[
 \sum_{L\ge0}Q_Lz^L
 =\frac{2G_{00}+G_{01}}{1-zG_{00}}
 =\frac{E+O}{1-zE}=2O,
\]
where the last equality is precisely (1). Comparing coefficients proves the asserted identity. Multiplying by the \(n\) possible exceptional indices gives \(nQ_{m-2}=2nM_{n-3}\) mass-\(n-1\) configurations. The sitewise complement \(x_i\mapsto2-x_i\) conjugates the dynamics to spatial reflection of itself, so the same count and stopping time hold at mass \(n+1\).

**4. Conditional probability.** Motzkin excursions obey the classical asymptotic
\[
 M_k\sim\frac{3\sqrt3}{2\sqrt\pi}\frac{3^k}{k^{3/2}}.
\]
Independently, a local central limit estimate for the sum of \(n\) i.i.d. uniform \(\{0,1,2\}\) variables gives
\[
 [z^{n-1}](1+z+z^2)^n\sim\frac{\sqrt3}{2\sqrt{\pi n}}3^n.
\]
Therefore the quotient of the exact extremizer number \(2nM_{n-3}\) by the total number of initial words of mass \(n-1\) tends to \(2/9\). Complement symmetry gives the same limit at mass \(n+1\). Summing the two sector populations and dividing by \(3^n\) gives the stated unconditional contribution.

## Verification

`verify_even_motzkin.py` is a standalone Python 3 check (standard library only). It independently runs the cellular update on **every** configuration of masses \(n-1,n+1\) for even sizes \(n=4,6,8,10,12\); compares being nonrecurrent at \(t=n/2-2\) against the unique exceptional parity peak; checks the exact counts \(8,48,336,2540,20040\); and independently checks the operator identity \(Q_L=2M_{2L+1}\) for \(L=0,\ldots,17\). Further scripts `verify.py` and `verify_independent.py` exhaustively check the general height/phase clock and orbit structure through lengths ten and nine, respectively. Actual stdout appears in the corresponding `.log` files. Computation corroborates the proof; it does not establish the statements for all lengths.

Reproduce with `python3 verify_even_motzkin.py`, `python3 verify.py`, `python3 verify_independent.py`. No external datasets or third-party packages are used.

## Relationship to prior work

The capacity-two flux, max-plus reduction and eventual two traffic phases are established by Nishinari–Takahashi (1998, especially Section IV). Those facts are credited as premises. Boccara–Fukś (1999) identify the corresponding three-state local rule numbered `6171534259461`; Nishinari–Takahashi (2000) study multi-value traffic extensions. Exact binary Rule-184 Catalan extremizers concern capacity one, not the present even-ring near-critical sectors.

A distinct directed three-colour cyclic automaton has an exact \(3nM_{n-2}\) last-entry count and an underlying asymmetric-gliders particle representation. Its **odd-ring Motzkin motif** is combinatorially similar to a capacity-two Burgers critical-density walk; it must not be mistaken for the new result. The present theorem instead counts maximizers of the **half-circumference** stopping clock \(n/2-1\) at the **even-ring off-critical masses** \(n\pm1\), where the key constraint is positivity only at alternate instants. The rank-one boundary correction and parity-sampled transfer are not consequences of that prior cyclic-colour theorem. The analogous result was compared in full text, rather than only through its abstract. No source inspected states or dominates the specific \(2nM_{n-3}\) even near-critical census.

## Limitations

The complete maximizer population at exactly critical mass \(N=n\) on even rings is not classified here. The limiting probability \(2/9\) is conditional on mass \(n\pm1\), not the unconditional probability of maximum entry over all initial words. Arbitrary larger capacities, nonperiodic boundaries and nonsynchronous updates are outside scope. Prior asymptotic traffic and Motzkin-combinatorics discoveries are expressly credited. Historical priority may be affected by unindexed or less accessible work; independent mathematical validation has not been performed.

## References

1. K. Nishinari and D. Takahashi, *Analytical properties of ultradiscrete Burgers equation and rule-184 cellular automaton*, J. Phys. A **31** (1998), 5439–5450, first published 1998-06-19. DOI https://doi.org/10.1088/0305-4470/31/24/006 .
2. N. Boccara and H. Fukś, *Number-conserving cellular automaton rules*, initial preprint 1999-05-06, https://arxiv.org/abs/adap-org/9905004 .
3. K. Nishinari and D. Takahashi, *A family of multi-value cellular automaton model for traffic flow*, initial preprint 2000-02-08, https://arxiv.org/abs/nlin/0002007 .
4. *Motzkin last-entry law and winding-selected basins in a directed three-colour cyclic automaton*, available public mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-motzkin-last-entry-law-and-winding-selected-basins-in-a-directed--b672f4087fac .
5. Motzkin numbers, OEIS A001006, https://oeis.org/A001006 (sequence background, not a source for the Burgers automaton law).
