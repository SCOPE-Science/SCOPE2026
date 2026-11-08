# Exact cyclic one-step image series of elementary cellular automaton Rule 73

## Finding

For every integer \(n\ge 1\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) update an **indexed** binary cyclic ring according to elementary cellular automaton Rule 73, simultaneously at every site. Write \(a_n=|\operatorname{im}F_n|\), counting different indexed output words, not source preimages and not rotation classes. The exact all-length generating function \(A(z)=\sum_{n\ge1}a_nz^n\) is

\[
\boxed{A(z)=-\frac{z}{2}\frac{H'(z)}{H(z)}-2z^2-5z^5,\qquad H(z)=\frac{f_3(z)f_6(z)^2}{f_1(z)^2f_2(z)f_4(z)^2f_5(z)}}.
\]

Here each \(f_i(z)\) is an explicitly given integer polynomial:

\[
\begin{aligned}
f_1(z)&=1-z,\\
f_2(z)&=1-z+z^2,\\
f_3(z)&=1-z^2-z^5,\\
f_4(z)&=1-z^2-z^3-z^5,\\
f_5(z)&=1-z-z^3+z^4-z^5+z^6-z^7,\\
f_6(z)&=1-4z+5z^2-2z^3+z^4-4z^5+9z^6-13z^7\\
&\quad+12z^8-7z^9+z^{10}+4z^{11}-6z^{12}+4z^{13}-2z^{14}.
\end{aligned}
\]

This is an identity of formal power series over the rationals. Its first twelve coefficients are

\[
(a_1,\dots,a_{12})=(2,2,5,12,17,34,79,140,275,544,992,1950).
\]

## Assumptions and scope

All indices are taken modulo \(n\), including \(n=1,2\). The local output is one exactly on input triples `000`, `011`, and `110`, and zero on the remaining five triples. Each of the \(2^n\) input rings is distinct as an indexed configuration, but coincident outputs are counted only once. The series does not count outputs of multiple iterations or orbits under rotation.

## Proof

**1. Exact cyclic output recognizer.** Index the four vertices of the order-two binary de Bruijn graph by \(ab\in\{00,01,10,11\}\). For every input triple \(abc\), draw \(ab\to bc\) with the label equal to the Rule-73 output on \(abc\). Let \(B_0,B_1\) be the associated Boolean \(4\times4\) matrices. An output word \(y_0\cdots y_{n-1}\) occurs on a cyclic ring if and only if the Boolean product \(B_{y_0}\cdots B_{y_{n-1}}\) has a nonzero diagonal entry. Indeed, a closed labeled walk gives the cyclic input bit sequence, and a cyclic input gives such a walk. This is true even for the two shortest rings.

**2. Finite deterministic counting automaton.** Use Boolean relations on the four vertices as deterministic states, start at the identity relation \(I\), and on output label \(b\) replace relation \(R\) by \(R\circ B_b\). Accept precisely when \(R\) has a nonzero diagonal. Breadth-first closure from \(I\) consists of exactly \(735\) distinct relations, \(631\) of which are accepting. Each candidate *output* word labels one deterministic path. With \(T\) the \(735\times735\) nonnegative integer transition-count matrix (row = successor state, column = source state), \(e\) the initial-state column and \(u\) the accepting-state row, it follows that \(a_n=uT^ne\) for \(n\ge1\).

**3. Rational-function certificate.** Let \(Q(z)=\prod_{i=1}^{6}f_i(z)=\sum_{j=0}^{34}q_jz^j\). Its degree is \(34\) and \(q_0=1\). The proposed series on the right-hand side of the boxed identity, called \(b(z)\), satisfies \(Q(z)b(z)\in\mathbb Q[z]\) with degree at most \(39\): logarithmic derivatives have denominator dividing \(Q\), and the two polynomial correction terms increase the numerator degree by at most five. Hence its coefficients obey

\[
\sum_{j=0}^{34}q_j b_{n-j}=0\quad\text{for every }n\ge40.
\]

The supplied independent standard-library program `verify_rule73.py` constructs the relations directly from the local rule and checks, using exact integers, both \(a_n=b_n\) for \(1\le n\le39\) and

\[
\sum_{j=0}^{34}q_j a_{n-j}=0\quad\text{for every }40\le n\le774.
\]

There are exactly \(735\) latter checks. To see why this finite certificate proves an infinite assertion, put \(w=\sum_{j=0}^{34}q_jT^{40-j}e\). The checked recurrence says \(uT^kw=0\) for \(0\le k\le734\). Cayley–Hamilton applied to the actual \(735\times735\) integer matrix \(T\) forces \(uT^kw=0\) for every \(k\ge0\). Thus the actual counts satisfy the recurrence for all \(n\ge40\). Equality through \(n=39\) and the common recurrence imply the boxed formula for every \(n\ge1\).

## Verification

Run `python verify_rule73.py`, which checks the complete finite implication and prints `VERIFY_OK`. The computation constructs the labeled graph and automaton, expands the proposed log-derivative series by formal polynomial division, verifies the first \(39\) terms, then checks the entire \(735\)-term annihilation certificate through \(n=774\). The separate `check_small.py` computes distinct output sets directly from all binary inputs for \(1\le n\le16\) and prints `BRUTE_OK`. Both files use Python's standard library only, and both were executed successfully.

The exhaustive check up to \(n=16\) is a consistency test; the proof for arbitrary lengths uses the actual finite-state dimension and Cayley–Hamilton. The large integer calculations are necessary but reproducible, not a claimed external formal proof.

## Relationship to prior work

Wolfram's 2002 analysis treats Rule 73 as a dynamically complex candidate for structured computation, emphasizing its spatial and temporal behavior. Adamatzky and Martínez (2010) tabulate morphological diversity of finite space-time blocks for elementary rules, including Rule 73; this is a different invariant from distinct one-step images of *all* cyclic source configurations. The Wolfram Atlas identifies Rule 109 as the color-conjugate of Rule 73, and therefore the present image cardinalities apply to Rule 109 as well. Kang (2013) investigates Rule 73 in a long-distance neighborhood model. Fukś (2003) counts iterated preimages of fixed blocks rather than the number of distinct cyclic images. The finite Garden-of-Eden census in the Elementary CA Zoo directly measures this invariant for sampled small ring lengths (including a finite Rule-73 equivalence class), but supplies neither a verified all-length formula nor a symbolic recurrence. Its finite table and this exact series share the same counted objects at the listed ring lengths, and those finitely many data points do not imply this result. These comparisons do not establish historical priority, but none of the inspected accessible treatments gives the stated generating function or a stronger implication that would yield it directly.

## Limitations

The statement concerns only one application of the specified local rule to indexed finite binary rings. It neither classifies all predecessors nor addresses multi-step image sizes, attractor structure, or the complete set of all elementary rules. Independent review of mathematical correctness and historical priority has not been performed. In particular, a potentially relevant Rule-73 study by Kang (2013) could be inspected only to abstract level, not full text; its focus on long-distance updates lowers but does not eliminate a priority risk.

## References

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, first published 2002-05-14, section on the threshold of universality, p. 699; Rule-73 note, p. 885. https://www.wolframscience.com/nks/p699--the-threshold-of-universality-in-cellular-automata/ ; https://www.wolframscience.com/nks/notes-3-2--rule-73/ . Publication date: https://www.wolfram-media.com/products/nks/ .
2. A. Adamatzky and G. J. Martínez, *On generative morphological diversity of elementary cellular automata*, Kybernetes 39 (2010), 72–82, DOI 10.1108/03684921011021282. Accessible author text: https://www.researchgate.net/publication/220626090_On_generative_morphological_diversity_of_elementary_cellular_automata .
3. Wolfram Atlas of Simple Programs, Rule 73, properties and equivalences. https://atlas.wolfram.com/01/01/73/01_01_1_73.html .
4. L. Kang, *Investigation of Rule 73 as Case Study of Class 4 Long-Distance Cellular Automata*, 2013, arXiv:1310.3311 (abstract consulted; full paper not obtained). https://arxiv.org/abs/1310.3311 .
5. H. Fukś, *Sequences of Preimages in Elementary Cellular Automata*, Complex Systems 14 (2003), 29–43. https://wpmedia.wolfram.com/uploads/sites/13/2018/02/14-1-2.pdf .
6. *Gardens of Eden*, Elementary CA Zoo, finite-ring orphan census for 88 elementary-rule equivalence classes, https://cellular.solves.ca/gardens-of-eden (consulted 2026-11-04).
