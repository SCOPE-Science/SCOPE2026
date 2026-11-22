# The pure shattering complex of projective line-packings

## Finding

Let \(\mathcal S\) be the 56 line spreads of \(\operatorname{PG}(3,2)\), and let \(\mathcal P\) be its 240 *packings*: partitions of all 35 projective lines into seven spreads. Query a spread \(s\in\mathcal S\) by whether it belongs to an unknown packing \(P\in\mathcal P\). A support \(T\subseteq\mathcal S\) is *shattered* when for every \(U\subseteq T\) there is a packing \(P\) with \(P\cap T=U\).

**Classification.** A support \(T\) is shattered exactly in the following cases:

1. \(|T|\le3\), and all its spreads occur together in at least one packing (the empty support is included);
2. \(|T|=4\), and its spreads occur together in **exactly one** packing.

No support with at least five spreads is shattered. The complete face polynomial is
\[
\Phi(z)=1+56z+840z^2+4200z^3+6720z^4.
\]
Hence \(\operatorname{VCdim}=4\); the shattering complex is pure of dimension three, with 6720 facets. The 6720 facets form exactly **two orbits of 3360** under projective collineations \(\operatorname{GL}(4,2)\). Exactly 840 compatible four-spread supports have two packing completions and fail shattering, constituting one collineation orbit.

## Assumptions and scope

Work in the unique four-dimensional binary vector space, whose fifteen nonzero vectors represent projective points. Each line is \(\{a,b,a+b\}\) for independent nonzero vectors \(a,b\). A *spread* is a five-line partition of the fifteen projective points. A *packing* is a seven-spread partition of all 35 projective lines. These are ordinary unlabeled partitions: no ordering of lines within a spread or spreads within a packing is retained. The Boolean concept corresponding to a packing \(P\) is the indicator function \(s\mapsto\mathbf1_{s\in P}\) on the fixed 56-element spread universe. All statements are exact for \(\operatorname{PG}(3,2)\), not assertions about larger projective spaces.

## Proof

**1. Exhaustive finite incidence lemma.** In this space, there are 35 distinct lines, 56 spreads and 240 packings. For a support \(T\) of \(k\) distinct spreads contained in some packing, write \(c(T)=|\{P\in\mathcal P:T\subseteq P\}|\). The exhaustive incidence table is

| \(k\) | Compatible supports | Values of \(c(T)\), with multiplicities |
|---|---:|---|
| 1 | 56 | 30 for every support |
| 2 | 840 | 6 for every support |
| 3 | 4200 | 2 for every support |
| 4 | 7560 | 1 for 6720 supports; 2 for 840 supports |
| 5 | 5040 | 1 for every support |

Here *compatible* means contained in some packing. This is a finite theorem certified by the self-contained exact-cover algorithms in `verify.py` and the independent labelled-Fano construction in `verify_fano.py`. To see why the enumeration is complete, form each projective line from a pair \(a,b\) and their vector sum; recursively cover the least uncovered point by a disjoint line, obtaining all spreads. Then recursively cover the least uncovered line by a disjoint spread, obtaining all packings. Every unordered exact cover has a unique ascending branch determined by its first uncovered element. The checker reconstructs the incidence table, rather than assuming it. Its labels may be permuted without changing the table. The Fano construction instead enumerates all seven-line labelled Fano planes on eight labels, modulo repeated labelled systems; it independently obtains the same table and verifies every relevant Boolean trace.

**2. Necessity.** Any shattered support must be contained in a packing, since its all-positive trace must occur. If a four-support \(T\) occurs in two packings, consider \(T\setminus\{x\}\). Exactly two packings contain that triple by the table, and both already contain \(x\); hence the trace with precisely \(x\) negative is impossible. Thus a shattered four-support has a unique packing completion.

**3. Sufficiency for sizes one through three.** Let \(T\) of size \(k\le3\) lie in a packing. Its all-positive trace exists. For \(k=3\), any chosen pair occurs in six packings, at most two of which include the omitted spread, so the corresponding two-positive trace exists. A chosen singleton lies in 30 packings, at most twelve of which contain either of the two excluded spreads, so its one-positive trace exists. At least \(240-3\cdot30>0\) packings avoid all three selected spreads. The same estimates, or restriction to a subset, establish all traces for \(k=1,2\).

**4. Sufficiency for unique four-completions.** Suppose \(|T|=4\) and precisely one packing contains \(T\). All-positive and all-negative traces exist, the latter because at least \(240-4\cdot30>0\) packings avoid \(T\). For any three selected spreads, exactly two packings contain them and only one contains the fourth: the second packing realizes the three-positive trace. A specified pair occurs in six packings; each of the two excluded spreads occupies at most two of these six, so at least two choices realize exactly that pair. A specified singleton occurs in 30 packings; each of the three excluded spreads rules out at most six, leaving at least twelve choices. Thus all sixteen traces are present.

**5. Exclusion of larger supports.** If a five-support \(T\) were shattered, every four-subset \(Q\subset T\) would be shattered and thus have a unique packing completion. But the packing realizing the all-positive trace on \(T\) would also contain \(Q\) and its fifth spread, contradicting the required trace positive on \(Q\) and negative on the fifth spread. Shattering is hereditary, so none of the larger supports is shattered.

**6. Counts, purity, and orbits.** The table gives 56, 840 and 4200 shattered supports of sizes one through three and exactly 6720 shattered four-supports. Every compatible triple belongs to two different packings; choose a fourth spread in one packing but not the other. Its extension is unique and hence is a shattered four-support. Every compatible pair and singleton extends to a compatible triple. Therefore all maximal shattered supports have size four. The projective group is generated by adjacent basis transpositions and elementary binary transvections. Acting on all compatible four-supports, an exact orbit traversal checks group order 20160 and partitions the unique-completion supports into two orbits, each of size 3360; it partitions the double-completion supports into one orbit of size 840. Each packing contains exactly 28 unique-completion four-supports, because there are 35 four-subsets of its seven spreads and exactly seven shared with another packing. The two facet orbits map to the two 120-element packing orbits, distinguishing the two facet types by the projective type of their unique completion. Two independently constructed orbit checks are supplied in `symmetry.py` and `verify_fano.py`.

## Verification

Run from the directory containing the files:

```sh
python3 verify.py
python3 symmetry.py
python3 verify_fano.py
```

Each program uses only the Python standard library. Expected terminal markers include `PACKING_SHATTER_PASS`, `GL4_ACTION_PASS`, and `FANO_PACKING_SHATTER_PASS`. The first program enumerates exact covers and verifies direct Boolean traces. The second verifies the full 20160-element projective linear group action and the orbit sizes. The third uses an independent labelled-Fano model of all packings, directly recomputes the incidence and trace distributions and obtains the same orbit split. The finite search is exhaustive for this particular finite object, not an inference from statistical sampling.

## Relationship to prior work

The 56 spreads and 240 packings are classical, not claimed as discoveries here. Magaud's public December 2021 proceedings paper (followed by the January 2022 arXiv posting) describes and verifies these configurations and their two projective packing orbits. Green's public 2025 work realizes the 240 packings through labelled Fano planes and the \(E_8\) root system and studies a Bruhat-like order and group actions. A related finite packing-trade computation analyzes when two packings share four constituent spreads, including the 840 such pairs; that intersection statistic is credited as prior information rather than rebranded as new. The present result instead classifies **every Boolean spread-membership trace support**, gives a unique-completion criterion for its facets, proves purity, and determines the complete face polynomial and facet orbits. The relationship is nontrivial: knowledge of pairwise packing overlaps alone is not an explicit determination of all binary traces on each support.

## Limitations

This is a finite classification for the smallest binary projective 3-space. It does not imply the same classification for other fields or projective dimensions and does not establish the adaptive/Littlestone dimension. Although the two geometric encodings independently reproduce the complete incidence spectrum, no separate external mathematical audit has been conducted. Historical priority cannot be guaranteed against unindexed classical design-theory computations; the sources inspected do not explicitly give the present VC-shattering classification.

## References

- N. Magaud, *Spreads and Packings of PG(3,2), Formally!*, first publicly included in ADG 2021 proceedings by December 2021, https://doi.org/10.4204/EPTCS.352.12 and https://arxiv.org/abs/2112.14770; standalone preprint dated 2022-01-03, https://arxiv.org/abs/2201.00541 (full-text Sections 2–4 inspected). Related expanded presentation: *Proof Pearl: Formalizing Spreads and Packings of the Smallest Projective Space PG(3,2) Using the Coq Proof Assistant*, ITP 2022, https://doi.org/10.4230/LIPIcs.ITP.2022.25.
- R. M. Green, *A partial order on the 240 packings of PG(3,2)*, public preprint dated 2025-11-04, https://arxiv.org/abs/2511.03040 (full-text Sections 1–3, 5 and concluding discussion inspected).
- J. W. P. Hirschfeld, *Finite Projective Spaces of Three Dimensions*, 1985, §17.5 (cited by the preceding primary works for classical packing facts; not separately used as evidence of an unreported shattering result).
