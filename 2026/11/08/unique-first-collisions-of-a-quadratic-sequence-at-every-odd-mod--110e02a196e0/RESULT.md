# Unique first collisions of a quadratic sequence at every odd modulus

## Finding
For each integer \(k\ge1\), set \(f(k)=2k(k-1)\). Fix an odd integer \(m\ge3\), and let \(J(m)\) be the smallest integer \(j\ge2\) for which \(f(i)\equiv f(j)\pmod m\) for some \(1\le i<j\).

Write \(\mathcal D(m)=\{d\in\mathbb Z_{>0}:d\mid m\}\). The function \(d\mapsto d+2m/d\) has a **unique** minimizer \(d_m\) on \(\mathcal D(m)\). The exact first collision time and the unique earlier colliding index are
\[
\boxed{J(m)=\frac{1+d_m+2m/d_m}{2},\qquad
 i_m=\frac{1+|d_m-2m/d_m|}{2}.}
\]
Thus the first \(J(m)-1\) values are pairwise incongruent modulo \(m\), and precisely one pair among the first \(J(m)\) values is congruent, namely \((i_m,J(m))\).

In particular, for every odd prime \(p\) and every integer \(t\ge1\),
\[
\boxed{J(p^{2t})=\frac{3p^t+1}{2},}
\]
and for all integers \(t\ge0\),
\[
\boxed{J(p^{2t+1})=\frac{(p+2)p^t+1}{2}.}
\]
For the even exponent, \(d_m=p^t\) and \(i_m=(p^t+1)/2\). For the odd exponent, \(d_m=p^{t+1}\) and \(i_m=((p-2)p^t+1)/2\). These statements include exponent one, already accessible via the classical prime-modulus argument; the composite-modulus classification is the additional content.

## Assumptions and scope
All indices are positive integers, all moduli are odd integers at least \(3\), and congruence means equality of integer residues. A 'first collision' is indexed by the later index \(j\), not by the difference between indices. Uniqueness refers to the pair \((i,j)\) at this first later index, not to congruence classes appearing later in the infinite periodic sequence. No claim is made for even moduli.

## Proof
**1. Exact parametrization of colliding pairs.** For integers \(1\le i<j\),
\[
f(j)-f(i)=2(j-i)(i+j-1).
\]
Since \(m\) is odd, \(f(i)\equiv f(j)\pmod m\) if and only if \(m\mid(j-i)(i+j-1)\). Set \(x=j-i\), \(y=i+j-1\). Then \(x,y\) are positive integers satisfying \(x<y\) and having opposite parity (because \(y-x=2i-1\)). Conversely, every such pair yields uniquely
\[
i=(y-x+1)/2,\qquad j=(y+x+1)/2,
\]
with positive integral indices and a congruence precisely when \(m\mid xy\).

**2. Reduce to complementary divisors.** As \(x,y\) have opposite parity, write their unordered pair as \(\{u,2v\}\), with \(u,v\ge1\) and \(u\) odd. Because \(m\) is odd, \(m\mid xy\) is equivalent to \(m\mid uv\). For each prime power \(p^a\parallel m\), distribute its exponent \(a\) between two nonnegative integers \(r,s\) with \(r\le v_p(u)\) and \(s\le v_p(v)\), possible since \(v_p(u)+v_p(v)\ge a\). Multiplying the assigned prime powers gives positive odd integers \(d\mid u\) and \(e\mid v\) with \(de=m\). Consequently,
\[
x+y=u+2v\ge d+2e=d+2m/d.
\]
Conversely, for every \(d\mid m\), the two positive numbers \(d\) and \(2m/d\) have opposite parity and are unequal; order them as \(x<y\). They satisfy \(m\mid xy\) and therefore yield a valid congruent pair with later index \((1+d+2m/d)/2\). Minimizing proves the formula for \(J(m)\).

**3. Uniqueness at the first collision.** Suppose positive divisors \(d_1,d_2\mid m\) give the same minimal sum. Algebra gives
\[
(d_1-d_2)\left(1-\frac{2m}{d_1d_2}\right)=0.
\]
The equality \(d_1d_2=2m\) is impossible because the left product is odd and the right product is even. Thus \(d_1=d_2=d_m\). For any colliding pair attaining the minimal sum, the inequalities \(u\ge d\), \(v\ge e\) in step 2 must both be equalities; otherwise their sum would exceed the minimum. Hence the unordered factors are exactly \(\{d_m,2m/d_m\}\). The inversion in step 1 gives a single pair, and its earlier index equals \(i_m\). By definition there can be no other collision at an earlier index, and no other congruent pair at index \(J(m)\).

**4. Explicit prime-power minimum.** If \(m=p^a\) for odd prime \(p\), its positive divisors are \(d=p^u\), \(0\le u\le a\). Put \(F_a(u)=p^u+2p^{a-u}\). Then
\[
F_a(u+1)-F_a(u)=(p-1)(p^u-2p^{a-u-1}).
\]
As \(p\ge3\), this difference changes sign from negative to positive precisely between \(u=t-1,t\) for \(a=2t\), and between \(u=t,t+1\) for \(a=2t+1\). More explicitly, when \(a=2t\), the differences are negative for \(u\le t-1\) and positive for \(u\ge t\); when \(a=2t+1\), they are negative for \(u\le t\) and positive for \(u\ge t+1\). Thus the unique minimizer is \(p^t\) in the even case and \(p^{t+1}\) in the odd case. Substitution yields both stated expressions and the earlier-index formulas. This completes the proof.

## Verification
The self-contained `verify.py` runs independent direct residue-table scans for every odd modulus from \(3\) to \(5001\), asserting both the predicted collision index and uniqueness of the earlier partner. It also checks each prime-power closed form against the divisor minimization for an explicit range. The original proof applies to all odd moduli; bounded computation is supporting evidence only.

Illustrations: modulo \(9\), the unique first pair is \((2,5)\); modulo \(15\), it is \((1,6)\); modulo \(25\), it is \((3,8)\); modulo \(49\), it is \((4,11)\); and modulo \(225\), it is \((4,22)\).

## Relationship to prior work
Zhi-Wei Sun, *On functions taking only prime values*, arXiv:1202.6589 (first posted 2012-02-29), Theorem 1.1(i), determines the *least modulus*, among all moduli, making the first \(n\) values of \(2k(k-1)\) pairwise distinct. His Theorem 2.1 gives necessary bounds for fixed moduli and his Theorem 2.2 covers a sufficient prime-modulus condition. These do not provide the exact first-repeat index or its uniquely determined collision partner at every odd composite modulus. The exponent-one prime formula follows from the known prime case and is not separately claimed new.

Sun's later *The least modulus for which consecutive polynomial values are distinct*, arXiv:1304.5988 (2013), studies minimum moduli for different families of polynomial values, not the fixed-modulus first-repeat invariant here.

Darin J. Ulness, *Structure of Triangular Numbers Modulo m* (2022), doi:10.3390/appliedmath2030020, studies periodicity, symmetry, occupancy and multiplicity of triangular numbers. For odd moduli, \(2k(k-1)\) is an invertible scalar multiple of a shifted triangular-number sequence. The accessible sections do not state this sharp first-collision divisor minimization or uniqueness; access to the entire article was rate-limited and historical-equivalence risk remains.

## Limitations
The classification assumes an odd modulus. Nothing here classifies even moduli or other quadratic polynomials. Historical uniqueness cannot be certified by searches; in particular a prior formulation using triangular numbers and near-square divisor pairs could be overlooked. The computational tests are finite and do not constitute an unrestricted proof. This work has undergone self-review only; no independent mathematical audit is claimed.

## References
1. Zhi-Wei Sun, *On functions taking only prime values*, arXiv:1202.6589 (original submission February 29, 2012); Journal of Number Theory 133 (2013), 2794–2812. https://arxiv.org/abs/1202.6589
2. Zhi-Wei Sun, *The least modulus for which consecutive polynomial values are distinct*, arXiv:1304.5988 (original submission April 22, 2013); Journal of Number Theory 160 (2016), 108–116. https://arxiv.org/abs/1304.5988
3. Darin J. Ulness, *Structure of Triangular Numbers Modulo m*, AppliedMath 2 (2022), 326–358. https://doi.org/10.3390/appliedmath2030020
