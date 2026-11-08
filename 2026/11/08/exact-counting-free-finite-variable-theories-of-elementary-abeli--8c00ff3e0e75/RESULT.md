# Exact counting-free finite-variable theories of elementary abelian two-groups in the relational group language

## Finding

Let \(V_d\) denote \((\mathbb F_2^d;R,0)\) for each integer \(d\geq0\), where \(R(x,y,z)\) means \(x+y=z\) and \(0\) names the identity. Consider ordinary first-order logic \(\mathrm{FO}^k\) with equality, at most \(k\) reusable individual-variable symbols, no counting or generalized quantifiers, and unbounded quantifier rank. Set
\[
\tau(k)=\begin{cases}k,&1\leq k\leq3,\\k-1,&k\geq4.\end{cases}
\]
**Theorem.** For all \(d,e\geq0\) and \(k\geq1\),
\[
V_d\equiv_{\mathrm{FO}^k}V_e\quad\Longleftrightarrow\quad\min(d,\tau(k))=\min(e,\tau(k)).
\]
Hence this family realizes exactly \(\tau(k)+1\) distinct \(k\)-variable theories. For \(d\geq3\), the smallest variable width that identifies \(V_d\) among these structures is \(d+2\); the widths for dimensions \(0,1,2\) are respectively \(1,2,3\). The hierarchy has a plateau between three and four variables, and is otherwise strict. In particular, the nonisomorphic groups \((\mathbb Z/2\mathbb Z)^4\) and \((\mathbb Z/2\mathbb Z)^5\), of orders \(16\) and \(32\), satisfy exactly the same \(\mathrm{FO}^5\) sentences in this relational vocabulary, but are separated by a sentence of \(\mathrm{FO}^6\).

## Assumptions and scope

All dimensions are nonnegative integers; \(V_0\) is the one-element group. The vocabulary is **relational**, consisting of a ternary graph-of-addition relation \(R\), a distinguished identity constant \(0\), and equality. There is no addition function symbol: replacing \(R\) by a binary function symbol changes the available atomic formulas and invalidates the stated counting-free variable bound. Logical equivalence quantifies over *all* sentences in the indicated fixed-variable fragment, regardless of quantifier rank. The characterization is relative to the displayed family, not all finite groups.

## Proof

**1. A sharp lower-variable obstruction for widths at least four.** Fix \(k\geq4\). In a position with at most \(k\) matched pebble pairs, require that for every *proper* subset of the currently occupied variable positions, the corresponding vector sums vanish on one side exactly when they vanish on the other. In characteristic two, these conditions are precisely the linear dependencies supported on fewer than \(k\) pebble positions. They imply agreement on equality with \(0\), equality of pebble values, and all ternary \(R\)-atoms, including atoms with repeated variables and identity constants: their zero-sum constraints are supported on at most three positions. Thus the relation preserves every atomic formula in this signature.

Assume both dimensions are at least \(k-1\). When Spoiler relocates one pebble, delete its old pair. The remaining at most \(k-1\) paired vectors have **all** their linear dependencies matched (any dependence uses a proper subset of the \(k\) possible positions). Consequently the linear map defined by matching those vectors is a well-defined isomorphism between their spans. If Spoiler chooses a vector in the pinned span, Duplicator uses its image. If Spoiler chooses one outside the span and the pinned rank is at most \(k-2\), both spaces contain a vector outside their pinned spans, so Duplicator also chooses outside. If the pinned rank is exactly \(k-1\), all \(k-1\) pinned vectors are independent. If the other space has a vector outside its pinned span Duplicator may use it; otherwise Duplicator takes the sum of all \(k-1\) pinned vectors. The latter choice introduces exactly one new dependency, supported on the **full** set of \(k\) occupied positions, which our invariant intentionally ignores. Even if Spoiler's chosen vector has the same full-support dependency, either response is permissible. The invariant is restored in both directions. The game can therefore continue for any number of rounds, establishing
\[
V_d\equiv_{\mathrm{FO}^k}V_e\qquad(d,e\geq k-1,\ k\geq4).
\]
The point of the full-support exception is that \(R\) has arity three: a dependence requiring four or more simultaneous variables is not itself an atomic constraint.

**2. The one-, two-, and three-variable obstruction.** With at most \(k\leq3\) pebbles, use the stronger invariant matching *all* dependencies of the pebbled vectors. When both dimensions are at least \(k\), after moving one pebble the other \(k-1\) vectors span a space of dimension at most \(k-1\), so either structure can realize the same choice inside or outside that span. This proves \(V_d\equiv_{\mathrm{FO}^k}V_e\) whenever \(d,e\geq k\), for \(k\in\{1,2,3\}\).

**3. Explicit distinguishing sentences below the saturation threshold.** The following sentences distinguish dimensions \(0/1\), \(1/2\), and \(2/3\), respectively: \(\exists x\,(x\ne0)\); \(\exists x\exists y\,(x\ne0\land y\ne0\land x\ne y)\); and
\[
\exists x\exists y\exists z\;[x,y,z\ne0\ \land\ x,y,z\text{ pairwise distinct}\ \land\ \neg R(x,y,z)].
\]
The last sentence asserts the presence of three linearly independent vectors in a binary vector space. In particular, it distinguishes dimension two from dimension three using three variable names.

For each \(m\geq3\), there is a formula \(\Sigma_m(x_1,\ldots,x_m)\) expressing \(x_1+\cdots+x_m=0\) with at most \(m+1\) different variable names in total. The base cases are \(\Sigma_1(x_1)\equiv(x_1=0)\), \(\Sigma_2(x_1,x_2)\equiv(x_1=x_2)\), and \(\Sigma_3(x_1,x_2,x_3)\equiv R(x_1,x_2,x_3)\). For \(m\geq4\), introduce an accumulator for the sum of the first two entries, then successively add entries through \(x_{m-2}\) and finally test that the last accumulator plus \(x_{m-1}\) equals \(x_m\). At each step, the already-consumed name \(x_1\) and a single auxiliary name \(z\) alternate as locally bound accumulators, so no additional names occur. For example,
\[
\Sigma_5(x_1,x_2,x_3,x_4,x_5)\;\equiv\;\exists z\,[R(x_1,x_2,z)\land\exists x_1\,(R(z,x_3,x_1)\land R(x_1,x_4,x_5))].
\]
The inner binding of \(x_1\) is harmless: its earlier occurrence has already been evaluated outside the new scope.

For \(m\geq3\), the finite conjunction
\[
\operatorname{Ind}_m:=\exists x_1\cdots\exists x_m\;\bigwedge_{\varnothing\ne S\subseteq\{1,\ldots,m\}}\neg\Sigma_{|S|}((x_i)_{i\in S})
\]
expresses existence of \(m\) independent vectors and uses only \(m+1\) distinct names. (For one- and two-element subsets use the specified base formulas.) It is true exactly in \(V_d\) with \(d\geq m\). Thus, for \(k\geq4\), any dimension \(d<k-1\) is separated from any greater one by \(\operatorname{Ind}_{d+1}\) when \(d\geq2\), using at most \(d+2\leq k\) names, and by the earlier small formulas when \(d\leq1\). For \(k\leq3\), the three small formulas handle all dimensions below \(k\).

Combining the saturation strategies and distinguishing sentences establishes the equivalence criterion. Truncating the dimension at the stated threshold yields the exact number of theories; requiring a formula for \(d+1\) independent vectors gives the claimed individual defining widths. The explicit witness in dimension four requires six variables, and its five-variable impossibility follows from the infinite-round strategy.

## Verification

Run `python3 verify_pebble.py` with Python 3 standard library. The accompanying `verify_output.txt` records its expected output. The script enumerates vector-tuple orbits by their binary linear-dependence kernels and tests, for widths four, five, and six and dimensions \((3,4)\), \((4,5)\), and \((5,6)\), that corresponding positions with the same proper-subset dependence signatures have exactly matching one-pebble successor signatures. It also verifies that every five-element subset of \(\mathbb F_2^4\) is dependent, all nonempty subsets of a five-vector basis of \(\mathbb F_2^5\) have nonzero sum, and the displayed five-term addition-chain formula evaluates correctly on specified tuples. These are finite corroborations; only the proof above establishes all dimensions and all rounds.

## Relationship to prior work

Gomaa's dissertation (2007), chapter 3, Definition 3.1 and Corollary 3.8, and his conference article (2008), Definition 1 and Corollary 40, use the same ternary group-operation relation plus identity constant. They assert an existential **five-variable** distinguishing sentence for every pair of nonisomorphic finite abelian groups. The two groups \(V_4\) and \(V_5\) contradict this unconditional assertion, even allowing unrestricted quantifier depth and quantifier alternation. In the inspected proof, the inference that nonisomorphic direct products yield different *sets* of cyclic component orders omits multiplicity: both these groups have component-order set \(\{2\}\), but four and five factors, respectively. This comparison concerns the stated universal five-variable result, not the separately established special-case cyclic-group bounds. A 2010 journal article by Gomaa repeats the five-variable assertion in its accessible abstract; its restricted full text was not verified, and no stronger conclusion about that version's detailed argument is drawn.

The finite-variable game results for groups without abelian normal subgroups by Grochow and Levet (2022) concern different group classes and/or enriched logical resources, hence do not cover these elementary abelian groups. Related work on prime-cyclic groups and on unbounded-variable EF rounds does not imply this bounded-variable dimension classification. The principal contribution here is the complete threshold theorem and the concrete counterfamily; the standard pebble-game characterization itself is background rather than claimed novelty.

## Limitations

The exact result holds only over elementary abelian two-groups with **relational** addition and a named zero. It makes no assertion for function-symbol group languages, other finite abelian groups, counting logic, generalized quantifiers, or quantifier-rank minima. An unlocated prior theorem about relational vector spaces could imply the classification, and further historical-priority checking is warranted. The computation samples fixed small dimensions and does not substitute for the infinite proof. Independent mathematical audit has not been performed.

## References

1. Walid Gomaa, *Model Theory and Complexity Theory*, doctoral dissertation, University of Maryland, public repository date 2007-07-06, chapter 3, Definition 3.1 and Corollary 3.8. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440
2. Walid Gomaa, *The Complexity of Identifying Finite Abelian Groups*, TMFCS 2008, Definition 1 and Corollary 40. https://www.researchgate.net/publication/221325692_The_Complexity_of_Identifying_Finite_Abelian_Groups
3. Walid Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20(8) (2010), 1087–1116, DOI 10.1142/S0218196710006047. Abstract inspected, full journal text not verified.
4. Joshua A. Grochow and Michael Levet, *On the Descriptive Complexity of Groups without Abelian Normal Subgroups*, 2022, https://arxiv.org/abs/2209.13725
