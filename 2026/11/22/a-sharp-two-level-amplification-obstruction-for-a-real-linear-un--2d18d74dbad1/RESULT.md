# A sharp two-level amplification obstruction for a real-linear unitary preserver

## Finding
Define the real-linear map \(\Phi:M_2(\mathbb C)\to M_2(\mathbb C)\) by
\[
\Phi\!\left(\begin{bmatrix}a&b\\c&d\end{bmatrix}\right)=
\begin{bmatrix}a&b\\-\overline b&\overline a\end{bmatrix}.
\]
It fixes the identity and sends **every** two-by-two complex unitary to a special unitary. At matrix level \(k\geq1\), let \(\Phi^{(k)}\) act entrywise on \(M_k(M_2(\mathbb C))\) with the ordinary \(M_{2k}(\mathbb C)\) operator norm. Then
\[
\boxed{\ \|\Phi^{(1)}\|=1,\qquad
\|\Phi^{(k)}\|=\sqrt{2}\quad\text{for all integers }k\geq2.\ }
\]
More sharply, for every \(k\geq2\) there is a **unitary** \(U_k\in M_k(M_2(\mathbb C))\) with \(\|\Phi^{(k)}(U_k)\|=\sqrt 2\). Thus the first possible matricial level already destroys unitary preservation, by exactly the largest possible operator-norm factor, even though the unamplified map preserves every unitary and has norm one.

## Assumptions and scope
All matrix algebras are over \(\mathbb C\), and \(\Phi\) is **real-linear**, not complex-linear. A block matrix \(X=[X_{ij}]\in M_k(M_2(\mathbb C))\) has norm as an operator on \(\mathbb C^k\otimes\mathbb C^2\); \(\Phi^{(k)}X=[\Phi(X_{ij})]\). The matrix-size parameter is **every integer** \(k\ge1\). No assumption of positivity, multiplicativity or complex-linearity is made. In this statement, the all-level amplification norm means the explicit supremum of these real-linear operator norms, avoiding any convention-dependent usage of complex-linear completely bounded maps.

## Proof
**Unamplified unitary preservation and norm.** For any \(a,b\in\mathbb C\), put
\[
Q(a,b)=\begin{bmatrix}a&b\\-\overline b&\overline a\end{bmatrix}.
\]
Direct multiplication gives \(Q(a,b)Q(a,b)^*=(|a|^2+|b|^2)I_2\) and \(\det Q(a,b)=|a|^2+|b|^2\). If \(U\in U(2)\), its first row has squared Euclidean norm one, so \(\Phi(U)=Q(u_{11},u_{12})\in SU(2)\). Also \(\|\Phi(X)\|=\sqrt{|a|^2+|b|^2}\le\|X\|\) for every \(X=\bigl[\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr]\), and equality occurs at \(I_2\); hence \(\|\Phi\|=1\).

**Upper bound at every matricial level.** Perform the standard unitary row/column permutation that changes the tensor-factor order from \(\mathbb C^k\otimes\mathbb C^2\) to \(\mathbb C^2\otimes\mathbb C^k\). In the reordered coordinates every input and its image have the forms
\[
X=\begin{bmatrix}A&B\\C&D\end{bmatrix},\qquad
\Phi^{(k)}X=Y=\begin{bmatrix}A&B\\-\overline B&\overline A\end{bmatrix},
\]
where \(A,B,C,D\in M_k(\mathbb C)\), and the bar denotes **entrywise** complex conjugation (not transpose). Put \(P=[A\ B]\) and \(R=[-\overline B\ \overline A]\). A row compression gives \(\|P\|\le\|X\|\). Moreover,
\[
RR^*=\overline{BB^*+AA^*}=\overline{PP^*},
\qquad \|R\|=\|P\|.
\]
For each column vector \(v\), \(\|Yv\|^2=\|Pv\|^2+\|Rv\|^2\le 2\|P\|^2\|v\|^2\). Thus \(\|\Phi^{(k)}X\|\le\sqrt2\|X\|\) for all \(k\). (The sharper \(k=1\) estimate was proved above.)

**Sharp unitary witness at level two.** Let
\[
J=\begin{bmatrix}0&1\\-1&0\end{bmatrix},\qquad
W=\begin{bmatrix}I_2&J\\J&I_2\end{bmatrix},\qquad
Z=\begin{bmatrix}I_2&J\\-J&I_2\end{bmatrix}.
\]
As \(J^*=-J\) and \(J^2=-I_2\), direct multiplication yields \(WW^*=2I_4\), \(Z=Z^*\), and \(Z^2=2Z\). Consequently \(U_2=W/\sqrt2\) is unitary, while \(Z/\sqrt2\) has norm \(\sqrt2\). Viewed in the reordered block coordinates, the first block row of \(U_2\) is \([I_2\ J]/\sqrt2\); hence \(\Phi^{(2)}(U_2)=Z/\sqrt2\) after the same tensor-factor permutation. For \(k>2\), append identity blocks on the unused \(k-2\) coordinates in each of the two tensor-factor sectors. The resulting input remains unitary, its image contains \(Z/\sqrt2\) as a reducing summand, and the universal upper bound forces its norm to equal \(\sqrt2\). This proves both sharpness and the asserted unitary witnesses at every \(k\ge2\).

The map is genuinely non-Jordan: for matrix units, \(E_{12}\circ E_{21}=I_2/2\), whereas \(\Phi(E_{21})=0\) and \(\Phi(E_{12})=J\). Thus \(\Phi(E_{12}\circ E_{21})=I_2/2\ne0=\Phi(E_{12})\circ\Phi(E_{21})\).

## Verification
The upper estimate and its attainment are exact identities valid in every matrix size. The accompanying `CHECK.py` verifies the unnormalized witness identities using symbolic matrices and checks the norm inequalities for reproducible finite random complex matrices at sizes \(k=1,2,3,4,6\). Its output is `AMPLIFICATION_CHECK_OK 301`. This diagnostic is not the proof of the universal bound; the row-compression argument above supplies that proof.

## Relationship to prior work
Cui, Wu and Yuan classify unital real-linear unitary preservers and identify the exceptional non-Jordan two-dimensional cases (arXiv:2611.13822v1, Theorem 4.3 and Corollary 4.5). Their Lemma 2.4 establishes the ordinary norm-one property of unital real-linear unitary preservers. These structural and norm-one facts are acknowledged as prior work. The present claim instead computes the **exact norms of every entrywise matrix amplification of one canonical non-Jordan preserver**, and exhibits a norm-attaining **unitary** at the minimal failing level. The source contains no calculation of that amplification constant or matrix-level witness. General operator-space results, including the row/column factorization framework of Pisier and Shlyakhtenko, provide context for matrix norms but are not the stated exact calculation for this map.

## Limitations
The theorem concerns the explicitly defined \(\Phi\), not a classification of amplification norms for **all** real-linear unitary preservers. No complex-linear completely bounded conclusion is asserted: the map is real-linear and the amplification norms are defined directly. The search did not eliminate the possibility that an older quaternionic operator-space formulation implicitly contains the same constant. No independent mathematical audit has been performed.

## References
1. Lu Cui, Wenming Wu and Wei Yuan, *\(\mathbb R\)-linear unitary preservers of \(C^*\)-algebras*, arXiv:2611.13822v1, posted 2026-11-10, https://arxiv.org/html/2611.13822v1, especially Lemma 2.4, Theorem 4.3 and Corollary 4.5.
2. Gilles Pisier and Dimitri Shlyakhtenko, *Grothendieck's Theorem for Operator Spaces*, arXiv:math/0108205, 2001, https://arxiv.org/abs/math/0108205 (general matrix-norm context, not this calculation).
