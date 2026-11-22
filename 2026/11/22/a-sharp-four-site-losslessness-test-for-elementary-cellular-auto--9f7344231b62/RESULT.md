# A sharp four-site losslessness test for elementary cellular automata on the golden-mean shift

## Finding

Consider any elementary binary radius-one cellular automaton \(F_r\) with Wolfram number \(r\in\{0,\ldots,255\}\). Restrict its **inputs**, but not necessarily its outputs, to the golden-mean shift \(X\subseteq\{0,1\}^{\mathbb Z}\), the bi-infinite sequences containing no contiguous `11`. Write the five effective local outputs

\[
(a,b,c,d,e)=\bigl(f_r(000),f_r(001),f_r(010),f_r(100),f_r(101)\bigr).
\]

The following are equivalent:

1. \(F_r|_X\) is injective on all bi-infinite admissible inputs.
2. For **every** integer \(n\ge1\), the induced map on indexed cyclic admissible binary words of length \(n\) is injective.
3. The induced map is injective at each of the four ring lengths \(n=1,2,3,4\).
4. The effective truth table satisfies all three exact tests:
   \[
   c\ne e,\qquad \neg(b=c=d),\qquad \neg(a=c\ \text{and}\ b=d).
   \]

Exactly **80 of the 256** elementary rules satisfy these conditions. Their ten effective truth-table masks are
\[
\{4,6,7,12,13,18,19,24,25,27\},\qquad
m=a+2b+4c+8d+16e.
\]
Every injective restriction has an explicit inverse block map of radius **at most one**, and exactly **16** of the 256 rules admit a radius-zero inverse on their restricted images. Every one of the other **176** rules has a collision on a cyclic ring of length at most four. The bound four is sharp: elementary Rule 5, for example, is injective on all admitted rings of lengths one, two and three, but is not injective at length four.

## Assumptions and scope

The local rule is \(f_r(u,v,w)=\lfloor r/2^{4u+2v+w}\rfloor\bmod2\). The input set forbids consecutive ones, including across the periodic boundary of a cyclic ring. An indexed ring is a word with specified positions, not a necklace modulo rotation. One synchronous update is observed. The map goes from \(X\) into the full binary shift and is **not** assumed to preserve \(X\); the result is injectivity onto its restricted image, not surjectivity of an endomorphism of \(X\). Periods one and two use repeated neighborhood indices in the usual cyclic way.

## Proof

**Only five local values matter.** On an input avoiding `11`, the triples `011`, `110` and `111` cannot occur. Thus each of the \(2^5=32\) five-bit patterns \((a,b,c,d,e)\) represents exactly \(2^3=8\) Wolfram rules with identical restrictions.

**Three necessary obstructions, each with an explicit short periodic witness.** When \(c=e\), the two distinct two-site words `01` and `10` both produce the uniform output \((c,c)\). When \(b=c=d\), the three rotations `001`, `010`, `100` all produce the uniform output \((c,c,c)\). When \(a=c\) and \(b=d\), the two distinct four-site words `1000` and `0010` produce the same output because shifting the single-one response by two sites does not change the output: its four cyclic values alternate between \(a=c\) and \(b=d\). These three collisions prove that each of the conditions in item 4 is necessary for global injectivity and that failure is always detected within four sites.

**The complete finite truth-table split.** Among the 32 effective masks, the first obstruction excludes 16. Of the remaining 16, the second excludes four masks \(14,15,16,17\). Of the remaining 12, the third excludes the two masks \(5,26\). Thus exactly ten effective masks remain, namely the set displayed above; each gives eight ordinary rules, so there are exactly 80. These counts follow immediately by enumerating the five Boolean variables in their stated bit order, and are independently reproduced by `verify.py`.

**Constructive inverses for the ten survivors.** It suffices to handle the five masks \(4,6,7,12,13\), because complementing every output bit sends effective mask \(m\) to \(31-m\). For a restricted output \(y=F_r(x)\), the following formulas reconstruct every \(x_i\):

| Effective masks | Decoder for \(x_i\) |
|---|---|
| \(4\) | \(y_i\) |
| \(6,7\) | \(y_i(1-y_{i+1})\) |
| \(12,13\) | \(y_i(1-y_{i-1})\) |

For masks \(27,25,24,19,18\), respectively, use the matching row after replacing each output bit \(y_j\) with \(1-y_j\). These identities are checked directly on the **thirteen** permitted binary five-site windows \(x_{i-2}\ldots x_{i+2}\) without `11`. Each decoder sees only \(y_{i-1},y_i,y_{i+1}\), which depend only on that five-site window; the finite table therefore proves the identities at **every site of every** bi-infinite admissible word and every cyclic ring, with no limiting or finite-size assumption. The executable `verify.py` independently enumerates those thirteen cases for all ten effective masks. These identities prove injectivity in items 1 and 2 and imply 3.

**Sharpness and inverse radii.** For mask \(5\), conditions one and two hold but the third fails, and Rule 5 is a representative. Since a length-one admissible ring contains only `0`, the map is trivially injective at length one. At length two, the first condition separates the two rotated single-one words; at length three, the second condition separates the three rotated single-one words, whose nonuniform outputs cannot equal that of the all-zero word. Thus Rule 5 is injective through length three but the four-site witness `1000`, `0010` collides. Finally, a radius-zero inverse must distinguish the old center bit by the new center bit alone. Within the ten masks, this is possible precisely for \(4\) and \(27\), where \(y_i=x_i\) and \(y_i=1-x_i\), respectively. The other eight masks produce both old center values for at least one common new center value, as checked on the five permitted source triples. Multiplying two effective patterns by eight rules each proves the stated count of 16. \(\square\)

## Verification

Run `python3 verify.py` with the Python standard library. The checker determines all 32 effective tables, constructs and checks each of the 22 finite periodic collisions, checks every permitted five-site source window under each of the ten decoding formulas, verifies exactly 80 original ECA rules per truth-table grouping, and cross-checks direct indexed-ring mappings for lengths one through twelve. It also confirms the two sharp four-site exception masks and that only two good masks admit a radius-zero inverse. These finite checks substantiate the explicit exhaustive local identities and short collision witnesses; the **all-length and bi-infinite statements follow from the local proof**, not from bounded ring enumeration.

## Relationship to prior work

Salo's work on regularity and generalized inverses of elementary cellular automata [1] gives general finite-state methods and explicitly discusses the behavior of Rule 28 on a related restricted shift (Proposition 20). It does not give this complete golden-mean-input injectivity census, the three Boolean conditions, or the sharp four-site collision threshold. Kopra [2] studies reversible cellular-automaton dynamics on beta-shifts and the general effect of restricting the source shift, but does not classify these 256 radius-one maps. Published work [3] gives Rule 28's unrestricted cyclic predecessor-fiber maxima, while [4] classifies existence of **some** uniquely invertible unrestricted finite output block for each rule. Neither property entails global one-to-one behavior on **every** golden-mean input or the source-specific 80/176 classification. The current theorem instead quantifies over every admissible input and every ring length and provides explicit local inverse formulas. Similarity searching alone is not a proof of novelty; see the associated review for the remaining historical-priority risk.

## Limitations

The restriction is specifically the two-symbol golden-mean shift and synchronous, nearest-neighbor binary local rules. The classification does not apply automatically to wider neighborhoods, asynchronous updates, unconstrained sources, higher iterates or arbitrary sparse constraints. An injective restriction need not map the source shift into itself. No claim is made about the topology or complete forbidden-word description of each restricted image. Historical literature may contain equivalent finite classifications under different terminology; no independent validation is claimed.

## References

1. V. Salo, *On von Neumann regularity of cellular automata*, first arXiv posting 2022-09-27, arXiv:2209.13373, https://arxiv.org/abs/2209.13373 (especially Sections 5–7).
2. J. Kopra, *Dynamics of Cellular Automata on Beta-Shifts and Direct Topological Factorizations*, Developments in Language Theory (2020), https://pmc.ncbi.nlm.nih.gov/articles/PMC7247874/.
3. *Sharp Lucas inverse-fiber law and output classification for cyclic Rule 28*, publicly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-lucas-inverse-fiber-law-and-output-classification-for-cycl--8fa574301e73.
4. *Exact finite-preimage identifiability for all elementary cellular automata*, publicly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-finite-preimage-identifiability-for-all-elementary-cellula--218bfa54da8f.
