# Exact Franel-support additive energy and a near-critical five-adic convolution dimension

## Finding

For the Franel numbers \(F_n=\sum_{j=0}^n\binom nj^3\) and every integer \(r\ge0\), define
\[
 A_r=\{0\le n<5^r:5\nmid F_n\},\qquad
 E_r=\#\{(a,b,c,d)\in A_r^4:a+b=c+d\}.
\]
All four elements in the energy are ordered, repetition is permitted, and the equality is of ordinary integers, not residues. The complete sequence of energies has the exact generating function
\[
 \boxed{\sum_{r\ge0}E_rz^r=\frac{1-23z}{1-59z+380z^2}.}
\]
In particular \(E_0=1\), \(E_1=36\), and
\[
 \boxed{E_{r+2}=59E_{r+1}-380E_r\quad(r\ge0).}
\]
The first terms are \(1,36,1744,89216,4601024,237558336\). Although the finite set has an interval as its complete ordinary twofold sumset,
\[
 \boxed{A_r+A_r=\{0,1,\ldots,2(5^r-1)\}\quad(r\ge0),}
\]
its sum-representation multiplicities become increasingly nonuniform. Set
\[
 \lambda_\pm=\frac{59\pm\sqrt{1961}}2,\qquad
 c_\pm=\frac{\sqrt{1961}\pm13}{2\sqrt{1961}}.
\]
Then the exact formula is \(E_r=c_+\lambda_+^r+c_-\lambda_-^r\), where \(\lambda_+>256/5\); hence
\[
 \frac{(2\cdot5^r-1)E_r}{256^r}
 \sim 2c_+\left(\frac{5\lambda_+}{256}\right)^r\longrightarrow\infty.
\]
This ratio compares actual energy with the Cauchy--Schwarz lower bound coming from the full sumset.

For the associated continuous probability measure, let \(\mu\) be the law of
\[
 X=\sum_{j=1}^\infty\xi_j5^{-j},\qquad
 \mathbb P(\xi_j=d)=\tfrac14\quad(d\in\{0,1,3,4\}),
\]
with independent digits, and put \(\nu=\mu*\mu\). Using the five-adic grid definition
\[
 D_2(\nu)=\lim_{r\to\infty}
 -\frac{\log\sum_{k\in\mathbb Z}\nu([k5^{-r},(k+1)5^{-r}))^2}{r\log5},
\]
the limit exists and is exactly
\[
 \boxed{D_2(\nu)=\frac{\log(256/\lambda_+)}{\log5}
 =0.994664087319881\ldots<1.}
\]
Consequently \(\nu\) has no density in \(L^2(\mathbb R)\). Neither singularity nor the absence of densities in other \(L^p\) spaces is asserted.

## Assumptions and scope

The congruence is modulo the prime five; \(n,r\) are nonnegative integers, and \(F_n\) is an ordinary integer. The empty base-five word is included, so \(A_0=\{0\}\). The convolution is the ordinary convolution of independent real random variables, not convolution on a finite residue ring. Every energy identity holds for each integer depth, not merely asymptotically. The logarithms are real and natural. No unproved hypothesis or numerical stabilization assumption is used.

The role of the Franel numbers is arithmetic rather than decorative: Lucas's binomial congruence gives exactly the four-digit support below, so the energy counts additive coincidences among nondivisible terms in every complete prime-power index block. This converts a one-variable divisibility condition into a four-variable additive invariant.

## Proof

**1. Franel support by Lucas congruence.** For \(0\le a<5\), write \(n=5m+a\). Lucas's theorem yields
\[
 \binom{5m+a}{5j+b}\equiv\binom mj\binom ab\pmod5
 \qquad(0\le b<5).
\]
Cubing and summing over all \(j,b\) (with zero binomial values outside the allowed index range) proves
\[
 F_{5m+a}\equiv F_mF_a\pmod5.
\]
A direct exact calculation gives
\[
 (F_0,F_1,F_2,F_3,F_4)=(1,2,10,56,346),
\]
whose modulo-five residues are \((1,2,0,1,1)\). Thus \(5\nmid F_n\) if and only if *no base-five digit of \(n\) equals two*. Precisely,
\[
 A_r=\left\{\sum_{j=0}^{r-1}d_j5^j:d_j\in D\right\},
 \qquad D=\{0,1,3,4\},\quad |A_r|=4^r.
\]

**2. Exact carry states.** Put \(C_s=\#\{(a,b)\in D^2:a+b=s\}\). For two sums to agree, their digitwise difference \(a+b-c-d\) at each place and an incoming signed carry \(i\) must satisfy
\[
 a+b-c-d+i=5j.
\]
Since the digit differences lie in \([-8,8]\), all admissible carries lie in \(\{-1,0,1\}\). Enumerating the sixteen ordered digit pairs on each side defines
\[
 T_{i,j}=\#\{(a,b,c,d)\in D^4:a+b-c-d+i=5j\},
 \quad i,j\in\{-1,0,1\}.
\]
In the stated carry order, exact digit enumeration gives
\[
 \boxed{T=\begin{pmatrix}17&28&6\\8&36&8\\6&28&17\end{pmatrix}.}
\]
The initial and final carries must both be zero: if the final carry is nonzero, the two integer sums differ by a nonzero multiple of \(5^r\). Thus the bijective digit enumeration proves
\[
 E_r=(T^r)_{0,0},
\]
where the index zero denotes the *middle* row and column, for all \(r\ge0\), including \(r=0\).

**3. Resolvent, recurrence and exact growth.** Reflection interchanges the signed carry states. The middle basis vector lies in the two-dimensional reflection-even subspace \((x,y,x)\), where \(T\) acts by
\[
 B=\begin{pmatrix}23&28\\16&36\end{pmatrix},\qquad
 \det(tI-B)=t^2-59t+380.
\]
Therefore \(E_{r+2}=59E_{r+1}-380E_r\) by Cayley--Hamilton, and \(E_0=1,E_1=36\). Multiplying the formal series by its recurrence denominator gives the claimed numerator \(1-23z\). Solving the recurrence yields the displayed \(c_\pm\) and \(\lambda_\pm\); both coefficients are positive and \(0<\lambda_-<\lambda_+\). For an exact proof of the critical strict inequality, the characteristic polynomial at \(256/5\) equals
\[
 (256/5)^2-59(256/5)+380=-484/25<0.
\]
Hence \(\lambda_+>256/5\), without relying on decimals.

**4. Full twofold sumset.** A direct digit check gives \(D+D=\{0,1,\ldots,8\}\), hence \(A_1+A_1=[0,8]\cap\mathbb Z\). Suppose for \(r\ge1\) that \(A_r+A_r=[0,2(5^r-1)]\cap\mathbb Z\). Writing the *leading* digit separately gives
\[
 A_{r+1}+A_{r+1}
 =\bigcup_{t=0}^8\bigl(t5^r+(A_r+A_r)\bigr).
\]
Each shifted interval has endpoint width \(2(5^r-1)\), and consecutive starts differ by \(5^r\). For \(r\ge1\) these intervals overlap or touch, and their union is precisely \([0,2(5^{r+1}-1)]\cap\mathbb Z\). The case \(r=0\) is immediate. By Cauchy--Schwarz, \(E_r\ge|A_r|^4/|A_r+A_r|=256^r/(2\cdot5^r-1)\); substitution of the exact spectral formula proves the divergence asserted above.

**5. Continuous convolution and grid masses.** The distribution \(\mu\) is nonatomic: prescribing the first \(r\) independent digits has probability \(4^{-r}\), and at most two base-five expansions can describe any single number. Let \(X,Y\) be independent with law \(\mu\). Their digit reflection \(d\mapsto4-d\) gives \(X\overset{d}=1-X\), so \(W=X+Y\overset{d}=2-W\). As \(W\) is nonatomic, \(\mathbb P(W<1)=\mathbb P(W>1)=1/2\).

Let \(w_{r,k}=16^{-r}\#\{(a,b)\in A_r^2:a+b=k\}\), extended as zero outside the finite support. Splitting \(X,Y\) after their first \(r\) digits expresses \(5^r(X+Y)\) as their integer prefix sum plus an independent tail \(W\) with the same law. Consequently the mass \(v_{r,k}=\nu([k5^{-r},(k+1)5^{-r}))\) satisfies exactly
\[
 v_{r,k}=\frac{w_{r,k}+w_{r,k-1}}2.
\]
Nonnegativity of \(w\) and the elementary shift inequality on \(\ell^2(\mathbb Z)\) give
\[
 \boxed{\frac{E_r}{2\cdot256^r}\le
 \sum_kv_{r,k}^2\le\frac{E_r}{256^r}.}
\]
Since \(E_r\sim c_+\lambda_+^r\) with \(c_+>0\), taking logarithms, dividing by \(r\log5\), and passing to the limit proves the claimed exact grid correlation dimension. Standard fixed-neighbor comparisons show that changing a grid to covering intervals or arbitrary small scales does not change this exponent.

Finally, if \(\nu=h(x)\,dx\) with \(h\in L^2(\mathbb R)\), Cauchy--Schwarz on each length-\(5^{-r}\) grid cell would give
\[
 5^r\sum_kv_{r,k}^2\le\|h\|_2^2\qquad(r\ge0).
\]
The proven lower bound instead grows asymptotically as a positive constant times \((5\lambda_+/256)^r\), whose base exceeds one. This contradiction excludes an \(L^2\) density.

## Verification

The standalone dependency-free `CHECK.py` independently constructs the three-state carry matrix from the sixteen ordered digit pairs per side, checks its even-sector characteristic polynomial and its exact recurrence through depth thirteen, computes the actual Franel residues by binomial sums for the first 513 indices, and independently enumerates every ordered pair and its sum for the first six depths (1,118,481 pairs in total). The exact counts, full-sumset property and arithmetic digit criterion agree. Its output begins `VERIFY_OK`. Reproduce with `python3 CHECK.py`.

These finite tests are *not* a proof of the all-depth statements. The proofs are Lucas's congruence, the complete finite carry-state identity, exact matrix algebra, the induction for the sumset and the analytic grid-mass comparison. The correlation dimension and absence of an \(L^2\) density are mathematical consequences of those identities, not numerical extrapolations.

## Relationship to prior work

Lucas's classical binomial congruence, and its Franel application discussed by Sun and by Malik--Straub, supply the digit-support premise. The appendix of Ash, Catoiu and Ríos-Collantes-de-Terán explicitly considers the same four-digit base-five Cantor set and establishes its interval twofold sumset, **so that full-sumset property is prior work**, used here only to contrast with exact representation nonuniformity. Wu develops general finite-type matrix and \(L^q\) dimension methods, but the inspected source does not evaluate this Franel-index energy sequence.

An especially close published comparison is the exact additive-energy and \(L^2\)-dimension calculation for a *three-digit base-four* self-convolution; it applies a similar carry-matrix technique to a different measure and gives a different characteristic polynomial. The present contribution is not a new generic carry method, and no general theorem is claimed. It is the specific evaluated, all-depth arithmetic invariant of the Franel nondivisibility support and its strict near-critical convolution consequence. Related exact dyadic energy work likewise treats a different digit-parity support. Unindexed older evaluations or a covering general theorem remain originality risks.

## Limitations

The numerical value of \(D_2\) is exact only for the displayed uniform self-convolution and the specified digit set; the work does not classify all digit alphabets, higher moments, other Franel moduli, or arbitrary truncation lengths. The non-\(L^2\) result alone does not determine singularity or any optimal \(L^p\) threshold. The full-sumset identity is credited to earlier work, not presented as new. The transfer-matrix technique is established. Novelty is a scoped comparison with identified literature, not proof that no implicit or unindexed evaluation exists. Independent mathematical validation has not been performed.

## References

1. Z.-W. Sun, *Congruences for Franel numbers*, arXiv:1112.1034, first posted 2011-12-05, https://arxiv.org/abs/1112.1034.
2. A. Malik and A. Straub, *Divisibility properties of sporadic Apéry-like numbers*, arXiv:1508.00297, first posted 2015-08-03, https://arxiv.org/abs/1508.00297.
3. J. M. Ash, I. Catoiu and M. Ríos-Collantes-de-Terán, *On the nth quantum derivative*, Appendix, Theorem 2, https://math.depaul.edu/mash/quant-n.pdf.
4. Y.-F. Wu, *Matrix representations for some self-similar measures on \(\mathbb R^d\)*, arXiv:2201.01909, first posted 2022-01-06, https://arxiv.org/abs/2201.01909.
5. *Exact correlation dimension and an \(L^2\) obstruction for a three-digit four-adic convolution*, published research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-correlation-dimension-and-an-l-obstruction-for-a-three-dig--0a6383f8b10e/RESULT.md.
6. *Exact dyadic additive energy of the evil-number set*, published research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-dyadic-additive-energy-of-the-evil-number-set--135609b4a49e/RESULT.md.
