# Exact algebra-retraction ranks and logarithmic cotangent corank in characteristic two

## Finding
Let \(k=\mathbb F_q\), where \(q=2^e\) and \(e\ge1\), and for each integer \(n\ge2\) let
\[
A_n=k[x_1,\ldots,x_n]/(x_1^2,\ldots,x_n^2).
\]
An **algebra retraction** means a unital \(k\)-algebra endomorphism \(P:A_n\to A_n\) satisfying \(P^2=P\). For \(0\le r\le n\), the number \(N_{n,r}(q)\) of retractions whose \(k\)-linear image has dimension \(2^r\) is
\[
\boxed{N_{n,r}(q)=\frac{|\mathrm{GL}_n(q)|}{|\mathrm{GL}_r(q)|\,|\mathrm{GL}_{n-r}(q)|}\,q^{E_{n,r}},}\qquad
E_{n,r}=n(2^n-1-n)-r(2^r-1-r)-(n-r)(2^n-2^r-(n-r)).
\]
Here \(|\mathrm{GL}_0(q)|=1\). These are all possible image dimensions. Thus the complete ordinary linear-rank enumerator is
\[
\boxed{F_{n,q}(z)=\sum_{r=0}^{n}N_{n,r}(q)z^{2^r}.}
\]
Equivalently, with \(s=n-r\) and Gaussian binomial coefficients,
\[
N_{n,n-s}(q)={n\brack s}_q q^{(n-s)2^n+(2s-n)2^{n-s}-(n-s)s-s}.
\]
If \(S_n=n-\dim_k\bigl((\operatorname{im}P\cap\mathfrak m)/(\operatorname{im}P\cap\mathfrak m)^2\bigr)\), where \(P\) is uniformly chosen among all retractions and \(\mathfrak m=(x_1,\ldots,x_n)\), then \(S_n=n-r\), where \(2^r=\dim_k\operatorname{im}P\). Set \(T_n=\lfloor\log_2 n\rfloor\) and \(C_q=\prod_{j\ge1}(1-q^{-j})^{-1}<\infty\). For every \(n\ge64\),
\[
\boxed{\Pr(T_n-2\le S_n\le T_n+2)\ge1-(n+1)C_q q^{-2^{n-1}}.}
\]
Hence a uniformly chosen retraction has \(k\)-linear image dimension \(\Theta(2^n/n)\) with probability tending to one. If \(H_n(q)=\sum_{r=0}^nN_{n,r}(q)\), then for fixed even prime power \(q\),
\[
\boxed{\log_q H_n(q)=(n-\log_2 n)2^n+O_q(2^n).}
\]

## Assumptions and scope
All maps are **unital and \(k\)-linear algebra maps**, not merely linear projections and not necessarily Hopf-algebra maps. Their rank is their dimension as \(k\)-linear maps on the \(2^n\)-dimensional algebra. The algebra is local, with unique maximal ideal \(\mathfrak m\) and cotangent space \(\mathfrak m/\mathfrak m^2\) of dimension \(n\). The restriction to characteristic two is essential to the argument: every element of \(\mathfrak m\) has square zero, so every assignment of generators to elements of \(\mathfrak m\) gives a unital algebra homomorphism. Over characteristic two \(A_n\) is also the group algebra of the elementary abelian group \((C_2)^n\), under \(x_i\leftrightarrow g_i-1\). No claim about arbitrary characteristic or noncommutative groups is made.

## Proof
**1. Automorphisms.** Write \(d_n=2^n-1-n\). Each \(a\in\mathfrak m\) has \(a^2=0\) because in characteristic two cross terms vanish and every positive-degree squarefree monomial squares to zero. An endomorphism is specified by an arbitrary ordered tuple of \(n\) elements of \(\mathfrak m\). It is an automorphism if and only if its linear terms yield an invertible map on \(\mathfrak m/\mathfrak m^2\): necessity follows from passage to the quotient; sufficiency follows by Nakayama's lemma and finite dimensionality, because the images generate \(\mathfrak m\) and hence the algebra. Each fixed invertible cotangent matrix has \(q^{nd_n}\) lifts. Therefore
\[
|\operatorname{Aut}_k(A_n)|=|\mathrm{GL}_n(q)|q^{n(2^n-1-n)}.
\]
**2. Conjugacy of retractions.** An idempotent \(P\) induces an idempotent linear map \(\bar P\) on the cotangent space, with some rank \(r\). By a linear change of the generators, which itself extends to an algebra automorphism in characteristic two, assume \(\bar P(x_i)=x_i\) for \(i\le r\), and \(\bar P(x_j)=0\) for \(j>r\). Let \(y_i=P(x_i)\) for \(i\le r\) and \(z_j=x_j-P(x_j)\) for \(j>r\). These elements have independent cotangent classes, so the substitution \(\phi(x_i)=y_i\) and \(\phi(x_j)=z_j\) extends to an algebra automorphism. By idempotence, \(P(y_i)=y_i\) and \(P(z_j)=0\), so \(P\circ\phi=\phi\circ P_r\), where \(P_r\) fixes the first \(r\) variables and kills the remaining variables. Every retraction is therefore conjugate to exactly one of the \(n+1\) standard maps \(P_r\). The image of \(P_r\) is canonically \(A_r\) and has dimension \(2^r\).

**3. Stabilizer enumeration.** Put \(s=n-r\). An automorphism \(\phi\) commutes with \(P_r\) precisely when the images of the first \(r\) variables lie in \(\operatorname{im}P_r\cap\mathfrak m\), and those of the remaining \(s\) variables lie in \(\ker P_r\). The two spaces have dimensions \(2^r-1\) and \(2^n-2^r\), respectively. Invertibility on the cotangent space requires independent diagonal blocks in \(\mathrm{GL}_r(q)\) and \(\mathrm{GL}_s(q)\). Choosing all higher coefficients freely gives the exact centralizer order
\[
|C_{\operatorname{Aut}_k(A_n)}(P_r)|=
|\mathrm{GL}_r(q)|\,|\mathrm{GL}_s(q)|\,
q^{r(2^r-1-r)+s(2^n-2^r-s)}.
\]
Orbit–stabilizer yields \(N_{n,r}(q)\). The Gaussian-binomial version follows from the standard identity \(|\mathrm{GL}_n(q)|/(|\mathrm{GL}_r(q)||\mathrm{GL}_s(q)|)={n\brack s}_q q^{rs}\). This proves all finite counts.

**4. Logarithmic cotangent corank.** Define
\[
\Phi_n(s)=(n-s)2^n+(2s-n)2^{n-s}-s,
\qquad B_{n,s}(q)=q^{-s(n-s)}{n\brack s}_q.
\]
Then \(N_{n,n-s}(q)=q^{\Phi_n(s)}B_{n,s}(q)\). The product formula for Gaussian binomials yields \(1\le B_{n,s}(q)\le C_q\). Direct subtraction gives
\[
\Phi_n(s+1)-\Phi_n(s)=2^{n-s}(n/2+1-s-2^s)-1.
\]
For \(n\ge64\), \(T=\lfloor\log_2 n\rfloor\), and \(0\le s\le T-3\), we have \(2^s\le n/8\), \(s\le T\le n/8\), so the difference is at least \(2^n-1\). For \(T+2\le s<n\), \(2^s>2n\), so the difference is at most \(-(3/4-1/(2n))2^n-1\), strictly smaller than \(-2^{n-1}\). Thus every term with \(s<T-2\), respectively \(s>T+2\), is at most \(C_q q^{-2^{n-1}}\) times the term at \(s=T-2\), respectively at \(s=T+2\). Summing at most \(n+1\) outlying terms proves the probability bound. Within the five-index window \(s=T+O(1)\), \(\Phi_n(s)=(n-\log_2 n)2^n+O(2^n)\). The bounds on \(B_{n,s}\), the tail estimate, and at most \(n+1\) terms establish the asserted logarithmic total-count asymptotic.

## Verification
Finite validation is independent of the orbit–stabilizer proof. The self-contained `verify.py` enumerates every algebra homomorphism of the four-dimensional algebra \(A_2\) over \(\mathbb F_2\) and \(\mathbb F_4\), tests \(P^2=P\), computes cotangent ranks, and compares multiplicities. It obtains respectively \((1,12,1)\) and \((1,80,1)\). The accompanying `verify.cpp`, when compiled with a C++17 compiler, directly enumerates all \(2^{21}\) generator-image triples for \(A_3\) over \(\mathbb F_2\) and obtains \((1,448,3584,1)\), again matching the theorem. The executable also verifies the one- and two-variable cases. Run `python3 verify.py` from the directory containing both files; output ends in `VERIFY_OK`. Finite experiments do not establish the all-dimensions theorem; Steps 1–4 provide that proof.

## Relationship to prior work
The classification of idempotent *matrices* over finite local rings and their number is part of the established study of finite-ring idempotents (Dolžan, 2021); these are not the same as multiplicative algebra self-retractions. Erdmann and Holloway (2006, Section 5) study precisely the truncated square-zero polynomial algebras \(A_n\), chiefly for support varieties of modules; their paper explicitly identifies the characteristic-two group-algebra realization. Neither paper, in the material inspected, provides the present full enumeration of **idempotent algebra endomorphisms** and its logarithmic cotangent-corank concentration. The proof here uses standard finite linear-group counts and Nakayama's lemma, and does not claim those tools as new.

## Limitations
The result is restricted to unital endomorphisms of \(A_n\) over finite fields of characteristic two. It does not classify Hopf retractions, arbitrary truncated complete intersections, endomorphisms in odd characteristic, or module-theoretic rank varieties. The asymptotic probability bound is stated for \(n\ge64\) and fixed \(q\). While exact literature searches found no direct identity, broad unpublished or poorly indexed results on retractions of local complete intersections may imply this formula; independent priority review is outstanding.

## References
1. D. Dolžan, *Bounds for the number of idempotents in finite rings*, Communications in Algebra; first published online May 28, 2021. DOI: 10.1080/00927872.2021.1929277.
2. K. Erdmann and M. Holloway, *The Avrunin and Scott theorem and a truncated polynomial algebra*, Journal of Algebra **299** (2006), 344–373, especially Section 5. DOI: 10.1016/j.jalgebra.2005.12.031. Authorized full text: https://ora.ox.ac.uk/objects/uuid:8df88d72-35f0-43fc-9955-98055912ff5d.
