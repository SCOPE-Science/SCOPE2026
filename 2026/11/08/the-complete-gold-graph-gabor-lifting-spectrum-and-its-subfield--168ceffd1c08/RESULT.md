# The complete Gold-graph Gabor lifting spectrum and its subfield transition

## Finding

Let \(m\ge2\), \(1\le r<m\), \(q=2^m\), \(h=\gcd(m,r)\), \(K=2^h\), and \(u=m/h\). On the additive group \(G=\mathbb F_q^2\), of order \(N=q^2\), take the unnormalized binary graph window
\[
 g(x,y)=\mathbf1_{\{y=x^{2^r+1}\}}.
\]
For translation \(s\in G\), modulation by an additive character \(\xi\in\widehat G\), and \(g_{s,\xi}=M_\xi T_sg\), define the complex-linear full intensity-lifting map
\[
 \mathcal L_g:\operatorname{End}(\mathbb C^G)\longrightarrow\mathbb C^{G\times\widehat G},\qquad
 \mathcal L_g(H)_{s,\xi}=\operatorname{tr}(H g_{s,\xi}g_{s,\xi}^*).
\]
Both spaces carry their unnormalized Hilbert--Schmidt/Euclidean norms. The **complete singular-value multiset** of this operator is the following (add multiplicities if singular values coincide):

* In **both** branches, \(q^2\) occurs once, and \(qK\) occurs \((q-1)q^3/K^2\) times.
* If \(u\) is **odd**, \(q\sqrt{qK}\) occurs \((q-1)q/K\) times.
* If \(u\) is **even**, \(q\sqrt q\) occurs \((q-1)Kq/(K+1)\) times, and \(qK\sqrt q\) occurs \((q-1)q/[K^2(K+1)]\) times.
* Every remaining singular value is zero, so that the complete count (including zeros) is \(q^4\).

In particular, the exact complex-linear rank is
\[
\boxed{
\operatorname{rank}\mathcal L_g=
\frac{(q-1)q^3}{K^2}+1+
\begin{cases}
(q-1)q/K,&u\text{ odd},\\[2pt]
(q-1)q(K^2-K+1)/K^2,&u\text{ even},
\end{cases}}
\]
and the positive-spectrum condition number is **exactly**
\[
\boxed{\kappa^+(\mathcal L_g)=q/K.}
\]
The kernel is the Weyl-operator span indexed by the zero ambiguity coefficients described explicitly below. The result has a genuine subfield transition between odd and even \(m/\gcd(m,r)\), even though the nonzero-translation ambiguity contribution is the same in both branches.

## Assumptions and scope

The exponent \(r\) is strictly between zero and \(m\). A nontrivial additive character of \(\mathbb F_q\) is \(\psi(z)=(-1)^{\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(z)}\); frequencies are paired with positions by \(\psi(bx+dy)\). The graph indicator has entries zero or one, not unit \(\ell^2\) norm. Time-frequency shifts are defined by \((T_sg)(z)=g(z-s)\) and \((M_\xi g)(z)=\xi(z)g(z)\). The singular values refer to the complete complex-linear matrix-domain lift, not to a nonlinear phase-retrieval map or a restriction to Hermitian matrices.

For \((a,c;b,d)\in\mathbb F_q^4\), define the unnormalized ambiguity coefficient
\[
 A_g(a,c;b,d)=\sum_{(x,y)\in G}g(x,y)g(x+a,y+c)\psi(bx+dy).
\]
All ensuing statements are unchanged in magnitude if conjugate or opposite-modulation conventions are used. For \(a\ne0\), let
\[
 D_a(x)=(x+a)^{2^r+1}+x^{2^r+1}
\]
and \(C_a=D_a(\mathbb F_q)\); every \(C_a\) has \(q/K\) members. Let \(R_d\) denote the radical of the polar bilinear form of the Boolean quadratic function \(Q_d(x)=\operatorname{Tr}(d x^{2^r+1})\) for \(d\ne0\). The **exact zero/nonzero support**, beyond the magnitude counts below, has a direct character-test description: if \(a\ne0\) and \(c\in C_a\), choose any \(x_0\) with \(D_a(x_0)=c\). Then \(A_g(a,c;b,d)\ne0\) exactly when
\[
\operatorname{Tr}\!\left((ba+d(a^{2^r}x_0+ax_0^{2^r}))t+da^{2^r+1}t^2\right)=0
\quad\text{for all }t\in\mathbb F_K.
\]
For \(a=c=0\), \(d\ne0\), the equivalent test is \(\operatorname{Tr}(bt)=Q_d(t)\) for all \(t\in R_d\). For \(a=c=d=0\), only \(b=0\) survives. All other shifts not meeting these conditions give zero. Consequently these conditions specify the entire Weyl-basis kernel without external data.

## Proof

**1. Nonzero translation fibers.** In characteristic two,
\[
D_a(x)=a^{2^r+1}+a^{2^r}x+ax^{2^r}.
\]
Writing \(x=at\), its linear part is \(a^{2^r+1}(t+t^{2^r})\). Its kernel consists exactly of \(a\mathbb F_K\), since the fixed field of the Frobenius power \(t\mapsto t^{2^r}\) is \(\mathbb F_{2^h}\). Therefore \(D_a\) takes \(q/K\) values and every nonempty fiber is \(x_0+a\mathbb F_K\), of size \(K\).

If \(a\ne0\), then \(A_g(a,c;b,d)=0\) for \(c\notin C_a\). For \(c\in C_a\), substitute \(x=x_0+at\), \(t\in\mathbb F_K\). The exponent in the ambiguity sum becomes, apart from a constant,
\[
\operatorname{Tr}\Bigl((ba+d(a^{2^r}x_0+ax_0^{2^r}))t+da^{2^r+1}t^2\Bigr).
\]
Both \(t\mapsto t\) and \(t\mapsto t^2\) are additive on \(\mathbb F_K\). Thus this is a linear functional of \(t\) over \(\mathbb F_2\). Orthogonality of its additive character gives ambiguity magnitude either \(0\) or \(K\). For fixed \((a,c,d)\), the varying parameter \(b\in\mathbb F_q\) restricts surjectively onto the dual of \(a\mathbb F_K\): this follows from nondegeneracy of the absolute trace pairing and \(a\ne0\). Exactly \(q/K\) choices of \(b\) make the functional zero. Hence the full count for nonzero \(a\) is
\[
\#\{(a,c;b,d):a\ne0,\ |A_g|=K\}
=(q-1)\frac qK\,q\,\frac qK
=\frac{(q-1)q^3}{K^2}.
\]
All remaining nonzero-translation coefficients vanish. If \(a=0,c\ne0\), the graph and its vertical translate are disjoint, so all coefficients vanish.

**2. Zero translation and binary quadratic radicals.** For \(a=c=0\),
\[
 A_g(0,0;b,d)=\sum_{x\in\mathbb F_q}\psi(bx+dx^{2^r+1}).
\]
When \(d=0\), this equals \(q\) only for \(b=0\). When \(d\ne0\), polarizing \(Q_d\) gives
\[
 B_d(x,t)=\operatorname{Tr}\bigl(d(x^{2^r}t+xt^{2^r})\bigr).
\]
Its radical condition, after applying the \(2^r\)-Frobenius power, is
\[
 d^{2^r}t^{2^{2r}}+dt=0.
\]
For nonzero \(t\), equivalently \(t^{2^{2r}-1}=d^{1-2^r}\). If \(u\) is odd, \(\gcd(m,2r)=h\); since \(2^h-1\) divides \(2^r-1\), this multiplicative equation has \(K-1\) nonzero solutions for every \(d\ne0\). Thus \(|R_d|=K\).

If \(u\) is even, then \(r/h\) is odd and \(\gcd(m,2r)=2h\). A cyclic-group exponent calculation shows that the equation has \(K^2-1\) nonzero solutions **if and only if** \(d\) belongs to the subgroup of \((K+1)\)-st powers of \(\mathbb F_q^*\), a group of order \((q-1)/(K+1)\); otherwise it has no nonzero solutions. More explicitly, if \(\zeta\) generates \(\mathbb F_q^*\) and \(d=\zeta^e\), solvability is equivalent to \(K^2-1\) dividing \(e(2^r-1)\). Since \((2^r-1)/(K-1)=1+K+\cdots+K^{r/h-1}\equiv1\pmod{K+1}\), this is precisely \(K+1\mid e\). Thus \(|R_d|=K^2\) for \((q-1)/(K+1)\) nonzero \(d\), and \(|R_d|=1\) for the remaining \((q-1)K/(K+1)\).

For completeness, the Walsh profile of any Boolean quadratic form follows exactly from the polar radical, without external numerical input. Expanding a square and setting \(y=x+t\) gives
\[
 \left|\sum_x(-1)^{Q_d(x)+\operatorname{Tr}(bx)}\right|^2
 =q\sum_{t\in R_d}(-1)^{Q_d(t)+\operatorname{Tr}(bt)}.
\]
Because \(Q_d\) is additive on \(R_d\), the right side is either \(q|R_d|\) or zero, with exactly \(q/|R_d|\) nonzero \(b\)'s. For odd \(u\), this yields \((q-1)q/K\) coefficients of modulus \(\sqrt{qK}\). For even \(u\), it yields \((q-1)q/[K^2(K+1)]\) of modulus \(K\sqrt q\) and \((q-1)Kq/(K+1)\) of modulus \(\sqrt q\). There is additionally one coefficient of modulus \(q\). These counts include every zero-translation frequency.

**3. Weyl diagonalization and normalization.** The Weyl operators \(\Pi_{s,\xi}=M_\xi T_s\), normalized as \(\Pi_{s,\xi}/\sqrt N\), form an orthonormal basis of \(\operatorname{End}(\mathbb C^G)\). Conjugating the rank-one projector \(P=gg^*\) by every Weyl operator multiplies its Weyl coefficient by a character of \(G\times\widehat G\). Hence the output of \(\mathcal L_g\) on a normalized Weyl basis vector is a character vector, of norm \(\sqrt N\,|A_g(s,\xi)|\), and different Weyl inputs give orthogonal output character vectors. This proves that the singular-value multiset is exactly \(\{\sqrt N|A_g(s,\xi)|\}\); here \(\sqrt N=q\). It also identifies the kernel as the span of Weyl operators with zero ambiguity coefficient.

The amplitude histogram from steps 1--2 gives every multiplicity and the displayed rank. Since \(u\ge2\) and \(q\ge K^2\), the smallest positive ambiguity magnitude is \(K\), and the largest is \(q\). Thus the positive condition number is \(q/K\). When \(u=2\), two pairs of listed positive singular values coincide; the instruction to add multiplicities handles this boundary exactly. No inference about nonlinear recovery follows from the complex-linear rank alone.

## Verification

The standalone script `artifacts/verify_gold_gabor.py` constructs fields in a polynomial basis, all graph overlaps, and every binary Walsh ambiguity coefficient by an exact integer Walsh--Hadamard transform. It checks the complete histogram for \(q=4,8,16,32\) and all listed \(r\) values, including both parity branches and the coinciding-value boundary at \(m=2h\). It additionally constructs the full \(256\times256\) Gabor-projector Gram matrix when \(q=4\) and verifies the predicted Gram eigenvalues numerically (this optional final check requires NumPy). The finite exact enumeration reports `GOLD_GABOR_ALL_EXACT_TESTS_PASS`; the direct Gram check reports `direct_projector_Gram_eigenvalues_q4=PASS`.

These experiments corroborate, but do not replace, the universal proofs of the derivative fibers, radicals, character orthogonality, and Weyl diagonalization. Reproduce by running `python3 artifacts/verify_gold_gabor.py` from the directory containing this result.

## Relationship to prior work

Feichtinger, Kozek and Luef [1] establish finite-abelian Gabor and spreading-operator methods. Bojarovska and Flinth [2, Section 2.2, particularly Theorem 2.3 and its proof] give the general Gabor lifting/ambiguity diagonalization and injectivity criteria. These are antecedents for the last step above, not claimed as new. Anbar, Meidl and Topuzoglu [3, Introduction and quadratic-Walsh theory] explain the general radical/plateaued Walsh framework; the quadratic-radical mechanism is classical. The Gold exponent and its derivative fibers are classical as well.

Two closely related published studies address the **same binary Gold graph** but a different operator: *Exact fourth moments and line-affine phase extremizers for Gold graphs* [4] studies the sharp Fourier-extension fourth moment and complex coefficient extremizers; *Phase-rigid sharp fourth moments for characteristic-two APN graph extension* [5] studies a related extension inequality for APN maps. The full texts inspected give derivative-fiber identities but no full time-frequency-shifted graph projector spectrum or all-Weyl-coefficient rank law. The original result asserted here is the resulting **complete Gabor lifting singular-value/multiplicity law**, including both subfield branches and the exact condition number, not the underlying classical quadratic sums, Gold derivatives, or general Gabor diagonalization.

## Limitations

Only complete (all-shift, all-modulation) complex-linear intensity lifting is classified. The rank does **not** establish nonlinear phase retrieval, sparse recovery, robustness after erasures, or uniqueness for arbitrary signals. The coefficient phases are not classified, only exact magnitudes, support counts, and the resulting singular spectrum. The sources listed establish essential general ingredients, and it remains possible that an unlocated older specialization or a stronger existing Gold-ambiguity theorem covers the explicit combined law. Independent validation has not been performed.

## References

1. H. G. Feichtinger, W. Kozek, F. Luef, *Gabor analysis over finite Abelian groups*, arXiv:math/0703228 (first posted 2007-03-08), Sections 3--4. https://arxiv.org/abs/math/0703228
2. I. Bojarovska, A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (first posted 2015-03-19), Section 2.2. https://arxiv.org/html/1503.05800v2
3. N. Anbar, W. Meidl, A. Topuzoglu, *Idempotent and p-potent quadratic functions: Distribution of nonlinearity and co-dimension*, arXiv:1603.04685 (first posted 2016-03-15), especially Section 1. https://arxiv.org/abs/1603.04685
4. *Exact fourth moments and line-affine phase extremizers for Gold graphs*, published mathematical research record, 2026-10-11, scientific statement and proof. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-fourth-moments-and-line-affine-phase-extremizers-for-gold--150031da8dce/RESULT.md
5. *Phase-rigid sharp fourth moments for characteristic-two APN graph extension*, published mathematical research record, 2026-10-11, scientific statement and proof. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-phase-rigid-sharp-fourth-moments-for-characteristic-two-apn-grap--673d8a1f1945/RESULT.md
