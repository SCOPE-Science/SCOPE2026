# Tangency-order trichotomy and log-periodic collapse-time tails in a sewed-focus family

## Finding
For each pair of integers \(m,n\ge2\), the switching system below has an exact global dynamical classification by the ratio \(p=m/n\). In the collapsing regime \(p>1\), physical absorption time for a uniformly sampled crossing amplitude has a strictly nonconstant log-periodic modulation of an exponentially decaying tail. The exponent is \(c=\log(p)/2\), giving the exact exponential-moment threshold.

Put \(L=\log p\), let \(\gamma\) be Euler's constant and define the real, analytic, nonconstant, one-periodic function
\[
P_p(w)=\frac1L\sum_{k\in\mathbb Z\setminus\{0\}}\Gamma\left(\frac{2\pi i k}{L}\right)e^{2\pi i k w}.
\]
The series converges absolutely. Set \(G_p(w)=w+P_p(w)\) and write \(W_p=G_p^{-1}\). Then \(G_p\) is an increasing bijection of the real line, \(W_p(z+1)=W_p(z)+1\), and
\[
Q_p(t)=e^{-\gamma}p^{z-W_p(z)},\qquad z=t/2+\gamma/L
\]
is positive, nonconstant, and two-periodic. For \(A\) uniform on \((0,1)\) and its absorption time \(T_p(A)\),
\[
\mathbb P(T_p(A)>t)=e^{-ct}(Q_p(t)+O_p(e^{-ct})) \quad(t\to\infty),
\]
where \(\mathbb E[e^{sT_p(A)}]<\infty\) exactly when \(s<c\). This is a statement about one-dimensional section measure, not planar Lebesgue measure.

## Assumptions and scope
Use the switching line \(y=0\), with forward evolution through transverse crossings. On \(y>0\) set \(\dot x=1\), and \(\dot y=-2m x^{2m-1}\) for \(x<0\) and \(\dot y=-2n x^{2n-1}\) for \(x\ge0\). On \(y<0\) set \(\dot x=-1\), and \(\dot y=-2n x^{2n-1}\) for \(x<0\) and \(\dot y=-2m x^{2m-1}\) for \(x\ge0\). At \(x=0\) use the continuous limiting normal component. At the origin, a trajectory terminating there is not continued through a nonunique singular extension. Other crossings are transverse because their two limiting normal components have the same strictly nonzero sign. Each half-plane field is \(C^{2\min(m,n)-2}\) across \(x=0\). We classify nonzero initial states and their forward evolution; no uniqueness through the singular origin is asserted.

## Proof
An upper flight from \((-a,0)\) begins on the graph \(y=a^{2m}-x^{2m}\) for negative \(x\), and after \(x=0\) follows \(y=a^{2m}-x^{2n}\), reaching \((a^p,0)\). Reflection across the origin gives the lower flight from \((a^p,0)\) to \((-a^{p^2},0)\). Their horizontal travel times are \(a+a^p\) and \(a^p+a^{p^2}\). Every initial point off the switching line hits it in finite forward time, as \(x\) traverses a half-line in its directed sign; hence section dynamics classifies every nontrivial forward orbit. The full section return is \(a\mapsto a^{p^2}\), with unique fixed positive radius \(a=1\) when \(p\ne1\), and every positive radius fixed when \(p=1\). For \(p<1\), all positive radii approach \(1\) and the unique period-four orbit is attracting. For \(p=1\) every nonzero orbit is periodic with period \(4a\). For \(p>1\), the radius-one period-four orbit is repelling; amplitudes \(a<1\) shrink to zero, whereas \(a>1\) diverge along an infinite-time orbit. This gives the global trichotomy (with time measured in the original flow). In the collapsing case, summing each flight yields exactly
\[
T_p(a)=a+2\sum_{j=1}^{\infty}a^{p^j}=2\sum_{j=0}^{\infty}e^{-q p^j}-e^{-q},\qquad q=-\log a.
\]
The series converges for each \(0<a<1\). The origin is reached in finite physical time because the section crossings converge there, and all flight times sum to this finite value.

For the asymptotic, write \(q=p^{-w}\), \(w=N+u\) with \(N\in\mathbb N\) and \(0\le u<1\). Define
\[
H_p(u)=\sum_{k\in\mathbb Z}\bigl(e^{-p^{k-u}}-\mathbf 1_{\{k<0\}}\bigr).
\]
Both tails converge absolutely and uniformly on compact \(u\)-ranges. Reindexing shows \(H_p(u+1)=H_p(u)+1\). The missing negative-index tail in the original sum lies between zero and \(q/(p-1)\), giving
\[
\sum_{j\ge0}e^{-qp^j}=w+C_p(w)+R_p(q),\qquad 0\le R_p(q)\le q/(p-1),
\]
where \(C_p(u)=H_p(u)-u\) is one-periodic. Termwise differentiation yields
\[
H_p'(u)=L\sum_{k\in\mathbb Z}p^{k-u}e^{-p^{k-u}}>0.
\]
The Fourier coefficients of this periodized exponential kernel are obtained by substituting \(v=p^{k-u}\) over the tiled positive half-line: for \(r\ne0\), the coefficient of \(C_p\) is \(\Gamma(2\pi i r/L)/L\). The constant coefficient, by integration of the exponential integral or its Mellin expansion, is \(1/2-\gamma/L\). Thus \(C_p=1/2-\gamma/L+P_p\) and
\[
T_p(e^{-q})=2w-2\gamma/L+2P_p(w)+E_p(q),\quad 0\le E_p(q)\le(1+2/(p-1))q.
\]
The Gamma function has no zeros, so the first nonzero Fourier coefficient proves that \(P_p\) is not constant. Since \(G_p'=H_p'>0\) and \(G_p(w+1)=G_p(w)+1\), it has the asserted increasing inverse.

The function \(T_p(a)\) is strictly increasing in \(a\in(0,1)\) and diverges as \(a\uparrow1\). For a large threshold \(t\), its inverse amplitude can be parametrized as \(a_t=e^{-p^{-w_t}}\). The displayed error bound, with a uniform positive lower bound on \(G_p'\), implies \(w_t=W_p(t/2+\gamma/L)+O_p(p^{-w_t})\). Hence \(\mathbb P(T_p(A)>t)=1-a_t=p^{-w_t}+O_p(p^{-2w_t})\), which is the tail formula. Nonconstancy of \(Q_p\) follows because if it were constant then \(W_p(z)-z\) would be constant, forcing \(P_p\) constant. The exponential moment criterion follows by integrating the positive tail against \(s e^{st}\); at \(s=c\) a positive periodic factor prevents integrability.

## Verification
The standalone script `CHECK.py` independently checks exact rational section powers and flight times for integer degree pairs, compares the periodized and Fourier expressions by high-precision arithmetic, checks the stated error bound and positivity, and tests the tail-phase relation numerically. Finite checks corroborate but do not prove universal statements. The proof is analytical.

## Relationship to prior work
Glendinning, Hogan, Homer, Jeffrey and Szalai (2023), Section 3, already establish finite-time collapse for the special ratio \(p=2\), including the exact sum \(T_2(a)\); that component is not claimed as novel. Their Section 4 treats local qualitative sewed-focus classes, rather than a global unequal-degree family with sharp section-sampled physical-time tails and an explicit nonconstant periodic amplitude. Their 2024 follow-up classifies topological singularity types; such classification alone does not specify the present quantitative tail. Flajolet, Gourdon and Dumas (1995) supply the classical Mellin method and log-periodic fluctuations for harmonic sums, so this analytic mechanism is credited and not claimed new in isolation.

## Limitations
The claimed distinction is the dynamical realization and exact section hitting-time distribution, not the generic Mellin transform of a lacunary exponential sum. The distribution is based on a uniform amplitude on one section and need not describe natural planar invariant measures. No uniqueness of extensions through the collapsed origin is asserted. Possible independently published, equivalent quantitative results outside inspected sources remain a priority risk; there has been no independent validation.

## References
1. P. Glendinning, S. J. Hogan, M. Homer, M. R. Jeffrey, R. Szalai, *Uncountably many cases of Filippov's sewed focus*, Journal of Nonlinear Science 33 (2023), article 52, DOI: 10.1007/s00332-023-09910-4, arXiv:2306.09743v1. First publicly online 2023-05-05.
2. P. Glendinning, S. J. Hogan, M. E. Homer, M. R. Jeffrey, R. Szalai, *Classification of Filippov Type 3 Singular Points in Planar Bimodal Piecewise Smooth Systems*, SIAM Journal on Applied Dynamical Systems 23 (2024), 2242–2261, DOI: 10.1137/23M1622842.
3. P. Flajolet, X. Gourdon, P. Dumas, *Mellin transforms and asymptotics: harmonic sums*, Theoretical Computer Science 144 (1995), 3–58, DOI: 10.1016/0304-3975(95)00002-E.
