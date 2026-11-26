# Fixed-space distribution and element-orbit count for the first Witt coordinate algebra in characteristic five

## Finding
Let \(q=5^e\) with \(e\ge1\), and let
\[
A=\mathbb F_q[t]/(t^5).
\]
Every \(\mathbb F_q\)-algebra automorphism is uniquely determined by
\[
\phi(t)=at+bt^2+ct^3+dt^4,
\]
where \(a\in\mathbb F_q^\times\) and \(b,c,d\in\mathbb F_q\). Put \(\delta_e=1\) when \(e\) is even and \(\delta_e=0\) when \(e\) is odd. If \(N_j(q)\) is the number of automorphisms with \(j\)-dimensional fixed subspace in \(A\), then
\[
N_5(q)=1,\qquad N_4(q)=q-1,\qquad N_3(q)=2q^2-q,
\]
\[
N_2(q)=(4+2\delta_e)q^3-2q^2,\qquad N_1(q)=(q-5-2\delta_e)q^3.
\]
No other fixed-space dimension occurs. Burnside's lemma therefore gives exactly
\[
q(9+2\delta_e)
\]
automorphism orbits on the underlying set of \(A\): \(9q\) for odd \(e\), and \(11q\) for even \(e\).

## Assumptions and scope
The field has characteristic \(5\), and \(A\) is the one-variable restricted Cartan coordinate algebra \(O(1;1)\). The result concerns ordinary \(\mathbb F_q\)-algebra automorphisms and their action on elements of \(A\), not the non-smooth automorphism group scheme over arbitrary base algebras. The finite-field extension degree enters only through whether \(\mathbb F_q^\times\) contains elements of order \(3\).

## Proof
An algebra endomorphism of \(A\) is determined by the image of \(t\). It is invertible exactly when the coefficient of \(t\) is nonzero, so the displayed parameterization gives all automorphisms and
\[
|\operatorname{{Aut}}(A)|=(q-1)q^3.
\]
On the ordered basis \((t,t^2,t^3,t^4)\) of the maximal ideal, substitution gives
\[
\phi(t^2)=a^2t^2+2ab t^3+(b^2+2ac)t^4,
\]
\[
\phi(t^3)=a^3t^3+3a^2b t^4,\qquad \phi(t^4)=a^4t^4.
\]
Thus a vector \(x_1t+x_2t^2+x_3t^3+x_4t^4\) is fixed exactly when
\[
(a-1)x_1=0,
\]
\[
bx_1+(a^2-1)x_2=0,
\]
\[
cx_1+2abx_2+(a^3-1)x_3=0,
\]
\[
dx_1+(b^2+2ac)x_2+3a^2bx_3+(a^4-1)x_4=0.
\]
The scalar subspace \(\mathbb F_q1\) is always fixed, so the fixed dimension in \(A\) is one plus the nullity of this system.

For \(a=1\), the cases are immediate. If \(b\ne0\), only \(x_4\) is free, giving fixed dimension \(2\), with \((q-1)q^2\) automorphisms. If \(b=0\) and \(c\ne0\), then \(x_3,x_4\) are free, giving dimension \(3\), with \(q(q-1)\) automorphisms. If \(b=c=0\) and \(d\ne0\), then \(x_2,x_3,x_4\) are free, giving dimension \(4\), with \(q-1\) automorphisms. Finally \(b=c=d=0\) is the identity and has fixed dimension \(5\).

For \(a=-1\), \(x_1=0\), and the equations force \(x_3=-bx_2\). The last equation becomes
\[
(b^2+c)x_2=0.
\]
Hence fixed dimension is \(3\) precisely when \(c=-b^2\), giving \(q^2\) automorphisms after the free choices of \(b,d\); the remaining \(q^3-q^2\) have fixed dimension \(2\).

If \(a\) has exact order \(3\) or \(4\), exactly one of \(a^2-1,a^3-1,a^4-1\) contributes a free variable after triangular elimination, so the fixed dimension is always \(2\), independently of \(b,c,d\). In \(\mathbb F_{5^e}^\times\), there are always two elements of exact order \(4\), and there are two elements of exact order \(3\) exactly when \(e\) is even. All remaining values of \(a\ne1,-1\) make every diagonal factor \(a^k-1\), \(1\le k\le4\), nonzero, so the fixed dimension is \(1\). Summing these cases yields the stated formulas for \(N_j(q)\); their sum is \((q-1)q^3\).

Burnside's lemma says that the number of orbits on \(A\) is
\[
\frac{1}{(q-1)q^3}\sum_{j=1}^5 N_j(q)q^j.
\]
Substitution and simplification give
\[
\sum_{j=1}^5 N_j(q)q^j=q^4(q-1)(9+2\delta_e),
\]
which proves the orbit count.

## Verification
The accompanying `verify.py` independently reconstructs the automorphism matrices. It exhaustively checks all \(500\) automorphisms over \(\mathbb F_5\), obtains the fixed-space distribution \((N_1,N_2,N_3,N_4,N_5)=(0,450,45,4,1)\), explicitly computes all \(45\) element orbits, and verifies Burnside's sum. It separately implements \(\mathbb F_{25}=\mathbb F_5[\alpha]/(\alpha^2-2)\), exhaustively checks all \(375000\) automorphisms there, and obtains \((281250,92500,1225,24,1)\), agreeing with the even-extension formula.

## Relationship to prior work
Bahturin and Kochetov identify the restricted Cartan coordinate algebra \(O(m;1)\) with the truncated polynomial algebra and use its automorphism group scheme to study Cartan-type Lie algebras; for \(p>3\) they recall the group-scheme isomorphism \(\operatorname{{Aut}}(O(m;1))\cong\operatorname{{Aut}}(W(m;1))\). Their statements supply the structural setting but not a finite-field fixed-space distribution or Burnside orbit count for \(O(1;1)\). An older paper of Deo and Maitra studies graded automorphisms of truncated polynomial algebras in characteristic zero; its graded automorphisms are a different, much smaller group and its theorems do not give the ordinary finite-field action counted here. Targeted database and literature searches located no statement implying the formulas above.

## Limitations
The theorem is specific to characteristic \(5\). For larger primes, the same triangular strategy applies but additional multiplicative orders can occur among \(1,\ldots,p-1\), and the fixed-space stratification requires further case analysis. The result counts orbits of elements, not conjugacy classes inside the automorphism group and not orbits on subspaces or ideals. No independent audit has been performed.

## References
1. Y. Bahturin and M. Kochetov, *Group gradings on restricted Cartan type Lie algebras*, arXiv:1001.0191v1; Pacific J. Math. 253 (2011), 289--319, DOI 10.2140/pjm.2011.253.289. The manuscript lists primary MSC 17B70 and defines \(O(m;1)\) as a truncated polynomial algebra.
2. S. Deo and J. K. Maitra, *Automorphism groups of truncated polynomial algebras*, Nat. Acad. Sci. Letters 20 (1997), 74--80. This treats graded automorphisms in characteristic zero and is used only as a comparison source.
