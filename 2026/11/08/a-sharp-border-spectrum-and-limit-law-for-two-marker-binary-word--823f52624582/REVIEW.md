# Scientific review: sharp border spectrum and limit law for two-marker binary words

## Correctness — PASS

The finite statement specifies exact binary words with two \(1\)s, indexed linear length \(n\ge2\), and *proper* exact borders. The proof partitions borders into those containing zero, one or two markers; the two-marker case cannot occur for a proper border. The only possible one-marker border has length \(a+c+1\) and requires \(b\ge\max(a,c)\). The resulting disjoint gap classes give the integer spectrum, the rational bivariate generating function, and a sharp maximum. Uniform \(O(1)\) accuracy of the finite count relative to the scaled piecewise density yields the local limit and moment formulas. Finite checks used a KMP implementation independent of the gap classification, all \(121485\) eligible words through length \(90\), plus formal rational coefficient checks and large-length arithmetic. None of the infinite proof depends on experimental extrapolation.

## Originality — PASS, with historical-priority qualification

Holub and Shallit (arXiv:1509.05240v1, 2015) analyze longest borders of unrestricted uniform words; their full paper establishes bounded limiting expectation and recurrence methods, not a fixed-weight-two all-length distribution or macroscopic limit. The period-set realization theorem of Halava, Harju and Ilie (2000) does not enumerate this constrained ensemble. Harju and Nowotka (TUCS TR 546, 2003) study bordered versus unbordered cyclic conjugates rather than the longest-border length of each fixed-content word. Related Abelian-border counts use a weaker equivalence relation. The present result supplies a new explicit coefficient law, bivariate enumerator and limit distribution that are not a direct numerical substitution in those published formulas. Searches of relevant mathematical records produced no covering claim. As with any literature search, an unindexed or implicit earlier equivalent remains possible; this is not a claim of absolute historical priority.

## Value — PASS

Border lengths control least periods, self-overlap and prefix-suffix synchronization. For the simplest nontrivial fixed-marker family with competing border types (two ones), the work gives an exact complete length spectrum, sharp extremal value, uniform local limit and explicit moments. The limiting border has order \(n\), in contrast to the order-one longest border under unrestricted fixed-alphabet sampling. Its density is flat to \(1/3\) and then declines linearly to \(2/3\); this structural transition records the competition between zero-only and one-marker self-overlaps. The precise finite distribution and phase transition are the mathematical contribution, rather than the elementary act of computing one particular border.

## Closest literature and limitations

- Š. Holub and J. Shallit, *Periods and borders of random words*, arXiv:1509.05240v1; STACS 2016, https://arxiv.org/html/1509.05240v1 . Inspected full HTML text, Sections 1–6, including statements of Theorems 3, 5, 7, 8.
- V. Halava, T. Harju, L. Ilie, *Periods and Binary Words*, JCTA 89 (2000), 298–303; full open manuscript https://www.csd.uwo.ca/~ilie/JCTA00.pdf . Its proved theorem is realization of period sets over binary alphabets.
- T. Harju, D. Nowotka, *Border Correlation of Binary Words*, TUCS TR 546 (2003), https://citeseerx.ist.psu.edu/document?doi=912065a268d68bfb1e44494181f636a0c491d9c2&repid=rep1&type=pdf . Inspected extracted text including the introduction, main results and final discussion; its target statistic is cyclic-conjugate border status.
- M. Christodoulakis et al., *Abelian borders in binary words*, Discrete Applied Mathematics 171 (2014), 141–146. Abstract inspected only; this is about Abelian, not exact, borders.

No assertion is made for unrestricted words at positive marker density, other finite alphabets, or circular words. Automated checks are finite; independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
