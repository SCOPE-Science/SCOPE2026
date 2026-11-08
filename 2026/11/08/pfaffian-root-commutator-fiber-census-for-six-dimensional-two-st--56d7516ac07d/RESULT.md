# Pfaffian-root commutator-fiber census for six-dimensional two-step Lie algebras with two-dimensional derived ideal

## Finding
Fix an arbitrary finite field \(k=\mathbb F_q\). The two-step Lie brackets considered here are the **entire family** of surjective alternating maps \(\beta:\bigwedge^2 V\twoheadrightarrow Z\), where \(\dim_k V=4\) and \(\dim_k Z=2\), on \(L=V\oplus Z\) with \([v+z,w+z']=\beta(v,w)\). This condition says that the derived subalgebra is exactly \(Z\), without requiring the full center to equal \(Z\).

Let \(\omega_\lambda=\lambda\circ\beta\) for \(\lambda\in Z^*\). In any basis of \(V\), the Pfaffian \(Q(\lambda)=\operatorname{Pf}(\omega_\lambda)\) is a homogeneous binary quadratic on \(Z^*\). Set
\[
 r=\#\{[\lambda]\in\mathbb P(Z^*):Q(\lambda)=0\}\in\{0,1,2,q+1\}.
\]
For a nonzero \(c\in Z\), put \(s(c)=1\) if its one-dimensional annihilator \(\{\lambda\in Z^*: \lambda(c)=0\}\) is a projective root of \(Q\), and put \(s(c)=0\) otherwise. Define \(N(c)=\#\{(X,Y)\in L^2:[X,Y]=c\}\). Then
\[
\boxed{N(0)=q^4\left[q^6+q^4-q^2+(q^4-q^2)r(q-1)\right],}
\]
\[
\boxed{N(c)=q^4\left[q^6-q^2+(q^4-q^2)(q s(c)-r)\right]\quad(c\ne0).}
\]
The nonzero fibers have two possible sizes, with \(r(q-1)\) targets having \(s(c)=1\), and \(q^2-1-r(q-1)\) targets having \(s(c)=0\). The size gap is \(q^5(q^4-q^2)\). This formula remains valid if one of these two populations is empty, as occurs when \(r=0\) or \(r=q+1\). In particular, it is valid over characteristic two.

## Assumptions and scope
All finite fields and every surjective alternating bracket on the specified vector spaces are included. In characteristic two, alternating means \(\beta(v,v)=0\), not merely skew-symmetry. A different basis of \(V\) multiplies the Pfaffian by a nonzero scalar, and a basis change in \(Z\) linearly changes its variables. Therefore the root set and its annihilator lines are intrinsic to the bracket. This is a census of *ordered labeled pairs*, not an isomorphism classification of Lie algebras.

## Proof
For a nontrivial additive character \(\psi:k\to\mathbb C^\times\), define \(F(c)=\#\{(v,w)\in V^2:\beta(v,w)=c\}\). The four independent central coordinates in an ordered pair \((X,Y)\in L^2\) yield \(N(c)=q^4 F(c)\).

**Step 1: alternating-rank dichotomy.** Surjectivity of \(\beta\) implies that \(\omega_\lambda\ne0\) for every \(\lambda\ne0\). The rank of such an alternating form on a four-space is either two or four in every characteristic. With matrix entries \(a_{ij}\), its Pfaffian is \(a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}\), and \(\det(\omega_\lambda)=Q(\lambda)^2\). Consequently \(\operatorname{rank}(\omega_\lambda)=2\) exactly when \(Q(\lambda)=0\), and equals four otherwise. Because \(Q\) is a binary quadratic (possibly identically zero), its number of projective zeros is precisely one of \(0,1,2,q+1\).

**Step 2: Fourier transform of the bracket pushforward.** Character orthogonality gives
\[
F(c)=\frac{1}{q^2}\sum_{\lambda\in Z^*}\psi(-\lambda(c))\sum_{v,w\in V}\psi(\omega_\lambda(v,w)).
\]
For a bilinear form \(B\) on a four-space with matrix rank \(d\), summation over \(w\) annihilates the contribution of every \(v\) outside its left radical, so \(\sum_{v,w}\psi(B(v,w))=q^{8-d}\). The zero functional contributes \(q^8\). The nonzero rank-four functionals contribute \(q^4\) apiece; each rank-two functional contributes \(q^6\). Hence
\[
F(c)=q^{-2}\bigg(q^8+q^4\sum_{\lambda\ne0}\psi(-\lambda(c))+(q^6-q^4)\sum_{\substack{\lambda\ne0\\Q(\lambda)=0}}\psi(-\lambda(c))\bigg).
\]

**Step 3: evaluating the two character sums.** For \(c=0\), the first sum is \(q^2-1\) and the second is \(r(q-1)\). For \(c\ne0\), the first sum is \(-1\). The roots comprise \(r\) projective lines; summing \(\psi(-t\lambda(c))\) over \(t\in k^\times\) contributes \(q-1\) when \(\lambda(c)=0\), and \(-1\) otherwise. There is exactly one projective line in \(Z^*\) annihilating nonzero \(c\), hence the second sum equals \(q s(c)-r\). Substitution gives the two asserted formulas and the claimed target populations.

**Consistency.** Summing over \(c\in Z\), the Fourier-orthogonality identity gives \(\sum_cF(c)=q^8\), and hence \(\sum_c N(c)=q^{12}=\#L^2\). Each formula is exact; no limiting or genericity assumption is used.

## Verification
Run `python3 verify_pfaffian_fibers.py` using Python 3.8 or later; no third-party modules are needed. The checker independently enumerates all \(q^8\) pairs of four-vectors and all \(q^2\) target fibers for explicit alternating-pencil families over prime fields of orders two, three, and five; it computes the rank of each nonzero pencil matrix using finite-field elimination rather than computing Pfaffians. The tested pencils include identically zero, repeated-root, split-root, and irreducible binary quadratics. There are eleven tested field/pencil configurations, and every individual fiber agrees with the formula. The exact expected output is provided in `pfaffian_output.txt`, ending in `PFAFFIAN_PENCIL_COMPLETE_BRACKET_FIBERS_PASS`. This finite check is supportive evidence, not an exhaustive enumeration of all surjective brackets or of all finite fields; the proof above supplies the unrestricted result.

## Relationship to prior work
Cicalò, de Graaf and Schneider classify six-dimensional nilpotent Lie algebras over arbitrary fields and, in particular, two-planes of alternating forms on a four-space, including the characteristic-two quadratic-form distinctions. The classification and its standard Pfaffian/Klein geometry are not new. Their Theorem 4.4 and Section 5 concern algebra isomorphism orbits rather than the number of *labeled ordered pairs* attaining each individual bracket output. The present result determines that complete target-by-target population, including the exact alignment of enhanced fibers with projective Pfaffian roots. De Graaf's earlier characteristic-not-two classification and classical additive-character orthogonality are also antecedents; neither is claimed as new. More general theorems on word-map distributions or representation zeta functions could subsume the count, so historical priority is provisional.

## Limitations
This result applies to six-dimensional two-step Lie algebras with a four-dimensional chosen complement and a two-dimensional derived ideal. It does not classify the Lie algebras up to isomorphism, give fiber sizes for arbitrary higher-dimensional pencils, or count automorphism-orbits of solutions. The classification of these Lie algebras and the underlying Fourier transform method are established mathematics. Independent audit and exhaustive historical-priority checking have not been performed.

## References
1. S. Cicalò, W. A. de Graaf, and C. Schneider, *Six-dimensional nilpotent Lie algebras*, arXiv:1011.0361 (first public 2010-11-01), especially Theorem 4.4 and Section 5. https://arxiv.org/abs/1011.0361
2. W. A. de Graaf, *Classification of 6-dimensional nilpotent Lie algebras over fields of characteristic not 2*, arXiv:math/0511668 (first public 2005-11-28). https://arxiv.org/abs/math/0511668
3. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, Annals of Combinatorics 22 (2018), 295–316, DOI:10.1007/s00026-018-0390-4. A separate matrix-Lie-algebra commuting-pair literature, not an assertion of coverage here.
