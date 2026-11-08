# Sharp fourth moments for zero-completed anisotropic conics without ternary resonance

## Finding

Let \(F=\mathbb F_q\) have prime-power order \(q\equiv7\pmod{12}\), let \(K=\mathbb F_{q^2}\), and set
\[
T=\{z\in K:N_{K/F}(z)=1\},\qquad S=T\cup\{0\}.
\]
For any nontrivial additive character \(\psi:F\to\mathbb C^\times\) and any function \(f:S\to\mathbb C\), define
\[
\mathcal E f(x)=\sum_{z\in S}f(z)\psi(\operatorname{Tr}_{K/F}(xz)),\quad x\in K.
\]
With counting measure on the input and uniform probability measure on \(K\), the exact sharp fourth-power norm is
\[
\boxed{\sup_{f\ne0}\frac{q^{-2}\sum_{x\in K}|\mathcal E f(x)|^4}{(\sum_{z\in S}|f(z)|^2)^2}=\frac{3(2q+3)}{2q+5}.}
\]
Every nonzero equality case, and only such a case, has a common positive modulus \(a\) on \(T\), a center coefficient satisfying \(|f(0)|^2=3a^2/2\), and the coherent antipodal products
\[
\boxed{f(z)f(-z)=\tfrac23 f(0)^2\quad(z\in T).}
\]
Equivalently, for arbitrary \(a>0\), \(\phi\in\mathbb R\), and one arbitrary angle \(\theta_j\) for each antipodal pair \(\{z_j,-z_j\}\), all equality cases are
\[
f(0)=\sqrt{3/2}\,a e^{i\phi},\qquad
f(z_j)=a e^{i(\phi+\theta_j)},\qquad
f(-z_j)=a e^{i(\phi-\theta_j)}.
\]
In addition, the proof supplies an **exact six-term nonnegative deficit identity**, stated below, valid for every complex coefficient array, not merely for extremizers.

## Assumptions and scope

The congruence assumption means \(q=p^r\) where \(p\equiv7\pmod{12}\) is prime and \(r\) is odd. In particular, the characteristic exceeds three and both \(-1\) and \(3\) are quadratic nonsquares in \(F\). Thus \(K=F(i)\) with \(i^2=-1\), conjugation sends \(i\) to \(-i\), and the norm is the anisotropic quadratic form \(N(u+iv)=u^2+v^2\). The set \(T\) has \(m=q+1\) points, split into \(J=m/2\) opposite pairs. The center is a genuine extra frequency and is counted once. Functions and all phases are arbitrary complex, including zeros. The Fourier-character convention only changes conjugations and not the stated norm or equality conditions.

## Proof

**Quadratic and arithmetic collision geometry.** The quadratic character of \(-1\) is negative because \(q\equiv3\pmod4\). For \(3\), quadratic reciprocity gives \((3/p)=-1\) at primes \(p\equiv7\pmod{12}\); since \(r\) is odd, \(3\) remains nonsquare in \(F\). The trace form on \(K\) is nondegenerate, so its additive characters satisfy the usual Fourier orthogonality relation.

Let \(Q(x)=N(x)\) and let \(B\) be its symmetric polar bilinear form, so \(Q(x+y)=Q(x)+Q(y)+2B(x,y)\). For \(s\ne0\), a pair \(a,b\in T\) with \(a+b=s\) has difference \(d=a-b\) satisfying \(B(s,d)=0\) and \(Q(d)=4-Q(s)\). Because \(Q\) is anisotropic, \(B(s,\cdot)=0\) is the one-dimensional space \(F(is)\). Hence there are at most two opposite solutions \(d,-d\), giving at most one unordered pair \(\{a,b\}\). If in addition \(s\in T\), then \(d=tis\) would require \(t^2=3\), which is impossible by the nonsquare property. Thus the extra pairs \((0,s),(s,0)\) never collide with a pair from \(T\). Every nonzero sum in \(S+S\) therefore has a unique unordered pair. The only exceptional sum is zero: it receives the diagonal pair \((0,0)\) and every ordered antipodal pair \((z,-z)\) from \(T\).

**Exact fourth-moment identity.** Put \(c=f(0)\), \(y=|c|^2\),
\[
B_0=\sum_{z\in T}|f(z)|^2,\quad
D=\sum_{z\in T}|f(z)|^4,\quad
R=\sum_{z\in T}|f(z)|^2|f(-z)|^2,\quad
H=\sum_{z\in T}f(z)f(-z).
\]
Orthogonality converts the fourth moment into the sum of squares of ordered-pair convolution fibers. Using the preceding classification, its exact value is
\[
\mathcal Q(f):=q^{-2}\sum_{x\in K}|\mathcal Ef(x)|^4
=2B_0^2-D-2R+|c^2+H|^2+4yB_0.\tag{1}
\]
The first three terms are the uncompleted-conic energy with its exceptional zero fiber removed; the fourth is the completed zero fiber; the last counts the new center/nonzero two-sums. No positivity assumption on \(f\) is used.

**Sharp bound and equality.** Choose one representative \(z_j\) from each opposite pair, and put
\[
s_j=|f(z_j)|^2+|f(-z_j)|^2,\quad
p_j=|f(z_j)f(-z_j)|,\quad
P=\sum_{j=1}^J p_j,
\]
so \(B_0=\sum_j s_j\), \(0\le P\le B_0/2\), \(D+2R=\sum_j(s_j^2+2p_j^2)\), and \(|c^2+H|\le y+2P\). Cauchy–Schwarz in the two lists implies
\[
\mathcal Q(f)\le
2B_0^2-\frac{B_0^2}{J}-\frac{2P^2}{J}+(y+2P)^2+4yB_0.
\]
As a function of \(P\) the right-hand side is strictly increasing on every nondegenerate interval in \([0,B_0/2]\) whenever \(B_0>0\), since its \(P\)-dependent part is \((4-4/m)P^2+4yP\). Replacing \(P\) by \(B_0/2\) gives
\[
\mathcal Q(f)\le y^2+6yB_0+(3-3/m)B_0^2.
\]
For \(M=y+B_0\), completing the square yields the *exact algebraic identity*
\[
y^2+6yB_0+(3-3/m)B_0^2
=\frac{3(2m+1)}{2m+3}M^2
-\left(2+\frac3m\right)
\left(B_0-\frac{2m}{2m+3}M\right)^2.
\]
This proves the asserted sharp constant after substituting \(m=q+1\). Equality requires \(B_0=2mM/(2m+3)>0\), so \(y=3B_0/(2m)>0\), and also requires \(P=B_0/2\), equality in both Cauchy inequalities, and equality in the center-fiber triangle inequality. These conditions say that all \(m\) peripheral squared moduli equal \(B_0/m=a^2\), that \(y=3a^2/2\), and that all complex products \(f(z)f(-z)\) have the phase of \(c^2\). Their magnitudes are all \(a^2\), giving precisely \(f(z)f(-z)=\tfrac23c^2\). Conversely the parametrized family saturates every step; no other extremizers exist.

**An exact six-term deficit.** Define \(M=y+B_0\), \(\kappa=3(2m+1)/(2m+3)\), and
\[
\begin{aligned}
\Delta_1&=\left(2+\frac3m\right)\left(B_0-\frac{2m}{2m+3}M\right)^2,\\
\Delta_2&=\sum_j s_j^2-B_0^2/J,\\
\Delta_3&=2\left(\sum_jp_j^2-P^2/J\right),\\
\Delta_4&=(4-4/m)(B_0^2/4-P^2),\\
\Delta_5&=4y(B_0/2-P),\\
\Delta_6&=(y+2P)^2-|c^2+H|^2.
\end{aligned}
\]
Every term is nonnegative for every \(f\), and direct substitution of (1) proves, without approximation,
\[
\boxed{\kappa\left(\sum_{z\in S}|f(z)|^2\right)^2-\mathcal Q(f)
=\Delta_1+\Delta_2+\Delta_3+\Delta_4+\Delta_5+\Delta_6.}\tag{2}
\]
The terms separately detect wrong center mass, uneven opposite-pair mass, dispersed pair products, opposite-point imbalance, failure of saturation, and phase mismatch. They give a concrete equality/deficit certificate; no uniform metric-distance stability constant is asserted.

## Verification

Run `python3 artifacts/verify.py` from the extracted package. The standard-library checker verifies conic cardinality, ordered-pair sum fibers, exact rational sharp ratios, numerical fourth-moment inequalities, equation (1), all six nonnegative terms and their sum in (2), and a genuinely independent character-sum Fourier computation on prime fields. The expected output is

`COMPLETED_ANISOTROPIC_CONIC_VERIFY_PASS fields=6 checks=324 independent_fourier=6 prime_fields=(7, 19, 31, 43, 67, 79)`

The checker tests six prime fields; the assertion for every eligible prime power follows from the preceding proof, not the finite checks. Randomized checks cannot substitute for exact algebraic quantifiers.

## Relationship to prior work

Work on the uncompleted anisotropic norm-one conic determines its sharp Fourier norm and complex extremizers. That theorem does not cover the extra central frequency, which changes the zero-sum convolution fiber and the optimal center/periphery amplitude ratio. Published work on arbitrary deletion masks for nonzero conics likewise does not allow adding the origin. A published four-part nonnegative deficit decomposition for planar nonzero conics is likewise restricted to the uncompleted level set and does not contain the new center-mass term or the six-part completed identity. A sharp theorem for a **completed split inverse graph** exhibits a similar nonresonant optimization, but its frequency set has \(q-1\) rather than \(q+1\) peripheral sites, and split and nonsplit conics are not affine-equivalent. It does not imply the nonsplit center-completion statement or its six-term deficit identity. Our restriction \(q\equiv7\pmod{12}\) identifies exactly a nonsplit, ternary-nonresonant family; the resonant nonsplit fields are not classified here. The finite-field restriction literature provides the surrounding sharp-extension framework but does not state this exact completed anisotropic result.

## Limitations

The theorem concerns fields of cardinality \(q\equiv7\pmod{12}\), the complete anisotropic norm-one conic together with its center, fourth moments, and the exact stated normalization. It does not cover nonsplit conics when \(3\) is a square, other erasure patterns after completion, higher moments, or uniform metric stability. A general published result for centrally completed additive sets with exactly one exceptional two-sum fiber might imply the theorem; such a result has not been located, so historical priority remains provisional. The six-term identity is exact, but its interpretation as a quantitative metric stability inequality would require further estimates. External independent validation has not been performed.

## References

1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first publicly posted 2024-05-26, https://arxiv.org/abs/2405.16647 .
2. A. Iosevich, D. Koh, S. Lee, T. Pham, and C.-Y. Shen, *On restriction estimates for the zero radius sphere over finite fields*, arXiv:1806.11387v1, https://arxiv.org/abs/1806.11387 .
3. *Sharp fourth-moment extension on the anisotropic finite-field norm-one conic*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-fourth-moment-extension-on-the-anisotropic-finite-field-no--b7ad248d6495 .
4. *Sharp Fourier extension and phase transitions under arbitrary erasures of finite-field conics*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourier-extension-and-phase-transitions-under-arbitrary-er--6b59f93aeabe .
5. *Sharp Fourier extension on the zero-completed finite-field inverse graph*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourier-extension-on-the-zero-completed-finite-field-inver--b05317385d5a .
6. *Exact deficit decomposition for planar finite-field quadratic extension*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-deficit-decomposition-for-planar-finite-field-quadratic-ex--f7276650ee6d .
