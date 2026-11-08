# Exact Valuation Spectrum for Finite Minimal Robust Classification Models

## Finding
Fix a finite nonempty set \(X\) of size \(n\) and \(m\ge1\) atomic classifications. Before assigning their Boolean truth sets, prescribe robust regions \(r_i\subseteq X\) for all \(i=1,\ldots,m\). Following the minimal robust-model construction, generate the topology \(\tau_r\) with the \(r_i\) as a subbase. Truth sets \(v_i\) are independent choices subject only to \(r_i\subseteq v_i\).

Define a **robust signature** \(s(x)=\{j:x\in r_j\}\). Points with the same signature form a block \(B\); the distinct blocks are ordered by inclusion of signatures. For each \(i\), let \(\mathcal M_i\) consist of the inclusion-maximal blocks disjoint from \(r_i\); put \(b_B=|B|\).

**Exact-realization and enumeration theorem.** The following conditions on a fixed family of truth sets \((v_i)\) are equivalent:

1. There is some topology \(\sigma\) on \(X\) with every \(r_j\) open in \(\sigma\) and \(\operatorname{int}_\sigma(v_i)=r_i\) for all \(i\).
2. The least topology \(\tau_r\) already satisfies \(\operatorname{int}_{\tau_r}(v_i)=r_i\) for all \(i\).
3. For every \(i\) and every maximal nonrobust block \(B\in\mathcal M_i\), at least one point of \(B\) is classified negatively: \(B\setminus v_i\ne\varnothing\).
4. For every \(i\) and \(x\in v_i\setminus r_i\), there is \(y\notin v_i\) such that \(s(x)\subseteq s(y)\).

Consequently the **exact labelled valuation spectrum** is
\[
\boxed{E(r)=\prod_{i=1}^m2^{n-|r_i|-\sum_{B\in\mathcal M_i}b_B}\prod_{B\in\mathcal M_i}(2^{b_B}-1).}
\]
Both products over empty index sets equal one. Uniform independent choice among the \(2^{\sum_i(n-|r_i|)}\) truth-set tuples containing the prescribed robust sets yields the exact-calibration probability
\[
\boxed{\prod_{i=1}^m\prod_{B\in\mathcal M_i}(1-2^{-b_B}).}
\]
For each classifier, the greatest feasible truth-set cardinality is \(n-|\mathcal M_i|\), with exactly \(\prod_{B\in\mathcal M_i}b_B\) maximizers. Thus the number of maximizers for total positive-label count is \(\prod_i\prod_{B\in\mathcal M_i}b_B\).

**Unavoidable robustness and single-step saturation.** For arbitrary fixed \(v_i\supseteq r_i\), set \(f_i=\operatorname{int}_{\tau_r}(v_i)\). Then
\[
\boxed{x\in f_i\iff\{y\in X:s(x)\subseteq s(y)\}\subseteq v_i.}
\]
Every topology containing the original prescribed regions has \(\operatorname{int}(v_i)\supseteq f_i\). Furthermore, with \(f=(f_1,\ldots,f_m)\) and its generated topology \(\tau_f\), one has \(\tau_f\subseteq\tau_r\) and \(\operatorname{int}_{\tau_f}(v_i)=f_i\) for all \(i\): the saturation is idempotent after one step.

## Assumptions and scope
The carrier \(X\) is a finite **labelled** set; duplicates of robust signatures are permitted. The modal robustness operator is topological interior. There are finitely many, independently valued atomic predicates, with no mutual-exclusion, covering, metric, continuity or multiclass constraints imposed on their truth sets. Robust prescriptions are required to be open, not necessarily the full interiors. A proposed *exact* robust annotation asks for equality between the desired region and the interior. The count enumerates all tuples of truth sets over fixed \(X\) and fixed robust regions, not isomorphism classes of topologies or models.

## Proof
**1. The signature preorder is the topology.** A finite intersection of prescribed regions contains \(x\) precisely when every region in that intersection also contains \(x\). Hence the smallest open neighbourhood of \(x\) is
\[
U_r(x)=\bigcap_{j:x\in r_j}r_j=\{y:s(x)\subseteq s(y)\},
\]
where the empty intersection means \(X\). Indeed every open containing \(x\) contains \(U_r(x)\), while \(U_r(x)\) is open. Therefore
\[
x\in\operatorname{int}_{\tau_r}(v_i)\iff U_r(x)\subseteq v_i. \tag{1}
\]
The condition \(r_i\subseteq v_i\) and openness of \(r_i\) imply \(r_i\subseteq\operatorname{int}_{\tau_r}(v_i)\).

**2. Only maximal nonrobust signature blocks need witnesses.** Since the \(i\)-th signature coordinate is constant on each block, the classes outside \(r_i\) form a lower ideal in the finite signature poset. Let \(B\in\mathcal M_i\). For any \(x\in B\), every class strictly above \(B\) belongs to \(r_i\) and hence to \(v_i\). Thus, by (1), \(x\notin\operatorname{int}_{\tau_r}(v_i)\) holds exactly when \(B\setminus v_i\ne\varnothing\). Every nonrobust class lies below at least one maximal class of this lower ideal. If that class contains a negative witness \(y\), then \(s(x)\subseteq s(y)\) and (1) excludes \(x\) from the interior. This proves condition 3 equivalent to condition 2, and yields condition 4 by the same witness argument.

If \(\sigma\) makes every prescribed \(r_j\) open, then \(\tau_r\subseteq\sigma\). Increasing a topology can only increase the interior of any fixed set. Because every \(r_i\) is open and contained in \(v_i\), \(\operatorname{int}_{\tau_r}(v_i)=r_i\) is necessary for exactness in any such \(\sigma\), and evidently sufficient by choosing \(\tau_r\). This proves conditions 1 and 2 equivalent and completes the realization criterion.

**3. Count and optimization.** In each maximal outside block \(B\in\mathcal M_i\), the positive/negative choices are arbitrary except that the entire block cannot be positive. This gives exactly \(2^{b_B}-1\) possibilities. Every other point outside \(r_i\) can be assigned independently, contributing a factor two; all points in \(r_i\) are forced positive. Independence of atomic valuations gives the displayed product. Dividing by \(2^{\sum_i(n-|r_i|)}\) gives the probability. Exactly one negative point per maximal block maximizes positives; each such block has \(b_B\) choices for that unique negative point, while all other points are positive. This proves the optimum and its multiplicity, including empty-ideal cases.

**4. Forced robustness and saturation.** Formula (1) proves the pointwise computation of \(f_i\), and topological inclusion proves that \(f_i\) is unavoidable under any admissible refinement. Each \(f_i\) is \(\tau_r\)-open, so \(\tau_f\subseteq\tau_r\). Yet \(f_i\) is \(\tau_f\)-open and contained in \(v_i\), hence \(f_i\subseteq\operatorname{int}_{\tau_f}(v_i)\subseteq\operatorname{int}_{\tau_r}(v_i)=f_i\). Thus equality holds after one update of annotations. This does **not** assert that every original \(r_i\) remains open in \(\tau_f\); only the original \(\tau_r\) is guaranteed to retain their openness.

## Verification
The standalone Python program `verify_robust_cores.py` uses integer bitmasks, independently generates finite topologies and evaluates the interior operator directly. For two predicates and every one of the \(3^{2n}\) pairs of nested prescribed and truth regions, through \(n=4\), it compared the signature criterion against an exhaustive search through **all** labelled topologies (the counts are \(1,4,29,355\)). It tested \(7{,}380\) nested-label datasets and \(564{,}869\) admissible topology comparisons; the exactness equivalence, one-step saturation and forced-core minimum all passed. A separate direct enumeration for **every** pair of robust regions through \(n=5\) (\(1{,}364\) pairs) matched the product count against every possible nested truth valuation. These finite computations are independent checks only; the proof above handles all finite \(n,m\).

For a concrete example, take four states \(X=\{a,b,c,d\}\) and two prescribed regions \(r_1=r_2=\{a\}\). The three nonrobust states have one common, maximal signature block. Each truth region can include any proper subset of those three states, so there are \((2^3-1)^2=49\) exact valuation tuples, and \(3^2=9\) tuples maximize the number of positive classifications.

## Relationship to prior work
Pichler and Tagliaferri, *Robust Classification in ML: A Topological Semantics Approach* (2026), introduce the semantic framework, robust labels, and minimal topology generated by prescribed open regions (Section 6.2 and Theorem 6.3). Their result guarantees a least topology and the lower bound \(r_i\subseteq\operatorname{int}(v_i)\). The present result accepts that construction and adds the exact-realization test for a fixed truth valuation, the complete labelled valuation spectrum, optimal positive-classification budgets and a one-step saturation identity. The proof uses standard elementary facts about generated finite topologies and finite preorders; these underlying facts are not claimed as new.

## Limitations
The exact count requires a finite labelled carrier and independent Boolean atomic valuations. It is **not** a count of multiclass-exclusive labelings or of labelled topologies, and it does not assert any analogous finite product for infinite families of atomic constraints. The one-step saturation may change the generated topology and need not preserve openness of the original subbasic regions, although their inclusion in the realized robust cores remains true. Equivalent enumerations in unindexed literature or standard finite-order enumeration accounts cannot be ruled out. No external independent mathematical or priority audit has been performed.

## References
Pichler, Dominik and Mirko Tagliaferri. *Robust Classification in ML: A Topological Semantics Approach*. Electronic Proceedings in Theoretical Computer Science **449** (2026), 185–201, DOI: 10.4204/EPTCS.449.12. Public preprint arXiv:2607.20185v1, posted 22 July 2026.
