# A sharp branching criterion and every countable stabilization rank for omega accumulation on prefix trees

## Finding

Let \(T\subseteq\mathbb N^{<\omega}\) be any nonempty, prefix-closed tree. Endow it with the Alexandrov topology of upward-closed sets for the prefix order. For \(A\subseteq T\), write
\[
\Omega_T(A)=\{s\in T:|A\cap T_s|=\infty\},\qquad T_s=\{t\in T:s\preceq t\}.
\]
This is the \(\omega\)-accumulation operator, equivalently the purely nonstandard halo diamond in Montacute's terminology [1].

**Branching classification.** The operator is idempotent on **every** subset of \(T\) precisely when \(T\) is finitely branching:
\[
(\forall A\subseteq T)\ \Omega_T^2(A)=\Omega_T(A)
\quad\Longleftrightarrow\quad
(\forall s\in T)\ |\operatorname{Child}_T(s)|<\infty.
\]

**Exact ordinal spectrum on one space.** Fix once and for all the countable space \(X=\mathbb N^{<\omega}\). For any prefix-closed \(A\subseteq X\), let \(A_0=A\), \(A_{\alpha+1}=\Omega_X(A_\alpha)\), and \(A_\lambda=\bigcap_{\alpha<\lambda}A_\alpha\) for each nonzero limit ordinal \(\lambda\). Let \(\rho(A)\) be the least ordinal satisfying \(A_\rho=A_{\rho+1}\). Then
\[
\{\rho(A): A\subseteq X\text{ prefix-closed}\}=\{\alpha:\alpha<\omega_1\}.
\]
Every countable successor stage has a **well-founded** prefix-tree witness that vanishes at that stage; every countable nonzero limit stage has a witness that stabilizes to a nonempty infinite spine. Thus the supremum of the stabilization stages is \(\omega_1\), which is not attained. In particular, arbitrarily long transfinite transients occur on a single countable non-\(T_1\) space, despite the depth-one collapse on each finitely branching prefix space.

## Assumptions and scope

Here \(\mathbb N=\{0,1,2,\ldots\}\), \(\mathbb N^{<\omega}\) is the set of finite strings, \(\emptyset\) its root, and \(s\preceq t\) means that \(s\) is an initial segment of \(t\). A prefix tree includes every prefix of each of its nodes. A node's immediate children are the nodes obtained by appending exactly one symbol. A *well-founded* tree has no infinite prefix-increasing chain. The basic open neighborhood of \(s\) is \(T_s\), so all open neighborhoods of \(s\) meet \(A\) infinitely exactly when \(T_s\cap A\) is infinite.

The ordinal iterates are taken on arbitrary subsets for the first classification, and on **prefix-closed subsets** for the second. This condition makes \(\Omega_X(A)\subseteq A\), so the transfinite trajectory is decreasing. There are no effectiveness or computability restrictions on witness trees; the theorem uses ordinary countable ordinal induction.

## Proof

**1. Operator facts.** Every \(\Omega_T(A)\) is prefix-closed. If \(s\preceq t\) and \(t\in\Omega_T(A)\), then \(A\cap T_s\supseteq A\cap T_t\) is infinite. For all \(A\subseteq T\) one also has \(\Omega_T^2(A)\subseteq\Omega_T(A)\): if \(s\in\Omega_T(\Omega_T(A))\), there exists \(t\in T_s\cap\Omega_T(A)\), and \(A\cap T_t\subseteq A\cap T_s\) is infinite. (The stronger premise that there are infinitely many such \(t\) is not required for this direction.) Finally, for prefix-closed \(A\), \(\Omega_T(A)\subseteq A\), since an infinite nonempty intersection \(A\cap T_s\) contains an extension of \(s\) lying in \(A\).

**2. Finite branching is sufficient.** Suppose every node has finitely many children, and take \(s\in\Omega_T(A)\). The set \(A\cap T_s\) is infinite. As the singleton \(\{s\}\) contributes at most one node, some immediate child \(s_1\) must have \(A\cap T_{s_1}\) infinite. Repeating constructs an infinite strict chain \(s=s_0\prec s_1\prec s_2\prec\cdots\), entirely contained in \(\Omega_T(A)\). Hence \(\Omega_T(A)\cap T_s\) is infinite, so \(s\in\Omega_T^2(A)\). Together with Step 1 this gives equality on all subsets, with no assumption that \(A\) is prefix-closed.

**3. Finite branching is necessary.** Conversely, suppose \(s\in T\) has infinitely many immediate children, and let \(A\) consist of those children. Then \(s\in\Omega_T(A)\), and the only points of \(\Omega_T(A)\) are the finitely many prefixes of \(s\), including \(s\): any strict extension of \(s\) lies in the cone of at most one selected immediate child and so sees at most one point of \(A\). Thus \(\Omega_T(A)\) is finite and \(\Omega_T^2(A)=\varnothing\), proving nonidempotence.

**4. Singleton-ended witness trees at each countable ordinal.** We construct, by transfinite recursion, a nonempty prefix-closed well-founded subtree \(B_\alpha\subseteq X\) for every countable ordinal \(\alpha\), with
\[
(\Omega_X)^\alpha(B_\alpha)=\{\emptyset\},\qquad (\Omega_X)^{\alpha+1}(B_\alpha)=\varnothing,
\]
and with the root present at every prior stage. Start with \(B_0=\{\emptyset\}\). If \(\alpha=\beta+1\), attach a copy of \(B_\beta\) below each child \(\langle n\rangle\) of a new root, for all \(n\in\mathbb N\). If \(\alpha\) is a nonzero countable limit, choose an increasing cofinal sequence \(\beta_n<\alpha\) and attach \(B_{\beta_n}\) below child \(\langle n\rangle\).

To justify the recursion, for a child cone \(\langle n\rangle^\frown X\), membership in the \(\Omega\)-image depends **only** on that cone. This locality persists through successor operations and intersections at limits, by transfinite induction. A copy of \(B_\beta\) therefore has its root alive through stage \(\beta\) and disappears by \(\beta+1\), independently of the other child cones. For a successor parent \(B_{\beta+1}\), infinitely many child roots survive at each stage at most \(\beta\); thus the parent root survives through \(\beta+1\), while all children vanish at that stage. For a limit parent \(B_\alpha\), at every \(\gamma<\alpha\) infinitely many child roots have \(\beta_n\ge\gamma\); hence the parent root survives at all successor stages below \(\alpha\) and therefore at the limit stage \(\alpha\). Each individual child vanishes by its stage \(\beta_n+1<\alpha\), leaving only the root. A final \(\Omega\) removes that singleton. The trees are countable and prefix-closed. They are well-founded by induction: an infinite branch would pass to one attached \(B_\beta\), but these have none. Thus \(B_\alpha\) has least stabilization stage exactly \(\alpha+1\).

**5. Every nonzero countable limit is a stabilization stage.** Let \(\lambda<\omega_1\) be a nonzero limit, and choose an increasing cofinal sequence \(\alpha_n<\lambda\). Let \(S=\{0^n:n\in\mathbb N\}\) be the infinite zero spine (\(0^0=\emptyset\)); define
\[
C_\lambda=S\ \cup\ \bigcup_{n\in\mathbb N}
\{0^n{}^\frown\langle 1\rangle{}^\frown t:t\in B_{\alpha_n}\}.
\]
The union is prefix-closed. Every spine vertex has infinitely many spine descendants and hence remains in every transfinite \(\Omega\)-iterate (by induction). Each side branch is a child cone isolated from the other side branches; the locality argument in Step 4 shows it disappears by stage \(\alpha_n+1<\lambda\). Consequently \(C_{\lambda,\lambda}=S\). Since \(\Omega_X(S)=S\), the iteration stabilizes at stage \(\lambda\). It cannot stabilize earlier: for every \(\gamma<\lambda\), pick \(n\) with \(\alpha_n\ge\gamma\); the root of that side branch still belongs to the stage-\(\gamma\) set, so that set properly contains \(S\). If an iteration ever stabilizes at a successor comparison, monotonicity makes it constant thereafter; therefore its first stabilization is exactly \(\lambda\).

**6. The zero rank and the upper bound.** The empty set has stabilization ordinal zero. For any prefix-closed \(A\subseteq X\), the ordinal iterates form a decreasing sequence; if no stage \(\alpha<\omega_1\) stabilized, then each difference \(A_\alpha\setminus A_{\alpha+1}\) would be nonempty. Choosing a removed node for every \(\alpha<\omega_1\) would inject \(\omega_1\) into countable \(X\), impossible. Therefore \(\rho(A)<\omega_1\). Steps 4, 5 and the empty set attain all countable ordinals, completing the classification.

## Verification

The core conclusions follow from the preceding explicit transfinite induction, not from finite experiments. As concrete boundary checks: a single root has stages \(\{\emptyset\},\varnothing\), giving stabilization ordinal \(1\); a root with infinitely many terminal children has stages \(B_1,\{\emptyset\},\varnothing\), giving ordinal \(2\). For each finite integer \(h\ge0\), the tree of strings of length at most \(h\) has successive stages equal to its levels truncated at length \(h-j\) for \(0\le j\le h\), followed by the empty set; this agrees with Step 4 for finite ordinals. An infinite chain \(S\) satisfies \(\Omega_X(S)=S\) and provides the permanent kernel of Step 5.

The proof establishes exact results for every countable ordinal and arbitrary prefix trees. No enumeration of finite truncations is presented as a certificate for transfinite assertions.

## Relationship to prior work

Montacute [1, Sections 6.1–6.3] identifies the purely nonstandard halo operation with \(\omega\)-accumulation, proves universal \(\Omega^2\subseteq\Omega\), and develops a transfinite \(\omega\)-Cantor–Bendixson decomposition. Those statements are premises and **not** claimed here as new. The additional conclusions here are the **if-and-only-if finite-branching criterion for equality on all inputs** and the **exact ranks for valuations in one fixed countable Alexandrov prefix space**. The original decomposition alone does not supply this sharp threshold or the fixed-space realization scheme.

The combinatorics of ordinal ranks and well-founded trees is classical [2,3]. In particular, Clote [2] studies ranks of well-founded portions of recursive trees and a distinct Cantor–Bendixson operation on infinite branches; that is not this countably-infinite-cone operation on the nodes. In \(T_1\) spaces, the two derivative notions agree and classical scattered sets can also exhibit arbitrary countable ranks. The finding does **not** assert the first realization of large ordinal ranks in topology; its scope is the sharp branching comparison and one specified **countable, non-\(T_1\)** Alexandrov space.

## Limitations

The rank realization uses potentially noncomputable prefix-closed sets and ordinals; effective ranks for computable valuations are not classified. The finite-branching criterion is for prefix trees with their upward Alexandrov topology, not for arbitrary topological spaces or unrelated modal operators. The full space \(X\) is itself a fixed point of \(\Omega\); the nontrivial ranks arise by varying the valuation \(A\). Historical equivalence with other tree-pruning terminology remains a possibility. Independent mathematical verification has not been performed.

## References

1. Yoàv Montacute, “Halo Semantics for Modal Logic”, first posted June 30, 2026, arXiv:2606.31885, especially Theorem 6.4, Lemma 6.15 and Theorem 6.14. https://arxiv.org/abs/2606.31885
2. Peter Clote, “On Recursive Trees with a Unique Infinite Branch”, *Proceedings of the American Mathematical Society* 93 (1985), 335–342, doi:10.1090/S0002-9939-1985-0770549-2.
3. Classical well-founded tree rank recursion and Kőnig's infinity lemma; used here as standard supporting mathematics rather than attributed as new.
