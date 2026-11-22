# Exact two-bond numerical-range bifurcation and tunneling for bilateral shifts

## Finding
Let \(c>1\) and let \(d\ge1\) be an integer. The bilateral weighted shift \(S_{c,d}\) on \(\ell^2(\mathbb Z)\) is defined by \(S_{c,d}e_n=w_ne_{n+1}\), where \(w_0=w_{d+1}=c\) and every other \(w_n=1\). Put \(J_{c,d}=(S_{c,d}+S_{c,d}^*)/2\). For \(0<r<1\), write \(L(r)=(r+r^{-1})/2\) and
\[
 F_+(r)=1-c^2r^2-(c^2-1)r^{d+2},\qquad
 F_-(r)=1-c^2r^2+(c^2-1)r^{d+2}.
\]
There is exactly one root \(r_+\in(0,1/c)\) of \(F_+\). A root \(r_-\in(1/c,1)\) of \(F_-\) exists exactly when
\[
 \boxed{d(c^2-1)>2}.\tag{1}
\]
When present, that root is unique. The essential spectrum of \(J_{c,d}\) is \([-1,1]\); its **complete** spectrum outside this interval consists of the simple eigenvalues \(\pm L(r_+)\) and, if (1) holds, also the simple eigenvalues \(\pm L(r_-)\). No eigenvalues occur in \([-1,1]\). At equality in (1), the lower outlier is replaced by a bounded, non-square-summable band-edge solution.

The **entire numerical range** is the closed disk
\[
 \boxed{W(S_{c,d})=\{z\in\mathbb C:|z|\le L(r_+)\}.}\tag{2}
\]
For fixed \(c>1\), as \(d\to\infty\), both positive outliers tend to \(L(1/c)=(c+c^{-1})/2\), and their exact first-order splitting is
\[
 \boxed{L(r_+)-L(r_-)\sim\frac{(c^2-1)^2}{2c^{d+3}}.}\tag{3}
\]
Moreover \(L(r_+)\) decreases strictly with \(d\), while \(L(r_-)\), once it exists, increases strictly with \(d\). Thus the *number* of positive bound modes has a sharp separation-dependent transition, but the outer numerical radius has no such disappearance.

## Assumptions and scope
All statements concern the **bilateral**, not unilateral, Hilbert-space shift with exactly two positive identical enhanced bonds at indices \(0\) and \(d+1\), separated by \(d\) normal bonds. The gap is an integer \(d\ge1\), the contrast is any real \(c>1\), and the spectrum is that of the bounded selfadjoint operator \(J_{c,d}\). The formula (3) fixes \(c\) before taking \(d\to\infty\); no uniform assertion as \(c\downarrow1\) is made. Formula (2) is the complex numerical range of \(S_{c,d}\), not its operator spectrum.

## Proof
**1. Free tails and exact matching.** Fix \(\lambda>1\) and its unique decaying parameter \(r\in(0,1)\) such that \(\lambda=L(r)\). Away from the exceptional bonds the eigenvector recurrence is
\[
 2\lambda u_n=u_{n-1}+u_{n+1}.
\]
Any square-summable candidate has left tail \(u_n=A r^{-n}\) for \(n\le0\), with \(A\ne0\). The equations across the first enhanced bond imply \(u_1=A/(cr)\) and, for \(1\le n\le d+1\),
\[
 u_n=\frac{A}{cr(1-r^2)}\left[(c^2-1)r^2r^{n-1}+(1-c^2r^2)r^{-(n-1)}\right].\tag{4}
\]
The right tail must obey \(u_{d+2}=cru_{d+1}\) and \(u_{d+2+j}=u_{d+2}r^j\) for every \(j\ge0\). Its equation at site \(d+1\) reduces to
\[
 u_d=(r+r^{-1}-c^2r)u_{d+1}.\tag{5}
\]
Inserting (4) into (5) and clearing nonzero factors gives exactly
\[
 (1-c^2r^2)^2=(c^2-1)^2r^{2d+4},\tag{6}
\]
namely \(F_+(r)F_-(r)=0\). Conversely, every root in \((0,1)\) constructs a nonzero square-summable eigenvector by (4) and the two tails. The left-tail datum \(A\) fixes the full vector, proving geometric simplicity; selfadjointness yields algebraic simplicity.

**2. Count of roots and the sharp threshold.** \(F_+(0)=1\), \(F_+(1)<0\), and \(F_+'(r)<0\) for \(0<r<1\), hence \(F_+\) has exactly one root. Since \(F_+(1/c)<0\), it lies below \(1/c\). For the second sign, use the factorization
\[
 F_-(r)=(1-r^2)\left[1-(c^2-1)H_d(r)\right],\qquad
 H_d(r)=\frac{r^2}{1+r}\sum_{j=0}^{d-1}r^j.\tag{7}
\]
The function \(H_d\) is strictly increasing on \((0,1)\): both \(r^2/(1+r)\) and \(\sum_{j=0}^{d-1}r^j\) are positive and nondecreasing, and the first increases strictly. Its endpoint limits are \(0\) and \(d/2\). Hence \(F_-\) has exactly one root in \((0,1)\) if and only if \((c^2-1)d/2>1\); otherwise none. Because \(F_-(1/c)>0\) and \(F_-(1)=0\), that root lies above \(1/c\). At equality the right/left tail solution of the band-edge recurrence \(2u_n=u_{n-1}+u_{n+1}\) is constant on both tails with opposite signs, and does not belong to \(\ell^2\), establishing the claimed resonance.

**3. Exhaustion and numerical range.** \(J_{c,d}\) differs from the free bilateral Jacobi matrix by a finite-rank perturbation, so its essential spectrum is \([-1,1]\). For an energy strictly inside the band, each free tail is a nondecaying combination of complex exponentials; at either edge it is affine in the site index. No such nonzero tail is square-summable, so there are no embedded or edge eigenvalues. Bipartite conjugation \((\Gamma u)_n=(-1)^nu_n\) gives \(\Gamma J_{c,d}\Gamma=-J_{c,d}\), providing exactly the negatives of the already listed positive eigenvalues. Their location and the essential band imply \(\|J_{c,d}\|=L(r_+)\).

The diagonal unitaries \(U_\theta e_n=e^{in\theta}e_n\) show \(U_\theta^*S_{c,d}U_\theta=e^{-i\theta}S_{c,d}\). The numerical range is convex and rotationally symmetric; its maximal real part is \(\sup_{\|u\|=1}\langle J_{c,d}u,u\rangle=L(r_+)\), achieved on a real normalized positive-eigenvalue vector. Rotations and convexity then give the closed disk (2), including its boundary.

**4. Monotonicity and tunneling.** At any fixed \(r\in(0,1)\), increasing \(d\) increases \(F_+(r)\), so its unique root increases; as \(L\) decreases on \((0,1)\), \(L(r_+)\) strictly decreases. For \(F_-\), the quantity \(H_d(r)\) increases strictly with \(d\); hence its root, when present, decreases and \(L(r_-)\) strictly increases. Both roots tend to \(1/c\), by (6) and monotone bracketing. Writing \(a=c^2-1\) and expanding the two equations at \(r_0=1/c\) yields, for fixed \(c\),
\[
 r_\pm=\frac1c\mp\frac a2 c^{-(d+3)}\left[1+O_c(dc^{-d})\right].\tag{8}
\]
Here the signs refer to \(F_+\) and \(F_-\), respectively; the error follows from the mean-value theorem since the derivatives of the perturbation \(ar^{d+2}\) are \(O_c(dc^{-(d+1)})\) near \(1/c\). Finally \(L'(1/c)=-(c^2-1)/2\); substitute (8) to obtain the two shifted energies and (3).

## Verification
The fully standalone `CHECK.py` uses rational arithmetic to test the transfer identity (6) directly against the boundary matching equation for 108 rational parameter choices, then tests root placement, the sharp threshold, strict monotonicity, and the full Jacobi eigenvector recurrence over several thousand combinations of contrasts, separations and sites. Run `python3 CHECK.py`; its observed output was `DOUBLE_BOND_TRANSFER_CHECK_OK 4498`. These finite checks support implementation fidelity only. Root uniqueness, the complete infinite spectrum and the asymptotics are established by the analytic proof above.

## Relationship to prior work
Ghosh, Birbonshi and Ojha (2026) derive numerical-radius formulas and bounds for geometrically damped periodic unilateral weighted shifts. Their full paper's introduction lists previously studied eventually constant *unilateral* weights; the particular two-separated-bond **bilateral** classification, explicit second-mode threshold, and asymptotic splitting (1)–(3) are not asserted there. Webb and Olver (2017 preprint; 2021 journal) give a general finite-rank Jacobi spectral-root framework and compute a single enhanced *boundary* bond. Its polynomial method can in principle be specialized, but its published general theorem does not state (1)–(3) or the whole-line numerical-range classification. Other work on two *onsite* perturbations and on adjacent defects in unilateral shifts provides related physical and operator-theoretic techniques, but not the same off-diagonal gap transition. Thus the contribution claimed here is the complete explicit special-family phase diagram and tunneling constant, not the novelty of transfer matrices or general finite-rank Jacobi spectral theory.

## Limitations
The model has exactly two identical enhanced positive weights; unequal defects, decaying backgrounds, and non-selfadjoint couplings are not treated. The splitting asymptotic is fixed-contrast only. The literature comparison does not establish an exhaustive priority claim against older, less indexed two-bond tight-binding calculations. No independent audit was performed.

## References
1. A. Ghosh, R. Birbonshi, S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486v1, publicly posted 2026-08-18, https://arxiv.org/abs/2608.17486 .
2. M. Webb, S. Olver, *Spectra of Jacobi operators via connection coefficient matrices*, arXiv:1702.03095, 2017, and *Communications in Mathematical Physics* **382** (2021), 657–707, https://arxiv.org/abs/1702.03095 , https://doi.org/10.1007/s00220-021-03939-w .
3. B. Hetényi, B. Dóra, *Localized states and skin effect around non-Hermitian impurities in tight-binding models*, arXiv:2508.00519, 2025, https://arxiv.org/abs/2508.00519 (one-bond, distinct model).
