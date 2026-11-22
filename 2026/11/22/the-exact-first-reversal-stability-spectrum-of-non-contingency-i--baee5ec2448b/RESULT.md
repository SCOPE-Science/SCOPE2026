# The exact first-reversal stability spectrum of non-contingency introspection on tournaments

## Finding

For every integer \(n\ge3\), consider the transitive tournament with vertices \(1,\ldots,n\) and arcs \(a\to b\) whenever \(a<b\). Choose exactly one pair \(1\le i<j\le n\), reverse the arc \(i\to j\) to \(j\to i\), and call the resulting irreflexive Kripke frame \(T_{n;i,j}\). The non-contingency operator is \(\Delta\varphi:=\Box\varphi\lor\Box\neg\varphi\).

**Theorem.** The schema \(\Delta p\to\Delta\Delta p\) is valid on \(T_{n;i,j}\) under all Boolean valuations if and only if either \(j=i+1\) or \((i,j)=(n-2,n)\). Thus exactly \(n\) of the \(\binom n2\) distinct one-arc reversals preserve the axiom, and the precise preservation fraction is \(2/(n-1)\).

There is a stronger, position-sensitive statement. Define \(B(n;i,j)\) to be the total number of pairs \((s,x)\) of a one-point valuation \(V(p)=\{s\}\) and a world \(x\) at which \(\Delta p\to\Delta\Delta p\) fails on \(T_{n;i,j}\). Then

\[
B(n;i,j)=
\begin{cases}
0,&j=i+1\text{ or }(i,j)=(n-2,n),\\
2(j-i)-1,&i+2\le j<n,\\
1,&j=n\text{ and }i\le n-3.
\end{cases}
\]

In particular every invalid frame in this family is already refuted by a valuation true at only one world. The full-schema assertion quantifies over **all** valuations; the refined count \(B\) concerns only singleton valuations and does not count general countervaluations.

## Assumptions and scope

A tournament is a finite loop-free complete orientation. Its directed arcs are used as the Kripke accessibility relation. For any valuation \(V(p)\subseteq\{1,\ldots,n\}\), \(\Delta p\) holds at \(x\) exactly when all successors of \(x\) agree on \(p\); an empty or singleton successor set agrees vacuously. The integers satisfy \(n\ge3\) and \(1\le i<j\le n\). The original orientation, rather than an unspecified relabelling, fixes the meaning of the reversal position.

## Proof

**1. Directed triangles.** The only cyclic triples in \(T_{n;i,j}\) are
\[
 j\to i\to k\to j,\qquad i<k<j.
\]
Indeed, every triple avoiding the flipped arc remains transitive. A singleton valuation \(V(p)=\{s\}\) has \(\Delta p\) false at a vertex \(v\) precisely when \(v\to s\) and \(v\) has at least two successors. If the axiom fails at \(x\) for this singleton, then \(\Delta p(x)\) is true and there are distinct successors \(v,u\) of \(x\) with \(\Delta p(v)\) false and \(\Delta p(u)\) true. Also \(x\ne s\): if \(x=s\), no successor of \(x\) can beat \(s\), so no successor could falsify \(\Delta p\). Moreover, \(x\) cannot beat \(s\) here: since \(\Delta p(x)\) holds for the singleton valuation, this would make \(s\) its only successor, precluding two different non-contingency values. Thus the vertices \((s,x,v)\) form a directed triangle \(s\to x\to v\to s\). Thus each such failure must occur in one of the three possible roles of a triple \((j,i,k)\) with \(i<k<j\).

**2. Counting all singleton failures when \(j<n\).** Put \(\ell=j-i-1\ge1\). In a cyclic triple \(j\to i\to k\to j\):

- If \(s=j\), the only possible failing root is \(x=i\). Every intermediate \(k\) has \(\Delta p(k)\) false because it beats both \(j\) (where \(p\) is true) and \(j+1\) (where \(p\) is false). The root \(i\) also beats \(j+1\), whose successors all disagree with none of their \(p\)-values, so \(\Delta p(j+1)\) is true. Exactly one failure \((j,i)\) results.
- If \(s=i\), the possible failing roots are the \(\ell\) intermediate vertices \(x=k\). Each has successors \(j\) and \(j+1\); the vertex \(j\) beats both \(i\) and \(j+1\) and has \(\Delta p(j)\) false, whereas \(\Delta p(j+1)\) is true. Exactly \(\ell\) failures result.
- If \(s=k\) is intermediate, the only possible failing root is \(x=j\). Its successors include \(i\) and \(j+1\); the vertex \(i\) beats \(k\) and \(j+1\), hence has \(\Delta p(i)\) false, while \(\Delta p(j+1)\) is true. This gives one failure for each of the \(\ell\) choices of \(k\).

There can be no additional singleton failures by the directed-triangle necessity in Step 1. Their total is \(1+\ell+\ell=2(j-i)-1\).

**3. Counting all singleton failures when \(j=n\).** Vertex \(j=n\) has just the successor \(i\), so it is impossible for it to be a failing root or to have \(\Delta p(j)\) false for any valuation. Accordingly the only possible singleton failure from the triangle list has \(s=n\) and \(x=i\). Its successors are \(i+1,\ldots,n-1\); for \(i\le n-3\), the vertex \(n-2\) beats both \(n\) and \(n-1\), and therefore has \(\Delta p\) false, whereas \(n-1\), with its one successor \(n\), has \(\Delta p\) true. Hence the failure exists exactly when \(i\le n-3\), and is unique. For \(i=n-2\), the only intermediate vertex \(n-1\) has one successor, so there is none.

**4. Proving full validity in the two exceptional families.** If \(j=i+1\), the flipped tournament is a transitive tournament with \(i\) and \(j\) exchanged in its total order. On any transitive tournament, a successor's successor set is contained in the original vertex's successor set; therefore, whenever \(\Delta p\) holds at a vertex, \(\Delta p\) holds at all its successors, so \(\Delta\Delta p\) holds there.

For \((i,j)=(n-2,n)\), the last three vertices form a directed three-cycle, with the earlier \(n-3\) vertices forming a transitive chain dominating that cycle. Each cycle vertex has exactly one successor, so both \(\Delta p\) and \(\Delta\Delta p\) are always true there. At each preceding vertex \(x\), every successor \(y\) has its entire successor set contained in the successor set of \(x\). Thus \(\Delta p(x)\) makes \(\Delta p(y)\) true for every such \(y\), and the axiom holds at \(x\). This handles every valuation and proves validity.

**5. Exact first-reversal count.** The adjacent reversals are the \(n-1\) choices \((i,i+1)\); the terminal skip-one reversal \((n-2,n)\) is a further distinct choice. The preceding steps show that every other reversal has a singleton countervaluation. Thus exactly \(n\) preserve the axiom, and \(\binom n2-n=n(n-3)/2\) destroy it.

## Verification

The included standard-library-only `check.py` independently constructs all reversed tournament adjacency masks, evaluates the non-contingency operator by Boolean masks, and compares every singleton countervaluation count against the piecewise theorem through \(n=9\). For every reversed tournament through \(n=8\), it additionally tests **every** Boolean valuation and checks agreement with the claimed full-validity classification. Running `python check.py` returns `VERIFY_OK reversals= 119 singleton_assignments= 868 all_valuation_assignments= 11256`. The finite computation is a regression test, not a proof for arbitrary \(n\); Steps 1–5 give the all-size proof.

## Relationship to prior work

Wang and Zenger's *Proof Theory for Non-Contingency Logic* (2026) develops general proof systems over frame conditions and provides the non-contingency semantic context; it does not address single-arc reversals of tournaments. Fan, Wang and van Ditmarsch's *Knowing Whether* (2013) establishes the semantics and treats transitivity and related frame properties, and explicitly discusses why knowing-whether formulas cannot globally define transitivity. Its transitivity-based sufficient validity does not classify nontransitive single-edge perturbations or their exact countervaluation multiplicities. The terminal triangle here is an essential nontransitive exception.

Related work on non-contingency introspection in finite outward trees determines a branching-vertex condition and a labelled-tree count; those frames are acyclic and not complete orientations. Work on first-order theories or path homology of tournaments after arc changes concerns different invariants. No claim of a novel basic modality or of a complete classification of all tournaments satisfying introspection is made.

## Limitations

The theorem concerns the first reversal layer around a **specified** transitive tournament, not all tournaments or more than one reversed arc. The refined integer \(B\) counts only single-world valuations and world failures, not the total number of countervaluations. No independent mathematical audit or exhaustive historical-priority review has been performed.

## References

1. Y. Wang and L. Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975, first posted 2026-09-30, https://arxiv.org/abs/2609.38975.
2. J. Fan, Y. Wang and H. van Ditmarsch, *Knowing Whether*, arXiv:1312.0144, first posted 2013-11-30, https://arxiv.org/abs/1312.0144.
3. L. N. Coregliano, *Quasi-carousel tournaments*, Journal of Graph Theory 88 (2018), 192–210, https://doi.org/10.1002/jgt.22205 (comparative tournament structural context only).
