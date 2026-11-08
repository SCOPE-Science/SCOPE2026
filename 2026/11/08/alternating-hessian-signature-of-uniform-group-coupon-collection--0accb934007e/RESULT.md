# Alternating Hessian signature of uniform group coupon collection

## Finding
Let \(n\ge 3\) and \(1\le s<n\) be integers. Independent drawings select an \(s\)-subset of an \(n\)-coupon set according to a probability vector \(p\), and \(F_{n,s}(p)\) is the expected number of drawings required to cover all coupons. At the uniform vector \(p_*\), the Hessian restricted to the probability-simplex tangent space has exactly \(d=\min(s,n-s)\) distinct *harmonic-level labels*, \(j=1,\ldots,d\), with eigenvalue
\[
\lambda_j=2\sum_{b=s}^{n-1}
  \frac{(-1)^{n-b+1}\binom{b-j}{s-j}\binom{n-s-j}{b-s}}
       {\bigl(1-\binom{b}{s}/\binom{n}{s}\bigr)^3}.
\]
Here a binomial coefficient is zero when its lower argument is outside the allowed range. The invariant harmonic subspace at level \(j\) has dimension \(\binom nj-\binom n{j-1}\) (the numerical eigenvalues of different levels need not be asserted distinct), and
\[
  \operatorname{sgn}(\lambda_j)=(-1)^{j+1}, \qquad \lambda_j\ne0.
\]
Consequently, for every \(2\le s\le n-2\) the uniform package law is a **nondegenerate strict saddle**: it has strictly improving and strictly worsening nearby probability perturbations. For \(s=1\) or \(s=n-1\) it is instead a positive-definite strict local minimum. More precisely, every odd harmonic level contributes positive curvature and every even level contributes negative curvature, with the above exact multiplicities.

## Assumptions and scope
The packet probabilities \(p_S\) are indexed by all \(s\)-subsets \(S\subseteq[n]\). We consider the relative interior of the probability simplex \(p_S>0\), \(\sum_Sp_S=1\), so expected coverage times and their derivatives are finite. A tangent vector \(v\) satisfies \(\sum_Sv_S=0\). This concerns the **local second-order geometry** of expected coverage time, not a characterization of globally optimal nonuniform distributions. The symmetric uniform point is stationary on the simplex.

## Proof
**1. Inclusion-exclusion and the Hessian.** For \(B\subseteq[n]\), write \(r_B(p)=\sum_{S\subseteq B,\ |S|=s}p_S\). The probability all coupons have not been seen after \(t\) draws is, by inclusion-exclusion over missing coupons,
\[
\Pr_p(T>t)=\sum_{B\subsetneq[n]}(-1)^{n-|B|+1}r_B(p)^t.
\]
Summing over \(t\ge0\) gives the exact identity
\[
F_{n,s}(p)=\sum_{B\subsetneq[n]}\frac{(-1)^{n-|B|+1}}{1-r_B(p)}.
\]
At \(p_*\), put \(m=\binom ns\). If \(|B|=b\), then \(r_B(p_*)=\binom bs/m\), and for a tangent vector \(v\),
\[
D^2F_{n,s}(p_*)[v,v]=2\sum_{b=s}^{n-1}\frac{(-1)^{n-b+1}}{(1-\binom bs/m)^3}\sum_{|B|=b}\left(\sum_{S\subseteq B,|S|=s}v_S\right)^2.
\tag{1}
\]
The full gradient at \(p_*\) has identical coordinates by permutation symmetry, so its restriction to tangent vectors is zero.

**2. Diagonalization of the inclusion operators.** Let \(W_{b,s}\) denote the matrix whose \((B,S)\)-entry is \(\mathbf1\{S\subseteq B\}\). On the space of real functions on \(j\)-subsets, let \(H_j\) be the kernel of the downward incidence operator: \(h\in H_j\) precisely when \(\sum_{J\supset R,\,|J|=j}h(J)=0\) for every \((j-1)\)-subset \(R\). Set \(H_0=\mathbb R\). For \(j\le s\), lift \(h\) to level \(s\) by
\[
 u_s(S)=\sum_{J\subseteq S,\,|J|=j}h(J).
\]
The Boolean-lattice up/down identity \(D_{r+1}U_r-U_{r-1}D_r=(n-2r)I\) implies that, for \(j\le r\le n-j\),
\[
 U_ru_r=(r+1-j)u_{r+1},\quad D_{r+1}u_{r+1}=(n-r-j)u_r,
 \quad \|u_r\|^2=\binom{n-2j}{r-j}\|h\|^2.
\]
It also gives an orthogonal decomposition of level \(s\) into the lifted spaces \(H_j\), \(0\le j\le d=\min(s,n-s)\), of dimensions \(\binom nj-\binom n{j-1}\). This can be checked inductively from the commutator and adjointness of \(U,D\), with no assumption on the signs of the Hessian.

Direct counting yields \(W_{b,s}u_s=\binom{b-j}{s-j}u_b\). By adjointness and the displayed norm identity, \(W_{b,s}^{\mathsf T}W_{b,s}\) acts on the lifted \(H_j\) as the scalar
\[
\binom{b-j}{s-j}\binom{n-s-j}{b-s}.
\tag{2}
\]
The value is zero for \(b>n-j\). Inserting (2) into (1) gives precisely the claimed eigenvalues and multiplicities. The constant level \(j=0\) is removed by the simplex tangent condition.

**3. Exact alternating signs.** Fix \(1\le j\le d\), put \(N=n-s-j\ge0\), and for integers \(0\le k\le N\) write
\[
 P(k)=\frac{\binom{s+k}s}{m},\qquad
 A(k)=\binom{s+k-j}{s-j},\qquad
 G(k)=\frac{A(k)}{(1-P(k))^3}.
\]
Here \(0<P(k)<1\), because \(s+k\le n-j<n\). With \(\Delta f(k)=f(k+1)-f(k)\), the binomial sum is exactly
\[
\lambda_j=2(-1)^{j+1}\Delta^N G(0).
\tag{3}
\]
Every forward difference of each of the nonnegative sequences \(P(k)\) and \(A(k)\) is nonnegative on the required finite range: the binomial identity \(\Delta^r\binom{s+k}s=\binom{s+k}{s-r}\) gives this for \(P\), and the analogous identity gives it for \(A\). Products preserve nonnegative forward differences by repeatedly applying \(\Delta(fg)(k)=f(k+1)\Delta g(k)+g(k)\Delta f(k)\). Using
\[
  (1-P(k))^{-3}=\sum_{\ell\ge0}\binom{\ell+2}{2}P(k)^\ell,
\]
which converges uniformly over the finite set \(0\le k\le N\), shows \(\Delta^N G(0)\ge0\). It is strict for \(N=0\), since \(G(0)>0\). For \(N\ge1\), the term \(\ell=N\) is strict: \(\Delta^N P^N(0)>0\). One direct justification is that \(m^N P(k)^N\) counts ordered \(N\)-tuples of \(s\)-subsets of \([s+k]\); its Newton coefficient \(\Delta^N P^N(0)\) counts (up to the positive factor \(m^{-N}\)) the tuples collectively using every one of a specified \(N\) additional labels. Such tuples exist, by taking one distinct additional label together with any \(s-1\) of the original \(s\) labels in each subset. Multiplying by \(A(k)\), which has nonnegative differences and is positive, retains strictness. Equation (3) proves \(\operatorname{sgn}\lambda_j=(-1)^{j+1}\) and nonvanishing for all admissible parameters.

**4. Geometry.** For \(2\le s\le n-2\), both \(j=1\) and \(j=2\) occur, so positive and negative quadratic tangent directions coexist. At an interior stationary point, the Taylor expansion implies respectively larger and smaller expected completion times for all sufficiently small nonzero perturbations in these directions. For \(s=1\) or \(s=n-1\), only positive level \(j=1\) remains, proving strict local minimality. As a concrete exact instance, for \(n=4,s=2\) the two tangent eigenvalues are \(3568/125\) and \(-432/125\), with multiplicities three and two.

## Verification
Run `python3 verify.py` with Python 3.10 or later, using only the standard library. The checker constructs the Hessian action independently from the proper-subset inclusion-exclusion sum, compares it to the proposed closed eigenvalues on explicit harmonic vectors, checks the finite-difference identity and signs, and confirms the actual expected-time curvature under small feasible nonuniform perturbations. Its exhaustive finite instances are not an infinite proof; the argument in Section 3 supplies the all-parameter sign theorem.

## Relationship to prior work
Berend and Sher (first public preprint September 21, 2025) prove Schilling's global nonoptimality conjecture by explicitly constructing better distributions. Their paper identifies the *Hessian method* as an approach attempted in special cases by Schilling but does not derive a universal local Hessian signature. The present result supplies that missing universal second-order picture and strengthens the simple existence of a better nonuniform distribution to arbitrarily small improvements in every nontrivial regime. Schilling (2021) is a historical source for the Hessian idea; its complete text was not accessible for direct comparison and priority relative to any unstated further Hessian claims remains a risk. Their companion 2026 asymptotic paper (arXiv:2605.06953) assumes uniform drawings and determines leading expected-time regimes, not perturbation curvature. The inclusion-matrix decomposition is classical (Gottlieb, 1966); novelty is not claimed for that algebra alone.

## Limitations
The theorem classifies second derivatives at the uniform probability vector, not global minimizers or nonlinear landscape away from it. Harmonic-level eigenvalues may accidentally coincide numerically, although each level is nonzero with the stated sign and multiplicity. It applies to independent fixed-size package draws with all package probabilities positive in a neighborhood of uniform. No publication-level novelty certification or independent audit is asserted. The 2021 Schilling paper could not be fully inspected; its specific special cases are not claimed as new.

## References
- D. Berend and T. Sher, *On a Conjecture of Schilling Regarding the Coupon Collector's Problem*, arXiv:2509.17201 (first posted September 21, 2025); journal version *On a conjecture on uniform group drawings in the coupon collector problem*, Stochastic Models, DOI:10.1080/15326349.2026.2671340.
- J. Schilling, *Results and conjectures on the role of the uniform distribution in the coupon collector's problem with group drawings*, Information Processing Letters 169 (2021), 106112, DOI:10.1016/j.ipl.2021.106112.
- D. H. Gottlieb, *A certain class of incidence matrices*, Proceedings of the American Mathematical Society 17 (1966), 1233–1237, DOI:10.1090/S0002-9939-1966-0204305-9.
- I. Adler and S. M. Ross, *The coupon subset collection problem*, Journal of Applied Probability 38 (2001), 737–746, DOI:10.1239/jap/1005091036.
- D. Berend and T. Sher, *Asymptotic Results for Uniform Group Drawing in the Coupon Collector’s Problem*, arXiv:2605.06953 (May 7, 2026).
