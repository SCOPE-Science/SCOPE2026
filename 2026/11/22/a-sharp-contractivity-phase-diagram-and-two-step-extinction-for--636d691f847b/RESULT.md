# A sharp contractivity phase diagram and two-step extinction for nilpotent-noise stochastic theta integration

## Finding
Consider the two-dimensional Itô equation
\[
\mathrm dX_t=(-I_2+\gamma N)X_t\,\mathrm dt+\sigma N X_t\,\mathrm dW_t,
\qquad N=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\]
where \(\gamma,\sigma\ge0\) and \(W\) is a standard real Wiener process. Let \(\theta\in[0,1]\), \(h>0\), and apply the drift-implicit theta-Maruyama update
\[
X_{k+1}=X_k+h\big[(1-\theta)AX_k+\theta AX_{k+1}\big]
+\sigma NX_k\Delta W_k,\quad A=-I_2+\gamma N,
\quad \Delta W_k\sim\mathcal N(0,h)
\]
with independent increments. Set
\[
c(h,\theta)=2+(2\theta-1)h,\qquad
c_*(\gamma,\sigma)=\frac{\sigma^2+\sqrt{\sigma^4+4\gamma^2}}2.
\]
**Exact phase diagram.** One-step mean-square Euclidean nonexpansivity, namely
\(\mathbb E[\|X_{k+1}\|_2^2\mid X_k=x]\le\|x\|_2^2\) for every deterministic \(x\in\mathbb R^2\), is equivalent to
\[
\boxed{c(h,\theta)\ge c_*(\gamma,\sigma).}
\]
Consequently its complete positive-step sets are:

- For \(0\le\theta<1/2\): \(0<h\le(2-c_*)/(1-2\theta)\) when \(c_*<2\), and the empty set when \(c_*\ge2\).
- For \(\theta=1/2\): every \(h>0\) when \(c_*\le2\), and no positive step otherwise.
- For \(1/2<\theta\le1\): every \(h>0\) when \(c_*\le2\), and exactly \(h\ge(c_*-2)/(2\theta-1)\) when \(c_*>2\).

The exact continuous Itô flow is mean-square Euclidean nonexpansive for all times and every initial state precisely when \(\gamma^2+2\sigma^2\le4\), which is equivalent to \(c_*\le2\). Thus, if \(\gamma^2+2\sigma^2>4\), the continuous flow initially expands some deterministic state, but every \(\theta>1/2\) produces a whole half-line of contractive **large** numerical steps, while \(\theta\le1/2\) produces no positive contractive step.

In contrast, the numerical method is asymptotically mean-square stable for **every** deterministic initial state, independently of \(\gamma\) and \(\sigma\), exactly for
\[
\begin{cases}
0<h<2/(1-2\theta),&0\le\theta<1/2,\\
h>0,&1/2\le\theta\le1.
\end{cases}
\]
There is also exact pathwise finite-step extinction: for every \(0\le\theta<1\), the special step \(h=1/(1-\theta)\) gives \(X_2=0\) for **every** starting vector and every pair of Wiener increments, although the first step may have arbitrarily large mean-square amplification. For example, with \(\theta=0\), \(h=1\), \(\gamma=10\), \(\sigma=4\), and \(X_0=(0,1)^{\mathsf T}\), one has \(\mathbb E\|X_1\|_2^2=116\) and \(X_2=0\) almost surely.

## Assumptions and scope
The result concerns a fixed Euclidean norm and the standard drift-implicit theta-Maruyama method with **explicit Itô noise** and independent Gaussian Brownian increments. Initial states are deterministic; conditional one-step results also hold for any square-integrable adapted state independent of its next increment. The normalization of the drift diagonal to \(-1\) fixes the time unit. Parameters satisfy \(\gamma,\sigma\ge0\), \(\theta\in[0,1]\), and \(h>0\); all boundary equalities in the nonexpansivity classification are included. The noise is rank-one and nilpotent, and the drift and diffusion commute. Nonexpansivity refers to the inequality with prefactor one at **one completed step**, whereas asymptotic mean-square stability means \(\mathbb E\|X_k\|_2^2\to0\) for every deterministic initial state. These are different properties.

## Proof
Write \(d=1+\theta h\), \(r=[1-(1-\theta)h]/d\), \(u=\gamma h/d^2\), and \(v=\sigma^2h/d^2\). Since \(N^2=0\), direct inversion of \(I-\theta hA\) gives the completed random matrix
\[
X_{k+1}=M_kX_k,\qquad M_k=rI_2+\big(u+(\sigma/d)\Delta W_k\big)N.
\]
Taking the conditional squared norm yields the exact symmetric matrix
\[
G=\mathbb E(M_k^{\mathsf T}M_k)
=\begin{pmatrix}r^2&ru\\ru&r^2+u^2+v\end{pmatrix}.
\]
One-step nonexpansivity for every initial vector is equivalent to \(I_2-G\succeq0\). The first principal entry and determinant are, by exact algebra,
\[
1-r^2=\frac{hc}{d^2},\qquad
\det(I_2-G)=\frac{h^2}{d^4}\big(c^2-\sigma^2c-\gamma^2\big).
\]
For \(c>0\), the two-by-two principal-minor criterion therefore reads \(c^2-\sigma^2c-\gamma^2\ge0\), exactly \(c\ge c_*\). For \(c<0\) the top-left principal entry is negative. For \(c=0\), positive semidefiniteness is possible only when \(\gamma=\sigma=0\), where \(G=I_2\) and \(c=c_*=0\). This proves the equivalence including degenerate endpoints. Since \(c\) is affine in \(h\), the three stated cases follow without missing or disconnected steps.

For the continuous equation, the Itô identity for the squared norm gives
\[
\frac{\mathrm d}{\mathrm dt}\mathbb E\|X_t\|_2^2
=\mathbb E[X_t^{\mathsf T}HX_t],\qquad
H=A+A^{\mathsf T}+(\sigma N)^{\mathsf T}(\sigma N)
=\begin{pmatrix}-2&\gamma\\\gamma&-2+\sigma^2\end{pmatrix}.
\]
The condition \(H\preceq0\) is necessary (take the derivative at time zero in every direction) and sufficient (integrate the displayed identity). Its exact two-by-two test is \(\gamma^2+2\sigma^2\le4\). Evaluating \(c^2-\sigma^2c-\gamma^2\) at \(c=2\) establishes the claimed equivalence with \(c_*\le2\).

For asymptotic mean-square stability, define the independent scalar coefficients \(b_k=u+(\sigma/d)\Delta W_k\). Nilpotence gives the exact product identity
\[
M_{n-1}\cdots M_0=r^nI_2+r^{n-1}\left(\sum_{k=0}^{n-1}b_k\right)N
\]
for \(n\ge1\), with the evident polynomial interpretation at \(r=0\). When \(|r|<1\), its expected squared Frobenius norm equals
\[
2r^{2n}+r^{2n-2}\big(n^2u^2+nv\big)\longrightarrow0,
\]
with all products zero after step two if \(r=0\). Conversely, \(Ne_1=0\) and \(M_ke_1=re_1\), so \(|r|\ge1\) prevents mean-square decay from \(e_1\). Thus mean-square stability holds exactly when \(|r|<1\). Using \(1-r^2=hc/d^2\) yields the stated step sets. Finally, at \(h=1/(1-\theta)\), \(r=0\), so every \(M_k\) is a scalar multiple of \(N\), and \(M_1M_0=0\) identically. The explicit example follows from \(M_k=(10+4\Delta W_k)N\) with \(\Delta W_k\sim\mathcal N(0,1)\).

## Verification
The standalone `verify.py` evaluates the matrix inverse and Gram matrix, checks five rational-function identities symbolically, checks two-step extinction for four rational implicitness parameters, and compares the exact principal-minor classification against 600 deterministic rational examples. It also checks the exact amplification factor of 116 in the extinction example. All tests pass using SymPy. These finite cases **support** the algebra but do not substitute for the universal argument above.

Run from a directory containing the embedded script: `python verify.py` (Python 3 and SymPy required). No random path simulations or Monte Carlo estimates enter the proof. For an independent direct check, calculate \(M_k\) from the displayed inverse, then compute \(G=\mathbb E M_k^{\mathsf T}M_k\) using only \(\mathbb E\Delta W=0\) and \(\mathbb E(\Delta W)^2=h\).

## Relationship to prior work
D'Ambrosio and Di Giovacchino, *Mean-square contractivity of stochastic theta-methods* (first posted September 10, 2020; arXiv:2009.04941), establish nonlinear contractivity estimates under one-sided Lipschitz and diffusion Lipschitz hypotheses. Their Section 4 gives sufficient method-dependent restrictions and unconditional implicit Euler contractivity for **already dissipative** equations. The present exact matrix condition instead applies to a nonnormal linear equation with potentially noncontractive continuous dynamics, distinguishes one-step norm contractivity from asymptotic mean-square stability, and identifies the large-step recovery threshold and an exact finite-step annihilation mechanism. It is not a replacement for general nonlinear bounds.

Buckwar and Sickenberger, *A comparative linear mean-square stability analysis of Maruyama- and Milstein-type methods* (arXiv:0912.1968, 2009), specialize their main linear test to scalar dynamics with multiple noises and investigate asymptotic stability, rather than a two-dimensional defective drift with one-step Euclidean matrix contractivity. Higham, *Mean-square and asymptotic stability of the stochastic theta method* (SIAM J. Numer. Anal. 38, 2000), develops scalar linear stability criteria; a full primary-text comparison was unavailable and priority remains subject to that limitation. Biščević, D'Ambrosio, and Di Giovacchino, *Contractivity of stochastic theta-methods under non-global Lipschitz conditions* (Applied Mathematics and Computation 505, 2025), provide broader contractivity methods but the inspected linear-drift case assumes a symmetric positive-definite drift matrix, unlike the present defective, nonnormal generator. These sources give the context, not an assertion that any one-dimensional formula is new.

## Limitations
This is an exact, highly structured, two-dimensional test-equation result: it does not classify general nonnormal SDEs, noncommuting noise operators, higher-dimensional Jordan chains, Milstein schemes, or nonlinear equations. One-step contraction at a large step does **not** imply good time-discretization accuracy, faithful transient behavior, or unconditional norm contractivity at smaller steps. The finite-step zero is a numerical resonance, not a property of the exact continuous diffusion. Literature priority has not received independent verification, and the full text of Higham (2000) was not available for comparison; its scalar focus is supported by available descriptions and by later primary papers.

## References
1. R. D'Ambrosio and S. Di Giovacchino, *Mean-square contractivity of stochastic theta-methods*, arXiv:2009.04941, first public September 10, 2020. https://arxiv.org/abs/2009.04941
2. E. Buckwar and T. Sickenberger, *A comparative linear mean-square stability analysis of Maruyama- and Milstein-type methods*, arXiv:0912.1968, December 10, 2009. https://arxiv.org/abs/0912.1968
3. D. J. Higham, *Mean-square and asymptotic stability of the stochastic theta method*, SIAM J. Numer. Anal. 38 (2000), 753–769. https://doi.org/10.1137/S003614299834736X
4. H. Biščević, R. D'Ambrosio, and S. Di Giovacchino, *Contractivity of stochastic theta-methods under non-global Lipschitz conditions*, Appl. Math. Comput. 505 (2025), 129527. https://doi.org/10.1016/j.amc.2025.129527
5. Z. Aminzare, *Stochastic logarithmic Lipschitz constants: A tool to analyze contractivity of stochastic differential equations*, arXiv:2111.03155, first public November 4, 2021. https://arxiv.org/abs/2111.03155
