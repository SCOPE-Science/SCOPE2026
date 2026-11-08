# Exact conductor spectrum in a squarefree family of Abhyankar–Moh semigroups

## Finding
Let \(q\ge 7\) be a prime satisfying \(q\equiv1\pmod6\), and let \(n=3q\). Write \(\mathcal C(n)\) for the set of conductors of all Abhyankar–Moh numerical semigroups of degree \(n\), including the semigroup \(\mathbb N\) of conductor zero. Then
\[
\mathcal C(3q)=\{0,3q-1\}\;\cup\;
\big\{c\in\mathbb Z:6q\le c\le(3q-1)(3q-2),\quad c\equiv0\ \text{or}\ 2\pmod6\big\}.
\]
In particular, \(\lvert\mathcal C(3q)\rvert=3q^2-5q+4\). Thus this infinite family of odd, non-prime-power degrees has exactly two isolated conductor values below \(6q\), and thereafter exactly the two specified residue classes modulo six up to the sharp global upper endpoint.

## Assumptions and scope
A numerical semigroup is a cofinite additive submonoid of \(\mathbb N\). Its conductor is the least \(c\ge0\) with \(c+\mathbb N\subseteq S\). A characteristic sequence \((v_0,\ldots,v_h)\) has strictly decreasing gcds \(e_i=\gcd(v_0,\ldots,v_i)\), with \(e_0=v_0\) and \(e_h=1\), and satisfies \(e_{i-1}v_i<e_iv_{i+1}\) for \(1\le i<h\). It generates an Abhyankar–Moh semigroup of degree \(n=v_0>1\) if \(e_{h-1}v_h<n^2\). These are the abstract semigroups of the cited literature, not a claim that every semigroup is realized by a particular plane curve. Only primes \(q\equiv1\pmod6\) with \(q\ge7\) are asserted.

For any such characteristic sequence, the standard conductor identity is
\[
c(S)=\sum_{i=1}^h\left(\frac{e_{i-1}}{e_i}-1\right)v_i-n+1.
\]
The characterization of admissible characteristic sequences and this identity appear in García Barroso et al. [1, Proposition 4 and equation (10)]. We use them as explicitly cited inputs, while proving the new uniform spectrum classification.

## Proof
**1. Exhaustion of possible gcd chains.** Since \(n=3q\) is a product of two distinct primes, every strict divisor chain from \(n\) to \(1\) has length at most two. Every characteristic sequence is therefore either \((n,a)\) with \(1\le a<n\), \(\gcd(n,a)=1\), or \((n,a,b)\) with \(d:=\gcd(n,a)\in\{3,q\}\) and \(\gcd(d,b)=1\). For a triple, writing \(a=dk\), the characteristic and Abhyankar–Moh inequalities become
\[
1\le k\le n/d-1,\quad \gcd(n/d,k)=1,\quad nk<b<n^2/d,\quad \gcd(d,b)=1.
\]
These are necessary and sufficient for this length-two gcd chain.

**2. The two-generator branch.** Here
\[
c(\langle n,a\rangle)=(n-1)(a-1).
\]
The choices \(a=1\) and \(a=2\) give \(0\) and \(n-1=3q-1\), respectively. The choice \(a=3\) is forbidden since \(3\mid n\); every other allowed \(a\) is at least four and produces a conductor at least \(3(n-1)\ge6q\). Since \(n-1\equiv2\pmod6\), and \(a\) is coprime to three, every two-generator conductor is congruent to zero or two modulo six. All are at most \((n-1)(n-2)\).

**3. The divisor \(d=q\).** We have \(a=qk\), \(k\in\{1,2\}\), and \(3qk<b<9q\), \(q\nmid b\). The conductor formula reduces to
\[
c=2qk+(q-1)b-3q+1.
\]
Because \(q\equiv1\pmod6\), this is congruent to \(2k-2\pmod6\), hence zero or two. Its minimum for \(k=1\) is \(3q(q-1)\ge6q\). The global upper bound in [2, Theorem 1] also applies, or one may maximize the formula at \(k=2\), \(b=9q-1\), obtaining exactly \((3q-1)(3q-2)\). This branch contributes no conductor outside the proposed spectrum.

**4. The divisor \(d=3\), including constructive sufficiency.** Now \(a=3k\), \(1\le k\le q-1\), and
\[
3qk<b<3q^2,\qquad 3\nmid b.
\]
The conductor formula is
\[
c=3(q-1)k+2b-3q+1.
\]
For each fixed \(k\), the smallest and largest permitted \(b\) are \(3qk+1\) and \(3q^2-1\). Therefore the corresponding conductors are precisely the integers congruent to zero or two modulo six in the closed interval \([L_k,U_k]\), where
\[
L_k=3(3q-1)k-3q+3,\qquad
U_k=3(q-1)k+6q^2-3q-1.
\]
Indeed, the admissible \(b\)'s occur as consecutive residues one or two modulo three; multiplying by two in the conductor formula gives successive residues zero and two modulo six, with no others. The endpoints satisfy \(L_k\equiv0\pmod6\) and \(U_k\equiv2\pmod6\). In particular,
\[
L_1=6q,\qquad U_{q-1}=(3q-1)(3q-2).
\]
Moreover, for every \(1\le k\le q-2\),
\[
U_k-L_{k+1}=6q^2-6qk-9q-1\ge3q-1>0.
\]
The intervals thus overlap and their union covers every number congruent to zero or two modulo six between \(6q\) and \((3q-1)(3q-2)\). Conversely every conductor from this branch has exactly one of those residue classes. Combining steps 2–4 establishes the stated equality.

**5. Cardinality.** The upper endpoint is \(9q^2-9q+2\). The integers in the large interval with permitted residues are paired as \(6q+6j\) and \(6q+6j+2\), for \(0\le j\le q(3q-5)/2\). There are \(q(3q-5)+2\) of them; adding the two exceptional conductors gives \(3q^2-5q+4\). This completes the proof.

## Verification
The accompanying stand-alone script `verify.py` independently enumerates every admissible characteristic sequence in degrees \(21,39,57,93,111\), computes their conductor using the characteristic-sequence identity, and compares the entire conductor sets to the displayed formula. It cross-checks all sequences at degrees \(21,39\), and a deterministic sample at degree \(57\), using an independently coded shortest-path Apéry-set conductor computation. Each tested degree matches exactly, with spectrum sizes \(116,446,992,2732,3926\). These finite checks are supplementary: the proof above is uniform in all admitted primes.

The hypothesis \(q\equiv1\pmod6\) is substantial. For the excluded prime \(q=5\), the admissible sequence \((15,5,17)\) has conductor \(64\equiv4\pmod6\). The verifier independently confirms this conductor.

## Relationship to prior work
García Barroso, García-García, Santana Sánchez and Vigneron-Tenorio [1] prove a complete interval theorem for **even** degrees, a separate description for odd **prime-power** degrees, and give a general per-degree enumeration algorithm based on characteristic sequences. They expressly ask to characterize conductors for odd degrees. Their algorithm could in principle compute each individual \(3q\) case, but their inspected statement does not give the simultaneous uniform residue-class answer, its proof of interval filling, or its closed conductor count for this odd squarefree family. The present argument applies their Proposition 4 and conductor identity rather than claiming those ingredients as new. Barrolleta, García Barroso and Płoski [2] prove the general maximum-conductor bound, which here supplies the right-hand endpoint but not the full intermediate spectrum. The comparison is a scientific literature assessment, not a claim that database searches prove publication priority.

## Limitations
No classification is asserted for arbitrary odd degrees, for \(q\equiv5\pmod6\), or for all primes beyond the displayed family. The result classifies conductor **values**, not the isomorphism types or multiplicities of numerical semigroups realizing each value. The proof relies on established characteristic-sequence and conductor results [1]. A mathematically equivalent observation in unindexed or subsequently published work remains possible.

## References
[1] E. R. García Barroso, J. I. García-García, L. J. Santana Sánchez and A. Vigneron-Tenorio, *Conductors of Abhyankar–Moh semigroups of even degrees*, arXiv:2209.04232v1 (first public 2022-09-09), https://arxiv.org/abs/2209.04232; Proposition 4, equation (10), Theorem A and concluding open question.

[2] R. D. Barrolleta, E. R. García Barroso and A. Płoski, *On the Abhyankar–Moh inequality*, arXiv:1407.0176v1 (first public 2014-07-01), https://arxiv.org/abs/1407.0176; Theorem 1 on the extremal conductor.

[3] F. Aroca Bisquert, A. Ayala Velasco and G. Ilardi, *Abhyankar–Moh semigroups for arbitrary hypersurfaces*, arXiv:2501.16552 (2025), https://arxiv.org/abs/2501.16552; abstract consulted for scope comparison only.
