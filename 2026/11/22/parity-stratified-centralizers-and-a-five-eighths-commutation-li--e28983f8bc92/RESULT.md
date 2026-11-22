# Parity-stratified centralizers and a five-eighths commutation limit in dihedral zero-Hecke monoids

## Finding
For every integer \(m\ge3\), the dihedral zero-Hecke monoid \(H_m=H_0(I_2(m))\) has a complete centralizer-size classification, as follows. The monoid consists of its identity \(1\), its longest absorbing element \(z\), and two alternating elements \(u_{a,s},u_{a,t}\) at each length \(1\le a<m\). Define \(C_m(x)=|\{y\in H_m:xy=yx\}|\).

If \(m=2k\) is even (\(k\ge2\)), then
\[
C_m(u_{a,\epsilon})=k+3\lceil a/2\rceil\qquad(1\le a<2k).
\]
The value \(k+3j\) occurs four times for each \(1\le j<k\), while the maximal centralizer size \(2m\) occurs four times: at \(1,z,u_{m-1,s},u_{m-1,t}\).

If \(m=2k+1\) is odd (\(k\ge1\)), then, for every \(1\le j\le k\),
\[
C_m(u_{2j-1,\epsilon})=k+3j-1,\qquad
C_m(u_{2j,\epsilon})=k+3j.
\]
Each of these sizes occurs twice; the value \(2m\) occurs twice, at \(1,z\), and nowhere else.

Consequently the number of **ordered commuting pairs** is
\[
N_m=\#\{(x,y)\in H_m^2:xy=yx\}=
\begin{cases}
\frac52m^2+3m,&m\text{ even},\\
\frac{5m^2+2m+1}{2},&m\text{ odd},
\end{cases}
\]
and the commutation probability for two independent uniform elements is
\[
\frac{N_m}{(2m)^2}=
\begin{cases}
\frac58+\frac{3}{4m},&m\text{ even},\\
\frac58+\frac{1}{4m}+\frac{1}{8m^2},&m\text{ odd}.
\end{cases}
\]
In particular, both parity subsequences approach exactly \(5/8\). This is a classification of **element centralizers in the monoid**, not a formula for the center of its monoid algebra.

## Assumptions and scope
The Coxeter system \(I_2(m)\) has two simple reflections \(s,t\) with braid length \(m\). The zero-Hecke monoid is defined by the idempotent relations \(\pi_s^2=\pi_s\), \(\pi_t^2=\pi_t\), and equality of the two alternating words of length \(m\). The elements \(u_{a,\epsilon}\) are alternating products of length \(a\), starting at \(\pi_\epsilon\). The two length-\(m\) words are a single element \(z\). Multiplication is the ordinary monoid (Demazure) product, not Coxeter group multiplication or multiplication of arbitrary linear combinations in an algebra. All assertions hold for every integer \(m\ge3\); no ground field is involved.

## Proof
**1. Normal forms and product law.** Every Coxeter group element of length strictly between zero and \(m\) has exactly one alternating reduced expression, specified by its first letter; there are two per length, while the identity and longest element are unique. The zero-Hecke monoid has the same normal forms. A right multiplication by a generator preserves an element when that generator is its right descent, and otherwise increases its length by one, up to the absorbing longest element. Hence for \(1\le a,b<m\), if \(\delta\) equals one when the final letter of \(u_{a,\epsilon}\) equals the initial letter \(\eta\) of \(u_{b,\eta}\), and equals zero otherwise, then
\[
u_{a,\epsilon}u_{b,\eta}=
\begin{cases}
u_{a+b-\delta,\epsilon},&a+b-\delta<m,\\z,&a+b-\delta\ge m.
\end{cases}
\]
The same rule, with \(a,\epsilon\) and \(b,\eta\) interchanged, gives the reverse product. The identity commutes with every element, as does \(z\).

**2. Complete commutation predicate.** The last letter of an alternating word equals its first letter exactly when its length is odd. Thus for two nonboundary elements, they commute precisely in one of these cases:

- They have the same first letter and their lengths have the same parity (then both products have the same unsaturated length and first letter, or both are \(z\)).
- Their first letters differ, both lengths are odd, and \(a+b\ge m\) (both products saturate).
- They are not covered by the preceding cases and \(a+b\ge m+1\) (both products saturate).

These alternatives are mutually compatible and exhaustive. In particular, unequal first letters cannot produce equal nonlongest elements.

**3. Centralizer count for odd \(m\).** Put \(m=2k+1\). There are \(k\) odd and \(k\) even nonboundary lengths. Fix a first letter. For length \(a=2j-1\), compatible partners with the same first letter number \(k+j-1\) (all odd lengths and the \(j-1\) sufficiently long even lengths); partners with the opposite first letter number \(2j-2\). Adding the two boundary elements gives \(2+k+j-1+2j-2=k+3j-1\). For \(a=2j\), same-first partners number \(k+j-1\), opposite-first partners number \(2j-1\), and adding the boundaries gives \(k+3j\). None reaches \(2m\), so only \(1,z\) are central.

**4. Centralizer count for even \(m\).** Put \(m=2k\). There are \(k\) odd and \(k-1\) even nonboundary lengths. For \(a=2j-1\), compatible same-first partners number \(k+j-1\), opposite-first partners number \(2j-1\), yielding \(k+3j\) after the two boundaries. For \(a=2j\), with \(1\le j<k\), same-first partners number \(k+j-1\), opposite-first partners number \(2j-1\), yielding the same \(k+3j\). At \(a=2k-1\) this equals \(4k=2m\), so precisely the two length-\(m-1\) elements join the center.

**5. Ordered pair enumeration.** Summing \(C_m(x)\) over \(x\in H_m\) gives the ordered count. In the even case, the spectrum from step 4 gives
\[
4\sum_{j=1}^{k-1}(k+3j)+4(4k)=10k^2+6k.
\]
In the odd case, the spectrum from step 3 gives
\[
2\sum_{j=1}^{k}(2k+6j-1)+2(4k+2)=10k^2+12k+4.
\]
Substituting \(m=2k\) or \(m=2k+1\), and dividing by the monoid cardinality squared \((2m)^2\), yields the displayed formulas and their common limit. No limiting approximation or finite sample is used in this proof.

## Verification
A standalone Python 3 checker (`dihedral_independent_check.py`) independently constructs each dihedral Coxeter group from the group law \((a,e)(b,f)=(a+(-1)^e b,e\oplus f)\), finds shortest group words by breadth-first search, and computes zero-Hecke products by length-ascent operations, rather than by the alternating-word product formula in the proof. It exhaustively checks all pairs, element centralizers, centers, and ordered commuting-pair totals for every \(3\le m\le64\); the captured output (`dihedral_independent_check.txt`) ends in `PASS`. These finite computations are reproducibility checks only; steps 1–5 prove the theorem for all \(m\ge3\).

## Relationship to prior work
Denton, Hivert, Schilling and Thiéry, *On the representation theory of finite J-trivial monoids* (first posted 2010-10-17), §2.4, gives the standard zero-Hecke presentation and monoid/Coxeter indexing, while §3.7.1 develops representation-theoretic quivers and a table of radical-filtration polynomials; it does not state prescribed element-centralizer sizes or a commuting-pair density. He, *Centers and Cocenters of 0-Hecke Algebras* (first posted 2015-02-07), proves bases of the **algebraic** center and cocenter, distinct from the complete centralizer-size spectrum of individual monoid basis elements. An earlier power-fiber calculation for these same dihedral monoids determines a different word map and does not imply the commutation predicate or centralizer-size distribution. The claimed contribution is only the complete monoid commutation predicate, centralizer spectrum, and resulting parity-dependent pair count and asymptotic density, not the normal forms, Demazure multiplication, or algebraic center results.

## Limitations
This result treats only finite dihedral Coxeter type \(I_2(m)\), not higher-rank or affine zero-Hecke monoids. A universal formula for centralizers in all finite \(\mathcal J\)-trivial monoids is not claimed. The sources inspected here did not yield an equivalent published centralizer enumeration; that search is not a proof of historical priority, and unlocated older dihedral monoid tables remain possible. The stand-alone checker confirms finitely many cases only and is not a substitute for the proof.

## References
- T. Denton, F. Hivert, A. Schilling, N. M. Thiéry, *On the representation theory of finite J-trivial monoids*, arXiv:1010.3455, first version 2010-10-17, https://arxiv.org/html/1010.3455v3 (especially §§2.4 and 3.7.1).
- X. He, *Centers and Cocenters of 0-Hecke Algebras*, arXiv:1502.02183, first version 2015-02-07, https://arxiv.org/pdf/1502.02183 (especially §§4–5).
- SageMath monoid documentation, *Hecke Monoids*, https://doc.sagemath.org/html/en/reference/monoids/sage/monoids/hecke_monoid.html (computational definition; no centralizer table asserted).
