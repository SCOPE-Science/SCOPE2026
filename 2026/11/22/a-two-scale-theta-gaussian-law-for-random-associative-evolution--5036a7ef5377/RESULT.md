# A two-scale theta–Gaussian law for random associative evolution algebras

## Finding
Fix a prime power \(q\ge 2\). Choose uniformly among all \(n\times n\) matrices \(A=(a_{ij})\) over \(\mathbb F_q\) for which the evolution algebra with a specified natural basis \(e_1,\ldots,e_n\), multiplication \(e_i e_j=0\) for \(i\ne j\), and \(e_i^2=\sum_j a_{ij}e_j\), is associative. These are **labelled, natural-basis presentations**; no quotient by algebra isomorphism is taken.

Let \(S_n=n-\dim\operatorname{Ann}(E_A)\) and let \(T_n\) be the dimension of the semisimple summand in the canonical associative-algebra decomposition \(E_A\simeq \mathbb F_q^{T_n}\oplus N\) with \(N^3=0\). For integers \(0\le t\le s\le n\), the exact joint number of matrices with \(S_n=s\), \(T_n=t\) is
\[
N_{n,q}(s,t)=\binom ns\binom st\big((q-1)q^{n-s}\big)^t\big(q^{n-s}-1\big)^{s-t}.
\]
In particular the total number is
\[
A_n(q)=\sum_{s=0}^{n}\binom ns\big(q^{n-s+1}-1\big)^s.
\]

Put \(m=\lceil n/2\rceil\), \(p=(q-1)/q\), and
\[
J_n=S_n-m,\qquad Z_n=\frac{T_n-pm}{\sqrt{mp(1-p)}}.
\]
Along odd dimensions \(n=2m-1\), \((J_n,Z_n)\) converges jointly to **independent** variables \((J_{\mathrm o},G)\), where \(G\sim\mathcal N(0,1)\) and
\[
\Pr(J_{\mathrm o}=j)=\frac{q^{-j^2}}{\Theta_{\mathrm o}(q)},\qquad
\Theta_{\mathrm o}(q)=\sum_{k\in\mathbb Z}q^{-k^2}.
\]
Along even dimensions \(n=2m\), the same holds with \(J_{\mathrm e}\), where
\[
\Pr(J_{\mathrm e}=j)=\frac{q^{-j(j-1)}}{\Theta_{\mathrm e}(q)},\qquad
\Theta_{\mathrm e}(q)=\sum_{k\in\mathbb Z}q^{-k(k-1)}.
\]
Consequently the annihilator dimension has only bounded, parity-dependent fluctuations around \(n-m\), while the semisimple dimension has Gaussian fluctuations of order \(\sqrt n\). The precise total-count asymptotics, for fixed \(q\), are
\[
A_{2m-1}(q)\sim\binom{2m-1}{m}q^{m^2}\Theta_{\mathrm o}(q),\qquad
A_{2m}(q)\sim\binom{2m}{m}q^{m(m+1)}\Theta_{\mathrm e}(q).
\]

## Assumptions and scope
The field size \(q\) is fixed as \(n\to\infty\), but may be any prime power, including even characteristic. The only randomization is uniform choice of a labelled associative structure matrix relative to a *fixed* natural basis. The integer \(S_n\) is the number of nonzero rows of \(A\), since \(\operatorname{Ann}(E_A)\) is spanned by the basis elements having zero square. The integer \(T_n\) is the number of nonzero diagonal entries of \(A\); its intrinsic interpretation is justified below. The count formulas use the standard empty-product convention \(0^0=1\) when a multiplicity exponent is zero. The limiting claims are weak joint convergence, including asymptotic independence, not finite-\(n\) independence. We do not enumerate isomorphism types.

## Proof
**1. Associativity and the intrinsic invariants.** For \(i\ne j\), associativity on the triple \((e_i,e_i,e_j)\) requires \(a_{ij}e_j^2=0\). Conversely, those conditions imply associativity on all basis triples by bilinearity. Thus whenever row \(j\) is nonzero, all off-diagonal entries \(a_{ij}\) with \(i\ne j\) vanish. Write \(S\subseteq\{1,\ldots,n\}\) for the set of nonzero rows, \(|S|=s\). Rows outside \(S\) are zero. Each row \(i\in S\) is any nonzero vector supported on \(\{i\}\cup S^c\), a vector space of dimension \(n-s+1\). These observations are compatible with and already structurally implicit in the published general normal form of Fernández Ternero, Gómez Sousa and Núñez-Valdés, Theorem 3.1 (2023); that normal form is **not claimed as new**.

The annihilator identity follows immediately from \(xe_i=x_i e_i^2\), and so \(S_n=s\). Write \(a_i=a_{ii}\). Modulo the annihilator, the active classes satisfy \(\overline e_i^2=a_i\overline e_i\) and all mixed products vanish. Those with \(a_i\ne0\) give \(\mathbb F_q\)-field factors after rescaling; those with \(a_i=0\) belong to the nilpotent radical. More explicitly, for \(a_i\ne0\), the element \(f_i=a_i^{-2}e_i^2\) is an idempotent, these \(f_i\) are pairwise orthogonal, and \(e_i-a_if_i\) annihilates the whole algebra. The remaining active classes have squares in the annihilator. Hence \(E_A\cong\mathbb F_q^t\oplus N\), with \(t=|\{i:a_{ii}\ne0\}|\) and \(N^3=0\), establishing the claimed basis-independent meaning of \(T_n\).

**2. Exact joint census.** Choose the \(s\) active rows in \(\binom ns\) ways and the \(t\) with nonzero diagonal entries in \(\binom st\) ways. An active row with nonzero diagonal has \((q-1)q^{n-s}\) choices; an active row with zero diagonal has \(q^{n-s}-1\) choices. Choices are independent across rows, proving the stated exact joint formula. Summing over \(t\) yields \(\binom ns(q^{n-s+1}-1)^s\), then summing over \(s\) gives \(A_n(q)\).

**3. Theta pinning of the annihilator dimension.** Let \(W_{n,s}=\binom ns(q^{n-s+1}-1)^s\). For \(n=2m-1\) and \(s=m+j\), factoring out \(\binom{2m-1}{m}q^{m^2}\) gives
\[
\frac{W_{2m-1,m+j}}{\binom{2m-1}{m}q^{m^2}}=
\frac{\binom{2m-1}{m+j}}{\binom{2m-1}{m}}
q^{-j^2}\big(1-q^{-(m-j)}\big)^{m+j}.
\]
For each fixed integer \(j\), the binomial ratio and final factor tend to one. Every term is bounded by \(q^{-j^2}\), independently of \(m\). The summable majorant permits dominated convergence over \(j\in\mathbb Z\). This proves the odd total asymptotic, the odd lattice law and tightness of \(J_n\). For \(n=2m\) the analogous factorization is
\[
\frac{W_{2m,m+j}}{\binom{2m}{m}q^{m(m+1)}}=
\frac{\binom{2m}{m+j}}{\binom{2m}{m}}
q^{-j(j-1)}\big(1-q^{-(m-j+1)}\big)^{m+j}.
\]
The summable majorant is \(q^{-j(j-1)}\). Dominated convergence proves the even asymptotic and even lattice law. Both majorants are summable for every \(q\ge2\).

**4. Gaussian scale and asymptotic independence.** Conditional on \(S_n=s\), the active rows are independent uniformly random nonzero vectors in \(\mathbb F_q^{n-s+1}\). Consequently
\[
T_n\mid(S_n=s)\sim\operatorname{Bin}\left(s,p_{n,s}\right),\qquad
p_{n,s}=\frac{(q-1)q^{n-s}}{q^{n-s+1}-1}.
\]
For every fixed \(j\), when \(s=m+j\) and \(m\to\infty\), we have \(s/m\to1\) and \(p_{n,s}=p+O_q(q^{-m+|j|})\). The binomial central limit theorem, together with negligible differences of centering and variance after the stated normalization, gives \(Z_n\mid(J_n=j)\Rightarrow\mathcal N(0,1)\). For any finite set of integer \(j\)'s this convergence is joint with their limiting theta probabilities. The already established tightness of \(J_n\) controls the discarded tails and proves convergence to the product of the theta lattice law and the standard Gaussian. Thus the limits are independent.

## Verification
The self-contained script `verify.py` enumerates all labelled structure matrices over \(\mathbb F_2\) through dimension four, over \(\mathbb F_3\) through dimension three, and uses the zero/nonzero support criterion over an abstract four-element field in dimension two. It checks associativity by *all basis triples* independently of the support rule for the prime-field cases, checks the exact joint counts \(N_{n,q}(s,t)\), and checks the coordinate component supports for dimensions one through seven. Its output is embedded as `verification_output.txt`; the final line is `VERIFY_OK`. These are finite checks, **not** a substitute for the infinite proof above.

## Relationship to prior work
Fernández Ternero, Gómez Sousa and Núñez-Valdés, *A Characterization of Associative Evolution Algebras* (2023), Theorem 3.1, explicitly establish the block normal form for all associative evolution algebras, and Proposition 3.2 establishes the semisimple-plus-cube-zero decomposition. Both are credited as prior work. The new statistical statement concerns the exact labelled joint distribution of **two intrinsic algebra dimensions**, its parity-dependent theta local limit, and a simultaneous independent Gaussian limit; none is asserted by that source. The 2026 survey by Kaygorodov, Martín González and Viruel motivates renewed study of evolution-algebra structure and moduli but is not credited with a quantitative claim. Previously published work on general finite-field evolution algebras concerns different sampling ensembles, generally without conditioning on associativity. The transition from a normal form to the joint limit requires the exact support-stratified count and two-scale asymptotic argument above.

## Limitations
The underlying normal form and abstract decomposition are published and are **not original contributions here**. The novelty assessment concerns only the explicit joint random-model theorem and its limiting distributions; previously unnoticed count tables or asymptotic equivalents remain a historical-priority risk. Sampling is by labelled natural-basis structure matrices, **not** by isomorphism classes. The theorem fixes \(q\) before taking \(n\to\infty\), and does not establish uniformity when \(q\) grows with \(n\). This is a statistical theorem for labelled presentations, and it does not provide a classification of isomorphism types.

## References
1. D. Fernández Ternero, V. M. Gómez Sousa, J. Núñez-Valdés, *A Characterization of Associative Evolution Algebras*, Contemporary Mathematics 4(1) (2023), 42–48, DOI: https://doi.org/10.37256/cm.4120232167 . Public full text: https://www.researchgate.net/publication/368609732_A_Characterization_of_Associative_Evolution_Algebras .
2. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248, first publicly posted 2026-10-15, https://arxiv.org/abs/2610.22248 .
3. R. M. Falcón and collaborators, *Classification of asexual diploid organisms by means of strongly isotopic evolution algebras defined over any field*, Journal of Algebra (2017), DOI: https://doi.org/10.1016/j.jalgebra.2016.11.018 . Earlier general annihilator strata, not the associativity-conditioned joint limit.
