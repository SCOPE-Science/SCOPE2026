# Logarithmic counting and interlacing of the cubic square-exception set
## Finding
For the cubic family of Kimura and Umemoto, let \(b\in\mathbb{Z}\setminus\{0,1\}\), let \(\theta\) be the unique real root of
\[
X^3-3bX-b^3,
\]
and set \(\eta_b=((b+1)-\theta)^{-1}\). Put \(\lambda=2+\sqrt3\) and
\[
E_n=\frac{\lambda^n-\lambda^{-n}}{2\sqrt3}.
\]
Kimura--Umemoto prove that the square-exception parameters, namely the integers \(b\) for which \(\eta_b\) is a square in \(O_{K_b}^\times\), are exactly
\[
b_\pm(n)=\frac12(E_{2n-1}-1)\pm2E_{n-1},\qquad n\in\mathbb{Z},
\]
after deleting the degenerate values \(0\) and \(1\).

The two positive branches are strictly interlaced:
\[
0<b_-(n)<b_+(n)<b_-(n+1)\qquad(n\ge2).
\]
For the negative branch, write \(m=-n\). Besides the isolated absolute values \(3\) and \(16\), define for \(m\ge2\)
\[
M_m^- =\frac12(E_{2m+1}+1)-2E_{m+1},\qquad
M_m^+ =\frac12(E_{2m+1}+1)+2E_{m+1}.
\]
Then
\[
16<M_2^-<M_2^+<M_3^-<M_3^+<\cdots,
\]
and the negative square-exceptions are \(-3,-16,-M_2^-,-M_2^+,-M_3^-,-M_3^+,\ldots\).

Both signs have the same two-scale geometry. As \(n\to\infty\),
\[
\frac{b_+(n)}{b_-(n)}\longrightarrow1,
\qquad
\frac{b_-(n+1)}{b_+(n)}\longrightarrow\lambda^2=7+4\sqrt3,
\]
and the analogous limits hold for \(M_m^+/M_m^-\) and \(M_{m+1}^-/M_m^+\).

Consequently, if
\[
N(X)=\#\left\{b\in\mathbb{Z}\setminus\{0,1\}:0<|b|\le X,\ \eta_b\in(O_{K_b}^\times)^2\right\},
\]
then
\[
N(X)=\frac{2\log X}{\log(2+\sqrt3)}+O(1).
\]
In particular, the paper's qualitative statement that the exceptions are sparse admits an explicit logarithmic counting law and a paired lacunary structure.

## Assumptions and scope
The statement concerns exactly the square-exception set classified in Kimura--Umemoto Theorem 5.2. It does not assert that every failure of fundamentality is a square-exception without the additional discriminant hypothesis used in their Theorem 5.5. The counting law is unconditional for the square-exception set itself.

The parameter \(b\) ranges over integers other than \(0\) and \(1\). The source proves that indices \(n\ge2\) produce all positive square-exceptions and indices \(n\le0\) produce all negative square-exceptions. The values \(b_-(0)=1\) and \(b_+(1)=b_-(1)=b_-(-1)=0\) are excluded by the standing convention.

## Proof
Let
\[
D_n=\frac{\lambda^n+\lambda^{-n}}2,
\qquad
E_n=\frac{\lambda^n-\lambda^{-n}}{2\sqrt3}.
\]
Then \(D_n^2-3E_n^2=1\), and the standard Binet identities give
\[
E_{r+1}-E_{r-1}=2D_r,
\qquad
D_{2r}=1+6E_r^2.
\]
Also \(E_n>0\) and is strictly increasing for \(n\ge1\), with \(E_1=1\) and \(E_2=4\).

For \(n\ge2\),
\[
b_+(n)-b_-(n)=4E_{n-1}>0.
\]
Moreover
\[
\begin{aligned}
b_-(n+1)-b_+(n)
&=\frac12(E_{2n+1}-E_{2n-1})-2(E_n+E_{n-1})\\
&=D_{2n}-2(E_n+E_{n-1})\\
&=1+6E_n^2-2(E_n+E_{n-1}).
\end{aligned}
\]
Since \(0<E_{n-1}<E_n\), this is greater than \(1+6E_n^2-4E_n>0\). Finally \(b_-(2)=5>0\). This proves the positive interlacing.

For negative indices put \(m=-n\). Since \(E_{-r}=-E_r\), the two absolute-value branches are \(M_m^-\) and \(M_m^+\) as stated. Their within-pair gap is
\[
M_m^+-M_m^-=4E_{m+1}>0.
\]
For \(m\ge1\), with \(k=m+1\ge2\),
\[
\begin{aligned}
M_{m+1}^- - M_m^+
&=D_{2m+2}-2(E_{m+2}+E_{m+1})\\
&=1+6E_k^2-2(E_{k+1}+E_k).
\end{aligned}
\]
The recurrence \(E_{k+1}=4E_k-E_{k-1}<4E_k\) gives
\[
M_{m+1}^- - M_m^+>1+6E_k^2-10E_k>0
\]
for \(E_k\ge4\). The degenerate value \(M_1^-=0\) is omitted, while \(M_0^+=3\), \(M_1^+=16\), and \(M_2^-=75\), yielding the asserted initial ordering.

The closed forms give, uniformly on either positive branch,
\[
b_\pm(n)=\frac{\lambda^{2n-1}}{4\sqrt3}\left(1+O(\lambda^{-n})\right),
\]
and on either negative-magnitude branch,
\[
M_m^\pm=\frac{\lambda^{2m+1}}{4\sqrt3}\left(1+O(\lambda^{-m})\right).
\]
The stated ratio limits follow immediately. Taking logarithms gives
\[
\log b_\pm(n)=(2n-1)\log\lambda-\log(4\sqrt3)+O(\lambda^{-n}),
\]
with the analogous formula for \(M_m^\pm\). Thus each sign contributes
\[
\frac{\log X}{\log\lambda}+O(1)
\]
parameters of magnitude at most \(X\), because there are two branch values per index and the exponent advances by two. Adding the positive and negative counts gives
\[
N(X)=\frac{2\log X}{\log\lambda}+O(1)
=\frac{2\log X}{\log(2+\sqrt3)}+O(1).
\]

## Verification
The proof above is symbolic and infinite; no finite experiment is used to infer the asymptotic theorem. The accompanying verifier reconstructs \(E_n\) from the exact recurrence \(E_0=0\), \(E_1=1\), \(E_{n+2}=4E_{n+1}-E_n\), checks the source's initial square-exception values, and stress-tests both interlacing inequalities and the two quotient limits over a finite range. Its role is normalization and arithmetic error detection only.

## Relationship to prior work
Kimura--Umemoto, arXiv:2609.37389v1, Theorem 5.2, supplies the complete Pell parametrization of the square-exception set and explicitly lists its first positive and negative terms. Their introduction describes these exceptions as sparse, and the inspected full text does not state a counting asymptotic or the branch-interlacing and successive-scale limits proved here.

A prior result on the same family determines exact fourth-power depth at two individual parameters, \(b=5\) and \(b=96\). That parameter-specific power-depth statement neither implies nor is implied by the global ordering and counting law here.

Classical Pell theory already implies exponential growth for an individual Pell sequence. The new content claimed here is deliberately narrower: the exact two-branch ordering for this square-exception parametrization, the resulting absence of branch collisions, the two quotient limits, and the coefficient \(2/\log(2+\sqrt3)\) for the signed parameter count.

## Limitations
This result does not classify higher power depths of \(\eta_b\), does not remove the discriminant hypothesis from the source's equivalence between non-fundamentality and being a square, and does not claim an effective best constant in the \(O(1)\) remainder. The quotient limits describe each sign separately; the merged ordering by absolute value of positive and negative parameters is not classified here.

## References
1. I. Kimura and H. Umemoto, *On an infinite family of cubic fields with explicit fundamental units*, arXiv:2609.37389v1, 2026, especially Theorem 5.2.
