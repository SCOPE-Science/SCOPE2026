# Cubic Fourier moments and elliptic exceptional ratios for two finite-field hyperbola shells

## Finding

Let \(F=\mathbb F_q\) be an **odd** finite field, let \(\lambda\in F^\times\setminus\{1\}\), and put
\[
H_u=\{(x,u/x):x\in F^\times\},\qquad S_\lambda=H_1\cup H_\lambda\subseteq F^2.
\]
Write \(\chi:F\to\{-1,0,1\}\) for the quadratic character, extended by \(\chi(0)=0\), and set
\[
a=\chi(-3),\quad b=\chi(1-4\lambda),\quad c=\chi(\lambda(\lambda-4)).
\]
For ordered additive convolution, the **three-step return count** and the unnormalized-Fourier cubic moment are exactly
\[
\boxed{(\mathbf1_{S_\lambda}^{*3})(0,0)=(q-1)(8+2a+3b+3c)
=\frac1{q^2}\sum_{\xi\in F^2}\widehat{\mathbf1_{S_\lambda}}(\xi)^3.}
\tag{1}
\]
Moreover the **entire threefold sumset** is
\[
\boxed{3S_\lambda=\begin{cases}
F^2\setminus\{(0,0)\},&a=b=c=-1,\\
F^2,&\text{otherwise}.
\end{cases}}\tag{2}
\]
In particular, every nonzero vector is attainable using exactly three (not necessarily distinct) summands for **all** odd field orders, including the small fields.

Let \(N_q\) denote the number of ratios \(\lambda\in F^\times\setminus\{1\}\) for which the origin is missing from \(3S_\lambda\). Then \(N_q=0\) unless \(q\equiv2\pmod3\). If \(q\equiv2\pmod3\) and the characteristic is five, then
\[
\boxed{N_q=(q-5)/4.}\tag{3}
\]
If \(q\equiv2\pmod3\) and the characteristic is not five, the curve
\[
E:\quad y^2=(1-4x)x(x-4)
\]
is smooth elliptic over \(F\), with Frobenius trace \(t_E=q+1-\#E(F)\), and
\[
\boxed{N_q=\frac{q-5+2\chi(-15)-t_E}{4},\qquad |t_E|\le2\sqrt q.}\tag{4}
\]
Consequently there exists a ratio with a missing origin **if and only if** \(q\equiv2\pmod3\) and \(q>5\). In that regime the exceptional fraction is asymptotic to one quarter: \(N_q=q/4+O(\sqrt q)\). More precisely, \(N_{11}=2\), with exceptional ratios \(7\) and \(8\) in \(\mathbb F_{11}\), while \(N_5=0\).

## Assumptions and scope

The group law is coordinatewise addition on \(F^2\), and convolution is **unnormalized**, \((f*g)(z)=\sum_{x+y=z}f(x)g(y)\). Fix any nontrivial additive character \(\psi\) on \(F\) and use \(\widehat f(\xi)=\sum_{z\in F^2}f(z)\overline{\psi(\xi\cdot z)}\). Fourier cubic moment in (1) uses the ordinary third power, not its absolute value; its sum is real by orthogonality. All three summands can repeat, but the two shells are disjoint because \(\lambda\ne1\). The integer \(q\) may be any odd prime power, including characteristic three or five. Statement (4) is invoked only for \(q\equiv2\pmod3\), which already excludes characteristic three; hence the only singular residue characteristic in this branch is five. No claim is made for even fields, nonunit shells, other numbers of shells, or a full threefold convolution at nonzero targets.

## Proof

**Step 1: exact two-shell twofold convolution.** For \(u,v\in\{1,\lambda\}\) and target \((A,B)\) with \(AB=s\ne0\), represent a pair of summands as \((x,u/x)\in H_u\) and \((A-x,v/(A-x))\in H_v\). Its sum equals \((A,B)\) precisely when
\[
Bx^2-(s+u-v)x+Au=0.
\]
Since \(u,v,A,B\ne0\), neither \(x=0\) nor \(x=A\) satisfies this equation. Thus every quadratic root supplies exactly one valid ordered pair, and there are \(1+\chi((s+u-v)^2-4su)\) pairs. Summing the four shell assignments yields, for \(AB=s\ne0\),
\[
\begin{split}
r_\lambda(A,B)&:=(\mathbf1_{S_\lambda}*\mathbf1_{S_\lambda})(A,B)\\
&=4+\chi(s(s-4))+\chi(s(s-4\lambda))
+2\chi\bigl(s^2-2(1+\lambda)s+(1-\lambda)^2\bigr).
\end{split}\tag{5}
\]
If exactly one of \(A,B\) is zero, the same-shell assignments contribute nothing and each mixed assignment contributes exactly one solution, so \(r_\lambda(A,B)=2\). At the origin only same-shell antipodal pairs contribute, giving \(r_\lambda(0,0)=2(q-1)\). This completely determines the twofold convolution, including every boundary target.

**Step 2: cubic return and threefold support.** The set \(S_\lambda\) is centrally symmetric. By (5), \(r_\lambda\) is constant on each shell because the right-hand side depends only on \(AB\). Evaluating (5) at \(s=1\) and \(s=\lambda\) gives respectively
\[
r_\lambda\big|_{H_1}=4+a+b+2c,\qquad
r_\lambda\big|_{H_\lambda}=4+a+c+2b.
\]
Therefore
\[
(\mathbf1_{S_\lambda}^{*3})(0,0)
=\sum_{z\in S_\lambda}r_\lambda(-z)
=(q-1)(8+2a+3b+3c).
\]
Fourier inversion and character orthogonality give the second equality in (1). Since \(a,b,c\in\{-1,0,1\}\), the bracket vanishes **exactly** when all three equal \(-1\).

By the axis computation in Step 1, every point on either coordinate axis belongs to \(2S_\lambda\), including the origin. For arbitrary \((A,B)\ne(0,0)\), if \(A\ne0\), subtract the shell point \((A,A^{-1})\in H_1\); the remainder is \((0,B-A^{-1})\in2S_\lambda\). If \(A=0,B\ne0\), subtract \((B^{-1},B)\in H_1\); the remainder is \((-B^{-1},0)\in2S_\lambda\). Thus every nonzero target is in \(3S_\lambda\), and (1) settles the only possible exception. This proves (2).

**Step 3: count exceptional ratios.** In an odd field, \(\chi(-3)=-1\) if and only if \(q\equiv2\pmod3\): outside characteristic three, this is equivalent to the absence of nontrivial cubic roots of unity by the discriminant of \(X^2+X+1\). In characteristic three \(\chi(-3)=0\), so there is never an exception. Therefore suppose henceforth \(q\equiv2\pmod3\), which implies characteristic at least five.

Set \(A(x)=1-4x\), \(B(x)=x(x-4)\), and \(P(x)=A(x)B(x)\). For \(x\notin\{0,1\}\), the required character conditions are \(\chi(A(x))=\chi(B(x))=-1\). Let \(T=\sum_{x\in F}\chi(P(x))\). Standard quadratic character sums give
\[
\sum_{x\in F\setminus\{0,1\}}\chi(A(x))=0,\qquad
\sum_{x\in F\setminus\{0,1\}}\chi(B(x))=0,\qquad
\sum_{x\in F\setminus\{0,1\}}\chi(P(x))=T-1.
\]
Indeed \(\sum_F\chi(A)=0\), \(\sum_F\chi(B)=-1\), \(\chi(A(0))=1\), \(\chi(A(1))=\chi(B(1))=-1\), and \(\chi(P(1))=1\). Expanding the character sieve therefore gives the preliminary sum
\[
\frac14\sum_{x\in F\setminus\{0,1\}}(1-\chi(A(x)))(1-\chi(B(x)))=\frac{q-3+T}{4}.\tag{6}
\]
This expression must be corrected at zeros of either character, since its factors are not exact indicators there.

If the characteristic is not five, the two distinct remaining zeros occur at \(x=4\) and \(x=1/4\). At the first, \(\chi(A(4))=\chi(-15)\); at the second, \(\chi(B(1/4))=\chi(-15)\). Their combined spurious contribution to (6) is \((1-\chi(-15))/2\). Consequently
\[
N_q=\frac{q-5+2\chi(-15)+T}{4}.
\]
The polynomial \(P(x)\) has three distinct roots \(0,4,1/4\), so the smooth completion of \(y^2=P(x)\) is an elliptic curve with one rational point at infinity and \(\#E(F)=q+1+T\). Thus \(T=-t_E\), giving (4) and its Hasse bound.

In characteristic five, the two nonzero zero positions coalesce at \(4=1/4\), and \(P(x)=x(x-4)^2\). Thus \(T=-1\) and the single doubly vanishing point contributes a spurious \(1/4\) to (6). Hence \(N_q=(q-3-1)/4-1/4=(q-5)/4\), proving (3). The exception at characteristic five is **not** evaluated using the singular cubic as an elliptic curve.

**Step 4: sharp existence threshold.** For \(q\equiv2\pmod3\) and characteristic other than five, (4) implies
\[
N_q\ge\frac{q-7-2\sqrt q}{4}>0\qquad(q\ge17).
\]
The only smaller such field is \(\mathbb F_{11}\), where direct quadratic-character evaluation gives precisely \(\lambda=7,8\). For characteristic five, the admissible field orders \(q\equiv2\pmod3\) are precisely \(5^{2k+1}\): (3) yields zero at \(5\) and positive values for all \(k\ge1\). Combining these cases with the character obstruction from Step 3 proves the final existence classification. \(\square\)

## Verification

Run `python3 artifacts/verify_two_shell_threefold.py`. The standalone Python program implements odd prime and extension fields, explicitly enumerates ordered sums of all pairs of shell points, independently checks (5) at every target in 15 field models, and compares the direct threefold support against (2) at every target for fields of order at most 17. It checks the cubic-origin count and the exceptional-ratio census in every tested field; field orders include \(3,5,7,9,11,13,17,19,23,25,27,29,31,49,125\). The code uses only Python's standard library. These finite checks are corroborating evidence; the universal statements rely on the algebraic derivation and the Hasse bound.

## Relationship to prior work

Stănică, Mulder, and Hittmeir (2026) study the **one-dimensional linear projection images** of pairs of modular hyperbolas; their character-sum and elliptic-trace perspective motivates asking for arithmetic transitions on mixed shells, but their image-union estimates do not yield ordered threefold **vector** sums or a cubic Fourier moment. Bower, Evans, Luo, and Miller (2012), and Khan, Magner, Senger, and Winterhof (2013), study coordinate projections or finite-field geometry of modular hyperbolas, rather than the present two-shell three-step return law.

A published theorem on threefold addition of a **single** split hyperbola guarantees nonzero targets for sufficiently large fields; this does **not** resolve the origin for the union of two distinct shells or classify exceptional shell ratios. A published mixed two-shell energy theorem computes a **fourth** Fourier moment, not the cubic return moment or the ratio-counting elliptic correction here. A published distinct-summand threefold theorem concerns a single shell and an additional distinctness constraint. The present contribution is the explicit two-shell cubic character law, its all-field zero-support criterion, and the arithmetic classification of exceptional ratios. Equivalent results could exist in unlocated literature, so absolute historical priority is not asserted.

## Limitations

The statement concerns odd fields and exactly two nonzero product levels. It does not determine the full numerical threefold convolution away from the origin, nor optimize over more shell levels, nor treat even characteristic. The genus-one count is a trace formula, not a uniform elementary polynomial in the field size. Finite tests cannot independently certify the infinite family; historical originality remains subject to further bibliographic checking and independent mathematical review.

## References

1. P. Stănică, E. Mulder, and M. Hittmeir, *Multi-target hyperbolic sieves and elliptic trace obstructions*, arXiv:2606.13018v1 (first public 2026-06-11), https://arxiv.org/abs/2606.13018.
2. A. Bower, R. Evans, V. Luo, and S. J. Miller, *Coordinate sum and difference sets of d-dimensional modular hyperbolas*, arXiv:1212.2930 (2012), https://arxiv.org/abs/1212.2930.
3. M. R. Khan, R. Magner, S. Senger, and A. Winterhof, *Two Combinatorial Geometric Problems Involving Modular Hyperbolas*, arXiv:1304.6943 (2013), https://arxiv.org/abs/1304.6943.
4. *Sharp three-sum covering of the split modular hyperbola over finite fields* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-three-sum-covering-of-the-split-modular-hyperbola-over-fin--02aca6c7a46d.
5. *Sharp distinct three-sum coverage of the split modular hyperbola* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-distinct-three-sum-coverage-of-the-split-modular-hyperbola--d7c0719593b0.
6. *Exact mixed additive energy of modular hyperbolas over odd residue rings* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-mixed-additive-energy-of-modular-hyperbolas-over-odd-resid--f8283f67d6a5.
7. The classical Hasse bound for the number of rational points on elliptic curves over finite fields.
