# Five \(3\)-adic isometries and singleton residue fibres for Narayana numbers

## Finding
Let \(a_0=0\), \(a_1=a_2=1\), and \(a_{n+3}=a_{n+2}+a_n\) for every integer \(n\ge0\). For any two distinct nonnegative integers \(s,t\) and every \(r\in\{1,4,5,6,7\}\),
\[
\nu_3\bigl(a_{8t+r}-a_{8s+r}\bigr)=1+\nu_3(t-s).
\]
Here \(\nu_3(m)\) is the exponent of three in a nonzero integer \(m\). Thus each of the five index progressions gives a scaled \(3\)-adic isometry, and, for every integer \(k\ge1\), the map
\[
t\longmapsto a_{8t+r}\pmod{3^k},\qquad 0\le t<3^{k-1},
\]
is a bijection onto the full set of residues congruent to \(a_r\pmod3\).

The least positive period of the complete sequence modulo \(3^k\) is \(8\cdot3^{k-1}\). In one such least period, every residue modulo \(3^k\) occurs; every residue congruent to \(2\pmod3\) occurs **exactly once**, and every residue congruent to \(0\) or \(1\pmod3\) occurs **at least twice**. Consequently every integer residue modulo every power of three occurs infinitely often among the Narayana numbers.

## Assumptions and scope
The sequence is the third-order Narayana recurrence with index-zero normalization \((0,1,1)\), rather than the convention beginning \((1,1,1)\); these are index shifts of the same positive sequence. The claims are for every positive power \(3^k\), every \(r\) in the stated five-element set, and all distinct \(s,t\ge0\). Zero differences are excluded from the valuation equation. The assertion of unique fibres refers only to residues congruent to \(2\pmod3\) and to a **least** modular period, not to all integer indices at once.

## Proof
Define \(v=(0,1,1)^{\mathsf T}\), \(e=(1,0,0)^{\mathsf T}\), and the integer matrix
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&0&1\end{pmatrix}.
\]
The recurrence gives \(a_n=e^{\mathsf T}M^nv\) for every \(n\ge0\). Direct integer multiplication yields
\[
M^8=\begin{pmatrix}4&3&6\\6&4&9\\9&6&13\end{pmatrix}=I+3B,
\qquad B=\begin{pmatrix}1&1&2\\2&1&3\\3&2&4\end{pmatrix}.
\]
Put \(T=M^8\). The elementary binomial theorem, inductively applied to a matrix congruent to the identity modulo three, gives for all integers \(j\ge0\) and \(u\ge1\) with \(3\nmid u\),
\[
T^{3^ju}\equiv I+u3^{j+1}B\pmod{3^{j+2}}.
\tag{1}
\]
For completeness, at \(j=0\) the nonconstant terms of order at least two in \((I+3B)^u\) are multiples of nine. If the statement for the exponent \(3^j\) is known, cubing the congruence at the next power preserves the leading matrix \(3^{j+2}B\) modulo \(3^{j+3}\); applying a power \(u\) coprime to three preserves the displayed leading factor. No commutativity assumptions between distinct matrices are needed because only powers of a single matrix occur.

The eight exact coefficients \(c_r=e^{\mathsf T}M^rBv\) for \(0\le r<8\) are
\[
(c_0,c_1,\ldots,c_7)=(3,4,6,9,13,19,28,41).
\]
In particular \(c_r\not\equiv0\pmod3\) precisely for \(r\in\{1,4,5,6,7\}\). For \(t>s\ge0\), write \(t-s=3^ju\) with \(3\nmid u\). From (1), using \(T^s\equiv I\pmod3\),
\[
\begin{aligned}
a_{8t+r}-a_{8s+r}
&=e^{\mathsf T}M^rT^s(T^{t-s}-I)v\\
&\equiv u3^{j+1}c_r\pmod{3^{j+2}}.
\end{aligned}
\]
The right-hand coefficient is a unit modulo three for the five listed values of \(r\), proving the exact valuation formula. Swapping \(t\) and \(s\) handles the other order.

For \(k\ge1\), the formula implies that two indices \(t,s\) yield the same residue modulo \(3^k\) in one such branch if and only if \(t\equiv s\pmod{3^{k-1}}\). Every branch is constant modulo three, since \(T\equiv I\pmod3\). It therefore takes exactly \(3^{k-1}\) different values, the size of a complete residue class modulo three within \(\mathbb Z/3^k\mathbb Z\), and so bijects onto that class. In particular the branches \(r=1,4,5\), with initial values congruent to \(1,2,0\pmod3\), respectively, cover all residue classes.

Equation (1) with \(u=1\) also shows \(M^{8\cdot3^{k-1}}\equiv I\pmod{3^k}\), giving the asserted period as an upper bound. Modulo three, the repeating eight-term word is \((0,1,1,1,2,0,1,0)\), whose least period is eight (no proper divisor of eight is a period). Hence any period modulo \(3^k\) must equal \(8d\) for some positive integer \(d\). Periodicity of the scalar sequence implies \(a_{1+8d}\equiv a_1\pmod{3^k}\); the valuation formula forces \(3^{k-1}\mid d\), so the least period is exactly \(8\cdot3^{k-1}\).

Among the eight index classes modulo eight, the residues of \(a_r\) modulo three are
\[
(0,1,1,1,2,0,1,0).
\]
Only \(r=4\) can yield the residue class \(2\pmod3\). In a least period its branch contains exactly one representative of every such residue, proving exact singleton fibres. The two isometric branches \(r=5,7\) cover each residue \(0\pmod3\) at least twice, and \(r=1,6\) do likewise for \(1\pmod3\). Finally the sequence repeats modulo \(3^k\) with its proved period, so every attained residue occurs infinitely often.

## Verification
The standalone pure-Python program `check_narayana.py` checks the two matrix identities, all eight values of \(c_r\), and the matrix lifting congruence (1) at levels \(0\le j\le9\). Independently generating the scalar recurrence, it checks all residues, the least orbit period, the five complete branch images, and singleton and lower-bound fibre counts for every \(1\le k\le8\). The eight complete periods contain \(26{,}240\) terms in total. Further exact-integer pair checks verify \(7{,}425\) distinct index pairs. These finite checks are diagnostics; the preceding matrix proof establishes the statements for all \(k,s,t\).

To reproduce, run `python3 check_narayana.py` with a standard Python 3 interpreter; no third-party libraries or input files are required.

## Relationship to prior work
Guadalupe (2021, arXiv:2112.06187) determines \(\nu_3(a_n)\) and proves particular prime-power index congruences, including the base-three period at the first levels. Ismail, Rihane and Anwar (2022, arXiv:2206.09174) determine \(\nu_3(a_n-1)\) and \(\nu_3(a_n+1)\). These are point-to-fixed-residue valuation laws; the present claim instead compares arbitrary pairs within five index branches, establishes full residue-class bijections at every prime power, and proves the exact singleton-fibre contrast. It does not claim the underlying recurrence, the modular period at small moduli, or those earlier valuation formulas as new.

Lang and Lang (2013, arXiv:1307.7463) establish residue-completeness statements for *second-order* Pell-type recurrences; their family does not contain this third-order Narayana recurrence. Kirthi (2015, arXiv:1509.05745) studies periods and correlations of Narayana numbers modulo *primes*, but available abstract-level evidence does not settle whether some broader congruence results appear in its full text. OEIS A271953 records finite Narayana periods and general least-period computations without this five-branch residue classification. Related residue-spectrum methods for other third-order recurrences do not imply a Narayana statement without the matrix calculation above.

## Limitations
No complete count formula is asserted for the varying multiplicities of residues congruent to \(0\) or \(1\pmod3\); the stated lower bound two is all that is proved for those classes. The theorem does not classify Narayana residues modulo prime powers other than three, and it makes no claim about decimal-digit pseudorandomness. The known valuation formulas and general lifting techniques make implicit prior coverage a genuine priority risk, especially where inaccessible older full texts may contain stronger modular results. Novelty is limited to the specific isometry/fibre theorem, as far as the inspected sources establish.

## References
1. R. Guadalupe, *On the 3-adic valuation of the Narayana numbers*, arXiv:2112.06187, first public version 12 December 2021, https://arxiv.org/abs/2112.06187.
2. M. Ismail, S. Rihane and M. Anwar, *Narayana Sequence and The Brocard-Ramanujan Equation*, arXiv:2206.09174, first public version 18 June 2022, https://arxiv.org/abs/2206.09174.
3. C. L. Lang and M. L. Lang, *Three term recurrence and residue completeness*, arXiv:1307.7463 (2013), https://arxiv.org/abs/1307.7463.
4. K. Kirthi, *Narayana Sequences for Cryptographic Applications*, arXiv:1509.05745 (2015), https://arxiv.org/abs/1509.05745.
5. OEIS A271953, *Period of the Narayana sequence modulo \(n\)*, https://oeis.org/A271953.
