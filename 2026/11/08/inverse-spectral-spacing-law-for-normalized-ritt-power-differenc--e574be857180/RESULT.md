# Inverse spectral-spacing law for normalized Ritt power differences

## Finding
Let \(0\le\phi<\pi/2\), put \(b=\cos\phi>0\), and let \((r_k)_{k\ge1}\) be any strictly decreasing positive sequence with \(r_k\to0\), \(r_1<2b\), and \(r_{k+1}/r_k\to q\in[0,1]\). On complex \(\ell^2(\mathbb N)\) set
\[
 T e_k=(1-r_ke^{i\phi})e_k,\qquad
 D_n=n\|T^n-T^{n+1}\|\quad(n\ge1).
\]
For \(0<q<1\), define
\[
 L(q)=\frac{\log(1/q)}{1-q},\qquad
 \Phi(q)=e\,L(q)e^{-L(q)},
\]
and extend continuously by \(\Phi(0)=0\) and \(\Phi(1)=1\). Then \(T\) is a normal Ritt contraction, \(T-I\) is compact, and the **entire accumulation set** of \((D_n)\) is exactly
\[
 \boxed{\left[\frac{\Phi(q)}{eb},\frac1{eb}\right]}.
\]
In particular the upper and lower limits are the respective endpoints. The ratio of the lower to the upper limit is \(\Phi(q)\); as \(\Phi:[0,1]\to[0,1]\) is continuous and strictly increasing, the asymptotic spectral ratio \(q\) is uniquely reconstructed from the two long-time norm limits, independently of \(\phi\).

The exact reduction underlying the result is, with \(h(x)=xe^{-x}\),
\[
 D_n=\frac1b\max_{k\ge1}h(bnr_k)+O(n^{-1}) \qquad (n\to\infty).
\]
The implied constant may depend on \(b\) and the sequence but not on \(n\). Every interval in the displayed family can be realized by choices with \(T-I\in\bigcap_{p>0}\mathcal S_p\), and the perturbation can have arbitrarily small \(\mathcal S_p\) quasi-norm for any *fixed* \(p>0\), without changing its limiting interval.

## Assumptions and scope
The space is the complex Hilbert space \(\ell^2(\mathbb N)\) with its standard orthonormal basis. The sequence \((r_k)\) is indexed by all positive integers; no regular-variation or exact-geometric assumption is made beyond the existence of \(q=\lim r_{k+1}/r_k\). The strict inequality \(r_1<2\cos\phi\) ensures every individual eigenvalue is strictly inside the unit disk. The scalar \(e\) in the formulas is Euler's number, not a basis vector. A Ritt operator means one with spectrum in the closed disk and \(\sup_{|z|>1}|z-1|\|(z-T)^{-1}\|<\infty\). Accumulation set means the set of finite real subsequential limits as integer \(n\to\infty\).

## Proof
**1. Ritt property.** For \(a(r)=|1-re^{i\phi}|=\sqrt{1-2br+r^2}\), the assumption \(0<r\le r_1<2b\) gives \(a(r)<1\). The quotient \((1-a(r))/r\) extends continuously to \(r=0\), with limit \(b>0\). Therefore there is \(c>0\) with \(1-a(r)\ge cr\) on \((0,r_1]\). For \(|z|>1\),
\[
 |z-1|\le |z-(1-re^{i\phi})|+r
 \le (1+c^{-1})|z-(1-re^{i\phi})|,
\]
because \(|z-(1-re^{i\phi})|\ge1-a(r)\ge cr\). Taking the supremum of these diagonal resolvents proves the Ritt estimate. The eigenvalues are strictly inside the disk, so \(T\) is a normal contraction, while \(T-I\) is compact since its diagonal entries tend to zero.

**2. Uniform scalar envelope.** Diagonalization gives \(D_n=\sup_k nr_k a(r_k)^n\). For sufficiently small \(r\), Taylor's formula gives
\[
 \log a(r)=-br+O(r^2),\qquad a(r)^n\le e^{-c_0nr}
\]
with \(c_0>0\). By the mean-value bound for the exponential, for these \(r\)
\[
 nr\,|a(r)^n-e^{-bnr}|
 \le C n^2r^3 e^{-c_1nr}\le C'/n.
\]
For the remaining \(r\) in a closed subinterval of \((0,r_1]\), both expressions are exponentially small in \(n\), uniformly. Taking the supremum proves the displayed \(O(n^{-1})\) reduction. The maximum exists since \(h(bnr_k)\to0\) as \(k\to\infty\).

**3. Upper and lower limits.** Write \(y_{k,n}=bnr_k\), so the envelope is \(b^{-1}\max_k h(y_{k,n})\). Because \(h\) increases on \([0,1]\) and decreases on \([1,\infty)\), it is never larger than \(1/e\). Choosing integers \(n_k\) nearest to \((br_k)^{-1}\) makes \(y_{k,n_k}\to1\), so the upper limit is exactly \(1/(eb)\).

For sufficiently large \(n\), there is a unique \(j=j(n)\) with \(y_{j,n}\ge1>y_{j+1,n}\) (ties may be assigned to the larger \(j\)); monotonicity of \(h\) gives the **exact two-neighbor formula**
\[
 \max_k h(y_{k,n})=
 \max\{h(y_{j,n}),h(y_{j+1,n})\}.
\]
Put \(q_j=r_{j+1}/r_j\). For fixed \(0<q_j<1\), as \(y\) varies on \([1,1/q_j]\), the decreasing function \(h(y)\) and the increasing function \(h(q_jy)\) cross only at
\[
 y=L(q_j)=\frac{\log(1/q_j)}{1-q_j},
 \qquad 1<L(q_j)<1/q_j.
\]
Thus their maximum has minimum \(L(q_j)e^{-L(q_j)}\), and this lower bound applies to every sufficiently large \(n\). When \(0<q<1\), integers nearest \(L(q)/(br_j)\) realize the crossing asymptotically, as \(j\to\infty\). This yields lower limit \(L(q)e^{-L(q)}/b\). If \(q=0\), instead choose integers near \((b\sqrt{r_jr_{j+1}})^{-1}\); the two bracketing arguments tend to infinity and zero respectively, so the lower limit is zero. If \(q=1\), the bracketing arguments both tend to one for every sufficiently large \(n\), so the lower and upper limits coincide. These agree exactly with \(\Phi(q)/(eb)\).

**4. No gaps in the accumulation set.** The derivative of \(x\mapsto xe^{-bx}\) and \(\sup_{x\ge0}x(1+x)e^{-bx}<\infty\) give, uniformly in \(k\),
\[
 |(n+1)r_ke^{-b(n+1)r_k}-nr_ke^{-bnr_k}|\le C/n.
\]
The maximum operation is nonexpansive for the supremum norm; combining this inequality with step 2 gives \(|D_{n+1}-D_n|=O(n^{-1})\). A bounded real sequence with successive differences tending to zero has the entire interval between its liminf and limsup as its accumulation set: crossing any intermediate value at arbitrarily large indices forces arbitrarily close terms. This completes the exact-interval assertion.

**5. Inverse and Schatten constructions.** For \(0<q<1\), the function \(L(q)\) decreases strictly from infinity to one, while \(x\mapsto e x e^{-x}\) decreases strictly for \(x>1\). Hence \(\Phi\) is a strictly increasing continuous bijection of \([0,1]\). For each prescribed \(q\), one may choose, for sufficiently small \(c>0\),
\[
 r_k=\begin{cases}
 c e^{-2^k},&q=0,\\
 c q^k,&0<q<1,\\
 c e^{-\sqrt{k}},&q=1.
 \end{cases}
\]
These are strictly decreasing, have the required successive-ratio limits, and belong to \(\ell_p\) for **every** \(p>0\). As the singular values of \(I-T\) are precisely \(r_k\), every corresponding \(I-T\) lies in every Schatten class. Scaling \(c\) makes any one prescribed Schatten quasi-norm arbitrarily small, without altering \(q\) or the accumulation interval. This is not a uniform bound over all exponents \(p\) simultaneously.

## Verification
The standalone standard-library Python file `checker.py` evaluates exact finite diagonal power-difference norms using \(\log(1+u)\) for numerical stability. It tests the predicted geometric peak and valley constants, the dense- and sparse-spacing regimes, and the two-neighbor crossing equation. It reports `finite_diagnostics_passed 297`. These finite tests are diagnostic only; steps 1–5 supply the infinite-dimensional proof and the complete accumulation-set argument.

## Relationship to prior work
Borichev, Gomilko, and Tomilov, *Beurling–Kato theory, Hardy–Sobolev calculus and Ritt operators* (arXiv:2607.10507, first submitted 11 July 2026), establish broad Ritt characterizations, norm gaps, and resolvent criteria. Badea, *Iterates of Ritt operators close to the identity* (arXiv:2609.27458), studies sampled powers and constructs diagonal normal test operators for Ritt-detection questions; its Theorem 5.9 concerns boundedness tests along subsequences of **time indices**, not the exact asymptotic cluster set for a fixed contracting ray spectrum. Mahillo and Rueda, *A Ritt–Kreiss condition: spectral localization and norm estimates* (arXiv:2404.12946), give global growth bounds; they do not supply the spectral-gap inverse or the exact limits above. These works provide definitions and motivating context. The new claim is the exact correspondence between *spatial eigenvalue-gap ratios* and *all cluster values* of the normalized power-difference norms, including its inverse and all-Schatten realizations; it does not assert novelty of the Ritt criterion itself.

## Limitations
The classification requires a common spectral ray and an asymptotic ratio limit. It does not extend automatically to nonnormal operators, spectra with multiple approach angles, or arbitrary oscillating gap ratios. The correction \(O(n^{-1})\) is for each fixed operator and is not uniform over all choices of sequences. Finite computations do not certify the infinite result. Publication priority beyond the literature compared here remains subject to external verification.

## References
1. A. Borichev, A. Gomilko, Yu. Tomilov, *Beurling–Kato theory, Hardy–Sobolev calculus and Ritt operators*, arXiv:2607.10507v1 (11 July 2026), https://arxiv.org/abs/2607.10507.
2. C. Badea, *Iterates of Ritt operators close to the identity*, arXiv:2609.27458 (23 September 2026), https://arxiv.org/abs/2609.27458.
3. A. Mahillo, S. Rueda, *A Ritt–Kreiss condition: spectral localization and norm estimates*, arXiv:2404.12946 (19 April 2024), https://arxiv.org/abs/2404.12946.
