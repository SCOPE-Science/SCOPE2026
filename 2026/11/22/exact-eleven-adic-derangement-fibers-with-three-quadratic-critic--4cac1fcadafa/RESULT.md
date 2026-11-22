# Exact eleven-adic derangement fibers with three quadratic critical branches

## Finding

Write \(D_0=1\) and \(D_n=nD_{n-1}+(-1)^n\) for the derangement numbers. For every \(k\ge1\) and residue \(y\pmod{11^k}\), let
\[
N_k(y)=\#\{0\le n<2\cdot11^k:D_n\equiv y\pmod{11^k}\}.
\]
The theorem below determines **every** \(N_k(y)\), at every level, using three explicitly specified eleven-adic critical values and ordinary square-root counts. In particular, for all \(k\ge1\),
\[
N_k(y)>0\quad\Longleftrightarrow\quad
 y\bmod11\in\{0,1,2,5,6,9,10\}.
\]
There are precisely \(7\cdot11^{k-1}\) attained residue classes modulo \(11^k\); the closure of the derangement values in \(\mathbb Z_{11}\) has Haar measure \(7/11\). Unlike the regular odd-prime examples, their fiber multiplicities are unbounded as \(k\) grows.

Here is the complete fiber formula. Define the locally analytic eleven-adic interpolation
\[
F(x)=\sum_{j\ge0}(-1)^j\prod_{i=0}^{j-1}(x-i),\qquad x\in\mathbb Z_{11}.
\]
For each integer \(a\in\{0,\ldots,10\}\), expand \(F(a+T)=\sum_{j\ge0}B_j(a)T^j\) near \(T=0\). Its three singular residue branches are
\[
\mathcal A=\{1,2,7\}.
\]
For each \(a\in\mathcal A\), there is a unique \(\tau_a\in\mathbb Z_{11}\) such that \(F'(a+11\tau_a)=0\). Set
\[
\gamma_a=F(a+11\tau_a),\qquad u_a=B_2(a)\in\mathbb Z_{11}^{\times}.
\]
These constants are uniquely determined by the convergent series above. Their initial exact digits are:

| \(a\) | \(B_1(a)/11\pmod {11}\) | \(u_a\pmod {11}\) | \(\tau_a\pmod {11}\) | \(\gamma_a\pmod {1331}\) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 8 | 2 | 121 |
| 2 | 9 | 6 | 2 | 1090 |
| 7 | 10 | 4 | 7 | 1050 |

For \(m\ge0\), let \(Q_m(w)\) be the number of square roots of \(w\) modulo \(11^m\), with \(Q_0=1\). It has the closed description
\[
Q_m(w)=\begin{cases}
11^{\lfloor m/2\rfloor},&w\equiv0\pmod{11^m},\\
2\cdot11^s,&\nu_{11}(w)=2s<m\text{ and the unit part of }w\text{ is a square modulo }11,\\
0,&\text{otherwise}.
\end{cases}
\]
(The second line applies only to nonzero residue classes.) Define \(\rho(0)=2\), \(\rho(1)=3\), \(\rho(5)=1\), \(\rho(9)=2\), and \(\rho(r)=0\) for other classes modulo eleven. For \(k\ge2\), define
\[
E_{a,k}(z)=\begin{cases}
11Q_{k-2}\!\left(u_a^{-1}\dfrac{z-\gamma_a}{121}\bmod11^{k-2}\right),&z\equiv\gamma_a\pmod{121},\\
0,&\text{otherwise}.
\end{cases}
\]
All quotients are taken in \(\mathbb Z_{11}\); the condition on the first line makes the quotient integral. The full formula, for **every** \(y\pmod{11^k}\), is
\[
\boxed{N_k(y)=\rho(y)+\rho(-y)+\sum_{a\in\mathcal A}\left(E_{a,k}(y)+E_{a,k}(-y)\right),\quad k\ge2.}
\]
For \(k=1\), put \(c(r)=\rho(r)+\mathbf1_{\{0,1,5\}}(r)\); then \(N_1(y)=c(y)+c(-y)\). In particular, the maximum \(N_k(y)\) is at least \(11^{1+\lfloor(k-2)/2\rfloor}\) for every \(k\ge2\): the critical fibers become arbitrarily large.

## Assumptions and scope

All indices are nonnegative integers, all congruences in this result use powers of the **fixed** prime eleven, and \(N_k\) counts one complete period of length \(2\cdot11^k\). No least-period assertion is needed. The interpolation \(F\), its Taylor coefficients, critical centers and square tests are exact eleven-adic objects, not floating-point approximations. This is a theorem about residue fibers, not a claim about the distribution of prime factors of \(D_n\) in general.

## Proof

**1. Interpolation and periodicity.** In every string of \(11k\) consecutive integers there are at least \(k\) multiples of eleven. Thus, for each \(x\in\mathbb Z_{11}\) and each \(k\ge1\), the summands of \(F(x)\) having index at least \(11k\) vanish modulo \(11^k\). The series converges uniformly, is one-Lipschitz and is analytic on the eleven-adic residue balls. For integral \(n\ge0\), every summand after index \(n\) vanishes, so \(F(n)=(-1)^nD_n\). Hence \(D_n\pmod{11^k}\) depends only on \(n\pmod{2\cdot11^k}\), and each \(x\pmod{11^k}\) occurs with both signs exactly once in that block.

For any \(a\pmod{11}\), write \(F(a+11t)=\sum_{j\ge0}11^jB_j(a)t^j\). The Taylor series is restricted: coefficients of degree \(j\) are divisible by \(11^j\). Indeed, the derivatives of falling factorials converge termwise, since removing at most \(j\) factors from a sufficiently long string still leaves arbitrarily many factors divisible by eleven.

**2. Exact branch certificate.** The following two vectors, indexed by \(a=0,1,\ldots,10\), are exact:
\[
(F(a)\bmod11)_a=(1,0,1,9,9,0,1,5,5,0,1),
\]
\[
(B_1(a)\bmod11)_a=(10,0,0,10,6,5,3,0,6,7,7).
\]
They follow by expanding the finite sum through falling-factorial index \(32\): when \(j\ge33\), every falling factorial contains at least three factors divisible by eleven, and removal of at most two factors leaves sufficient powers for the relevant constant, linear, or quadratic jet. The same integer recurrence computes \(B_1(a)\pmod{121}\) and \(B_2(a)\pmod{11}\). At \(a=1,2,7\), it gives the displayed critical table.

**3. Eight regular branches.** If \(B_1(a)\) is an eleven-adic unit, then
\[
(F(a+11t)-F(a))/11\equiv B_1(a)t\pmod{11}.
\]
Higher Taylor terms carry extra powers of eleven. Consequently the displayed map of \(t\) is an isometry and a bijection \(\mathbb Z_{11}\to\mathbb Z_{11}\), by one-digit-at-a-time lifting. Each regular source branch covers its entire target residue ball, with one preimage in that branch for every target modulo \(11^k\). Counting the eight regular branches by their target residues gives \(\rho\).

**4. Three quadratic branches.** For \(a\in\mathcal A\), \(B_1(a)\in11\mathbb Z_{11}\) while \(B_2(a)\) is a unit. Therefore
\[
H_a(t):=\frac{F(a+11t)-F(a)}{121}
\equiv\frac{B_1(a)}{11}t+B_2(a)t^2\pmod{11}.
\]
The derivative of this restricted analytic function is congruent to a nonconstant affine function with invertible slope \(2B_2(a)\). It has one and only one zero \(\tau_a\in\mathbb Z_{11}\), established by Hensel lifting. Expanding around that critical point yields
\[
H_a(\tau_a+s)-H_a(\tau_a)=s^2U_a(s),
\qquad U_a(s)\equiv B_2(a)\pmod{11}.
\]
The quotient \(U_a(s)/u_a\) belongs to \(1+11\mathbb Z_{11}\) and has a unique analytic square root congruent to one modulo eleven. Thus \(\phi_a(s)=s\sqrt{U_a(s)/u_a}\) is an eleven-adic isometry and bijection. This establishes the exact global normal form on each singular branch:
\[
F(a+11t)=\gamma_a+121u_a\phi_a(t-\tau_a)^2.
\]
To obtain \(F(x)\equiv z\pmod{11^k}\), the required square congruence is modulo \(11^{k-2}\). Since \(t\pmod{11^{k-1}}\) has eleven lifts of every class modulo \(11^{k-2}\), the number of preimages in this singular branch is precisely \(E_{a,k}(z)\). The standard valuation classification of squares gives the displayed formula for \(Q_m\).

**5. Combine signs and prove consequences.** Summing contributions of the eight regular and three critical branches gives the unsigned fiber law. The even/odd sign split yields \(N_k(y)=M_k(y)+M_k(-y)\), proving the formula. Every critical image stays inside a target ball already fully covered by at least one regular branch; therefore exactly the seven stated target residues occur at every level. Their Haar measure is \(7/11\). For \(z=\gamma_a\), the critical square congruence has \(11^{\lfloor(k-2)/2\rfloor}\) roots; including its eleven index lifts proves the claimed unbounded fiber lower bound.

## Verification

The standalone file `check.py` computes Taylor jets by exact modular integer recurrences (not numerical differentiation), checks all three critical centers modulo eleven, and independently enumerates the classical derangement recurrence on complete blocks. It compares **all** residue fibers to the formula for \(k=1,2,3,4,5,6\), respectively covering \(11,121,1331,14641,161051,1771561\) distinct target residues and \(22,242,2662,29282,322102,3543122\) input indices. Exact counts of attained residues are \(7,77,847,9317,102487,1127357\); maximum fibers at these levels are \(6,26,48,125,246,1335\). The infinite theorem follows from the arguments above, not from this finite experiment.

## Relationship to prior work

Miska established recurrence, periodicity, and valuation/Hensel tools for derangements. O'Desky and Richman established a general locally analytic interpolation of derangement-like polynomials, including the convergent falling-factorial series underlying \(F\). These **general tools are prior results**. The claim here is the specifically evaluated eleven-adic three-critical-branch geometry and the resulting exact prime-power residue-fiber function. Previously studied prime two, three, five and seven fibers are distinct parameter cases and do not imply this numerical classification without additional analysis. The possibility of a stronger, unindexed general fiber theorem remains a priority limitation.

## Limitations

The result does not settle the analogous fibers for other primes or claim a new general interpolation theorem. The three constants \(\gamma_a,u_a\) are given by exact convergent eleven-adic constructions, with initial digits and an algorithm, rather than closed rational integers. The computed tests only reach level six; unrestricted validity relies on the proved analytic normal form. Historical originality is based on inspected sources and mathematical-index searches, not an exhaustive proof of first discovery. Independent audit has not been performed.

## References

- P. Miska, *Arithmetic Properties of the Sequence of Derangements and its Generalizations*, first public arXiv version dated 2015-08-09, https://arxiv.org/abs/1508.01987 (especially the recurrence and Sections 3–4 on modular periodicity and Hensel lifting).
- A. O'Desky and D. H. Richman, *Derangements and the p-adic incomplete gamma function*, first public arXiv version dated 2020-12-08, https://arxiv.org/abs/2012.04615 (especially Theorems 4.3 and 4.5 on local analyticity and the falling-factorial interpolation).
