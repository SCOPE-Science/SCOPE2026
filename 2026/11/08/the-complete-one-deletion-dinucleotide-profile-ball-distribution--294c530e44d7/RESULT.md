# The complete one-deletion dinucleotide-profile ball distribution for binary words

## Finding
For a finite binary word \(w=w_1\cdots w_n\) of length \(n\ge2\), write \(p(w)=(c_{00},c_{01},c_{10},c_{11})\), where \(c_{ab}\) counts occurrences of the adjacent pair \(ab\) in the **linear** word. Define the one-deletion profile ball
\[
\mathcal B(w)=\{p(w_1\cdots w_{i-1}w_{i+1}\cdots w_n):1\le i\le n\},
\]
where equal output profiles are counted once, and put \(b(w)=|\mathcal B(w)|\). Let
\[
N_j(n)=|\{w\in\{0,1\}^{n}:b(w)=j\}|,\qquad
G_j(z)=\sum_{n\ge2}N_j(n)z^n.
\]
The full distribution is supported on \(j\in\{1,2,3,4,5,6\}\) and its six rational generating functions \(G_j(z)=P_j(z)/Q_j(z)\) are given below.

For compactness define
\[
\begin{aligned}
A(z)&=z^2-z+1, &B(z)&=z^2+z-1,\\
C(z)&=z^3+z-1, &E(z)&=z^3-z^2+2z-1,\\
H(z)&=(z-1)(z+1)A(z)B(z)C(z)E(z),\\
J(z)&=(2z-1)H(z).
\end{aligned}
\]
The denominators are \(Q_1(z)=z-1\), \(Q_2(z)=B(z)C(z)\), \(Q_3(z)=H(z)\), and \(Q_4(z)=Q_5(z)=Q_6(z)=J(z)\). The numerators are
\[
\begin{aligned}
P_1(z)&=2z^2(z-2),\\
P_2(z)&=-2z^3(2z^4+2z^3+z^2+z-2),\\
P_3(z)&=2z^3(z^{11}-5z^{10}+9z^9-9z^8+8z^7+z^6-5z^4+7z^3-4z^2-z+1),\\
P_4(z)&=-2z^5(3z^{10}-24z^9+48z^8-81z^7+99z^6-67z^5+29z^4-18z^3+20z^2-13z+3),\\
P_5(z)&=-2z^6(z^{10}-9z^9+28z^8-51z^7+86z^6-107z^5+77z^4-29z^3+9z^2-6z+2),\\
P_6(z)&=2z^9(z^7-6z^6+12z^5-20z^4+30z^3-36z^2+24z-6).
\end{aligned}
\]
In particular, six distinct received profiles are attainable for the first time at \(n=9\), for exactly \(N_6(9)=12\) labeled source words. If \(W_n\) is uniformly random on \(\{0,1\}^n\), then
\[
\lim_{n\to\infty}\Pr\bigl(b(W_n)=6\bigr)=\frac18.
\]
The result counts **profiles of distinct deletion descendants**, not the number of distinct deletion descendants themselves.

## Assumptions and scope
All words are linear, indexed, and binary; neither reversal nor complementation is quotiented out. Exactly one symbol is deleted, including either endpoint, and the adjacent-pair profile of the length-\(n-1\) descendant retains pair multiplicities. For a length-one descendant the profile is the zero quadruple. The formulas cover all integers \(n\ge2\); they do not mix the length-one input convention into the generating functions.

## Proof
Let \(e_{ab}\) be the standard coordinate vector indexed by pair \(ab\), and let \(\delta=p(\text{descendant})-p(w)\). An endpoint deletion contributes \(-e_{ab}\), where \(ab\) is the removed end edge. An internal deletion with local triple \(abc\) contributes
\[
\delta=-e_{ab}-e_{bc}+e_{ac}.
\]
For the eight binary triples these reduce to just four vectors:
\[
\begin{array}{c|c}
\text{triple}&\delta\\\hline
000,001,100&-e_{00}\\
011,110,111&-e_{11}\\
010&e_{00}-e_{01}-e_{10}\\
101&e_{11}-e_{01}-e_{10}
\end{array}
\]
The endpoint vectors \(-e_{00}\), \(-e_{11}\) are already listed, whereas \(-e_{01}\) and \(-e_{10}\) add two new possibilities. All six vectors are distinct. Thus \(1\le b(w)\le6\) and \(b(w)\) is the number of present features labeled \(A,B,C,D,E,F\): the first four are triggered by the displayed triple classes, with \(A\) or \(B\) also triggered by an appropriate endpoint pair, while \(E\) and \(F\) are triggered only by endpoint pairs \(01\) and \(10\). Distinct vectors stay distinct after adding the same base profile \(p(w)\).

Here is an exact finite rational expression for the complete distribution. Index the four states by \(00,01,10,11\). For each subset \(T\subseteq\{A,B,C,D,E,F\}\), define a four-by-four matrix \(M_T\) whose entry from \(ab\) to \(bc\) is one exactly if the triple \(abc\) triggers a feature in \(T\), and zero otherwise. Let \(v_T\) be the column vector whose entry at \(ab\) is one exactly if the endpoint pair \(ab\) triggers a feature in \(T\). For any word of length \(n\ge2\), all its deletion-change features belong to \(T\) precisely when its initial and final pairs are accepted by \(v_T\) and its successive triples follow \(M_T\). Hence the number of such words is
\[
f_T(n)=v_T^{\mathsf T} M_T^{\,n-2}v_T.
\]
For a fixed feature set \(S\), the elementary identity
\[
t^{|S|}=\sum_{T\supseteq S}t^{|T|}(1-t)^{6-|T|}
\]
then gives the **exact all-length bivariate generating function**
\[
\boxed{
\sum_{n\ge2}\sum_{j=1}^{6}N_j(n)t^jz^n
=z^2\sum_{T\subseteq\{A,B,C,D,E,F\}}
t^{|T|}(1-t)^{6-|T|}
v_T^{\mathsf T}(I-zM_T)^{-1}v_T.
}
\]
Every inverse exists over formal power series because its matrix has constant term \(I\). Direct algebra of these sixty-four at-most-four-state terms yields exactly the six rational functions displayed in the Finding. The attached `verify_all.py` gives an integer-arithmetic proof certificate for that algebra: each summand has denominator degree at most four and numerator degree at most five. A common denominator of all sixty-four terms therefore has degree at most \(256\), with aggregate numerator degree at most \(257\). The six claimed rational expressions have denominators of degree at most \(13\) and numerators of degree at most \(16\), so every cross-multiplied difference is a polynomial of degree at most \(272\). The verifier independently generates all exact coefficients through degree \(279\), checking agreement with each claimed rational expression; hence every cross-multiplied difference vanishes identically. This is finite polynomial identity verification, not an extrapolation from an unbounded sequence.

The numerator \(P_6(z)\) starts at degree nine and its degree-nine coefficient after division by \(Q_6\) is twelve. Consequently \(N_6(n)=0\) for \(2\le n<9\) and \(N_6(9)=12\).

Finally, for all sufficiently large \(n\), both features \(E,F\) can occur only when the first and last adjacent pairs are the opposite transitions \(01,10\), in either order. For \(n\ge4\), the probability of those two boundary orientations is exactly \(1/8\). Conditional on such endpoints, the internal random bits contain linearly many disjoint triples. Each of \(000,111,010,101\) occurs in a fixed disjoint random triple with probability \(1/8\); the union bound gives conditional failure probability at most \(4(7/8)^{\lfloor(n-4)/3\rfloor}\). Occurrence of those four triples ensures all four internal feature types. The upper bound \(1/8\) and this matching asymptotic lower bound prove the limit.

## Verification
Run `python3 verify_all.py` to regenerate the six rational-function coefficient lists and the feature automaton using integer arithmetic alone. Its algebraic degree certificate proves all six rational identities for arbitrary length by checking coefficients \(0\) through \(279\), a strict margin beyond the degree-\(272\) bound. Run `python3 independent_brute.py` to enumerate literal deletion descendants and their profiles independently for every word of length \(2\) through \(14\). Both programs execute without third-party Python modules; their outputs were checked after extraction from the packaged files.

The first distributions \((N_1(n),\ldots,N_6(n))\) are \((2,10,14,6,0,0)\) for \(n=5\), \((2,60,144,178,116,12)\) for \(n=9\), and \((2,586,2294,5518,6792,1192)\) for \(n=14\). For every \(n\), the six counts sum to \(2^n\). The exact arithmetic and the structural proof apply to all lengths, whereas the direct string enumeration is finite corroboration only.

## Relationship to prior work
Kiah, Puleo and Milenkovic introduced profile-vector coding for noisy DNA-read collections and analyzed synthesis substitutions, sequencing substitutions and incomplete coverage. Their profile-vector definition is the same multiplicity statistic used here, but their source-error model and enumeration questions do not give the distinct profile shadows of every *symbol deletion* or the distribution of their cardinalities. Jacquet, Knessl and Szpankowski studied the total number of Markov-type profiles, a different global enumeration statistic. A published exact binary two-multispectrum result counts the total set of realizable linear pair profiles and the singleton word classes, rather than deletion-induced output profiles from each individual input. A two-read deletion-reconstruction graph result counts pairs of source words with intersecting **word** deletion balls, not the size of a **profile** deletion ball. None of those statements alone determines the six-class laws above.

## Limitations
This is an exact combinatorial result for single source-symbol deletion, linear binary words and adjacent-pair count vectors. It does not establish analogous six-class laws over larger alphabets, for longer \(k\)-gram profiles, cyclic words, multiple deletions, substitution noise, or optimal error-correcting code sizes. The published-source comparison cannot exclude an overlooked equivalent treatment under Markov-type or histogram-channel terminology; independent historical-priority assessment is outstanding.

## References
1. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, first public arXiv version 2015-02-02, arXiv:1502.00517v1, https://arxiv.org/abs/1502.00517.
2. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Transactions on Information Theory 58(7), 4261–4272 (2012), DOI:10.1109/TIT.2012.2191476.
3. *Exact binary two-multispectrum code size and singleton classification*, published published-finding corpus research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71/RESULT.md.
4. *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, published published-finding corpus research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91/RESULT.md.
