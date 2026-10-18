# Sharp \(L^2\)-to-\(L^4\) constants for a single additive collision
## Finding
Let \(\Gamma\) be a torsion-free discrete abelian group and let \(A\subset\Gamma\) be finite. Assume that, among unordered two-element multisets drawn from \(A\) with repetition allowed, exactly one pair-sum value has two distinct representations and every other pair-sum value has one representation.

For coefficients \(c=(c_a)_{a\in A}\), define
\[
F_c(\chi)=\sum_{a\in A}c_a\chi(a),\qquad \chi\in\widehat\Gamma,
\]
where \(\widehat\Gamma\) has normalized Haar measure, and write
\[
\Lambda_4(A)^4=
\sup_{c\ne0}
\frac{\|F_c\|_4^4}{\bigl(\sum_{a\in A}|c_a|^2\bigr)^2}.
\]
There are exactly two possible collision types.

If the unique relation is
\[
a+b=c+d
\]
with \(a,b,c,d\) all distinct, then
\[
\boxed{\Lambda_4(A)^4=\frac94}.
\]
The nonzero extremizers are exactly those supported on \(\{a,b,c,d\}\), with equal coefficient moduli and with the two pair products in phase:
\[
c_a c_b\overline{c_c c_d}>0.
\]

If the unique relation is
\[
u+w=2v
\]
with \(u,v,w\) distinct, then
\[
\boxed{\Lambda_4(A)^4=\frac{15}{7}}.
\]
The nonzero extremizers are exactly those supported on \(\{u,v,w\}\) whose squared moduli satisfy
\[
|c_u|^2:|c_v|^2:|c_w|^2=2:3:2
\]
and whose collision terms are in phase:
\[
c_v^2\overline{c_uc_w}>0.
\]

Thus the first failure of two-fold additive independence already has a complete sharp fourth-moment classification: a four-point parallelogram defect and a three-term-progression defect have different exact constants and different extremal mass profiles.

## Assumptions and scope
The group \(\Gamma\) is discrete, abelian, and torsion-free. Torsion-freeness ensures that a unique nontrivial equality between unordered pair sums can only have one of the two forms above: two disjoint off-diagonal pairs, or one off-diagonal pair colliding with a diagonal pair. The theorem concerns only the exponent \(4\) and exactly one nontrivial unordered pair-sum collision.

The Haar normalization is \(\int_{\widehat\Gamma}1=1\). Coefficients outside the displayed collision subsystem are allowed a priori; the equality analysis proves that every extremizer sets them to zero.

## Proof
Put
\[
x_a=|c_a|^2,\qquad S=\sum_{a\in A}x_a.
\]
By Parseval applied to \(F_c^2\),
\[
\|F_c\|_4^4
=\sum_{s\in\Gamma}\left|\sum_{a+b=s}c_ac_b\right|^2,
\]
where the inner sum is over ordered pairs. If all unordered pair sums were distinct, this would equal
\[
\sum_a x_a^2+4\sum_{a<b}x_ax_b
=2S^2-\sum_a x_a^2.
\]
The unique collision changes exactly one fiber.

For a disjoint-pair relation \(a+b=c+d\), the exceptional fiber contributes
\[
|2c_ac_b+2c_cc_d|^2,
\]
so
\[
\|F_c\|_4^4
=2S^2-\sum_t x_t^2
+8\operatorname{Re}(c_ac_b\overline{c_cc_d}).
\]
Hence
\[
\|F_c\|_4^4
\le 2S^2-\sum_t x_t^2+8\sqrt{x_ax_bx_cx_d}.
\]
Let \(r=x_a+x_b+x_c+x_d\). The arithmetic-geometric mean inequality gives
\[
\sum_t x_t^2\ge x_a^2+x_b^2+x_c^2+x_d^2
\ge4\sqrt{x_ax_bx_cx_d},
\]
and
\[
\sqrt{x_ax_bx_cx_d}\le\left(\frac r4\right)^2.
\]
Therefore
\[
\|F_c\|_4^4
\le2S^2+\frac{r^2}{4}
\le\frac94 S^2.
\]
Equality forces all coefficients outside \(\{a,b,c,d\}\) to vanish, the four displayed moduli to be equal, and the exceptional cross term to have maximal positive real part. These conditions are also sufficient.

For a three-term relation \(u+w=2v\), the exceptional fiber contributes
\[
|c_v^2+2c_uc_w|^2,
\]
so
\[
\|F_c\|_4^4
=2S^2-\sum_t x_t^2
+4\operatorname{Re}(c_v^2\overline{c_uc_w}).
\]
Write \(x=x_u\), \(y=x_v\), \(z=x_w\), and \(r=x+y+z\). Then
\[
\|F_c\|_4^4
\le2S^2-\sum_t x_t^2+4y\sqrt{xz}.
\]
For fixed \(p=x+z\),
\[
\sqrt{xz}\le\frac p2,
\qquad
x^2+z^2\ge\frac{p^2}{2}.
\]
Consequently
\[
4y\sqrt{xz}-(x^2+y^2+z^2)
\le2yp-y^2-\frac{p^2}{2}.
\]
Since \(p+y=r\), the right side is
\[
r^2\left(\frac17-\frac{(7y/r-3)^2}{14}\right)
\le\frac{r^2}{7}.
\]
Thus
\[
\|F_c\|_4^4
\le2S^2+\frac{r^2}{7}
\le\frac{15}{7}S^2.
\]
Equality forces all coefficients outside \(\{u,v,w\}\) to vanish, \(x=z\), \(y/r=3/7\), hence \(x:y:z=2:3:2\), and maximal positive alignment of \(c_v^2\) with \(c_uc_w\). These conditions are sufficient.

Finally, because \(\Gamma\) is torsion-free, two distinct colliding unordered pairs cannot share exactly one element, and two distinct diagonal pairs cannot have the same sum. Therefore the two cases exhaust the hypothesis.

## Verification
`artifacts/verify.py` independently reconstructs ordered pair-sum fibers for representative and exhaustively enumerated small integer supports, checks the two exact witnesses, and stress-tests the sharp upper bounds on every single-collision support it finds in a bounded census. Its current output is stored in `artifacts/verification_output.txt`.

The finite computation is corroborative only. The theorem for arbitrary finite \(A\) and arbitrary torsion-free \(\Gamma\) follows from the Parseval identities and scalar inequalities above.

## Relationship to prior work
Neuwirth's work on metric unconditionality and Fourier analysis makes explicit that even Fourier moments are polynomial expressions governed by arithmetic relations among frequencies, and for even exponents characterizes exact unconditionality through additive independence. That framework motivates the single-collision question but does not state these sharp \(L^2\)-to-\(L^4\) constants or equality cases.

A published comparison result on four-point phase-only fourth moments fixes all coefficient moduli and therefore addresses a different optimization. The present theorem allows arbitrary amplitudes and applies to finite sets of any cardinality subject only to one collision. A prior exact three-frequency calculation already contains the value \(15/7\) for the isolated three-term progression; the new statement shows that adding any number of otherwise collision-free frequencies cannot improve that value, classifies all global extremizers, and simultaneously gives the distinct four-point collision constant \(9/4\).

## Limitations
The theorem does not treat two or more nontrivial pair-sum collisions, groups with torsion, exponents other than \(4\), stability of near-extremizers, or finite cyclic sampling. The originality search cannot exclude an older equivalent statement expressed purely in \(\Lambda(4)\), additive-energy, or autoconvolution terminology.

## References
1. S. Neuwirth, *Metric unconditionality and Fourier analysis*, arXiv:math/9707211v1, first public version 1997-07-28; Studia Math. 131 (1998), 19-62. The paper records MSC 42A55 first and develops the even-exponent additive-relation framework.
2. A published published-finding corpus comparison record with opaque identifier `2b7f859e0b5c` treats phase-only four-point fourth moments.
