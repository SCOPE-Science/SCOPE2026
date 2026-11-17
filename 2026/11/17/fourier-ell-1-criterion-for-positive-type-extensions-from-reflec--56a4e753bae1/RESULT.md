# Fourier-\(\ell^1\) criterion for positive-type extensions from reflection cosets

## Finding
Let \(H\) be a finite abelian group with \(N=|H|\ge1\), and let \(G=H\rtimes_{-1}C_2\) be its generalized dihedral group. Write \(s\) for the involution which acts by inversion, and set \(\Delta=\{e\}\cup Hs\). Define a scalar function \(\varphi:\Delta\to\mathbb C\) with \(\varphi(e)=1\), and write \(u(h)=\varphi(hs)\).

The function \(\varphi\) is partially positive-definite, in the sense of testing every matrix \((\varphi(xy^{-1}))_{x,y\in\Sigma}\) with \(\Sigma\Sigma^{-1}\subseteq\Delta\), **if and only if** all \(u(h)\) are real and lie in \([-1,1]\). It admits a normalized positive-definite extension to all of \(G\) **if and only if**
\[
 \boxed{\quad\sum_{\chi\in\widehat H}|\widehat u(\chi)|\le1,\qquad
 \widehat u(\chi)=\frac1N\sum_{h\in H}u(h)\overline{\chi(h)}.\quad}
\]
Here \(\widehat H\) denotes the character group. Every feasible extension can be constructed from a finite convex combination of explicit one- and two-dimensional unitary coefficient states.

The local and global cones agree for every datum precisely when \(N\le2\). For every \(N\ge3\), the all-ones reflection datum with the value at exactly one reflection replaced by \(-1\) is locally positive but not extendible; its Fourier \(\ell^1\) norm is exactly \(3-4/N>1\). Thus the first obstruction occurs for \(G\cong S_3\). In that case the extendible triples form a symmetric circular bicone occupying the exact fraction \(\pi\sqrt3/8\) of the local cube.

## Assumptions and scope
The group \(H\) is arbitrary but finite and abelian. Multiplication in \(G\) is specified by \(s^2=e\) and \(shs=h^{-1}\). Every element \(hs\) is an involution, and \(Hs\) is a coset, not a subgroup unless \(H\) is trivial. The positivity condition on \(\Delta\) quantifies over every finite \(\Sigma\subseteq G\) satisfying \(\Sigma\Sigma^{-1}\subseteq\Delta\). A full extension \(\Phi:G\to\mathbb C\) is positive-definite when \((\Phi(xy^{-1}))_{x,y\in G}\) is positive semidefinite. The asserted criterion includes endpoints and Fourier norm equality. No continuity assumption is needed on a finite group.

## Proof

### 1. Local positivity imposes only interval bounds
All differences between distinct elements of an admissible \(\Sigma\) must belong to the odd coset \(Hs\), since the identity is the only even element in \(\Delta\). Parities alternate along any such difference. Thus three distinct elements cannot have all their pairwise differences in \(Hs\): a two-colouring of a three-element set cannot have every pair of opposite colours. Hence \(|\Sigma|\le2\). Every \(hs\) is self-inverse, so a two-point test has the form
\[
 \begin{pmatrix}1&u(h)\\u(h)&1\end{pmatrix}\succeq0.
\]
Hermiticity makes \(u(h)\) real, and positivity is equivalent to \(|u(h)|\le1\). Conversely those tests exhaust all admissible \(\Sigma\), proving the assertion.

### 2. Necessity of the Fourier bound
Let \(\Phi\) be a normalized positive-definite extension. By the finite-group GNS construction there are a unitary representation \(\pi:G\to\mathcal U(\mathcal H)\) and a unit vector \(\xi\) with \(\Phi(g)=\langle\pi(g)\xi,\xi\rangle\). Set \(\eta=\pi(s)\xi\), also a unit vector. Restricting \(\pi\) to the finite abelian subgroup \(H\) gives the orthogonal spectral decomposition \(\pi(h)=\sum_{\chi\in\widehat H}\chi(h)P_\chi\), where some projections may vanish. Therefore
\[
 u(h)=\langle\pi(h)\eta,\xi\rangle
 =\sum_{\chi\in\widehat H}\chi(h)\langle P_\chi\eta,\xi\rangle.
\]
Character orthogonality identifies \(\widehat u(\chi)=\langle P_\chi\eta,\xi\rangle\) (with the usual convention conjugating the coefficient if the Hilbert product is linear in its second slot). Cauchy--Schwarz yields
\[
 \sum_\chi|\widehat u(\chi)|
 \le\sum_\chi\|P_\chi\eta\|\,\|P_\chi\xi\|
 \le \|\eta\|\,\|\xi\|=1.
\]
This is an exact necessary obstruction, not a finite sampling heuristic.

### 3. Construction at every permitted Fourier datum
Assume \(u:H\to\mathbb R\) and \(L:=\sum_\chi|\widehat u(\chi)|\le1\). Fourier inversion holds on \(H\), and real-valuedness gives \(\widehat u(\chi^{-1})=\overline{\widehat u(\chi)}\). Separate the characters into inversion-fixed characters and two-element inverse pairs.

For an inversion-fixed character \(\chi=\chi^{-1}\), the coefficient \(c=\widehat u(\chi)\) is real. Use the one-dimensional unitary character \(\pi_{\chi,\varepsilon}\) of \(G\) defined by \(\pi_{\chi,\varepsilon}(h)=\chi(h)\) and \(\pi_{\chi,\varepsilon}(s)=\varepsilon\in\{\pm1\}\), with \(\varepsilon=\operatorname{sgn}c\). Give this state weight \(|c|\); its reflection contribution is \(c\chi(h)\).

For one representative \(\chi\) from a pair \(\{\chi,\chi^{-1}\}\), set \(c=\widehat u(\chi)\). The two-dimensional unitary representation
\[
 \pi_\chi(h)=\begin{pmatrix}\chi(h)&0\\0&\overline{\chi(h)}\end{pmatrix},\qquad
 \pi_\chi(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
satisfies the generalized-dihedral relations. For \(c\ne0\), take the positive trace-one density matrix
\[
 \rho_\chi=\tfrac12\begin{pmatrix}1&\overline c/|c|\\c/|c|&1\end{pmatrix}.
\]
Then \(\operatorname{tr}(\rho_\chi\pi_\chi(hs))=\operatorname{Re}((c/|c|)\chi(h))\), so the weighted state with weight \(2|c|\) contributes exactly
\[
 c\chi(h)+\overline c\,\overline{\chi(h)}.
\]
The sum of the positive weights assigned to all fixed characters and inverse pairs is exactly \(L\). Fill the unused state weight \(1-L\) with the equally weighted mixture of the two characters that are trivial on \(H\) and take \(s\) to \(1\) or \(-1\), respectively; its reflection contribution is zero. The resulting functional is a normalized convex combination of positive states on \(C^*(G)\), hence its coefficient function \(\Phi\) is positive-definite on all of \(G\). Fourier inversion shows \(\Phi(hs)=u(h)\) for every \(h\in H\). The same construction covers \(c=0\) by simply omitting that block and covers \(L=1\) without a residual state.

### 4. Exact small-group threshold and obstruction
For \(N=1\), the Fourier norm equals the magnitude of the sole value. For \(N=2\), the exact identity \(\tfrac12(|a+b|+|a-b|)=\max(|a|,|b|)\) proves that every locally positive real datum is extendible. Let \(N\ge3\) and fix \(h_0\in H\). For \(u=1-2\mathbf1_{\{h_0\}}\), the trivial Fourier coefficient is \(1-2/N\), while each of the other \(N-1\) coefficients has magnitude \(2/N\). Thus
\[
 \sum_\chi|\widehat u(\chi)|=1-\frac2N+(N-1)\frac2N=3-\frac4N>1.
\]
Every value of \(u\) is \(\pm1\), so local positivity holds even though extension fails.

### 5. The smallest case and its exact geometric fraction
When \(H=C_3\), the odd coset consists of all three transpositions of \(S_3\). Write its real values as \(a,b,c\) and \(m=(a+b+c)/3\). Fourier inversion and character orthogonality yield
\[
 \sum_{\chi\in\widehat H}|\widehat u(\chi)|
 =|m|+\sqrt{\frac23}\sqrt{(a-m)^2+(b-m)^2+(c-m)^2}.
\]
The extendible region in the local cube \([-1,1]^3\) is therefore
\[
 |m|+\sqrt{\frac23}\|(a-m,b-m,c-m)\|_2\le1.
\]
It is a double cone with apices \(\pm(1,1,1)\), base disk in the plane \(a+b+c=0\) of Euclidean radius \(\sqrt{3/2}\), and total three-dimensional volume \(\pi\sqrt3\). The uniform-volume fraction among all locally admissible triples is exactly \(\pi\sqrt3/8\).

## Verification
The finite diagnostic script `check_extension.py` reconstructs full-group positive semidefinite Gram matrices for cyclic groups of orders \(1,2,3,4,5,6,7,8,12\), samples feasible Fourier data, and checks the sharp one-negative obstruction and small-order endpoints. Execute `python check_extension.py` in a Python 3 environment with NumPy. It prints `PASS 2638 finite diagnostics`. All universally quantified assertions above follow from the independent analytic argument; the numerical tests are not treated as exhaustive evidence for arbitrary finite abelian groups.

## Relationship to prior work
Kakariadis, Leimbach, Todorov and van Suijlekom (2026), especially their definitions of positivity domains and positive-type extensions and their five-point \(\mathbb Z^2\) example, provide the immediate framework. The present theorem gives an exact **scalar** restriction cone for a different natural family, all finite generalized dihedral groups, including an explicit Fourier norm, constructive extension and a sharp universal local/global boundary at group order six. The general positive-extension criteria of Levene, Lin and Todorov (2015/2016) and the chordal Cayley-graph sufficient criterion of Bakonyi and Timotin (2008/2011) do not state the numerical Fourier-\(\ell^1\) criterion. The latter chordality hypothesis does not apply here when \(|H|\ge2\), because the Cayley graph is \(K_{N,N}\). Standard finite-group Fourier theory supplies the proof machinery and is not claimed as new.

## Limitations
Only scalar-valued positive-definite extensions are classified; operator-valued extensions, nonabelian base groups, and arbitrary positivity domains are not addressed. The exact criterion may admit an equivalent formulation in the established Fourier--Stieltjes literature. While no directly covering statement was identified in the inspected sources, this does not establish absolute publication priority. The special \(S_3\) bicone is a consequence, not a claim of an independent general convexity principle.

## References
1. E. T. A. Kakariadis, M. Leimbach, I. G. Todorov, W. D. van Suijlekom, *Operator systems and positive extensions over discrete groups*, arXiv:2603.29958v1 (31 March 2026), especially Sections 3 and 5. https://arxiv.org/abs/2603.29958
2. R. H. Levene, Y.-F. Lin, I. G. Todorov, *Positive extensions of Schur multipliers*, arXiv:1511.07049 (2015; subsequent published version), especially Section 5. https://arxiv.org/abs/1511.07049
3. M. Bakonyi, D. Timotin, *Extensions of positive definite functions on amenable groups*, arXiv:0808.1273 (2008); Canadian Mathematical Bulletin 54 (2011), 3--11, especially Theorem 2.1. https://arxiv.org/abs/0808.1273
