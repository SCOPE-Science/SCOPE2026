# Sharp universal colored-permutation profiles and a de Bruijn circuit-partition census

## Finding

Fix integers \(q\ge2\) and \(d\ge1\). In finite nonempty structures with one named bijection \(f\) and exactly one of \(q\) named, mutually exclusive, exhaustive unary colors at every vertex, consider complete quantifier-free one-point profiles on the terms \(x,f(x),\ldots,f^d(x)\). A structure is *depth-\(d\) universal* when it realizes every profile realizable in any such finite structure. Then:

1. The number of possible profiles is
   \[
   T_{q,d}=q^{d+1}+\sum_{c=1}^{d}q^c.
   \]
2. The minimum order of a depth-\(d\) universal structure is
   \[
   M_{q,d}=q^{d+1}+\sum_{c=1}^{d}c\,N_q(c),\qquad
   N_q(c)=\frac1c\sum_{j=0}^{c-1}q^{\gcd(c,j)}.
   \]
   Every minimum structure has exactly one colored \(c\)-cycle of each rotation-necklace type of length \(c\), for every \(1\le c\le d\). The remaining \(q^{d+1}\) vertices lie on cycles of length greater than \(d\) and realize each color word of length \(d+1\) exactly once.
3. The minimum structures, up to color- and function-preserving isomorphism, correspond bijectively to the **short-cycle-free transition systems** on the directed de Bruijn graph \(B(q,d)\). This graph has vertices the color words of length \(d\), arcs the words of length \(d+1\), with each arc directed from its prefix to its suffix. At every vertex choose a bijection matching its \(q\) incoming arcs with its \(q\) outgoing arcs; the resulting permutation of arcs must have no cycle of length at most \(d\).

   Write \(\mathcal S_{q,d}\) for the finite set of directed simple cycles of \(B(q,d)\) of length at most \(d\), distinguishing arcs, and let \(r_v(F)\) be the number of selected cycle passages through \(v\). The exact number of isomorphism types of minimum universal structures is
   \[
   E_{q,d}=\sum_{\substack{F\subseteq\mathcal S_{q,d}\\
               \text{cycles of }F\text{ pairwise arc-disjoint}}}
       (-1)^{|F|}\prod_{v\in\{0,\ldots,q-1\}^{d}}
          \bigl(q-r_v(F)\bigr)!.
   \]
   Here the empty selection contributes \((q!)^{q^d}\). Equivalently, \(E_{q,d}\) counts all such local matchings with no short cycle; the inclusion–exclusion formula is an effective finite integer expression valid for all \(q,d\) in scope.
4. If \(\pi(w)\) is the least cyclic color period of necklace \(w\) and \(\mathcal N_{q,c}\) is the set of necklaces of length \(c\), every minimum model has automorphism-group order
   \[
   A_{q,d}=\prod_{c=1}^{d}\prod_{w\in\mathcal N_{q,c}}\frac{c}{\pi(w)}.
   \]
   Therefore the exact number of such structures on a fixed labeled domain of size \(M_{q,d}\) is \(E_{q,d}M_{q,d}!/A_{q,d}\).

For the binary palette \(q=2\), the successive quadruples \((d,T_{q,d},M_{q,d},E_{q,d})\) at depths \(d=1,2,3,4\) are \((1,6,6,1)\), \((2,14,16,3)\), \((3,30,36,40)\), and \((4,62,76,7749)\). For three colors at depth one they are \((1,12,12,64)\). In particular, at binary depth two one of the three minimum models has two distinct long four-cycles, so minimum models need not have a single de Bruijn cycle.

## Assumptions and scope

The function \(f\) is a *permutation* of the entire finite domain, not an arbitrary endofunction. All color names remain distinguished; relabeling colors is not an isomorphism. Every vertex satisfies exactly one of the \(q\) unary predicates. No quantifiers, external parameters, predecessor term symbols, or additional relations are included in the profile language. Equality atoms between all indicated terms and all unary color atoms at those terms are included. The theorem is for integers \(q\ge2\) and \(d\ge1\); the single-color boundary is not asserted by the displayed minimum formula.

## Proof

**1. Classification of point profiles.** In a permutation, a point lies on a directed cycle of some length \(c\). If \(c\le d\), the equality atoms on \(x,f(x),\ldots,f^d(x)\) determine \(c\), and the color atoms determine the first \(c\) colors. Conversely every such \(c\)-letter word is realized by a colored \(c\)-cycle. Thus there are \(q^c\) depth-\(d\) profiles with visible exact cycle length \(c\). If \(c>d\), the displayed iterates are distinct and the profile specifies exactly an arbitrary color word of length \(d+1\), yielding \(q^{d+1}\) further profiles. This proves the count.

**2. Forced short cycles.** A cycle of length \(c\le d\) with a fixed cyclic color necklace realizes the point profiles indexed by the cyclic rotations of that necklace, and no other cycle length can realize them because the equality pattern determines \(c\). Two distinct necklaces of the same length cannot cover each other's profiles. Hence every universal structure contains at least one cycle for every necklace of each short length. Burnside's lemma applied to cyclic rotations gives \(N_q(c)=c^{-1}\sum_{j=0}^{c-1}q^{\gcd(c,j)}\), so these necessary short components occupy at least \(\sum_{c\le d}cN_q(c)\) vertices.

**3. Forced long budget and its attainment.** Each vertex on a cycle longer than \(d\) realizes exactly one of the \(q^{d+1}\) no-repeat color profiles; a vertex on a shorter cycle realizes none. Thus at least \(q^{d+1}\) vertices must belong to long cycles. A cyclic de Bruijn word of order \(d+1\) over \(q\) colors has length \(q^{d+1}\) and contains each word of length \(d+1\) once as a cyclic factor. Its length exceeds \(d\) because \(q\ge2\). Use that word as the colors of a single long permutation cycle and adjoin precisely one representative cycle of each short necklace. This realizes every profile and attains the lower bound. Equality in the lower bound forces exactly the stated components and one occurrence of every no-repeat profile.

**4. Complete classification of optimizers.** At the minimum, associate to each long vertex its unique length-\(d+1\) color word. This labels the long vertices bijectively by the arcs of \(B(q,d)\). If a vertex has word \(a_0\ldots a_d\), its successor has prefix \(a_1\ldots a_d\), so the permutation \(f\) matches each incoming arc at a de Bruijn vertex to one outgoing arc there. Because \(f\) is bijective, these are bijections. The cycles of the induced arc permutation are exactly the long cycles, so all have length greater than \(d\). Conversely, any family of such local bijections defines a permutation of the arcs; color an arc-vertex by its first letter. The overlap condition makes its forward color word equal to the arc label, and the no-short-cycle condition guarantees the required equality pattern. The canonical arc labels are invariant under colored permutation isomorphisms and distinguish all long vertices, giving a bijection between minimum-model isomorphism types and admissible local matchings.

**5. Exact census.** Every cycle of the arc permutation of length \(\ell\le d\) projects to a *simple* directed cycle of \(B(q,d)\): if two of its length-\(d\) overlap states coincided, the underlying periodic color sequence would have period strictly smaller than \(\ell\), because a block of length \(d\ge\ell\) determines an entire period. Then its length-\(d+1\) arc words would repeat, contradicting distinctness of the \(\ell\) vertices of a permutation cycle. Thus the forbidden short cycles are exactly those listed in \(\mathcal S_{q,d}\), not merely a subclass. For each directed simple short cycle \(C\) in \(B(q,d)\), consider the event that the chosen local matchings turn \(C\) into a complete cycle of the arc permutation. A family \(F\) of distinct selected events is impossible if two selected cycles share an arc. Otherwise they prescribe \(r_v(F)\) distinct incoming-to-outgoing pairs at each vertex \(v\), leaving \((q-r_v(F))!\) local choices. Inclusion–exclusion over the forbidden events gives the displayed formula for \(E_{q,d}\). Each short colored \(c\)-cycle is preserved setwise by any automorphism, and the rotations preserving its coloring form a group of order \(c/\pi(w)\); no two forced cycles have the same colored necklace. The long part is pointwise fixed because its distinct forward color words distinguish every vertex. Hence every optimizer has automorphism-group order \(A_{q,d}\), and orbit–stabilizer gives its labeled count.

## Verification

Run `python3 VERIFY.py` with Python 3. The script independently enumerates all transition systems and all arc-disjoint short-cycle inclusion–exclusion terms at \((q,d)=(2,1),(2,2),(2,3),(2,4),(3,1)\), checks Burnside necklace counts for three palettes through length six, verifies the binary depth-two census by a separate direct necklace-multiset enumeration, and brute-forces all colored permutations of up to six vertices at binary depth one. Its checked output includes `VERIFY_OK 25` and the values displayed above. These finite checks corroborate but do not replace the all-parameter argument in the Proof section.

## Relationship to prior work

Kuželka (2026, §8.1.2–8.1.3) develops forward profiles for unary function structures and enforces their compatibility along cycles; his paper studies model-counting complexity and does not state the sharp universal colored-permutation minimum or its all-optima census. Sawada and Gabrić (2025) study generating individual universal cycles via de Bruijn graphs; classical de Bruijn cycles provide the attaining *one-cycle* long construction here, but do not enumerate every minimum multi-cycle realization. Burnside's necklace count, standard local edge-transition systems and inclusion–exclusion are credited as mathematical ingredients. The minimum-domain problem, its forced short-cycle sector, and the exact short-cycle-free optimizer census are the combined assertions here. Related published enumerations of colored permutation theories and de Bruijn special-purpose covers are not claimed to be new.

## Limitations

This concerns quantifier-free one-point profiles only, not full first-order theories or counting-rank equivalence. The bijective-function assumption is essential: arbitrary endofunctions have transient orbits and require a different analysis. The all-parameter formula for \(E_{q,d}\) is finite inclusion–exclusion, not a claimed elementary closed product or efficient algorithm in the binary input lengths of \(q,d\). The displayed binary numerical census is proved by the finite formula and corroborated independently for the shown cases; no extrapolated sequence or asymptotic is asserted. Earlier equivalent formulations of the combined minimum-and-census question under circuit-partition terminology remain a historical-priority risk.

## References

- Ondřej Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580 (first public version August 31, 2026), §§2.1, 8.1.2–8.1.3, 8.1.6. https://arxiv.org/html/2608.30580v2
- Joe Sawada and Daniel Gabrić, *Random generation of universal cycles and de Bruijn sequences*, arXiv:2510.16545 (first public version October 18, 2025), §§1–3. https://arxiv.org/abs/2510.16545
- *De Bruijn Sequence and Universal Cycle Constructions*, construction reference for standard de Bruijn graph and Euler tours (accessed November 2026). https://debruijnsequence.org/db/graph
- Burnside's lemma (classical necklace-counting formula) and inclusion–exclusion (classical finite counting principles).
