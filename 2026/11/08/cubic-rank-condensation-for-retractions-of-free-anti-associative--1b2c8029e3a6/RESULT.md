# Cubic-rank condensation for retractions of free anti-associative algebras

## Finding
Let \(q\) be any odd prime power, \(K=\mathbb F_q\), and \(F_n\) the free nonunital anti-associative \(K\)-algebra on \(n\ge 1\) generators. Thus \((ab)c=-a(bc)\) for all elements. For \(0\le r\le n\), put \(B(t)=t^2+t^3\), \(d(r)=r+B(r)\), and let \({n\brack r}_q\) denote the Gaussian binomial coefficient.

Every composition-idempotent algebra endomorphism \(e:F_n\to F_n\) has image isomorphic to \(F_r\) for a unique \(r\), so its linear rank is exactly \(d(r)\). The number of **distinct embedded image subalgebras** of this type is
\[
 I_{n,r}(q)={n\brack r}_q q^{r(B(n)-B(r))}.
\]
Every such embedded image is attained by exactly \(q^{(n-r)d(r)}\) idempotent endomorphisms. Consequently the complete linear-rank enumerator is
\[
 \boxed{\mathcal R_{n,q}(z)=\sum_{r=0}^{n}{n\brack r}_q\,q^{r(B(n)-B(r))+(n-r)d(r)} z^{d(r)}.}
\]
No other ranks occur, and both endpoint strata contain one endomorphism.

Let \(r_n\) be the degree-one generator rank of a uniformly selected idempotent endomorphism. Write
\[
 E_n(x)=-2x^4+(n-2)x^3+(n-2)x^2+(n^3+n^2+2n)x
\]
and let \(x_n\in(0,n)\) denote the unique real maximum point of \(E_n\) for all sufficiently large \(n\). For every fixed odd \(q\), there exists \(c_q>0\) such that
\[
 \Pr\{r_n\in\{\lfloor x_n\rfloor,\lceil x_n\rceil\}\}=1-O_q(q^{-c_qn^2}).
\]
Here \(x_n=\alpha n+O(1)\), where \(\alpha\in(0,1)\) is the unique root of \(8\alpha^3-3\alpha^2-1=0\), approximately \(0.6610498029006993\). This root is irrational. In particular, the image dimension divided by \(\dim F_n\) converges in probability to \(\alpha^3\), approximately \(0.288870065718145\).

## Assumptions and scope
The characteristic is odd; neither algebra units nor unital homomorphisms are involved. The free algebra \(F_n\) has the graded vector-space decomposition
\[
 F_n=V\oplus(V\otimes V)\oplus(V\otimes V\otimes V),\qquad \dim_K V=n,
\]
where \(u\,v=u\otimes v\), \(u\,(v\otimes w)=u\otimes v\otimes w\), and \((u\otimes v)\,w=-u\otimes v\otimes w\); all other homogeneous products vanish. These rules satisfy anti-associativity and exhibit the universal free object in odd characteristic. Distinguish \(e^2=e\), composition-idempotence of a map, from an idempotent element in the algebra. The linear rank \(d(r)\) is the dimension of the image, not the rank on \(V\) alone.

## Proof
**Step 1: Automorphism lifting and orbit structure.** Let \(J=F_n^2\). Every assignment of the \(n\) free generators to arbitrary elements with an invertible degree-one coefficient matrix extends uniquely to an automorphism: the map is invertible on \(F_n/J\), on \(J/F_n^3\), and on \(F_n^3\), whence it is invertible on \(F_n\). In particular the kernel \(G\) of the map \(\operatorname{Aut}(F_n)\to\operatorname{GL}(V)\) consists of arbitrary higher-degree shifts of each generator, and
\[
 |G|=q^{nB(n)}.
\]

Let \(e^2=e\) and let \(P\) be the induced idempotent on \(V\). Write \(V=U\oplus W\) with \(U=\operatorname{im}P\), \(W=\ker P\), \(\dim U=r\). Define a generator assignment \(g(u)=e(u)\) for basis elements \(u\in U\) and \(g(w)=w-e(w)\) for basis elements \(w\in W\). It is identity modulo \(J\), hence extends to an automorphism \(g\in G\). On all generators, \(eg=gP\), so \(e=gPg^{-1}\), where the symbol \(P\) on the right denotes the homogeneous algebra projection fixing the free subalgebra on \(U\) and killing words containing letters from \(W\). This also proves \(\operatorname{im}e\cong F_r\) and its dimension is \(r+r^2+r^3\).

**Step 2: Exact stabilizers.** Fix the degree-one projection \(P\). A \(g\in G\) commutes with \(P\) precisely when the higher-degree part of \(g(u)\), \(u\in U\), consists only of words entirely in \(U\), whereas the higher-degree part of \(g(w)\), \(w\in W\), consists only of words containing a letter from \(W\). There are respectively \(B(r)\) and \(B(n)-B(r)\) dimensions for each of the \(r\) and \(n-r\) inputs. Thus the number of lifts of this fixed projection is
\[
 \frac{|G|}{|C_G(P)|}=q^{r(B(n)-B(r))+(n-r)B(r)}.
\]
The number of rank-\(r\) idempotents on the \(n\)-space \(V\) is \({n\brack r}_q q^{r(n-r)}\), giving the stated total count.

To count embedded images for each fixed leading \(r\)-plane \(U\), use the orbit of the standard free subalgebra \(F(U)\) under \(G\). Its stabilizer consists of all shifts of generators in \(U\) by the \(B(r)\)-space of higher \(U\)-words, while generators in \(W\) may be shifted arbitrarily. Its orbit therefore has size \(q^{r(B(n)-B(r))}\). There are \({n\brack r}_q\) leading \(r\)-planes. Dividing the total map count by the image count shows that the number of retractions onto **each** such image is the constant \(q^{(n-r)(r+B(r))}\).

**Step 3: Cubic rank condensation.** The stratum weight is \(w_{n,r}={n\brack r}_q q^{r(B(n)-B(r))+(n-r)d(r)}\). For fixed \(q\), write \(w_{n,r}=c_{n,r}(q)q^{E_n(r)}\), with
\[
 c_{n,r}(q)=q^{-r(n-r)}{n\brack r}_q,\qquad
 1\le c_{n,r}(q)\le\left(\prod_{j\ge1}(1-q^{-j})\right)^{-1}.
\]
The indicated polynomial is obtained by expanding \(2r(n-r)+r(B(n)-B(r))+(n-r)B(r)\).

Uniformly for \(0\le t\le1\), \(n^{-4}E_n(nt)\to f(t)=t+t^3-2t^4\). Its derivative is \(f'(t)=1+3t^2-8t^3\), which has exactly one zero \(\alpha\) in \((0,1)\): it increases on \((0,1/4)\), then decreases, crosses zero once, and is negative at \(1\). Its second derivative at that zero is strictly negative. The derivative of \(E_n\) similarly has a unique zero in \((0,n)\) for large \(n\), because its second derivative initially increases then decreases and is negative near the unique critical point; its endpoint derivative signs are positive and negative. Denote this maximizing zero by \(x_n\). Standard polynomial expansion or the implicit-function theorem at the simple root gives \(x_n=\alpha n+O(1)\).

Choose a small fixed neighborhood of \(\alpha\). Within that neighborhood the second derivative of \(E_n\) is at most \(-c n^2\) for some fixed \(c>0\), once \(n\) is sufficiently large. Every integer outside the two bracketing integers for \(x_n\) but inside the neighborhood has weight at most \(q^{-c'n^2}\) times the larger bracketing weight, by strong concavity. Outside the neighborhood, the unique strict maximum of \(f\) gives a larger exponent gap of order \(n^4\). Since there are at most \(n+1\) terms and the factors \(c_{n,r}(q)\) are uniformly bounded above and below, the combined excluded probability is \(O_q(q^{-c_qn^2})\), after adjusting the positive constant. It follows that \(r_n/n\to\alpha\) in probability and hence \(d(r_n)/(n+n^2+n^3)\to\alpha^3\).

The rational-root theorem shows that \(8t^3-3t^2-1\) has no rational roots: any rational root would have numerator \(\pm1\) and denominator dividing \(8\), and direct substitution excludes them. Thus \(\alpha\) is irrational.

## Verification
A standalone script, `verify.py`, uses the structure constants \(e_i e_j=f_{ij}\), \(e_i f_{jk}=g_{ijk}\), \(f_{ij}e_k=-g_{ijk}\) to construct full algebra endomorphisms from generator images and test composition-idempotency without using the counting formula as its acceptance criterion. It exhausts all one-generator assignments over \(\mathbb F_3\) and \(\mathbb F_5\), and over \(\mathbb F_3\) it enumerates all degree-two choices for the canonical two-generator rank-one projection and solves the exact finite linear systems for the degree-three coefficients. It finds \(81\) admissible quadratic assignments, each with \(3^8\) cubic completions, giving \(3^{12}\) lifts of that fixed projection. A separate conjugacy test checks sample automorphisms and linear image ranks in dimensions two and three. Run `python verify.py` to reproduce the `VERIFY_OK` output. No finite check replaces the general orbit-stabilizer and asymptotic arguments.

## Relationship to prior work
Remm, *Anti-associative algebras* (first public preprint February 22, 2022, arXiv:2202.10812), Section 2.3, establishes the free graded algebra and its dimensions; this is an explicit starting premise, not a new result. Cerqua and Facchini, *Pre-Lie algebras, their multiplicative lattice, and idempotent endomorphisms* (first public preprint January 6, 2023, arXiv:2301.02627), Section 6, develop the relationship between idempotent endomorphisms and semidirect decompositions, but do not supply this specific finite-field enumeration. Earlier retraction enumerations for free two-step associative and truncated symmetric algebras are also structurally related; the current theorem uses a different free anti-associative algebra with a nonzero cubic layer and a new degree-four exponential-scale saddle point. The claimed new content is the exact image and map fibers and the cubic irrational condensation law, not the general identification of retractions with split objects.

## Limitations
The free-algebra basis proof and theorem require odd characteristic, and the probabilistic conclusions hold for fixed odd field order. The result concerns **embedded** algebra maps and images rather than isomorphism classes of abstract free algebras. The two-point statement is asymptotic and does not identify which of the two adjacent ranks dominates for each finite \(n\). Existing general free-object projection arguments may offer alternate proofs; publication priority remains subject to further literature verification, especially for presentations using operadic terminology.

## References
1. E. Remm, *Anti-associative algebras*, arXiv:2202.10812, first public February 22, 2022, Section 2.3. https://arxiv.org/abs/2202.10812
2. M. Cerqua and A. Facchini, *Pre-Lie algebras, their multiplicative lattice, and idempotent endomorphisms*, arXiv:2301.02627, first public January 6, 2023, Section 6. https://arxiv.org/abs/2301.02627
