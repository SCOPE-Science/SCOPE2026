# Exact collision reversal for cubic maps over odd prime-power rings

## Finding
Let \(p\) be an odd prime, \(k\ge1\), and \(c\in\mathbb Z\) with \(p\nmid c\). Put \(f_c(x)=x^3+cx\) and define the ordered equal-value collision count
\[
C_{p,k}(c)=\#\{(x,y)\in(\mathbb Z/p^k\mathbb Z)^2:f_c(x)\equiv f_c(y)\pmod{p^k}\}.
\]
Equivalently, if \(N_{p,k,c}(z)=\#\{x\bmod p^k:f_c(x)\equiv z\pmod{p^k}\}\), then \(C_{p,k}(c)=\sum_{z\bmod p^k}N_{p,k,c}(z)^2\).

For \(p\ge5\), let \(\chi_p\) be the Legendre character, and set \(\varepsilon_p=\chi_p(-3)\) and \(\eta_{p,c}=\chi_p(-c/3)\), where division is in \(\mathbb F_p\). Then **at every exponent**
\[
\boxed{C_{p,k}(c)=p^{k-1}\left(2p-\varepsilon_p+(1+\eta_{p,c})\big((k-1)(p-1)-1\big)\right).}
\]
For the exceptional odd prime \(p=3\), the exact formula is
\[
\boxed{C_{3,k}(c)=\begin{cases}3^k,&c\equiv1\pmod3,\\3^{k+1},&c\equiv-1\pmod3.\end{cases}}
\]

For fixed \(p\ge5\), changing \(\eta_{p,c}\) from \(-1\) to \(+1\) changes the collision count by exactly
\[
\Delta_{p,k}=2p^{k-1}\big((k-1)(p-1)-1\big).
\]
Thus the class with two critical points has **two fewer collisions modulo \(p\)** but **strictly more collisions modulo every \(p^k\) with \(k\ge2\)**. In particular the normalized collision count \(C_{p,k}(c)/p^k\) is constant in \(k\) when \(\eta_{p,c}=-1\), but grows linearly in \(k\) when \(\eta_{p,c}=+1\).

## Assumptions and scope
All variables \(x,y,z\) range over complete residue systems modulo the specified prime power; collisions are ordered and include \(x=y\). The coefficient \(c\) may depend on \(p\) and \(k\), but must remain a unit modulo \(p\). The result holds uniformly for **all odd primes** and **all positive exponents**, not only for primes where the cubic has a particular number of finite-field values. It does not claim any formula for \(p=2\) or for coefficients divisible by \(p\). For \(p\ge5\), the polynomial is the third Dickson polynomial \(D_3(x,a)=x^3-3ax\) with \(a=-c/3\).

## Proof
**1. Reduce collisions to a plane divisor.** In the polynomial ring over the integers,
\[
f_c(x)-f_c(y)=(x-y)(x^2+xy+y^2+c).
\]
Call the two factors \(L=x-y\) and \(Q=x^2+xy+y^2+c\). For every \(p\ge5\), the line \(L=0\) has \(p\) points over \(\mathbb F_p\). The affine conic \(Q=0\) has
\[
\#Q(\mathbb F_p)=\sum_{x\bmod p}\left(1+\chi_p(-3x^2-4c)\right)=p-\chi_p(-3).
\]
The last equality follows from the elementary quadratic-character identity \(\sum_x\chi_p(x^2-d)=-1\) for \(d\ne0\): count the pairs satisfying \(v^2=x^2-d\) by factoring \((x-v)(x+v)=d\), which has \(p-1\) solutions.

**2. Identify exactly the transverse crossings.** The two components meet at \(x=y=a\) with \(3a^2+c=0\). Hence their number is
\[
I=1+\chi_p(-c/3)\in\{0,2\}.
\]
At a crossing \(a\ne0\), so the Jacobian determinant of \((L,Q)\) with respect to \((x,y)\) is \(6a\not\equiv0\pmod p\). Thus on the residue disk of each crossing the coordinate change \((x,y)\mapsto(u,v)=(L,Q)\) gives a bijection onto \((p\mathbb Z_p)^2\); concretely, substitute \(y=x-u\) to get \(v=3x^2-3xu+u^2+c\), which has derivative \(6a\not\equiv0\pmod p\) in \(x\), so the one-variable Hensel lemma gives the claimed unique lift for every \(u,v\) in the target disk. The conic is smooth at every other point because its two partial derivatives vanish together only at \((0,0)\), and \(Q(0,0)=c\ne0\). Each point of exactly one smooth component therefore admits precisely \(p^{k-1}\) lifts of \(LQ=0\pmod{p^k}\).

**3. Count the crossing fibers, not merely the branches.** At a fixed crossing modulo \(p\), the number of pairs \((u,v)\in(p\mathbb Z/p^k\mathbb Z)^2\) with \(uv\equiv0\pmod{p^k}\) equals
\[
p^{k-1}+(k-1)(p-1)p^{k-1}=p^{k-1}\big(1+(k-1)(p-1)\big).
\]
Indeed, \(u=0\) allows \(p^{k-1}\) values of \(v\). For each valuation \(1\le r<k\), there are \((p-1)p^{k-r-1}\) choices of \(u\) and \(p^r\) choices of \(v\), contributing \((p-1)p^{k-1}\) for each \(r\). This count includes \(k=1\) via the empty sum.

There are \(p+(p-\varepsilon_p)-2I\) finite-field points on exactly one of the two smooth components. Adding their lifts and the contributions of \(I\) crossings yields
\[
\begin{aligned}
C_{p,k}(c)
&=p^{k-1}\big(p+p-\varepsilon_p-2I+I[1+(k-1)(p-1)]\big)\\
&=p^{k-1}\big(2p-\varepsilon_p+I[(k-1)(p-1)-1]\big),
\end{aligned}
\]
which is the asserted formula. Subtracting the two values \(I=2\) and \(I=0\) gives the exact sign reversal: \(\Delta_{p,1}=-2\) and \(\Delta_{p,k}>0\) for \(k\ge2\).

**4. The exceptional prime three.** For any unit \(c\in\mathbb Z_3\), if \(x\equiv y\pmod3\) then
\[
\frac{f_c(x)-f_c(y)}{x-y}=x^2+xy+y^2+c\equiv c\not\equiv0\pmod3.
\]
Thus the restriction of \(f_c\) to each of the three input residue disks is a distance-preserving bijection onto its corresponding output disk. Modulo three, \(f_c(x)\equiv(1+c)x\). When \(c\equiv1\), these disks map to three distinct target disks and \(f_c\) is a permutation modulo each \(3^k\); hence \(C_{3,k}(c)=3^k\). When \(c\equiv-1\), all three source disks map bijectively onto the one disk \(3\mathbb Z_3\); each of its \(3^{k-1}\) residue targets has three preimages and all other targets have none. Therefore \(C_{3,k}(c)=9\cdot3^{k-1}=3^{k+1}\).

## Verification
An independent standard-library implementation is included as `verify_cubic.py`. Run `python3 verify_cubic.py`. It independently enumerates full residue-to-fiber histograms for \(474\) combinations drawn from \(p\in\{3,5,7,11,13,17\}\), several exponents and three integer lifts of each unit coefficient modulo \(p\). Its largest tested modulus is \(6561\). For all tested moduli at most \(100\), it additionally counts all ordered pairs directly, without reusing the histogram method. It separately verifies the phase-difference formula at four exponents for five primes. These checks are finite corroboration; the preceding argument proves all permitted parameters.

## Relationship to prior work
Fang, Fernando and Wu (arXiv:2307.06325, first public July 12, 2023) study permutation behavior, fixed points and cycle types of reversed Dickson polynomials, and recall classical Dickson polynomials and the prime-power permutation criterion. The present cubic collision statistic is different from a permutation or cycle classification. Sun (2003) studies cubic and quartic root counts modulo a single prime, not the exact total equal-value count at every prime-power depth. DesJardins and Zieve (arXiv:math/0103046) develop cycle-lifting dynamics for general polynomial maps modulo odd prime powers, rather than this target-summed collision law. Indexed mathematical comparisons included cubic Dickson iteration modulo powers of three at a nonunit coefficient and quartic equal-value collision counts; neither implies the stated all-unit-coefficient cubic result. The proof here is self-contained and does not assume novelty from a failed database search.

## Limitations
The result computes the second moment of fiber multiplicities, not their complete distribution for each target, and is restricted to odd primes and unit coefficients. It does not establish an exact novelty guarantee against all unpublished, unindexed or implicit local-zeta calculations. The polynomial's nonunit-coefficient behavior (especially at the ramified primes) is outside the theorem. No independent mathematical audit is claimed.

## References
1. J. Fang, N. Fernando, H. Wu, *Reversed Dickson polynomials*, arXiv:2307.06325 (2023), https://arxiv.org/abs/2307.06325.
2. Z.-H. Sun, *Cubic and quartic congruences modulo a prime*, J. Number Theory 102 (2003), https://doi.org/10.1016/S0022-314X(03)00067-2.
3. D. L. desJardins, M. E. Zieve, *On the Structure of Polynomial Mappings Modulo an Odd Prime Power*, arXiv:math/0103046, https://arxiv.org/abs/math/0103046.
