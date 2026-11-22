# Exact real-zero collision staircase for a two-activity hard-core wheel gas

## Finding

For every integer \(n\ge4\), consider the hard-core lattice gas on the wheel \(K_1\vee C_n\). Every rim vertex has one common complex fugacity \(z\), while the hub has an independently fixed **nonnegative real** fugacity \(t\). Write \(d=\lfloor n/2\rfloor\) and
\[
Z_n(z;t)=\sum_{S\subseteq V\text{ independent}}z^{|S\cap C_n|}t^{\mathbf1_{\{\mathrm{hub}\in S\}}}=I(C_n,z)+t.
\]
The following is the complete real-zero phase diagram as \(t\) increases. For \(1\le j\le \lfloor d/2\rfloor\), define
\[
\theta_{n,j}=\frac{(2j-1)\pi}{n-1},\qquad
\tau_{n,j}=2^{1-n}\sec^{n-1}\theta_{n,j},\qquad
\zeta_{n,j}=-\frac{1}{4}\sec^2\theta_{n,j}.
\]
Then \(0<\tau_{n,1}<\cdots<\tau_{n,\lfloor d/2\rfloor}\). For every \(t\ge0\), the number of **negative real roots counted with multiplicity** is exactly
\[
N_{\mathbb R}(n,t)=d-2\#\{j:\tau_{n,j}<t\}.
\]
At a threshold \(t=\tau_{n,j}\), exactly one negative root \(\zeta_{n,j}\) is double, and all other roots are simple; no other real parameter produces multiple roots. Thus all roots are real and negative precisely when
\[
\boxed{\ 0\le t\le \tau_{n,1}=2^{1-n}\sec^{n-1}\!\left(\frac{\pi}{n-1}\right)\ }.
\]
The endpoint has exactly one double root. For larger \(t\), conjugate pairs leave the negative real axis one at a time at the explicit thresholds. After the last threshold there are zero real roots when \(d\) is even and one when \(d\) is odd.

The collision has an explicit square-root local law. For \(\delta\downarrow0\), the two roots leaving at the \(j\)-th threshold obey
\[
 z_\pm=\zeta_{n,j}\pm i A_{n,j}\sqrt\delta+O_n(\delta),\quad
 A_{n,j}=\frac{2^{(n-2)/2}\sin\theta_{n,j}\cos^{(n-5)/2}\theta_{n,j}}{\sqrt{n(n-1)}},
\quad t=\tau_{n,j}+\delta.
\]
For fixed \(j\), the sharp large-rim onset is
\[
\tau_{n,j}=2^{1-n}\exp\!\left(\frac{(2j-1)^2\pi^2}{2(n-1)}+O_j(n^{-3})\right).
\]
In particular, the largest possible hub fugacity preserving all-real rim-fugacity zeros decays exponentially in the rim size.

## Assumptions and scope

The graph has exactly \(n\ge4\) rim sites forming a simple cycle, all joined to one universal hub. Allowed independent configurations have no occupied adjacent pair. The rim's common fugacity is the **only variable whose complex roots are counted**. Hub fugacity \(t\) is a separately fixed, finite, nonnegative real parameter. There are no interactions beyond hard-core exclusion, and no claim is made for independently varied rim activities or other graphs. A root is counted with its algebraic multiplicity.

## Proof

**Partition and degree.** An occupied hub excludes every rim site, contributing exactly \(t\); an empty hub contributes the usual cycle independence polynomial. Counting nonadjacent \(k\)-subsets of an \(n\)-cycle gives
\[
P_n(z)=I(C_n,z)=\sum_{k=0}^{d}\frac{n}{n-k}\binom{n-k}{k}z^k,
\]
which has positive leading coefficient and degree \(d\). With \(\lambda_\pm=(1\pm\sqrt{1+4z})/2\), the two-state hard-core transfer recursion gives the classical identity
\[
P_n(z)=\lambda_+^n+\lambda_-^n.
\]
For \(z\ge-1/4\), this is strictly positive: for \(-1/4\le z\le0\), both branches are nonnegative, whereas for \(z>0\), the positive branch exceeds the magnitude of the negative branch. Therefore \(P_n(z)+t\) has no root in \([-1/4,\infty)\) for \(t\ge0\).

**All stationary values.** Parametrize the entire remaining real half-line by
\[
 z(\theta)=-\frac{1}{4\cos^2\theta},\qquad 0<\theta<\pi/2.
\]
Then \(\lambda_\pm=e^{\pm i\theta}/(2\cos\theta)\), so
\[
P_n(z(\theta))=2^{1-n}\frac{\cos(n\theta)}{\cos^n\theta},\qquad
\frac{d}{d\theta}P_n(z(\theta))=-n2^{1-n}\sec^{n+1}\theta\sin((n-1)\theta).
\]
Because \(z'(\theta)<0\), every finite critical point of \(P_n\) is at
\[
\theta_k=\frac{k\pi}{n-1},\qquad k=1,\ldots,d-1.
\]
These are exactly \(d-1\) distinct critical points, exhausting the roots of the degree-\(d-1\) derivative. At each,
\[
P_n(z(\theta_k))=(-1)^k2^{1-n}\sec^{n-1}\theta_k.
\]
Odd \(k\) are strict negative minima and even \(k\) are strict positive maxima. The negative minima have strictly decreasing values with increasing odd \(k\), hence their cancellation parameters \(\tau_{n,j}\) are strictly increasing. All critical points are nondegenerate because the displayed sine derivative has a simple zero there and \(z'(\theta_k)\ne0\).

**Counting without missed roots.** At \(t=0\), the \(d\) zeros are the distinct numbers
\[
-\frac{1}{4}\sec^2\!\left(\frac{(2\ell-1)\pi}{2n}\right),\qquad\ell=1,\ldots,d.
\]
As \(t\) varies, real roots can change count only at a multiple real root, which requires the derivative to vanish. All such derivative zeros were enumerated above; with \(t\ge0\) only the odd-indexed negative minima can be canceled. At each such cancellation precisely two simple negative roots merge into one double root and, for larger \(t\), become a nonreal conjugate pair. Since the leading coefficient and degree are fixed, no roots enter from infinity. Each threshold lowers the real-root count by two after, but not at, equality. These observations prove the stated exact root-count formula and real-rootedness interval, including its boundary.

**Unfolding and scale.** At an odd \(k=2j-1\), differentiating the displayed parametric identity twice and using \(z'(\theta_k)\ne0\) yields
\[
P_n''(\zeta_{n,j})=\frac{2^{3-n}n(n-1)\cos^{5-n}\theta_{n,j}}{\sin^2\theta_{n,j}}>0.
\]
The analytic Taylor expansion of \(P_n(z)+\tau_{n,j}+\delta\) at this double zero gives \((z-\zeta)^2=-2\delta/P_n''(\zeta)+O(\delta^{3/2})\), giving the explicit \(A_{n,j}\) above and the \(O_n(\delta)\) real correction. Finally \(\log\sec u=u^2/2+O(u^4)\) refined to \(u^2/2+u^4/12+O(u^6)\) shows the stated \(O_j(n^{-3})\) exponent remainder for each fixed \(j\).

## Verification

The standalone file `verify_wheel_zeros.py` independently constructs the cycle polynomial both by enumerating all independent binary configurations and by the exact binomial coefficient formula. For each rim size \(4\le n\le14\), it checks exact Sturm real-root counts at rational hub fugacities between and beyond all critical thresholds, and compares all critical polynomial values with the trigonometric identity. Exact common-factor calculations separately certify double roots at \((n,t)=(4,1),(5,1/4),(7,1/27)\). All checks passed. The mathematical all-size conclusions follow from the displayed proof, not from a finite experiment.

## Relationship to prior work

The cycle independence polynomial and its Chebyshev formula are established; the partition identity \(P_n(z)+t\) follows immediately by the hub-independent-set split and is **not** the novelty claim. The 2003 paper by Levit and Mandrescu concerns root locations for very well-covered graph expansions. Chudnovsky and Seymour's claw-free theorem proves real-rootedness for standard single-activity independence polynomials of claw-free graphs; it neither treats the independently fixed hub fugacity nor implies the present all-rim-size threshold. Brown and Cameron examine Hurwitz stability (left-half-plane zeros), not a complete real-root collision staircase. Prakash and Sharma use the unperturbed cycle Chebyshev formula to bound separation of its first two zeros, not roots of the two-activity family. The table of known independence polynomials includes the univariate wheel graph but does not provide the two-activity, fixed-hub real-zero classification. The closest identified indexed wheel–whirl Ehrhart-pencill result concerns a different polynomial and is not an implication of or proof for this result. The distinctive assertion here is the exact, strictly ordered full collision staircase together with the exponential critical scale and local pair-opening law.

## Limitations

The branch-count theorem is limited to a single independently fixed nonnegative real hub activity and one common complex rim variable. Allowing negative or complex hub activity changes the threshold ordering and is not treated. Complex zeros at positive hub fugacities do not constitute physical singularities on the positive-real fugacity axis or a thermodynamic phase transition. Prior-work search cannot establish global historical priority; an unindexed earlier Chebyshev perturbation analysis might imply the same formulas. The finite tests complement, rather than replace, the all-size proof.

## References

1. V. E. Levit and E. Mandrescu, *On the Roots of Independence Polynomials of Almost All Very Well-Covered Graphs*, arXiv:math/0305227, first preprint 2003-05-15, https://arxiv.org/abs/math/0305227.
2. M. Chudnovsky and P. Seymour, *The Roots of the Independence Polynomial of a Clawfree Graph*, manuscript dated 2004-02-01, https://www.ias.edu/sites/default/files/math/csdm/03-04/mchudnovsky_the_roots_of_the_stable_set.pdf.
3. J. I. Brown and B. Cameron, *On the Stability of Independence Polynomials*, Electronic Journal of Combinatorics 25 (2018), P1.46; arXiv:1802.02478, https://arxiv.org/abs/1802.02478.
4. O. Prakash and V. Sharma, *On the Roots of Independence Polynomial: Quantifying the Gap*, FSTTCS 2025, https://doi.org/10.4230/LIPIcs.FSTTCS.2025.48.
5. E. W. Weisstein, *Independence Polynomial*, MathWorld, https://mathworld.wolfram.com/IndependencePolynomial.html (classical cycle and wheel formulas).
