# Optimal alternating Markov-hole escape in integer expanding maps

## Finding

Let \(b\ge 2\) be an integer and let \(T_b(x)=bx\bmod 1\) act on \([0,1)\). At each of \(n\) successive times choose one of the two holes of equal Lebesgue measure \(b^{-2}\):
\[
H_0=[0,b^{-2}),\qquad H_1=[1-b^{-2},1).
\]
The choice sequence \(w=(w_0,\ldots,w_{n-1})\in\{0,1\}^{n}\) is fixed in advance. Define its survival probability for Lebesgue-uniform initial position by
\[
S_{b,n}(w)=\operatorname{Leb}\{x\in[0,1):T_b^k(x)\notin H_{w_k}\text{ for }0\le k<n\}.
\]
Set \(A_0=b\), \(A_1=b^2-1\), and \(A_{n+2}=bA_{n+1}-A_n\) for all \(n\ge0\). Then
\[
\boxed{\min_{w\in\{0,1\}^n}S_{b,n}(w)=\frac{A_n}{b^{n+1}}.}
\]
For every \(n\ge2\), the **only** minimizing choice sequences are the two strictly alternating sequences \(0101\cdots\) and \(1010\cdots\). At \(n=1\) both singleton choices minimize; at \(n=0\) the empty choice is the only one.

For \(b=2\) the exact optimum is \(A_n=n+2\) and hence \(\min S_{2,n}(w)=(n+2)/2^{n+1}\). For \(b\ge3\), putting
\[
r_b=\frac{b+\sqrt{b^2-4}}{2},
\]
one has the exact closed form
\[
A_n=\frac{r_b^{n+2}-r_b^{-(n+2)}}{r_b-r_b^{-1}}.
\]
Thus the sharp maximum achievable exponential escape rate over all infinite, predetermined binary choice sequences is
\[
\boxed{\rho_b=\log(b/r_b)}
\]
with the \(b=2\) convention \(r_2=1\). Alternation attains this rate. For the fixed-hole strategy, the survivor growth exponent is
\[
s_b=\frac{b-1+\sqrt{(b-1)(b+3)}}{2}>r_b,
\]
so the optimal switching strategy has strictly faster exponential escape than keeping either single hole open. The optimal count also coincides, for all times, with the count for a **static non-overlapping** length-two hole coded by the cross-pair \(0(b-1)\). That cross-pair is a different hole, unavailable in the two-endpoint choice menu.

## Assumptions and scope

All probabilities use Lebesgue measure, the deterministic map \(T_b\), and a non-adaptive schedule chosen before the initial point. The two holes represent the length-two base-\(b\) digit cylinders \(00\) and \((b-1)(b-1)\). Base-\(b\) expansion ambiguities occur only at countably many endpoints and do not affect Lebesgue measure. The minimization is over all \(2^n\) choice sequences, with no periodicity or statistical restrictions. The maximal exponential rate uses \(\limsup_{n\to\infty}-n^{-1}\log S_{b,n}(w_{[0,n)})\); the universal finite-horizon lower bound ensures no deterministic infinite schedule can exceed \(\rho_b\). This statement does **not** claim that alternation is the only infinite schedule attaining that exponent.

## Proof

**Exact symbolic count.** Fix \(b\ge2\). Let \(v_j\) count surviving digit words of the current length ending in digit \(j\in\{0,\dots,b-1\}\), with initial length one and \(v_j=1\). Write \(V=\sum_jv_j\). Opening hole \(H_0\) at the current time forbids an adjacent pair of zero digits; opening \(H_1\) forbids an adjacent pair of final digits. In general, for choice \(c\in\{0,1\}\), let \(j_c=(b-1)c\). The new vector has components
\[
(A_cv)_j=\begin{cases}V-v_{j_c},&j=j_c,\\V,&j\ne j_c.\end{cases}
\]
After \(n\) restrictions, \(V\) is exactly the number of admissible words of length \(n+1\). Each corresponding digit cylinder has measure \(b^{-(n+1)}\), proving \(S_{b,n}(w)=V/b^{n+1}\).

**Global greedy comparison, including all future choices.** Let \(J\) swap the extreme digits \(0\) and \(b-1\) while fixing all other coordinates. Define \(F_r(v)\) as the minimum final total \(\sum_jv_j\) after any \(r\)-step continuation from an arbitrary nonnegative vector \(v\). Each \(A_c\) has nonnegative entries and no zero column; consequently, every linear functional \(v\mapsto\mathbf1^{\mathsf T}A_{c_r}\cdots A_{c_1}v\) has strictly positive coefficients. Its minimum over finitely many continuations is strictly increasing under a coordinatewise nonnegative, nonzero increment. Also \(F_r(Jv)=F_r(v)\), because \(JA_0J=A_1\).

If \(v_0\ge v_{b-1}\), then \(A_0v\le JA_1v\) coordinatewise, with strict inequality in the zeroth coordinate when \(v_0>v_{b-1}\); all other coordinates agree. Thus for every \(r\ge0\),
\[
F_r(A_0v)\le F_r(JA_1v)=F_r(A_1v),
\]
and the inequality is strict when \(v_0>v_{b-1}\). By symmetry, when \(v_{b-1}>v_0\), choosing hole \(H_1\) is uniquely optimal regardless of how many future choices remain. In words, always exclude a self-transition at the endpoint with the larger current count.

Initially both endpoint counts equal one, so either first choice is optimal. After excluding endpoint \(j_c\), its new count is \(V-v_{j_c}\), while the opposite endpoint has new count \(V\). Every count along the process is positive, hence the opposite endpoint is the strictly larger one. Induction forces strictly alternating choices after the first step. This proves the claimed optimality and uniqueness for every \(n\ge2\), without relying on finite enumeration.

**Recurrence and closed form.** Let \(A_n\) be the total count on an alternating schedule after \(n\) restrictions. At the first restriction, \(A_1=b^2-1\). From the second restriction onward, the chosen endpoint was not restricted at the preceding step, so its current count equals the preceding total \(A_{n-1}\). Consequently,
\[
A_{n+1}=bA_n-A_{n-1}\qquad(n\ge1).
\]
The characteristic equation is \(r^2-br+1=0\). For \(b>2\), its distinct roots are \(r_b\) and \(r_b^{-1}\), yielding the displayed closed form; for \(b=2\) the double root one gives \(A_n=n+2\).

**Comparison with a fixed hole.** If the same endpoint is excluded at every step, let \(B_n\) be the admissible count after \(n\) restrictions. The count-vector update, or the standard one-symbol self-transition recurrence, gives \(B_0=b\), \(B_1=b^2-1\) and
\[
B_{n+2}=(b-1)(B_{n+1}+B_n).
\]
Its larger characteristic root is \(s_b\) as displayed. Since \(r_b^2=br_b-1\), evaluation of the fixed-hole polynomial at \(r_b\) gives
\[
r_b^2-(b-1)r_b-(b-1)=r_b-b<0.
\]
The polynomial has exactly one positive root, so \(s_b>r_b\). In particular the alternating schedule improves the exponential escape rate strictly at every integer base.

**Equivalence of counts with a non-overlapping fixed cylinder.** For the static hole consisting of the single cylinder \(0(b-1)\), the forbidden two-letter word has distinct first and last digits. The number of allowed digit words starts at \(b\) and \(b^2-1\). After each restriction, the number of words ending in digit \(0\) is the preceding total, because only an appended final digit \(b-1\) is restricted. Thus the total satisfies the same recurrence \(A_{n+1}=bA_n-A_{n-1}\). Hence the static cross-pair hole and the optimally switched endpoint self-pair holes have identical survival probabilities for every horizon. This count equivalence is a classical no-self-overlap enumeration, not an independent novelty assertion.

## Verification

The standalone file `checker.py` performs independent direct enumeration of admissible digit words for bases \(2\) through \(4\), exhaustive comparison of all binary schedules through eleven restrictions for bases \(2\) through \(8\), and longer exact recurrence and fixed-hole comparisons. It passed 2,174 finite assertions. These checks are corroborations only; the global minimization and infinite-horizon rates follow from the proof above.

To reproduce: run `python checker.py` with Python 3.9 or newer. No third-party Python packages, randomness, or external data are needed.

## Relationship to prior work

Atnip--Froyland--González-Tokman--Vaienti develop random open-interval-map thermodynamic formalism and pressure-based escape rates, including random expanding-map examples. That framework motivates the present explicit finite-horizon optimization, but does not supply the all-schedule greedy comparison or the exact Chebyshev count. Livorati--Georgiou--Dettmann--Leonel study periodically moving and breathing holes in the doubling map, using Ulam approximations and orbit overlap, rather than discrete arbitrary-choice endpoint cylinders. Cheriyath--Agarwal analyze time-independent unions of forbidden cylinders and their correlation-polynomial escape rates; the classical static no-overlap formula already implies the present recurrence for a **different**, cross-pair hole, but not minimization among switched endpoint holes. Bolding--Bunimovich compare first-hitting curves of **fixed** equal-size Markov holes and outline an escape-accelerating switching prescription in section 2. Their prescribed menu includes other partition cells, including the cross-pair type unavailable here; their fixed-hole hitting comparisons do not prove the exact all-schedule optimization for the restricted pair of self-loop cylinders, nor the uniqueness of its two minimizing-survival schedules. Bahsoun--Schmeling--Vaienti study annealed random holes and conditionally stationary measures, not deterministic optimal scheduling.

The new mathematical assertion is the strict, simultaneous optimality of alternating endpoint holes for **every finite horizon and integer base**, together with the observation that it realizes the performance of an otherwise unavailable static, non-overlapping cross-pair hole. The basic digit coding, the classical static cross-pair recurrence, transfer matrices, and characteristic-root method are standard and are not claimed as discoveries.

## Limitations

Only two symmetric length-two endpoint holes are allowed; this is not an optimizer theorem over all locations or hole lengths. The initial distribution is Lebesgue, and hole choices cannot depend on the hidden initial position. The theorem is exact at finite times but does not classify every aperiodic schedule with the same asymptotic exponent. Its originality assessment is based on inspected accessible sources and indexed search, not a proof of absence from every unpublished or unindexed source. Independent mathematical audit is outstanding.

## References

1. J. Atnip, G. Froyland, C. González-Tokman, S. Vaienti, *Thermodynamic Formalism for Random Interval Maps with Holes*, arXiv:2103.04712, first preprint 2021-03-08, https://arxiv.org/abs/2103.04712 . Sections 4, 13, 14, 15.
2. A. L. P. Livorati, O. Georgiou, C. P. Dettmann, E. D. Leonel, *Escape through a time-dependent hole in the doubling map*, arXiv:1312.7030, https://arxiv.org/abs/1312.7030 . Sections II--IV.
3. H. Cheriyath, N. Agarwal, *Subshifts of Finite Type with a Hole*, arXiv:1905.11767, https://arxiv.org/abs/1905.11767 . Sections 2--6.
4. W. Bahsoun, J. Schmeling, S. Vaienti, *On Transfer Operators and Maps with Random Holes*, arXiv:1405.0361, https://arxiv.org/abs/1405.0361 . Sections 1, 4.
5. M. Bolding, L. A. Bunimovich, *Where and When Orbits of Strongly Chaotic Systems Prefer to Go*, arXiv:1707.04231, https://arxiv.org/abs/1707.04231 . Sections 1-3, especially the section 2 switching prescription.
