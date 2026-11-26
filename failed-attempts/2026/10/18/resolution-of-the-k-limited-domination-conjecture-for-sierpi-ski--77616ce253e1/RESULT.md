# Resolution of the \(k\)-limited domination conjecture for Sierpiński graphs

## Finding

**Theorem.** Let \(n\ge1\), \(m\ge2\), and \(1\le k\le m-1\) be integers. For the classical Sierpiński graph \(S(n,m)\),
\[
\boxed{\gamma_k^{\mathrm L}(S(n,m))=(m-k)m^{n-1}.}
\]
Here \(\gamma_k^{\mathrm L}\) is the minimum cardinality of a dominating set in which each selected vertex has at most \(k\) neighbors outside the set. The theorem establishes Conjecture 12 of Božović (arXiv:2610.01584, 1 October 2026) in its full stated range. The previously established cases \(k=1\) and \(m=3\) are included, but the claimed advance is the unrestricted remaining range, particularly \(m\ge4\) and \(2\le k\le m-1\).

The upper bound has a uniform explicit construction: omit vertices according to an even-degree circulant relation on their final two symbols. The lower bound uses a two-level clique charging argument and does not assume that every base clique meets the dominating set.

## Assumptions and scope

Let \(A=\{0,1,\ldots,m-1\}\). The vertices of \(S(n,m)\) are words \(u=(u_1,\ldots,u_n)\in A^n\). Distinct words \(u,v\) are adjacent precisely when there is an index \(h\in\{1,\ldots,n\}\) with
\[
 u_t=v_t\quad(t<h),\qquad u_h\ne v_h,\qquad
 u_t=v_h,\ v_t=u_h\quad(t>h).
\]
For \(n=1\) this gives \(K_m\). A set \(D\subseteq V(G)\) dominates when every vertex outside \(D\) has a neighbor in \(D\). It is \(k\)-limited when, in addition, \(|N_G(x)\setminus D|\le k\) for every \(x\in D\). All vertices are distinctly labelled by their words; no graph isomorphism quotient is used in the count or cardinality.

For \(n\ge2\), a **base clique** \(B_p\) is the induced \(K_m\) on words \((p,a)\), with \(p\in A^{n-1}\) and \(a\in A\). There are \(m^{n-1}\) disjoint base cliques. An edge between different base cliques is called a **link**. Their clique-level quotient is \(S(n-1,m)\): two prefixes \(p,q\) are adjacent precisely when one link joins \(B_p\) to \(B_q\). Every vertex of \(S(n,m)\) lies on at most one link. These facts follow directly from the word adjacency rule, as detailed below.

## Proof

**1. Structural fact about links.** For a word \(u\), a link at index \(h<n\) can occur only when \(u_h\ne u_{h+1}=\cdots=u_n\). Hence, if there is such an index, it is uniquely determined: it is the symbol immediately preceding the final constant suffix. It follows that no vertex is incident with two links. For adjacent base prefixes \(p,q\), the defining first-disagreement index uniquely specifies the last symbol of the corresponding endpoint in each of \(B_p,B_q\), so there is exactly one link. Conversely, projecting a link onto its prefixes produces the defining adjacency of \(S(n-1,m)\). In particular, every constant prefix has degree \(m-1\) in the quotient, and every nonconstant prefix has degree \(m\): the full graph \(S(t,m)\) has precisely the \(m\) constant words of degree \(m-1\), with all other vertices of degree \(m\).

**2. Upper bound.** For \(n=1\), any \(m-k\) vertices of \(K_m\) form a \(k\)-limited dominating set, so assume \(n\ge2\). Put
\[
 r=2\lfloor k/2\rfloor,\qquad \varepsilon=k-r\in\{0,1\}.
\]
On \(A\), take the simple undirected circulant graph \(H_r\) joining each \(a\) to \(a\pm1,\ldots,a\pm(r/2)\pmod m\). Because \(r\le m-1\) and is even, these neighbors are distinct and \(H_r\) is \(r\)-regular; \(H_0\) is edgeless. Define a symmetric binary relation \(R\subseteq A^2\) by
\[
 (a,b)\in R\quad\Longleftrightarrow\quad
 \big(\varepsilon=1\ \text{and}\ a=b\big)\ \text{or}\ \{a,b\}\in E(H_r).
\]
Every row of \(R\) has exactly \(r+\varepsilon=k\) entries, and every diagonal entry has the same membership status \(\varepsilon\).

Let \(U\) contain exactly those words whose last two symbols \((u_{n-1},u_n)\) belong to \(R\), and let \(D=A^n\setminus U\). Each base clique has exactly \(k\) vertices in \(U\) and \(m-k\ge1\) in \(D\). Thus every vertex of \(U\) is dominated inside its base clique. A selected vertex has exactly \(k\) neighbors in \(U\) within that clique.

No link joins \(D\) to \(U\). Indeed, if a link has first-disagreement index \(h=n-1\), the last two symbols at its endpoints are \((a,b)\) and \((b,a)\), and these have the same membership in the symmetric relation \(R\). If \(h\le n-2\), the last two symbols at its endpoints are \((a,a)\) and \((b,b)\), and all diagonal pairs have the same membership in \(R\). Consequently, every selected vertex has exactly \(k\) neighbors outside \(D\), all inside its base clique. We have therefore constructed a \(k\)-limited dominating set of size
\[
 |D|=(m-k)m^{n-1}.
\]
This proves the claimed upper bound.

**3. Lower bound.** Fix an arbitrary \(k\)-limited dominating set \(D\) of \(S(n,m)\) for \(n\ge2\), and let \(d_p=|D\cap B_p|\). If \(d_p>0\), then any selected vertex in that clique is adjacent to all \(m-d_p\) omitted vertices of the clique. Hence
\[
 d_p>0\quad\Longrightarrow\quad d_p\ge m-k.
\]
Call a prefix \(p\) **empty** if \(d_p=0\). Every vertex in \(B_p\) must then have a selected neighbor outside \(B_p\). There is at most one link at each vertex, and different quotient neighbors correspond to different links. Thus an empty prefix has full quotient degree \(m\) and, for **every** neighbor \(q\) of \(p\) in \(S(n-1,m)\), the linked vertex of \(B_q\) belongs to \(D\). That selected vertex has a neighbor outside \(D\) in \(B_p\), in addition to all \(m-d_q\) omitted neighbors in its own base clique. Therefore
\[
 p\text{ empty},\ q\sim p\quad\Longrightarrow\quad
 m-d_q+1\le k,\quad d_q\ge m-k+1.
\]

Partition the vertex set of the quotient \(S(n-1,m)\) into its own base cliques of order \(m\). When \(n=2\), the entire quotient \(S(1,m)=K_m\) is a single such clique. In one quotient clique \(Q\), either no prefix is empty, in which case \(\sum_{p\in Q}d_p\ge m(m-k)\), or one prefix is empty. Two empty prefixes cannot occur in the same \(Q\): they are adjacent, but every neighbor of an empty prefix has at least \(m-k+1\ge2\) selected vertices in its base clique. If \(p\in Q\) is the unique empty prefix, all other \(m-1\) prefixes are its quotient neighbors and satisfy the stronger bound. Hence
\[
 \sum_{q\in Q}d_q\ge(m-1)(m-k+1)
 =m(m-k)+(k-1)\ge m(m-k).
\]
Summing this inequality over the disjoint quotient cliques yields
\[
 |D|=\sum_{p\in A^{n-1}}d_p\ge(m-k)m^{n-1}.
\]
The lower and upper bounds coincide. For \(n=1\), the assertion was proved in Step 2. This completes the proof for every integer \(n\ge1\), \(m\ge2\), \(1\le k\le m-1\). \(\square\)

## Verification

The accompanying standard-library Python program reconstructs the graph adjacency independently from the first-difference definition and from a separate edge-generation rule. It compares these on 16 graph instances, directly checks the proposed sets on 75 parameter cases, and checks the quotient-link structure on 12 graph instances. It also exhaustively computes minima for 22 small parameter cases, inspecting 198,420 subset masks. All checks completed successfully. The structural proof, not the finite computation, establishes the unrestricted theorem. Run \(\texttt{python3 verify_sierpinski.py}\) from the directory containing the script.

## Relationship to prior work

Božović, *On \(k\)-limited domination: complexity and Sierpiński graphs* (arXiv:2610.01584v1, 1 October 2026), proves the formula for \(k=1\) and for \(m=3\) and states the displayed general equality as Conjecture 12 on page 9. The present result establishes the conjecture in its stated full range. The foundational paper by Božović, Kovijanić Vukićević, Radić and Tepeh (arXiv:2606.22422; DOI 10.1007/s40314-026-03902-2) gives general bounds, the complete-graph case, and regular-graph comparisons with \((1,t)\)-domination; these bounds do not determine the formula on nonregular Sierpiński graphs. Tepeh (arXiv:2606.22428) studies computational complexity and Cartesian-product families. Liu (arXiv:2008.09807) concerns ordinary, Roman and double Roman domination on the same graph family; those are different invariants.

The new proof uses a uniform final-symbol circulant construction and a quotient-clique lower-bound charging argument. It does not assert novelty for previously proven special cases or for elementary circulant regularity.

## Limitations

The theorem concerns the classical Sierpiński graphs built from complete alphabets, not arbitrary generalized Sierpiński graphs over an input graph. The proof determines the **minimum size** of \(k\)-limited dominating sets, not their total number or a classification of all minimizers. The parameter range \(k\ge m\) is not addressed; no extrapolation is claimed. This mathematical proof and its program were checked in one review; independent audit and definitive literature priority have not been established.

## References

1. D. Božović, *On \(k\)-limited domination: complexity and Sierpiński graphs*, arXiv:2610.01584v1 (first posted 2026-10-01), Section 5 and Conjecture 12, p. 9. https://arxiv.org/pdf/2610.01584
2. D. Božović, Ž. Kovijanić Vukićević, G. Radić and A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422 (2026); DOI 10.1007/s40314-026-03902-2. https://link.springer.com/article/10.1007/s40314-026-03902-2
3. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428 (2026). https://arxiv.org/abs/2606.22428
4. C.-A. Liu, *Domination in the Sierpiński graphs \(S(K_n,t)\)*, arXiv:2008.09807 (2020). https://arxiv.org/abs/2008.09807
