# Complete parity–ternary residue profiles of the six critical Klarner affine orbit sets

## Finding

Let \(\mathcal K\) be the six ordered coefficient triples
\[
\mathcal K=\{(0,3,10),(0,2,3),(2,0,15),(1,0,2),(2,1,0),(1,6,0)\}.
\]
For \(\tau=(a,b,c)\in\mathcal K\), let \(S_\tau\subseteq\mathbb Z_{\ge0}\) be the smallest set containing \(0\) and closed under
\[
A(x)=2x+a,\qquad B(x)=3x+b,\qquad C(x)=6x+c.
\]
For every integer \(k\ge1\), write \(m_k=2\cdot3^k\), and let \(R_\tau(k)=S_\tau\bmod m_k\). The six exact residue images fall into three cardinality classes:

| Coefficients \(\tau\) | Exact cardinality \(|R_\tau(k)|\) | Fraction of \(m_k\) as \(k\to\infty\) |
| --- | --- | --- |
| \((0,3,10)\), \((2,1,0)\) | \(4\cdot3^{k-1}\) | \(2/3\) |
| \((0,2,3)\), \((1,0,2)\) | \((3^{k+1}+1)/2\) | \(3/4\) |
| \((2,0,15)\), \((1,6,0)\) | \(3\) if \(k=1\); \(8\cdot3^{k-2}\) if \(k\ge2\) | \(4/9\) |

More precisely, for residues \(0\le r<m_k\):

1. For \(\tau=(0,3,10)\), exactly the even \(r\) and the odd \(r\equiv3\pmod6\) occur. For \(\tau=(2,1,0)\), exactly the even \(r\) and the odd \(r\equiv1\pmod6\) occur.
2. For \(\tau=(0,2,3)\), every even \(r\) occurs; an odd \(r\) occurs precisely when either \(r=m_k-1\), or, with \(t=\nu_3(r+1)<k\), one has \((r+1)/(2\cdot3^t)\equiv2\pmod3\). For \(\tau=(1,0,2)\), every odd \(r\) occurs; an even \(r\) occurs precisely when either \(r=0\), or, with \(t=\nu_3(r)<k\), one has \(r/(2\cdot3^t)\equiv1\pmod3\).
3. For \(\tau=(2,0,15)\), the even residues are precisely \(r\equiv0,2\pmod6\). The odd residues are \(r\equiv3\pmod6\) when \(k=1\), and precisely \(r\equiv9,15\pmod{18}\) when \(k\ge2\). For \(\tau=(1,6,0)\), the odd residues are precisely \(r\equiv0,1\pmod3\); the even residues are \(r\equiv0\pmod6\) when \(k=1\), and precisely \(r\equiv0,6\pmod{18}\) when \(k\ge2\).

In particular, the \(4/9\) and \(2/3\) profiles distinguish two other naturally occurring critical free affine-semigroup triples from the previously studied \(3/4\) profile. These are finite-modulus image densities; none is asserted to equal the natural density of its infinite orbit set.

## Assumptions and scope

All maps act on nonnegative integers, and the initial seed is \(0\). Composition may use any finite word, including the empty word. The modulus is exactly \(2\cdot3^k\) with \(k\ge1\). The pairs of indices in the table denote two distinct coefficient triples, not an unproved conjugacy of pointed orbit sets. Each count is for distinct residues, not the number of representing words.

Write \(\nu_3(n)\) for the largest \(t\ge0\) for which \(3^t\mid n\), when \(n>0\). For an orbit image \(S\bmod q\), we use closure under the induced maps on \(\mathbb Z/q\mathbb Z\), which equals the reduction of the integer orbit, since each finite reachable state is represented by a finite word.

## Proof

**Primitive-unit lemma.** For every \(k\ge1\), the integer \(2\) has multiplicative order \(2\cdot3^{k-1}\pmod{3^k}\). Indeed, the lifting-the-exponent identity \(\nu_3(2^{2\cdot3^j}-1)=j+1\) gives the order inductively, starting from order \(2\pmod3\). Thus powers of \(2\) traverse all units of \(\mathbb Z/3^k\mathbb Z\).

**Ternary projections.** The images of the six orbit sets modulo \(3^k\) are, in the displayed order of \(\mathcal K\):
\[
\mathbb Z/3^k\mathbb Z,\quad\mathbb Z/3^k\mathbb Z,\quad
\{x:x\not\equiv1\pmod3\},\quad\mathbb Z/3^k\mathbb Z,\quad
\mathbb Z/3^k\mathbb Z,\quad\{x:x\not\equiv2\pmod3\}.
\]
To verify the full images, use the primitive-unit lemma: for \((0,3,10)\), \(A^j(C(0))=10\cdot2^j\) supplies every unit and \(B(x)=3(x+1)\) supplies all multiples of \(3\) inductively. For \((0,2,3)\), \(A^j(B(0))=2^{j+1}\) supplies units and \(C(x)=3(2x+1)\) supplies all multiples of \(3\). For \((1,0,2)\), \(A^j(0)=2^j-1\) supplies all classes except those congruent to \(2\pmod3\), while \(C(x)=3(2x)+2\) supplies the excluded class by induction. For \((2,1,0)\), \(A^j(0)=2^{j+1}-2\) supplies classes not congruent to \(1\pmod3\), while \(B(x)=3x+1\) supplies that class by induction. All four inductions start at \(k=1\). For \((2,0,15)\), the same primitive orbit \(2^{j+1}-2\) fills exactly the classes \(0,2\pmod3\), while the other two maps land in \(0\pmod3\); hence no further class occurs. For \((1,6,0)\), the primitive orbit \(2^j-1\) fills exactly the classes \(0,1\pmod3\), while the other two maps land in \(0\pmod3\).

**The first pair.** When \(\tau=(0,3,10)\), the maps \(A,C\) always produce even numbers; an odd output from \(B\) has even input, hence is \(3(2y)+3\equiv3\pmod6\). Ternary surjectivity makes \(A(S_\tau)\) all even classes modulo \(m_k\), and then \(B\) applied to those even classes makes every odd class \(3\pmod6\). For \(\tau=(2,1,0)\), the same argument, using \(A,C\) even and \(B(2y)=6y+1\), yields all even classes and exactly the odd classes \(1\pmod6\). Each has \(3^k+3^{k-1}=4\cdot3^{k-1}\) classes.

**The middle pair.** With \(\tau=(0,2,3)\), both \(A\) and \(B\) preserve or reset even parity, and \(C\) makes an odd number. Therefore every odd orbit element has a last occurrence of \(C\), followed by some number \(t\ge0\) of applications of \(B\), so it is of the form \(B^t(C(x))\). One calculates
\[
B^t(C(x))+1=2\cdot3^t(3x+2).
\]
For \(t<k\), the full ternary projection of \(S_\tau\) yields exactly the asserted odd \(3\)-adic shell; for \(t\ge k\), the single class \(-1\pmod{m_k}\) occurs. All even classes occur through \(A\). With \(\tau=(1,0,2)\), \(A\) generates all odd classes by ternary surjectivity, and every even orbit element other than the initial \(0\) has a last \(C\) followed only by \(B\). Here
\[
B^t(C(x))=2\cdot3^t(3x+1),
\]
which supplies exactly the stated even shells and the class \(0\pmod{m_k}\). In each case there are \(3^k\) unrestricted-parity classes, and \(1+\sum_{t=0}^{k-1}3^{k-t-1}=(3^k+1)/2\) further classes.

**The final pair.** For \(\tau=(2,0,15)\), every even orbit element is congruent to \(0\) or \(2\pmod6\), and \(A(x)=2(x+1)\) maps the full allowed ternary projection onto all such even classes. An odd orbit element has a last \(C\), followed only by \(B(x)=3x\), and
\[
C(x)=3(2x+5).
\]
Because \(x\equiv0,2\pmod3\), its possible odd outputs modulo \(18\) are \(15,9\) respectively. All their lifts occur by varying \(x\) across its allowed ternary classes; subsequent \(B\)-iterations remain in the same two classes modulo \(18\). At level \(k=1\) these merge to \(3\pmod6\). For \(\tau=(1,6,0)\), \(A(x)=2x+1\) maps the allowed ternary projection onto precisely all odd classes \(0,1\pmod3\). Every even orbit element other than \(0\) has a last \(C(x)=6x\), followed by applications of \(B(x)=3x+6\). Thus its even classes modulo \(18\) are precisely \(0,6\); all lifts occur through \(C\), and \(B\) preserves their union. At \(k=1\) only the even class \(0\pmod6\) remains. For \(k\ge2\), each case has \(2\cdot3^{k-1}\) classes of one parity plus \(2\cdot3^{k-2}\) of the other parity, giving \(8\cdot3^{k-2}\). At \(k=1\), both have three classes. This proves every asserted image and count.

## Verification

The standalone Python 3 file `check_orbits.py` independently computes the closure of the six affine maps by breadth-first search on the finite ring \(\mathbb Z/(2\cdot3^k)\mathbb Z\), compares it with the exact residue predicates above, and verifies all cardinality formulas for all six triples and \(1\le k\le9\). Run `python3 check_orbits.py`. It reports 54 complete set equalities, including the boundary levels \(k=1,2\). These finite tests detect transcription and boundary errors; they are not the proof for arbitrary \(k\), which is the argument above.

## Relationship to prior work

Shamazov and Talambutsa, *On orbit sets generated by semigroups of one-dimensional affine functions* (arXiv:2507.06875, first posted July 9, 2025), Section 4, explicitly lists precisely the six triples and addresses freeness and ordinary counting-density questions, not these complete residue images. The present calculation answers a different local finite-quotient question. Lagarias's 2016 exposition and Klarner's earlier work supply the classical setting. Existing exact modular work for the single triple \((0,2,3)\) already covers that row's image and its \(3/4\) limit; those facts are included here solely to present the complete six-tuple picture. The substantive new comparisons are the remaining five tuples, especially the new \(2/3\) and \(4/9\) local-density branches.

## Limitations

No statement about the natural density of the orbit sets as subsets of nonnegative integers follows from a limiting fraction of reachable congruence classes. The result concerns only moduli \(2\cdot3^k\); it does not assert a corresponding formula for arbitrary moduli, nor quantify the number of words realizing a residue. Priority uncertainty remains because relevant early work on the six semigroups and comprehensive tables may contain an implicit equivalent computation that was not accessible in full.

## References

- K. F. Shamazov and A. L. Talambutsa, *On orbit sets generated by semigroups of one-dimensional affine functions*, arXiv:2507.06875v1, July 9, 2025; later *Expositiones Mathematicae* **44** (2026), 125765. https://arxiv.org/abs/2507.06875
- J. C. Lagarias, *Erdős, Klarner, and the 3x + 1 Problem*, *American Mathematical Monthly* **123** (2016), 753–776. https://doi.org/10.4169/amer.math.monthly.123.08.753
- D. A. Klarner, *A Sufficient Condition for Certain Semigroups to Be Free*, *Journal of Algebra* (1982). https://doi.org/10.1016/0021-8693(82)90010-2
- D. A. Klarner and R. Rado, *Arithmetic properties of certain recursively defined sets*, *Pacific Journal of Mathematics* **53** (1974), 445–463. https://msp.org/pjm/1974/53-2/pjm-v53-n2-p13-p.pdf
