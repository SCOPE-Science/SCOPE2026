# Ten quadratic eleven-adic sheets in the ten-step Tribonacci gaps

## Finding

Let \(T_0=T_1=0\), \(T_2=1\), and \(T_{n+3}=T_{n+2}+T_{n+1}+T_n\) for every \(n\ge0\). Put \(D_n=T_{n+10}-T_n\). For every \(r\in\{0,\ldots,9\}\) there exist a unique \(\tau_r\in\mathbb Z_{11}\), a critical value \(A_r\in\mathbb Z_{11}\), and a bijective isometry \(u_r:\mathbb Z_{11}\to\mathbb Z_{11}\) such that for every \(t\in\mathbb Z_{11}\),
\[
D_{10t+r}=A_r+11\,(3\cdot7^r)u_r(t)^2.
\]
Here the left-hand side is the unique continuous extension from nonnegative integers of the indicated subsequence. The critical values are constructively defined in the proof and satisfy \(A_r\equiv4\cdot7^r\pmod{11}\); these ten residue classes are distinct. Consequently, for all \(k\ge1\), the set \(I_k\) of gap values modulo \(11^k\) is exactly the reduction of the following *disjoint* union:
\[
\overline{\{D_n:n\ge0\}}^{(11)}
=\bigsqcup_{r=0}^9\left(A_r+11(3\cdot7^r)\mathbb Z_{11}^{\,2}\right).
\]
The least period of \((D_n\bmod11^k)\) is \(10\cdot11^{k-1}\). Writing \(S_0=1\), and, for \(m\ge1\),
\[
S_m=1+5\sum_{j=0}^{\lfloor(m-1)/2\rfloor}11^{m-2j-1},
\]
the exact image cardinality is
\[
|I_k|=10S_{k-1}.
\]
In the least period, the multiplicity of a residue \(y\) belonging to sheet \(r\) equals the number of square roots modulo \(11^{k-1}\) of
\[
(y-A_r)/(11\cdot3\cdot7^r).
\]
Here division by \(11\) is interpreted after choosing the unique sheet with \(y\equiv A_r\pmod{11}\), and the quotient is taken modulo \(11^{k-1}\). Every residue with \(11\mid y\) is absent. The closure has normalized Haar measure
\[
\boxed{\mu\left(\overline{\{D_n:n\ge0\}}^{(11)}\right)=\frac5{12}.}
\]

## Assumptions and scope

All integer indices \(n,t\) are nonnegative unless otherwise specified. The \(11\)-adic integers are denoted \(\mathbb Z_{11}\); \(\mathbb Z_{11}^{\,2}=\{z^2:z\in\mathbb Z_{11}\}\). The prime \(11\), the lag \(10\), and the ordinary impulse-initialized Tribonacci recurrence are fixed. All statements about images, root multiplicities, least periods, and Haar measure are exact at every positive modulus depth and at the inverse limit. No assertion is made for other lags or primes.

## Proof

**1. Exact companion-matrix identities.** Define
\[
Q=\begin{pmatrix}0&1&0\\0&0&1\\1&1&1\end{pmatrix},\qquad
X=Q^{10}-I=\begin{pmatrix}43&68&81\\81&124&149\\149&230&273\end{pmatrix},\qquad e=(0,0,1)^\mathsf T.
\]
Then \(T_n=e_1^\mathsf TQ^ne\) and \(D_{10t+r}=e_1^\mathsf TQ^r(I+X)^tXe\). The following identities are obtained by exact integer multiplication; the standalone checker independently verifies the necessary congruences:
\[
N=X\bmod11=\begin{pmatrix}10&2&4\\4&3&6\\6&10&9\end{pmatrix},
\quad N^2=0\pmod{11},\quad QN=7N\pmod{11},
\quad X^3/11=7N\pmod{11}.
\]
The entries of \(X^2\) and \(X^3\) are all divisible by \(11\), and the entries of \(X^4\) by \(121\). In particular \(X^{2j}\) and \(X^{2j+1}\) are divisible entrywise by \(11^j\). For every \(r\), the value \(D_{10t+r}\bmod11\) is therefore independent of \(t\) and equals \(4\cdot7^r\); since \(7\) has multiplicative order \(10\pmod{11}\), these ten residues are pairwise distinct.

**2. Integral analytic interpolation.** Since the powers of \(X\) tend to zero \(11\)-adically, the Mahler-binomial series
\[
F_r(t)=e_1^\mathsf TQ^r\left(\sum_{i\ge0}\binom ti X^i\right)Xe
\]
converges for every \(t\in\mathbb Z_{11}\) and agrees with \(D_{10t+r}\) for nonnegative integer \(t\). Each \(\binom ti\in\mathbb Z_{11}\). Define \(f_r(t)=(F_r(t)-F_r(0))/11\). Set
\[
\alpha_r=e_1^\mathsf TQ^r(X^2/11)e,
\qquad \beta_r=e_1^\mathsf TQ^r(X^3/11)e.
\]
Both are integers, and an exact expansion gives
\[
f_r(t)=\alpha_rt+\beta_r\binom t2+11H_r(t),\qquad H_r\in\mathbb Z_{11}\langle t\rangle.
\]
Here \(\mathbb Z_{11}\langle t\rangle\) is the ring of restricted power series with \(11\)-integral coefficients tending to zero. To justify the last assertion rather than relying on formal notation, the \(i\)-th remaining Mahler term for \(i\ge3\) has the form \(c_{r,i+1}\binom ti/121\) with \(\nu_{11}(c_{r,i+1})\ge\lfloor(i+1)/2\rfloor\). Expansion into powers of \(t\) introduces at worst the denominator \(i!\). The bound \(\lfloor(i+1)/2\rfloor-2-\nu_{11}(i!)\ge0\) for every \(i\ge3\), tending to infinity, proves integral analytic convergence of the tail. Because \(X^3/11\equiv7N\pmod{11}\),
\[
\beta_r\equiv 6\cdot7^r\pmod{11},\qquad
f_r(t)\equiv\alpha_rt+(6\cdot7^r)\binom t2\pmod{11}.
\]
In particular its quadratic leading coefficient is the unit \(\lambda_r=3\cdot7^r\in\mathbb Z_{11}^\times\).

**3. A global \(11\)-adic quadratic normal form.** The derivative \(f_r'(t)\pmod{11}\) is a linear polynomial of nonzero slope \(6\cdot7^r\). Hensel lifting gives one and only one \(\tau_r\in\mathbb Z_{11}\) with \(f_r'(\tau_r)=0\). Let \(a_r=f_r(\tau_r)\) and \(\lambda_r=3\cdot7^r\). Since the linear term of the Taylor expansion at \(\tau_r\) vanishes, division by the square of \(t-\tau_r\) in the restricted power-series ring yields
\[
f_r(t)-a_r=\lambda_r(t-\tau_r)^2(1+11K_r(t)),\qquad K_r\in\mathbb Z_{11}\langle t\rangle.
\]
The factor \(1+11K_r(t)\) has its uniquely specified square root \(1+11L_r(t)\) in the same ring, defined by the convergent binomial series. Hence
\[
u_r(t)=(t-\tau_r)(1+11L_r(t))
\]
satisfies \(f_r(t)=a_r+\lambda_r u_r(t)^2\). The restricted power series \(L_r\) is \(1\)-Lipschitz, so \(u_r(t)-u_r(s)\) equals \((t-s)\) times a \(11\)-adic unit for all distinct \(s,t\). Therefore \(u_r\) preserves every \(11\)-adic distance and induces an injection, hence a permutation, on every finite quotient \(\mathbb Z/11^k\mathbb Z\). It is consequently surjective on \(\mathbb Z_{11}\). Defining \(A_r=F_r(0)+11a_r\) proves the advertised identity, and \(A_r\equiv4\cdot7^r\pmod{11}\) follows from step 1.

**4. Images, fibers, and least periods.** By density of nonnegative integers in \(\mathbb Z_{11}\), each of the ten image sheets is exactly \(A_r+11\lambda_r\mathbb Z_{11}^{\,2}\), with disjointness forced by their reductions modulo \(11\). Since \(u_r\) permutes every residue class ring, the fiber count on the \(r\)-th branch is precisely the square-root multiplicity modulo \(11^{k-1}\). A square modulo \(11^m\) is either zero, or has valuation \(2j<m\) and a square leading unit, contributing \(5\cdot11^{m-2j-1}\) distinct residues at that valuation. Adding the zero class gives \(S_m\) and the image formula.

The gap sequence modulo \(11\) cycles through ten distinct nonzero residues, so a period is divisible by \(10\). Its subsequence \(F_r(t)=F_r(0)+11f_r(t)\) is periodic modulo \(11^k\) with \(t\)-period \(11^{k-1}\), by the integral analytic expansion. To prove minimality, if \(q\not\equiv0\pmod{11}\), then \(f_r(t+q)-f_r(t)\) is a nonzero affine function of \(t\pmod{11}\), since the quadratic leading coefficient is a unit. If \(11\mid q\), Taylor's formula at a point where \(f_r'(t)\) is a unit shows \(\nu_{11}(f_r(t+q)-f_r(t))=\nu_{11}(q)\). Thus no smaller positive shift in \(t\) is a period modulo \(11^{k-1}\), proving \(10\cdot11^{k-1}\) is the least \(n\)-period. Finally, the normalized Haar measure of \(\mathbb Z_{11}^{\,2}\) is
\[
\sum_{j\ge0}\frac5{11}\,11^{-2j}=\frac{11}{24}.
\]
Every sheet is an affine image scaled by \(11\), hence has measure \(1/24\). The ten disjoint sheets have total measure \(10/24=5/12\), as asserted.

## Verification

Run `python3 check.py` with a standard Python 3 interpreter. The checker uses exact integers and verifies the companion-matrix congruences, nonzero quadratic leading coefficients for all ten branches, complete residue histograms and square-root fiber-size bounds at depths \(1\) through \(5\), and the failure of the preceding candidate period at each tested depth. The observed image cardinalities at depths \(1,2,3,4,5\) are respectively \(10,60,560,6110,67110\). These finite checks do not prove any infinite statement; the analytic and algebraic arguments above supply the proof.

## Relationship to prior work

Klaška, *Tribonacci modulo \(2^t\) and \(11^t\)* (2008), proves exact periods of all generalized Tribonacci recurrences and supplies the relevant companion-matrix lifting identities (especially Lemma 3.1 and Theorem 3.10). In particular, its period theorem applies to this lag-ten difference recurrence. Its statements and proof do **not** classify the attainable values of the difference recurrence, their complete prime-power fibers, or the ten quadratic critical-value sheets; the present argument derives a new integral analytic quadratic normal form beyond the period classification. Catalani (2002) supplies related characteristic-root background. Baker–Luca–Porrill (2026) studies \(11\)-adic zeros of the *original* Tribonacci sequence, not the complete image and fibers of ten-step gaps. A published result on the ordinary Tribonacci sequence's \(2\)-adic image concerns a different prime and a different sequence. No independence or external certification is claimed.

## Limitations

The result does not assert anything for other lags or primes, nor any optimal first positive index representing a given residue. The values \(A_r\) are defined constructively by unique \(11\)-adic Hensel roots; no simple closed integer expression for them is claimed. Historical priority has residual risk from general \(p\)-adic distribution and Morse-normal-form literature. The exact residue theorem is proved in this manuscript and supported by finite reproduction, but has not undergone independent mathematical validation.

## References

1. M. Catalani, *On the roots of the cubic defining the Tribonacci sequences*, arXiv:math/0209265, publicly submitted 2002-09-20. https://arxiv.org/abs/math/0209265
2. J. Klaška, *Tribonacci modulo \(2^t\) and \(11^t\)*, Mathematica Bohemica 133 (2008), 377–387. DOI: 10.21136/MB.2008.140627. https://dml.cz/manakin/handle/10338.dmlcz/140627
3. L. Baker, F. Luca and K. Porrill, *On periods of the Tribonacci sequence modulo primes*, arXiv:2609.22364, 2026-09-17. https://arxiv.org/abs/2609.22364
4. *The complete dyadic value image and seven-twelfths density of Tribonacci numbers*, published research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-complete-dyadic-value-image-and-seven-twelfths-density-of-tr--a24da7d7968e
