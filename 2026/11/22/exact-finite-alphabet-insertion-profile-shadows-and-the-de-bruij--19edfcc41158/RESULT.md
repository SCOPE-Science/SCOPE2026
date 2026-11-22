# Exact finite-alphabet insertion-profile shadows and the de Bruijn threshold

## Finding
Fix a labeled alphabet \(\Sigma\) with \(|\Sigma|=q\ge3\). For every nonempty linear word \(w=w_1\cdots w_n\), let \(P(w)\) be the vector of multiplicities of its \(q^2\) ordered contiguous two-letter factors. Let \(I_q(w)\) be the number of *distinct vectors* \(P(v)\) obtained by inserting exactly one symbol from \(\Sigma\) at any of the \(n+1\) gaps of \(w\), endpoints included. These are profile vectors, not insertion words or insertion operations.

Define \(U(w)=|\{a:a\text{ occurs in }w\}|\), \(L(w)=|\{a:aa\text{ occurs in }w\}|\), and \(T(w)=|\{(a,b):a\ne b,\ ab\text{ occurs in }w\}|\); each counts distinct symbols or digrams, not their multiplicities. Then for every \(n\ge1\),
\[
\boxed{I_q(w)=U(w)+(q-1)L(w)+(q-2)T(w)+2(q-1)-\mathbf1_{\{w_1\ne w_n\}}.}
\]

The sharp all-length maximum is
\[
\boxed{\sup_{n\ge1}\max_{w\in\Sigma^n} I_q(w)=M_q=q(q-1)^2+3q-2.}
\]
A word attains this maximum **if and only if** every ordered two-letter word over \(\Sigma\) is a contiguous factor and its first and last letters agree. The shortest maximum words have length exactly \(q^2+1\), and they are precisely the linearizations (with a repeated initial letter at the end) of order-two \(q\)-ary de Bruijn cycles. Consequently the number of labeled shortest maximum words is exactly
\[
\boxed{(q!)^q.}
\]
For a uniformly random length-\(n\) word \(W_n\), and every \(n\ge2\),
\[
0\le \frac1q-\Pr(I_q(W_n)=M_q)\le q^2(1-q^{-2})^{\lfloor n/2\rfloor};
\]
thus the probability of maximum insertion-profile ambiguity tends exponentially to \(1/q\). For example the capacities and shortest attaining lengths are \(M_3=19\) at \(n=10\), \(M_4=46\) at \(n=17\), and \(M_5=93\) at \(n=26\). The binary case recovers an existing result and is not asserted as new.

## Assumptions and scope
The alphabet symbols are labeled, and words are indexed and **linear**; the profile does not include a wraparound pair. An insertion adds one letter without removing or substituting an existing letter. Distinct resulting words with identical ordered-pair multiplicities represent one profile. Empty source words are excluded. No assumption of distinct adjacent letters, symbol balance, or error distribution is imposed. All formulas are exact over integers; the probability statement uses independent uniform source letters and fixed \(q\). The claimed new nonbinary scope is \(q\ge3\); the pointwise formula also holds at \(q=2\), consistently with the earlier binary result.

## Proof
Let \(e_{ab}\) be the basis vector associated with ordered pair \(ab\), where \(a,b\in\Sigma\). If symbol \(x\) is inserted between consecutive letters \(a,b\), the changed pair-profile is
\[
\Delta(a,x,b)=e_{ax}+e_{xb}-e_{ab}.
\]
If \(x=a\) or \(x=b\), this change reduces respectively to \(e_{aa}\) or \(e_{bb}\). Every positive single-loop vector \(e_{aa}\) with \(a\) appearing somewhere in \(w\) can be realized by duplicating one of its occurrences, including at an endpoint; no such vector arises if \(a\) is absent. This gives exactly \(U(w)\) vectors.

For \(x\notin\{a,b\}\), the three coordinates in \(\Delta(a,x,b)\) are distinct and its unique negative coordinate is \(-e_{ab}\). This uniquely determines the existing ordered digram \(ab\); once \(a,b\) are fixed, the remaining positive coordinates determine the inserted letter \(x\). Consequently the changes from all such internal insertions are distinct from each other and from the one-coordinate vectors. Every loop \(aa\) occurring in \(w\) offers \(q-1\) choices for \(x\); every ordered nonloop digram \(ab\) offers \(q-2\) choices. Thus the number of these signed, three-coordinate vectors is exactly \((q-1)L(w)+(q-2)T(w)\).

At the left boundary an insertion contributes the single positive coordinate \(e_{xw_1}\), and at the right boundary it contributes \(e_{w_nx}\). Their loop vectors are already included in \(U(w)\). Excluding loops, the left and right sets each have size \(q-1\). They share a nonloop coordinate exactly when \(w_1\ne w_n\), in which case the unique shared coordinate is \(e_{w_nw_1}\); when the endpoints agree their only shared coordinate is a loop. Hence they contribute precisely \(2(q-1)-\mathbf1_{\{w_1\ne w_n\}}\) additional single-coordinate vectors. Three-coordinate changes cannot coincide with single-coordinate changes. Since each resulting profile equals \(P(w)+\Delta\), equality of resulting profiles is exactly equality of these changes. The pointwise formula follows.

For \(q\ge3\), each of the coefficients of \(U,L,T\) is strictly positive, and
\[
U\le q,\quad L\le q,\quad T\le q(q-1),\quad \mathbf1_{\{w_1\ne w_n\}}\ge0.
\]
Substitution yields \(I_q(w)\le q+q(q-1)+(q-2)q(q-1)+2(q-1)=M_q\). Equality forces all three maxima and matching endpoints. The three maxima jointly are equivalent to the occurrence of all \(q^2\) ordered digrams. Conversely their occurrence and matching endpoints attain the bound, establishing the exact equality characterization.

There are only \(n-1\) contiguous ordered digram positions in a length-\(n\) word. Thus \(n\ge q^2+1\) is necessary. Consider the complete directed graph on the \(q\) symbols, including one loop at each vertex and one directed edge for every ordered pair of different vertices. Every vertex has indegree and outdegree \(q\), so there is an Euler circuit traversing each of its \(q^2\) edges once. Reading consecutive vertices yields a closed length-\(q^2+1\) word containing every ordered pair exactly once and having equal endpoints. Such words are exactly linearizations of order-two de Bruijn cycles, which proves the threshold and existence. Appending repetitions of the initial letter gives a maximum word at every greater length.

For completeness, the classical BEST Euler-tour enumeration combined with the directed matrix-tree count gives \(q^{q-2}((q-1)!)^q\) such de Bruijn cycles up to rotation: the graph without its loops has \(q^{q-2}\) rooted in-arborescences for a prescribed root, and each vertex contributes \((q-1)!\) local edge orders. Because every ordered digram is distinct, each cycle has exactly \(q^2\) distinct indexed starting edges and gives \(q^2\) different closed linear words. Their number is therefore \(q^2q^{q-2}((q-1)!)^q=(q!)^q\). This is the classical de Bruijn count, applied to the new equality characterization; the count of de Bruijn cycles itself is not claimed as new.

For the probability bound, maximality implies \(W_{n,1}=W_{n,n}\); that event has probability \(1/q\). For each fixed digram \(ab\), inspect the \(\lfloor n/2\rfloor\) disjoint two-letter blocks beginning at odd positions. They are independent and equal \(ab\) with probability \(q^{-2}\), so the probability that \(ab\) is absent from the entire word is at most \((1-q^{-2})^{\lfloor n/2\rfloor}\). A union bound over the \(q^2\) digrams, together with the equality characterization, proves the displayed estimate and limit.

## Verification
The standalone `verify_profile.py` enumerates every literal inserted word and calculates its ordered-pair profile from scratch, independently of the pointwise formula, for alphabets \(q=2,3,4,5\) and lengths respectively through \(10,8,5,4\). These comprise \(14{,}030\) shorter input words. The separate complete ternary length-ten census computes *literal* insertion profiles for all \(3^{10}=59{,}049\) candidate words, yielding \(73{,}079\) total direct source-word checks. A second symbolic integer-vector check enumerates the distinct insertion-change types at each tested alphabet size. The script also constructs de Bruijn witness words for \(2\le q\le7\), tests their sharp profile counts and selected longer extensions, and exhaustively counts all ternary length-ten maximum words using literal insertion profiles, obtaining \(216\) as predicted by \((3!)^3\). The recorded `verification_output.txt` shows all tests passed. Run `python3 verify_profile.py` with a standard Python 3 interpreter in the same directory as the script; no external packages or data files are required. Finite enumeration corroborates but does not replace the unrestricted proof above. The classical Euler-tour count is justified by BEST and the matrix-tree theorem; no machine computation is asserted to prove it for every alphabet size.

## Relationship to prior work
Eyal En Gad's 2026 paper on linear hashing of substring counts treats local changes of \(q\)-ary substring-count vectors under bounded edits and establishes asymptotic code-existence bounds. Its local-change machinery motivates the present statistic, but its inspected statements do not classify the entire one-symbol insertion-profile neighborhood at fixed two-gram length, nor give the sharp all-alphabet capacity, onset, or extremizers. Kiah, Puleo, and Milenkovic establish the DNA sequence-profile model, count global observable profile types and study substitution and coverage error models, rather than these exact local single-insertion shadows.

The published *Exact single-insertion dinucleotide-profile ambiguity in binary words* gives the binary four-coordinate pointwise law and complete binary distribution. The binary instance of the present formula agrees with that known result. For \(q\ge3\), however, the term \((q-2)T(w)\) distinguishes all observed **oriented nonloop digrams**, an independent phenomenon absent in the binary alphabet. This yields the all-alphabet sharp capacity and a de Bruijn minimum-length/equality classification not established in that inspected binary treatment. The related published binary one-deletion profile distribution concerns the opposite edit operation, which does not imply the insertion result. The de Bruijn enumeration used to count minimal maximizers is independently classical; its combination with a profile-channel equality condition supplies the contribution here.

## Limitations
This statement concerns only ordered two-gram multiplicities, linear source strings, a single **insertion**, and alphabets of cardinality at least three for the asserted new portion. It is not a theorem about all \(k\)-gram lengths, multiple edits, optimal codebooks, cyclic input profiles, or the distribution of profile-ball sizes away from the maximum. The equivalence to a de Bruijn cycle is proved only for shortest maximal words, not arbitrary longer maximizers. Targeted literature and database comparisons do not exclude an unindexed equivalent under other terminology; independent historical-priority assessment has not been performed.

## References
1. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493, earliest public version 2026-09-16, https://arxiv.org/abs/2609.19493.
2. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517, earliest public version 2015-02-02, https://arxiv.org/abs/1502.00517; author-hosted full text https://www3.ntu.edu.sg/home/hmkiah/docs/papers/DNASeqProfile.pdf.
3. *Exact single-insertion dinucleotide-profile ambiguity in binary words*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-single-insertion-dinucleotide-profile-ambiguity-in-binary--7545727346c0.
4. *The complete one-deletion dinucleotide-profile ball distribution for binary words*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-complete-one-deletion-dinucleotide-profile-ball-distribution--294c530e44d7.
5. N. G. de Bruijn and T. van Aardenne-Ehrenfest, classical enumeration of de Bruijn cycles by Euler tours, with BEST and directed matrix-tree methods; formula and references collected at https://en.wikipedia.org/wiki/De_Bruijn_sequence.
