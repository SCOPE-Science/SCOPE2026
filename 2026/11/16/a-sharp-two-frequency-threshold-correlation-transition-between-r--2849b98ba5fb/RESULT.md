# A sharp two-frequency threshold-correlation transition between reciprocal radii

## Finding

Let \(f:\mathbb T\to[-1,1]\) be continuous, even, \(1\)-periodic, strictly decreasing on \([0,1/2]\), satisfy \(f(0)=1\), and obey \(f(t+1/2)=-f(t)\). For \(0<r\le1/4\), write \(\alpha_r=f(r)\) and, for distinct positive integer frequencies \(a,b\), put
\[
P_r(a,b)=m\{t\in\mathbb T:\ [f(at)>\alpha_r\text{ and }f(bt)>\alpha_r]\ \text{or}\ [f(at)<-\alpha_r\text{ and }f(bt)<-\alpha_r]\},
\]
where \(m\) is normalized Lebesgue measure on \(\mathbb T=\mathbb R/\mathbb Z\). Define \(F_r(2)=\inf_{1\le a<b}P_r(a,b)\).

For the **entire closed interval** \(1/6\le r\le1/5\),
\[
\boxed{F_r(2)=\begin{cases}
(28r-4)/5,&1/6\le r\le3/16,\\
4r/3,&3/16\le r\le1/5.
\end{cases}}
\]
The pair \(\{1,5\}\) attains the first branch, and \(\{1,3\}\) attains the second. Both attain the common value \(1/4\) at the **sharp switch radius** \(r=3/16\); further pairs can also attain equality there. All positive common-integer dilations of these pairs are likewise extremal in the stated branches. No complete classification of every minimizing pair is claimed.

For the cosine, the formula holds at every threshold \(\cos(2\pi/5)\le\alpha\le1/2\), with \(r=\arccos(\alpha)/(2\pi)\); the switching threshold is \(\alpha=\cos(3\pi/8)\). The result applies without changing its constants to every stated antipodal waveform.

## Assumptions and scope

All Fourier frequencies are positive and distinct, with no size cutoff. Since \(f\) has the stated shape, \(f(t)>\alpha_r\) is equivalent up to null endpoints to \(\|t\|_{\mathbb T}<r\), and \(f(t)<-\alpha_r\) to \(\|t-1/2\|_{\mathbb T}<r\). Thus only the level-arc half-width \(r\) matters. The uniform probability measure is on the parameter circle, not an independently sampled two-torus. Boundaries of strict threshold inequalities have measure zero. The infimum ranges over arbitrarily large frequencies, and common integer dilations do not change the measure.

## Proof

**Step 1: An exact two-frequency identity.** Divide \((a,b)\) by their greatest common divisor, which preserves \(P_r\), and henceforth assume they are coprime with \(1\le a<b\). Define the periodic Bernoulli polynomial
\[
B(x)=\{x\}^{2}-\{x\}+1/6,
\]
where \(\{x\}\) is the fractional part. Let \(U_r\) indicate \(\|t\|_{\mathbb T}<r\) and let \(V_r(t)=U_r(t-1/2)\). Their Fourier coefficients are
\[
\widehat U_r(0)=2r,\quad \widehat U_r(k)=\frac{\sin(2\pi kr)}{\pi k}\ (k\ne0),\quad \widehat V_r(k)=(-1)^k\widehat U_r(k).
\]
The simultaneous-threshold probability is \(\int_{\mathbb T}[U_r(at)U_r(bt)+V_r(at)V_r(bt)]\,dt\). Coprimality forces nonzero matching Fourier indices to be \((bk,-ak)\). Using the absolutely convergent correlation series and \(\sum_{k\ge1}\cos(2\pi kx)/k^2=\pi^2 B(x)\) gives the **exact identity valid for all real \(r\in(0,1/4]\)**:
\[
P_r(a,b)=8r^2+\begin{cases}
\dfrac{2}{ab}[B((b-a)r)-B((a+b)r)],&a,b\text{ both odd},\\[2mm]
\dfrac1{2ab}[B(2(b-a)r)-B(2(a+b)r)],&a+b\text{ odd}.
\end{cases}\tag{1}
\]
Since the pair is coprime, these are the only parity possibilities. The equality is for probability measures, not just an asymptotic estimate.

**Step 2: Sharp candidates and an infinite-frequency cutoff.** Direct substitution into (1), or elementary interval intersection, gives on \(1/6\le r\le1/5\)
\[
P_r(1,5)=\frac{28r-4}{5},\qquad P_r(1,3)=\frac{4r}{3}.
\]
They cross precisely at \(r=3/16\). Let \(Q(r)\) be their smaller value, the right-hand side of the finding. Direct differentiation separately on the two subintervals shows
\[
8r^2-Q(r)\ge1/32,\qquad 1/6\le r\le1/5,
\tag{2}
\]
with equality only at \(r=3/16\). The function \(B\) ranges from \(-1/12\) to \(1/6\), so \(B(x)-B(y)\ge-1/4\). Formula (1) therefore implies
\[
P_r(a,b)\ge
\begin{cases}
8r^2-1/(2ab),&a,b\text{ odd},\\
8r^2-1/(8ab),&a+b\text{ odd}.
\end{cases}\tag{3}
\]
Combining (2) and (3) proves \(P_r(a,b)\ge Q(r)\) **uniformly over the continuum** whenever \(ab\ge16\) in the odd--odd case or \(ab\ge4\) in the opposite-parity case. This is the rigorous infinite-frequency exclusion; no finite frequency search is treated as exhaustive without this analytic bound.

**Step 3: The complete finite remainder.** Coprimality and the product restrictions in Step 2 leave *exactly nine* unordered positive pairs:
\[
(1,2),\ (1,3),\ (1,5),\ (1,7),\ (1,9),\ (1,11),\ (1,13),\ (1,15),\ (3,5).
\]
For each such pair, the only possible changes of the fractional-part branches in (1), within the interval \([1/6,1/5]\), occur at the endpoints or at \(3/16\). In fact, the only interior Bernoulli branch switch is at \(3/16\) for the pair \((1,15)\). Therefore \(P_r(a,b)-Q(r)\) is affine on each of \([1/6,3/16]\) and \([3/16,1/5]\), and it suffices to verify nonnegativity at the three endpoints. The following table gives the **exact differences** at \(r=1/6,3/16,1/5\), respectively:

| Frequencies | \(1/6\) | \(3/16\) | \(1/5\) |
|---|---:|---:|---:|
| \((1,2)\) | \(1/30\) | \(0\) | \(1/30\) |
| \((1,3)\) | \(4/45\) | \(0\) | \(0\) |
| \((1,5)\) | \(0\) | \(0\) | \(4/75\) |
| \((1,7)\) | \(16/105\) | \(1/14\) | \(8/105\) |
| \((1,9)\) | \(4/45\) | \(0\) | \(0\) |
| \((1,11)\) | \(8/165\) | \(1/22\) | \(16/165\) |
| \((1,13)\) | \(8/65\) | \(1/26\) | \(8/195\) |
| \((1,15)\) | \(4/45\) | \(0\) | \(4/75\) |
| \((3,5)\) | \(4/45\) | \(1/30\) | \(4/75\) |

Every entry follows by substituting the corresponding rational arguments into the elementary polynomial \(B\); the checker reproduces them using exact rational arithmetic. Each table entry is nonnegative. Affinity between endpoints completes the inequalities for every real \(r\) in the interval. Together with the infinite-frequency cutoff and the two attaining pairs, this proves the stated sharp formula. \(\square\)

## Verification

The dependency-free `CHECK.py` separately calculates the Bernoulli formula and exact geometric overlaps of lifted arc intervals; it compares them at numerous rational radii and primitive frequencies. It exhaustively regenerates the nine finite exceptional pairs, verifies the complete rational difference table and absence of additional interior fractional-part breakpoints, and checks both sharp candidate formulas. An exact rational certificate, not a floating-point grid, supports the finite part. The unbounded-frequency conclusion follows from (2)--(3) and the parity/product classification; experiments alone would not prove it. Run `python3 CHECK.py` using Python 3 standard-library modules.

## Relationship to prior work

Giannitsi and Madrid, arXiv:2610.38135 (first posted 2026-10-28), define antipodal-wave threshold correlations, establish the general lower bound \(F_r(n)\ge4r^n\), and study their asymptotic exponential rate; its inspected main theorems and relevant proof sections do not state an exact two-frequency minimization for the present continuum. The general lower bound gives only \(4r^2\) at \(n=2\), strictly weaker than the displayed sharp values. The published sharp reciprocal-radius two-frequency result on published-finding corpus covers \(r=1/m\), including the endpoint values \(r=1/6\) and \(r=1/5\), but asserts no result for the open interval. Another published published-finding corpus result establishes \(P_r(A)/r\) nondecreasing and exact \(F_r(2)=4r/3\) for \(r\ge1/5\); applying that monotonicity to the known value at \(1/6\) yields only \(F_r(2)\ge4r/5\), not the new affine lower branch, nor the sharp switch at \(3/16\). Its piecewise-affinity observation for **fixed pairs** is used here as an acknowledged general fact, while the new statement minimizes over **all** pairs with a uniform analytical frequency cutoff.

The sign-only work of Gonçalves, Oliveira e Silva and Steinerberger, and of Zang, Zhao, Zhao and Zhou, addresses \(r=1/4\) or general counts at zero threshold, not the present positive-threshold continuum. The classical Fourier and Bernoulli identities are inputs, not asserted original. The new claim concerns the exact phase boundary and optimal value in the previously unresolved interval between two reciprocal radii.

## Limitations

The theorem is restricted to two unshifted integer frequencies and \(1/6\le r\le1/5\) (equivalently, a specified interval of positive thresholds). It does not classify every frequency pair attaining equality, prove sharp values for smaller radii, or settle the multivariate or three-frequency problem. It does not determine the large-frequency-count exponential rate for nonreciprocal radii. Publication priority remains provisional because an older unindexed exact pair-optimization result using a different formulation could exist.

## References

1. C. Giannitsi and J. Madrid, *Exponential decay of threshold correlations for symmetric periodic functions*, arXiv:2610.38135, first public 2026-10-28; https://arxiv.org/html/2610.38135v1.
2. F. Gonçalves, D. Oliveira e Silva and S. Steinerberger, *A Universality Law for Sign Correlations of Eigenfunctions of Differential Operators*, arXiv:1903.06826 (2019); https://arxiv.org/abs/1903.06826.
3. S. Dou, A. Goh, K. Liu, M. Legate and G. Pettigrew, *Cosine Sign Correlation*, arXiv:2212.02496 (2022); https://arxiv.org/abs/2212.02496.
4. S. Zang, Y. Zhao, Y. Zhao and C. Zhou, *Extremal cosine sign correlations*, arXiv:2610.33190, first posted 2026-10-23; https://arxiv.org/abs/2610.33190.
5. *Sharp reciprocal-threshold two-frequency cosine correlations*, publicly indexed published-finding corpus record `2026/11/1/SCOPE-sharp-reciprocal-threshold-two-frequency-cosine-correlations--37afa94b7519` (2026).
6. *Sharp radius scaling for simultaneous Fourier-threshold correlations*, publicly indexed published-finding corpus record `2026/11/1/SCOPE-sharp-radius-scaling-for-simultaneous-fourier-threshold-correlat--3926797a2c98` (2026).
