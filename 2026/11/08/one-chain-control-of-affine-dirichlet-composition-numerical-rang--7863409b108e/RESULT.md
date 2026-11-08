# One-chain control of affine Dirichlet-composition numerical ranges and convexified Davis–Wielandt shells

## Finding
Let \(m\ge2\) be an integer, \(b\in\mathbb C\) with \(a=\operatorname{Re}b>0\), and let \(C_{m,b}f(s)=f(ms+b)\) on the coefficient Hilbert space \(\mathscr H^2\) of ordinary Dirichlet series. Set \(w_k=2^{-a m^k}\), and let \(S\) be the compact unilateral weighted shift \(Se_k=w_ke_{k+1}\) on \(\ell^2(\mathbb N_0)\). Write \(R=w(S)=\lambda_{\max}((S+S^*)/2)\), where \(w(S)\) is its numerical radius.

**Exact numerical range.**
\[
W(C_{m,b})=\operatorname{conv}\bigl(\{1\}\cup\{z\in\mathbb C:|z|\le R\}\bigr).
\]
This is a closed, proper, explicitly specified disk-and-point convex hull; \(0<R\le 2^{-a}<1\).

**Exact support of the closed convexified Davis–Wielandt shell.** Define
\[
\mathcal D(T)=\{(\langle Tf,f\rangle,\|Tf\|^2):\|f\|=1\}\subset\mathbb C\times\mathbb R.
\]
For all \(\theta\in\mathbb R\) and \(\tau\in\mathbb R\),
\[
\begin{split}
&\sup_{(z,t)\in\mathcal D(C_{m,b})}\bigl(\operatorname{Re}(e^{-i\theta}z)+\tau t\bigr)\\
&\quad=\max\{\cos\theta+\tau,\lambda_{\max}(J_{m,a}(\tau))\},
\end{split}
\]
where \(J_{m,a}(\tau)=(S+S^*)/2+\tau S^*S\) is the compact real Jacobi operator with off-diagonal entries \(w_k/2\) and diagonal entries \(\tau w_k^2\). Thus a single chain based at the integer \(2\) determines the *entire closed convex hull* \(\overline{\operatorname{conv}}\mathcal D(C_{m,b})\), even though the composition operator has infinitely many other reducing chains.

The support is effective: let \(J_{m,a}^{[N]}(\tau)\) be the \((N+1)\)-square truncation with edges \(w_0,\ldots,w_{N-1}\) and diagonal \(\tau w_0^2,\ldots,\tau w_{N-1}^2,0\). For every \(N\ge1\),
\[
\bigl|\lambda_{\max}(J_{m,a}(\tau))-\lambda_{\max}(J_{m,a}^{[N]}(\tau))\bigr|
\le 2^{-a m^N}+|\tau|2^{-2a m^N}.
\]
The full shell itself, without taking its closed convex hull, is **not** claimed to have the same form. The imaginary part of \(b\) changes neither of these geometries; more strongly, all operators with the same \(m\) and \(a\) are unitarily equivalent.

## Assumptions and scope
Here \(\mathscr H^2=\{\sum_{n\ge1}c_n n^{-s}:\sum_{n\ge1}|c_n|^2<\infty\}\) and the monomials \(n^{-s}\) form an orthonormal basis. The numerical range of a Hilbert-space operator is \(W(T)=\{\langle Tf,f\rangle:\|f\|=1\}\). The symbol \(ms+b\) is admitted for every integer \(m\ge2\) and every \(\operatorname{Re}b>0\). The top spectral value of each compact self-adjoint Jacobi operator is its largest eigenvalue (positive in these cases); no limit or unknown constant is hidden in the statement. The result concerns \(47A12\) geometry, not a classification of all composition symbols.

## Proof
**(1) Exact orbit decomposition.** For \(e_n(s)=n^{-s}\),
\[
C_{m,b}e_n=n^{-b}e_{n^m}.
\]
The vector \(e_1\) is fixed. Every integer \(n\ge2\) has a unique representation \(n=r^{m^k}\), with \(k\ge0\) and \(r\ge2\) not an integer \(m\)-th power. Consequently, the orthogonal complement of constants splits into reducing chains indexed by these \(r\), and on chain \(r\) the map is a weighted forward shift with successive weight moduli \(r^{-a m^k}\). The nonzero complex phases along each one-way chain can be eliminated by an inductively chosen diagonal unitary. In particular \(C_{m,b}\) is unitarily equivalent to
\[
1\oplus\bigoplus_{r\ \mathrm{not\ an}\ m\mathrm{th\ power},\ r\ge2}S_r,
\quad S_r e_k=r^{-a m^k}e_{k+1}.
\]
The chain \(r=2\) occurs for every \(m\ge2\), and its weights dominate those of all the other chains coordinatewise.

**(2) Numerical-radius domination.** For a positive-weight shift \(S_v\), diagonal gauge symmetry makes \(W(S_v)\) rotation invariant. The Toeplitz–Hausdorff theorem gives convexity. The shift is compact if its weights tend to zero, so the positive maximal eigenvalue of \(\operatorname{Re}S_v\) is attained. Hence \(W(S_v)\) is the closed disk of radius \(\lambda_{\max}(\operatorname{Re}S_v)\). If \(0\le v_k\le w_k\), then \(\lambda_{\max}(\operatorname{Re}S_v)\le\lambda_{\max}(\operatorname{Re}S_w)\), by taking absolute values in the Rayleigh quotient. Taking numerical ranges of the orthogonal direct sum proves the first displayed equality. It is exactly attained by mixing \(e_1\) and vectors from the \(r=2\) chain.

**(3) A nonstandard domination lemma valid for either sign of the quadratic coefficient.** Let \(v=(v_k)\) and \(w=(w_k)\) be bounded nonnegative finite weight lists, with \(v_k\le w_k\), and let \(S_v,S_w\) denote the corresponding finite nilpotent shifts. For every real \(\tau\),
\[
\lambda_{\max}(\operatorname{Re}S_v+\tau S_v^*S_v)
\le\lambda_{\max}(\operatorname{Re}S_w+\tau S_w^*S_w).
\]
For \(\tau\ge0\) this is direct Perron–Frobenius/Rayleigh comparison of the entrywise nonnegative symmetric matrices. For \(\tau=-u<0\), completion of the square yields for *every* shift \(A\)
\[
\operatorname{Re}\langle Ax,x\rangle-u\|Ax\|^2
\le\frac1{4u}\|x\|^2.
\]
It remains to compare levels \(0<\lambda<1/(4u)\). The matrix \(Q_w=\lambda I-(\operatorname{Re}S_w-uS_w^*S_w)\) is positive definite exactly when all the backward scalar Schur pivots are positive:
\[
 d_N=\lambda,\qquad
 d_k=\lambda+w_k^2\left(u-\frac1{4d_{k+1}}\right),\quad k=N-1,\ldots,0.
\]
If they are positive then automatically \(0<d_k\le\lambda<1/(4u)\), by backward induction. For the shorter weight list \(v\), its pivots \(\widetilde d_k\) satisfy \(d_k\le\widetilde d_k\le\lambda\): the recurrence is increasing in the incoming pivot and decreasing in the squared edge weight throughout this interval. Therefore \(Q_w>0\) implies \(Q_v>0\). Taking \(\lambda\) immediately above the upper eigenvalue of the larger shift, or using the universal ceiling if that eigenvalue reaches \(1/(4u)\), establishes the inequality. This argument deliberately does *not* compare the Jacobi matrices in Loewner order (which would be false).

Pass to infinite compact shifts by truncating at edge \(N\), whose norm error is the largest omitted weight. Their quadratic terms converge in norm, so the same top-eigenvalue monotonicity holds for all the chains \(S_r\) and the dominant \(S=S_2\).

**(4) Support of the shell.** A real supporting functional of \(\mathcal D(T)\) is the top Rayleigh value of \(\operatorname{Re}(e^{-i\theta}T)+\tau T^*T\). Along a chain, a diagonal unitary removes \(\theta\) and any phases, and Step (3) says that no \(r>2\) chain can exceed the \(r=2\) top spectral value, for positive **or negative** \(\tau\). The fixed constant vector contributes \(\cos\theta+\tau\). The top value of a direct sum is the supremum of its block top values. Hence the second formula, including all supporting directions. The standard support-function characterization of closed convex sets establishes precisely the claimed closed convex hull and no stronger nonconvex-shell assertion.

**(5) Effective error.** Let \(S^{[N]}\) retain only edges before \(N\). Since the weights decrease, \(\|S-S^{[N]}\|=w_N\), while \(\|S^*S-(S^{[N]})^*S^{[N]}\|=w_N^2\). The top of a self-adjoint operator changes by no more than its operator-norm perturbation, giving the displayed super-exponential truncation estimate.

## Verification
Run \(`python3 check.py`\) with Python 3. The script uses exact rational arithmetic to verify Schur-pivot determinant identities, monotone positivity for numerous finite edge lists with both positive and negative quadratic contributions, unique integer power-chain factorizations on a finite domain, and the first-omitted-weight identities. Its successful output is `DIRICHLET_DW_JACOBI_CHECK_OK 22575 exact rational assertions`. These finite checks are diagnostic; the proof above supplies the statements for all integers, all real parameters and infinite-dimensional spaces.

## Relationship to prior work
Lahiri, Ojha, Halder and Birbonshi (2026, arXiv:2608.29294, Section 5, Proposition 5.2 and Question 5.4) give the isometric case \(\operatorname{Re}b=0\) and a general quadratic bound for positive translations, then ask for the shape of affine-symbol Davis–Wielandt shells. This finding gives an exact numerical range and an exact support description of the *closed convexified* shell when \(m\ge2\) and \(\operatorname{Re}b>0\); it does not answer the stronger question of the exact nonconvex shell. Finet and Queffélec (2004) investigate Dirichlet-series composition numerical ranges, including normal and isometric classes, but its full text was not available for direct comparison. The supporting Jacobi comparison works beyond composition operators and is the critical added structural step; mere decomposition into weighted shifts would not prove the negative-\(\tau\) support formula.

## Limitations
The result requires integer \(m\ge2\) and strictly positive real translation part. The case \(\operatorname{Re}b=0\) belongs to the established isometric theory; \(m=0,1\) have different orbit structures. The closed convex hull of the three-dimensional Davis–Wielandt shell is characterized, but the possibly nonconvex shell itself and its full boundary-point attainment are not. The parameter-dependent Jacobi top eigenvalue is specified exactly and approximable with a certified error, not given by an elementary formula. Earlier unpublished or differently formulated Davis–Wielandt dominance theorems could subsume the comparison lemma and require additional literature verification.

## References
1. S. Lahiri, S. Ojha, S. Halder and R. Birbonshi, *Numerical range and invariant subspaces of weighted composition operators on the Hardy space of Dirichlet series*, arXiv:2608.29294v1 (first public August 29, 2026), especially Section 5, Proposition 5.2 and Question 5.4. https://arxiv.org/abs/2608.29294
2. C. Finet and H. Queffélec, *Numerical range of composition operators on a Hilbert space of Dirichlet series*, Linear Algebra and its Applications 377 (2004), 1–10, DOI:10.1016/j.laa.2003.05.003 (abstract consulted; full text not inspected).
3. B. Lins, I. M. Spitkovsky and S. Zhong, *The normalized numerical range and the Davis–Wielandt shell*, arXiv:1712.01070 (2017), abstract/description consulted for related matrix geometric context. https://arxiv.org/abs/1712.01070
4. C. K. Li and Y. T. Poon, *Davis–Wielandt shells of normal operators*, Glasgow Math. J. 51 (2009), related normal-operator shell theory (abstract consulted).
