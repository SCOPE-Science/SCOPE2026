# Conditional alternation: exact shattering series and a sharp one-third dimension law

## Finding

Let \(\mathcal H_n\subseteq\{0,1\}^n\), for integers \(n\ge0\), consist of the length-\(n\) binary words containing neither `000` nor `011` as a consecutive factor. Equivalently, whenever a zero starts a three-letter window, its two successors must differ. For a coordinate support \(S\subseteq[n]\), call \(S\) *shattered* if for every assignment \(\lambda:S\to\{0,1\}\) there is a word \(w\in\mathcal H_n\) with \(w_i=\lambda(i)\) for each \(i\in S\). Put \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\).

The complete two-variable generating function is

\[
\boxed{\sum_{n\ge0}\Phi_n(z)t^n=\frac{1-t+tz+t^2z^2-2t^3z+t^3z^2+t^4z-t^4z^2}{(1-t)(1-t-2t^3z+t^4z)}.}
\]

For every integer \(n\ge1\), the exact VC dimension is

\[
\boxed{\operatorname{VCdim}(\mathcal H_n)=\left\lfloor\frac{n+4}{3}\right\rfloor,}\qquad \operatorname{VCdim}(\mathcal H_0)=0.
\]

In particular, the first coefficients are \(\Phi_5(z)=1+5z+10z^2+2z^3\), \(\Phi_8(z)=1+8z+28z^2+30z^3+4z^4\), and \(\Phi_9(z)=1+9z+36z^2+50z^3+16z^4\). A 14-state automaton given below recognizes exactly the indicator words of shattered supports. It has a finite potential certificate proving the bound at *every* length.

## Assumptions and scope

Words are linearly indexed, not cyclic. Factors are contiguous. The support indicator has `1` in selected coordinates and `0` elsewhere; these indicator bits are *not* the hypothesis bits. The existential completion of unspecified coordinates may depend on the queried assignment. The empty support is shattered because \(\mathcal H_n\) is nonempty at every length. Ordinary VC dimension is used; no assertion about Littlestone dimension or fixed-background independence entropy is made.

## Proof

**Forbidden-pattern automaton.** The four states \(q_0,q_1,q_2,q_3\) record the longest suffix of the currently read hypothesis word that is a proper prefix of a forbidden factor, represented respectively by the suffixes ``, `0`, `00`, `01`. Its bit transitions are

| State | Read `0` | Read `1` |
|---|---|---|
| \(q_0\) | \(q_1\) | \(q_0\) |
| \(q_1\) | \(q_2\) | \(q_3\) |
| \(q_2\) | reject | \(q_3\) |
| \(q_3\) | \(q_1\) | reject |

All four nonrejecting states accept at the end of a word. Identify subsets of these four states by four-bit masks, with the bit of \(q_0\) least significant. If \(P\) is such a subset, define \(\delta_b(P)\) to be the set of nonrejecting successors on hypothesis bit \(b\). Thus \(\delta_b\) distributes over unions, and \(\delta_b(\varnothing)=\varnothing\).

**Universal-support determinization.** After reading an indicator prefix, each fixed assignment to queried positions leaves a nonempty subset \(P\) of possible hypothesis-automaton states if and only if that assignment can be completed up to this point. To require this for *every* assignment, keep an antichain \(\mathcal F\) of inclusion-minimal such subsets: larger subsets can be discarded because the corresponding assignment is less restrictive under all future updates. Initially \(\mathcal F=\{\{q_0\}\}\), encoded as `(1,)`. On an unqueried indicator bit `0`, send every \(P\in\mathcal F\) to \(\delta_0(P)\cup\delta_1(P)\); on a queried indicator bit `1`, send every \(P\) to *both* \(\delta_0(P)\) and \(\delta_1(P)\). If any resulting subset is empty the support indicator is rejected; otherwise retain just inclusion-minimal subsets. Induction on the indicator prefix proves this construction accepts exactly the shattered supports. In particular, discarding supersets is valid because successor maps preserve set inclusion for each future bit and every branch.

An explicit breadth-first closure yields the following complete reachable table. Each state is written as the sorted antichain of nonzero subset masks, followed by its two successor indices; `-` is rejection. The state indexed `0` is initial. Every listed state is accepting.

| \(i\) | Antichain of masks | Indicator `0` | Indicator `1` |
|---:|---|---:|---:|
|0|`(1,)`|1|2|
|1|`(3,)`|3|4|
|2|`(1,2)`|5|6|
|3|`(15,)`|3|4|
|4|`(6,9)`|5|6|
|5|`(3,12)`|7|8|
|6|`(1,2,4,8)`|8|-|
|7|`(10,)`|9|10|
|8|`(2,8)`|11|-|
|9|`(14,)`|9|10|
|10|`(6,8)`|11|-|
|11|`(2,12)`|12|13|
|12|`(10,12)`|7|8|
|13|`(2,4,8)`|8|-|

Closure of these 14 states under the stated update rule is a finite exact check, not a sampling argument. Let \(T_0,T_1\) be their Boolean adjacency matrices: \((T_b)_{ij}=1\) if the table gives a transition from \(i\) to \(j\) on indicator bit \(b\), and zero otherwise. With \(e_0\) the initial coordinate vector and \({\bf1}\) the 14-component vector of ones, the exact transfer identity is

\[
\sum_{n\ge0}\Phi_n(z)t^n=e_0^\mathsf T\left(I-tT_0-tzT_1\right)^{-1}{\bf1}.
\]

Elementary rational elimination in the explicit 14-by-14 matrix gives the stated displayed fraction (and the attached checker independently evaluates the symbolic resolvent). The matrix identity itself follows from the expansion as a formal power series, since each accepted indicator path of length \(n\) contributes weight \(z^{|S|}\).

**Uniform upper bound.** Assign to the table states the nonnegative potential

\[
(D_0,\ldots,D_{13})=(4,4,2,4,2,3,0,3,1,3,1,2,3,0).
\]

A direct examination of *every* allowed table transition \(i\xrightarrow{s}j\), with \(s\in\{0,1\}\), establishes

\[
D_i\ge 3s-1+D_j.
\]

Summing these inequalities along an accepted indicator word of length \(n\) with \(k\) selected positions telescopes to \(3k-n\le D_0-D_{\rm final}\le4\). Thus \(k\le\lfloor(n+4)/3\rfloor\). The complete potential vector and transition table are exact finite certificates for the *infinite-length* upper bound.

**Sharp construction.** For each \(k\ge0\), the indicator word `11(001)^k` is accepted: after its initial `11`, the table is in state `6`, each factor `001` first follows \(6\to8\to11\to13\), and thereafter loops \(13\to8\to11\to13\). Appending zero, one, or two additional indicator zeros preserves acceptance (states `13`, `8`, `11`, respectively). The resulting supports have \(k+2\) members on lengths \(3k+2\), \(3k+3\), or \(3k+4\), meeting the upper bound. For length one the indicator `1` is accepted. Together with the length-zero convention, this proves the exact dimension formula.

## Verification

The standalone `verify_conditional_alternation.py` reconstructs the DFA, performs antichain determinization and checks every row of the table; then it verifies the complete 14-state potential inequality. Independently, it enumerates all admissible hypothesis words, all supports, and all coordinate traces at each length through 12, comparing the direct result with the automaton. It checks 28 generating-function coefficients against the exact rational identity and, when `sympy` is installed, evaluates the full symbolic matrix resolvent. Run `python3 verify_conditional_alternation.py` with Python 3; `sympy` is required only for the optional symbolic-resolvent check. The actual replay and exact output are supplied in `verification_output.txt`. The finite experiments corroborate the matrix identity and proof; they are not substituted for the all-length argument.

## Relationship to prior work

The family is a two-step conditional-alternation constraint: after a zero, the next two bits must differ. This is not the two-monochromatic-triples language (`000`,`111`) for which a prior exact shattering polynomial and \(\lfloor n/2\rfloor+1\) dimension are known, nor the distinct language (`000`,`101`) previously analyzed by a five-state automaton. For example, at length eight the first comparator has \(41\) supports of size four (and eight of size five), whereas the current language has just four size-four supports and no size-five supports; therefore neither exact shattering enumeration is a rephrasing of the other. These counts do not alone establish priority; the inspected proofs concern different forbidden languages.

Johnson (2021) studies the VC dimension of translates of an individual infinite binary word, rather than all coordinate projections of the entire finite pattern-avoiding language. Eğecioğlu and Iršič (2020) study binary run-restricted hypercube graphs and enumerative properties, not the universal-existential coordinate shattering criterion here. The 14-state support-recognition theorem, its rational face series and the sharp conditional-alternation VC formula are the specific new claims.

## Limitations

The proof concerns the exact pair of forbidden contiguous factors `000` and `011`, on finite *linear* words. It makes no claims about length-four constraints, cyclic words, equivalence of all forbidden-factor pairs, Littlestone dimension, or all related shifts. The novelty search is evidence-based, not a theorem of unique historical priority; unindexed or inaccessible equivalent results could exist. No independent mathematical review has been performed.

## References

1. H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490, first publicly posted 2021-01-16, https://arxiv.org/abs/2101.06490.
2. Ö. Eğecioğlu and V. Iršič, *Fibonacci-run graphs I: basic properties*, arXiv:2010.05518, first publicly posted 2020-10-12, https://arxiv.org/abs/2010.05518.
3. *A regular shattering complex for binary words with no monochromatic triple*, available at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-regular-shattering-complex-for-binary-words-with-no-monochroma--a86c7bc37664.
