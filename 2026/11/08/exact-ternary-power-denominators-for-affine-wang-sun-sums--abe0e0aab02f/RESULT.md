# Exact ternary-power denominators for affine Wang–Sun sums

## Finding
For every integer \(a\ge1\), put \(m=3^a\) and \(n=2m\). Let \(\Delta_n\) be the fixed-point-free elements of the affine permutation group of \(\mathbb Z/n\mathbb Z\), acting by \(\pi(x)=vx+u\), where \(v\) is invertible modulo \(n\). Define the affine Wang–Sun sum
\[
S_n=\sum_{\pi\in\Delta_n}\operatorname{sign}(\pi)
\prod_{x\in\mathbb Z/n\mathbb Z}
\frac{1+\zeta^{x-\pi(x)}}{1-\zeta^{x-\pi(x)}},
\qquad \zeta=e^{2\pi i/n}.
\]
Then \(S_{2\cdot3^a}\) is rational, and its reduced denominator is **exactly** \(3^{3^a}\). In fact, writing \(S_{2\cdot3^a}=P_a/Q_a\) in lowest terms with \(Q_a>0\), one has
\[
Q_a=3^{3^a},\qquad P_a\equiv1\pmod3.
\]
The companion alternating cotangent block
\[
C_{2m}=\sum_{r=1}^{2m-1}(-1)^r
\left(i\cot\frac{\pi r}{2m}\right)^{2m}
\]
has the same exact reduced denominator and numerator residue when \(m=3^a\).

## Assumptions and scope
The exponent \(a\) ranges over **all** positive integers. The signs of affine permutations are ordinary permutation signs on the \(n\) residue classes, and \(\Delta_n\) excludes fixed points. Therefore no factor in the defining product has zero denominator. The denominator of a rational number always means the positive denominator of its reduced fraction. The \(3\)-adic valuation is normalized by \(v_3(3)=1\) and extends to the cyclotomic field in the proof; \(v_3(0)=+\infty\).

## Proof
**1. Rationality and denominator support.** Write \(u(\xi)=(1+\xi)/(1-\xi)\). For \(m=3^a\), the identity \(u(e^{2\pi ir/(2m)})=i\cot(\pi r/(2m))\) gives
\[
C_{2m}=A_m-B_m,
\quad A_m=\sum_{\substack{\xi^m=1\\\xi\ne1}}u(\xi)^{2m},
\quad B_m=\sum_{\xi^m=-1}u(\xi)^{2m}.
\]
Both sets of roots are stable under the Galois group of \(\mathbb Q(\zeta_{2m})\), so both sums are rational. Each root contributing to \(A_m\) has order \(3^j\) for some \(1\le j\le a\). Its denominator \(1-\xi\) has algebraic norm \(3\), so \(u(\xi)\) is integral away from the prime \(3\). A root in \(B_m\) either equals \(-1\) (whose contribution vanishes) or has order \(2\cdot3^j\), for which \(1-\xi\) is an algebraic unit because \(\Phi_{2\cdot3^j}(1)=1\). Hence every term is integral away from \(3\), and rationality yields
\[
C_{2m}\in\mathbb Z[1/3].
\]

**2. Unique lowest \(3\)-adic layer.** The prime \(3\) is totally ramified in the cyclotomic field of \(3^a\)-th roots. For each primitive \(3^j\)-th root \(\xi\),
\[
v_3(1-\xi)=\frac{1}{\varphi(3^j)}
=\frac1{2\cdot3^{j-1}},\qquad v_3(1+\xi)=0.
\]
Thus
\[
v_3\bigl(u(\xi)^{2m}\bigr)=-\frac{m}{3^{j-1}}.
\]
The only terms attaining valuation \(-m\) are the two primitive cube roots \(\omega,\omega^2\). Since \(u(\omega)^2=u(\omega^2)^2=-1/3\), their combined contribution is
\[
2(-1/3)^m.
\]
All other roots in \(A_m\) have order \(3^j\) with \(j\ge2\), and each contributes valuation at least \(-m/3\). Every root in \(B_m\) is \(-\eta\) for a \(3\)-power root \(\eta\); modulo the unique prime above \(3\), one has \(\eta\equiv1\), so \(1-(-\eta)=1+\eta\) is a unit and \(1+(-\eta)=1-\eta\) is integral. All terms of \(B_m\) therefore have nonnegative valuation. Consequently
\[
C_{2m}=2(-1/3)^m+R_m,
\qquad v_3(R_m)>-m.
\]
Because the leading coefficient \(2\) is a \(3\)-adic unit, the ultrametric inequality gives
\[
v_3(C_{2m})=-m,\qquad
3^m C_{2m}\equiv2(-1)^m\equiv1\pmod3.
\]
Together with \(C_{2m}\in\mathbb Z[1/3]\), this proves the full exact-denominator claim for the block.

**3. Transfer to the affine sum.** Agustín-Aquino's affine-divisor reduction [1, Theorem 5.1], combined with its local multiplicity formula [1, Proposition 3.4], specializes when \(n=2\cdot3^a\) to
\[
S_{2\cdot3^a}=C_{2\cdot3^a}
+\sum_{j=1}^{a-1}2\cdot3^{2(a-j)-1}C_{2\cdot3^j}.
\]
Indeed, all relevant even divisors are \(2\cdot3^j\); all quotient indices are odd, all permutation-sign factors are \(+1\), and the \(j=0\) term vanishes since \(C_2=0\). For \(1\le j<a\), the already proved block result gives
\[
v_3\left(2\cdot3^{2(a-j)-1}C_{2\cdot3^j}\right)
=2(a-j)-1-3^j>-3^a.
\]
Therefore none of these lower-divisor terms can cancel the unique \(3\)-adic leading term of \(C_{2\cdot3^a}\), proving
\[
v_3(S_{2\cdot3^a})=-3^a,\qquad
3^{3^a}S_{2\cdot3^a}\equiv1\pmod3.
\]
The divisor formula shows \(S_{2\cdot3^a}\in\mathbb Z[1/3]\); the exact denominator and numerator residue follow. \(\square\)

## Verification
The included `verify.py` computes the alternating blocks using exact rational Newton sums of the roots of
\[
F_m(t)=\frac{(t+1)^m-(t-1)^m}{2m},\qquad
G_m(t)=\frac{(t+1)^m+(t-1)^m}{2},
\]
whose roots correspond to the even and odd cotangent contributions when \(m\) is odd. It then applies the specialized affine-divisor formula. Checks for \(a=1,2,3\) yield the denominators \(27\), \(19683\), and \(7625597484987\), respectively, with reduced numerator \(1\pmod3\). The two smaller cases reproduce the values printed in [1, Table 1]. Run `python3 verify.py` with a standard Python 3 installation; no third-party packages are required. These finite computations corroborate the cyclotomic proof but do not certify every exponent.

## Relationship to prior work
The 2026 paper [1] evaluates the full affine Wang–Sun sum for arbitrary even moduli by a divisor reduction and closed cotangent formulas. It proves denominator \(p\) at modulus \(2p\) only for primes \(p>3\) [1, Theorem 8.2], and its table records the cases \(n=6\) and \(n=18\). Its all-index evaluation formula allows individual computations but does not state the exact uniform \(3^{3^a}\) denominator law. The new ingredient is a uniform ramification argument isolating the two primitive cube roots as the unique terms of smallest \(3\)-adic valuation, plus its survival through every lower-divisor contribution. Liu and Xin [2] provide general closed formulas for weighted trigonometric power sums; the inspected formulas do not assert this uniform reduced-denominator law. The earlier affine study [3] supplies numerical cases and explicitly leaves the full affine evaluation open. The present theorem is consistent with all of them.

## Limitations
The result concerns the particular moduli \(2\cdot3^a\); it does not determine reduced denominators for arbitrary mixed moduli or full numerators. Its priority comparison is based on the identified primary papers and available records, so an unindexed equivalent theorem cannot be ruled out. The proof is mathematical rather than a formal-machine proof, and no independent mathematical validation has been performed.

## References
1. O. A. Agustín-Aquino, *The Wang–Sun Sum over Affine Derangements*, arXiv:2610.02806v1 (first public 2026-10-02), https://arxiv.org/html/2610.02806v1.
2. J. Liu and G. Xin, *Root-of-unity weighted trigonometric power sums: a constant term approach*, arXiv:2607.29130 (first public 2026-07-31), https://arxiv.org/abs/2607.29130.
3. O. A. Agustín-Aquino, *Wang–Sun Formula in the Affine General Linear Group*, arXiv:2207.14495 (first public 2022-07-29), https://arxiv.org/abs/2207.14495.
