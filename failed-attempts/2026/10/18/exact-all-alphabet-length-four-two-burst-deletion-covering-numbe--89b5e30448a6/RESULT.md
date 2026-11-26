# Exact all-alphabet length-four two-burst-deletion covering number

## Finding

For an alphabet \(\Sigma\) with \(|\Sigma|=q\ge2\), denote by \(B_q(4,2)\) the least size of a length-four code \(C\subseteq\Sigma^4\) for which every ordered pair in \(\Sigma^2\) is obtained from some codeword by deleting exactly two **consecutive** coordinates. Then

\[
\boxed{B_q(4,2)=\left\lceil\frac{q^2}{3}\right\rceil \qquad(q\ge2).}
\]

There is a uniform explicit optimal construction. When \(3\mid q\), its deletion-output sets are disjoint triples and hence partition all \(q^2\) ordered pairs. When \(3\nmid q\), each codeword still has three distinct outputs; precisely two outputs appear twice and the remaining outputs appear once. In particular the values for \(q=2,3,4,5,6,7,8\) are \(2,3,6,9,12,17,22\), respectively.

## Assumptions and scope

An alphabet is merely a set of \(q\) distinguishable labels, and the code has **fixed length four**. The deletion channel removes one pair of adjacent positions, either positions \(1,2\), positions \(2,3\), or positions \(3,4\). Its outputs are distinct words, not deletion scripts with multiplicity. The result is about *covering*, not about general-radius deletion correction, arbitrary two deletions, or longer block lengths.

For \(x=(a,b,c,d)\), the set of distinct two-burst-deletion outputs is
\[
\mathcal D(x)=\{(c,d),(a,d),(a,b)\}.
\]

## Proof

**1. Lower bound.** Every length-four source has at most three two-burst-deletion outputs, because there are only three possible consecutive pairs to delete. A code covering all \(q^2\) ordered pairs therefore has size at least \(\lceil q^2/3\rceil\).

**2. Incidence-grid interpretation.** Identify an ordered pair \((i,j)\) with cell \((i,j)\) of a \(q\)-by-\(q\) grid. For \(x=(a,b,c,d)\) with \(a\ne c\) and \(b\ne d\), the outputs occupy three distinct cells \((a,b),(a,d),(c,d)\): the three corners of a \(2\)-by-\(2\) subrectangle other than \((c,b)\). Conversely every such three-corner placement comes from precisely the displayed source form. Thus a cover by codewords with three distinct outputs is equivalent to covering the grid with these oriented three-cell corner tiles, whose arms may span nonconsecutive rows or columns.

**3. Seven local templates.** For a rectangle with \(r\) row labels \(0,\ldots,r-1\) and \(s\) column labels \(0,\ldots,s-1\), write each codeword as the literal four-digit tuple \(abcd\) interpreted as \((a,b,c,d)\), where \(a,c\) are local row indices and \(b,d\) are local column indices. The following exact templates cover every cell of their indicated rectangle:

| Rectangle | Four-index templates | Output multiplicities |
| --- | --- | --- |
| \(2\times2\) | `0110`, `1100` | two cells twice, others once |
| \(2\times3\) | `0012`, `1001` | all cells once |
| \(3\times2\) | `0120`, `1021` | all cells once |
| \(3\times3\) | `0211`, `1022`, `2100` | all cells once |
| \(3\times4\) | `0210`, `0123`, `1321`, `2012` | all cells once |
| \(4\times3\) | `0120`, `1130`, `2112`, `3102` | all cells once |
| \(4\times4\) | `0122`, `0320`, `1331`, `2113`, `3310`, `3312` | two cells twice, others once |

For each row of this table, direct substitution into \(\mathcal D(a,b,c,d)=\{(c,d),(a,d),(a,b)\}\) verifies both the asserted cell coverage and multiplicities. Every listed word has three distinct outputs, since \(a\ne c\) and \(b\ne d\). The two exceptional rectangles use two more incidences than their area; each other rectangle uses precisely its area.

**4. Partition the whole square.** Split both the row labels and column labels into blocks of equal sizes as follows:

- if \(q=3k\), take \(k\) blocks of size \(3\);
- if \(q=3k+1\), take \(k-1\) blocks of size \(3\), then one of size \(4\);
- if \(q=3k+2\), take \(k\) blocks of size \(3\), then one of size \(2\).

These formulas cover every \(q\ge2\); the middle case begins at \(q=4\). For each Cartesian-product rectangle of a row block and a column block, apply the corresponding local template, relabeling the local row and column indices by their actual alphabet symbols. Since the row-column rectangles partition all \(q^2\) cells, this gives a global cover; no two codewords from different rectangles coincide, because their first/third and second/fourth coordinates locate their source rectangle uniquely.

When \(3\mid q\), all rectangles are \(3\)-by-\(3\), and the code has exactly \(q^2/3\) words, each output once. Otherwise there is a unique corner rectangle of size \(4\)-by-\(4\) or \(2\)-by-\(2\); every other rectangle is one of the four fully tiled types. Let \(h\) be \(4\) or \(2\), respectively. The global number of codewords is
\[
\frac{q^2-h^2}{3}+\frac{h^2+2}{3}=\frac{q^2+2}{3}=\left\lceil\frac{q^2}{3}\right\rceil,
\]
with exactly the two overlaps from the exceptional corner rectangle. In all cases this attains the lower bound, proving the theorem.

## Verification

The standalone `verify.py` replays all seven local templates, checks their complete cell incidence matrices, generates the block construction for every integer \(2\le q\le100\), and tests codeword uniqueness, exact size, coverage of every ordered pair, and exact stated multiplicities. It uses only the Python standard library and prints `VERIFY_OK` upon success. This finite replay checks the templates and implementation; the all-\(q\) assertion is justified by the universal partition argument above, not by extrapolation.

## Relationship to prior work

Xie, Sun and Ge (2026), arXiv:2606.15379v1, introduce general \(q\)-ary two-burst-deletion covering constructions. Their Theorem VI.1 states the binary differential-VT perfect-covering property, and their Theorem VI.4 gives a general \(q\)-ary family with an existence upper bound \(q^n/(2n\lfloor q/2\rfloor^2)\). Neither displayed theorem specializes to the present sharp all-\(q\) length-four formula or the rectangular incidence tiling. At \(q=4\), for example, that general upper bound gives \(8\) words, whereas the exact optimum here is \(6\). The binary case \(B_2(4,2)=2\) is not claimed as new.

Lenz, Rashtchian, Siegel and Yaakobi (2020), arXiv:1911.09944v4, treat nonburst insertion/deletion covering and asymptotic bounds. Their general deletion-ball results do not supply the present exact adjacent-two-deletion parameter. The potentially familiar finite-grid three-corner tiling viewpoint is an equivalent formulation, so earlier work under a design/tiling vocabulary remains an originality risk.

## Limitations

The formula applies only to a single burst of **exactly two adjacent deletions in a length-four source**. It does not determine higher lengths, unrestricted two-deletion covering, list sizes, or optimal-code classifications. When \(3\mid q\), the exhibited design has disjoint three-output balls; for other alphabets, the two repeated outputs do **not** rule out other types of perfect partitions using irregular smaller balls. An exhaustive literature search cannot certify global novelty.

## References

1. Chengfei Xie, Yubo Sun, and Gennian Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1, June 13, 2026, Sections II and VI. https://arxiv.org/html/2606.15379v1
2. Andreas Lenz, Cyrus Rashtchian, Paul H. Siegel, and Eitan Yaakobi, *Covering Codes using Insertions or Deletions*, arXiv:1911.09944v4, 2020. https://arxiv.org/abs/1911.09944
