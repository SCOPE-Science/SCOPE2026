# A logarithmic second Weyl term at the critical Bergman-kernel trace boundary on a rank-two matrix ball

## Finding
Let \(\Omega=\{Z\in M_2(\mathbb C):I-ZZ^*>0\}\) and, for fixed \(\gamma>0\), let \(d\nu_\gamma(Z)=c_\gamma\det(I-ZZ^*)^\gamma\,dV(Z)\) be probability-normalized volume. Define the positive Bergman-type integral operator on \(L^2(\Omega,d\nu_\gamma)\) by
\[
(T_\gamma f)(Z)=\int_\Omega \frac{f(W)}{\det(I-ZW^*)^{\gamma+1}}\,d\nu_\gamma(W).
\]
Write \(N_\gamma(\tau)=\#\{j:s_j(T_\gamma)>\tau\}\), counting multiplicities for \(\tau>0\). Put
\[
A_\gamma=(\gamma+1)(\gamma+2)(\gamma+3),\qquad
B_\gamma=\gamma(\gamma+1)(\gamma+2).
\]
The exact two-term counting law is
\[
\boxed{N_\gamma(\tau)=\frac{(\gamma+1)(\gamma+2)^2(\gamma+3)}{6\tau}
-\frac{(A_\gamma B_\gamma)^{2/3}}6\tau^{-2/3}\log(1/\tau)
+O_\gamma(\tau^{-2/3})}\qquad(\tau\downarrow0).
\]
In particular, \(T_\gamma\) is measurable in the weak trace ideal \(\mathcal L^{1,\infty}\), is not trace class, and has
\[
\lim_{j\to\infty}j\,s_j(T_\gamma)=\lim_{J\to\infty}\frac{\sum_{j=1}^J s_j(T_\gamma)}{\log J}
=\operatorname{Tr}_\omega(T_\gamma)=\frac{(\gamma+1)(\gamma+2)^2(\gamma+3)}6
\]
for every Dixmier trace \(\operatorname{Tr}_\omega\). It lies in \(\mathcal S_p\) precisely when \(p>1\). At \(\gamma=1\), the first coefficient is exactly \(12\) and the second is \(-144^{2/3}/6\). The logarithmic second term is nonzero for every fixed \(\gamma>0\).

## Assumptions and scope
The domain is the complex \(2\times2\) matrix ball (Cartan type \(I_{2,2}\)), not the ordinary complex four-ball. The determinant has the holomorphic branch fixed by its convergent power series at \(Z=0\); positivity and the spectral representation below give the bounded extension of the integral operator. The weight exponent satisfies \(\gamma>0\), the kernel exponent is exactly \(\gamma+1\), and the operator is studied on the indicated Hilbert space. All asymptotics hold for fixed \(\gamma\), not uniformly as \(\gamma\downarrow0\). The operator vanishes on the orthogonal complement of the holomorphic weighted Bergman subspace. Singular values are arranged in nonincreasing order, with repetitions.

## Proof
**Step 1: exact spectral reduction.** Under the action of \(U(2)\times U(2)\), the holomorphic polynomial subspace decomposes orthogonally into irreducible types indexed by \((m,n)\) with integers \(m\ge n\ge0\). The representation is \(S_{(m,n)}(\mathbb C^2)\otimes S_{(m,n)}(\mathbb C^2)^*\), of dimension \((m-n+1)^2\) (Weyl's two-row dimension formula). The Faraut–Korányi expansion and the normalized weighted Bergman reproducing kernel identify the scalar of the integral operator on this type as
\[
\lambda_{m,n}=\frac{(\gamma+1)_m(\gamma)_n}{(\gamma+4)_m(\gamma+3)_n}=a_m b_n,
\]
where \((q)_k=q(q+1)\cdots(q+k-1)\), with \((q)_0=1\), and
\[
a_m=\frac{A_\gamma}{(m+\gamma+1)(m+\gamma+2)(m+\gamma+3)},\qquad
b_n=\frac{B_\gamma}{(n+\gamma)(n+\gamma+1)(n+\gamma+2)}.
\]
All scalars are positive, bounded by one, and tend to zero off any finite set of types; the resulting operator is positive and compact. These spectral factors follow in particular from the published general eigenvalue formula in Ding (2020), Section 3, specialized to genus four, root multiplicity two, and weighted parameter \(\gamma\). Their multiplicities can also be verified directly by the \(U(2)\times U(2)\) representation. Hence the exact integer counting formula is
\[
N_\gamma(\tau)=\sum_{n=0}^\infty\sum_{m=n}^\infty(m-n+1)^2\mathbf1_{\{a_m b_n>\tau\}}.
\]

**Step 2: a uniform cutoff reduction.** Set \(x=\tau^{-1/3}\), \(h_n=(A_\gamma b_n)^{1/3}\). Since
\[
a_m=\frac{A_\gamma}{(m+\gamma+2)^3-(m+\gamma+2)},
\]
the largest admissible \(m\), whenever one exists, is \(x h_n+O_\gamma(1)\), uniformly in \(n\). Indeed the positive root of \(y^3-y=(xh_n)^3\), at \(y\ge\gamma+2>2\), differs from \(xh_n\) by a uniformly bounded quantity, and passage to an integer cutoff adds at most one. The active \(n\)'s are precisely an initial interval, because \(a_n b_n\) decreases strictly, and its final index is \(O_\gamma(x^{1/2})\), as \(a_n b_n\sim A_\gamma B_\gamma n^{-6}\). Summing successive squares and using the cutoff error gives
\[
N_\gamma(\tau)=\frac13\sum_{n\ge0}(xh_n-n)_+^3+O_\gamma(x^2).
\]
Here the per-index replacement error is bounded by \(C_\gamma((xh_n)^2+1)\) for relevant indices; its sum is \(O_\gamma(x^2)\), because \(\sum_n h_n^2<\infty\) and only \(O_\gamma(x^{1/2})\) indices contribute. Near the endpoint, where the positive-part and exact cutoff disagree, \(xh_n-n\) remains bounded and contributes no larger error.

**Step 3: logarithmic interaction of the partition coordinates.** Let \(Q(x)\) be the greatest integer \(n\ge0\) with \(xh_n>n\). Since \(b_n=B_\gamma n^{-3}(1+O_\gamma(n^{-1}))\),
\[
Q(x)=(A_\gamma B_\gamma)^{1/6}x^{1/2}+O_\gamma(1).
\]
Expand the cubic positive part for \(0\le n\le Q(x)\):
\[
\frac13\sum_{n\le Q}(xh_n-n)^3
=\frac{x^3}3\sum_{n\le Q}h_n^3
-x^2\sum_{n\le Q}nh_n^2
+x\sum_{n\le Q}n^2h_n-\frac13\sum_{n\le Q}n^3.
\]
The last two terms are \(O_\gamma(x^2)\), because \(h_n=O_\gamma((n+1)^{-1})\) and \(Q=O_\gamma(x^{1/2})\). The omitted tail of \(\sum h_n^3\) contributes \(x^3O_\gamma(Q^{-2})=O_\gamma(x^2)\). The exact moment sum is
\[
\sum_{n=0}^\infty b_n=\frac{\gamma+2}{2}.
\]
One way to verify it is to use the beta-integral formula \(b_n=\frac{B_\gamma}{2}\int_0^1u^{n+\gamma-1}(1-u)^2\,du\), sum the geometric series under the integral, and evaluate the remaining beta integral. Therefore the cubic main term equals \(A_\gamma(\gamma+2)x^3/6\). Finally,
\[
nh_n^2=\frac{(A_\gamma B_\gamma)^{2/3}}n+O_\gamma(n^{-2}),\qquad
\sum_{n\le Q}nh_n^2=\frac{(A_\gamma B_\gamma)^{2/3}}2\log x+O_\gamma(1).
\]
Thus
\[
N_\gamma(\tau)=\frac{A_\gamma(\gamma+2)}6x^3
-\frac{(A_\gamma B_\gamma)^{2/3}}2x^2\log x+O_\gamma(x^2).
\]
Substitution of \(x=\tau^{-1/3}\) proves both coefficients and the claimed remainder. The logarithm comes specifically from the borderline harmonic sum over the *second* partition coordinate; it is not the leading one-row spectral law.

**Step 4: consequences.** The leading term \(N_\gamma(\tau)\sim C_\gamma/\tau\), with \(C_\gamma=A_\gamma(\gamma+2)/6>0\), implies by monotone inversion \(s_j(T_\gamma)\sim C_\gamma/j\). It follows that \(T_\gamma\in\mathcal S_p\) exactly for \(p>1\), and partial sums of singular values are \(C_\gamma\log J+o(\log J)\). Since this ordinary logarithmic mean converges, every Dixmier trace has the same stated value. The positive second coefficient is subtracted, so its sign is strictly negative.

## Verification
The accompanying Python 3 program `verify_count.py` computes the exact integer counting function using rational arithmetic for rational \(\gamma\) and rational thresholds. It independently compares its binary-search count with direct enumeration at small scales, then reports scaled discrepancies from the proved two-term expansion for \(\gamma=1/2,1,2\). The checks verify arithmetic and implementation consistency, not the infinite asymptotics. The analytical derivation above is the certificate of the infinite statement.

## Relationship to prior work
Ding (2020, arXiv:2009.09613), Section 3, supplies the exact general partition-indexed characteristic and the sharp Schatten-membership criterion for bounded symmetric domains, including type \(I_{2,2}\). The present result *uses* those exact eigenvalues and does not claim them as new. Its additional claim is the **ordered spectral counting function with a sharp second Weyl term of order \(\tau^{-2/3}\log(1/\tau)\)** and the explicit rank-two weak-trace coefficient along the full positive critical-weight curve. Ding and Fan (2020, arXiv:2004.13635) compute Dixmier traces on ordinary rank-one complex balls; that geometry is not the rank-two matrix ball here. Upmeier and Wang (2015, arXiv:1508.04710) treat sub-Toeplitz commutators on quotient modules of symmetric domains, not this positive determinant-kernel integral operator. Upmeier (2021) derives eigenvalues for different K-invariant Toeplitz operators, not the claimed two-term counting law. No comparison proves universal historical priority; unindexed literature on matrix-ball spectral zeta functions remains a specific risk.

## Limitations
The normalization of \(d\nu_\gamma\) as a probability measure is essential for the constants. The theorem is for fixed \(\gamma>0\), not uniform near \(\gamma=0\), where a representation-theoretic degeneration changes the rank structure. The remainder \(O_\gamma(\tau^{-2/3})\) does not identify its bounded oscillations or a third Weyl coefficient. All claims are analytic; no numerical finite test has been extrapolated into a proof.

## References
1. L. Ding, *Schatten class Bergman-type and Szegő-type operators on bounded symmetric domains*, arXiv:2009.09613, first posted 21 September 2020, especially Sections 2–4 and the spectral characteristic formula. https://arxiv.org/abs/2009.09613
2. L. Ding and J. Fan, *On the compactness of Bergman-type integral operators*, arXiv:2004.13635, first posted 28 April 2020, Section 4 on unit-ball Macaev ideals and Dixmier traces. https://arxiv.org/abs/2004.13635
3. H. Upmeier and K. Wang, *Dixmier trace for Toeplitz operators on symmetric domains*, arXiv:1508.04710, first posted 19 August 2015. https://arxiv.org/abs/1508.04710
4. H. Upmeier, *Eigenvalues of K-invariant Toeplitz operators on bounded symmetric domains*, Integral Equations and Operator Theory 93 (2021), article 27. https://doi.org/10.1007/s00020-021-02639-3
