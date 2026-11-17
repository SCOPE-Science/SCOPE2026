# Normality and the exact census of two-agent someone-knows frames

## Finding
Let two named S5 agents have equivalence relations \(E\) and \(F\). The bundled modality "someone knows" becomes a normal modal operator **if and only if** the two equivalence classes through every world are comparable by inclusion. On such frames it is extensionally identical to distributed knowledge, whose accessibility is \(E\cap F\). This modal characterization has an exact structural and enumerative consequence: the connected components are oriented refinements of a single equivalence class, and both the labelled and unlabelled numbers admit closed generating functions.

Write \(B_k\) for the Bell number of partitions of a labelled \(k\)-element set, and \(p(k)\) for the number of integer partitions of \(k\). The number \(a_n\) of ordered pairs of equivalence relations on the labelled set \([n]\), with the named agent roles distinguished, satisfying normality is
\[
\sum_{n\ge0}a_n\frac{z^n}{n!}=\exp\!\left(2e^{e^z-1}-e^z-1\right).
\]
The number \(u_n\) of isomorphism types of these pairs under permutations of worlds **without swapping the agents** is
\[
\sum_{n\ge0}u_nz^n=\prod_{k\ge1}\frac{1}{(1-z^k)^{2p(k)-1}}.
\]
Their respective initial values, beginning with the formal empty coefficient, are \(1,1,4,19,111,774,6229\) and \(1,1,4,9,24,52\). For fixed \(n\ge1\), the exact fraction of normal ordered pairs of S5 relations is \(a_n/B_n^2\).

## Assumptions and scope
Fix a nonempty finite set \(W\) of worlds and equivalence relations \(E,F\subseteq W\times W\). Write \([w]_E\) and \([w]_F\) for their classes. For every truth set \(X\subseteq W\), define the usual box truth-set operator \(K_E(X)=\{w:[w]_E\subseteq X\}\), similarly \(K_F\), and the someone-knows operator \(S(X)=K_E(X)\cup K_F(X)\). The distributed-knowledge box is \(K_{E\cap F}\). "Normal" means the bundled modality validates the normal distribution axiom for all propositional valuations (equivalently, preserves binary meets, since it preserves the top truth set and is monotone). All asserted operators act on the full power set of worlds; no restricted valuations are assumed.

The frame is *laminar* when, whenever an \(E\)-class \(A\) intersects an \(F\)-class \(B\), either \(A\subseteq B\) or \(B\subseteq A\). Its connected components mean equivalence classes of \(E\vee F\), the smallest equivalence relation containing both relations. The named relations are ordered: an isomorphism must preserve \(E\) and \(F\) separately. The empty structure is used only for the conventional constant coefficient of generating functions.

## Proof
**1. Pointwise operator equivalence.** If the two classes \([w]_E\) and \([w]_F\) are incomparable, take \(X=[w]_E\) and \(Y=[w]_F\). Then \(w\in S(X)\cap S(Y)\), but neither of the two classes is contained in \(X\cap Y\), so \(w\notin S(X\cap Y)\). Conversely, if the two classes are comparable, their intersection is their smaller class, so \(w\in S(X)\) precisely when \([w]_{E\cap F}\subseteq X\). This proves equivalence between meet preservation, pointwise class comparability and the equality \(S=K_{E\cap F}\); the blockwise laminar condition is exactly the pointwise comparability condition, because each intersecting pair shares some world.

To see that modal normality is equivalent to meet preservation, let \(S\) be the monotone top-preserving operator already defined. Meet preservation implies the usual distribution axiom by the inclusion \(S(X\Rightarrow Y)\cap S(X)\subseteq S(Y)\), where \(X\Rightarrow Y=(W\setminus X)\cup Y\). Conversely, validity of distribution for arbitrary valuations applied to \(X\) and \(Y\) follows from monotonicity \(S(Y)\subseteq S(X\Rightarrow (X\cap Y))\) together with the distribution axiom. If the laminar condition holds, a structural induction on modal formulas substitutes \(K_{E\cap F}\) for each occurrence of \(S\), including nested occurrences. Since \(E\cap F\) is an equivalence relation, the resulting operator is an S5 box.

**2. Connected components.** Consider a connected component \(C\) of the join \(E\vee F\). The collection of all \(E\)- and \(F\)-classes meeting \(C\) is a finite laminar family whose intersection graph is connected, because an \(E\vee F\) path corresponds to overlapping blocks. Choose a maximal block \(M\) in this family. Every block overlapping \(M\) is contained in it. Inducting along a path of overlapping blocks shows every block in the component is contained in \(M\), hence \(C=M\). If \(M\) is an \(E\)-class, \(E\) is universal on \(C\) and \(F\) is any partition of \(C\); symmetrically when \(M\) is an \(F\)-class. The descriptions overlap only when both relations are universal on \(C\). Conversely, an arbitrary disjoint union of such components has comparable classes everywhere, so this normal form is exhaustive and unique modulo the common-universal overlap.

**3. Labelled count.** On a fixed labelled \(k\)-set with \(k\ge1\), the previous dichotomy gives exactly \(c_k=2B_k-1\) connected pairs. By the exponential formula for assemblies of labelled components,
\[
A(z)=\exp\left(\sum_{k\ge1}(2B_k-1)\frac{z^k}{k!}\right).
\]
The Bell exponential generating function \(\sum_{k\ge0}B_k z^k/k!=e^{e^z-1}\) yields the claimed \(A(z)=\exp(2e^{e^z-1}-e^z-1)\). A reproducible integer recurrence obtained by differentiating \(A(z)\) is
\[
a_0=1,\qquad a_{n+1}=\sum_{j=0}^{n}\binom nj(2B_{j+1}-1)a_{n-j}.\]

**4. Unlabelled count.** A connected component of size \(k\) is specified, up to a world permutation, by an orientation (which agent has the universal class) and an integer partition of the \(k\) vertices giving the sizes of the other agent's classes. There are \(p(k)\) possibilities for each orientation, with the common-universal type counted twice; hence \(d_k=2p(k)-1\) types. An arbitrary unlabelled frame is a multiset of these connected types, so its ordinary generating function is the stated Euler product. The initial coefficients follow by standard integer partition recurrences. This proves the complete labelled and isomorphism counts.

## Verification
The standalone Python script `checker.py` uses only the standard library. Running `python checker.py` prints `NORMAL_BUNDLE_PARTITION_CENSUS_OK` upon success. It enumerates every ordered pair of set partitions for \(1\le n\le6\), checks that the laminar condition agrees with the labelled generating-function coefficients (44,168 pair checks), and for \(1\le n\le4\) independently enumerates all truth-set pairs to test binary meet preservation (255 frame checks). It also computes permutation-orbit classes through four worlds and checks the unlabelled Euler-product coefficients through five worlds. Finite testing supplements but does not establish the universal conclusions, which follow from the proof above.

## Relationship to prior work
Ågotnes and Wáng (2021) introduce the "somebody knows" modality and establish that it is not normal across the full class of Kripke or S5 models: conjunction closure fails on specific frames. Their work also gives neighborhood completeness and a complexity classification. Ding, Liu and Wang (2023) study its weakly aggregative logic through hypergraphs and neighborhood semantics; the accessible abstract and publisher preview establish that context but do not suffice to exclude hidden finite-frame enumeration results. Ding and Yang (first publicly posted March 27, 2026) develop a general theory of bundled modalities and, in particular, axiomatize someone-knows over S5 models. The present result addresses a distinct exact framewise question: which finite two-agent frames make the operator normal, and how many such frames exist with and without labels? The Bell and integer-partition enumeration ingredients, and labelled exponential formula, are classical and are not claimed as new.

## Limitations
The result is restricted to exactly two named agents, finite nonempty S5 frames, all Boolean valuations and standard Kripke semantics. It makes no assertion about three or more agents, KD45 frames, effective complexity or asymptotic estimates for the counts. It is possible that the laminarity criterion or an equivalent enumeration occurs in older specialist sources or a sequence database not successfully inspected; no independent historical-priority audit has been performed. The 2023 journal paper was inspected only through its available abstract and first-page publisher preview, not in full text. All core mathematical implications are established directly here and do not rely on those inaccessible sections.

## References
1. T. Ågotnes and Y. N. Wáng, *Somebody Knows*, Proceedings of KR 2021, doi:10.24963/kr.2021/1. Full article: https://proceedings.kr.org/2021/1/kr2021-0001-agotnes-et-al.pdf
2. Y. Ding, J. Liu and Y. Wang, *Someone Knows That Local Reasoning on Hypergraphs is a Weakly Aggregative Modal Logic*, Synthese 201 (2023), doi:10.1007/s11229-022-04032-y.
3. Y. Ding and Y. Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268v1, first public March 27, 2026, https://arxiv.org/abs/2603.26268 .
4. Classical set-partition and labelled exponential formula identities, e.g. the exponential formula in labelled enumerative combinatorics.
