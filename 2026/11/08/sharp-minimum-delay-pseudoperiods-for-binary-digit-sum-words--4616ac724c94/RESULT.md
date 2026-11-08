# Sharp minimum-delay pseudoperiods for binary digit-sum words

## Finding

For every integer \(m\ge 2\), consider the infinite word
\[
t_m(n)=s_2(n)\bmod m,\qquad n\ge 0,
\]
where \(s_2(n)\) is the number of ones in the binary representation of \(n\). A **pseudoperiod shift set** is a finite nonempty set \(S\) of positive integers such that
\[
\forall n\ge0\quad \exists d\in S:\quad t_m(n+d)=t_m(n).
\]
The least possible maximum shift is exactly
\[
D_m=2^m-1.
\]
**Among shift sets whose maximum is this least possible value, the minimum cardinality is exactly**
\[
K_m=2m-1.
\]
One simultaneously optimal shift set is
\[
S_m=\{2^j:0\le j<m\}\;\cup\;
\{2^m-2^j:0\le j<m-1\}.
\]
Thus the shortest possible forward horizon is exponential in \(m\), but only \(2m-1\) fixed probes are needed at that horizon. More precisely, every cardinality-optimal shift set at the minimum horizon must contain all the powers \(2^j\) for \(0\le j<m\), must contain \(2^m-1\), and must meet each of the \(m-2\) disjoint upper-half binary-weight classes described in the proof. This last condition is necessary, not asserted sufficient.

## Assumptions and scope

The word is right-infinite and indexed from zero; all arithmetic is on nonnegative integers. The alphabet is the residue ring \(\mathbb Z/m\mathbb Z\). Shift sets are independent of the starting position and contain distinct positive integers. The optimization is **lexicographic**: minimize the maximum shift first and then the number of shifts among those attaining that horizon. No claim is made that \(2m-1\) is the minimum number of shifts without the maximum-delay restriction. The case \(m=2\) agrees with the classical three-shift phenomenon; the uniform sharp support law for arbitrary \(m\) is the result under examination.

## Proof

Write \(w(n)=s_2(n)\) and put \(B=2^m-1\). We prove the horizon lower bound, the validity of \(S_m\), and the matching support lower bound.

**1. The horizon cannot be smaller.** At position \(n=0\), equality requires \(w(d)\equiv0\pmod m\). For \(1\le d<2^m-1\) we have \(1\le w(d)\le m-1\); hence none is admissible. Every pseudoperiod shift set therefore has maximum at least \(B\).

**2. The proposed \(2m-1\) shifts suffice for every position.** Its two displayed families are disjoint (the only potential overlap would be \(2^{m-1}\), omitted from the second family). Thus \(|S_m|=m+(m-1)=2m-1\), and its largest member is \(B\).

Fix an arbitrary \(n\ge0\). If its lowest \(m\) bits are all zero, then adding \(B\) introduces exactly \(m\) ones without carrying, so \(w(n+B)-w(n)=m\) and the required equality holds.

Otherwise suppose, for a contradiction, that no power \(2^j\), \(0\le j<m\), works. If bit \(j\) of \(n\) is one and bit \(j+1\) is zero, then adding \(2^j\) simply changes the adjacent pattern \(10\) (read from low to high bits) to \(01\), preserving \(w\). Hence there is no such adjacent pattern at any \(j<m\). Consequently the low \(m\) bits consist of \(a\) zeros followed by \(m-a\) ones, for some \(0\le a<m\), and bit \(m\) is also one. Equivalently,
\[
n=2^m H+(2^m-2^a),
\]
where \(H\) has \(T\ge1\) trailing one-bits. For every \(a\le j<m\), adding \(2^j\) clears precisely \(m-j+T\) consecutive ones and sets the following zero to one; thus
\[
w(n+2^j)-w(n)=1-(m-j+T).
\]
Since no such shift works, none of the \(m-a\) consecutive integers
\[
T+1,T+2,\ldots,T+m-a
\]
is congruent to \(1\) modulo \(m\). It follows, by checking the omitted residues in a complete block modulo \(m\), that \(r=T\bmod m\) lies in \(\{1,\ldots,a\}\). In particular, the case \(a=0\) cannot occur under the supposition. Set \(j=a-r\); then \(0\le j<a\le m-1\), so \(d=2^m-2^j\) belongs to the second family of \(S_m\). Addition gives the exact identity
\[
n+d=2^m(H+1)+(2^m-2^a-2^j).
\]
The trailing-one carry in \(H\) changes its weight by \(1-T\). The lower \(m\)-bit weight changes from \(m-a\) to \(m-j-1\). Therefore
\[
w(n+d)-w(n)=(1-T)+(m-j-1)-(m-a)=a-j-T=r-T\equiv0\pmod m.
\]
Thus this second-family shift works after all. The construction is uniform in \(n\), proving the infinite pseudoperiod property and attaining horizon \(B\).

**3. At least \(2m-1\) shifts are necessary at horizon \(B\).** For every \(n\), define its exact admissible shift set inside the optimal horizon by
\[
E(n)=\{d\in\{1,\ldots,B\}:w(n+d)\equiv w(n)\pmod m\}.
\]
Any pseudoperiod \(S\subseteq\{1,\ldots,B\}\) must intersect every \(E(n)\). We exhibit \(2m-1\) pairwise disjoint nonempty such sets.

First, \(E(0)=\{B\}\), because \(B\) is the only positive number at most \(B\) with binary weight divisible by \(m\).

For each \(j\in\{0,\ldots,m-1\}\), put
\[
N_j=2^j(2^{m+1}-1).
\]
Then \(E(N_j)=\{2^j\}\). Indeed, write any tested shift as \(d=q2^j+r\), \(0\le r<2^j\). If \(q=0\), the weight change is \(w(r)\in\{1,\ldots,j\}\), not zero modulo \(m\). If \(q\ge1\), the weight change is
\[
w(q-1)+w(r)-m.
\]
Since \(1\le d\le B\), its first two summands have a sum between \(0\) and \(m-1\). Thus divisibility by \(m\) forces \(q=1\) and \(r=0\), exactly the shift \(2^j\).

Finally, for each \(\ell\in\{1,\ldots,m-2\}\), put
\[
N_{\ell}'=(2^{\ell+1}-1)2^{m-1}.
\]
For \(1\le d<2^{m-1}\), the weight change is \(w(d)\in\{1,\ldots,m-1\}\), so the shift fails. For \(d=2^{m-1}+r\), \(0\le r<2^{m-1}\), the high bits pass from \(\ell+1\) ones to a single one; the weight change is \(w(r)-\ell\). Therefore
\[
E(N_{\ell}')=\{2^{m-1}+r:0\le r<2^{m-1},\ w(r)=\ell\}.
\]
These \(m-2\) Hamming-weight classes are nonempty and mutually disjoint. They avoid all powers \(2^j\) (the only upper-half power has \(r=0\)) and also avoid \(B\) (which has \(w(r)=m-1\)). Together with \(E(0)\) and the \(m\) singleton sets \(E(N_j)\), we have \(1+m+(m-2)=2m-1\) disjoint nonempty constraints. Every valid \(S\) must choose a different shift from each, and hence \(|S|\ge2m-1\). Step 2 achieves equality, proving the theorem.

The argument also proves the stated necessary structure of every optimum: it must choose each compulsory singleton shift and one member from each upper-half weight class. The proof makes no claim that choosing arbitrarily from these classes always works.

## Verification

The independent standard-library script `verify.py` recomputes the explicit \(S_m\), checks the horizon obstruction and all \(2m-1\) exact disjoint witness sets for \(2\le m\le10\), exhaustively tests the pseudoperiod property for the first 4,000 starting indices at each of these moduli, and runs seeded tests on 700 further starting indices with up to 180 binary digits per modulus. It reports `VERIFY_OK moduli=9 assertions=79047`. The infinite quantifiers and optimality follow from the proof above, not from these finite tests.

## Relationship to prior work

Meleshko, Ochem, Shallit and Shan introduced the pseudoperiod-shift formalism and studied classical automatic words, including the binary Thue–Morse word, in arXiv:2207.10171 (first posted July 20, 2022). The paper proves three-shift pseudoperiodicity for the classical two-symbol Thue–Morse word and discusses general finite-word decision complexity, but it does not give the present arbitrary-alphabet sharp minimum-delay cardinality theorem.

Zhao and Zhang, *Sums of Digits and the Distribution of Generalized Thue-Morse Sequences* (2017), prove the exact minimum length of a consecutive interval that contains every digit-sum residue; their binary-base formula specializes to \(2^m-1\). This supplies the previously known dense-window benchmark. It does **not** give a fixed set of only \(2m-1\) offsets, nor prove that no smaller offset set works at that horizon. The key new distinction is between bounded gaps for each letter and a single **sparse, position-independent** return-shift set, with sharp support optimality.

## Limitations

The minimal cardinality is established only **subject to attaining the least possible largest shift**. Larger maximum shifts might permit fewer offsets; this theorem does not decide that unrestricted minimum. The mathematical proof is self-contained, but originality is assessed only against the accessible sources and records searched; an unindexed equivalent result is possible. The finite verifier is supporting reproducibility evidence, not an independent audit of the infinite proof.

## References

1. J. Meleshko, P. Ochem, J. Shallit, S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171, first public version July 20, 2022. https://arxiv.org/html/2207.10171v3 (Definition 1, Proposition 2, Sections 3–4).
2. H. Zhao, D. Zhang, *Sums of Digits and the Distribution of Generalized Thue-Morse Sequences*, Journal of Integer Sequences 20 (2017), Article 17.3.3, publicly dated January 7, 2017. https://cs.uwaterloo.ca/journals/JIS/VOL20/Zhao/zhao23.pdf (Theorems 4–5, Corollary 12).
