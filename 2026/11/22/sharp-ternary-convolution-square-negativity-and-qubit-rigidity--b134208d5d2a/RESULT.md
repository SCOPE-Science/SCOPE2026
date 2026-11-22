# Sharp ternary convolution-square negativity and qubit rigidity

## Finding

Let \(G=\mathbb Z/3\mathbb Z\) and \(n\ge 1\). Every positive, normalized matrix-valued measure
\[\mu=A_0\delta_0+A_1\delta_1+A_2\delta_2,\qquad A_j\in M_n(\mathbb C),\quad A_j\succeq0,\quad A_0+A_1+A_2=I_n\]
has a Hermitian convolution square at each group element and satisfies the **sharp uniform Loewner inequality**
\[\boxed{(\mu*\mu)(k)\succeq-\tfrac1{24}I_n\quad\text{for all }k\in G.}\]
Here \((\mu*\mu)(k)=\sum_{a+b=k} A_aA_b\), with multiplication in the displayed order. For each \(n\ge2\), equality of the least eigenvalue with \(-1/24\) at a specified \(k\) occurs if and only if, after renaming its square atom \(C\) and its two mixed atoms \(A,B\), the triple is simultaneously unitarily equivalent to an orthogonal direct sum of the following **forced two-dimensional block** and an arbitrary normalized positive triple:
\[
A_*=\begin{pmatrix}\frac12&\frac{\sqrt{30}}{12}\\\frac{\sqrt{30}}{12}&\frac5{12}\end{pmatrix},\quad
B_*=\begin{pmatrix}\frac12&-\frac{\sqrt{30}}{12}\\-\frac{\sqrt{30}}{12}&\frac5{12}\end{pmatrix},\quad
C_*=\begin{pmatrix}0&0\\0&\frac16\end{pmatrix}.
\]
The sharp negative convolution phenomenon is impossible for scalar-valued positive measures, and also impossible for normalized positive matrix-valued measures on groups of order at most two. Hence the three-element group and a two-dimensional coefficient space are simultaneously minimal.

## Assumptions and scope

The coefficient matrices are arbitrary finite-dimensional complex Hermitian positive-semidefinite matrices, including singular matrices. Normalization is exactly \(\mu(G)=I_n\), not trace normalization. Convolution is ordered matrix convolution on the additive three-cycle, without assuming pairwise commutativity or convolution idempotence. The eigenvalue bound is claimed for each of the three convolution-square coefficients separately. The equality classification concerns *attaining the lower eigenvalue*, not a requirement that the whole coefficient equal a scalar matrix.

For any \(k\), the unordered solutions of \(a+b=k\) contain one diagonal pair and one pair of reverse mixed terms, so one can write \((\mu*\mu)(k)=C^2+AB+BA\) for some permutation \((A,B,C)\) of the three positive coefficients. Thus the coefficient is Hermitian.

## Proof

**1. A positive effect inequality.** Let \(A,B,C\succeq0\) satisfy \(A+B+C=I_n\). Define \(S=A+B=I_n-C\) and \(X=A-B\). Then \(0\preceq S\preceq I_n\), \(-S\preceq X\preceq S\), and \(X=X^*\). On the support of \(S\), the contraction factorization \(X=S^{1/2}YS^{1/2}\) holds with \(Y=Y^*\) and \(-I\preceq Y\preceq I\); extend \(Y\) by zero on \(\ker S\). Consequently,
\[
X^2=S^{1/2}YSYS^{1/2}\preceq S^{1/2}Y^2S^{1/2}\preceq S.
\]
The first inequality uses \(S\preceq I_n\) and remains valid despite noncommutativity; the second uses \(Y^2\preceq I_n\).

**2. Sharp sum-of-squares decomposition.** Since \(AB+BA=(S^2-X^2)/2\) and \(S=I_n-C\), direct expansion yields
\[
\boxed{AB+BA+C^2+\frac1{24}I_n
=\frac12(S-X^2)+\frac32\left(C-\frac16 I_n\right)^2\succeq0.}
\]
This proves the asserted inequality for every convolution-square coefficient, in all dimensions.

**3. Exact sharpness.** Set \(A=A_*\), \(B=B_*\), \(C=C_*\) as in the theorem. These matrices are positive (the first two have determinant zero and eigenvalues \(0,11/12\)), and their sum equals \(I_2\). With \(X=A-B\) and \(S=A+B\),
\[S=\operatorname{diag}(1,5/6),\quad X=\sqrt{5/6}\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
AB+BA+C^2=\operatorname{diag}(1/12,-1/24).\]
Take \(\mu(0)=A\), \(\mu(1)=B\), \(\mu(2)=C\), for which the convolution coefficient at \(1\) equals \(AB+BA+C^2\). Orthogonally adjoining any positive normalized triple, including scalar diagonal blocks, attains the same eigenvalue for all \(n\ge2\).

**4. Rigidity of equality.** Suppose a unit vector \(v\) satisfies \((AB+BA+C^2)v=-v/24\). Both positive terms in Step 2 then annihilate \(v\). Therefore
\[Cv=\tfrac16v,\qquad X^2v=Sv=\tfrac56v.\]
Put \(z=S^{1/2}v\), and use the factorization of Step 1. The positive identity
\[
S-X^2=S^{1/2}(I-Y^2)S^{1/2}+S^{1/2}Y C YS^{1/2}
\]
shows that both \((I-Y^2)z=0\) and \(C^{1/2}Yz=0\). Thus \(CYz=0\); the latter vector lies in the \(S\)-eigenspace of eigenvalue \(1\), so \(CXv=C S^{1/2}Yz=0\). Define \(w=\sqrt{6/5}\,Xv\). Then \(\|w\|=1\), \(Cw=0\), and \(w\perp v\) because \(Cv=v/6\). Moreover
\[Xv=\sqrt{5/6}\,w,\qquad Xw=\sqrt{5/6}\,v.\]
The subspace \(\operatorname{span}\{w,v\}\) therefore reduces both \(C\) and \(X\), hence also \(S=I_n-C\) and \(A=(S+X)/2\), \(B=(S-X)/2\). In the ordered orthonormal basis \((w,v)\) their two-dimensional restrictions are exactly \((A_*,B_*,C_*)\); positivity and normalization hold separately on the orthogonal complement. Conversely, any such orthogonal direct sum has eigenvalue \(-1/24\) by Step 3. No irreducibility assumption is needed.

**5. Minimality.** For scalar coefficients, convolution of nonnegative measures has nonnegative coefficients on every group. A group of order one is trivial. On the two-cycle, writing \(\mu=A\delta_0+B\delta_1\) with \(A+B=I_n\), the matrices commute because \(B=I_n-A\), and its convolution square has coefficients \(A^2+B^2\) and \(2AB\), both positive semidefinite. The two-cycle argument works in every matrix dimension, whereas Step 3 supplies a noncommutative \(2\times2\) realization on the three-cycle.

## Verification

The self-contained file `verify_z3_effects.py` verifies the witness and the exact contact polynomial symbolically using rational arithmetic and radicals. It also tests 9,000 matrix-convolution coefficients generated from positive random effects across six finite dimensions, plus 999 points on a rank-one extremal family. These finite tests are supplementary only; Steps 1–5 provide the proof for all finite dimensions. Run with `python verify_z3_effects.py` using Python with `sympy` and `numpy` installed.

## Relationship to prior work

Jabbari's November 2026 matrix Kawada–Itô theorem establishes **automatic commutativity at convolution idempotents** for positive matrix-valued measures on arbitrary locally compact groups, and notes that general positive matrix-valued convolutions need not remain positive. Its classification assumes \(\mu*\mu=\mu\); the present theorem instead fixes total mass \(I_n\), drops idempotence, and gives the sharp negative spectral excursion together with complete equality rigidity on the smallest possible nontrivial group. Neither claim entails the other through the stated hypotheses.

Deng (2013) studies sequential and Jordan products of quantum effects and algebraic operator conditions, rather than the sharp summed three-effect lower bound for ordered group convolution. Girard–Plávala–Sikora study Jordan products of quantum channels and compatibility. Guo–Luo (2024) consider negativity of Jordan products of POVM effects; their abstract is relevant, but their complete article was not accessible for a decisive detailed comparison. This is a residual bibliographic originality risk, not evidence of coverage or priority.

## Limitations

The theorem concerns square convolution **only** on the three-cycle, normalized by matrix mass. It makes no claim that the convolution-square measure is positive, nor that arbitrary groups share the same universal sharp constant. The equality theorem classifies a lower spectral contact, not all spectra, nor minimizers under other normalizations. The result is established by self-review and numerical/symbolic ancillary checks; no independent audit has been performed. Bibliographic priority remains uncertain because a closely related 2024 Jordan-negativity paper could not be examined in full.

## References

1. A. Jabbari, *The Matrix Kawada–Itô Theorem and Harmonic Rigidity on Locally Compact Groups*, arXiv:2611.09755, first public version November 6, 2026. https://arxiv.org/abs/2611.09755
2. C. Deng, *A Note on Sequential Product of Quantum Effects*, Abstract and Applied Analysis 2013, article 520436. https://doi.org/10.1155/2013/520436
3. M. Girard, M. Plávala, J. Sikora, *Jordan products of quantum channels and their compatibility*, Nature Communications 12, 2129 (2021), arXiv:2009.03279. https://arxiv.org/abs/2009.03279
4. Y. Guo, S. Luo, *Quantifying incompatibility between positive operator-valued measures via negativity of the Jordan product*, Physical Review A 110, 062206 (2024). https://doi.org/10.1103/PhysRevA.110.062206
