# Range invariance is the exact missing hypothesis in an atomic-subspace transport theorem

## Finding
Theorem 4.6 of Ghosh--Samanta states that if \(\Lambda\) is a \(g\)-atomic subspace with respect to \(K\) and \(U\) is positive and invertible, then the transported family built from \(I+U\) is again a \(g\)-atomic subspace with respect to the same \(K\). This is false without a range-compatibility hypothesis between \(I+U\) and \(K\).

Take
\[
H=\mathbb R^2,\qquad
K=P_{\operatorname{span}\{e_1\}}
=
\begin{pmatrix}1&0\\0&0\end{pmatrix},
\]
with one component
\[
J=\{1\},\qquad W_1=H,\qquad v_1=1,\qquad \Lambda_1=K^*=K.
\]
Then
\[
\|\Lambda_1f\|^2=\|K^*f\|^2,
\]
so \(\Lambda\) is a Parseval \(K\)-\(g\)-fusion frame. By the paper's Theorem 4.2, it is a \(g\)-atomic subspace with respect to \(K\).

Now choose
\[
U=
\begin{pmatrix}
1&1/2\\
1/2&1
\end{pmatrix},
\qquad
A:=I+U=
\begin{pmatrix}
2&1/2\\
1/2&2
\end{pmatrix}.
\]
The eigenvalues of \(U\) are \(1/2\) and \(3/2\), so \(U\) is positive and invertible. Since \(W_1=H\), the transported family in Theorem 4.6 has analysis operator
\[
\Lambda_1A=KA.
\]
For
\[
f=(1,-4)
\]
one has
\[
Af=(0,-15/2),
\qquad
KAf=0,
\qquad
K^*f=e_1.
\]
Hence the transformed family cannot satisfy any positive lower \(K\)-\(g\)-fusion-frame bound.

For a fixed invertible operator \(A\), the exact universal condition ensuring that this transport preserves every \(K\)-\(g\)-fusion frame is
\[
R(K)\subseteq R(AK).
\]
Equivalently, there is a constant \(c>0\) such that
\[
KK^*\le c\,AKK^*A^*.
\]
For Theorem 4.6, the elementary additional hypothesis
\[
UK=KU
\]
is sufficient, because then \(A=I+U\) commutes with \(K\) and therefore \(R(AK)=R(K)\).

## Assumptions and scope
The counterexample uses exactly the paper's setting and its own equivalence theorem between \(g\)-atomic subspaces and \(K\)-\(g\)-fusion frames. No infinite-dimensional phenomenon, convergence issue, or degenerate controller is involved.

The exact range criterion is a universal preservation statement for a fixed invertible transport \(A\): it characterizes when every \(K\)-\(g\)-fusion frame remains one after the corresponding transported construction. It does not claim that a particular frame must fail whenever the range condition fails; the one-component Parseval frame provides the necessary witness.

## Proof
Let \(S_\Lambda\) denote the frame operator of a \(K\)-\(g\)-fusion frame. Then for some \(\alpha>0\),
\[
S_\Lambda\ge \alpha KK^*.
\]
Under an invertible transport \(A\), the paper's calculation gives the transformed frame operator
\[
S'_\Lambda=AS_\Lambda A^*.
\]

Suppose first that
\[
R(K)\subseteq R(AK).
\]
Douglas' factorization theorem is equivalent to the existence of \(c>0\) with
\[
KK^*\le c\,AKK^*A^*.
\]
Therefore
\[
S'_\Lambda
=
AS_\Lambda A^*
\ge
\alpha AKK^*A^*
\ge
\frac{\alpha}{c}KK^*.
\]
The transported family is thus again a \(K\)-\(g\)-fusion frame, with its upper Bessel bound following from boundedness of \(A\).

Conversely, suppose the transport preserves every \(K\)-\(g\)-fusion frame. Use the one-component family \(W_1=H\), \(v_1=1\), \(\Lambda_1=K^*\). Its frame operator is \(KK^*\), and it is Parseval relative to \(K\). The transported frame operator is
\[
AKK^*A^*.
\]
Preservation of the lower \(K\)-bound forces
\[
KK^*\le c\,AKK^*A^*
\]
for some \(c>0\), and Douglas' theorem gives
\[
R(K)\subseteq R(AK).
\]
This proves necessity and sufficiency.

For the explicit \(2\times2\) example,
\[
R(K)=\operatorname{span}\{e_1\},
\qquad
R(AK)=\operatorname{span}\{(2,1/2)\},
\]
so the exact criterion fails.

The source proof instead writes
\[
AS_\Lambda A^*\ge S_\Lambda
\]
from positivity of \(U=A-I\) and \(S_\Lambda\). That operator-order implication is not valid in general without additional commutation. More importantly, even invertibility and positivity of \(A\) alone do not imply preservation of the fixed range \(R(K)\), which is the exact obstruction above.

## Verification
The source full text was inspected at Theorem 4.2, Theorem 4.4, Corollary 4.5, and Theorem 4.6. Theorem 4.2 identifies \(g\)-atomic subspaces with \(K\)-\(g\)-fusion frames. Theorem 4.4 explicitly assumes commutation of its transport with \(K\), while Theorem 4.6 drops that compatibility and then uses the unsupported order step described above.

All calculations in the counterexample are exact. The matrix \(U\) is positive invertible because its eigenvalues are \(1/2\) and \(3/2\). The vector \(f=(1,-4)\) gives \(KAf=0\) while \(K^*f=e_1\), which immediately contradicts any positive lower \(K\)-frame bound.

No finite experiment, numerical optimization, or approximate certificate is used.

## Relationship to prior work
Douglas' range-factorization theorem supplies the exact equivalence between
\[
R(K)\subseteq R(AK)
\]
and domination of \(KK^*\) by \(AKK^*A^*\); that theorem is prior input, not a novelty claim.

The source itself already imposes the commutation condition \(K(U+V)=(U+V)K\) in Theorem 4.4 and Corollary 4.5 when transporting \(g\)-atomic subspaces. This makes the absence of any corresponding range-compatibility condition in Theorem 4.6 mathematically significant rather than cosmetic.

Targeted searches for the exact source, Theorem 4.6, positive-invertible transport, range-invariance formulations, and noncommuting \(K\)-\(g\)-fusion-frame transport did not locate an indexed correction or an equivalent source-specific counterexample. Closest indexed work concerns other range-compression, perturbation, and operator-orbit questions rather than this theorem.

## Limitations
The simple repair \(UK=KU\) is sufficient but stronger than the exact universal condition \(R(K)\subseteq R((I+U)K)\). No claim is made that commutation is necessary.

The result addresses Theorem 4.6 and its iterated variant only through the first-step failure. It does not audit unrelated statements in the paper. An unindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. P. Ghosh and T. K. Samanta, *Generalized atomic subspaces for operators in Hilbert spaces*, arXiv:2102.01965v1, 3 February 2021; Mathematica Bohemica 147 (2022), 325--345, DOI 10.21136/MB.2021.0130-20.
2. R. G. Douglas, *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proceedings of the American Mathematical Society 17 (1966), 413--415.
