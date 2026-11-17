# Exact Griesmer attainment for three-dimensional binary functional batch retrieval

## Finding

Write \(\mathrm{FB}(3,t,2)\) for the shortest length of a rank-three binary linear storage matrix serving **every multiset** of \(t\) nonzero linear-form requests by \(t\) pairwise disjoint sets of columns. For every integer \(t\geq1\),

\[
\boxed{\mathrm{FB}(3,t,2)=t+\left\lceil\frac t2\right\rceil+\left\lceil\frac t4\right\rceil+\mathbf{1}_{\{t=2\}}.}
\]

In particular, \(\mathrm{FB}(3,6,2)=11\) and \(\mathrm{FB}(3,10,2)=18\). Except at \(t=2\), the optimum attains the binary dimension-three Griesmer lower bound. The special case of repeated identical requests (functional PIR) attains that lower bound even at \(t=2\).

## Assumptions and scope

All vector spaces are over \(\mathbb F_2\), with dimension exactly three and nonzero requested vectors. A matrix with columns \(g_1,\ldots,g_n\in\mathbb F_2^3\) serves \((v_1,\ldots,v_t)\) when there exist pairwise disjoint, nonempty column-index subsets \(R_i\) whose column spans contain \(v_i\). The construction below meets the stronger condition \(\sum_{j\in R_i}g_j=v_i\). Columns may repeat, and no locality restriction is imposed. The minimum is taken over all rank-three matrices, not only systematic ones.

Represent \(\mathbb F_2^3\setminus\{0\}\) by the integers \(1,\ldots,7\) with addition equal to bitwise XOR. Six finite blocks, listed by their ordered columns, are used:

| Role | Columns | Request count | Length |
|---|---|---:|---:|
| \(A\) | `1,2,4` | \(1\), functional batch | 3 |
| \(P\) | `1,2,4,7` | \(2\), identical requests only | 4 |
| \(B\) | `1,1,2,4,6` | \(2\), functional batch | 5 |
| \(C\) | `1,2,3,4,5,6` | \(3\), functional batch | 6 |
| \(D\) | `1,2,3,4,5,6,7` | \(4\), functional batch | 7 |
| \(E\) | `1,2,3,4,5,6,7,1,2,4,7` | \(6\), functional batch | 11 |

The certificates in `recovery_certificates.json` supply an explicit disjoint-recovery partition for **every** request multiset in each relevant block. There are, respectively, \(7,7,28,84,210,924\) complete request cases, totaling \(1260\); the second block requires only repeated-request lists.

## Proof

**Lower bound.** Suppose a rank-three matrix serves any list of \(t\) nonzero requests. For each nonzero information vector \(a\), select a nonzero target \(v\) with \(a\cdot v=1\). Every one of the \(t\) pairwise disjoint recovery sets of \(v\) must meet the support of the nonzero codeword \((a\cdot g_j)_{j=1}^n\). Therefore the generated binary code has minimum distance at least \(t\). The classical binary Griesmer bound gives

\[
n\geq t+\left\lceil\frac t2\right\rceil+\left\lceil\frac t4\right\rceil=:G(t).
\]

**Finite blocks.** For each of \(A,B,C,D,E\), the supplied finite certificate exhibits disjoint nonempty recovery sets for every multiset of the indicated size drawn from all seven nonzero targets, and not merely from the actual columns. In particular, block \(E\) is a \(6\)-functional batch realization with only eleven columns. For \(P\), the certificate covers every pair of equal nonzero requests, making it a \(2\)-functional PIR realization of length four. `checker.py` checks the entire specified finite request domain, all bit masks, every XOR, pairwise disjointness, and rank three; no numerical optimization assertion is used in this finite proof.

**All request counts.** A concatenation of a \(u\)-functional batch block and a \(v\)-functional batch block is a \((u+v)\)-functional batch block: split any multiset of \(u+v\) requests into arbitrary submultisets of these sizes and use disjoint physical blocks. Write \(t=4a+r\), with \(0\leq r\leq3\). The following constructions all have exactly \(G(t)\) columns:

- \(r=0\): \(a\) copies of \(D\), provided \(a\geq1\).
- \(r=1\): \(a\) copies of \(D\), followed by \(A\).
- \(r=2\), \(a\geq1\): \(a-1\) copies of \(D\), followed by \(E\).
- \(r=3\): \(a\) copies of \(D\), followed by \(C\).

The sole omitted case is \(t=2\), where \(B\) supplies length five. Block \(P\) shows that functional PIR at \(t=2\) still attains \(G(2)=4\).

**Strict exception at two requests.** If a rank-three four-column binary generator supported two disjoint recoveries of every nonzero target, the preceding support argument would give a \([4,3,d\geq2]\) code. Its one-dimensional dual must be spanned by the all-ones word; otherwise some coordinate would support a weight-one codeword. Consequently its four nonzero, distinct columns sum to zero. There are three nonzero targets that are not themselves columns. For any such target, any recovery subset must contain at least two columns. To serve two different such targets with just four columns one would need two complementary pairs. But the sums of complementary pairs are equal because all four columns sum to zero. This is impossible. Thus \(\mathrm{FB}(3,2,2)>4\), and block \(B\) establishes equality with five.

Together the lower bound and constructions give the stated formula for every positive integer \(t\).

## Verification

Run `python3 checker.py` with `recovery_certificates.json` in the same directory. The checker re-derives the full finite list of nonzero request multisets (rather than relying on a list of favored requests), checks exactly one certificate per multiset, verifies every indicated XOR and disjointness, and checks the ranks of all six matrices. Its expected final line is `PASS: 1260 exhaustive finite request instances; all recoveries independent/disjoint`. The infinite extension is the concatenation argument above, not an inference from a finite experiment.

## Relationship to prior work

The 2019 functional PIR/batch study of Zhang, Etzion, and Yaakobi develops the model, proves the seven-column dimension-three four-request functional batch construction, and tabulates an upper bound of nineteen for **functional PIR** at ten requests in dimension three; our eleven-column six-request **functional batch** block and the resulting eighteen-column ten-request batch design are not established in its inspected results. The 2025 study of Kılıç, Ravagnani, and Salizzoni establishes certain exact functional PIR lengths and the binary simplex-multiple family, but its displayed recurrence concerns functional PIR rather than the simultaneous, possibly different, requests required here. The 2026 all-symbol study of Boruchovsky, Gruica, Niemann, and Yaakobi gives the immediate recent motivation for distinguishing retrieval variants; its corresponding inspected results establish small-request parameters rather than this unrestricted all-request-count functional batch law.

The standard Griesmer inequality is prior knowledge, as are the functional batch definition and some individual blocks. The statement claimed here is their all-length sharp combination driven by the explicit six-request block and a complete two-request exception; we do not claim the classical components separately as new.

## Limitations

The theorem is confined to binary linear rank-three storage matrices, unrestricted recovery subset sizes, and exact nonzero linear-form requests. It does not settle higher dimensions, nonbinary fields, bounded-locality retrieval, or actual PIR-protocol communication costs. The finite witnesses have been checked computationally; independent mathematical verification and definitive historical priority confirmation have not been performed.

## References

1. Y. Zhang, T. Etzion, E. Yaakobi, *Bounds on the Length of Functional PIR and Batch Codes*, arXiv:1901.01605, first public January 6, 2019. https://arxiv.org/html/1901.01605v2
2. A. B. Kılıç, A. Ravagnani, F. Salizzoni, *The Length of Functional Batch and PIR Codes*, arXiv:2508.02586, first public August 4, 2025. https://arxiv.org/html/2508.02586v2
3. A. Boruchovsky, A. Gruica, J. Niemann, E. Yaakobi, *Serving Every Symbol: All-Symbol PIR and Batch Codes*, arXiv:2601.04041, first public January 7, 2026. https://arxiv.org/html/2601.04041v2
4. J. H. Griesmer, *A bound for error-correcting codes*, IBM Journal of Research and Development **4** (1960), 532–542.
