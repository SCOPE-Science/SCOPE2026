# Rigidity and exact count of six-point shattering supports in the smallest rank-three Kneser graph

## Finding

Let \(G=\operatorname{KG}(13,3)\) have vertex set \(V=\binom{[13]}3\), with two vertices adjacent precisely when the corresponding triples are disjoint. Let \(\mathcal N=\{N_G(C):C\in V\}\) be its open-neighborhood family. Write \(s_6(13)\) for the number of unordered six-element subsets \(S\subseteq V\) that are VC-shattered by \(\mathcal N\).

**Theorem (rigidity of the first maximum layer).** A six-element support \(S\) is shattered if and only if there exist ten mutually distinct ground points \(c,a_1,a_2,a_3,p_{1,1},p_{1,2},p_{2,1},p_{2,2},p_{3,1},p_{3,2}\) such that
\[
S=\bigl\{\{c,a_j,p_{j,t}\}:j=1,2,3,\ t=1,2\bigr\}.
\]
In particular, all shattered six-supports lie in one orbit under ground-set permutations, and their exact number is
\[
s_6(13)=13\binom{12}{3}\binom96\frac{6!}{(2!)^3}=21{,}621{,}600.
\]
The exact probability that six uniformly chosen distinct graph vertices are shattered is \(21{,}621{,}600/\binom{286}{6}=21{,}621{,}600/721{,}005{,}537{,}967\).

The earlier result that the VC dimension of \(\operatorname{KG}(n,3)\) first reaches six when \(n=13\), together with an existence witness of this form, is **not** a new claim. The new result classifies **all** witnesses at the sharp order and computes the exact top coefficient there.

## Assumptions and scope

The graph is finite, simple and undirected. A neighborhood is **open**, not closed, and its center is a three-subset. A support is shattered if every one of its \(2^{|S|}\) Boolean traces is realized by some neighborhood. The theorem concerns six-element supports only in the ambient graph \(\operatorname{KG}(13,3)\); no all-order shattering polynomial is asserted. We count unordered supports, not ordered enumerations, and identify supports under permutations of \([13]\).

## Proof

**1. Replace disjointness by hit traces and extract private coordinates.** Label a hypothetical shattered support \(S=\{F_1,\ldots,F_6\}\). For any three-point center \(Q\), complementing the open-neighborhood trace within \([6]\) yields its *hit set* \(H(Q)=\{i:Q\cap F_i\ne\varnothing\}\). Shattering is equivalent to realizing all \(64\) hit sets. In particular, the singleton hit set \(\{i\}\) requires a coordinate \(p_i\in F_i\) that belongs to no other \(F_j\); the six selected private coordinates are distinct. The empty hit set requires three unused ambient coordinates. Let \(X=(\bigcup_i F_i)\setminus\{p_1,\ldots,p_6\}\), so \(|X|\le13-6-3=4\). Each residual pair \(e_i=F_i\setminus\{p_i\}\) is a two-element subset of \(X\).

**2. Four residual coordinates are necessary.** If \(|X|\le3\), choose two residual pairs whose union contains every coordinate in \(X\). Such a pair exists: either all residual pairs coincide (when \(|X|=2\)), or two distinct pairs span the three-element set \(X\). Any query hitting all four triples other than these two while avoiding the omitted two cannot use their residual coordinates, and therefore must hit the remaining four triples through four different private points. A three-coordinate query cannot do that. This contradicts shattering. Thus \(|X|=4\), the six selected private points and three unused points exhaust \([13]\).

**3. The residual multigraph is a star.** For every pair of indices \(i\ne j\), realizing the hit set \([6]\setminus\{i,j\}\) would be impossible if \(e_i\cup e_j=X\), since the only allowed used coordinates would be four distinct private points. Therefore the six two-element sets \(e_i\) are pairwise intersecting (including possible repeats). They use all four elements of \(X\). Any pairwise-intersecting family of two-subsets spanning four vertices has a common point: if there is no common point, three suitable edges form a triangle, and every edge meeting all three lies in those three vertices. Thus some \(c\in X\) belongs to every \(e_i\). Write \(X=\{c,a_1,a_2,a_3\}\) and let \(m_j\ge1\) be the number of residual pairs \(\{c,a_j\}\); \(m_1+m_2+m_3=6\).

**4. Each of the three arms occurs twice.** Fix an arm index \(\ell\). Omit one sample triple from each of the two *other* arms, and ask for a query hitting all remaining four sample triples. Avoiding both omitted triples forbids \(c\) and both other arm coordinates. Among used nonprivate points, only \(a_\ell\) is available. The query must include it, otherwise four private points would be necessary; then each of the \(4-m_\ell\) remaining triples outside arm \(\ell\) still requires its own private point. Hence \(1+(4-m_\ell)\le3\), i.e. \(m_\ell\ge2\). Applying this to all three arms gives \(m_1=m_2=m_3=2\), proving necessity and uniqueness up to relabeling.

**5. Every such support is shattered.** Given any requested hit set \(T\subseteq[6]\), independently in each of the three two-element arms choose \(a_j\) if both corresponding triples should be hit, the relevant private point if exactly one should be hit, and nothing if neither should be hit. This uses at most three coordinates and hits exactly \(T\). Pad to a three-element center with the three unused ambient coordinates. Every hit set, hence every complementary open-neighborhood trace, occurs.

**6. Exact counting without overcount.** Choose the unique hub in \(13\) ways, choose its three unordered arm coordinates in \(\binom{12}{3}\) ways, choose the six private coordinates from the remaining nine ground points in \(\binom96\) ways, and partition those six private coordinates among the three already distinguished arms as unordered pairs in \(6!/(2!)^3\) ways. The unused three coordinates are forced. Because the hub has incidence degree six, arm points degree two, private points degree one, and unused points degree zero, this enumeration counts every support exactly once. Independently, the stabilizer of a support in the ground-set permutation group has size \(3!\,(2!)^3\,3!=288\): permuting the three arms, swapping each pair of private points, and permuting the three unused points. Its orbit therefore has \(13!/288=21{,}621{,}600\) members, agreeing with the direct count.

## Verification

From this directory, run `python3 verify.py` and `python3 independent_check.py` using Python 3 and the standard library. The first independently generates all actual query traces for \(\binom{13}{3}=286\) possible centers and classifies the \(462\) multisets of six residual edges on a four-element set. Exactly four multisets satisfy all \(64\) traces, one for each choice of the common hub, and each has multiplicity profile \((2,2,2)\). It also tests the \(28\) residual-edge multisets using three coordinates at ground size twelve, none of which are shattered. The second script uses independently constructed star-cover masks to reproduce the four successful profiles. Both scripts check the stated integer count. The unlimited mathematical conclusion for this fixed ambient graph follows from steps 1–6, not from extrapolating computations.

## Relationship to prior work

The previously determined exact rank-three Kneser open-neighborhood VC profile established that dimension six begins at \(n=13\) and supplied a three-doubled-spoke witness; neither **existence** nor the onset is claimed here. The present theorem strengthens that existence statement by proving the uniqueness of the support type and counting every labeled occurrence at the sharp order. These two conclusions do not follow merely from knowing the dimension or exhibiting one witness.

Bhattacharya, Chakraborty, Ghosh, Mishra and Paraashar study disjointness in terms of communication complexity under VC restrictions, not the top shattered-support coefficient of a fixed Kneser graph. Benediktsson, Macpherson and Adler analyze Johnson and Hamming adjacency relations; Johnson adjacency on triples is not the disjointness relation on triples. The existing general literature therefore supplies relevant context but not this asserted classification. Historical priority under other terminology remains a residual risk.

## Limitations

The proof and enumeration concern the first ambient order with six-point shattering, not arbitrary \(n>13\), where additional support types can occur. The independent scientific audit is not performed. The originality assessment is a best-knowledge literature and available-record comparison, not a proof of worldwide priority. Finite test programs corroborate, but do not replace, the complete structural argument.

## References

1. A. Bhattacharya, S. Chakraborty, A. Ghosh, G. Mishra and M. Paraashar, *Disjointness through the Lens of Vapnik-Chervonenkis Dimension: Sparsity and Beyond*, arXiv:2006.13712v1, first public 2020-06-24.
2. B. G. Benediktsson, D. Macpherson and I. Adler, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, first public 2020-07-31.
