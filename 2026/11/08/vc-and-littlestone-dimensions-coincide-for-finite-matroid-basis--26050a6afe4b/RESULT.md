# VC and Littlestone dimensions coincide for finite matroid basis incidence

## Finding
For every finite matroid \(M=(E,r_M)\), consider its bases as subsets of \(E\) and Boolean queries \(h_B(e)=1\) if and only if \(e\in B\). Define
\[
 d(M)=\max\{|S|:S\subseteq E\text{ is independent in both }M\text{ and }M^*\}.
\]
Then
\[
\operatorname{VCdim}(\mathcal B(M))=\operatorname{Ldim}(\mathcal B(M))=d(M)
=\min_{A\subseteq E}\bigl(2r_M(A)+|E\setminus A|-r_M(E)\bigr).
\]
In fact the entire simplicial complex of VC-shattered supports is the common-independence system of \(M\) and its dual \(M^*\). Equivalently, the common dimension is
\[
\max_{B_1,B_2\in\mathcal B(M)}|B_1\setminus B_2|,
\]
which equals half the largest symmetric difference between two bases.

## Assumptions and scope
A matroid here is finite, with a nonempty basis family; the rank-zero matroid and matroids with loops or coloops are included. The dual rank satisfies \(r_{M^*}(X)=|X|-r_M(E)+r_M(E\setminus X)\). All dimensions are finite nonnegative integers, with dimension zero for a singleton hypothesis class. The Littlestone dimension is the greatest depth of a full binary membership-query tree whose every root-to-leaf binary response sequence is realized by a basis; a query may vary with the earlier responses.

## Proof
**Step 1: exact shattered supports.** If a set \(S\subseteq E\) is VC-shattered, its all-positive trace belongs to a basis, so \(S\) is independent in \(M\). Its all-negative trace is a basis in \(E\setminus S\), so \(E\setminus S\) spans \(M\), equivalently \(S\) is independent in \(M^*\). Conversely assume both conditions. For every \(T\subseteq S\), \(T\) is independent; also \(E\setminus S\) spans the entire matroid. Hence \(T\cup(E\setminus S)\) spans \(M\), and the basis-extension axiom produces a basis containing \(T\) and using no element of \(S\setminus T\). Thus \(S\) is shattered and \(\operatorname{VCdim}=d(M)\).

**Step 2: rank min--max.** Apply the classical two-matroid intersection theorem to the independence systems of \(M\) and \(M^*\):
\[
 d(M)=\min_{A\subseteq E}\bigl(r_M(A)+r_{M^*}(E\setminus A)\bigr).
\]
Substitute the dual-rank identity to obtain the displayed formula. Introduce the integer-valued function
\[
 F_M(A)=2r_M(A)+|E\setminus A|-r_M(E).
\]

**Step 3: a pointwise deletion--contraction identity.** Suppose \(e\in E\) is neither a loop nor a coloop. Put \(E'=E\setminus\{e\}\). Since \(r(M\setminus e)=r(M)\), for every \(X\subseteq E'\),
\[
 F_{M\setminus e}(X)=F_M(X)-1.
\]
Since \(r_{M/e}(X)=r_M(X\cup\{e\})-1\) and \(r(M/e)=r(M)-1\),
\[
 F_{M/e}(X)=F_M(X\cup\{e\})-1.
\]
The two kinds of subset \(X\) exhaust all subsets of \(E\) according to whether they contain \(e\). Taking minima therefore gives the exact identity
\[
 d(M)=1+\min\bigl\{d(M\setminus e),d(M/e)\bigr\}
\]
**for every element whose basis-membership query is nonconstant**. No optimization over \(e\) is needed for this equality.

**Step 4: online induction.** Let \(\ell(M)\) denote the Littlestone dimension of the basis-indicator class. If every element is a loop or coloop, \(M\) has a unique basis and \(d(M)=\ell(M)=0\). Otherwise a query on a loop or coloop has one impossible answer and cannot be the root of a complete positive-depth tree. A query on any other element \(e\) divides the concepts into bases omitting \(e\), which are the bases of \(M\setminus e\), and bases containing \(e\), which after deleting that fixed coordinate are the bases of \(M/e\). Thus the defining minimax recursion is
\[
\ell(M)=1+\max_{e\text{ neither loop nor coloop}}
\min\{\ell(M\setminus e),\ell(M/e)\}.
\]
By induction on \(|E|\), both minor dimensions equal their respective \(d\) parameters. Step 3 makes the displayed minimum equal to \(d(M)-1\) for *every* available splitting element, and hence \(\ell(M)=d(M)\). This completes the proof.

**Equivalent extremal description.** Every independent-and-coindependent \(S\) is included in some basis \(B_1\) and disjoint from a basis \(B_2\); then \(|B_1\setminus B_2|\ge|S|\). Conversely, \(S=B_1\setminus B_2\) is independent in \(M\) and coindependent because \(B_2\) is contained in its complement. Taking maxima gives the basis-pair formula.

## Verification
The attached `check.py` enumerates bases, membership traces, full Littlestone recursion, basis-pair distances and rank-minimum values on sample finite graphic, binary-representable, uniform and partition matroids. Its `check_output.txt` records the successful replay. These computations corroborate the theorem only on the enumerated finite examples; the general proof rests on the matroid-intersection theorem, rank duality and exact deletion--contraction identities above. Reproduce using `python check.py` in Python 3.9 or later.

## Relationship to prior work
Guingona, Kolesnikov, Nierwinski and Soucy (2021), arXiv:2109.04805, Theorem 3.10, prove equality of VC and Littlestone dimensions for a different family: zero sets of nontrivial linear combinations of independent functions. Their hypotheses do not describe the basis-indicator family of an arbitrary matroid. Mofidi (2022), Theorem 3.3(1), characterizes shattered supports for spanning-tree hypergraphs of connected graphs as acyclic edge sets whose removal leaves the graph connected. That is precisely the graphic-matroid specialization of Step 1; it does not establish the online dimension or the all-matroid equality above. The rank formula comes from the classical matroid-intersection min--max theorem, and is not claimed as an independent new rank formula. The research contribution is the identified universal coincidence with Littlestone rank and its deletion--contraction argument.

## Limitations
The theorem concerns exactly the class of *all bases* of one finite matroid, not arbitrary constant-cardinality set families, independent-set classes, or arbitrary restrictions of the basis family. It does not assert equality for those other classes. Independent mathematical validation has not been performed; the available literature search does not establish absolute historical priority. A 2024 sample-compression study of oriented-matroid complexes addresses a different family of sign-vector systems and has not been exhaustively ruled out as a source of potentially related methods.

## References
1. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1, 10 September 2021, Theorem 3.10, https://arxiv.org/pdf/2109.04805.
2. A. Mofidi, *On the VC-dimension, covering and separating properties of the cycle and spanning tree hypergraphs of graphs*, Transactions on Combinatorics 11(1) (2022), 29–43, Theorem 3.3, https://doi.org/10.22108/TOC.2021.127880.1832.
3. J. Edmonds, the classical matroid-intersection min--max theorem (maximum common independent-set cardinality); used as an established theorem, not attributed as new.
4. V. Chepoi, K. Knauer and M. Philibert, *Labeled sample compression schemes for complexes of oriented matroids*, related background on VC dimension and oriented-matroid sign-vector classes; https://pageperso.lis-lab.fr/~kolja.knauer/COMpression_bis_repetita_bis.pdf.
