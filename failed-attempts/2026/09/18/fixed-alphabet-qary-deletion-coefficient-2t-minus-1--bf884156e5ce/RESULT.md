# Corroborating derivation of the fixed-alphabet q-ary deletion coefficient \(2t-1\)

## Provenance correction

This package is **not a separate originality claim**. The same theorem had already been added to the
SCOPE repository in the record

`2026/09/18/fixed-qary-deletion-codes-2t-minus-1--0b8ba422fcea`

at commit `16286e5fce08fe8b0dfd1d35cec5c21c696f587b`, timestamped
2026-09-18 04:23:02 UTC. This record first entered the repository later that day at commit
`c4a347eb8acfce1ceee4652e749e43e2c5fa463b`, timestamped 2026-09-18 19:28:14 UTC.

The mathematics below remains valid and provides a separately written corroborating derivation, plus a
finite verification artifact for the q-ary local-bubble step. It should not be counted as an additional
independent discovery of the theorem.

## Result

Let \(q\ge2\) and \(t\ge2\) be fixed. For all sufficiently large \(n\), there is a code
\(C\subseteq\Sigma_q^n\) correcting \(t\) deletions with
\[
n-\log_q|C|
\le (2t-1)\log_q n+O_{q,t}(\log\log n).
\]
Equivalently, in bits,
\[
\bigl(n-\log_q|C|\bigr)\log_2 q
\le (2t-1)\log_2 n+O_{q,t}(\log\log n).
\]

This is the fixed-alphabet extension of Eyal En Gad's binary theorem
(arXiv:2609.19493). En Gad's Section 8 explicitly lists the fixed-larger-alphabet coefficient
\(2t-1\) as an open question.

## Proof

We retain En Gad's binary length scale
\[
k=2\lceil\log_2 n\rceil+2,\qquad L=3(k+1).
\]
A q-ary word is \(k\)-unique if its length-\(k\) substrings are pairwise distinct. For two distinct
starting positions, equality of the corresponding length-\(k\) windows has probability exactly
\(q^{-k}\), including when the windows overlap: for shift \(s<k\), equality says that a block of
length \(k+s\) has period \(s\), leaving \(q^s\) choices among \(q^{k+s}\). Therefore
\[
\Pr[\text{not \(k\)-unique}]
\le {n\choose2}q^{-k}
\le {n\choose2}2^{-k}<\frac18,
\]
so a positive constant fraction of all q-ary words are \(k\)-unique.

As in the binary proof, an \((L-1)\)-unique word traces a simple path in the q-ary de Bruijn graph,
and its Boolean length-\(L\) spectrum determines the word. The shared-source-letters lemma is purely
positional and is unchanged by the alphabet size.

For the local edit step, let \(d\in\Sigma_q\), \(1\le\rho\le k+1\), and let \(A,B\) have length
\(L-\rho\) with
\[
A_{\rm last}\ne d,\qquad B_{\rm first}\ne d.
\]
Set
\[
P=A d^\rho B,\qquad P'=A d^{\rho-1}B.
\]
The two walks have the same first and last \(L-1\) letters. If a vertex window of \(P\), beginning at
offset \(a\), equals a vertex window of \(P'\), beginning at offset \(b\), the shared-source lemma gives
\(a-b\in\{0,1\}\). If \(a=b>0\), the compared windows include the location where the longer word has
\(d\) and the shorter word has \(B_{\rm first}\ne d\), contradiction. If \(a=b+1\) before the
terminal vertex, they include the location where the longer word has \(d\) and the shorter word has
\(A_{\rm last}\ne d\), contradiction. Hence only the two endpoints are shared. Thus every separated
single insertion/deletion gives the same bubble structure as in the binary proof. A separated
alignment with \(t\) deletions and \(t\) insertions gives a rule consisting of \(2t\) vertex-disjoint
bubbles with entries in \(\{-1,0,1\}\).

The random torus hash acts on the integer spectrum vector and is independent of the alphabet size.
Exceptional alignments still have only
\[
O_{q,t}(L n^{2t-1})
\]
records: the binary factor \(2^d\) for inserted symbols becomes \(q^d\), a constant for fixed \(q,t\).

The bounded-witness extraction is also alphabet-free once the bubble catalogue has the same support
properties. The counting lemma changes only by a constant number of q-ary choices per local
instruction: a bubble header records the edited symbol \(d\), and transferring a \(k\)-stretch across a
deletion may require one extra q-ary symbol. Thus for some constant \(a_{q,t}\), generating witness
sets with \(R\) rules and \(c\) connected bubble-support components number at most
\[
n^c(LR)^{a_{q,t}R}.
\]
Because we retained \(L\ge\log_2 n\), En Gad's large-witness absorption \(n\le2^R\) for \(R>L\)
remains literally valid.

Consequently one may choose
\[
Q=C_{q,t}\,n^{2t-1}L^{b_{q,t}}
\]
with fixed constants \(C_{q,t},b_{q,t}\) so that a positive constant fraction of \(k\)-unique words
survive the exceptional-conflict and non-bipartite-component discards. Taking one side of every
remaining bipartite component and then the largest hash-label class gives
\[
|C|\ge c_{q,t}\frac{q^n}{Q}.
\]
Therefore
\[
n-\log_q|C|
\le (2t-1)\log_q n+O_{q,t}(\log\log n).
\]

## Independent-audit verification

The local verification artifact `artifacts/verify_qary_local.py` was rerun during the independent
audit. It reproduced:

- 42 exact overlapping-window probability cases;
- 2,783,928 q-ary local bubble cases;
- 32,642,112 offset comparisons;

and ended with `PASS`.

These checks corroborate the local q-ary step; the all-\(n\) theorem is established by the analytic
argument above.

## Scientific status

The theorem itself is a meaningful resolution of En Gad's fixed-alphabet open question, but within
this repository that result belongs to the earlier record
`fixed-qary-deletion-codes-2t-minus-1--0b8ba422fcea`. The present record is retained only as
corroborating derivation and reproducibility evidence.

## Limitations

- This record is not a separate original discovery.
- The construction is existential and does not provide efficient encoding or decoding.
- \(q\) and \(t\) are fixed as \(n\to\infty\).
- The \(O_{q,t}(\log\log n)\) term remains, and no coefficient below \(2t-1\) is proved.
- The external priority question remains unusually time-sensitive because En Gad's motivating preprint
  was posted only days before these SCOPE records.

## References

1. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*,
   arXiv:2609.19493 (2026).
2. S. Liu, I. Tjuawinata and C. Xing, *Explicit Construction of q-ary 2-deletion Correcting Codes
   with Low Redundancy*, arXiv:2306.02868 / IEEE Trans. Inf. Theory 70 (2024).
3. W. Song and K. Cai, *Non-binary Two-Deletion Correcting Codes and Burst-Deletion Correcting
   Codes*, arXiv:2210.14006.
