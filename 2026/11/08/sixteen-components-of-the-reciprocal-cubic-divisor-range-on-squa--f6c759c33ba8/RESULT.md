# Sixteen components of the reciprocal-cubic divisor range on squarefree integers

## Finding

Let \(\mathcal S\) be the set of positive squarefree integers and define \(\sigma_{-3}(n)=\sum_{d\mid n}d^{-3}\). Put \(Q=\{2,3,5,7\}\),
\[
 C_S=\prod_{p\in S}(1+p^{-3})\quad(S\subseteq Q),\qquad
 U=\prod_{p\ge 11}(1+p^{-3})=\frac{\zeta(3)}{\zeta(6)\prod_{p\in Q}(1+p^{-3})}.
\]
Then the exact topological closure of the squarefree range is
\[
 \boxed{\overline{\{\sigma_{-3}(n):n\in\mathcal S\}}
       =\bigcup_{S\subseteq Q}[C_S,UC_S].}
\]
The sixteen intervals on the right are nonempty and pairwise disjoint. Consequently the closure has **exactly sixteen connected components and fifteen bounded complementary gaps** within its convex hull. This is an exact answer at \(k=1\), \(r=3\) to the component-count problem for divisor-function ranges restricted by maximum prime exponent.

## Assumptions and scope

All primes are ordinary positive rational primes, and the empty product equals one. The closure is taken in the real line, and the input variable ranges over **all** squarefree positive integers, including one. An endpoint may be a limit rather than the value of a finite input. No statement is made about nonsquarefree input integers or exponents other than three. The identity \(\prod_p(1+p^{-3})=\zeta(3)/\zeta(6)\) follows by absolutely convergent Euler products.

## Proof

**1. Tail reduction.** For squarefree \(n\), multiplicativity gives \(\sigma_{-3}(n)=\prod_{p\mid n}(1+p^{-3})\). Set \(a_p=\log(1+p^{-3})\), so \(\sum_pa_p<\infty\). For a sequence of positive summable weights \(a_j\) with \(a_j\le\sum_{i>j}a_i\) at every index, the set of all infinite subsums is the full interval \([0,\sum_ja_j]\). Indeed, to express a target \(t\) in that interval, at each index take the weight if the remaining target exceeds the subsequent total; otherwise omit it. The inequality ensures that the remainder lies in the subsequent interval, and the remaining tails tend to zero. Finite subsums are dense in the infinite subsums, so exponentiating this assertion yields the full interval of tail products.

**2. Five exact finite tail checks.** For each \(p\in\{11,13,17,19,23\}\), let \(q_1,\ldots,q_5\) denote the following five primes. In order these lists are
\[
\begin{array}{c|c}
 11&(13,17,19,23,29)\\
 13&(17,19,23,29,31)\\
 17&(19,23,29,31,37)\\
 19&(23,29,31,37,41)\\
 23&(29,31,37,41,43)
\end{array}
\]
Exact rational multiplication verifies
\[
 1+p^{-3}<\prod_{j=1}^5(1+q_j^{-3}).
\]
Taking logarithms and including the remaining positive terms proves \(a_p<\sum_{q>p}a_q\) for these five primes. The accompanying reproducibility program performs every comparison as a rational-integer equality/inequality, not a floating-point test.

**3. Infinite tail inequality.** Nagura's classical prime interval theorem says that every integer \(x\ge25\) admits a prime strictly between \(x\) and \(6x/5\). For every prime \(p\ge29\), the \(j\)-th following prime therefore satisfies \(q_j<(6/5)^jp\). Let \(t=p^{-3}\) and \(h=(5/6)^3=125/216\). Since \(\log(1+z)\ge z-z^2/2\) for \(z\ge0\),
\[
 \sum_{q>p}a_q \ge \sum_{j\ge1}\log(1+t h^j)
 \ge t\frac{h}{1-h}-\frac{t^2}{2}\frac{h^2}{1-h^2}.
\]
Because \(0<t\le29^{-3}\), the latter is strictly larger than \(t\) by the exact inequality
\[
 \frac{h}{1-h}-\frac{1}{2\cdot29^3}\frac{h^2}{1-h^2}
 =\frac{2079146625}{1513630118}>1.
\]
Since \(\log(1+t)<t\), the requisite inequality \(a_p<\sum_{q>p}a_q\) holds for every \(p\ge29\) as well. Steps 1–3 show that the closure of products over primes \(p\ge11\) is exactly \([1,U]\).

**4. Exact separation of the sixteen head intervals.** All other squarefree factors are uniquely assigned to the finite head \(Q\), so the first displayed union is exact. It remains to prove the sixteen intervals are separate. Enumerating the rational \(C_S\), the strict ascending order of subset masks (bit positions corresponding in order to \(2,3,5,7\)) is
\[
 0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15.
\]
A finite exact-rational comparison of the 15 consecutive quotients gives
\[
 \min_{i=1}^{15}\frac{C_{i+1}}{C_i}=\frac{344}{343}.
\]
On the other hand, using that all primes \(\ge31\) are odd,
\[
\begin{aligned}
 \log U&\le \sum_{p\ge11}p^{-3}\\
 &\le\sum_{p\in\{11,13,17,19,23,29\}}p^{-3}
       +31^{-3}+\frac{1}{4\cdot31^2}\\
 &=\frac{6873910901010396038995101}{3484482229214561906464984708}
 <\frac1{500}.
\end{aligned}
\]
Here the last term bounds \(\sum_{j\ge0}(31+2j)^{-3}\) by its first term and the integral of the decreasing function \((31+2t)^{-3}\) over \([0,\infty)\). The elementary estimate \(e^x\le(1-x)^{-1}\) for \(0\le x<1\) yields
\[
 1<U<e^{1/500}\le\frac{500}{499}<\frac{344}{343}.
\]
Thus \(UC_i<C_{i+1}\) for every consecutive head coefficient. The union comprises sixteen pairwise disjoint closed intervals, completing the proof.

## Verification

The standalone `verify.py` (Python standard library only) checks the five finite-prime inequalities, the exact infinite-tail coefficient bound, the rational upper bound for \(\log U\), all sixteen coefficients, their total ordering, and the minimum consecutive coefficient ratio. Running `python3 verify.py` prints `VERIFY_OK`. These finite checks verify the arithmetic certificates in Steps 2–4; the infinite prime-tail conclusion relies on Nagura's published prime-interval theorem and the stated analytic argument, rather than experimental enumeration.

## Relationship to prior work

Defant's 2015 work introduces the restricted divisor function \(\sigma_{-r,k}\) and explicitly asks which parameter values produce a specified finite number of closure intervals. Its density criterion determines connectedness thresholds, not the component count for this particular nondense squarefree case. Defant's work on unitary divisor functions treats all positive integer inputs with unitary prime-power factors, a genuinely larger domain than squarefree integers. Other work on the **unrestricted** \(\sigma_{-r}\) range supplies bounds or counts for a different input domain. The formula here determines the exact restricted \(k=1\), \(r=3\) component count; the elementary tail-subsum framework and Nagura theorem are prior tools, not claimed as inventions.

## Limitations

The result does not describe the closure for all ordinary integers, nor give the full component-count function as the real exponent varies. The number sixteen is mathematically proved for the stated one parameter choice; it is not an exhaustive resolution of the entire parameter-classification problem. Searches of accessible sources cannot exclude an unindexed earlier equivalent classification. No independent external validation has been performed.

## References

1. Colin Defant, *On the Density of Ranges of Generalized Divisor Functions with Restricted Domains*, arXiv:1507.02663 (first public 2015-07-09), https://arxiv.org/abs/1507.02663.
2. Colin Defant, *On the Density of Ranges of Generalized Divisor Functions*, arXiv:1506.05432 (2015), https://arxiv.org/abs/1506.05432.
3. Colin Defant, *Ranges of Unitary Divisor Functions*, arXiv:1507.02654 (2015), https://arxiv.org/abs/1507.02654.
4. Jitsuro Nagura, *On the Interval Containing At Least One Prime Number*, Proc. Japan Acad. 28 (1952), 177–181, DOI:10.3792/pja/1195570997.
5. Nina Zubrilina, *On the Number of Connected Components of the Ranges of Divisor Functions*, arXiv:1711.02871 (2017), https://arxiv.org/abs/1711.02871.
6. Aarav Achenjang and Jonathan Berger, *The Number of Connected Components of the Ranges of Divisor Functions*, arXiv:1808.07550 (2018), https://arxiv.org/abs/1808.07550.
