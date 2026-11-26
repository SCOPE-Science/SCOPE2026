# Cyclic-descent classification of complements of repeated permutation words

## Finding
Let \(q\ge2\), let \(P=a_0a_1\cdots a_{q-1}\) be a word of pairwise distinct symbols, and let \(m\ge1\), \(0\le k\le m\). Put \(r=m-k\). For \(0\le s<q\), write \(R_s=a_sa_{s+1}\cdots a_{q-1}a_0\cdots a_{s-1}\), the cyclic rotation by \(s\) positions. For \(\mathbf{s}=(s_1,\ldots,s_r)\in\{0,\ldots,q-1\}^r\), define
\[
d(\mathbf{s})=\sum_{i=1}^{r-1}{\bf1}_{s_i>s_{i+1}}+{\bf1}_{r>0,\,s_r>0},
\]
with \(d(())=0\). The complement-scattered-factor set obtained by deleting an embedding of \(P^k\) from \(P^m\) is **exactly**
\[
C(P^m,P^k)=\left\{R_{s_1}\cdots R_{s_r}:d(\mathbf{s})\le k\right\}.
\]
All listed outputs are distinct. In particular its cardinality has the explicit finite alternating-binomial form
\[
\boxed{\left|C(P^m,P^k)\right|=\sum_{j=0}^{k}(-1)^{k-j}\binom{r}{k-j}\binom{qj+r}{r}.}
\]
Here a binomial coefficient with its lower argument outside the range is zero. More precisely, if \(F_{q,r}(z)=\sum_{\mathbf{s}}z^{d(\mathbf{s})}\), then
\[
\boxed{\sum_{r\ge0}F_{q,r}(z)t^r=\frac{(1-z)\bigl(1-(1-z)t\bigr)^{q-1}}{\bigl(1-(1-z)t\bigr)^q-z},\qquad F_{q,r}(z)=(1-z)^{r+1}\sum_{j\ge0}\binom{qj+r}{r}z^j.}
\]
The identities involving the infinite series are identities of formal power series and determine polynomials in \(z\). For \(k=0\), the set is \(\{P^m\}\); for \(r=0\), it is \(\{\varepsilon\}\). If \(k\ge r\), every one of the \(q^r\) concatenations of cyclic rotations occurs.

## Assumptions and scope
A *scattered occurrence* of a word \(u\) in a word \(w\) is a strictly increasing sequence of positions in \(w\) spelling \(u\). Its *complement* is the word left by removing those positions and retaining the order of all other positions. The set \(C(w,u)\) consists of distinct such complements (not counted with embedding multiplicity). The theorem holds for all and only the quantified values of \(q,m,k\) above, independently of the specific distinct letter labels of \(P\). Positions and rotation indices in the proof are zero-based.

## Proof
**1. Forced block structure.** Fix a deletion/retention scan of \(P^m\) whose deleted letters spell \(P^k\). Just before a scanned letter, let \(i\) be the number already deleted and \(j\) the number already retained. The next original letter is \(a_{(i+j)\bmod q}\); the next required deleted letter, if any, is \(a_{i\bmod q}\). Since the letters of \(P\) are distinct, a deletion is possible only if \(j\equiv0\pmod q\). Thus all deletions occur between complete retained blocks of length \(q\). During a retained block the deleted count \(i\) remains fixed, so its \(q\) symbols form precisely \(R_{i\bmod q}\). Every complement therefore has the asserted unique rotation-block representation.

**2. Exact deletion cost.** Let \(s_1,\ldots,s_r\) denote the rotation indices in that representation. Write \(s_0=s_{r+1}=0\). Let \(t_h\) be the number of deleted letters before block \(h+1\) for \(0\le h<r\), and after the final block for \(h=r\). Each \(t_h\ge0\), and the required congruences are
\[
t_h\equiv s_{h+1}-s_h\pmod q\quad(0\le h\le r),\qquad \sum_{h=0}^{r}t_h=qk.
\]
The least possible total deletion count is the sum of the least nonnegative residues of these differences. Each strictly decreasing transition contributes one additional \(q\) when its ordinary difference is replaced by that residue. Because the ordinary differences telescope to zero, their least-residue sum is exactly \(q\,d(\mathbf{s})\). The initial transition \(0\to s_1\) never decreases; the last transition \(s_r\to0\) decreases exactly when \(s_r>0\). Therefore the congruences have a nonnegative solution summing to \(qk\) exactly if \(d(\mathbf{s})\le k\): use the least residues and add \(q(k-d(\mathbf{s}))\) deletions to any one gap. Such a schedule explicitly reconstructs an embedding of \(P^k\) whose complement is the specified rotation-block word. This proves both inclusions, including the empty-block case.

**3. Counting descents.** Define a \(q\times q\) matrix \(M\) indexed by \(0,\ldots,q-1\) by \(M_{ab}=z\) if \(a>b\) and \(M_{ab}=1\) otherwise. The sequence \((0,s_1,\ldots,s_r,0)\) has weight \(z^{d(\mathbf{s})}\), so
\[
F_{q,r}(z)=(M^{r+1})_{00}.
\]
Put \(D_q(t)=\det(I-tM)\) and \(A=1-(1-z)t\). Subtracting each preceding original row from the next row, proceeding from bottom to top, transforms rows \(2,\ldots,q\) into equations with adjacent entries \(-A,1\). Expansion or elimination against the first row gives
\[
D_q(t)=1-t\sum_{h=0}^{q-1}A^h=\frac{A^q-z}{1-z}.
\]
The last displayed quotient is polynomial because the numerator is divisible by \(1-z\); the equality initially holds for \(z\ne1\) and hence identically. The \((0,0)\) cofactor is \(D_{q-1}(t)\); define \(D_0(t)=1\), so this also covers \(q=1\) algebraically. Consequently,
\[
\sum_{r\ge0}F_{q,r}(z)t^r=\frac{D_{q-1}(t)/D_q(t)-1}{t}=\frac{(1-z)A^{q-1}}{A^q-z}.
\]
Expanding as \((1-z)\sum_{j\ge0}z^j A^{-qj-1}\) and extracting \(t^r\) yields
\[
F_{q,r}(z)=(1-z)^{r+1}\sum_{j\ge0}\binom{qj+r}{r}z^j.
\]
Finally \(\lvert C(P^m,P^k)\rvert=\sum_{d=0}^{k}[z^d]F_{q,r}(z)=[z^k]F_{q,r}(z)/(1-z)\). Coefficient extraction from the preceding identity gives the claimed finite binomial sum. Distinctness of the rotation blocks ensures there is no further quotient by collisions. This proves the theorem.

## Verification
Run `python3 checker.py` (Python standard library only) beside this file. The independent oracle enumerates complement words by dynamic programming on remaining deletion/retention choices, without using the rotation classification. All \(117\) tested parameter triples with \(2\le q\le5\), \(1\le m\le7\), \(0\le k\le m\), and \(qm\le27\) matched the predicted complement sets and cardinalities (\(1927\) total distinct outputs across cases). A separate transfer dynamic program matched the finite alternating sum for \(4480\) parameter triples through \(q=9\) and \(m=32\). The output is recorded in `checker_output.txt`. The proof above, not finite verification, establishes the universal quantifiers.

## Relationship to prior work
Adamson, Fleischmann, and Huch (arXiv:2603.20790, first submitted 2026-03-21) define complement scattered factors, give general algorithms, and prove broad structural properties about singleton complements and shuffles. Their full open-access HTML manuscript was examined, in particular the definition (Section 2), enumeration algorithm (Section 3), and complementary/shuffle results (Section 4). The present theorem specializes that notion to two nested powers of a single distinct-letter permutation, but goes beyond a generic enumeration algorithm by identifying *all* outputs as cyclic-rotation blocks with a bounded descent statistic and giving a parameter-uniform closed count. The descent-polynomial identity is classical-type combinatorial algebra; novelty is not claimed for the abstract Eulerian polynomial independently of this string-complement interpretation. Liang, Sagan, and Zhuang (2023) study shuffle-compatibility of statistics on disjoint permutations and cyclic permutations, a different distribution problem that does not determine these complements. Published-record and related finding searches did not reveal a broader statement implying the classification; this is not a proof of unique priority.

## Limitations
The result addresses complements of an exact smaller whole power \(P^k\) in \(P^m\) where \(P\) has no repeated letters. It does not classify complements for arbitrary deletion patterns, partial periods, repeated-letter base blocks, or embedding multiplicities. The explicit binomial sum can involve cancellation, although the descent description is manifestly nonnegative. Relevant but unindexed or differently worded prior material may remain. No independent mathematical audit is asserted.

## References
1. D. Adamson, P. Fleischmann, and A. Huch, “(Sets of) Complement Scattered Factors,” arXiv:2603.20790v1 (2026-03-21), https://arxiv.org/html/2603.20790v1 , Sections 2–4.
2. J. Liang, B. E. Sagan, and Y. Zhuang, “Cyclic Shuffle-Compatibility Via Cyclic Shuffle Algebras,” *Annals of Combinatorics* 28 (2024), 615–654; first published 2023-10-24, https://doi.org/10.1007/s00026-023-00669-9 .
