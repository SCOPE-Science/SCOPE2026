# Sharp uniform Koszul conditioning and essential-spectrum collapse for normal row tuples

## Finding
Let \(H\ne\{0\}\) be a complex Hilbert space and \(T=(T_j)_{j\ge1}\) a pairwise commuting family of bounded **normal** operators. Assume the row bound
\[
C_T:=\sup_{n\ge1}\left\|\sum_{j=1}^{n}T_jT_j^*\right\|<\infty.
\]
Let \(E_T\) be its joint projection-valued spectral measure on \(\ell^2\), and let \(K_T\) be its **norm-topological support**, i.e. \(\lambda\in K_T\) exactly when \(E_T(B_{\ell^2}(\lambda,r))\ne0\) for all \(r>0\). Then \(K_T\) is a nonempty bounded closed set, and in the infinite-exterior Taylor-type definitions of Wang–Zhang–Zhang–Zhu,
\[
\boxed{\sigma(T)=\sigma_e(T)=K_T.}
\]
For any \(\lambda\notin K_T\), define \(L_T(\lambda)\) as the infimum of \(c\ge0\) such that **for every degree \(k\ge0\)** and every cycle \(x\in\ker\partial_{T-\lambda,k}\), there is \(y\) one degree higher with \(\partial_{T-\lambda,k+1}y=x\) and \(\|y\|\le c\|x\|\). The exact optimal uniform Koszul lifting constant is
\[
\boxed{L_T(\lambda)=\frac1{\operatorname{dist}(\lambda,K_T)}.}
\]
For two such commuting-normal row-bounded families \(T,S\) acting on the same \(H\), set
\[
\Delta(T,S)=\left\|\left(\sum_{j\ge1}(T_j-S_j)^*(T_j-S_j)\right)^{1/2}\right\|.
\]
The sum is a bounded strong monotone limit. Their spectra obey the **sharp** perturbation bound
\[
\boxed{d_H(K_T,K_S)\le\Delta(T,S).}
\]
The coefficient one is attained by one-dimensional scalar tuples. These statements form an exact spectral-and-conditioning theorem for the normal class, including noncompact joint spectra.

## Assumptions and scope
Here \(\Lambda^k=\bigwedge^k\ell^2\), \(\Lambda^0=\mathbb C\), and \(\partial_{T-\lambda,k}:H\otimes\Lambda^k\to H\otimes\Lambda^{k-1}\) is the bounded Koszul differential \(\sum_{j\ge1}(T_j-\lambda_jI)\otimes E_{j,k}^*\) (strong operator limit). The Fredholm definition permits finite-dimensional homology in only finitely many degrees and requires uniform lifting in all remaining degrees, as in arXiv:2610.41882v1, Definitions 1.1 and 1.12. No norm convergence of the full operator series is assumed. The relevant topology on \(\ell^2\) is its **norm topology**, not the product topology used for some older infinite joint spectra. The Hausdorff distance is taken between bounded nonempty closed sets, which need not be compact.

## Proof
**Spectral measure and Laplacian.** Since the normal operators commute, Fuglede's theorem makes their generated von Neumann algebra abelian. The joint spectral representation has coordinates \(z_j\), with \(\sum_j|z_j|^2\le C_T\) almost everywhere. The associated spectral measure is therefore concentrated on a bounded subset of \(\ell^2\). For \(\lambda\in\ell^2\), define the bounded positive operator
\[
B_\lambda=\operatorname{SOT}\!\sum_{j\ge1}(T_j-\lambda_j I)^*(T_j-\lambda_j I)
=\int_{\ell^2}\|z-\lambda\|_2^2\,dE_T(z).
\]
Consequently \(\inf\sigma(B_\lambda)=\operatorname{dist}(\lambda,K_T)^2\). Put \(d=\partial_{T-\lambda}\) on the full antisymmetric Fock space. Canonical anticommutation and the normal commutation relations give, on **every** degree,
\[
\boxed{dd^*+d^*d=B_\lambda\otimes I_\Lambda.}\tag{1}
\]
The identity extends by strong limits from the finite-coordinate identities because the row bound makes \(d\) bounded (as in the source's Lemma 2.12).

**Outside the support: exact lifting.** For \(\lambda\notin K_T\), write \(\delta=\operatorname{dist}(\lambda,K_T)>0\), so \(B_\lambda\ge\delta^2 I\). It commutes with \(d,d^*\). For any cycle \(x\) in degree \(k\), set \(y=(B_\lambda^{-1}\otimes I)d_{k+1}^*x\). Equation (1) gives \(d_{k+1}y=x\), while
\[
\|y\|^2=\langle(B_\lambda^{-1}\otimes I)x,x\rangle\le\delta^{-2}\|x\|^2.
\]
This proves invertibility in the *uniform* infinite-degree definition. The bound is optimal already in degree zero: \(d_1d_1^*=B_\lambda\), hence the unique minimum-norm preimage of \(x\in H\) is \(d_1^*B_\lambda^{-1}x\). Its operator norm is \(\|B_\lambda^{-1/2}\|=\delta^{-1}\). Therefore \(L_T(\lambda)=\delta^{-1}\).

**On the support: failure of Fredholmness.** If \(\lambda\in K_T\), then \(0\in\sigma(B_\lambda)\). If \(\ker B_\lambda\ne0\), every subspace \(\ker B_\lambda\otimes\Lambda^k\) consists of harmonic cycles (annihilated by \(d\) and \(d^*\)); it injects into degree-\(k\) homology. Since \(\Lambda^k\) is infinite-dimensional for every \(k\ge1\), the homologies are infinite-dimensional and the tuple cannot be Fredholm. If \(\ker B_\lambda=0\), then \(d_1^*\) is injective but not bounded below because \(d_1d_1^*=B_\lambda\) has spectral infimum zero. Therefore \(\operatorname{ran}d_1\) is dense but nonclosed. A bounded operator range of finite algebraic codimension must be closed: if its quotient were finite-dimensional, adding any finite-dimensional algebraic complement would yield a bounded surjection, and the open mapping theorem would make the complement projection continuous. Hence the degree-zero homology \(H/\operatorname{ran}d_1\) is infinite-dimensional, contradicting Fredholmness. Thus every \(\lambda\in K_T\) lies in \(\sigma_e(T)\), proving equality of the three sets.

**Sharp perturbation bound.** Every \(\lambda\in K_T\) admits unit vectors \(x_n\in H\) with \(\sum_j\|(T_j-\lambda_jI)x_n\|^2\to0\), by the spectral measure in an arbitrarily small ball around \(\lambda\). Hilbert-space triangle inequality gives
\[
\left(\sum_j\|(S_j-\lambda_jI)x_n\|^2\right)^{1/2}
\le \left(\sum_j\|(T_j-\lambda_jI)x_n\|^2\right)^{1/2}+\Delta(T,S).
\]
The left-hand side is at least \(\operatorname{dist}(\lambda,K_S)\) by the joint spectral theorem for \(S\). Passing to the limit and then exchanging \(S,T\) proves the Hausdorff estimate. For \(H=\mathbb C\), take the zero tuple and a tuple with a single scalar coordinate \(a\ne0\); equality holds.

**Noncompact witness.** On \(H=\ell^2\) let \(T_j\) be the rank-one orthogonal projection onto the \(j\)-th coordinate. Then \(\sum_jT_jT_j^*=I\) strongly, but not in operator norm; the Koszul partial sums are not norm-Cauchy by the finite-tail CAR identity. The joint spectral measure has atoms at the vectors \(e_j\in\ell^2\), so
\[
\sigma(T)=\sigma_e(T)=\{e_j:j\ge1\},
\]
a bounded, norm-closed, noncompact subset of \(\ell^2\). The finite-variable Fredholm analogue is different: the infinitely many exterior degrees are essential to the collapse at even an isolated finite-multiplicity eigenvalue.

## Verification
The proofs of the CAR identity, the optimal degree-zero lower bound, the nonclosed-range alternative and the perturbation estimate cover all infinite-dimensional and noncompact cases analytically; no finite enumeration is used as an infinite proof. A standalone finite-fermionic-matrix checker, included as `CHECKER.py`, tests the CAR identity, nilpotence and optimal degree-zero lifting for several normal diagonal tuples. Execute with `python CHECKER.py` where NumPy is installed. The checker only tests finite instances and is not a substitute for the proof.

## Relationship to prior work
Wang–Zhang–Zhang–Zhu (arXiv:2610.41882v1) introduced the infinite-exterior definitions and proved the normal CAR identity (Lemma 2.12), normal joint-spectrum criterion (Lemma 3.10), and spectral–essential-spectral equality **under the stronger norm-convergence assumption** (Theorem 1.14). Their Remarks 3.12 and 5.5 construct arbitrary bounded closed spectral and essential-spectral sets in special diagonal models. These established ingredients and examples are credited here. The present theorem combines exact uniform conditioning, *unconditional normal-class* Fredholm collapse, and sharp metric perturbation control in a single statement, including normal examples outside the norm-convergence scope. Finite-variable Taylor–Fredholm theory and the older product-topology infinite joint spectrum do not assert this infinite-degree normal classification. All priority comparisons are best-knowledge rather than independent publication certification.

## Limitations
The result is confined to countable commuting **normal** row-bounded sequences on a complex Hilbert space and to the named infinite-exterior spectral/Fredholm definitions. For general nonnormal commuting tuples, the CAR scalar Laplacian fails and the essential spectrum may be strictly smaller than the full spectrum. The sharp perturbation metric is the **column norm of the difference tuple**, not the maximum of individual coordinate norms or product-topology convergence. The ingredients are elementary once the source's infinite Koszul framework is available; an older equivalent general theorem remains a priority risk. The finite checker cannot certify statements for infinitely many degrees.

## References
1. Penghui Wang, Fan Zhang, Ruoyu Zhang, Zeyou Zhu, *Taylor-type joint spectrum and essential spectrum of row-bounded sequences of commuting operators*, arXiv:2610.41882v1, first posted 2026-10-30, https://arxiv.org/html/2610.41882v1 (Definitions 1.1, 1.12; Theorem 1.14; Lemmas 2.12, 3.10; Remark 5.5).
2. J. L. Taylor, *A joint spectrum for several commuting operators*, Journal of Functional Analysis 6 (1970), 172–191 (finite-variable background; bibliographic reference via item 1).
3. Z. Słodkowski and W. Żelazko, *On joint spectra of commuting families of operators*, Studia Mathematica 50 (1974), 127–148 (older product-topology definition; bibliographic reference via item 1).
