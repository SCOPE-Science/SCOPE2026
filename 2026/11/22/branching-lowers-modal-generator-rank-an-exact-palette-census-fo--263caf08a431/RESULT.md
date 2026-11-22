# Branching lowers modal generator rank: an exact palette census for finite reflexive cluster bouquets

## Finding
Let \(B\) be a nonempty root cluster of size \(r\), and let \(C_1,\ldots,C_m\) be \(m\geq1\) nonempty terminal equivalence clusters with respective sizes \(s_1,\ldots,s_m\). Accessibility is universal inside each cluster; all root worlds additionally see every terminal world; and terminal worlds do not see other clusters or the root. All clusters have labelled vertices. Equip the finite powerset Boolean algebra with the ordinary forward possibility operator \(\Diamond\). Let \(k\geq0\) propositional subsets be a prospective ordered generating tuple, and put \(q=2^k\). Each vertex has its Boolean \(k\)-colour; denote the sets of colours appearing in the root and terminal clusters by \(T,S_1,\ldots,S_m\), respectively.

**Exact full-generation criterion.** The tuple generates the whole modal powerset algebra if and only if its colours are injective separately inside every cluster, the terminal palettes \(S_i\) are pairwise different, and, **only in the one-terminal case \(m=1\)**, \(T\not\subseteq S_1\). For \(m\geq2\), no restriction is imposed on overlap between root and terminal palettes.

Write \(m_s=|\{i:s_i=s\}|\) and \((a)_{\underline b}=a(a-1)\cdots(a-b+1)\), with value zero for \(b>a\), and adopt \(\binom qs=0\) when \(s>q\). The exact number of ordered generating \(k\)-tuples is
\[
G_k=\begin{cases}
(q)_{\underline r}\displaystyle\prod_{s\geq1}\bigl(\binom qs\bigr)_{\underline{m_s}}(s!)^{m_s},&m\geq2,\\[5pt]
(q)_{\underline{s_1}}\bigl((q)_{\underline r}-(s_1)_{\underline r}\bigr),&m=1.
\end{cases}
\]
In particular, when \(m\geq2\), the least permitted *alphabet size* is exactly
\[
q_* = \min\bigl\{q\in\mathbb N:q\geq r\text{ and }\binom qs\geq m_s\text{ for all }s\geq1\bigr\},
\]
and the minimum number of Boolean generators is \(\lceil\log_2 q_*\rceil\). For \(m=1\), the known linear-cluster specialization is \(q_*=\max(r,s_1+1)\).

**Strict rank decrease under frame enlargement.** A one-point root above a two-point terminal cluster requires at least two Boolean generators. Adjoining an incomparable singleton terminal cluster makes **one generator sufficient**: its two terminal supports \(\{0,1\}\) and \(\{0\}\) are different, even though root colour \(0\) repeats. Thus branching changes the generator threshold rather than merely adding cost. When \(m\geq2\) and \(m\) terminal clusters all have fixed size \(s\), with fixed root size \(r\), the least number of generators is \(\frac1s\log_2 m+O(1)\) as \(m\to\infty\). For every generating tuple with \(m\geq2\), all singletons have explicit modal definitions of depth at most two, and that bound is sometimes necessary.

## Assumptions and scope
The accessibility relation is reflexive and transitive. The root \(B\) is a complete strongly connected component, distinct from every terminal component. Root worlds see all of \(W=B\sqcup\bigcup_iC_i\); each terminal world sees exactly its terminal component. Terminal components are *named in the counting parameters* through their given labelled carriers, not by additional symbols in the modal language. The language includes arbitrary Boolean operations, truth constants, and one forward modality; no counting, hybrid, global, backward, or second modality is used. Every \(k\)-tuple of subsets corresponds uniquely to a \(q\)-colouring of the labelled vertices, because \(q=2^k\), including \(k=0\). Distinct tuples are counted literally, without quotienting by permutations or automorphisms.

The primary new claim concerns the branching regime \(m\geq2\). The \(m=1\) formulas are included only as an **already-established comparator** from the linear chain of clusters.

## Proof
**1. Necessity: intracluster colours.** If two distinct vertices in any one complete cluster carry the same colour, their transposition is a colour-preserving automorphism of the frame. All formulas built from the proposed generators therefore have the same truth value at those vertices, and the full Boolean powerset algebra cannot be generated.

**2. Necessity: terminal supports.** If two different terminal components have the same colour-support set, choose same-coloured vertices, one in each. The relation matching equal colours in these two components is a pointed bisimulation: a successor in either component is matched inside the other because each component has the same support. No formula can distinguish this pair, irrespective of the root. Hence terminal supports must be different. When there is only one terminal component and \(T\subseteq S_1\), every root vertex has a same-coloured terminal vertex; matching same colours between root and terminal is a pointed bisimulation because both root and terminal successor-colour sets equal \(S_1\). Hence full generation fails. This last argument is needed only for \(m=1\).

**3. Sufficiency under branching.** Assume \(m\geq2\), all colours within a component are pairwise different, and the terminal supports \(S_1,\ldots,S_m\) are pairwise distinct. For each colour \(c\in[q]\), the Boolean minterm \(\chi_c\) isolates exactly the vertices of colour \(c\). For each nonempty palette \(S\subseteq[q]\), set
\[
\delta_S=\Bigl(\bigwedge_{c\in S}\Diamond\chi_c\Bigr)\land\Bigl(\bigwedge_{c\notin S}\neg\Diamond\chi_c\Bigr).
\]
A terminal world satisfies \(\delta_S\) exactly when its terminal component's support is \(S\). Define
\[
\rho=\bigwedge_{i=1}^{m}\Diamond\delta_{S_i}.
\]
Every root world satisfies \(\rho\), since it can access each terminal component. No terminal world satisfies \(\rho\), since it has access only to its own component, and at least two distinct supports occur. Consequently \(\rho\) defines precisely \(B\). By injectivity within each component, \(\rho\land\chi_c\) isolates each root world of colour \(c\), while \(\neg\rho\land\delta_{S_i}\land\chi_c\) isolates the unique terminal vertex with colour \(c\) in \(C_i\). All singletons are definable, so the generated Boolean algebra is the entire powerset. Each formula uses at most two nested possibility operators. No condition \(T\not\subseteq S_i\) was needed.

**4. The single-terminal comparison.** If \(m=1\) and \(T\not\subseteq S_1\), choose \(c\in T\setminus S_1\). Then \(\Diamond\chi_c\) holds at every root world and at no terminal world, so it isolates the root component. Colour minterms distinguish points within both components. Together with Steps 1–2, this proves the criterion also for \(m=1\), agreeing with the previously published adjacent-palette condition for a two-cluster chain.

**5. Enumeration and rank.** Assigning \(r\) distinct colours to the labelled root worlds gives \((q)_{\underline r}\) choices. For each terminal size \(s\), there are \(\binom qs\) distinct possible supports, and the \(m_s\) labelled terminal components of that size must receive different supports, giving \((\binom qs)_{\underline{m_s}}\) choices. Every selected support can be bijectively assigned to the \(s\) labelled vertices in that component in \(s!\) ways. Independent multiplication across sizes proves the first count. With one terminal component, \((q)_{\underline{s_1}}\) counts its injective colourings and \((q)_{\underline r}-(s_1)_{\underline r}\) counts the injective root colourings whose palettes are not subsets of that terminal support, proving the second count. In the branching case each factor is positive exactly when \(q\geq r\) and \(\binom qs\geq m_s\) for every occurring \(s\). Taking the first allowed power of two \(q=2^k\) proves the rank formula.

**6. Sharp depth and rank decrease.** Fix root colour \(0\), first terminal colours \(0,1\), and second terminal colour \(0\). Its terminal palettes are \(\{0,1\}\) and \(\{0\}\), so Step 3 proves generation with one Boolean predicate. The root vertex and the colour-\(0\) vertex in the two-point terminal component have identical depth-zero and depth-one modal observations: both have colour \(0\) and see exactly colours \(\{0,1\}\). They are therefore not distinguishable at depth one, but \(\rho\) separates them at depth two. By contrast, without the singleton terminal component, the two-point terminal support is all of \(\{0,1\}\), so any root colour lies inside it and generation fails with one predicate. A third available colour permits a one-terminal generating colouring, and hence two Boolean predicates suffice. Finally, for fixed \(s,r\), the binomial estimate \(\binom qs=q^s/s!+O(q^{s-1})\) gives \(q_*=(s!m)^{1/s}+O(1)\) and the stated logarithmic generator-rank asymptotic.

## Verification
Run the accompanying standard-library-only Python 3 file `VERIFY.py` directly using `python3 VERIFY.py`. It enumerates the actual labelled frames and all \(k\)-colourings in 116 bounded parameter cases (root sizes one to three and terminal-size tuples of length one through three, with at most four colours and a configured maximum of 100000 colourings per case). For every tested colouring it independently computes the stable modal bisimulation/refinement partition and compares discreteness against the stated palette criterion. It independently counts generating colourings and compares with the exact product formula. In 5641 small instances it additionally constructs the generated Boolean modal algebra directly and tests whether it equals the full powerset. It separately asserts the strict generator-rank decrease. The recorded checker line is:

```
VERIFY_OK cases=116 exhaustive_labelings=281347 generating_labelings=63202 direct_algebra_checks=5641
```

These bounded computations corroborate but do not establish the theorem for unbounded parameters. The unrestricted proof is Steps 1–6 above.

## Relationship to prior work
Agnew (2026) studies general criteria for local finiteness of transitive modal complex algebras and their associated frames. Finite cluster bouquets are automatically finite modal algebras, so that local-finiteness criterion does not supply a sharp minimum generator number or a literal generating-tuple census.

The published adjacent-palette theorem for finite \(\mathsf{S4.3}\) linear chains of equivalence clusters gives a two-cluster noncontainment criterion: our \(m=1\) statement is **covered by** that theorem, rather than novel. The published finite \(\mathsf{S5}\) random-generation analysis gives the distinct-support obstruction for multiple *disjoint* equivalence components, but does not account for root worlds that access every component, nor the rank decrease caused by new branches. Published finite-modal exchangeability calculations on rooted \(\mathsf{S4}\) bouquets classify the observable *root theory* for a single root and equal-sized terminal clusters, and already establish a depth-two expressivity phenomenon. They do not assert the exact labelled generating-tuple census, the heterogeneous terminal-size/root-cluster extension, or the rank decrease. The published free-algebra calculation over all height-two partial orders concerns equivalence of formulas across a frame class, rather than generation of the whole fixed finite modal powerset algebra. These distinctions are about mathematical hypotheses and implications, not titles alone.

## Limitations
All root and terminal components are finite, nonempty, and complete in the accessibility relation. The theorem is not claimed for arbitrary finite transitive frames, partially ordered roots, nonnormal modalities, or languages without Boolean negation. The one-terminal case is prior work. Full historical uniqueness is not certified: earlier modal-algebra generator results under other terminology, especially for branched preorders and fixed coloured finite frames, remain a priority risk. The sample checks are finite; the proof, not the experiments, supports all positive parameter values. Independent expert and historical-priority validation have not been performed.

## References
- G. Agnew, *On Local Finiteness of Modal K4 Algebras*, arXiv:2606.02941 (first publicly available 2026-06-01), https://arxiv.org/abs/2606.02941.
- *Adjacent-palette rigidity and exact generation census for finite S4.3 cluster chains*, published scientific result, 2026-10-13, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-adjacent-palette-rigidity-and-exact-generation-census-for-finite--519d6caa5be5.
- *Sharp random-generation threshold and logarithmic phase spectrum for finite S5 modal algebras*, published scientific result, 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-random-generation-threshold-and-logarithmic-phase-spectrum--74d0bdb5e90d.
- *Finite modal exchangeability on rooted S4 bouquets: exact observable and hidden dimensions*, published scientific result, 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-finite-modal-exchangeability-on-rooted-mathsf-s4-bouquets-exact--a6ce0005e8b0.
- *Exact free-algebra cardinalities and modal-depth cutoff for height-two partial orders*, published scientific result, 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-free-algebra-cardinalities-and-modal-depth-cutoff-for-heig--704161647189.
