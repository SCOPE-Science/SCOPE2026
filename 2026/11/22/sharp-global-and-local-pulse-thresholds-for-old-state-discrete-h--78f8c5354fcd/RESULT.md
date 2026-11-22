# Sharp global and local pulse thresholds for old-state discrete harvesting

## Finding

**Theorem (a horizon-independent phase diagram for concentrated harvest effort).** Fix any integer \(N\ge2\), positive constants \(\tau,q,y^0,\eta,\lambda,E\), and an effort cap \(U_{\max}\ge E\). Let admissible controls \(u=(u^0,\ldots,u^{N-1})\) satisfy \(0\le u^i\le U_{\max}\) and \(\sum_i u^i=E\). Define the positive pure-removal step and old-state harvest objective by
\[
y^{i+1}=\frac{y^i}{1+\tau q u^i},\qquad
J_0(u)=\frac{\lambda\tau}{2}\sum_{i=0}^{N-1}(u^i)^2
-\eta\tau q\sum_{i=0}^{N-1}u^i y^i.
\]
Put
\[
S=\tau qE,\qquad c=\frac{\lambda}{\eta y^0\tau q^2},\qquad c_1=\frac1{1+S}.
\]
Then the **global** minimizers of \(J_0\) are exactly the \(N\) one-pulse controls \(E e_k\), \(k=0,\ldots,N-1\), **if and only if** \(c\le c_1\). Their common minimum in this regime is \(\eta y^0(cS^2/2-S)\). If \(c>c_1\), every global minimizer has at least two positive components.

The exact **local** classification of one-pulse controls is:

- When \(c\le c_1\), all \(N\) one-pulse controls are strict local (and global) minimizers.
- When \(c_1<c<1\), only the **last-step pulse** \(E e_{N-1}\) is a strict local minimizer; it is **not** global. Every earlier one-pulse control is not a local minimizer.
- When \(c\ge1\), no one-pulse control is a local minimizer.

For any value of \(c>0\), in every global minimizer the positive effort amounts, when listed in temporal order and ignoring zero steps, are nonincreasing. More strongly, for a fixed multiset of step efforts, placing the positive values in nonincreasing order never increases \(J_0\), and strictly decreases it whenever a larger positive amount is moved before a smaller positive amount.

These statements hold uniformly for every finite horizon \(N\). No statement is made about uniqueness or the full interior support pattern of the global minimizers when \(c>c_1\).

## Assumptions and scope

The pure-removal state scheme is implicit in the loss and has no production, spatial diffusion or predator coupling. The old-state quadrature is evaluated at \(y^i\), whereas a removal-flux reward would use the actual step loss \(y^i-y^{i+1}\). Time steps and catchability are constant. The budget is an equality constraint, and \(E\le U_{\max}\) ensures that any one-pulse allocation is feasible. All constants displayed as positive are strictly positive. The constraints form a compact simplex, so global minimizers exist.

The natural primary classification is nonlinear optimization (MSC2020 90C30). The source is the pure-removal comparison in Autran's 2026 work; this theorem only concerns the old-state objective, not the full predator–prey control problem.

## Proof

**1. Exact normalization and comparison.** Write \(x_i=\tau q u^i\), \(\sum_i x_i=S\), and \(P_i=\prod_{j<i}(1+x_j)\), with \(P_0=1\). Then \(y^i=y^0/P_i\). Dividing the objective by \(\eta y^0\) gives
\[
F_c(x)=\frac c2\sum_i x_i^2-\sum_i\frac{x_i}{P_i}.
\]
For every one-pulse vector \(S e_k\), \(F_c(S e_k)=cS^2/2-S\). Define
\[
Q(x)=\sum_{i<j}x_ix_j,\qquad
R(x)=S-\sum_i\frac{x_i}{P_i}
=\sum_i x_i\left(1-\frac1{P_i}\right).
\]
The **exact objective difference**, independently of the pulse location, is
\[
F_c(x)-F_c(S e_k)=R(x)-cQ(x). \tag{1}
\]

**2. Universal strict interference bound.** Set \(s_i=\sum_{j<i}x_j\). Since all components are nonnegative, \(P_i\ge1+s_i\). For each index having \(x_i>0\) and \(s_i>0\), one has \(0<s_i<S\) and therefore
\[
1-\frac1{P_i}\ge\frac{s_i}{1+s_i}>
\frac{s_i}{1+S}.
\]
For indices with \(x_i s_i=0\), the required termwise comparison holds as equality. Summing yields
\[
R(x)\ge\frac{Q(x)}{1+S}, \tag{2}
\]
with **strict inequality whenever \(Q(x)>0\)**. Indeed, when at least two components are positive, at least one summand has both \(x_i,s_i>0\). The condition \(Q(x)=0\) is equivalent to exactly one positive component because \(S>0\).

If \(c\le c_1\), (1)–(2) imply \(F_c(x)>F_c(S e_k)\) for every non-pulse feasible \(x\), proving all the asserted global minimizers and their strictness even at equality \(c=c_1\). The lower gap estimate \(F_c(x)-F_c(S e_k)>(c_1-c)Q(x)\) also follows whenever \(Q(x)>0\).

**3. Sharpness and loss of global optimality.** For \(0<\varepsilon<S\), take the vector with \(x_0=S-\varepsilon\), \(x_1=\varepsilon\) and all other entries zero. A direct calculation gives
\[
F_c(x)-F_c(S e_k)
=\varepsilon(S-\varepsilon)
\left(\frac1{1+S-\varepsilon}-c\right). \tag{3}
\]
If \(c>c_1\), this is negative for sufficiently small positive \(\varepsilon\), so **no** one-pulse vector is globally optimal. Moreover, dividing \(R(x)\) by \(Q(x)\) in this family and letting \(\varepsilon\downarrow0\) gives \(c_1\), proving that the constant in (2) is best possible. Compactness yields a global minimizer, and it must have at least two positive components.

**4. Classification of local pulse minima.** If \(k<N-1\) and \(c>c_1\), place \(S-\varepsilon\) at index \(k\) and \(\varepsilon\) at a later index. Formula (3) still holds, giving a feasible strict-descent direction arbitrarily close to \(S e_k\). Thus every earlier pulse is not a local minimizer.

For the last pulse, let \(\delta=\sum_{i<N-1}x_i\) and \(x_{N-1}=S-\delta\), where \(0<\delta<S\). Since \(P_{N-1}\ge1+\delta\) and all earlier terms of \(R(x)\) are nonnegative,
\[
R(x)\ge\frac{(S-\delta)\delta}{1+\delta}.
\]
Also \(Q(x)=(S-\delta)\delta+Q(x_0,\ldots,x_{N-2})\le(S-\delta)\delta+\delta^2/2\). By (1),
\[
F_c(x)-F_c(S e_{N-1})\ge
(S-\delta)\delta\left(\frac1{1+\delta}-c\right)
-\frac{c\delta^2}{2}. \tag{4}
\]
For every \(c<1\), the right-hand side is positive for all sufficiently small \(\delta>0\), uniformly over the distribution of earlier effort. Hence the last pulse is a strict local minimizer. For \(c\ge1\), move an amount \(\varepsilon\) to any earlier step and retain \(S-\varepsilon\) at the last step. In this ordering the exact difference is
\[
F_c(x)-F_c(S e_{N-1})
=\varepsilon(S-\varepsilon)\left(\frac1{1+\varepsilon}-c\right)<0,
\]
so the last pulse is not locally optimal. Together with the global result, this proves the full local three-regime classification.

**5. Ordering of nonzero efforts.** Suppose two successive *positive* values in temporal order are \(a,b>0\), possibly separated by zero entries, and let \(P\) be the population denominator preceding them. Their normalized old-state reward before swapping is \((a+b/(1+a))/P\), whereas after swapping it is \((b+a/(1+b))/P\); subsequent denominators agree. Their reward difference is exactly
\[
\frac{ab(a-b)}{P(1+a)(1+b)}.
\]
The quadratic effort penalty is permutation-invariant. Thus putting a larger positive amount first strictly lowers the objective. Repeated exchanges sort all positive values and prove the assertion; zeros may be freely repositioned without changing the objective.

## Verification

Run `python VERIFY.py` with Python 3 and no dependencies. The exact-rational checker enumerates finite allocation grids at \(2\le N\le7\), tests the strict gap and benchmark threshold, checks exact adjacent-swap identities, and checks explicit descent above the threshold. Its recorded output is `VERIFY_OK 14155 rational checks, 3256 strict-split cases`. These checks do not replace the all-parameter proof above, and finite enumeration cannot establish its universal quantifiers.

A simple scale example is \(S=2\), \(c=1/4\). The one-pulse vectors are exactly all global minimizers for **every** \(N\ge2\), even though \(1/(1+S)^2=1/9<1/4\). If \(1/3<c<1\), those one-pulse vectors cease to be globally optimal, but the last-step pulse remains a strict nonglobal local minimum.

## Relationship to prior work

Autran (arXiv:2611.20131v1, Section 6.1) introduces the pure-removal state and old-state versus new-state reward costs. Proposition 6.3 treats **two steps**, proving an extreme-allocation conclusion under the **sufficient** condition \(c<(1+S)^{-2}\); Proposition 6.2 gives a particular nonglobal local-minimum example. Neither statement supplies the exact global boundary \(c=(1+S)^{-1}\) for arbitrary \(N\), the independent local-pulse transition \(c=1\), or the arbitrary-horizon rearrangement rule. These are comparisons of logical coverage, not assertions of exclusive priority. Cacace, Oliviero and Pezzella (arXiv:2501.13085) study a broader production–destruction optimal-control scheme based on dynamic programming, but no corresponding exact fixed-budget phase diagram was established from accessible descriptions.

## Limitations

The theorem applies to pure removal with equal step lengths, a quadratic effort cost and a single shared total-effort budget small enough to fit in one time step. It does not classify all interior critical points or mixed-support global minimizers above the first threshold. It does not imply a new result for the true removal-flux quadrature or for the spatial Lotka–Volterra dynamics. Comparison with prior literature is based on identified accessible material and does not independently certify complete historical priority. Independent mathematical audit has not been performed.

## References

1. A. Autran, *Quadrature-Induced Local Minima in Structure-Preserving Lotka–Volterra Control*, arXiv:2611.20131v1 (first publicly released 2026-11-15), https://arxiv.org/html/2611.20131, especially Section 6 and Propositions 6.2–6.3.
2. S. Cacace, A. Oliviero, M. Pezzella, *Modified Patankar Semi-Lagrangian Scheme for the Optimal Control of Production-Destruction Systems*, arXiv:2501.13085v1 (2025-01-22), https://arxiv.org/abs/2501.13085.
