# Rigidity and a forbidden near-maximal type for two-generator numerical-semigroup quotients

## Finding
Let \(p\ge5\) be an integer and let \(a,b\ge 2p+1\) be coprime integers with \(\gcd(ab,p)=1\). Define the numerical semigroup
\[
Q=\{n\in\mathbb Z_{\ge0}:pn\in\langle a,b\rangle\}.
\]
Its **type** \(t(Q)\) is the cardinality of the pseudo-Frobenius set \(\operatorname{PF}(Q)\), where a pseudo-Frobenius number is a gap \(n\notin Q\) satisfying \(n+q\in Q\) for every nonzero \(q\in Q\).

**Near-maximal type rigidity.** For every integer \(N\ge0\) with \(3N+2\le p\),
\[
t(Q)=p-N \quad\Longleftrightarrow\quad a\equiv b\equiv1-N\pmod p.
\]
There is exactly one admissible ordered residue-class pair for the value \(p-N\) when \(\gcd(1-N,p)=1\), and none otherwise. In particular, **the penultimate value is impossible**:
\[
\boxed{t(Q)\neq p-1\qquad(p\ge5).}
\]
Moreover, \(t(Q)=p\) occurs exactly when \(a\equiv b\equiv1\pmod p\). For \(p\ge8\), the value \(p-2\) occurs in exactly the class \(a\equiv b\equiv-1\pmod p\). For \(p\ge11\), the value \(p-3\) occurs exactly when \(a\equiv b\equiv-2\pmod p\), provided that \(p\) is odd; it cannot occur when \(p\) is even.

## Assumptions and scope
No primality assumption is made on \(p\). The inequalities \(a,b\ge2p+1\), coprimality \(\gcd(a,b)=1\), and unit conditions modulo \(p\) are essential to the uniform residue-permutation reduction. The theorem classifies only the indicated top portion of the type spectrum; it does not classify all other types, minimal generators, or the exact pseudo-Frobenius values at each parameter.

## Proof
**1. Gap parametrization.** Sylvester's two-generator gap parametrization states that every positive gap of \(\langle a,b\rangle\) is uniquely
\[
ab-ia-jb>0,\qquad i,j\in\mathbb Z_{\ge1}.
\]
Positivity forces \(i<b\) and \(j<a\). Thus every positive gap \(n\) of \(Q\) is of the form \(n=(ab-ia-jb)/p\) for a unique positive pair satisfying the divisibility condition.

For such a gap and any nonzero \(q=(ra+sb)/p\in Q\), with \(r,s\in\mathbb Z_{\ge0}\), the value \(n+q\) is a gap of \(Q\) exactly when \(r<i\) and \(s<j\). Indeed, in this case its numerator is \(ab-(i-r)a-(j-s)b\), again a positive Sylvester gap. If \(r\ge i\), then the numerator rewrites as \((r-i)a+(a-j+s)b\in\langle a,b\rangle\), and the case \(s\ge j\) is symmetric. Consequently the pseudo-Frobenius gaps correspond to coordinatewise minimal points among the positive pairs \((i,j)\) for which \(p\mid ab-ia-jb\).

Every such minimal point lies in \([1,p]^2\): if \(i>p\), replacing \(i\) by \(i-p\) preserves divisibility and makes the gap numerator larger by \(pa\), so the original point is not minimal. Similarly for \(j>p\).

**2. A permutation of the residue box.** For \(1\le i,j\le p\), positivity holds automatically because
\[
ab-p(a+b)=(a-p)(b-p)-p^2\ge (p+1)^2-p^2=2p+1>0.
\]
Since \(b\) is a unit modulo \(p\), each \(i\in\{1,\ldots,p\}\) admits exactly one \(j_i\in\{1,\ldots,p\}\) with
\[
j_i\equiv a-(ab^{-1})i\pmod p.
\]
The sequence \(j_1,\ldots,j_p\) is a permutation of \(1,\ldots,p\), because \(a\) is also a unit modulo \(p\). A point \((i,j_i)\) is coordinatewise minimal precisely when \(j_i\) is strictly below all previous entries. Consequently \(t(Q)\) is the number of left-to-right record minima in this affine modular permutation. In particular \(t(Q)\le p\).

**3. Near-maximal record rigidity.** Suppose this permutation has \(R=p-N\) records. Their values form a strictly decreasing sequence of length \(R\). Between consecutive record values there are \(R-1\) drops, each at least one, whose total does not exceed \(p-1\). Thus at most \(N\) of those drops are at least two. The \(N\) nonrecord positions can interrupt at most \(N\) record-to-record adjacency relations. Therefore at least
\[
(R-1)-N-N=p-3N-1
\]
record transitions are simultaneously adjacent in position and have exact numerical drop one. Since \(3N+2\le p\), this count is at least one. Any such transition forces the affine step to be \(-1\) modulo \(p\). Hence \(ab^{-1}\equiv1\pmod p\) and therefore \(a\equiv b\pmod p\).

When \(a\equiv b\), the permutation descends cyclically by one. Its record minima form exactly the initial descending run, whose length is the representative of \(a-1\pmod p\) in \(\{1,\ldots,p\}\). For that length to equal \(p-N\), one must have \(a\equiv 1-N\pmod p\). This proves necessity. Conversely, if \(a\equiv b\equiv1-N\pmod p\), then the cyclicly descending permutation starts at \(p-N\), hence has exactly \(p-N\) record minima. This proves sufficiency.

For \(N=1\), the required residue is zero, contrary to the unit hypothesis, so type \(p-1\) is impossible. For any allowed \(N\) with \(\gcd(1-N,p)=1\), choose the unique residue \(r\in[1,p]\) representing \(1-N\). For every integer \(k\ge0\), take \(a=(k+2)p+r\) and \(b=a+p\). Then \(\gcd(a,b)=\gcd(a,p)=1\) and all assumptions hold; varying \(k\) produces infinitely many valid coprime pairs realizing each allowed class.

## Verification
Run `python3 check_near.py` with Python 3 and standard library only. One independent finite route generates the quotient semigroup from bounded residue combinations, computes its Apéry set by Dijkstra's algorithm, and extracts its pseudo-Frobenius numbers. That route agreed with the Sylvester-coordinate Pareto rule for 12,343 triples and with the record-count expression for 4,351 triples. A further exhaustive modular-unit census checked 3,491,756 instances of the near-maximal equivalence for all moduli from 5 through 100. Explicit realized-class checks extended through modulus 300. The included `verification_output.txt` records actual outputs. These computations are consistency checks, not a replacement for the proof above.

## Relationship to prior work
Cabanillas (2019), especially Section 5.3, Theorems 6 and 7, **already provides the complete pseudo-Frobenius theory for quotients of two-generated semigroups**, using a lattice model, continued fractions, and Ostrowski numeration. Therefore the general ability to calculate pseudo-Frobenius values, and the individual exact-type formulas derivable from that theory, are not claimed here as new. The contribution asserted here is a **uniform forbidden type and near-top parameter-rigidity theorem across every modulus**, established by an elementary rigidity argument for almost completely descending modular permutations; these cross-parameter structural statements were not located in the inspected primary text.

Liu (2023) develops generating functions and generator systems for numerical-semigroup quotients and cites the earlier quotient and minimal-generator literature; it does not supply the forbidden-near-maximal-type statement. Earlier general methods are stronger for computing the full set for individual inputs, but do not alone state or prove the uniform near-top rigidity without the extra permutation argument.

## Limitations
The claim assumes \(\gcd(p,ab)=1\) and sufficiently large generators. It does not give the full type distribution. Its novelty is assessed against accessible primary literature and indexed records rather than certified against all past mathematical work. Because Cabanillas gives complete individual pseudo-Frobenius formulas, any previously unnoticed corollary or equivalent treatment of high-type rigidity in that literature would supersede the asserted originality. Independent scientific audit has not been performed.

## References
1. E. Cabanillas, *Quotients of numerical semigroups generated by two numbers*, 17 April 2019, arXiv:1904.08240, especially Sections 2.2, 5.2, 5.3, Theorems 6 and 7.
2. F. Liu, *Generating functions for the quotients of numerical semigroups*, 18 December 2023, arXiv:2312.10889; later *Bulletin of the Australian Mathematical Society* 110 (2024), 427–438.
3. A. Adeniran, S. Butler, C. Defant, Y. Gao, P. E. Harris, C. Hettle, Q. Liang, H. Nam and A. Volk, *On the genus of a quotient of a numerical semigroup*, *Semigroup Forum* 98 (2019), 690–700; title and abstract consulted for scope.
