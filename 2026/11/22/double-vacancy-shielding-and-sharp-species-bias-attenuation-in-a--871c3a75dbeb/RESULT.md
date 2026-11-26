# Double-vacancy shielding and sharp species-bias attenuation in antagonistic adsorption

## Finding

In irreversible one-attempt, two-species antagonistic adsorption on the integer line, **two consecutive terminal vacancies are an exact probabilistic separator**: conditional on sites \(0\) and \(1\) both remaining vacant, the entire terminal configurations on \(\{\ldots,-2,-1\}\) and \(\{2,3,\ldots\}\) are independent. In particular, the species immediately flanking such a gap are conditionally independent. Their conditional law exhibits a *sharp universal fivefold attenuation* of the original deposition color bias.

Let \(p\in(0,1)\) be the proposal probability of species \(A\), let \(q=1-p\), and write \(\gamma=\sqrt{pq}\), \(S=\sinh\gamma/\gamma\), and \(C=\cosh\gamma\). Define
\[
 w_A=q\left[1-S+\frac{p}{\gamma^2}(C-1)\right],\quad
 w_B=p\left[1-S+\frac{q}{\gamma^2}(C-1)\right],\quad
 W=w_A+w_B=2C-1-S.
\]
Then \(W>0\). With \(E=\{\eta_0=\eta_1=\varnothing\}\) for the frozen terminal state, for every \(i,j\in\{A,B\}\),
\[
 \Pr(E,\eta_{-1}=i,\eta_2=j)=w_iw_j,
 \qquad \Pr(E)=W^2.
\]
Thus the left and right flanking colors are independent given \(E\), with \(\pi_A=w_A/W\) and \(\pi_B=w_B/W\). More sharply,
\[
 \boxed{\pi_A-\pi_B=(p-q)\,\kappa(p),\qquad
 \kappa(p)=\frac{\sinh\gamma/\gamma-1}{2\cosh\gamma-1-\sinh\gamma/\gamma},\qquad
 0<\kappa(p)<\frac15.}
\]
The bound is **sharp** as \(p\downarrow0\) or \(p\uparrow1\): \(\kappa(p)\to1/5\). For \(p\ne 1/2\), the absolute species imbalance among particles flanking an observed double-vacancy gap is strictly less than one fifth of the absolute proposal imbalance. At \(p=1/2\), both imbalances are zero. As \(p\uparrow1\), the conditional flank distribution tends to \((\pi_A,\pi_B)=(3/5,2/5)\), even though \(A\)-proposals become overwhelming. At the balanced point, \(\Pr(E)=(2\cosh(1/2)-1-2\sinh(1/2))^2\approx0.045395125835236\), and the joint probability of \(E\) with each flanking-color pair is \(\Pr(E)/4\).

The two-site cut is nontrivial: a *single* terminal vacancy is not an independence separator even when \(p=q=1/2\). For the occupancy indicators of species \(A\) at sites \(-1\) and \(1\), their covariance conditioned on a vacancy at \(0\) equals approximately \(-0.0433870456804\), which is strictly nonzero. An exact expression is given in the proof.

## Assumptions and scope

At every site \(i\in\mathbb Z\), independently select an arrival time \(U_i\sim\operatorname{Uniform}[0,1]\) and a proposed species \(Y_i\in\{A,B\}\) with \(\Pr(Y_i=A)=p\). Initially every site is empty. At its single arrival time the site accepts its proposal if neither adjacent site is already occupied by the *opposite* species. Occupied particles are permanent; rejected proposals are never retried. Write \(\eta_i\in\{A,B,\varnothing\}\) for the terminal state after all attempts. Opposite species cannot occupy neighboring sites; same-species neighbors can.

The infinite process exists almost surely: the status of a fixed site is determined by a finite random ancestor set. A dependency extending along a specified nearest-neighbor chain of length \(m\) requires strictly decreasing independent arrival times, of probability \(1/(m+1)!\). The union of at most \(2^m\) possible paths yields a summable bound. All events below are consequently well defined as finite-path limits. The cut is a conditional *distributional* statement about terminal configurations, not a claim that their unconditioned halves are independent or that arbitrary transient vacant pairs are separators.

## Proof

**1. One-sided occupation law.** Run the process independently on \(\{\ldots,-2,-1\}\) with site \(0\) held vacant, and let \(a(u)\) and \(b(u)\) be the probabilities the rightmost site has accepted species \(A\) or \(B\) by time \(u\). An endpoint \(A\)-proposal at time \(u\) succeeds exactly when its sole neighbor has not previously accepted \(B\). Before that endpoint proposal, the neighbor's backward half-line evolves as an independent copy of the same one-sided process. Thus
\[
 a'(u)=p[1-b(u)],\qquad b'(u)=q[1-a(u)],\qquad a(0)=b(0)=0.
\]
Writing \(\gamma=\sqrt{pq}\), the unique solution is
\[
 a(u)=1-\cosh(\gamma u)+\frac p\gamma\sinh(\gamma u),\quad
 b(u)=1-\cosh(\gamma u)+\frac q\gamma\sinh(\gamma u).
\]
These are probabilities, hence nonnegative, and both are strictly positive for \(0<u\le1\) and \(0<p<1\).

**2. Exact decomposition of a double vacancy.** Independently run the left-half-line process on sites \(i\le-1\), the right-half-line process on sites \(i\ge2\), and draw the separate marks \((U_0,Y_0)\) and \((U_1,Y_1)\). Let \(E_L\) be the event that the isolated left endpoint \(-1\) has accepted a species opposite to \(Y_0\) *before* time \(U_0\). Let \(E_R\) be the analogous event that isolated right endpoint \(2\) has accepted a species opposite to \(Y_1\) before \(U_1\). The events use disjoint independent marks.

Crucially, the **full-line** event \(E\) is exactly \(E_L\cap E_R\). If both hold, whichever of sites \(0\) or \(1\) attempts first is blocked by its already-occupied exterior neighbor; the second is blocked in the same way. The exteriors therefore evolve exactly as their isolated half-line counterparts. Conversely, if both sites end empty, each must have been rejected at its unique attempt; since its other interior neighbor is also never occupied, only its own exterior neighbor can have rejected it. That exterior site had already been occupied and evolved independently of the never-accepted central pair. Thus both isolated conditions are necessary. On \(E\), the actual left and right terminal half-line configurations coincide with the isolated ones.

It follows from the independent-mark factorization of \(E_L\) and \(E_R\) that, for **arbitrary** measurable events \(L\) depending only on terminal sites \(i\le-1\) and \(R\) depending only on terminal sites \(i\ge2\),
\[
 \Pr(L\cap R\mid E)=\Pr(L\mid E)\Pr(R\mid E).
\]
This proves the full conditional half-line independence, not merely its flanking-color projection.

**3. Exact flanking law.** The probability of \(E_L\) with the endpoint species equal to \(A\) is \(q\int_0^1a(u)\,du=w_A\), because the failed proposal at \(0\) must be \(B\). Similarly it is \(p\int_0^1b(u)\,du=w_B\) when the endpoint species is \(B\). Integrating the solutions in Step 1 gives the displayed formulas for \(w_A,w_B\). Both half-line events have total probability \(W=w_A+w_B\), proving \(\Pr(E)=W^2\), all four joint color probabilities, and the conditional independence assertions.

**4. Sharp attenuation.** Direct subtraction yields
\[
 w_A-w_B=(p-q)(S-1),\quad w_A+w_B=2C-1-S,
\]
so the conditional color contrast is \((p-q)\kappa(p)\). Positivity follows because \(S>1\) when \(\gamma>0\) and \(W>0\) by Step 3. To prove strict upper bound, use the absolutely convergent Taylor series
\[
 W-5(S-1)=2(C+2-3S)
 =2\sum_{n=2}^{\infty}\frac{\gamma^{2n}}{(2n)!}\left(1-\frac{3}{2n+1}\right)>0.
\]
Therefore \(0<\kappa(p)<1/5\). As \(\gamma\downarrow0\), the numerator \(S-1=\gamma^2/6+O(\gamma^4)\), while \(W=5\gamma^2/6+O(\gamma^4)\); their ratio tends to \(1/5\). This is attained as a limit when one species becomes rare, proving sharpness and the stated \(3/5,2/5\) boundary law.

**5. A single vacancy does not separate.** For \(p=q=1/2\), put \(z=e^{-1/2}\). The established single-species block and distance-two formulas, or their direct one-sided integrals, give
\[
 \Pr(\eta_0=\varnothing)=z^2,\quad
 \Pr(\eta_{-1}=A,\eta_0=\varnothing)=\frac{1-z^2}{2}-(1-z)^2,
\]
\[
 \Pr(\eta_{-1}=A,\eta_0=\varnothing,\eta_1=A)
 =z-\frac32z^2.
\]
Their conditional covariance is exactly
\[
 \frac{z-\tfrac32z^2}{z^2}
 -\left[\frac{\tfrac12(1-z^2)-(1-z)^2}{z^2}\right]^2
 =-0.0433870456804\ldots\ne0.
\]
It is negative, for example by substituting the rigorously bounded value \(0.6065306597<z<0.6065306598\) into this continuous rational expression. Thus one vacancy fails as a separator; two are minimal for this conditional-independence phenomenon.

## Verification

The standalone standard-library script `checker.py` exhaustively enumerates all arrival orders and all color proposals on finite paths of five, six, and seven sites for five rational proposal biases. Exact rational totals for two consecutive vacancies and each of the four flanking-color patterns agree with independent finite-half-line polynomial recurrences. More stringently, the checker enumerates **entire left and right terminal configurations** and confirms that their joint distribution given the vacancy pair has exact rank one on each tested finite path. Taylor coefficient positivity and the sharp \(1/5\) limit are separately checked, as are numerical specializations of the closed formulas. Executing `python checker.py` reports 180 passed assertions. These finite checks do not substitute for the infinite-volume factorization and Taylor-series proof.

## Relationship to prior work

Do Amaral and dos Santos [1] define exactly this one-attempt model and give its one-site color densities via a decreasing-time decomposition. Their one-sided method is an explicit antecedent of Step 1; those densities are not claimed as new. The published same-color cluster-intensity result [2] determines all maximal monochromatic-cluster length marginals. Together with single-site vacancy density and the fact that terminal vacant runs have length at most two, this **already implies the uncolored number \(\Pr(E)\)**; that isolated quantity is not offered as a novel theorem. The published second-neighbor result [3] obtains exact \(A\)-occupancy correlation at distance two and the \(A,\varnothing,A\) probability, hence also informs the single-vacancy counterexample. It does not calculate \(A,\varnothing,\varnothing,B\) or establish independent *full halves* conditioned on a double vacancy.

The assessed contribution is precisely the **full double-vacancy separation law and the sharp species-resolved bias attenuation**. Scalar one-site densities, uncolored vacancy-cluster intensities, and a distance-two same-color correlation neither specify the conditional joint law of arbitrary separated half-line configurations nor imply the sharp contrast bound. The repeated-proposal two-species setting [4] has a distinct dynamics and is not interchangeable with one-attempt adsorption. Classical single-species gap studies [5] use another deposition rule. No claim of exhaustive publication priority is made.

## Limitations

The separation law concerns the final jammed configuration, not intermediate times, and requires a one-dimensional nearest-neighbor graph, independent iid proposed colors and uniform attempt times, and **exactly one** deposition attempt per site. It does not assert independence for a single vacancy, arbitrary random gaps, two-dimensional lattices, or processes with repeated attempts. The exact \(\Pr(E)\) is included to normalize the conditional laws, but, by the implication comparison above, it is not a stand-alone novelty claim. The fivefold bound is strict for every nondegenerate bias; equality holds only as a singular bias limit where conditioning events themselves become rare.

## References

[1] C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, first public 2023-06-16, arXiv:2306.09786v1. https://arxiv.org/abs/2306.09786

[2] *Exact geometric tails for same-species clusters in one-shot antagonistic adsorption*, published 2026-11-01, https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-exact-geometric-tails-for-same-species-clusters-in-one-shot-anta--04ec1f49bc46

[3] *Exact second-neighbor correlation in one-shot antagonistic adsorption*, published 2026-11-02, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-second-neighbor-correlation-in-one-shot-antagonistic-adsor--b16701b2c768

[4] P. H. L. Martins, R. Dickman, and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, arXiv:2211.04622v1, first public 2022-11-09. https://arxiv.org/abs/2211.04622

[5] C. S. do Amaral and D. C. dos Santos, *Density and correlation in a random sequential adsorption model*, arXiv:2210.05627v1, first public 2022-10-11. https://arxiv.org/abs/2210.05627
