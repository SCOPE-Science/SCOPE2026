# Sharp higher-moment Fourier synthesis on every finite abelian difference set

## Finding
Let \(G\) be a finite abelian group of order \(v\). Let \(E\subset\widehat G\) be a nontrivial \((v,k,\lambda)\)-difference set: \(2\le k<v\), and every nonidentity element of \(\widehat G\) has exactly \(\lambda\ge1\) ordered representations \(e e'^{-1}\) with \(e,e'\in E\). For arbitrary complex coefficients \(c_e\), put \(F(x)=\sum_{e\in E}c_e e(x)\) and \(S=\sum_{e\in E}|c_e|^2\). Set \(a=(k-\lambda)/k=(v-k)/(v-1)\).

**Theorem.** For every real \(p\ge4\),
\[
\frac1v\sum_{x\in G}|F(x)|^p\le
\frac{k^{p/2}+(v-1)a^{p/2}}v\,S^{p/2}.
\]
The displayed constant is the exact sharp \(\ell^2(E)\)-to-normalized-\(L^p(G)\) operator norm raised to the power \(p\). For every \(p>4\), every nonzero equality family is precisely
\[
c_e=C\overline{e(x_0)}\qquad(e\in E),
\quad C\in\mathbb C\setminus\{0\},\ x_0\in G.
\]
There are exactly \(v\) distinct projective equality rays. At \(p=4\) the constant remains sharp but this equality description need not be exhaustive.

The sixth-power case has an **exact three-term nonnegative deficit**. For \(S>0\), define \(u_x=|F(x)|^2/S\); for \(d\in\widehat G\) define
\[
R_d=\sum_{e e'^{-1}=d}c_e\overline{c_{e'}},\qquad
B_d=\sum_{e e'^{-1}=d}|c_e|^2|c_{e'}|^2.
\]
Writing \(C_6=[k^3+(v-1)a^3]/v\), one has
\[
\begin{aligned}
C_6-\frac1v\sum_xu_x^3={}&(k+2a)\lambda
\sum_{e\in E}\left(\frac{|c_e|^2}{S}-\frac1k\right)^2\\
&+\frac{k+2a}{S^2}\sum_{d\ne1}\bigl(\lambda B_d-|R_d|^2\bigr)
+\frac1v\sum_{x\in G}(u_x-a)^2(k-u_x).
\end{aligned}
\]
Every term is nonnegative. Thus the sharp sixth moment has both an exact algebraic stability decomposition and a complete equality classification for all difference sets, cyclic or not.

## Assumptions and scope
The group \(G\) is finite and abelian, with \(v\ge3\), and the Fourier synthesis frequencies lie in its character group \(\widehat G\). Multiplication in \(\widehat G\) is used in the difference-set definition; in additive character coordinates \(e e'^{-1}\) is simply their difference. Uniform probability measure \(1/v\) is used on \(G\), but the input coefficient \(\ell^2\) norm is unnormalized. The theorem covers arbitrary complex coefficients and all real \(p\ge4\), not only even integers. No statement is made for \(2<p<4\) or for sets with nonuniform differences. Zero coefficient data attain equality trivially and are excluded from the rigidity assertion.

## Proof
**1. Mean, cap, and sharp fourth moment.** Assume \(S>0\). Character orthogonality gives
\[
\frac1v\sum_xu_x=1,
\qquad 0\le u_x\le k
\]
by Parseval and Cauchy--Schwarz. The same orthogonality applied to \(|F|^2\) gives
\[
\frac1v\sum_xu_x^2=\frac1{S^2}\sum_{d\in\widehat G}|R_d|^2.
\]
Here \(R_1=S\). For each \(d\ne1\), the difference-set hypothesis gives precisely \(\lambda\) summands, so \(|R_d|^2\le\lambda B_d\). Summing \(B_d\) over nonidentity \(d\) counts every pair of distinct frequencies once. Thus, with \(Q=\sum_e|c_e|^4\),
\[
\frac1v\sum_xu_x^2\le1+\lambda(1-Q/S^2)
\le C_4:=1+\lambda(1-1/k).
\]
In fact the exact nonnegative fourth-moment deficit is
\[
C_4-\frac1v\sum_xu_x^2=
\lambda\sum_e\left(\frac{|c_e|^2}{S}-\frac1k\right)^2
+\frac1{S^2}\sum_{d\ne1}(\lambda B_d-|R_d|^2).
\tag{1}
\]
These identities hold with no parity or cyclicity assumption.

**2. A sharp quadratic majorant.** Write \(s=p/2\ge2\). Define
\[
A_s=\frac{k^s-a^s-sa^{s-1}(k-a)}{(k-a)^2},\qquad
Q_s(t)=a^s+sa^{s-1}(t-a)+A_s(t-a)^2.
\]
Convexity of \(t^s\) gives \(A_s\ge0\). For \(s>2\), the third derivative of \(t^s\) is strictly positive on \((0,k]\), and the Hermite divided-difference remainder for the nodes \(a,a,k\) reads
\[
t^s-Q_s(t)=[a,a,k,t](z\mapsto z^s)\,(t-a)^2(t-k).
\]
Its divided difference is strictly positive for \(0<t\le k\), so
\[
Q_s(t)\ge t^s\quad(0\le t\le k),
\]
with equality exactly at \(t=a\) and \(t=k\). At \(t=0\) the assertion follows by continuity, and the inequality is strict there because \(a>0\). For \(s=2\), \(Q_s(t)=t^2\) identically.

**3. The two-point extremal distribution.** The difference-set equation \(k(k-1)=\lambda(v-1)\) yields
\[
\frac{k+(v-1)a}{v}=1,\qquad
\frac{k^2+(v-1)a^2}{v}=C_4.
\]
Consequently, using \(\mathbb E u=1\), \(\mathbb E u^2\le C_4\), and the fact that \(Q_s\) is a quadratic with nonnegative quadratic coefficient,
\[
\begin{aligned}
\mathbb E u^s&\le\mathbb E Q_s(u)
\le\frac{Q_s(k)+(v-1)Q_s(a)}v\\
&=\frac{k^s+(v-1)a^s}{v}.
\end{aligned}
\]
Multiplication by \(S^s\) proves the inequality. More precisely the deficit is
\[
\frac{k^s+(v-1)a^s}{v}-\mathbb E u^s
=A_s(C_4-\mathbb E u^2)+\mathbb E[Q_s(u)-u^s].
\tag{2}
\]
For \(s=3\), \(A_3=k+2a\) and \(Q_3(t)-t^3=(t-a)^2(k-t)\). Substitution of (1) into (2) is the displayed three-term sixth-moment identity.

**4. Sharpness and all equality cases above the fourth moment.** For any \(x_0\in G\), take \(c_e=C\overline{e(x_0)}\) with \(C\ne0\). Its Fourier synthesis has squared normalized magnitude \(u_{x_0}=k\); at every other point \(x\ne x_0\), the difference-set character-sum identity gives \(u_x=(k-\lambda)/k=a\). Hence it attains equality for every \(p\ge4\). Conversely, for \(s>2\), equality in (2) requires \(u_x\in\{a,k\}\) at every point. Their prescribed mean and \(a\ne k\) force exactly one point \(x_0\) with \(u_{x_0}=k\). Equality \(|F(x_0)|^2=kS\) in the elementary Cauchy--Schwarz inequality forces \(c_e=C\overline{e(x_0)}\) for every \(e\). If two points gave the same projective coefficient ray, all characters \(e e'^{-1}\) for \(e,e'\in E\) would be trivial on their difference; the difference-set property makes these characters exhaust \(\widehat G\), so the points coincide. There are exactly \(v\) rays.

## Verification
Run `python3 checker.py` using only the Python standard library. It checks exact difference counts, exact rational \(L^4\) and \(L^6\) bounds on Gaussian-integer inputs, exact rational quadratic-majorant identities for integral exponents three and four, and numerical character-equality profiles at real exponents \(4,4.25,5,6,7.75,10\) for cyclic examples of orders \(7,11,13,19\) and a noncyclic 16-point binary group. Its recorded output starts `VERIFY_OK`. The theorem for all real \(p\ge4\), all difference sets, and all coefficients follows from the proof, not finite testing.

For the Singer \((7,3,1)\) and \((13,4,1)\) sets, the sharp sixth-power constants are \(37/9\) and \(85/16\), respectively. For the Paley \((11,5,2)\) difference set, the corresponding value is \(289/25\); the noncyclic \((16,6,2)\) bent-function difference set provides a structurally distinct check.

## Relationship to prior work
Fickus, Jasper, Mixon and Peterson (2017) and Fickus and Schmitt (2019) explain harmonic equiangular tight frames in terms of difference sets; their inspected constructions concern frame geometry and do not state the sharp \(L^p\) synthesis norm for the full range \(p>4\).

The published result *Sharp fourth-moment extension and exact deficit for finite abelian difference sets* gives precisely the \(p=4\) input (1), and is not reasserted as a new theorem. The new claim is the **simultaneously sharp all-real-\(p>4\) law**, the strict equality-ray classification for every difference set, and the full sixth-order two-mechanism-plus-pointwise deficit (2). This does not follow from the usual Hölder interpolation of sharp \(L^4\) and \(L^\infty\) bounds, which is not sharp on nontrivial difference sets: the extremal Fourier profile has two distinct nonzero squared-modulus levels.

The published *Sharp sixth-moment constant for finite subgroup-hole spectra* gives another genuine special case: taking the removed subgroup to have one character makes the retained frequencies a complement-of-singleton difference set. Its sharp sixth-moment constant agrees with the formula above for \(k=v-1\), but its theorem is restricted to sixth powers and subgroup-complement spectra.

The Fano Singer sixth-power constant \(37/9\), and the order-three Singer constant \(85/16\), were obtained previously for the particular spectra \((7,3,1)\) and \((13,4,1)\). They are explicitly acknowledged as special cases, not independent new discoveries. The present implication runs from the all-difference-set theorem to those finite instances; neither single-instance result or the isolated fourth-moment theorem, as stated, covers all real exponents and all finite abelian difference sets. Unknown equivalent classical convex-order or frame-potential inequalities remain a priority risk.

## Limitations
Sharpness requires a genuine difference set, not a partial difference set or a general tight frame. The cases \(2<p<4\) are not classified. The fourth-moment equality family may contain extra non-character phases, as in the Fano example. The analytic proof does not establish that this theorem is absent from unindexed historical inequalities, and no independent audit is asserted. The finite checker is a reproducibility check only.

## References
1. M. Fickus, J. Jasper, D. G. Mixon, J. D. Peterson, *Hadamard Equiangular Tight Frames*, arXiv:1703.05353v1, first public 2017-03-15, primary MSC 42C15. https://arxiv.org/abs/1703.05353
2. M. Fickus, C. A. Schmitt, *Harmonic equiangular tight frames comprised of regular simplices*, arXiv:1903.09177v1, first public 2019-03-21, primary MSC 42C15. https://arxiv.org/abs/1903.09177
3. *Sharp fourth-moment extension and exact deficit for finite abelian difference sets*, published 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-exact-deficit-for-finite-abeli--f000b50fe5d9
4. *Sharp sixth moment and complete extremizers for the Fano Singer spectrum*, published 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moment-and-complete-extremizers-for-the-fano-singer--5260cc41f9aa
5. *Sharp sixth-moment constant for finite subgroup-hole spectra*, published 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moment-constant-for-finite-subgroup-hole-spectra--1b6345819859
