# Exact Lie spectra and inverse run rigidity for distinct-letter periodic blocks

## Finding

Let \(q\ge2\), let \(c_0,\ldots,c_{q-1}\) be pairwise distinct symbols, and let \(a_0,\ldots,a_{q-1}\) be positive integers. Write
\[
P=c_0^{a_0}c_1^{a_1}\cdots c_{q-1}^{a_{q-1}},\qquad L=\sum_{i=0}^{q-1}a_i,\qquad W=P^\omega.
\]
For \(n\ge1\), let \(\mathcal L_W(n)\) be the number of cyclic-conjugacy classes of length-\(n\) contiguous factors \(v\) of \(W\) such that **every** cyclic rotation of \(v\) occurs as a contiguous factor of \(W\). Define \(U(n)=\#\{i:a_i\ge n\}\). Then the exact, all-length Lie complexity is
\[
\boxed{\mathcal L_W(n)=U(n)+\mathbf1_{L\mid n}+E(n),}
\]
where
\[
E(n)=\begin{cases}
1,&q=2,\ \min(a_0,a_1)\ge2,\ n=2,\\
1,&q=2,\ \min(a_0,a_1)=1,\ 2\le n<L,\\
0,&\text{otherwise}.
\end{cases}
\]
These summands count distinct classes. Specifically, the complete classes are precisely:

1. The single-letter classes \([c_i^n]\), when \(1\le n\le a_i\).
2. The period-power class \([P^{n/L}]\), when \(L\mid n\).
3. For the two-letter case with both run lengths at least two, the extra class \([c_0c_1]\) at \(n=2\).
4. For the two-letter case with a singleton run, its letter \(c\) and the other letter \(d\) give the extra class \([c d^{n-1}]\) at every \(2\le n<L\).

Equivalently, setting \(G_W(z)=\sum_{n\ge1}\mathcal L_W(n)z^n\),
\[
G_W(z)=\sum_{i=0}^{q-1}\frac{z(1-z^{a_i})}{1-z}+\frac{z^L}{1-z^L}
+\begin{cases}
0,&q\ge3,\\
z^2,&q=2,\ \min(a_0,a_1)\ge2,\\
\displaystyle\sum_{j=2}^{L-1}z^j,&q=2,\ \min(a_0,a_1)=1.
\end{cases}
\]
The final sum is empty when \(L=2\).

**Inverse rigidity.** Within this family, the entire sequence \((\mathcal L_W(n))_{n\ge1}\) uniquely determines the alphabet size \(q\), the least period \(L\), and the multiset \(\{a_0,\ldots,a_{q-1}\}\), though not necessarily its cyclic order. Thus two such words have the same Lie complexity if and only if their run-length multisets agree (up to renaming of symbols).

## Assumptions and scope

The alphabet symbols are labeled and pairwise distinct; each appears in exactly one positive-length run in the defining primitive period \(P\), and the host is the infinite purely periodic word \(P^\omega\). Circular rotations are rotations of an **observed finite factor**, not rotations of the infinite host. A class is counted only if every one of its finite rotations occurs somewhere in the host. The statements hold for every integer \(n\ge1\), including the binary period \(L=2\) and arbitrary larger repetition lengths.

## Proof

**Step 1 (allowed transitions).** For \(q\ge3\), the only different-letter adjacent pairs occurring in \(W\) are \(c_ic_{i+1}\), indices taken modulo \(q\). If every rotation of a mixed factor \(v\) occurs, every different-letter adjacent pair in the **circular** word \([v]\), including the last-to-first pair, must be one of these allowed pairs. Hence the cyclic succession of the maximal constant-letter blocks of \(v\) traces one or more complete circuits through \(c_0,c_1,\ldots,c_{q-1}\). In particular, it has at least three cyclic blocks. In the binary case the allowed different-letter pairs go both ways, and the number of cyclic blocks is an even positive integer.

**Step 2 (interior-block rigidity).** In \(W\), a maximal run of \(c_i\) occurring strictly between letters different from \(c_i\) necessarily has length exactly \(a_i\). Suppose a cyclic run \(R\) of \(v\) is accompanied by at least two other cyclic runs. By choosing a rotation of \(v\) that starts inside or at the beginning of a different run and leaves at least one letter from another run after \(R\), one obtains a rotation in which the full \(R\) is strictly internal, with a different letter on each side. Since that rotation is a factor of \(W\), \(R\) must have the host's exact run length. This applies to every run if \(q\ge3\), and also if \(q=2\) and \(v\) has at least four cyclic runs. Accordingly each such mixed rotation-complete word is a circular power of \(P\); its length is a positive multiple of \(L\). Conversely, every rotation of \(P^k\), for \(k\ge1\), appears in \(W\). All these words supply exactly one class per multiple of \(L\).

**Step 3 (the two-run binary exception).** Consider a mixed circular factor with just two runs, represented by \(c_0^r c_1^s\), where \(r,s\ge1\). If \(r,s\ge2\), rotating inside the \(c_1\)-run exposes the entire \(c_0\)-run internally and forces \(r=a_0\); rotating inside the \(c_0\)-run forces \(s=a_1\). This is the full period class. If \(r=1<s\), a rotation cut inside the longer run forces \(a_0=1\), while occurrence of \(c_1^s\) requires \(s\le a_1\). These conditions suffice: every rotation of \(c_0c_1^s\), including ones of the form \(c_1^j c_0c_1^{s-j}\), occurs across a singleton \(c_0\)-run in \(W\). The case \(s=1<r\) is symmetric. Finally, both rotations of \(c_0c_1\) occur for all positive \(a_0,a_1\). Removing the full period case leaves exactly the two exceptional regimes in \(E(n)\).

**Step 4 (unary classes and enumeration).** For each symbol \(c_i\), the only fully unary class at length \(n\) is \([c_i^n]\), and it occurs exactly when \(n\le a_i\). The mixed classes from Steps 1–3 are distinct from the unary classes and from one another. Counting gives the stated formula; summing their indicator functions gives \(G_W(z)\).

**Step 5 (inverse statement).** For all sufficiently large \(n\), all unary and exceptional classes have disappeared, so \(\mathcal L_W(n)=\mathbf1_{L\mid n}\). Therefore \(L\) is the least positive \(d\) for which \(\mathcal L_W(kd)>0\) for all sufficiently large positive integers \(k\); smaller or nonmultiplicative candidates have infinitely many missing multiples. Also \(q=\mathcal L_W(1)\). If \(q\ge3\), then \(U(n)=\mathcal L_W(n)\) for \(1\le n<L\), recovering the run multiset from the differences \(U(n)-U(n+1)\). For \(q=2\), \(L=2\) gives \(\{1,1\}\). If \(L>2\), a singleton run is detected by \(\mathcal L_W(2)=2\) (against \(3\) when both lengths are at least two), and its multiset is \(\{1,L-1\}\). Otherwise \(U(1)=U(2)=2\) and \(U(n)=\mathcal L_W(n)\) for \(3\le n<L\), again recovering both lengths. This proves inverse rigidity and the equivalence of spectra with run-length multisets.

## Verification

A standalone Python-standard-library checker is included as `verify_lie.py`. It independently enumerates every length-\(n\) factor of the period, groups factors into cyclic rotation classes, and checks whether **all** rotations occur. It compares the actual class sets (not just counts) to the explicit classification and separately to the numerical formula.

Its verified output was:

```text
PASS: 31840 exhaustive parameter-length configurations (q=2..5, run lengths=1..4, n=1..2L)
PASS: 1600 reproducible randomized parameter-length configurations (q=6,7)
PASS: predicted and observed complete conjugacy CLASS SETS match, not merely class counts
All tests use direct periodic-factor enumeration; infinite claims use the proof.
```

For example, for run lengths \((3,3)\), the first twelve complexity values are \((2,3,2,0,0,1,0,0,0,0,0,1)\); for \((1,4)\), the first ten are \((2,2,2,2,1,0,0,0,0,1)\); and for \((2,2,3)\), the first seven are \((3,3,1,0,0,0,1)\). The finite checks do not establish the universal result; the run-rigidity proof does.

## Relationship to prior work

Bell and Shallit introduced Lie complexity and established a general upper bound by successive factor-complexity differences, together with automaticity for automatic source words [1]. Their exact examples concern named nonperiodic automatic and morphic words, not this periodic block family. De Luca and Fici gave exact Lie complexity for irrational-slope Sturmian words [2]; those hosts are aperiodic, so their continued-fraction classification does not imply the present distinct-letter periodic-run theorem. Li developed Rauzy-cycle bounds and extended/prefix Lie complexity [3], without an exact run-profile enumeration. This finding supplies an object-specific complete class classification and an inverse reconstruction law not stated in those examined results. The distinction between complete cyclic-conjugacy classes and classes containing merely one factor is essential.

## Limitations

The classification requires a **purely** periodic host with one positive run per distinct symbol in its primitive period; it does not cover arbitrary repeated-letter block patterns, ultimately periodic words with a preperiod, or unrestricted mechanical/Sturmian words. It recovers the multiset of run lengths, not their cyclic order. Searches and primary-literature comparisons cannot eliminate all risk of an unindexed equivalent statement; there has been no independent scientific audit.

## References

[1] J. P. Bell and J. Shallit, *Lie Complexity of Words*, first public arXiv version 7 February 2021, [arXiv:2102.03821](https://arxiv.org/abs/2102.03821), especially §§1–2, 6–7.

[2] A. De Luca and G. Fici, *On the Lie Complexity of Sturmian Words*, first public arXiv version 2 June 2022, [arXiv:2206.00995](https://arxiv.org/abs/2206.00995), especially §§2–3.

[3] S. Li, *A Note on the Lie Complexity and Beyond*, first public arXiv version 12 July 2022, [arXiv:2207.05859](https://arxiv.org/abs/2207.05859), especially §§1–3 and the stated extensions.
