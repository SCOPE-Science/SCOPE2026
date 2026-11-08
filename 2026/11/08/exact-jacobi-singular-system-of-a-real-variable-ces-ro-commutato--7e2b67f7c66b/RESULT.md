# Exact Jacobi singular system of a real-variable Cesàro commutator

## Finding
Let \(H=L^2((0,1);\mathbb C)\), let \(M\) denote multiplication by \(x\), and let \(C\) be the bounded real-variable Cesàro operator
\[
(Cf)(x)=\frac1x\int_0^x\frac{f(t)}{1-t}\,dt\qquad(0<x<1).
\]
Set \(T=MC-CM\). For every integer \(n\ge1\), define the functions
\[
 u_n(x)=\sqrt{2n+1}\,x P_{n-1}^{(0,2)}(2x-1),\qquad
 v_n(x)=\sqrt{2n+1}\,(1-x)P_{n-1}^{(2,0)}(2x-1),
\]
where \(P_m^{(a,b)}\) denotes the usual Jacobi polynomial, normalized by \(P_m^{(a,b)}(1)=\binom{m+a}{m}\).

**Complete singular-system theorem.** Both \((u_n)_{n\ge1}\) and \((v_n)_{n\ge1}\) are orthonormal bases of \(H\), and
\[
 Tv_n=\frac{1}{n(n+1)}u_n,\qquad
 T^*u_n=\frac{1}{n(n+1)}v_n\quad(n\ge1).
\]
Consequently the entire nonzero singular-value sequence, including multiplicity, is
\[
 \boxed{s_n(T)=\frac1{n(n+1)}\qquad(n\ge1).}
\]
In particular, \(\|T\|=1/2\), \(\|T\|_{\mathcal S_1}=1\), and
\[
 \|T\|_{\mathcal S_2}^2=\frac{\pi^2}{3}-3,\qquad
 T\in\mathcal S_p\ \Longleftrightarrow\ p>\tfrac12\quad(0<p<\infty).
\]
At the critical value, \(T\) belongs to weak \(\mathcal S_{1/2}\), with \(\sup_{n\ge1}n^2s_n(T)=1\), but not to strong \(\mathcal S_{1/2}\). Despite these nonzero singular values, \(T\) is quasinilpotent: \(\sigma(T)=\{0\}\).

## Assumptions and scope
The Hilbert space is complex \(L^2(0,1)\) with Lebesgue measure, and all norms and singular values refer to that unweighted Hilbert structure. The Jacobi parameters are fixed to \((0,2)\) and \((2,0)\). The operator \(C\) is the **normal real-variable Cesàro operator containing the denominator \(1-t\)**, not the classical Hardy averaging operator \(f\mapsto x^{-1}\int_0^x f\). The Schatten equivalence is asserted for every real \(p>0\), using quasi-norm ideals when \(p<1\). The singular-value index starts at \(n=1\).

## Proof
**1. Kernel and compactness.** The commutator is initially computed on, for example, compactly supported smooth functions in \((0,1)\):
\[
 (Tf)(x)=\frac1x\int_0^x\frac{x-t}{1-t}f(t)\,dt
       =\int_0^1K(x,t)f(t)\,dt,\quad
 K(x,t)=\mathbf1_{\{0<t<x<1\}}\frac{x-t}{x(1-t)}.
\]
Since \(x-t\le x(1-t)\) for \(0<t<x<1\), we have \(0\le K\le1\). Thus \(K\in L^2((0,1)^2)\) and \(T\) extends as a Hilbert–Schmidt operator. Because \(M\) and \(C\) are bounded, this extension is the original commutator.

**2. Orthogonality and completeness.** The shifted Jacobi orthogonality formulas, for integers \(m,k\ge0\), give
\[
 \int_0^1 x^2 P_m^{(0,2)}(2x-1)P_k^{(0,2)}(2x-1)\,dx
   =\frac{\delta_{mk}}{2m+3},
\]
\[
 \int_0^1 (1-x)^2 P_m^{(2,0)}(2x-1)P_k^{(2,0)}(2x-1)\,dx
   =\frac{\delta_{mk}}{2m+3}.
\]
The \(\sqrt{2n+1}\) factors make the two displayed systems orthonormal. Jacobi polynomials are dense in both weighted spaces \(L^2(x^2dx)\) and \(L^2((1-x)^2dx)\); multiplication by \(x\) and by \(1-x\), respectively, are unitary maps from these weighted spaces onto ordinary \(L^2(dx)\). Hence both systems are complete.

**3. The exact all-degree integral identity.** Set \(m=n-1\). The terminating hypergeometric formulas (ordinary polynomials) read
\[
 P_m^{(2,0)}(2t-1)=(-1)^m\,{}_2F_1(-m,m+3;1;t),
\]
\[
 P_m^{(0,2)}(2x-1)=(-1)^m\binom{m+2}{2}\,{}_2F_1(-m,m+3;3;x).
\]
Term-by-term integration is legitimate because the sums terminate. Using
\(\int_0^x(x-t)t^k\,dt=x^{k+2}/[(k+1)(k+2)]\) and \((3)_k=(k+2)!/2\), coefficient comparison yields
\[
 \int_0^x(x-t)P_m^{(2,0)}(2t-1)\,dt
 =\frac{x^2}{(m+1)(m+2)}P_m^{(0,2)}(2x-1).
\]
Insert \(v_n(t)=\sqrt{2n+1}(1-t)P_{n-1}^{(2,0)}(2t-1)\) into the kernel. The factors \((1-t)\) cancel and the identity gives
\[
 Tv_n(x)=\frac{\sqrt{2n+1}}{x}\int_0^x(x-t)P_{n-1}^{(2,0)}(2t-1)\,dt
          =\frac{u_n(x)}{n(n+1)}.
\]
Completeness of both orthonormal systems shows that this is an **entire** singular-value decomposition: in particular \(T^*u_n=v_n/[n(n+1)]\), with no missing spectral branches or multiplicities.

**4. Sharp ideal classification.** The sequence \(1/[n(n+1)]\) strictly decreases to zero. Its largest entry is \(1/2\). Telescoping gives
\(\|T\|_{\mathcal S_1}=\sum_{n\ge1}(1/n-1/(n+1))=1\). Partial fractions give
\[
 \frac1{n^2(n+1)^2}=\frac1{n^2}+\frac1{(n+1)^2}-\frac2{n(n+1)},
\]
so \(\sum_{n\ge1}s_n(T)^2=2\zeta(2)-3=\pi^2/3-3\). Since \(n^2s_n(T)\to1\), the series \(\sum_n s_n(T)^p\) converges exactly when \(2p>1\), and the stated weak endpoint follows.

**5. Spectrum, distinct from singular spectrum.** The kernel inequality \(0\le K(x,t)\le\mathbf1_{\{t<x\}}\) gives \(|T^jf|\le V^j|f|\) pointwise, where \((Vg)(x)=\int_0^xg(t)\,dt\). The iterated Volterra kernel of \(V^j\) is \(\mathbf1_{t<x}(x-t)^{j-1}/(j-1)!\). Schur's test yields \(\|V^j\|\le1/j!\), hence \(\|T^j\|\le1/j!\) and the spectral radius of \(T\) vanishes. Compactness and nontriviality therefore imply \(\sigma(T)=\{0\}\). In particular \(T\) is an injective, trace-class quasinilpotent whose singular spectrum is nevertheless the displayed infinite sequence.

## Verification
Execute the accompanying standalone script using `python3 check_jacobi_svd.py` (Python standard library only). It checks 44 exact rational polynomial-integral identities, for degrees \(0\) through \(43\), and 392 exact rational weighted Jacobi orthogonality relations, including cross terms, for indices \(0\) through \(13\). It also checks a finite telescoping identity. The expected marker is `REAL_CESARO_JACOBI_EXACT_OK 44 polynomial-integral identities; 392 weighted orthogonality identities`. These finite checks corroborate the proof; the all-degree identities and infinite-dimensional statements follow from the analytic arguments above, not extrapolation.

## Relationship to prior work
Belli, Gül, Ross, and Siskakis introduce the real-variable Cesàro operator on \(L^2(0,1)\) and establish its normality, norm, spectrum, and invariant-subspace properties (arXiv:2604.19691v1, 21 April 2026). Their subsequent *Crescents and the Real Variable Cesàro Operator* (arXiv:2606.08600v1, 7 June 2026; open-access journal version September 2026) extends the operator analysis to \(L^p\). Neither examined full text supplies a Jacobi singular-value decomposition of the coordinate commutator.

A superficially similar but mathematically **different** object is the Hardy–Volterra commutator \(MH-HM\), where \((Hf)(x)=x^{-1}\int_0^x f(t)\,dt\). Its kernel is \((x-t)/x\), lacking the essential factor \(1/(1-t)\). Deng, Fischer, and Hofmann (arXiv:2401.11411v1, 21 January 2024) establish quadratic-order singular-value decay for this Hardy-based composite operator; their statement neither identifies the present singular basis nor implies the exact numbers. Related published spectral work on that Hardy commutator gives an implicit characteristic determinant, again for the different kernel. Classical Jacobi orthogonality is used as a proof tool, not asserted to be new.

## Limitations
The result concerns the fixed multiplication symbol \(x\), not arbitrary bounded multipliers, and only the Hilbert case \(p=2\). It does not classify commutators with other functions or the essential spectrum of \(C\) itself. The exact Jacobi integration identity is classical, so the remaining priority risk is a broader weighted-integration or inverse-Jacobi Green-operator theorem that could contain this specific commutator after a nontrivial change of representation. A search not finding such a result is not a uniqueness proof; independent publication-priority and mathematical audits have not been performed.

## References
1. A. Belli, U. Gül, W. T. Ross, A. G. Siskakis, *The Cesàro operator on \(L^2(0,1)\)*, arXiv:2604.19691v1, publicly submitted 21 April 2026; https://arxiv.org/abs/2604.19691 .
2. A. Belli, U. Gül, W. T. Ross, A. G. Siskakis, *Crescents and the Real Variable Cesàro Operator*, arXiv:2606.08600v1, 7 June 2026; *Integral Equations and Operator Theory* **98** (2026), art. 42, DOI:10.1007/s00020-026-02865-7.
3. Y. Deng, H.-J. Fischer, B. Hofmann, *The degree of ill-posedness for some composition governed by the Cesàro operator*, arXiv:2401.11411v1, 21 January 2024.
4. N. M. Chuong, H. D. Hung, *A generalized weighted Hardy–Cesàro operator, and its commutator on weighted \(L^p\) and BMO spaces*, arXiv:1208.5242v1, 26 August 2012.
5. G. Szegő, *Orthogonal Polynomials*, American Mathematical Society Colloquium Publications, vol. 23, for Jacobi polynomial orthogonality and terminating series identities.
