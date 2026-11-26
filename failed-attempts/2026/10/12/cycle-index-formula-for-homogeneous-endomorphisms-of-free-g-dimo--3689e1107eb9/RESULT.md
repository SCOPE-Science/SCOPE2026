# Cycle-index formula for homogeneous endomorphisms of free g-dimonoids
## Finding
Let \(D_r=XT_a^b(1)\) be the free g-dimonoid on a finite generator set \(X\) with \(|X|=r\ge1\). For \(k\ge1\), let \(E_{r,k}\) consist of the endomorphisms that send every free generator to an element whose \(X\)-word has length exactly \(k\).

For a partition
\[
\lambda=1^{m_1}2^{m_2}\cdots\vdash r,
\]
put
\[
z_\lambda=\prod_{d\ge1}d^{m_d}m_d!,\qquad
c(\lambda)=\sum_{d\ge1}m_d,
\]
and
\[
F_d(\lambda)=\sum_{e\mid d}e m_e.
\]
Then the exact number of conjugacy classes of \(E_{r,k}\) under the natural conjugation action of \(\operatorname{Aut}(D_r)\) is
\[
\boxed{
N_{r,k}=\sum_{\lambda\vdash r}
\frac{2^{(k-1)c(\lambda)}}{z_\lambda}
\prod_{d\ge1}F_d(\lambda)^{k m_d}
}.
\]

At \(k=1\), the slice \(E_{r,1}\) is the full transformation monoid on \(X\), so \(N_{r,1}\) is exactly the number of unlabeled functional digraphs on \(r\) vertices. The first values are
\[
1,3,7,19,47,130
\]
for \(r=1,2,3,4,5,6\). At \(k=2\), the corresponding values are
\[
2,36,996,44360,2629684,195117636.
\]

For each fixed \(r\), the identity permutation gives the dominant Burnside term. Consequently
\[
N_{r,k}=\frac{(2^{k-1}r^k)^r}{r!}
\left(1+O_r\!\left((2^{k-1}r^k)^{-1}\right)\right)
\quad(k\to\infty).
\]

## Assumptions and scope
A g-dimonoid is a set with two associative binary operations satisfying the two bar identities. The free object used here is the explicit model
\[
D_r=\{(w,u):w\in F[X],\ u\in\{a,b\}^*,\ |w|-|u|=1\}.
\]
The length of \((w,u)\) means \(|w|\). Thus its length-\(k\) layer contains
\[
2^{k-1}r^k
\]
elements.

The action considered is conjugation by the full algebra automorphism group of the free g-dimonoid. The recent structural source proves
\[
\operatorname{Aut}(D_r)\cong S_r,
\]
with a permutation of generators acting by relabeling the letters of \(w\) and leaving the \(a,b\)-word \(u\) unchanged.

## Proof
Because \(D_r\) is free on \(X\), an endomorphism is uniquely determined by the images of the \(r\) generators. Hence
\[
|E_{r,k}|=(2^{k-1}r^k)^r.
\]

Fix \(\sigma\in S_r\), and write \(m_d(\sigma)\) for the number of \(d\)-cycles of \(\sigma\). An endomorphism \(\varphi\in E_{r,k}\) is fixed by conjugation with \(\sigma\) exactly when
\[
\varphi\sigma=\sigma\varphi.
\]
Consider one \(d\)-cycle of generators. Once the image of one generator on that cycle is chosen, equivariance forces the images of all other generators on the cycle. Returning after \(d\) steps is consistent exactly when the chosen image is fixed by \(\sigma^d\).

The number of generators fixed by \(\sigma^d\) is
\[
F_d(\sigma)=\sum_{e\mid d}e m_e(\sigma).
\]
A length-\(k\) element is fixed by \(\sigma^d\) precisely when each of its \(k\) generator letters is fixed by \(\sigma^d\); its \(k-1\) letters from \(\{a,b\}\) are unaffected. Therefore
\[
|\operatorname{Fix}_{D_{r,k}}(\sigma^d)|
=2^{k-1}F_d(\sigma)^k.
\]
It follows that
\[
|\operatorname{Fix}_{E_{r,k}}(\sigma)|
=\prod_{d\ge1}
\left(2^{k-1}F_d(\sigma)^k\right)^{m_d(\sigma)}.
\]
Burnside's lemma now gives
\[
N_{r,k}=\frac1{r!}\sum_{\sigma\in S_r}
\prod_{d\ge1}
\left(2^{k-1}F_d(\sigma)^k\right)^{m_d(\sigma)}.
\]
Grouping permutations by cycle type \(\lambda\), whose conjugacy class has size \(r!/z_\lambda\), yields the displayed partition formula.

For \(k=1\), a generator image is just another generator, so \(E_{r,1}\) is the full transformation monoid on \(X\), and conjugation by \(S_r\) is exactly relabeling of functional digraphs.

For the asymptotic, the identity term is \((2^{k-1}r^k)^r\). Every nonidentity permutation has at most \(r-1\) cycles and satisfies \(F_d(\sigma)\le r\). Its fixed-point contribution is therefore at most
\[
(2^{k-1}r^k)^{r-1}.
\]
There are only \(r!-1\) such permutations, proving the stated fixed-\(r\) error term.

## Verification
The accompanying checker evaluates the partition formula exactly using rational arithmetic and independently enumerates conjugation orbits for
\[
1\le r\le3,\qquad 1\le k\le2.
\]
It obtains
\[
N_{1,1}=1,\ N_{1,2}=2,\ N_{2,1}=3,\ N_{2,2}=36,\ N_{3,1}=7,\ N_{3,2}=996,
\]
and terminates with `VERIFY_OK`. These finite tests are regression checks only; the theorem for arbitrary \(r\) and \(k\) is the symbolic Burnside argument above.

## Relationship to prior work
Zhuchok and Zhuchok give the explicit free g-dimonoid model, prove that its full automorphism group is the symmetric group on the free generators, and use the endomorphism semigroup to recover the rank of the free object. Their article does not state an orbit count for homogeneous endomorphisms, a cycle-index formula, or the functional-digraph specialization.

Earlier work on free commutative g-dimonoids determines isomorphisms and automorphisms of their endomorphism semigroups; it concerns a different commutative free object and a different action. It does not imply the formula above.

The case \(k=1\) recovers the familiar conjugacy problem for finite transformations, but the factors \(2^{k-1}\) and the powers \(F_d(\lambda)^k\) encode the noncommutative g-dimonoid layers for every \(k\ge2\).

## Limitations
The theorem counts conjugacy classes only inside the homogeneous slice where all generator images have the same prescribed length. It does not classify individual orbit representatives, stabilizers, or conjugacy in the entire infinite endomorphism semigroup.

The primary 2026 article was inspected in full open-access HTML. An older construction paper for free g-dimonoids was located through the bibliography and search index but was not needed for the proof because the 2026 article reproduces the normal form and automorphism action. An equivalent orbit formula hidden in older semigroup-enumeration terminology remains a residual originality risk.

## References
1. A. V. Zhuchok and Y. V. Zhuchok, “Free g-dimonoids are determined by their endomorphism semigroups,” *Archiv der Mathematik* 127 (2026), 233–240, DOI 10.1007/s00013-026-02280-9.
2. Y. V. Zhuchok, “Automorphisms of the endomorphism semigroup of a free commutative g-dimonoid,” *Algebra and Discrete Mathematics* 21 (2016), no. 2.
3. Y. V. Zhuchok, “On one class of algebras,” *Algebra and Discrete Mathematics* 18 (2014), no. 2, 306–320.
