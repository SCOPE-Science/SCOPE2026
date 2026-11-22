# Nine Cartier-square-zero parameters in the characteristic-seven cyclic-quintic genus-four family

## Finding

Let \(k=\overline{\mathbb F}_7\). For every \(t\in k\setminus\{0,1\}\), let \(X_t\) be the smooth projective model of the tame cyclic cover
\[
y^5=x(x-1)(x-t).
\]
It has genus \(4\). Its Cartier operator \(\mathcal C\) on regular differentials satisfies \(\mathcal C^3=0\) and \(\operatorname{rank}\mathcal C=2\) throughout the entire smooth family. Thus the Jacobian always has geometric \(7\)-rank zero and \(a\)-number two. The second Cartier power vanishes precisely at nine distinct parameter values, namely the roots of
\[
P(t)=t^9-t^8+t^7+2t^5+2t^4+t^2-t+1\in\mathbb F_7[t].
\]
At these parameters the complete ranks of \((\mathrm{id},\mathcal C,\mathcal C^2,\ldots)\) are \((4,2,0,0,\ldots)\); at all other parameters they are \((4,2,1,0,0,\ldots)\). Explicitly,
\[
P(t)=(t-2)(t+1)(t+3)(t^2-3t+1)(t^2-t-1)(t^2+t-1).
\]
The three linear roots lie in \(\mathbb F_7\), and the six quadratic roots lie in \(\mathbb F_{49}\setminus\mathbb F_7\); all nine are simple and avoid \(0\) and \(1\).

If \(j(t)=256(t^2-t+1)^3/[t^2(t-1)^2]\) is the classical Legendre cross-ratio invariant of the four branch points, then the Cartier-square-zero locus is **exactly**
\[
\mathcal C^2=0\quad\Longleftrightarrow\quad j(t)\in\{4,6\}\subset\mathbb F_7.
\]
The nine ordered parameters constitute exactly two orbits under reordering the three simple branch points, with orbit sizes six and three; hence there are exactly two corresponding unordered branch configurations in this family.

## Assumptions and scope

The characteristic is exactly \(7\); \(k\) is algebraically closed and therefore perfect. The base parameter excludes \(0,1\), ensuring four distinct branch points including infinity. The ramification exponents of this degree-five cyclic cover are \((1,1,1,2)\). The genus formula \(2g-2=5(-2)+4(5-1)=6\) gives \(g=4\). The claim concerns the Cartier action on \(H^0(X_t,\Omega^1)\) and the marked family. It does not assert a complete Newton-polygon or Ekedahl–Oort classification beyond these Cartier-power ranks, nor does it classify unmarked curves with unrelated automorphisms.

## Proof

Write \(f=x(x-1)(x-t)\). At the unique point above infinity the pole orders of \(x,y,dx\) are \(5,3,6\); at each finite branch point \(dx\) vanishes to order four while \(y\) has a simple zero. Consequently, the following are all regular, and they form a basis because the genus is four:
\[
\omega_2=dx/y^2,\quad \omega_3=dx/y^3,\quad
\omega_{40}=dx/y^4,\quad\omega_{41}=x\,dx/y^4.
\]
For each \(1\le j\le4\), take the unique \(1\le q\le4\) with \(7q\equiv j\pmod5\). Then \(\omega=x^i dx/y^j=(x^i f^{(7q-j)/5}dx)/y^{7q}\), and Cartier extracts the terms of degree congruent to \(6\pmod7\) from the numerator, taking seventh roots of coefficients. Direct expansion over \(\mathbb F_7[t]\) gives
\[
A=[x^6]f^5=-5t^4(t+1),\quad
B=[x^{13}]f^5=5(t+2)(2t+1),\quad
V=[x^5]f^2=-2(t+1).
\]
The only nonzero basis images are
\[
\mathcal C(\omega_3)=A^{1/7}\omega_{40}+B^{1/7}\omega_{41},\quad
\mathcal C(\omega_{40})=\omega_2,\quad
\mathcal C(\omega_{41})=V^{1/7}\omega_2;
\qquad \mathcal C(\omega_2)=0.
\]
Here the coefficient \([x^6]f^2\) equals one. Because \(A,B\) cannot vanish simultaneously for \(t\notin\{0,1\}\), the image of \(\mathcal C\) has dimension exactly two. Every image of \(\mathcal C^2\) lies in \(k\omega_2\), and semilinearity gives
\[
\mathcal C^2(\omega_3)=\bigl(A+B V^7\bigr)^{1/49}\omega_2,\quad
\mathcal C^2(\omega_2)=\mathcal C^2(\omega_{40})=\mathcal C^2(\omega_{41})=0.
\]
Thus \(\mathcal C^3=0\) identically and \(\mathcal C^2=0\) precisely when \(P(t)=A+B V^7=0\). Expanding yields the displayed degree-nine polynomial and its factorization. Its three degree-two factors have discriminant \(5\), which is a nonsquare in \(\mathbb F_7\), and the three degree-one factors are pairwise distinct. Values \(t=0,1\) are not roots. This proves the rank profiles and exact cardinalities over the algebraic closure.

For the branch invariant let \(U(t)=4(t^2-t+1)^3\) and \(D(t)=t^2(t-1)^2\) in \(\mathbb F_7[t]\); \(256=4\) in characteristic seven. Put \(L=(t-2)(t+1)(t+3)\) and \(Q=(t^2-3t+1)(t^2-t-1)(t^2+t-1)\). Direct identities modulo seven are
\[
P=LQ,\qquad U-4D=-3Q,\qquad U-6D=-3L^2.
\]
Since \(D\ne0\) on the smooth base, these identities prove \(P=0\iff j\in\{4,6\}\). The standard six anharmonic transformations partition the roots into one orbit of size three at \(j=6\) and one orbit of size six at \(j=4\). In this cover family the order-two branch exponent at infinity is distinguished, so these orbits are exactly the unordered configurations of the three remaining simple branch points.

## Verification

The accompanying standalone script `verify_cartier_char7.py` implements exact arithmetic in \(\mathbb F_{49}=\mathbb F_7[z]/(z^2+1)\), derives the Cartier coefficients anew by polynomial convolution, builds the semilinear Cartier matrix, and computes the ranks of its first three powers for every one of the \(47\) smooth parameters in \(\mathbb F_{49}\). It confirms exactly nine square-zero parameters, their splitting into \(j=4\) (six) and \(j=6\) (three), and rank profiles \((2,0,0)\) or \((2,1,0)\). This finite check is corroborative; the displayed symbolic identities and degree-nine factorization establish the infinite-field assertion.

Run with `python3 verify_cartier_char7.py`; expected terminal line is `CARTIER_CHAR7_49_EXACT_OK 47 smooth parameters; 9 square-zero; j4=6, j6=3`.

## Relationship to prior work

Elkin develops regular-differential bases and a Cartier-operator method for general cyclic covers, which provide the known machinery used here; no characteristic-seven nine-root calculation appears in the inspected sections. Moonen identifies the special one-dimensional cyclic-cover families; this cover is the genus-four \(M[11]\) family. Li–Mantovan–Pries–Tang determine the generic \(\mu\)-ordinary Dieudonné module and candidate basic Newton polygon for that family at primes congruent to two or three modulo five, but do not list these nine characteristic-seven parameter values or the two precise cross-ratio invariants. Cavalieri–Pries identify the same family while deriving mass formulas under the incompatible condition \(p\equiv1\pmod5\). Streng's explicit constructions concern different labelled special families. A related published Cartier-square-zero calculation in characteristic three is not an implication of this characteristic-seven classification, whose exceptional divisor has degree nine rather than one.

## Limitations

Full historical priority is not certified: a computational table in unindexed notes or a specialization of a more general unpublished algorithm could coincide with this exact parameter classification. The computation of a Cartier-power filtration is not by itself a proof of a particular Newton polygon at the exceptional fibers. Branch-parameter equivalence is asserted only for the marked cyclic-cover model, not for arbitrary isomorphisms of the underlying curves. Finite-field enumeration supplements but never replaces the symbolic proof.

## References

1. Arsen Elkin, *The Rank of the Cartier operator on cyclic covers of the projective line*, arXiv:0708.0431, initial public version 2007-08-02. https://arxiv.org/abs/0708.0431
2. Ben Moonen, *Special subvarieties arising from families of cyclic covers of the projective line*, arXiv:1006.3400, initial public version 2010-06-17. https://arxiv.org/abs/1006.3400
3. Wanlin Li, Elena Mantovan, Rachel Pries, Yunqing Tang, *Newton polygons arising for special families of cyclic covers of the projective line*, arXiv:1805.06914 (2018). https://arxiv.org/abs/1805.06914
4. Renzo Cavalieri, Rachel Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891 (2023). https://arxiv.org/abs/2308.14891
5. Marco Streng, *Explicit supersingular cyclic curves*, arXiv:2501.14902 (2025). https://arxiv.org/abs/2501.14902
