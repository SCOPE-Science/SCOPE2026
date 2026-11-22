# A sharp rate-imbalance frontier for all-step BDF2 positivity on two-state Markov chains

## Finding

Let \(a,b>0\), \(\sigma=a+b\), and let
\[
Q=\begin{pmatrix}-a&a\\b&-b\end{pmatrix}
\]
be a two-state continuous-time Markov generator acting on row probability vectors. With constant step \(h>0\), define the backward-Euler-started BDF2 transition operators by
\[
M_0=I,\qquad M_1=(I-hQ)^{-1},\qquad
M_n=(3I-2hQ)^{-1}(4M_{n-1}-M_{n-2})\quad(n\ge2).
\]
Every \(M_n\) has row sums one. The following is a sharp necessary and sufficient condition for **all** of these matrices to be entrywise nonnegative at **every** positive step size:
\[
\boxed{\frac{\max(a,b)}{\min(a,b)}\le17+12\sqrt2.}
\]
More precisely, define \(r=h\sigma\) and the scalar sequence
\[
z_0(r)=1,\quad z_1(r)=\frac1{1+r},\quad
(3+2r)z_n(r)=4z_{n-1}(r)-z_{n-2}(r)\quad(n\ge2).
\]
For all \(r>0\) and \(n\ge0\), its *sharp global lower envelope* is
\[
\boxed{z_n(r)\ge-(17-12\sqrt2).}
\]
Equality holds only at \(n=2\) and \(r=3+3\sqrt2\). Also \(z_n(r)<1\) for all \(n\ge1\). Consequently, at the sharp rate-ratio boundary a diagonal entry of \(M_2\) vanishes exactly at this normalized step; below the ratio boundary every \(M_n\), \(n\ge1\), is strictly positive for every \(h>0\). If the rate ratio exceeds the boundary, some positive steps generate a negative entry already at \(n=2\), whereas all sufficiently small and all sufficiently large steps yield nonnegative \(M_n\) for *every* \(n\ge0\).

For a rational strict witness take \((a,b)=(40,1)\), \(h=7/41\). Then \((M_2)_{11}=-3/697<0\) in the displayed state ordering, even though both \(M_0\) and \(M_1\) are nonnegative.

## Assumptions and scope

The two transition rates are strictly positive, the timestep is constant, and the starting step is precisely backward Euler at the same \(h\). The recurrence is interpreted in exact arithmetic and applied to an initial row probability vector \(p_0\) via \(p_n=p_0M_n\). The assertion of positivity requires every \(p_0\) in the two-state probability simplex and every integer \(n\ge0\); it does *not* quantify over independently specified pairs of prior probability vectors. No assertion concerns numerical rounding, stability under arbitrary starting-history perturbations, nonlinear Markov models, larger state spaces, or variable-step BDF2.

## Proof

**1. Stationary projection and the sharp reduction.** Set
\[
\Pi=\frac1\sigma\begin{pmatrix}b&a\\b&a\end{pmatrix},
\qquad Q=-\sigma(I-\Pi),\qquad \Pi^2=\Pi.
\]
The mass and centered eigenspaces of \(Q\) have eigenvalues \(0\) and \(-\sigma\). Induction in the multistep recurrence therefore gives
\[
M_n=\Pi+z_n(r)(I-\Pi).
\]
For \(n\ge1\), the off-diagonal entries are \((1-z_n)\Pi_{ij}\), and the two diagonal entries are, respectively,
\[
\frac{b+a z_n}{\sigma},\qquad\frac{a+b z_n}{\sigma}.
\]
Provided \(z_n<1\), mass preservation and entrywise nonnegativity are therefore equivalent to
\[
z_n\ge-\frac{\min(a,b)}{\max(a,b)}.
\]
It remains to find the global scalar lower envelope and verify the strict upper bound.

**2. Scalar positivity at small steps.** When \(0<r<1/2\), the characteristic equation
\[
(3+2r)\xi^2-4\xi+1=0
\]
has two distinct positive roots. The backward-Euler-started solution is strictly positive at every index; explicitly, with \(s=\sqrt{1-2r}\), it equals
\[
z_n=A_s(2-s)^{-n}-B_s(2+s)^{-n},
\quad A_s=\frac{(2-s)(1+s)^2}{2s(3-s^2)},\quad
B_s=\frac{(2+s)(1-s)^2}{2s(3-s^2)}.
\]
Here \(A_s-B_s=1\), \(A_s,B_s>0\), and \((2-s)^{-n}\ge(2+s)^{-n}\), so \(z_n>0\). At \(r=1/2\) the repeated-root solution is \(z_n=2^{-n}(1+n/3)>0\). The difference equation
\[
(3+2r)(z_{n+1}-z_n)=(z_n-z_{n-1})-2rz_n
\]
starts with \(z_1-z_0<0\); positivity implies strict decrease. Thus \(0<z_n<1\) for \(0<r\le1/2\), \(n\ge1\).

**3. A uniform large-index bound.** If \(r>1/2\), write \(D=3+2r>4\), \(\rho=D^{-1/2}<1/2\), and choose \(0<\theta<\pi/2\) so that
\[
\cos\theta=\frac2{\sqrt D},\qquad
\sin\theta=\frac{\sqrt{2r-1}}{\sqrt D}.
\]
Matching the backward-Euler starter gives the exact formula
\[
z_n=\rho^n\left[\cos(n\theta)+
\frac{\sin(n\theta)}{(1+r)\sqrt{2r-1}}\right].
\]
The elementary bound \(|\sin(n\theta)|\le n\sin\theta\) implies
\[
|z_n|\le\rho^n\left(1+\frac{n}{(1+r)\sqrt D}\right)
\le 2^{-n}\left(1+\frac n3\right).
\]
In particular, \(|z_n|\le5/192<29/1000\) for every \(n\ge7\), since the last sequence decreases with \(n\ge1\). For \(n\ge1\) this same inequality implies \(z_n<1\).

**4. Exact finite-index lower bounds.** Put \(N_1=1\), \(N_2=3-r\), and
\[
N_n=4N_{n-1}-(3+2r)N_{n-2}\quad(n\ge3).
\]
Then \(z_n=N_n/[(1+r)(3+2r)^{n-1}]\) for \(n\ge2\), and
\[
\begin{aligned}
N_3&=9-6r,\\
N_4&=2r^2-27r+27,\\
N_5&=(2r-9)(10r-9),\\
N_6&=-4r^3+128r^2-405r+243.
\end{aligned}
\]
For \(n=3,4,5,6\), set \(t=r-1/2>0\) and
\[
P_n(t)=1000N_n(r)+29(1+r)(3+2r)^{n-1}.
\]
Exact expansion yields
\[
\begin{aligned}
P_3&=116t^3+638t^2-4840t+6696,\\
P_4&=232t^4+1740t^3+6872t^2-18968t+16784,\\
P_5&=464t^5+4408t^4+16704t^3+51552t^2-58304t+43136,\\
P_6&=928t^6+10672t^5+51040t^4+125920t^3+307600t^2-138944t+116544.
\end{aligned}
\]
For \(P_4,P_5,P_6\), every higher-degree monomial is nonnegative on \(t\ge0\), and each trailing quadratic (the last three terms) has positive leading and constant coefficients and strictly negative discriminant. For \(P_3\), on \(0\le t\le2\), substituting \(u=2-t\) gives \(496+896u+(1334-116u)u^2>0\); on \(t\ge2\), substituting \(u=t-2\) gives \(496-896u+1334u^2+116u^3>0\), since the first three terms form a strictly positive quadratic. Hence \(z_n>-29/1000\) for \(3\le n\le6\). Since
\[
17-12\sqrt2>\frac{29}{1000}>\frac5{192},
\]
none of these or larger indices can reach \(-(17-12\sqrt2)\).

**5. The unique minimizer and two-state frontier.** The only possibly lower value occurs at \(n=2\), for which
\[
z_2(r)=\frac{3-r}{(1+r)(3+2r)},\qquad
z_2'(r)=\frac{2(r^2-6r-9)}{(1+r)^2(3+2r)^2}.
\]
There is exactly one positive critical point, \(r_*=3+3\sqrt2\), the strict global minimum with value \(z_2(r_*)=-(17-12\sqrt2)\). The index \(n=0\) has value one, and \(n=1\) is positive, so this proves the global infimum and its unique equality case. The two diagonal inequalities from step 1 are now simultaneously true for every \(r,n\) precisely when \(\min(a,b)/\max(a,b)\ge17-12\sqrt2\). Taking reciprocals proves the advertised sharp boundary.

**6. Safe small and large steps outside the frontier.** For all \(0<r\le1/2\), all centered scalar coefficients are positive and decreasing, so \(M_n\) is nonnegative for all indices, regardless of the rates. As \(r\to\infty\), \(z_1\to0\), and step 3 gives a uniform \(O(r^{-1})\) bound on \(\sup_{n\ge2}|z_n(r)|\) (use \(\rho\to0\) and decreasing powers). Thus all entries of \(M_n\), \(n\ge1\), are strictly positive for sufficiently large \(r\). When the rate ratio exceeds the sharp threshold, setting \(r=r_*\) makes one diagonal entry of \(M_2\) negative, proving the claimed intervening failure. This does not classify every intermediate admissible step window.

## Verification

Run `python verify.py` with Python 3 and SymPy 1.11 or later. The verifier checks exact symbolic formulas for the first six scalar iterates, all shifted-polynomial identities used in the positivity proof, the exact minimizer and reciprocal threshold, 560 exact-rational Markov-matrix recurrence identities, and the explicit negative rational witness. The recorded output is included in `verification_output.txt`. These finite computations check algebra and examples; the infinite-index, all-parameter assertions follow from the analytic bounds and sign certificates proved above.

## Relationship to prior work

Classical monotonicity-preserving linear multistep analysis gives the known general BDF2 positivity/monotonicity timestep restriction for suitable starts, and the backward-Euler-started scalar BDF2 sign-loss threshold \(r=1/2\) and delayed first negative index have already been obtained. This work does not claim either result anew. Li and Liao study variable-step BDF stability, not the present fixed-generator, all-iterate Markov-simplex condition. A published optimized two-step stiff-integrator family **contains standard BDF2 at its parameter value \(\kappa=0\)**, but its Markov-simplex classification quantifies over **arbitrary independent starting histories**. It excludes the standard BDF2 parameter under that stronger requirement, without deciding positivity for the specific backward-Euler-generated history. Its result therefore does not imply the present theorem. The present claim combines a sharp global lower envelope of the scalar BDF2 response with the rank-one stationary projector of an irreducible two-state exchange, yielding the necessary and sufficient all-step rate-imbalance frontier.

## Limitations

This result is for two states, positive rates, constant steps and the specifically prescribed backward-Euler starter. It is not a strong-stability-preservation theorem for general generators or arbitrary two-step input histories, and it does not establish the exact full set of admissible timesteps outside the rate-ratio frontier. Historical priority remains subject to specialist literature on cone-preserving multistep recurrences that might encode an equivalent result. The mathematical checks here are not an independent audit.

## References

1. W. Hundsdorfer, S. J. Ruuth and R. J. Spiteri, *Monotonicity-Preserving Linear Multistep Methods*, CWI report MAS-R0210 (public 2002-04-30), https://ir.cwi.nl/pub/4231/04231D.pdf.
2. Z. Li and H.-L. Liao, *Stability of Variable-Step BDF2 and BDF3 Methods*, first public arXiv version 2022-01-03, https://arxiv.org/abs/2201.00527v1.
3. *Exact delayed sign loss just beyond BDF2's positivity boundary*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-delayed-sign-loss-just-beyond-bdf2-s-positivity-boundary--cf66315c5a14.
4. *Exact positive-decay phase diagram for backward-Euler-started BDF2 on alternating time grids*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-positive-decay-phase-diagram-for-backward-euler-started-bd--34750bc994c5.
5. *A sharp seven-sixteenths stationary-balance frontier for two-step probability-simplex preservation*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-seven-sixteenths-stationary-balance-frontier-for-two-ste--8623505eab6d.
