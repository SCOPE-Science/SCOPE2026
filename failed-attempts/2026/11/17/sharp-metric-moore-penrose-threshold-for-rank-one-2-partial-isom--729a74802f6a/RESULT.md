# Sharp metric Moore–Penrose threshold for rank-one \(2\)-partial isometries

## Finding
For every nonzero rank-one \(2\)-partial isometry \(T\) on the complex Hilbert plane, put \(S=2T^*-(T^*)^2T\). There exists a positive-definite Hermitian inner product with respect to which \(S\) is the Moore–Penrose inverse of \(T\) **if and only if** \(\|T\|<\sqrt2\). This threshold is sharp; all permitted operator norms at least \(1/\sqrt2\) occur. In particular, the general assertion posed in Question 6 of Aouichaoui–Buchała–Garcia is false, already in complex dimension two.

An exact counterexample, in the standard orthonormal basis, is
\[
T_0=\frac1{\sqrt3}\begin{pmatrix}\sqrt5&0\\ 2&0\end{pmatrix}.
\]
Its canonical generalized inverse \(S_0=2T_0^*-(T_0^*)^2T_0\) cannot be a Moore–Penrose inverse under any positive-definite Hermitian inner product on \(\mathbb C^2\).

## Assumptions and scope
The Hilbert space is \(\mathbb C^2\), with an arbitrary chosen standard inner product and its adjoint \(*\). A nonzero operator \(T\) is a \(2\)-partial isometry when \(T\beta_2(T)=0\), where \(\beta_2(T)=T^{*2}T^2-2T^*T+I\). The generalized inverse \(S\) is formed using this **original** adjoint. We ask whether there is **one** new positive-definite Hermitian matrix \(G\) such that both \(ST\) and \(TS\) are selfadjoint in \(\langle x,y\rangle_G=\langle Gx,y\rangle\), with the same metric for domain and codomain. Two unrelated metrics are not allowed. Rank zero and higher rank are outside the classification; the single counterexample nevertheless answers the unrestricted yes/no question negatively.

## Proof
Write \(T=\alpha uv^*\) for \(\alpha=\|T\|>0\) and unit vectors \(u,v\). Set \(z=\alpha^2\) and \(c=|v^*u|\). Direct calculation gives
\[
T^*T=zvv^*,\qquad T^{*2}T^2=z^2c^2vv^*,\qquad
T\beta_2(T)=0\iff z^2c^2-2z+1=0.
\]
Thus \(c^2=(2z-1)/z^2\), which is feasible precisely when \(z\ge1/2\). In fact, \(1-c^2=(z-1)^2/z^2\ge0\), so every such \(z\) is realized by \(v=e_1\), \(u=(c,s)^{\mathsf T}\), \(s=|z-1|/z\), and \(T=\sqrt z\,uv^*\).

Multiplication of \(T\) by a scalar of modulus one changes \(S\) by its reciprocal phase and leaves \(ST,TS\) unchanged. Hence, without loss for the metric question, a unitary basis and this phase choice give \(v=e_1\) and \(u=(c,s)^{\mathsf T}\) with \(c,s\ge0\). The above quadratic relation yields
\[
P:=ST=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Q:=TS=z\begin{pmatrix}c^2(2-z)&2cs\\ cs(2-z)&2s^2\end{pmatrix}.
\]
Using \(z(2-zc^2)=1\), the same formulas give \(P^2=P\), \(Q^2=Q\), \(TST=T\), and \(STS=S\). Thus only the two metric-adjoint Penrose conditions remain.

A positive Hermitian metric \(G\) makes \(P\) selfadjoint precisely when \(GP=P^*G\). Since \(P\) is the displayed coordinate projection, this forces \(G=\operatorname{diag}(g_1,g_2)\) with \(g_1,g_2>0\). For \(c,s>0\), the identity \(GQ=Q^*G\) is exactly
\[
2g_1=(2-z)g_2.
\]
When \(z<2\), the explicit positive metric \(G=\operatorname{diag}(1,2/(2-z))\) satisfies both identities; this remains valid at \(z=1/2\) (where \(c=0\)) and at \(z=1\) (where \(s=0\)), since then both projections are diagonal. When \(z\ge2\), the relations \(c^2=(2z-1)/z^2\) and \(s^2=(z-1)^2/z^2\) imply \(cs>0\), but the displayed necessary equation contradicts positivity of both diagonal metric entries. The criterion follows.

For clarity, the exact witness has \(z=3\), \(c=\sqrt5/3\) and \(s=2/3\). Calculation gives
\[
\beta_2(T_0)=\operatorname{diag}(0,1),\quad
S_0T_0=\operatorname{diag}(1,0),\quad
T_0S_0=\begin{pmatrix}-5/3&4\sqrt5/3\\-2\sqrt5/3&8/3\end{pmatrix}.
\]
The first two matrices show \(T_0\beta_2(T_0)=0\). Moreover, \(\operatorname{tr}((S_0T_0)(T_0S_0))=-5/3\). Two projections selfadjoint in a common positive-definite inner product must have nonnegative product trace (conjugate both by the square root of the metric and use \(\operatorname{tr}(AB)=\|AB\|_{\mathrm F}^2\) for orthogonal projections). This gives an independent coordinate-free obstruction for the witness.

## Verification
The accompanying standalone program `check.py` uses SymPy exact symbolic arithmetic to reconstruct the rank-one idempotent formulas, test the metric commutators, confirm representative admissible norms, and verify the witness's two projection matrices and negative trace. Run `python check.py` with SymPy installed. The proof above, not the finite tests, establishes the all-norm classification.

## Relationship to prior work
Aouichaoui, Buchała, and Garcia (arXiv:2606.12865v1, §§2 and 6) introduce the relevant generalized inverse, establish the reflexive identities, derive the rank-one \(2\)-partial-isometry equation, and explicitly ask in Question 6 whether a suitable inner product always makes their inverse Moore–Penrose. Those results are premises and motivation, not asserted here as new. The additional contribution is the exact simultaneous-metric criterion and a counterexample establishing a negative answer. The classical four Penrose equations and partial-isometry theory are standard; the source below provides background.

## Limitations
The classification is for nonzero rank-one operators in complex dimension two; it is not a characterization in arbitrary dimension or rank. It assumes one and the same positive-definite Hermitian form for both adjoint conditions. Its originality assessment is literature-based, not a guarantee that no equivalent earlier result exists.

## References
1. M. A. Aouichaoui, M. Buchała, S. R. Garcia, *On \(m\)-partial isometries: spectra, weighted shifts, and similarity*, arXiv:2606.12865v1 (submitted June 11, 2026), https://arxiv.org/abs/2606.12865. §2, Remark 2.6, Lemma 2.8, §6, Question 6.
2. S. L. Campbell and C. D. Meyer, *Generalized Inverses of Linear Transformations*, SIAM, 2012, chapter 4, doi:10.1137/1.9780898719048.ch4 (classical background).
