# An exact complex three-by-three penultimate Schatten Gelfand number in the quasi-Banach range

## Finding
For every \(0<p\le 1\) and \(p<q\le\infty\), the eighth Gelfand number of the complex-linear identity \(\mathrm{id}:\mathcal S_p^3(\mathbb C)\to\mathcal S_q^3(\mathbb C)\) is
\[
c_8(\mathrm{id})=2^{1/q-1/p}.
\]
Here \(1/\infty=0\). The infimum is attained by the two-dimensional *complex* subspace
\[
E=\operatorname{span}_{\mathbb C}\left\{I_3,\operatorname{diag}(1,\zeta,\zeta^2)\right\},\qquad \zeta=e^{2\pi i/3}.
\]
At the terminal index, \(c_9(\mathrm{id})=3^{1/q-1/p}\), a strict reduction from \(c_8\) for every \(p<q\).

## Assumptions and scope
The matrix field and the subspaces in the Gelfand-number definition are **complex**. The Schatten \(s\)-quasi-norm of a matrix is \(\|A\|_s=(\sum_{j=1}^3\sigma_j(A)^s)^{1/s}\) for \(s>0\), and \(\|A\|_\infty=\max_j\sigma_j(A)\). For a linear map between nine-dimensional complex spaces,
\[
c_k(\mathrm{id})=\inf_{\substack{F\subset\mathbb C^{3\times3}\ \operatorname{codim}_{\mathbb C}F<k}}\ \sup_{0\ne A\in F}\frac{\|A\|_q}{\|A\|_p}.
\]
For \(k=8\), it suffices to consider complex two-dimensional subspaces: any higher-dimensional competitor contains one. The estimates also apply when the source has a quasi-norm (\(p<1\)).

## Proof
**Universal lower bound.** Let \(F\) be any complex matrix two-plane, with independent basis \(A,B\). The homogeneous cubic \(D(s,t)=\det(sA+tB)\) either vanishes identically, or has a zero on the complex projective line (including \([1:0]\) or \([0:1]\)). Thus \(F\) contains a nonzero \(C\) with \(\operatorname{rank}C\le2\). The matrix is nonzero because \(A,B\) are independent. Since \(p<q\), the power-mean comparison on at most two nonzero singular values yields
\[
\frac{\|C\|_q}{\|C\|_p}\ge(\operatorname{rank}C)^{1/q-1/p}\ge2^{1/q-1/p}.
\]
Here the exponent is negative. Therefore \(c_8\ge2^{1/q-1/p}\).

**Sharp complex plane.** Write \(U=\operatorname{diag}(1,\zeta,\zeta^2)\). Each element of \(E\) is \(aI_3+bU\) with complex coefficients \(a,b\). Its three singular values are \(s_j=|a+b\zeta^j|\), with indices modulo three. The exact linear identities
\[
a+b\zeta^j=-\zeta(a+b\zeta^{j+1})-\zeta^2(a+b\zeta^{j+2})
\]
show that \(s_j\le s_{j+1}+s_{j+2}\). Since \(0<p\le1\), subadditivity of the function \(t\mapsto t^p\) gives \(s_j^p\le s_{j+1}^p+s_{j+2}^p\). For a nonzero matrix, normalize by \(w_j=s_j^p/(s_0^p+s_1^p+s_2^p)\); then \(w_j\in[0,1/2]\) and \(\sum_jw_j=1\). When \(q<\infty\), the convex function \(t\mapsto t^{q/p}\), with \(q/p>1\), has its maximum over this capped simplex at a permutation of \((1/2,1/2,0)\). Hence
\[
\sum_{j=0}^2 w_j^{q/p}\le2^{1-q/p},\qquad \frac{\|aI_3+bU\|_q}{\|aI_3+bU\|_p}\le2^{1/q-1/p}.
\]
For \(q=\infty\), the cap \(w_j\le1/2\) directly gives \(\|aI_3+bU\|_\infty/\|aI_3+bU\|_p\le2^{-1/p}\). The particular matrix \(I_3-U\) has singular values \((0,\sqrt3,\sqrt3)\), attaining equality for every exponent pair. Combining bounds proves the theorem.

**Terminal index.** Any complex line has a norm ratio at least \(3^{1/q-1/p}\) by the three-singular-value power-mean comparison. The line \(\mathbb C I_3\) attains it. Thus \(c_9=3^{1/q-1/p}\).

## Verification
Each step above is finite-dimensional and exact; there is no asymptotic or enumeration argument. In particular, determinant-root existence requires algebraic closure and cannot be replaced by a real sign-change argument. The supplementary `checker.py` tests sampled complex coefficients, 12 exponent pairs, both endpoint and intermediate exponents, and the extremal rank-two witness. Its successful finite test output is `COMPLEX_SCHATTEN_PENCIL_DIAGNOSTICS_OK 8076`. These samples are not the proof of the universal norm inequality.

## Relationship to prior work
Prochno, *Gelfand numbers of Schatten class embeddings in the quasi-Banach range* (2026), investigates Schatten Gelfand numbers with **real** matrix entries, supplies general asymptotic estimates, and gives the terminal-index exact value. The present theorem supplies a sharp *penultimate* complex-field value for the smallest nontrivial cubic determinant situation. Hinrichs–Prochno–Vybíral (2020) and Prochno–Strzelecki (2021) address real-matrix Schatten width estimates; their investigated conclusions do not directly state this complex field-specific two-plane invariant. The real penultimate matrix-width formula in earlier work has the same numerical value in size three but uses a real two-plane and does not imply a bound for all complex coefficients in the present subspace. Li–Nakatsukasa–Soma–Uschmajew (2017) study related orthogonal tensors and rank-one approximation geometry; their field-dependent existence results are not the asserted sharp quasi-Schatten width.

## Limitations
This result concerns \(3\times3\) complex matrices and exponents \(0<p\le1\), \(p<q\le\infty\). The subadditivity step fails for \(p>1\); no formula in that range is asserted. The proof does not establish higher-dimensional complex Gelfand numbers or uniqueness of the extremizing plane. An unlocated older complex-width theorem could contain an equivalent statement; no priority or independent mathematical certification is claimed.

## References
1. J. Prochno, *Gelfand numbers of Schatten class embeddings in the quasi-Banach range*, arXiv:2611.08448, first public version 2026-11-05; full revised preprint also inspected.
2. A. Hinrichs, J. Prochno, and J. Vybíral, *Gelfand numbers of embeddings of Schatten classes*, arXiv:2011.06554 (2020).
3. J. Prochno and M. Strzelecki, *Gelfand numbers of Schatten class embeddings*, arXiv:2103.13050 (2021).
4. C. Li, Y. Nakatsukasa, N. Soma, and A. Uschmajew, *On orthogonal tensors and best rank-one approximation ratio*, arXiv:1707.02569 (2017).
