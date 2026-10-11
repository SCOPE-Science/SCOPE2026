# Tight orthogonal arrays exclude nonbinary dimension-four length-maximal codes at defect \(q-1\)
## Finding

For every integer alphabet size \(q\ge 2\), a \(q\)-ary length-maximal code of dimension \(4\) and Singleton defect \(q-1\) exists if and only if \(q=2\). Equivalently, for every \(q\ge 3\) there is no \((q^2+q+2,q^4,q^2)_q\) code attaining the maximal-arc-type length bound, whereas the binary \([8,4,4]_2\) extended Hamming code attains the bound at \(q=2\).

## Assumptions and scope

A \(q\)-ary code here is an arbitrary code over an alphabet of integer size \(q\ge 2\); linearity and a field structure are not assumed. Following Alderson, an \((n,q^k,d)_q\) code has Singleton defect
\[
s=n-k+1-d,
\]
and is length-maximal when
\[
n=(s+1)(q+1)+k-2.
\]
The claim concerns exactly \(k=4\) and \(s=q-1\).

## Proof

Assume first that a length-maximal code \(C\) exists with \(k=4\) and \(s=q-1\). Its parameters are forced:
\[
n=q(q+1)+2=q^2+q+2,\qquad
d=n-4+1-(q-1)=q^2,\qquad
|C|=q^4.
\]

Alderson proves that a length-maximal code is symbol-uniform and that every code of dimension at least \(2\) obtained from it by successive shortening remains symbol-uniform. Apply this to any three distinct coordinates \(i,j,\ell\). Fix arbitrary alphabet symbols \(a,b,c\). Symbol-uniformity leaves exactly \(q^3\) codewords with coordinate \(i\) equal to \(a\). After shortening at \(i\), symbol-uniformity leaves exactly \(q^2\) with coordinate \(j\) equal to \(b\). After shortening again at \(j\), symbol-uniformity leaves exactly \(q\) with coordinate \(\ell\) equal to \(c\). Thus every triple of symbols occurs exactly \(q\) times in every choice of three columns. Hence \(C\) is an orthogonal array
\[
\operatorname{OA}(q^4,q^2+q+2,q,3).
\]

For strength \(3\), Rao's bound is
\[
N\ge 1+n(q-1)+(n-1)(q-1)^2.
\]
Substituting \(n=q^2+q+2\) gives
\[
1+(q^2+q+2)(q-1)+(q^2+q+1)(q-1)^2=q^4=N,
\]
so this orthogonal array attains Rao's bound.

Noda's classification of strength-\(3\) orthogonal arrays attaining Rao's bound says that every such array is of one of two types:
\[
\operatorname{OA}(2n,n,2,3),\quad n\equiv 0\pmod 4,
\]
or
\[
\operatorname{OA}(q^3,q+2,q,3),\quad q\ \text{even}.
\]
For \(q\ge 3\), the first type is impossible because its alphabet is binary. The second type is also impossible for our parameters because it would require \(q^4=q^3\), hence \(q=1\). Therefore no such length-maximal code exists for any \(q\ge 3\).

For \(q=2\), the binary \([8,4,4]_2\) extended Hamming code has Singleton defect
\[
8-4+1-4=1=q-1
\]
and length
\[
8=(1+1)(2+1)+4-2,
\]
so it is length-maximal. This proves the if-and-only-if statement.

## Verification

The accompanying `artifacts/verify.py` constructs the binary witness as the affine-function code \(\operatorname{RM}_2(1,3)\), checks that it has \(16\) distinct words, minimum distance \(4\), Singleton defect \(1\), and the required length-maximal equality. It also checks that every three-coordinate projection contains each binary triple exactly twice, and numerically checks the displayed Rao equality for a broad integer range as a consistency test.

The all-\(q\) nonexistence is not inferred from finite computation: it follows from the algebraic Rao equality together with Noda's classification theorem.

## Relationship to prior work

Alderson's 2026 work establishes the maximal-arc-type length bound for arbitrary nonlinear codes and the symbol-uniformity of every successive shortening in the equality case. In dimension \(4\), it leaves two non-MDS defect regimes; for \(s=q-1\) it derives the necessary condition \((q+2)\mid 36\), leaving six alphabet sizes at the parameter level. The argument above uses the resulting strength-\(3\) orthogonal-array structure together with Noda's 1986 classification of tight strength-\(3\) arrays to eliminate every nonbinary case at once.

The contribution is the coding-theoretic consequence for the full dimension-\(4\), defect-\(q-1\) length-maximal branch. Noda's theorem itself is classical, and Alderson's length-maximal structure theorem is taken as prior work.

## Limitations

This result does not address the other surviving dimension-\(4\) non-MDS regime \(s=q-2\), nor does it classify codes away from exact length maximality. The originality assessment is necessarily literature-dependent; searches under length-maximal, \(A^s\)MDS, tight orthogonal-array, Rao-bound, and exact-parameter formulations found no source stating this coding corollary, but an equivalent observation under different terminology could exist.

## References

1. Tim Alderson, *Length-Maximal Codes with Given Singleton Defect: Structure and Bounds*, arXiv:2604.03784v1, first public version 2026-04-04.
2. Ryuzaburo Noda, *On Orthogonal Arrays of Strength 3 and 5 Achieving Rao's Bound*, Graphs and Combinatorics 2 (1986), 277–282, DOI 10.1007/BF01788102.
