# Universal helper-set recovery in the MDS-pair EAQLRC family
## Finding

Consider any code in the MDS-intersection family of Li, Ling, Lu, Luo, and Zhu Theorem 6. Thus the code is an optimal pure entanglement-assisted quantum locally recoverable code with parameters
\[
\llbracket n,n+c-2d+2,d;c\rrbracket_q
\]
and guaranteed locality
\[
r=n-d+1.
\]

For every transmitted coordinate \(i\), **every** subset
\[
R\subseteq[n]\setminus\{i\},\qquad |R|=r,
\]
is a recovery set for \(Q_i\) in the source's recovery model, where the recovery channel may additionally access Bob's reliable halves of the preshared entangled pairs.

Consequently the complete family of size-\(r\) recovery sets for a fixed erased coordinate is the full uniform hypergraph
\[
\binom{[n]\setminus\{i\}}r.
\]
In particular, the number of size-\(r\) recovery sets is exactly
\[
N_i=\binom{n-1}{r}=\binom{n-1}{d-2}.
\]
For every fixed helper subset \(T\subseteq[n]\setminus\{i\}\) with
\[
|T|=t\le r,
\]
the number of these recovery sets containing \(T\) is
\[
\binom{n-1-t}{r-t}.
\]
Thus every individual helper coordinate occurs in
\[
\binom{n-2}{r-1}
\]
size-\(r\) recovery sets, and every pair of helpers occurs together in
\[
\binom{n-3}{r-2}
\]
of them when \(r\ge2\).

The largest possible collection of pairwise disjoint size-\(r\) recovery sets is exactly
\[
\left\lfloor\frac{n-1}{r}\right\rfloor.
\]
Hence the construction is not merely locally recoverable from one specially chosen helper set: after one transmitted qudit is erased, **any** choice of \(r\) surviving transmitted qudits can be used as the helper set.

For the source's example
\[
\llbracket5,2,3;1\rrbracket_5,
\]
one has \(r=3\). Each coordinate therefore has all
\[
\binom43=4
\]
three-helper recovery sets.

## Assumptions and scope

The source family exists for prime powers \(q\ge3\) and integers \(n,d,c\) satisfying
\[
2\le d\le n\le q+1,
\qquad
\max\{0,2d-n-1\}\le c\le d-1,
\]
subject to the exceptional triples excluded in Theorem 6: \((n,d,c)=(q+1,2,1)\) and \((q+1,q+1,q)\), and additionally \((q+1,q/2+1,0)\) when \(q\) is even.

The statement concerns the guaranteed recovery channel in Definition 5 and Theorem 2 of the source. A recovery set contains transmitted qudits only, while the channel is allowed to access Bob's reliable entanglement register.

The claim is about recovery sets of size exactly
\[
r=n-d+1.
\]
It does not assert that \(r\) is the minimum possible locality of every individual code in the family; the source itself notes that its support criterion is sufficient and that actual minimum locality can be smaller.

## Proof

The source constructs two classical codes \(C_X\) and \(C_Z\) for which
\[
C_X^\perp
\quad\text{and}\quad
C_Z^\perp
\]
are both MDS codes with parameters
\[
[n,d-1,n-d+2]_q=[n,d-1,r+1]_q.
\]
Its Theorem 2 says that if, for a coordinate \(i\), one can choose
\[
h_i^X\in C_X^\perp,
\qquad
h_i^Z\in C_Z^\perp
\]
such that \(i\) lies in both supports and the union of the two supports has size at most \(r+1\), then the other coordinates in that union form a recovery set for \(Q_i\).

We first recall the exact support property of an MDS code. Let \(D\) be an
\[
[n,k,n-k+1]_q
\]
MDS code and let \(S\subseteq[n]\) have size
\[
|S|=n-k+1.
\]
Its complement \(T=[n]\setminus S\) has size \(k-1\). For a generator matrix of \(D\), every set of \(k-1\) columns is linearly independent. Therefore the condition that a codeword vanish on all coordinates in \(T\) imposes \(k-1\) independent linear conditions on the \(k\)-dimensional message space. There is a one-dimensional space of nonzero codewords vanishing on \(T\).

Any such nonzero word has support contained in \(S\). It cannot vanish at an additional coordinate of \(S\), because then it would vanish on \(k\) coordinates whose generator columns are linearly independent, forcing the message and hence the codeword to be zero. Thus its support is exactly \(S\).

Now fix a transmitted coordinate \(i\) and an arbitrary helper set
\[
R\subseteq[n]\setminus\{i\},
\qquad
|R|=r.
\]
Put
\[
S=R\cup\{i\}.
\]
Then \(|S|=r+1=n-d+2\). Applying the MDS support property to each of \(C_X^\perp\) and \(C_Z^\perp\) gives words
\[
h_i^X\in C_X^\perp,
\qquad
h_i^Z\in C_Z^\perp
\]
with
\[
\operatorname{Supp}(h_i^X)
=
\operatorname{Supp}(h_i^Z)
=S.
\]
The paired-support hypothesis of the source's Theorem 2 is therefore satisfied with union support exactly \(S\). The recovery construction in that theorem shows that
\[
S\setminus\{i\}=R
\]
is a recovery set for \(Q_i\).

Since \(R\) was an arbitrary \(r\)-subset of the \(n-1\) other transmitted coordinates, every such subset is a recovery set. There are exactly
\[
\binom{n-1}{r}
\]
of them.

The incidence formulas are then purely combinatorial. A fixed \(t\)-subset \(T\) is contained in precisely those \(r\)-subsets obtained by adjoining \(r-t\) coordinates chosen from the remaining \(n-1-t\), giving
\[
\binom{n-1-t}{r-t}.
\]

Finally, any pairwise disjoint family of \(r\)-subsets of an \((n-1)\)-element helper set has size at most
\[
\left\lfloor\frac{n-1}{r}\right\rfloor.
\]
Because **all** \(r\)-subsets are recovery sets, this upper bound is attained by partitioning any
\[
r\left\lfloor\frac{n-1}{r}\right\rfloor
\]
helpers into blocks of size \(r\). This proves the exact disjoint-recovery count.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It checks the support mechanism in the source's smallest displayed parameter example
\[
(q,n,d,c)=(5,5,3,1),
\]
for which
\[
r=3
\]
and the relevant dual MDS parameters are
\[
[5,2,4]_5.
\]
The verifier constructs the length-five Reed--Solomon code of affine linear functions over \(\mathbb F_5\). It exhausts all nonzero codewords and confirms that every four-coordinate subset occurs as the exact support of a minimum-weight word.

For each of the five erased coordinates it then enumerates all four possible three-helper subsets and confirms that adjoining the erased coordinate gives one of these MDS minimum supports. It independently checks the binomial incidence formulas and exact disjoint-matching formula over a range of \((n,d)\) values.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Li--Ling--Lu--Luo--Zhu prove the MDS-pair construction and establish locality \(r=n-d+1\). In the proof of their Theorem 6 they choose, for each coordinate, a set \(S_i\) of size \(r+1\) and invoke the MDS fact that every such set supports a minimum-weight dual codeword. The proof needs only one such set per coordinate and therefore concludes only the existential locality statement.

The result here quantifies the unused symmetry in that same proof: the choice of \(S_i\) is arbitrary, and the code construction itself does not depend on it. Re-running the paired-support argument for every \((r+1)\)-set containing \(i\) gives the complete size-\(r\) recovery hypergraph, its full incidence profile, and the exact maximum number of pairwise disjoint size-\(r\) local recovery routes.

Kshirsagar, Matthews, and Shapiro subsequently introduced an EAQLRC framework with availability, where multiple suitably disjoint local recovery sets are part of the code specification. Their constructions use Vandermonde/random, Tamo--Barg, fiber-product, and algebraic-geometry code families. The literature inspected does not state the universal-helper-set property for the Li--Ling--Lu--Luo--Zhu MDS-intersection family. In the single-erasure case, the disjoint recovery sets proved here provide the corresponding multiplicity directly.

## Limitations

The theorem classifies all recovery sets of the **source-guaranteed size** \(r\), not all recovery sets of every possible cardinality. Some codes in the family may admit recovery from fewer than \(r\) transmitted qudits, because the source's locality criterion is sufficient rather than necessary.

The pairwise-disjoint count is exact within the complete size-\(r\) recovery system. No claim is made about simultaneous recovery from multiple erased transmitted qudits.

The recovery model assumes Bob's halves of the preshared entangled pairs are reliable and accessible, exactly as in the source paper.

## References

1. Yang Li, San Ling, Zhenliang Lu, Gaojun Luo, and Shixin Zhu, *Entanglement-Assisted Quantum Locally Recoverable Codes: Characterizations, Bounds, and Constructions*, arXiv:2607.27091v1, first public 29 July 2026.
2. Rutuja Kshirsagar, Gretchen L. Matthews, and Julia Shapiro, *Entanglement-assisted quantum locally recoverable codes: bounds and constructions with availability*, arXiv:2608.09886, first public 10 August 2026.
