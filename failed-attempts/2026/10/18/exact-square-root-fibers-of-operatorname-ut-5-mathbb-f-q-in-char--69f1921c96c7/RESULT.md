# Exact square-root fibers of \(\operatorname{UT}_5(\mathbb F_q)\) in characteristic two

## Finding

Let \(q=2^f\) with \(f\geq1\), let \(G=\operatorname{UT}_5(\mathbb F_q)\), and define \(R(Y)=|\{X\in G:X^2=Y\}|\). Every nonzero fiber has one of exactly five cardinalities. Their **complete spectrum**, with the number of distinct targets at each cardinality, is

| Square-root fiber \(R(Y)\) | Number of targets \(Y\) |
| :-- | --: |
| \(q^3(q-1)\) | \(q^3(q-1)(q^2-1)\) |
| \(q^4(q-1)\) | \(q(q-1)(2q^2+2q-1)\) |
| \(q^4(q^2-1)\) | \(2q(q-1)\) |
| \(3q^5(q-1)\) | \(q-1\) |
| \(q^5(5q-4)\) | \(1\), the identity |

In particular the exact size of the square image is
\[
|G^2|=q^6-q^5+q^4+q^3-q^2,
\]
where \(G^2=\{X^2:X\in G\}\) denotes the **set** of squares. The total square-root mass equals \(q^{10}=|G|\). The last fiber, at the identity, is an instance of the pre-existing zero-square enumeration in triangular matrices; the contribution here is the remaining pointwise distribution and its complete spectrum.

## Assumptions and scope

Write every possible square target uniquely as
\[
Y=I+A E_{13}+B E_{24}+C E_{35}+D E_{14}+E E_{25}+F E_{15},
\]
with \(A,B,C,D,E,F\in\mathbb F_q\). All \(Y\) outside this six-coordinate subgroup have \(R(Y)=0\). Within it, the following disjoint conditions give **every** fiber:

| Target condition | \(R(Y)\) |
| :-- | --: |
| \(B\ne0\) and \((A,C)\ne(0,0)\) | \(q^3(q-1)\) |
| \(B\ne0\), \(A=C=0\), \(BF=DE\) | \(q^4(q-1)\) |
| \(B\ne0\), \(A=C=0\), \(BF\ne DE\) | \(0\) |
| \(B=0\), \(AC\ne0\) | \(0\) |
| \(B=0\), exactly one of \(A,C\) nonzero | \(q^4(q-1)\) |
| \(A=B=C=0\), \(DE\ne0\) | \(q^4(q-1)\) |
| \(A=B=C=0\), exactly one of \(D,E\) nonzero | \(q^4(q^2-1)\) |
| \(A=B=C=D=E=0\), \(F\ne0\) | \(3q^5(q-1)\) |
| \(A=B=C=D=E=F=0\) | \(q^5(5q-4)\) |

The displayed rules make no assumptions about whether \(q\) is prime: all finite fields of characteristic two are included.

## Proof

**Step 1: six equations.** Write \(X=I+N\), with strict upper-triangular entries \(a,b,c,d,e,f,g,h,i,j\) at positions \((12),(23),(34),(45),(13),(24),(35),(14),(25),(15)\), respectively. Since the field has characteristic two, \(X^2=I+N^2\). Ordinary matrix multiplication gives exactly
\[
A=ab,\quad B=bc,\quad C=cd,\quad D=af+ce,\quad E=bg+fd,\quad F=ai+eg+hd.
\]
The tenth coordinate \(j\) is free. When \((a,d)\ne(0,0)\), the last equation is one nonzero linear equation in \((h,i)\), having \(q\) solutions for any prescribed \(F\). Including \(j\) gives a factor \(q^2\).

**Step 2: the branch \(a=d=0\).** In this branch \(A=C=0\), and the other four equations become
\[
\begin{pmatrix}B&E\\D&F\end{pmatrix}
=\begin{pmatrix}b\\e\end{pmatrix}\begin{pmatrix}c&g\end{pmatrix}.
\]
A specified nonzero rank-one matrix has exactly \(q-1\) outer-product representations: scaling the first factor by any unit determines the inverse scaling of the second. A zero matrix has \(2q^2-1\) representations, since at least one entire factor must vanish. Higher-rank matrices have none. The unused variables \(f,h,i,j\) contribute \(q^4\). Thus this branch contributes \(q^4(q-1)\) at every nonzero rank-one matrix, \(q^4(2q^2-1)\) at zero, and zero elsewhere.

**Step 3: the branch \((a,d)\ne(0,0)\).** If \(B\ne0\), then \(b,c\ne0\), and \(a=A/b\), \(d=C/c\). This branch exists exactly when \((A,C)\ne(0,0)\). Choose \(b\) in \(q-1\) ways; then \(c\) is fixed. The two equations for \(D,E\) admit \(q\) choices of \((e,f,g)\), since \(c\ne0\) determines \(e\) and \(b\ne0\) determines \(g\) once \(f\) is chosen. Including the factor from Step 1 gives \(q^3(q-1)\). If \(B=0\) but \(A,C\) are both nonzero, then \(b,c\ne0\), a contradiction. If \(B=0\) and exactly one of \(A,C\) is nonzero, direct elimination first fixes the relevant one of \(a,d\) and one of \(b,c\), leaving \(q^2(q-1)\) assignments among the first seven coordinates and hence \(q^4(q-1)\) with Step 1.

It remains to impose \(A=B=C=0\). In the branch \((a,d)\ne(0,0)\), partition the solutions according to \((b,c)\):

* If \(b\ne0\), then \(c=a=0\), \(d\ne0\), and necessarily \(D=0\). This contributes \(q^4(q-1)^2\), for every prescribed \(E,F\).
* If \(c\ne0\), then \(b=d=0\), \(a\ne0\), and necessarily \(E=0\). This contributes \(q^4(q-1)^2\), for every prescribed \(D,F\).
* If \(b=c=0\), then \(D=af\), \(E=df\). For \((D,E)=(0,0)\), we must have \(f=0\) and may choose any \((a,d)\ne(0,0)\), giving \(q^4(q^2-1)\) solutions. For \((D,E)\ne(0,0)\), choose \(f\ne0\), which fixes \((a,d)\), giving \(q^4(q-1)\) solutions. In both situations \(e,g\) are free and the last equation and \(j\) provide the required factors. All contributions are independent of \(F\).

Adding the disjoint branches from Steps 2 and 3 yields every line in the pointwise table. For instance, when \(A=B=C=D=E=0\) and \(F\ne0\), division by \(q^4\) gives \(2(q-1)^2+(q^2-1)+(q-1)=3q(q-1)\). When also \(F=0\), the last \(q-1\) is replaced by \(2q^2-1\), giving \(q(5q-4)\) after division by \(q^4\).

**Step 4: count targets.** The first fiber type has \((q-1)(q^2-1)q^3\) targets. For the second, sum the disjoint counts \(q^2(q-1)\) (nonzero \(B\) satisfying \(BF=DE\)), \(2q^3(q-1)\) (exactly one of \(A,C\) nonzero), and \(q(q-1)^2\) (\(A=B=C=0\) and \(DE\ne0\)). Their sum is \(q(q-1)(2q^2+2q-1)\). The final three types respectively have \(2q(q-1)\), \(q-1\), and one target. The only zeros inside the six-coordinate subgroup are \(q^2(q-1)^2\) cases with \(B\ne0,A=C=0,BF\ne DE\) and \(q^3(q-1)^2\) cases with \(B=0,AC\ne0\). Subtracting their sum from \(q^6\) proves the square-image polynomial. Summing all fiber sizes with their multiplicities gives \(q^{10}\), independently equal to the number of inputs. This completes the proof.

## Verification

The accompanying standalone `verify_ut5_square_fibers.py` uses finite-field arithmetic and literal multiplication of strict upper-triangular matrices. It exhaustively enumerates all \(q^{10}\) inputs up to a free corner coordinate and all \(q^6\) possible prescribed targets for \(q=2\) and \(q=4\); it compares every fiber, the full spectrum, and total mass. Over \(q=8\), it independently counts nine selected pointwise fibers and checks two thousand sampled matrix squares. Results: `GF 2 EXHAUSTIVE_OK`, `GF 4 EXHAUSTIVE_OK`, `GF 8 POINTWISE_OK`, and `ALL_EXACT_CHECKS_PASSED`. The general theorem is proved above; these finite checks are not a substitute for a proof for all \(f\).

## Relationship to prior work

Dolfi, Singh, and Yadav (2019) establish structural results on power images in finite unitriangular groups; their image data include the two small-field cases \(q=2,4\), and their first nonsurjective characteristic-two dimension is five. Bier (2012) establishes structural width and representability statements. Ekhad and Zeilberger (1995/1996) count triangular square-zero matrices in general; that covers the **identity** square-root fiber here. The novel candidate is limited to the **nonidentity exact prescribed-target fibers and complete five-level distribution** uniformly in characteristic-two field size; neither a previously known small-field image number nor the known identity fiber is asserted to be new. A prior formula outside the examined literature remains possible.

## Limitations

The theorem treats \(5\times5\) unitriangular matrices over characteristic-two finite fields only. No statement is made for odd characteristic or larger matrices. Literature overlap was investigated but not exhaustively certified, and equivalent older triangular-matrix root-counting results could exist. A prior equivalent enumerative statement outside the examined literature could exist.

## References

1. S. Dolfi, A. Singh, and M. K. Yadav, *p-Power conjugacy classes in U(n,q) and T(n,q)*, arXiv:1905.04244, version initially public 2019-05-10; later *Journal of Algebra and Its Applications*, DOI 10.1142/S0219498821501218.
2. A. Bier, *The width of verbal subgroups in the group of unitriangular matrices over a field*, 2012, DOI 10.1142/S0218196712500191.
3. S. Ekhad and D. Zeilberger, *The Number of Solutions of X²=0 in Triangular Matrices Over GF(q)*, first available 1995-12-01; *Electronic Journal of Combinatorics* 3 (1996), R2, DOI 10.37236/1226, arXiv:math/9512224.
4. H. Wu and W. Zhou, *Singular Cholesky Fibers over Finite Fields*, arXiv:2609.00533, concerning a different matrix map but citing triangular square-zero counts.
