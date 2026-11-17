# Sharp radius-two identifying codes on three-symbol positions of directed de Bruijn graphs

## Finding
For each integer alphabet size \(q\ge 3\), let \(\vec B(q,3)\) be the directed de Bruijn graph with vertex set \(\mathcal A^3\), \(|\mathcal A|=q\), and arcs \(abc\to bcx\) for every \(x\in\mathcal A\). A *radius-two identifying code* is a subset \(S\subseteq\mathcal A^3\) such that the sets \(B_2^-(v)\cap S\), as \(v\) runs through all vertices, are nonempty and pairwise distinct, where \(B_2^-(v)\) denotes vertices that can reach \(v\) in at most two directed steps.

**Theorem.** For every integer \(q\ge3\),
\[
\gamma^{\mathrm{ID}}_2(\vec B(q,3))=q^2(q-1).
\]
The explicit code
\[
S_q=\{abc\in\mathcal A^3:a\ne c\}
\]
achieves this minimum. In particular, the same simple code that was previously known to identify using radius one at odd word lengths also identifies using radius two at length three, provided \(q\ge3\).

## Assumptions and scope
The vertices are *indexed length-three words*, rather than necklace or rotation equivalence classes. Directed distance is measured **toward** the vertex being identified: \(B_2^-(v)\) is the closed in-ball, not the out-ball. No restriction on loops or repeated letters is imposed. All integer alphabet sizes \(q\ge3\) are included, without primality assumptions. The theorem is not asserted for larger word lengths or larger radii.

The binary exception \(q=2\), whose optimum is seven rather than the baseline four, is a result explicitly recorded in Boutin–Horan Goliber–Pelto's original work and is not claimed as new.

## Proof
**Step 1: necessary size.** Fix a length-two prefix \(ab\). All \(q\) vertices \(abx\), as \(x\in\mathcal A\), have the same set of positive-length predecessors, since those predecessors depend only on the prefix \(ab\). Their closed in-balls can therefore differ only in the two respective centers (a center can also happen to occur among the common predecessors). Thus any two distinct vertices sharing that prefix cannot both be omitted from an identifying code; otherwise their intersections with the code would coincide. Therefore an identifying code includes at least \(q-1\) vertices for each of the \(q^2\) prefixes, giving
\[
|S|\ge q^2(q-1).
\]
This is also the specialization of the established general lower bound of Boutin, Horan Goliber and Pelto (Theorem 3.8).

**Step 2: decomposition of identifying sets.** Let \(S=S_q\) and write the vertex to identify as \(abc\). Its in-ball consists precisely of the vertex itself, its one-step predecessors \(xab\), and its two-step predecessors \(xya\), with \(x,y\in\mathcal A\). Intersecting with \(S\) yields
\[
I(abc)=R_a\cup M_{a,b}\cup E_{a,b,c},
\]
where
\[
R_a=\{xya:x\ne a,\ y\in\mathcal A\},\qquad
M_{a,b}=\{xab:x\ne b\},
\]
and \(E_{a,b,c}=\{abc\}\) if \(a\ne c\), while \(E_{a,b,c}=\varnothing\) if \(a=c\). These are sets; any overlap is understood as a union without multiplicity.

**Step 3: recover the first symbol.** Every vertex of \(R_a\) ends in \(a\), and \(|R_a|=q(q-1)\). For each different final letter \(z\ne a\), at most \(q-1\) members of \(M_{a,b}\) and at most one member of \(E_{a,b,c}\) can end in \(z\). Thus the final-letter class \(a\) contains at least \(q(q-1)\) elements of \(I(abc)\), while each other final-letter class contains at most \(q\). Since \(q(q-1)>q\) for \(q\ge3\), \(a\) is uniquely recoverable from \(I(abc)\) as its most populous final-letter class.

**Step 4: recover the middle symbol.** With \(a\) known, subtract the known set \(R_a\). If \(b=a\), then \(M_{a,b}\subseteq R_a\), and the remainder contains at most the singleton \(E_{a,b,c}\). If \(b\ne a\), then all \(q-1\ge2\) elements of \(M_{a,b}\) end in \(b\ne a\) and lie outside \(R_a\). A possible singleton \(E_{a,b,c}\) can add at most one element in any other final-letter class. Consequently, \(b=a\) is detected by the absence of a final-letter class of size at least two in \(I(abc)\setminus R_a\); otherwise, \(b\) is its unique class with at least two members. Hence \(b\) is uniquely recoverable.

**Step 5: recover the final symbol.** Having determined \(a,b\), subtract \(R_a\cup M_{a,b}\). If \(c=a\), the remainder is empty. If \(c\ne a\), the vertex \(abc\) is outside \(R_a\), because it ends in \(c\ne a\). It is also outside \(M_{a,b}\): membership would require \(abc=xab\), forcing \(b=a\) from the second position and \(c=b=a\) from the last, contrary to \(c\ne a\). Therefore the remainder is exactly \(\{abc\}\), which determines \(c\). The entire word \(abc\) is recovered uniquely from the identifying set.

Finally, \(R_a\) has \(q(q-1)>0\) vertices, so no identifying set is empty. Thus \(S_q\) is a radius-two identifying code. Its cardinality is exactly \(q^2(q-1)\), attaining Step 1's bound and proving the theorem. \(\square\)

## Verification
The proof above is valid for every integer \(q\ge3\) and does not rely on finite enumeration. The accompanying `verify.py` computes closed in-balls by reverse breadth-first expansion, checks the displayed set decomposition, and tests all distinct identifying signatures for \(3\le q\le8\). It separately checks the known binary exception exhaustively. The C++17 program `crosscheck.cpp` independently builds closed in-balls from the reverse-arc formula and confirms the code size and pairwise distinct signatures for the same six alphabet sizes.

Execute `sh run_checks.sh` from the extracted directory using Python 3 and a C++17 compiler. Expected final lines are `VERIFY_OK` and `CROSSCHECK_OK`. The tests provide independent finite cross-checks; the five-step symbolic argument is the infinite proof.

## Relationship to prior work
Boutin, Horan Goliber and Pelto (arXiv:1412.5842, first public 18 December 2014) established the universal bound \(q^{n-1}(q-1)\) for radius-\(t\) identifying codes on directed de Bruijn graphs. Their Theorems 3.9 and 3.10 construct radius-two optima only in ranges excluding \(n=3\); their Theorem 3.14 proves that the same endpoint-inequality code is radius-one identifying at odd lengths, including \(n=3\). Their Figure 2 and adjoining text already handle the binary radius-two exception with seven vertices. They also provide a possibly nonoptimal construction in the different critical regime \(n=2t-1\ge5\).

The present theorem establishes the missing **radius-two**, length-three sufficiency and sharpness of the endpoint-inequality set for **every alphabet size at least three**. Radius-one identification does not formally imply radius-two identification, since enlarging neighborhoods can cause identifying sets to coincide. The novelty asserted is not the code set itself or the lower bound, but the second-radius separation property and complete nonbinary boundary optimum. A search cannot rule out all obscure subsequent treatments; independent priority review has not been performed.

## Limitations
The construction applies to \(n=3,t=2,q\ge3\), not to larger radii or all values of \(n=2t-1\). The binary exception and the radius-one endpoint-inequality construction are prior work. The result is a mathematical proof, but no independent scientific audit or exhaustive historical priority certification has been performed. Verification programs use finite alphabet sizes only and do not substitute for the symbolic proof.

## References
1. D. Boutin, V. Horan Goliber and M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842, first submitted 18 December 2014; especially Definition 3.7, Theorems 3.8, 3.9, 3.10, 3.14, and Figure 2. https://arxiv.org/abs/1412.5842
2. 2020 Mathematics Subject Classification, section 68R10, *Graph theory in computer science*. https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=68R10
