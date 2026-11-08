# Sharp cyclic 2-binomial fingerprint bounds at fixed binary weight

## Finding

Let \(w\) be a binary word of length \(n\ge 2\) containing exactly \(k\) ones, where \(1\le k<n\). Let \(\rho(w)\) be the number of distinct 2-binomial equivalence classes represented by its \(n\) cyclic rotations. Put \(d=\gcd(n,k)\) and \(L=n/d\). Then

\[
L\le \rho(w)\le n-d+1.
\]

Both bounds are attained for every allowed pair \((n,k)\). In fact, \(\rho(w)=L\) if and only if \(w=u^d\) for a binary word \(u\) of length \(L\) containing \(k/d\) ones. The upper bound is attained by the block-clustered word \(w=0^{n-k}1^k\). Thus

\[
\min_{|w|=n,\,|w|_1=k}\rho(w)=\frac{n}{\gcd(n,k)},\qquad
\max_{|w|=n,\,|w|_1=k}\rho(w)=n-\gcd(n,k)+1.
\]

In particular, when \(\gcd(n,k)=1\), all \(n\) rotations of **every** such word have different 2-binomial signatures. Here different means non-equivalent under scattered-subsequence counts, not merely different as literal strings.

## Assumptions and scope

A scattered occurrence of a word \(v\) in \(u\) is an increasing sequence of positions spelling \(v\). Words are 2-binomially equivalent when all scattered counts of length at most two agree. The rotations of \(w=w_0\cdots w_{n-1}\) are \(R_i(w)=w_i\cdots w_{n-1}w_0\cdots w_{i-1}\), for \(0\le i<n\). Repetitions of literal rotations do not affect \(\rho\). The theorem ranges over **all** binary words of the stated length and weight, and does not concern adjacent-pair profiles or 2-abelian equivalence.

The constant words \(0^n\) and \(1^n\) have \(\rho=1\) and are excluded solely to avoid notational degeneracy.

## Proof

**1. Reduction to one scattered-subsequence statistic.** Every rotation has \(k\) ones and \(n-k\) zeros. The scattered counts of \(00\) and \(11\) are therefore fixed, while the counts of \(01\) and \(10\) sum to \(k(n-k)\). Thus 2-binomial equivalence of two rotations is equivalent to equality of the single integer \(S_i=\binom{R_i(w)}{01}\).

Moving the initial letter of a rotation to its end changes \(S_i\) by \(-k\) if that letter is zero (the initial zero formerly preceded all \(k\) ones), and by \(n-k\) if that letter is one (the moved one now follows all \(n-k\) zeros). Write \(a=(n-k)/d\) and \(b=k/d\), so \(\gcd(a,b)=1\) and \(L=a+b\). Set \(H_i=(S_i-S_0)/d\), with the index extended cyclically and \(H_n=H_0\). Then

\[
H_{i+1}-H_i=\begin{cases}a,&w_i=1,\\-b,&w_i=0.\end{cases}
\]

**2. Universal lower bound and all equality cases.** Both increments are congruent to \(-b\) modulo \(L\); hence \(H_i\equiv -bi\pmod L\), and \(\gcd(b,L)=1\). In particular, \(H_0,\ldots,H_{L-1}\) are pairwise distinct, proving \(\rho(w)\ge L\). More precisely, \(H_i\equiv H_j\pmod L\) holds precisely when \(i\equiv j\pmod L\).

If \(\rho(w)=L\), each congruence class modulo \(L\) is represented by exactly one integer height. Thus \(H_{i+L}=H_i\) for every cyclic index \(i\). Subtracting successive equalities gives \(H_{i+L+1}-H_{i+L}=H_{i+1}-H_i\). The two increments \(a\) and \(-b\) are different, so \(w_{i+L}=w_i\) for all \(i\). Therefore \(w=u^d\) with \(|u|=L\), \(|u|_1=b\). Conversely such a power has at most \(L\) literal rotations, and the preceding lower bound proves \(\rho(w)=L\).

**3. Balanced-window removal lemma.** Every cyclic binary word of length \(dL\) containing \(db\) ones has a cyclic window of length \(L\) containing exactly \(b\) ones. Indeed, let \(q_i\) be the count of ones in the \(L\)-window starting at \(i\). The average of the \(dL\) counts is \(b\), since each one occurs in exactly \(L\) windows, and \(|q_{i+1}-q_i|\le1\). If no count equaled \(b\), the average condition would force counts both below and above \(b\), contradicting the unit-step change around the cycle.

In the height walk, such a window has net increment \(ba-(L-b)b=0\), so its initial and final heights agree. Delete the corresponding \(L\) consecutive edges and reconnect the walk at that common height. The remaining cyclic word has \((d-1)L\) letters and \((d-1)b\) ones, while retaining the **same** normalized step sizes \(+a,-b\). The new height walk visits all the original integer heights except possibly the \(L-1\) interior heights of the deleted segment. Hence if \(\rho_d\) denotes a height count for a word with \(d\) copies of the primitive length and content totals, the deletion produces a word with \(\rho_d\le\rho_{d-1}+L-1\).

For \(d=1\), the congruence argument already gives \(\rho_1=L\). Applying the deletion inequality inductively yields

\[
\rho_d\le L+(d-1)(L-1)=dL-d+1=n-d+1.
\]

**4. Sharp upper construction.** For \(w=0^{da}1^{db}\), the height walk first visits \(0,-b,-2b,\ldots,-dab\), i.e. \(da+1\) levels. Its return segment contributes the \(db-1\) intermediate values \(-dab+ta\), \(1\le t<db\). A return height coincides with a downward height exactly when \(b\mid ta\), equivalently \(b\mid t\), since \(\gcd(a,b)=1\). There are exactly \(d-1\) such overlaps. Consequently

\[
\rho(w)=(da+1)+(db-1)-(d-1)=d(a+b)-d+1=n-d+1,
\]

which finishes the proof.

## Verification

The standalone \`verify.py\` uses direct scattered-subsequence enumeration, independently of the height-walk formula. It checks all 8,166 nonconstant binary words of lengths \(2\) through \(12\), confirms the universal bounds and the exact characterization of every lower-bound equality case, and confirms both extremal constructions for each content. Its output is:

\`VERIFY_OK: all 8166 nonconstant binary words of lengths 2..12; exact minima, maxima, and all equality cases\`

The finite exhaustive check is a diagnostic only; the proof above establishes the assertions for arbitrarily large lengths.

## Relationship to prior work

Rigo and Salimov's 2013 contribution introduced binomial equivalence and studied its complexity for infinite words. Lejeune, Rigo, and Rosenfeld (2020) characterized binary 2-binomial classes by Parikh matrices and considered the cardinalities of full equivalence classes among all words, not the number encountered along one fixed cyclic orbit. Richomme (2025) related the binary scattered \(01\)-count to lattice paths and integer partitions; his full-text discussion of classes and fair words does not give the present sharp fixed-weight rotation-orbit extrema or the power characterization of minimizers. Cassaigne, Fici, Sciortino, and Zamboni (2014) studied conjugacy classes of contiguous factors of infinite words: that cyclic-complexity invariant is different from the current scattered-subsequence quotient within a *single* necklace.

The novelty claim concerns the simultaneous sharp lower and upper bounds for every pair \((n,k)\), with the complete minimum-equality classification. It does not claim that the underlying binomial equivalence, rotation operation, or lattice-path representation is new.

## Limitations

The theorem treats binary alphabet, scattered patterns of lengths at most two, and full cyclic rotation orbits at fixed weight. It does not classify **all** upper-extremizing words or enumerate words attaining each intermediate value; it does not cover higher binomial orders or larger alphabets. The literature comparison is targeted, not a proof of absolute historical priority. Independent audit has not been performed.

## References

- M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013, author-preprint publicly available 2013-05-27. https://orbi.uliege.be/handle/2268/149313
- M. Lejeune, M. Rigo and M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732 (2020). https://arxiv.org/abs/2001.11732
- G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159 (2025). https://arxiv.org/abs/2510.07159
- J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843 (2014). https://arxiv.org/abs/1402.5843
