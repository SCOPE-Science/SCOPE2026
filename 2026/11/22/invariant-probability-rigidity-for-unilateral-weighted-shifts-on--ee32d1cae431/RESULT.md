# Invariant-probability rigidity for unilateral weighted shifts on \(c_0\)

## Finding
Let \(\mathbb K\) be \(\mathbb R\) or \(\mathbb C\), and write \(c_0=c_0(\mathbb N_0;\mathbb K)\). Given any bounded sequence of nonzero weights \((w_n)_{n\ge1}\), define the backward weighted shift
\[
(B_wx)_n=w_{n+1}x_{n+1}\quad(n\ge0),\qquad P_0=1,\quad P_n=\prod_{k=1}^{n}w_k.
\]
Then the following assertions are equivalent:

1. There is a Borel probability \(\mu\ne\delta_0\) on \(c_0\) invariant under \(B_w\).
2. \(|P_n|\to\infty\) as \(n\to\infty\).
3. \(B_w\) has a nonzero fixed vector in \(c_0\).
4. There is a **nonatomic, compactly supported, strongly mixing** invariant Borel probability on \(c_0\).

Consequently, if \(|P_n|\) fails to tend to infinity, \(\delta_0\) is the **unique** invariant Borel probability. The necessity direction makes no assumptions of ergodicity, independence of coordinates, or finite moments. In view of the classical topological-mixing criterion for these shifts, the existence of *any* nontrivial invariant Borel probability coincides with topological mixing; this identification does not say that the invariant measure has full support.

## Assumptions and scope
Here \(c_0\) consists of scalar sequences converging to zero, with the supremum norm. Each \(w_n\ne0\); the sequence is uniformly bounded above, ensuring that \(B_w\) is a bounded operator. No positive lower bound on individual weights is required. A probability is *nontrivial* when it differs from \(\delta_0\), and a probability-preserving dynamical system is *strongly mixing* when
\[
\lim_{n\to\infty}\mu(A\cap B_w^{-n}C)=\mu(A)\mu(C)
\]
for all Borel sets \(A,C\subseteq c_0\). The claim concerns the one-sided shift only, not arbitrary bilateral or operator-valued shifts.

## Proof
**1. A necessary coordinate-rigidity principle.** Let \(X=(X_n)_{n\ge0}\) be a \(c_0\)-valued random vector with \(B_w\)-invariant Borel law \(\mu\). For each \(n\ge0\), invariance under \(B_w^n\) and the exact coefficient identity give
\[
P_nX_n=(B_w^nX)_0\overset{d}{=}X_0.
\]
If \(|P_n|\not\to\infty\), there is a strictly increasing sequence \((n_j)\) and a finite \(M\) with \(|P_{n_j}|\le M\) for all \(j\). Since every realization \(X\) lies in \(c_0\), we have \(X_{n_j}\to0\) almost surely. Thus \(P_{n_j}X_{n_j}\to0\) almost surely. The variables \(P_{n_j}X_{n_j}\) all have the same distribution as \(X_0\), hence \(X_0=0\) almost surely. The same distributional identity and \(P_n\ne0\) now imply \(X_n=0\) almost surely for each fixed \(n\). Intersecting the countably many probability-one events yields \(X=0\) almost surely, or \(\mu=\delta_0\). This proves the contrapositive of (1) implies (2) and uniqueness when (2) fails.

**2. Fixed points.** The fixed-point equations \(w_{n+1}x_{n+1}=x_n\) give exactly \(x_n=x_0/P_n\) for all \(n\ge0\). Hence a nonzero fixed point belongs to \(c_0\) if and only if \(|P_n|\to\infty\). If that condition holds, \(v=(P_n^{-1})_{n\ge0}\) is a nonzero fixed point and \(\delta_v\) is an invariant Borel probability. This proves the equivalence of (2) and (3), together with (3) implies (1).

**3. Compact Bernoulli coding and strong mixing.** Suppose (2). Take \(D=[-1,1]\) in the real case and the closed unit disk \(D=\{z\in\mathbb C:|z|\le1\}\) in the complex case. Equip \(D\) with a nonatomic probability \(\lambda\) of full support, e.g. normalized length or area measure, respectively. Let \(\Omega=D^{\mathbb N_0}\) with the product topology and Bernoulli product probability \(\nu=\lambda^{\otimes\mathbb N_0}\), and let \(\sigma(u_0,u_1,\ldots)=(u_1,u_2,\ldots)\).
Define
\[
\Phi:\Omega\longrightarrow c_0,\qquad \Phi(u)_n=P_n^{-1}u_n.
\]
Because \(\sup_{n>N}|P_n|^{-1}\to0\), the finite-coordinate truncations of \(\Phi\) converge uniformly on \(\Omega\); therefore \(\Phi\) is continuous for the product topology. Since every \(P_n\ne0\), it is injective, and its image \(K\) is compact. The exact identity
\[
(B_w\Phi(u))_n=w_{n+1}P_{n+1}^{-1}u_{n+1}=P_n^{-1}u_{n+1}=(\Phi\sigma(u))_n
\]
shows \(B_w\circ\Phi=\Phi\circ\sigma\). Thus \(\mu=\Phi_*\nu\) is an invariant probability supported on \(K\). It is nonatomic because its zeroth-coordinate marginal is \(\lambda\). For cylinder events in \(\Omega\), the independence of disjoint coordinate blocks gives \(\nu(A\cap\sigma^{-n}C)=\nu(A)\nu(C)\) for all sufficiently large \(n\); a monotone-class argument extends this to all Borel events. Hence \((\Omega,\nu,\sigma)\) is strongly mixing, and so is its continuous, measurable isomorphic copy \((K,\mu,B_w|_K)\), proving (4). Obviously (4) implies (1). All equivalences follow.

**Illustrative boundary.** The bounded positive weights \(w_n=(n+1)/n\) satisfy \(P_n=n+1\), so nontrivial compactly supported mixing invariant laws exist. Conversely, concatenate for each \(k\ge1\) a block of \(k\) weights \(2\) followed by \(k\) weights \(1/2\). The cumulative products return to \(1\) after every block but reach \(2^k\) midway. This shift is hypercyclic by the standard unbounded-limsup criterion, yet by the theorem its *only* invariant Borel probability is \(\delta_0\). These examples distinguish pointwise divergence from mere unboundedness.

## Verification
The proof rests on three exact, independently checkable identities: \((B_w^nx)_0=P_nx_n\), \(B_w(P_n^{-1})=(P_n^{-1})\), and \(B_w\Phi=\Phi\sigma\). The first gives a fully infinite-dimensional measure-theoretic contradiction using almost-sure coordinate decay, not a finite approximation; the second and third are exact algebraic identities. A standalone standard-library checker included as `checks/verify_examples.py` verifies the prefix identities and coding over finite prefixes for two admissible weight families and the return/spike behavior of the alternating-block boundary example. Its finite tests are illustrative only and are **not** substituted for the proofs of the limiting, measure-theoretic, or mixing assertions.

## Relationship to prior work
Grivaux, Matheron, and Menet [1, §§2 and 7] characterize nontrivial invariant measures on \(\ell_p\) for finite \(p\) and explicitly pose the \(c_0\) version as Question 7.7. Their Proposition 6.6(c) treats a necessary condition **only for invariant product measures** on a full coordinate product. The present theorem proves that condition for *every* invariant Borel probability carried by \(c_0\), with no product, ergodicity or moment hypotheses. Their fixed-point construction already supplies the easy sufficiency mechanism on suitable sequence spaces; novelty is specifically assessed for the unrestricted necessity and complete \(c_0\) equivalence. The author-hosted manuscript [2, p. 35] still states Question 7.7. Menet and Papathanasiou [3] classify mixing and chaos for related shifts but do not formulate a characterization of arbitrary invariant Borel probabilities on \(c_0\). Known topological-mixing characterizations imply a consequence of the theorem, not its unrestricted measure-theoretic converse.

## Limitations
The construction produces mixing measures with **compact support**, not necessarily full support in \(c_0\). A statement about arbitrary invariant measures is established only for one-sided scalar weighted shifts with nonzero bounded weights. No rate of mixing for arbitrary Borel sets, classification of all invariant measures, or statement about nonlinear/operator-valued/bilateral shifts is asserted. A published historical-priority claim has not been independently certified; unindexed later results could affect originality. The argument is mathematically complete as written but has not undergone independent validation.

## References
[1] S. Grivaux, É. Matheron and Q. Menet, *Orthogonality of invariant measures for weighted shifts*, arXiv:2312.13920v1 (first public posting 21 December 2023), especially Proposition 2.1, Remark 2.3, Proposition 6.6(c) and Question 7.7. https://arxiv.org/html/2312.13920v1

[2] S. Grivaux, É. Matheron and Q. Menet, *Orthogonality of invariant measures for weighted shifts*, author-hosted full-text manuscript, p. 35. https://matheron.perso.math.cnrs.fr/recherche_fichiers/PetitMachin.pdf

[3] Q. Menet and D. Papathanasiou, *Dynamics of weighted shifts on \(\ell^p\)-sums and \(c_0\)-sums*, arXiv:2408.11153v1 (20 August 2024). https://arxiv.org/html/2408.11153v1
