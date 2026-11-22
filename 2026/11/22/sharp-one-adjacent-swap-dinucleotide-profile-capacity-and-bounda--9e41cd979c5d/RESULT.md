# Sharp one-adjacent-swap dinucleotide-profile capacity and boundary law

## Finding
For each integer \(q\ge2\), let \(\Sigma\) be a labeled \(q\)-letter alphabet. For a finite linear word \(w\), let \(H_2(w)\in\mathbb Z_{\ge0}^{\Sigma^2}\) record the multiplicity of each ordered adjacent pair. Let \(B_q(w)\) be the number of distinct such vectors obtained from \(w\) by **at most one adjacent interchange**, including the unchanged word. Define
\[
I_q=1+2\binom q2+14\binom q3+24\binom q4.
\]
Then every finite word satisfies
\[
B_q(w)\le M_q:=I_q+2
=3+2\binom q2+14\binom q3+24\binom q4.
\]
The bound is attained for every length \(n\ge q^4+3\) when \(q\ge3\); when \(q=2\), it is attained at **exactly** the lengths \(n\ge8\), and at no smaller lengths. Thus \(M_2=5\), \(M_3=23\), \(M_4=95\), and \(M_5=283\).

Moreover, for independent uniformly sampled letters, \(W_n\in\Sigma^n\), the limit distribution is
\[
\lim_{n\to\infty}\Pr\bigl(B_q(W_n)=I_q+j\bigr)
=\binom2j\left(\frac{q-1}{q}\right)^j\left(\frac1q\right)^{2-j},\quad j=0,1,2,
\]
with probability tending to zero for all other values. In particular, the limiting fraction of maximizing words is \(((q-1)/q)^2\).

## Assumptions and scope
All words are linear and have ordered, overlapping adjacent-pair profiles; letters are distinct labels, and no cyclic wraparound is included. Swaps may exchange identical letters, but the no-error outcome is explicitly included regardless. There is no limitation on multiplicities or composition. The result counts **profiles**, not distinct descendant words or code sizes. The result makes no claim about the exact least saturating length when \(q\ge3\).

For a matrix of ordered-pair unit coordinates, write \(e_{uv}\) for the unit vector indexed by \((u,v)\). For a four-letter context \(abcd\) with the middle two symbols \(b,c\) interchanged, the profile change is
\[
\Delta(a,b,c,d)=e_{ac}+e_{cb}+e_{bd}-e_{ab}-e_{bc}-e_{cd}.
\]
Define \(\mathcal I_q=\{\Delta(a,b,c,d):a,b,c,d\in\Sigma,\ b\ne c\}\); this set includes the zero vector. The support of a change vector is the set of symbols appearing in one of its nonzero ordered-pair coordinates.

## Proof
**1. Exact local support classification.** Direct integer arithmetic in the signed unit-vector formula, checking the at most \(4^4\) four-symbol contexts, establishes that for each specified support \(S\subseteq\Sigma\), the number of distinct nonzero vectors in \(\mathcal I_q\) whose support equals \(S\) is as follows:

| \(|S|\) | Number for each specified support |
|---:|---:|
| 2 | 2 |
| 3 | 14 |
| 4 | 24 |

There is exactly one zero vector and no changes with other nonempty support sizes. This is a finite symbolic classification, not an extrapolation from measurements at small alphabet sizes: every context contains at most four symbols; four pairwise different symbols contribute six distinct signed directed edges and retain all four symbols in support; repeated-symbol contexts are completely represented by equality patterns on four positions. Relabeling any support and any auxiliary context symbols into a four-element alphabet preserves the signed vector and its support. Enumerating those equality patterns yields the displayed per-support counts. The attached `check_local.py` implements the finite certificate with integer coordinates, checks every specified support for alphabets two through eight, and prints the complete support counts. Consequently
\[
|\mathcal I_q|=1+2\binom q2+14\binom q3+24\binom q4=I_q
\]
for **every** integer \(q\ge2\).

**2. Endpoint separation and exact per-word formula.** For \(n\ge4\), every non-boundary adjacent swap uses one four-letter context, and its change belongs to \(\mathcal I_q\). For any change vector \(z\), define outgoing and incoming sums \(R_u(z)=\sum_vz_{uv}\), \(C_u(z)=\sum_vz_{vu}\). Interior changes have \(R(z)=C(z)=0\), as both endpoints and symbol content of the whole word remain fixed. A first-position swap of unequal symbols has \(R(z)=0\), \(C(z)\ne0\); a last-position swap has \(C(z)=0\), \(R(z)\ne0\). Therefore those two boundary changes are distinct from one another, from zero, and from every interior change. Equal-letter boundary swaps change no profile. Hence the **exact**, every-word formula is
\[
B_q(w)=\left|\{0\}\cup
\{\Delta(w_{i-1},w_i,w_{i+1},w_{i+2}):2\le i\le n-2\}\right|
+\mathbf1_{w_1\ne w_2}+\mathbf1_{w_{n-1}\ne w_n}.
\]
The formula gives the universal upper bound \(I_q+2\) for \(n\ge4\); for \(n\le3\), there are at most three outputs, below that bound.

**3. Attainment over every larger alphabet.** A cyclic de Bruijn word of order four over \(q\) letters has exactly \(q^4\) cyclic four-letter factors, one of each kind. Repeat this word periodically and take a linear window of length \(n\ge q^4+3\). It has every four-letter context, so realizes all of \(\mathcal I_q\) through interior swaps. Of the \(q^4\) possible starting rotations, exactly \(q^3\) have equal first two letters, because every four-letter block appears once; for any specified final index, exactly \(q^3\) rotations have equal last two letters. When \(q\ge3\), \(2q^3<q^4\), so some rotation satisfies **both** boundary inequalities. Its profile ball contains all \(I_q\) interior/baseline changes plus both boundary changes, hence attains \(M_q\).

**4. Binary first attainment.** With two symbols, the nonzero interior changes are the opposite vectors \(\pm(e_{00}+e_{11}-e_{01}-e_{10})\); their four-letter witnesses respectively are `0101` or `1010` and `0011` or `1100`. For every integer \(t\ge1\), the word
\[
w_t=\mathtt{01011}\,\mathtt 0^{\,t}\,\mathtt{01}
\]
has unequal first and last pairs and contains both required four-letter patterns; hence \(B_2(w_t)=5\), at all lengths \(t+7\ge8\). The complete enumeration of \(2^n\) binary words for every \(2\le n\le7\), independently reproduced by `check_global.py`, gives maxima \(2,3,4,4,4,4\), so length eight is first.

**5. Limiting law.** For uniform independent input letters, the probability that any fixed four-letter factor is absent from the disjoint sampled four-letter blocks of a long word is at most \((1-q^{-4})^{\lfloor(n-4)/4\rfloor}\). Taking a union bound over \(q^4\) possible factors shows that all interior changes occur with probability tending to one exponentially fast. Outside that exceptional event, the exact formula reduces to \(I_q\) plus the indicators of unequal letters in the first and last adjacent pairs. These two indicators are independent Bernoulli variables of success probability \((q-1)/q\) for \(n\ge4\). The stated three-point binomial limit follows.

## Verification
The supplied self-contained `check_local.py` computes all signed change vectors and checks support classes separately for each chosen subset of two, three, or four symbols at each alphabet size \(2\le q\le8\). Its recorded results are in `local_output.txt`.

An independently implemented `check_global.py` generates whole profile balls by recomputing ordered-pair histograms of actual swapped words. It exhausts all binary words of lengths two to eight; checks the infinite binary witness formula for lengths eight to thirty-nine; and constructs order-four de Bruijn witnesses for alphabet sizes two through six, checking all four-letter factors and full profile balls. Its recorded output is in `global_output.txt`. The all-alphabet proof rests on the finite-support argument and de Bruijn existence, not on treating finite numerical tests as infinite certificates.

## Relationship to prior work
Kiah, Puleo, and Milenkovic (2015), *Codes for DNA Sequence Profiles*, study full substring-multiplicity observations, their metric, global profile counts, and error-correcting codes. Their Sections 2–3 and 7 do not state a one-adjacent-interchange profile-ball capacity theorem; general coding bounds do not imply the sharp number of distinct swap-induced profiles of one source. Gabrys, Yaakobi, and Milenkovic (2018), *Codes in the Damerau Distance for Deletion and Adjacent Transposition Correction*, analyze the **word-level** edit ball and code redundancy, including the binary count by runs, rather than ordered-pair-profile collisions and this alphabet-general saturation. En Gad (first submitted September 16, 2026), *Polynomially larger deletion codes by linear hashing of substring counts*, motivates the study of linear differences of substring-count vectors for edit channels; its accessible abstract concerns coding redundancy, not an exact adjacent-swap bigram capacity. The latter manuscript's full text could not be inspected, so it remains a priority uncertainty rather than a claimed disjointness based on the abstract.

## Limitations
No exact shortest saturation length is claimed for \(q\ge3\); the de Bruijn length is a constructive sufficient threshold and the elementary lower bound is \(n\ge M_q\). The limiting law assumes independent, uniform input letters and a fixed alphabet size. The theorem does not address longer read lengths, more than one swap, or the size of an optimal correction code. A direct prior equivalence not present in the inspected sources remains possible, especially in material whose full text was inaccessible. No independent scientific validation has been performed.

## References
1. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517v1, first public February 2, 2015. https://arxiv.org/html/1502.00517v1
2. R. Gabrys, E. Yaakobi, O. Milenkovic, *Codes in the Damerau Distance for Deletion and Adjacent Transposition Correction*, IEEE Transactions on Information Theory 64 (2018), 2550–2570, doi:10.1109/TIT.2017.2778143. Full text: https://yaakobi.net.technion.ac.il/files/2020/07/33_Damerau_IT18.pdf
3. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493, first public September 16, 2026. https://arxiv.org/abs/2609.19493
4. N. G. de Bruijn, *A combinatorial problem*, Proc. Koninklijke Nederlandse Akademie van Wetenschappen 49 (1946), 758–764, the classical de Bruijn cycle construction.
