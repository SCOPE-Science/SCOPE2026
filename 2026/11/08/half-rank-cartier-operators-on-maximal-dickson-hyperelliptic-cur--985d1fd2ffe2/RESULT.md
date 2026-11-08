# Half-rank Cartier operators on maximal Dickson hyperelliptic curves

## Finding
Let \(k=\overline{\mathbb F}_p\) have characteristic an odd prime \(p>3\). Let \(n>5\) be odd and assume \(p^2\equiv-1\pmod{2n}\). Write \(D_n\in\mathbb Z[x]\) for the monic Dickson/Chebyshev polynomial determined by \(D_n(t+t^{-1})=t^n+t^{-n}\). Let \(X_n\) be the smooth projective model of
\[
 y^2=(x+2)D_n(x).
\]
Then necessarily \(n\equiv1\pmod4\), \(X_n\) has genus \(g=(n-1)/2\), and the Cartier operator \(\mathcal C\) on \(H^0(X_n,\Omega^1)\) satisfies
\[
 \operatorname{rank}(\mathcal C)=\frac{n-1}{4}=\frac g2,
 \qquad a(\operatorname{Jac}X_n)=\frac{n-1}{4},
 \qquad\mathcal C^2=0,
 \qquad\operatorname{im}\mathcal C=\ker\mathcal C.
\]
Here the \(a\)-number is \(g-\operatorname{rank}(\mathcal C)\). The exact **first** Cartier rank is the new invariant evaluated here. Maximality over \(\mathbb F_{p^4}\), and, under additional numerical exceptions, the automorphism-group description, are pre-existing results, not new claims: \(X_n\) is maximal over \(\mathbb F_{p^4}\); if neither \(2n-1\) nor \(4n-1\) is a power of \(p\), its full geometric automorphism group is cyclic of order two (Borges–Reis, Theorem 1.2).

In particular, \(n=13\) and any prime \(p\equiv5\pmod{26}\) with \(p>5\), or \(p\equiv21\pmod{26}\), give a maximal genus-six curve with \(a=3\), Cartier rank three, and only its hyperelliptic involution as automorphism. This includes \(p=31\) and \(p=47\). The congruence classes contain infinitely many primes by Dirichlet's theorem.

## Assumptions and scope
All curves and Cartier operators are over an algebraically closed field of odd characteristic; \(p^2\equiv-1\pmod{2n}\) implies \(p\nmid n\). The polynomial \(D_n\) is normalized by \(D_0=2\), \(D_1=x\), and \(D_m=xD_{m-1}-D_{m-2}\). It has distinct roots because \(p\nmid n\); since \(n\) is odd, \(D_n(-2)=-2\ne0\). Hence the defining polynomial has \(n+1\) distinct roots and genus \(g=(n-1)/2\). \(\mathcal C\) is the \(p^{-1}\)-linear Cartier operator on global regular differentials, and rank and kernel are interpreted as \(k\)-subspaces.

## Proof
**A tame Fermat-type cover.** Consider the smooth curve
\[
 Y_n:\quad w^2=t^{2n}+1.
\]
It has genus \(n-1\). The map \(\sigma(t,w)=(t^{-1},w/t^n)\) is an involution. Set
\[
 x=t+t^{-1},\qquad y=(t+1)w/t^{(n+1)/2}.
\]
These functions are invariant under \(\sigma\) (the exponent \((n+1)/2\) is integral), and satisfy
\[
 y^2=(t+t^{-1}+2)(t^n+t^{-n})=(x+2)D_n(x).
\]
The extension \(k(Y_n)/k(x,y)\) has degree two (since \(t\) solves \(t^2-xt+1=0\)), hence \(X_n=Y_n/\langle\sigma\rangle\). Because \(2\) is invertible, pullback identifies the invariant differentials of \(Y_n\) with the differentials of \(X_n\), and Cartier commutes with pullback.

**Cartier matrix of the cover.** Put \(m=(p-1)/2\), and take the holomorphic basis
\[
 \omega_i=t^{i-1}\,dt/w,\qquad 1\le i\le n-1.
\]
The standard hyperelliptic Cartier formula expresses \(\mathcal C(\omega_i)\) as a sum of \(c_{pi-j}^{1/p}\omega_j\), where \(c_e\) is the coefficient of \(t^e\) in
\[
 (t^{2n}+1)^m=\sum_{h=0}^{m}\binom mh t^{2nh}.
\]
Every \(\binom mh\) is nonzero modulo \(p\), because \(0\le h\le m<p\). Therefore \(\mathcal C(\omega_i)\ne0\) precisely when the least positive residue \(r_i\equiv pi\pmod{2n}\) lies in \(\{1,\ldots,n-1\}\). In that event the image is a nonzero multiple of \(\omega_{r_i}\). The exponent \(pi-r_i\) is a nonnegative multiple of \(2n\), with multiplier at most \(m\), so there are no hidden truncation exceptions. No two different \(i\) have the same target, because \(p\) is invertible modulo \(2n\).

Under the involution, \(\sigma^*\omega_i=-\omega_{n-i}\). For \(1\le i\le g\), the \(g\) invariant forms \(\eta_i=\omega_i-\omega_{n-i}\) form a basis of the pullback of \(H^0(X_n,\Omega^1)\). Because \(p\) is odd, \(r_{n-i}\equiv n-r_i\pmod{2n}\), so both members of each pair are simultaneously active or inactive. When active, their binomial coefficients agree by \(\binom m h=\binom m{m-h}\), and \(\mathcal C(\eta_i)\) is a nonzero multiple of \(\eta_j\) or its negative, where \(j=\min(r_i,n-r_i)\). Distinct active pairs have distinct target pairs: equality would imply either \(i=i'\) or \(i+i'=n\), impossible for two distinct indices in \(\{1,\ldots,g\}\). Thus the rank on \(X_n\) is the number of active representatives \(i=1,\ldots,g\).

**Fixed-point-free residue pairing.** Let \(S=\{1,\ldots,n-1\}\) and define \(\theta:S\to S\) by
\[
 \theta(i)=\min\bigl(r_i,2n-r_i\bigr),\qquad r_i\equiv pi\pmod{2n},\quad1\le r_i\le2n-1.
\]
Neither \(r_i=0\) nor \(r_i=n\) occurs, since \(p\) is invertible modulo \(2n\). The congruence \(p^2\equiv-1\pmod{2n}\) shows \(\theta^2(i)=i\). No \(i\) is fixed: otherwise \(pi\equiv\pm i\pmod{2n}\), hence \(p^2i\equiv i\pmod{2n}\), implying \(2i\equiv0\pmod{2n}\), impossible for \(i\in S\). Moreover, \(\theta\) swaps active and inactive indices: if \(r_i<n\), then \(p\theta(i)\equiv-i\pmod{2n}\), which is inactive; if \(r_i>n\), then \(p\theta(i)\equiv i\pmod{2n}\), which is active. Exactly half of \(S\), namely \((n-1)/2\) elements, are active. Since the involution \(i\mapsto n-i\) preserves activity and has no fixed points on \(S\), exactly \((n-1)/4\) active indices occur among the invariant representatives \(1\le i\le g\). In particular this count proves \(n\equiv1\pmod4\).

Therefore \(\operatorname{rank}(\mathcal C|_{X_n})=(n-1)/4\), and \(a=g-\operatorname{rank}(\mathcal C)=(n-1)/4\).

**Nilpotence and extremal kernel/image.** Any nonzero two-step Cartier transition on \(Y_n\) would give \(p^2i\equiv j\pmod{2n}\) with \(1\le i,j\le n-1\), but \(p^2i\equiv-i\pmod{2n}\), whose residue lies in \(\{n+1,\ldots,2n-1\}\). Thus \(\mathcal C^2=0\) on \(Y_n\) and on \(X_n\). Finally the rank is half the dimension, so \(\operatorname{im}\mathcal C\subseteq\ker\mathcal C\) and their dimensions coincide; equality follows.

**Maximality and few automorphisms (prior results).** Here \(n\mid(p^2+1)/2\). Tafazolian–Top proved maximality of the Dickson curve over \(\mathbb F_{p^4}\); Borges–Reis Theorem 1.2 gives geometric \(\operatorname{Aut}(X_n)=C_2\) provided \(n>5\), \(p>3\) and neither \(2n-1\) nor \(4n-1\) is a power of \(p\). In the \(n=13\) prime residue classes above, those exceptions are absent for \(p>5\). No novelty is asserted for either of these cited statements.

## Verification
The standalone Python 3 script `cheb_verify.py` reconstructs \(D_n\) from its recurrence, computes the coefficients of \(((x+2)D_n(x))^{(p-1)/2}\) modulo \(p\), forms the full \(g\times g\) Cartier–Manin matrix, and performs exact modular row reduction and multiplication. It independently checks rank \(g/2\) and square-zero for the six cases \((p,n)=(5,13),(7,25),(13,17),(31,13),(47,13),(73,13)\), returning `VERIFY_OK`. These finite checks are not an infinite proof; the residue pairing above proves the statement for all admissible \((p,n)\).

## Relationship to prior work
Tafazolian–Top (2019) already constructs Dickson quotients and proves maximality criteria. Borges–Reis (2026), Theorem 1.2, already proves the two-element geometric automorphism group under explicit numerical hypotheses. Garcia–Tafazolian (2008) gives general Cartier nilpotence consequences for maximal curves; thus nilpotence alone is not original. Novoselov (2019) computes Cartier matrices for a related sparse covering family, with generalized-permutation methods but a different defining equation. Tafazolian–Top (2025) studies the Chebyshev curve without the additional factor \(x+2\). The contribution isolated here is an exact first Cartier rank and \(a\)-number for the Dickson **quotient** family in the order-four residue class, giving an explicit half-genus invariant on maximal curves with the smallest automorphism group. The underlying formula is new relative to the inspected results, not an assertion of independently established historical priority.

## Limitations
The theorem concerns odd \(n>5\), primes \(p>3\) with \(p^2\equiv-1\pmod{2n}\), and the specific normalization of the Dickson polynomial. It does not classify all congruence classes, all isogeny types, or full Ekedahl–Oort types. The \(a\)-number and first Cartier rank do not by themselves determine the full \(p\)-torsion group scheme. A related 2025 open-access published article was compared using its abstract and publication description, not its entire body, leaving a residual historical-priority risk. Independent mathematical validation has not been performed.

## References
1. H. Borges and L. Reis, *Maximal Curves with Few Automorphisms*, arXiv:2610.37777v1 (first submitted 2026-10-27), Theorem 1.2 and its proof, https://arxiv.org/abs/2610.37777.
2. S. Tafazolian and J. Top, *On Certain Maximal Hyperelliptic Curves Related to Chebyshev Polynomials*, arXiv:1902.06262v2 (2019), especially Section 4, https://arxiv.org/abs/1902.06262.
3. A. Garcia and S. Tafazolian, *Certain maximal curves and Cartier operators*, Acta Arithmetica 135 (2008), 199–218, doi:10.4064/aa135-3-1.
4. S. A. Novoselov, *Counting points on hyperelliptic curves of type \(y^2=x^{2g+1}+ax^{g+1}+bx\)*, arXiv:1902.05992v1 (2019), https://arxiv.org/abs/1902.05992.
5. S. Tafazolian and J. Top, *CM theory, maximal hyperelliptic curves, and Chebyshev polynomials*, arXiv:2509.00273v1 (2025), https://arxiv.org/abs/2509.00273.
6. G. Dias, S. Tafazolian and J. Top, *On certain maximal curves related to Chebyshev polynomials*, Finite Fields and Their Applications 101 (2025), 102521, doi:10.1016/j.ffa.2024.102521.
