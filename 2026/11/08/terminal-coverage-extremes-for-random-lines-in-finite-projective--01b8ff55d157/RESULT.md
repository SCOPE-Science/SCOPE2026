# Terminal coverage extremes for random lines in finite projective planes

## Finding

For any sequence of existing finite projective planes whose orders \(q\) grow without bound, **the last points reached by independent uniformly sampled lines form the same asymptotic Poisson extreme process as in unrestricted equal-size subset sampling**. Specifically, with \(v=q^2+q+1\), \(k=q+1\), \(s=v/k\), and first-hit times \(\tau_P\),
\[
\sum_P\delta_{\tau_P/s-\log v}\ \Longrightarrow\ \operatorname{PPP}(e^{-x}\,dx)
\]
in the space of locally finite counting measures on \(\mathbb R\), with vague convergence. The full random \(k\)-subset mechanism on the same \(v\) points has the identical limit.

For the total cover time \(T_q=\max_P\tau_P\), this gives
\[
\Pr\!\left(\frac{T_q}{s}-\log v\le x\right)\to\exp(-e^{-x}),\qquad
\mathbb E T_q=s(\log v+\gamma)+o(s),\quad
\operatorname{Var} T_q=\frac{\pi^2}{6}s^2+o(s^2).
\]
Here \(\gamma\) is Euler's constant. For any fixed \(j\ge1\), the \(j\)-th last first-hit time, centered and scaled identically, converges jointly across finitely many \(j\) to \(-\log\Gamma_j\), where \(\Gamma_j=E_1+\dots+E_j\) and the \(E_i\) are independent unit exponentials. The differences between the two mechanisms' means and variances are respectively \(o(q)\) and \(o(q^2)\).

## Assumptions and scope

A finite projective plane of order \(q\) has \(v=q^2+q+1\) points and lines, each line containing \(k=q+1\) points, each point belonging to \(k\) lines, and each pair of distinct points contained together in exactly one line. No coordinatization or assumption that \(q\) is a prime power is needed; the limit is only along orders of planes that exist. The sequence of sampled lines is independent and uniform with replacement. Each \(\tau_P\) is the positive integer first-draw time at which point \(P\) is covered. The comparison full mechanism instead draws one uniform \(k\)-subset of the \(v\) points at each independent round. These are *distinct mechanisms*: their finite-order higher joint probabilities need not agree.

## Proof

**1. Exact avoidance estimates.** For \(r\) distinct points \(P_1,\ldots,P_r\), let \(H(A)\) be the number of lines hitting a set \(A\) of these points. Counting the \(k\) incident lines at each point and using the fact that every pair shares exactly one line gives
\[
|A|k-\binom{|A|}{2}\ \le\ H(A)\ \le\ |A|k.
\]
Consequently, for fixed \(r\), uniformly in subsets \(A\subseteq\{P_1,\ldots,P_r\}\),
\[
\log\!\left(1-\frac{H(A)}{v}\right)=-\frac{|A|k}{v}+O_r(q^{-2}).
\]
This estimate is applied for large enough \(q\), so all logarithms have positive arguments. For the unrestricted mechanism, a draw avoids \(A\) with probability \(\binom{v-|A|}{k}/\binom vk\); the product formula likewise gives \(\log \Pr(\text{avoid }A)=-|A|k/v+O_r(q^{-2})\).

**2. Multitime joint survival.** Fix real numbers \(x_1,\ldots,x_r\) and define the integer thresholds \(t_i=\lfloor s(\log v+x_i)\rfloor\). At round \(u\), to keep all \(P_i\) unhit until their respective thresholds we need to avoid the active set \(A_u=\{P_i:t_i\ge u\}\). Independence between rounds and Step 1 give
\[
\log\Pr(\tau_{P_i}>t_i\ \forall i)
 =-\frac{k}{v}\sum_{i=1}^r t_i
 +O_r\!\left(\frac{\log v}{q}\right)
 =-r\log v-\sum_{i=1}^r x_i+o(1).
\]
The bounds are uniform over the \(r\) distinct labeled points, so
\[
(v)_r\Pr(Y_{P_i}>x_i\ \forall i)\to\prod_{i=1}^r e^{-x_i}.
\]
Exactly the same argument works for unrestricted random \(k\)-subsets.

**3. Extreme point-process limit.** For disjoint bounded half-open intervals \(I_j=(a_j,b_j]\), inclusion-exclusion of the multitime survival events in Step 2 shows that the factorial moment of the vector of point counts satisfies, for every fixed tuple of nonnegative integers \(r_j\),
\[
\mathbb E\prod_j(\Xi_q(I_j))_{r_j}
\longrightarrow\prod_j(e^{-a_j}-e^{-b_j})^{r_j}.
\]
These are precisely the mixed factorial moments of independent Poisson variables with respective means \(e^{-a_j}-e^{-b_j}\). The joint factorial-moment method (Poisson laws have finite moment-generating functions near zero), together with bounded expected counts on compact intervals, proves convergence of the locally finite point process to \(\operatorname{PPP}(e^{-x}dx)\). The same argument applies to intervals \((a,\infty)\), as \(\mathbb E\Xi_q((a,\infty))\to e^{-a}\), giving tightness of the uppermost points. Under the transformation \(z=e^{-x}\), limiting points become a homogeneous rate-one Poisson process on \((0,\infty)\), whose first \(j\) arrivals are \(\Gamma_j\). This proves all stated order-statistic limits, including the Gumbel law for the maximum.

**4. Moment convergence.** In the line mechanism, the one-round probability that one fixed point is missed is \(a=1-k/v\), and the probability two distinct points are both missed is \(b=1-(2k-1)/v\). The identity
\[
b-a^2=\frac{v-k^2}{v^2}=-\frac{q}{v^2}<0
\]
implies that distinct indicators of remaining uncovered are pairwise negatively correlated after any integer number of rounds. Hence the number \(U_t\) of uncovered points satisfies \(\operatorname{Var}U_t\le\mathbb E U_t\), with \(\mathbb E U_t=v(1-k/v)^t\). For \(X_q=T_q/s-\log v\), the union bound for late coverage and the second-moment bound for premature coverage imply, with an absolute constant \(C\) for all large \(q\),
\[
\Pr(X_q>x)\le Ce^{-x},\qquad
\Pr(X_q<-x)\le Ce^{-x}\qquad(x\ge0).
\]
For the second bound use \(\Pr(U_t=0)\le\operatorname{Var}U_t/(\mathbb E U_t)^2\le1/\mathbb E U_t\) at \(t=\lfloor s(\log v-x)\rfloor\), and note that \(\mathbb E U_t\ge c e^x\) while \(t\ge0\); for negative \(t\) early coverage is impossible. These uniform exponential tails imply uniform integrability of every fixed polynomial in \(X_q\), and hence convergence of its first two moments to those of the standard Gumbel distribution: mean \(\gamma\), variance \(\pi^2/6\).

For unrestricted \(k\)-subset draws, the one-point avoidance probability is the same, and the two-point avoidance probability \((v-k)(v-k-1)/(v(v-1))\) is no larger than its square, giving identical bounds. Since \(s\sim q\), the stated differences in raw means and variances follow from the common expansions.

## Verification

Run `python3 CHECK.py` using Python 3's standard library. The checker generates the incidence structures of \(PG(2,q)\) for the prime orders \(q=2,3,5\), checks every point degree, every pair of points' unique common line, the avoidance union bounds on all subsets of up to four points, and the strict pairwise negative covariance. It also independently enumerates small sample paths to verify the multitime survival product and computes the exact \(q=2\) mean \(163/30\) by inclusion-exclusion. These finite checks corroborate the algebraic inputs but do not establish the asymptotic theorem; Steps 1–4 provide its proof for arbitrary existing projective planes.

## Relationship to prior work

Barak-Pelleg and Berend (arXiv:2606.28216, first public date 2026-06-26) determined small-order projective and affine-plane mean cover times and studied a different star mechanism. Their projective-plane numerical comparisons do not supply a growing-order terminal-point-process or moment theorem. Grunbaum and Yaakobi (arXiv:2510.25305, 2025) give exact recovery-set formulas and mean bounds for fair mechanisms, not the marked extreme-point process. Betken and Thäle (2023), and Athreya, Mukherjee and Mukherjee (2023), study uniformly sampled full subsets and related super-coupon models; their scopes do not establish the line-restricted process limit for projective planes. Mikhailov (1996/1997) proves a general one-time Poisson uncovered-point limit for independent random subset coverings; the full paper was not accessible for statement-level comparison, and any implications of its general theorem beyond one-time count convergence remain a priority risk. The present result explicitly claims the *marked joint terminal process and two moment limits*, not a first general Poisson theorem for uncovered coupons.

## Limitations

The result is asymptotic only as \(q\to\infty\), with no finite-order domination, monotonicity, or sign for the tiny difference between the projective and full mechanisms. It yields only \(o(q)\) control on the mean gap, not an absolute constant or its sign. It does not establish a convergence rate, finite-sample total-variation estimate, or uniformity in the index of the last point. Historical-priority risk persists for broad random covering theorems, particularly the inaccessible full text of Mikhailov's 1996/1997 result. The statement is not independently validated.

## References

- D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216v1 (2026), https://arxiv.org/html/2606.28216.
- Y. Grunbaum and E. Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305 (2025), https://arxiv.org/abs/2510.25305.
- C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, Journal of Applied Probability 60 (2023), https://doi.org/10.1017/jpr.2023.6.
- S. Athreya, S. Mukherjee and S. S. Mukherjee, *On a generalisation of the coupon collector problem*, arXiv:2304.01145 (2023), https://arxiv.org/abs/2304.01145.
- V. G. Mikhailov, *Limit theorems for a random covering of a finite set and for the number of solutions of a system of random equations*, Theory of Probability and Its Applications 41 (1997), 265–274, https://doi.org/10.1137/S0040585X97975472 (abstract consulted; full text unavailable).
