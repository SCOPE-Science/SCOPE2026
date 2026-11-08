# Orientation law for Fourier sampling on ternary quadratic spheres

## Finding
Let \(F=\mathbb F_q\) be an odd finite field, let \(V\) be a three-dimensional \(F\)-vector space, and let \(Q:V\to F\) be a nondegenerate quadratic form of determinant square class \(\delta\in F^\times/(F^\times)^2\). For \(j\in F^\times\), write \(S_j=\{x\in V:Q(x)=j\}\) and \(\sigma=\eta(-\delta j)\in\{-1,1\}\), where \(\eta\) is the quadratic character. Then \(|S_j|=q^2+\sigma q\).

Fix any nontrivial additive character \(\psi:F\to\mathbb C^\times\). For every two-dimensional linear frequency plane \(L\le V^*\), define the normalized Fourier sampling operator
\[
 (\mathcal A_L c)(x)=|S_j|^{-1/2}\sum_{\ell\in L}c_\ell\psi(\ell(x)),\qquad x\in S_j.
\]
Its \(q^2\)-by-\(q^2\) Gram matrix \(\mathcal A_L^*\mathcal A_L\) has the exact spectra below. Let \(Fv=L^\perp\) be the annihilator line in \(V\).

**Isotropic annihilator:** If \(Q(v)=0\), the Gram eigenvalues, given as \((\text{eigenvalue},\text{multiplicity})\), are
\[
\begin{array}{c|c}
0&q-1-\sigma\\
q^2/(q^2+\sigma q)&q^2-q\\
q^3/(q^2+\sigma q)&1+\sigma
\end{array}.
\]
The last line has zero multiplicity when \(\sigma=-1\). Its rank is \(q^2-q+1+\sigma\).

**Anisotropic annihilator:** If \(s=Q(v)\ne0\), put \(\varepsilon=\eta(-\delta s)\in\{-1,1\}\). The Gram eigenvalues are
\[
\begin{array}{c|c}
0&(q^2-\sigma q-q+\varepsilon)/2\\
q^2/(q^2+\sigma q)&q-\varepsilon\\
2q^2/(q^2+\sigma q)&(q^2+\sigma q-q+\varepsilon)/2
\end{array}.
\]
Its rank is \((q^2+\sigma q+q-\varepsilon)/2\).

There are exactly \(q+1\) isotropic annihilator lines and exactly \(q(q+\varepsilon)/2\) anisotropic lines of each type \(\varepsilon\). Thus these spectra classify *every* frequency plane, including its kernel dimension and all nonzero singular values.

The maximum possible rank is \(q^2-q+1+\sigma\). It is achieved by all and only the \(q+1\) isotropic annihilator planes, except when \(q=3\) and \(\sigma=1\), in which case the three additional anisotropic planes of type \(\varepsilon=-1\) tie for maximal rank. For \(\sigma=-1\), the isotropic planes produce a tight nonzero singular spectrum (a scalar partial isometry) on the \(q^2-q\)-dimensional identifiable subspace. For \(\sigma=1\), the isotropic planes have positive singular-value condition number \(\sqrt q\), whereas every anisotropic plane has positive singular-value condition number \(\sqrt2\).

## Assumptions and scope
The field has odd cardinality \(q\ge3\). The form is homogeneous, nondegenerate, and of dimension exactly three. The level \(j\) is nonzero. The frequency plane consists of *all* \(q^2\) additive characters from a two-dimensional linear subspace, and the observation domain is the complete quadric level set with uniform weights. Zero eigenvalues represent genuinely unobservable coefficient vectors, not numerical singularity. The coefficient space is complex; the quadratic-form data are over \(F\).

The determinant square class \(\delta\) is that of the symmetric Gram matrix \(B\) defined by \(Q(x)=x^\top Bx\) in any basis. Because basis changes multiply the determinant by a square, \(\eta(\delta)\) and the signs in the theorem are intrinsic. Changing the representative \(v\) of its line multiplies \(s\) by a square and does not change \(\varepsilon\).

## Proof
**1. Fourier diagonalization by fibers.** Let \(K=L^\perp\), a one-dimensional subspace of \(V\), and let \(\pi:V\to V/K\) be the quotient projection. For \(y\in V/K\), set
\[m(y)=\#\{x\in S_j:\pi(x)=y\}.\]
The evaluation of characters \(L\cong(V/K)^*\) on the quotient is a complete \(q^2\)-point Fourier matrix \(H\), with \(HH^*=q^2 I\). Since \(\psi(\ell(x))\) is constant on each coset of \(K\), orthogonality gives
\[
\mathcal A_L^*\mathcal A_L
=|S_j|^{-1}H^*\operatorname{diag}(m(y))H.
\]
Hence the Gram spectrum consists exactly of \(q^2m(y)/|S_j|\), one eigenvalue for every quotient coset \(y\). This identity holds even when \(m(y)=0\).

**2. Elementary finite-field quadratic counts.** The character-sum identities for a nondegenerate binary quadratic form \(R\) of determinant \(\Delta\) and a nonzero \(j\) are
\[
\#\{z\in F^2:R(z)=j\}=q-\eta(-\Delta),
\]
and for a nondegenerate ternary form \(Q\) they are
\[
\#\{x\in F^3:Q(x)=j\}=q^2+\eta(-\delta j)q,
\qquad
\#\{x\in F^3:Q(x)=0\}=q^2.
\]
For completeness, diagonalize the forms. Orthogonality writes the number of solutions as \(q^{-1}\sum_{t\in F}\psi(-tj)\prod_i\sum_{x\in F}\psi(t a_i x^2)\). For \(t\ne0\), each inner sum equals \(\eta(t a_i)G\), where \(G=\sum_x\psi(x^2)\) obeys \(G^2=\eta(-1)q\). The even-dimensional \(t\)-sum is \(-1\) for \(j\ne0\), and the odd-dimensional sum is \(\eta(-j)G\). Substitution gives exactly the displayed formulas. In particular the number of nonzero isotropic vectors is \(q^2-1\), so there are \(q+1\) isotropic projective lines.

**3. Isotropic annihilator.** Suppose \(Q(v)=0\). By nondegeneracy, choose \(w\) such that \(B_Q(v,w)=1\), where \(B_Q(u,w)=(Q(u+w)-Q(u)-Q(w))/2\). Replacing \(w\) by \(w-Q(w)v/2\) makes \(Q(w)=0\). The orthogonal complement of the hyperbolic plane \(Fv+Fw\) is a one-dimensional anisotropic line \(Fz\), and
\[
Q(tv+uw+rz)=2tu+\kappa r^2,
\qquad \eta(\kappa)=\eta(-\delta).
\]
The quotient \(V/Fv\) has coordinates \((u,r)\). When \(u\ne0\), exactly one \(t\) satisfies \(Q=j\), giving \(q^2-q\) fibers of size one. When \(u=0\), the fiber has size \(q\) precisely if \(\kappa r^2=j\), otherwise zero. As \(j\ne0\), the equation for \(r\) has \(1+\eta(j/\kappa)=1+\sigma\) solutions. Thus there are \(1+\sigma\) fibers of size \(q\), and \(q-1-\sigma\) empty fibers, giving the isotropic spectrum and rank.

**4. Anisotropic annihilator.** Suppose \(Q(v)=s\ne0\). Orthogonal decomposition gives \(V=Fv\oplus v^{\perp_Q}\), with \(Q(tv+w)=st^2+R(w)\). The binary residual form \(R\) has determinant square class \(\delta/s\), so its sign is \(\eta(-\delta/s)=\varepsilon\). Each coset corresponds to one \(w\), and its fiber is the number of solutions of \(st^2=j-R(w)\). There are \(q-\varepsilon\) fibers of size one, by the binary count. Every other fiber has size zero or two. If \(N_2\) denotes the number of size-two fibers, then summing all fiber sizes gives \(2N_2+q-\varepsilon=|S_j|=q^2+\sigma q\), so
\[
N_2=(q^2+\sigma q-q+\varepsilon)/2,
\qquad
N_0=(q^2-\sigma q-q+\varepsilon)/2.
\]
Fourier diagonalization proves the anisotropic spectrum and rank.

**5. Orientation counts, optimality, and conditioning.** For each \(a\in F^\times\), the ternary count gives \(q^2+\eta(-\delta a)q\) vectors of norm \(a\). Summing over the \((q-1)/2\) values of fixed sign \(\varepsilon=\eta(-\delta a)\), then dividing by \(q-1\) representatives per line, yields exactly \(q(q+\varepsilon)/2\) anisotropic projective lines. For a fixed \(\sigma\), the larger anisotropic rank occurs at \(\varepsilon=-1\). The difference between the isotropic rank and this rank equals
\[
\frac{(q-1)(q-3)}2\quad(\sigma=1),
\qquad
\frac{q^2-2q-1}2\quad(\sigma=-1).
\]
These are nonnegative for \(q\ge3\), with equality only when \(q=3,\sigma=1\). The multiplicities above establish the maximizing-plane classification. Dividing the largest positive Gram eigenvalue by the smallest gives \(q\) for isotropic planes with \(\sigma=1\), \(1\) for isotropic planes with \(\sigma=-1\), and \(2\) for all anisotropic planes. Taking square roots gives the stated positive singular-value condition numbers.

## Verification
The included `CHECK.py` constructs finite fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_9,\mathbb F_{11}\) explicitly (using \(X^2+1\) for the genuine quadratic extension \(\mathbb F_9\)). For each field it examines two discriminant square classes, both nonzero-radius square classes, and *all* \(q^2+q+1\) annihilator directions. For every direction it enumerates every quotient coset and its fiber cardinality, and compares all multiplicities and ranks with the formulas. It additionally checks direct Fourier Gram entries for all three geometric direction types at small field sizes. Execute with `python3 CHECK.py`; it requires only the Python standard library. The observed summary is `CHECK_OK configurations=1300 multiplicity_assertions=5200 direct_gram_classes=24 fields=3,5,7,9,11`. These finite tests are checks of, not replacements for, the general proof.

## Relationship to prior work
Pham and Xue, *Sharp spherical \(L^p\to L^4\) extension estimates over finite fields in odd dimensions* (arXiv:2610.29664, first version 2026-10-21), study sharp extension estimates and sparse recovery when missing frequencies lie on spheres. Their main theorem and signal-recovery section do not compute the exact frame spectrum of complete two-dimensional frequency planes *sampled on* a ternary quadratic sphere. Fraser and Rakhmonov, *Exceptional projections in finite fields: Fourier analytic bounds and incidence geometry* (arXiv:2503.15072, 2025), give general bounds on projection sizes and a subspace Plancherel identity. Those results motivate looking at projection fibers, but do not specify the quadratic-sign-dependent, all-orientation spectral classification obtained here. Standard finite-field quadratic counts and Fourier orthogonality are prior mathematical ingredients, not novel claims.

The contribution is the combined exact full spectral and multiplicity classification, the conic-indexed rank-optimal orientation theorem, the exceptional \(q=3\) tie, and the tightness/conditioning tradeoff. General subspace Plancherel on its own does not imply the numerical classification without the quadratic coset analysis. A prior unindexed equivalent projective-quadric calculation is a residual originality risk.

## Limitations
This is exact noiseless finite-dimensional linear sampling, not phase retrieval, nonlinear recovery, or the global \(L^p\to L^4\) restriction problem. It does not classify incomplete frequency planes, positive reweighting, characteristic two, degenerate forms, zero-radius quadrics, or ambient dimensions other than three. The smallest *positive* singular value describes stability only after quotienting by the nontrivial kernel; no plane gives full column rank. The rank-optimal orientation is not in general the least-conditioned orientation among all planes. Independent external validation has not been performed.

## References
- T. Pham and B. Xue, *Sharp spherical \(L^p\to L^4\) extension estimates over finite fields in odd dimensions*, arXiv:2610.29664, version 1 (2026-10-21), https://arxiv.org/abs/2610.29664.
- J. M. Fraser and F. Rakhmonov, *Exceptional projections in finite fields: Fourier analytic bounds and incidence geometry*, arXiv:2503.15072, version 2 (2025-04-23), https://arxiv.org/abs/2503.15072.
- A. Iosevich and D. Koh, *Extension theorems for spheres in the finite field setting*, Forum Mathematicum 22 (2010), 457–483, arXiv:0712.1627.
