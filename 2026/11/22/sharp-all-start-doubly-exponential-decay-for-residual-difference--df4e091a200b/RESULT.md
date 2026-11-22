# Sharp all-start doubly-exponential decay for residual-difference gradient iteration on two spectral levels

## Finding
Consider a consistent linear system and the residual-difference (RD, or short Barzilai–Borwein) gradient method initialized with one exact residual steepest-descent step, as defined below. Suppose that the positive residual Gram operator has exactly two distinct active eigenvalues \(a>b>0\), and both spectral projections of the starting residual are nonzero. Then the residual converges **doubly exponentially from every mixed start**, with the exact exponent
\[
\boxed{\displaystyle \lim_{n\to\infty}\frac{1}{n}\log\log\frac{\|r_0\|_2}{\|r_n\|_2}=\log\sqrt2.}
\]
There is no balanced, merely geometric-convergence exception. More precisely, write \(\kappa=a/b\), \(t=\log(\|P_a r_0\|_2^2/\|P_b r_0\|_2^2)\), \(L=\log\kappa\), \(q=\sqrt2\), and \(\theta=\arccos(1/(2\sqrt2))\). The exactly determined oscillation amplitude satisfies
\[
\boxed{\displaystyle C^2=4L^2+\frac{16}{7}(t+L/2)^2\ge4L^2>0.}
\]
The bound is sharp: equality holds exactly for initial spectral-energy ratio \(e^{-L/2}=\kappa^{-1/2}\). The complete scaled logarithmic residual obeys
\[
\boxed{\displaystyle
-q^{-n}\log\frac{\|r_n\|_2}{\|r_0\|_2}
=C H(n\theta-\delta)+O_{a,b,r_0}(nq^{-n}),}
\]
where \(\delta\) and the positive, continuous, \(2\pi\)-periodic function \(H\) are explicit in the proof. If the starting residual belongs to only one active eigenspace, the initial step instead solves it exactly.

## Assumptions and scope
Let \(A\in\mathbb R^{m\times d}\) have full column rank, \(m\ge d\), and let \(Ax_*=c\) be consistent. Write \(r_k=c-Ax_k\) and \(B=AA^\top\). Assume \(B\) has exactly two distinct **positive** eigenvalues \(a>b>0\) on the range of \(A\), of arbitrary multiplicities. As consistency implies \(r_0\in\operatorname{ran}(A)\), its zero-eigenspace component is absent. Let \(P_a,P_b\) be the orthogonal projections onto the corresponding eigenspaces. All arithmetic is exact.

Define
\[
 x_{k+1}=x_k+\alpha_k A^\top r_k,\qquad
 \alpha_0=\frac{\|r_0\|_2^2}{r_0^\top B r_0},\qquad
 \alpha_k=\frac{\|r_k-r_{k-1}\|_2^2}{(r_k-r_{k-1})^\top B(r_k-r_{k-1})},\quad k\ge1.
\]
The rule at positive indices is precisely the residual-difference step (the short BB analogue) in Xu [1]; the specified first step is ordinary residual steepest descent. The conclusion is an \(R\)-type double-exponential statement about residual norms, not a one-step \(Q\)-superlinear bound or a finite-precision performance guarantee.

## Proof
**1. Exact two-level RD recurrence.** With spectral energies \(u_k=\|P_a r_k\|_2^2\), \(v_k=\|P_b r_k\|_2^2\) and \(e_k=u_k/v_k\), the first steepest-descent step gives \(e_1=1/e_0\) whenever both energies are positive. For \(k\ge1\), the exact identity \(r_k-r_{k-1}=-\alpha_{k-1}Br_{k-1}\) yields
\[
 \alpha_k=\frac{a^2e_{k-1}+b^2}{a^3e_{k-1}+b^3},\qquad
 1-a\alpha_k=\frac{b^2(b-a)}{a^3e_{k-1}+b^3},\qquad
 1-b\alpha_k=\frac{a^2(a-b)e_{k-1}}{a^3e_{k-1}+b^3}.
\]
Both multipliers are nonzero. Consequently, every mixed residual stays mixed and
\[
 e_{k+1}=\frac{e_k}{\kappa^4e_{k-1}^2}.
\]
Put \(z_k=\kappa^2e_k\) and \(\phi_k=\log z_k\). Then \(z_{k+1}=z_k/z_{k-1}^2\) and \(\phi_{k+1}=\phi_k-2\phi_{k-1}\), with
\[
 \phi_0=2L+t,\qquad \phi_1=2L-t.
\]

**2. Exact nonzero-amplitude gap.** The characteristic roots of the logarithmic recurrence are \(q e^{\pm i\theta}\). Thus
\[
 \phi_j=Cq^j\cos(j\theta-\delta),\quad
 C\cos\delta=2L+t,\quad
 C\sin\delta=\frac{2L-3t}{\sqrt7}.
\]
Squaring gives \(C^2=(2L+t)^2+(2L-3t)^2/7=4L^2+16(t+L/2)^2/7\). Because \(L>0\), the oscillation cannot vanish for **any** starting spectral ratio. The unique minimum over all mixed starts is \(C=2L\), attained at \(t=-L/2\). In contrast, standard matched delayed long (BB1/DR) steps can have zero oscillation amplitude at a balanced start [2,3].

**3. Complete norm asymptotics.** In terms of \(z_{k-1}=e^{\phi_{k-1}}\), the two RD multipliers from step \(k\ge1\) become
\[
 1-a\alpha_k=-\frac{\kappa-1}{1+\kappa e^{\phi_{k-1}}},\qquad
 1-b\alpha_k=\frac{(\kappa-1)e^{\phi_{k-1}}}{1+\kappa e^{\phi_{k-1}}}.
\]
Uniformly over real \(s\), \(\log(1+\kappa e^s)=[s]_++O_\kappa(1)\) and \(\log(1+\kappa e^s)-s=[-s]_++O_\kappa(1)\), where \([s]_+=\max(s,0)\). Taking logs of all multipliers from \(k=1\) to \(n-1\) therefore gives
\[
 -\log\|P_a r_n\|_2=\sum_{j=0}^{n-2}[\phi_j]_++O_{a,b,r_0}(n),\qquad
 -\log\|P_b r_n\|_2=\sum_{j=0}^{n-2}[-\phi_j]_++O_{a,b,r_0}(n).
\]
Define the absolutely and uniformly convergent series
\[
 U(\varphi)=\sum_{m=2}^\infty q^{-m}[\cos(\varphi-m\theta)]_+,\qquad
 H(\varphi)=\min\{U(\varphi),U(\varphi+\pi)\},
\]
and choose \(\delta\in\mathbb R/(2\pi\mathbb Z)\) as in Step 2. Changing summation index \(m=n-j\), and using the geometric tail bound, yields
\[
 -q^{-n}\log\|P_a r_n\|_2=C U(n\theta-\delta)+O(nq^{-n}),\qquad
 -q^{-n}\log\|P_b r_n\|_2=C U(n\theta-\delta+\pi)+O(nq^{-n}).
\]
The log Euclidean norm differs from the larger component log by at most \(\log\sqrt2\), so the minimum of these two positive log expressions gives the claimed uniform-in-iteration profile; subtracting the fixed \(\log\|r_0\|_2\) alters only its remainder.

**4. Uniformly positive phase envelope and sharp exponent.** The angle satisfies \(2\cos\theta=1/\sqrt2\). Were \(\theta/\pi\) rational, \(2\cos\theta\) would be an algebraic integer; it is not, since its norm in \(\mathbb Q(\sqrt2)\) is \(-1/2\). Thus the rotation by \(\theta\) is dense modulo \(2\pi\). Every phase therefore has infinitely many indices \(m\) with positive and with negative cosine, implying both \(U(\varphi)\) and \(U(\varphi+\pi)\) strictly positive. Uniform convergence makes \(H\) continuous; compactness supplies \(0<\min H\le\max H<\infty\). Since \(C\ge2L>0\), the scaled negative log residual is bounded above and below by positive constants for all sufficiently large \(n\). Hence \(\|r_n\|_2/\|r_0\|_2=\exp[-\Theta(q^n)]\), and taking double logarithms proves the limit \(\log q\). If one initial spectral projection vanishes, \(\alpha_0\) equals the inverse of the remaining eigenvalue and \(r_1=0\), as claimed.

## Verification
Run `python3 verify_rd.py` with Python 3's standard library. The reproducibility script independently builds 20 two-mode exact-rational trajectories, checks the RD difference quotient against its spectral formula and both logarithmic ratio identities, verifies the first-step inversion, and compares 25 late-iteration normalized log residuals against a separately evaluated truncated series. Output: `VERIFY_OK 417 finite exact-rational and independent scaled-log checks`. The truncation and numerical comparisons are diagnostics, not a substitute for Step 4's infinite-iteration proof.

## Relationship to prior work
Xu [1] introduces DR and RD, identifies them as BB1 and BB2 analogues, and analyzes **DR**, not RD, on a two-singular-value model. Prior two-dimensional BB analyses [4,5] obtain (at least) \(R\)-superlinear behavior for generic starts; the recent universal rate paper [6] gives sharp \(R\)-linear *upper envelopes* for both fixed BB rules. Two published mathematical findings establish an exact scaled-log profile for **matched BB1** [2] and eliminate its balanced orbit by **alternating** long/short steps [3]. The present statement does not claim new BB formulas, the logarithmic characteristic roots, generic two-dimensional BB superlinearity, nor the universal series construction in [2]. The distinct statement is the **pure RD/short-step rule with one residual SD initialization**: that rule's transformed two-log-state initialization cannot lie on the balanced orbit, and it has a *sharp, positive initial-ratio-uniform amplitude gap* \(C\ge2\log\kappa\), without alternating step types. The relation to weighted delayed-Rayleigh conjugacy [7] makes earlier implicit coverage a residual originality risk; the first-step constraint and amplitude minimization must be checked in any future priority audit.

## Limitations
Only exactly two active positive singular-value squares, a consistent system, exact arithmetic, and the specified first step are treated. Convergence speed is nonuniform as \(a/b\downarrow1\), although the equal-eigenvalue system is solved in one initial step. The theorem does not address rounding, difference cancellation, arbitrary spectra, or wall-clock efficiency. Earlier unindexed short-step analyses and implicit corollaries of the general BB conjugacy remain priority risks; no independent audit has been performed.

## References
[1] Xin Xu, *Two-point residual step size gradient methods for linear systems*, arXiv:2611.02743v1, first public 2026-11-02, https://arxiv.org/abs/2611.02743.

[2] *A universal log-periodic gradient envelope for two-mode Barzilai–Borwein descent*, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-universal-log-periodic-gradient-envelope-for-two-mode-barzilai--80f835ec743a.

[3] *Alternating long–short spectral steps eliminate the balanced two-mode slowdown*, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-alternating-long-short-spectral-steps-eliminate-the-balanced-two--0e04302e58f6.

[4] J. Barzilai and J. M. Borwein, *Two-Point Step Size Gradient Methods*, IMA Journal of Numerical Analysis 8 (1988), 141–148, https://doi.org/10.1093/imanum/8.1.141.

[5] M. Raydan, *Convergence Rate for the 2 Eigenvalues Case*, thesis Chapter 5, https://camo.ici.ro/books/thesis/raydan.pdf.

[6] S. Yang and Y. Yuan, *The Sharp Worst-Case Asymptotic Rate of the Barzilai–Borwein Method in \(\mathbb R^d\) and Hilbert Spaces*, arXiv:2608.07839, https://arxiv.org/abs/2608.07839.

[7] S. Yang and Y. Yuan, *R-Linear Convergence of Barzilai–Borwein Methods on Strictly Convex Quadratics via Closed-Cone Homogeneous Dynamics*, arXiv:2609.12100, https://arxiv.org/abs/2609.12100.
