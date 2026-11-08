# Exact 23-adic isometries and uniform distribution of Padovan numbers

## Finding
Let \(P_0=P_1=P_2=1\) and \(P_{n+3}=P_{n+1}+P_n\) for all integers \(n\geq0\). For every residue-branch index \(r\in\{0,1,\ldots,21\}\) and distinct integers \(s,t\geq0\),
\[
\boxed{\nu_{23}(P_{r+22t}-P_{r+22s})=\nu_{23}(t-s).}
\]
Consequently, for every integer \(k\geq1\), the least period of \((P_n\bmod 23^k)_{n\geq0}\) is exactly \(22\cdot23^k\). In each least period, **each** of the \(23^k\) residue classes occurs **exactly 22 times**. Thus the Padovan sequence is uniformly distributed modulo every power of \(23\); each of its 22 index branches extends to a bijective isometry of \(\mathbb Z_{23}\).

## Assumptions and scope
The Padovan indexing here is fixed by the first three terms all being \(1\), in contrast with the shifted presentation sometimes used in sequence databases. For a nonzero integer \(z\), \(\nu_{23}(z)\) denotes the exponent of \(23\) dividing \(z\); the exact difference theorem excludes \(s=t\). The residue-period assertions concern the ordinary integer sequence and all positive powers of \(23\), not other primes.

## Proof
Put
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},\qquad
w=\begin{pmatrix}1\\1\\1\end{pmatrix},\qquad
e=(1,0,0).
\]
Then \(P_n=eM^nw\) for \(n\ge0\). Direct exact matrix multiplication (reproduced in the verifier) gives, over \(\mathbb F_{23}\),
\[
M^{22}=I+N,\quad
N=\begin{pmatrix}16&13&22\\22&15&13\\13&12&15\end{pmatrix},
\quad N^2=0,\quad Nw=5\begin{pmatrix}1\\10\\10^2\end{pmatrix}.
\]
The vector \((1,10,10^2)^T\) is an eigenvector of \(M\) with eigenvalue \(10\) in \(\mathbb F_{23}\). In particular, for \(0\le r\le21\),
\[
eM^rNw=5\cdot10^r\pmod{23},
\]
which is nonzero (indeed, \(10\) has multiplicative order \(22\)). For any integer \(t\geq0\), the nilpotence gives
\[
P_{r+22t}=eM^r(I+N)^tw=P_r+5\cdot10^r t\pmod{23}.
\]
Therefore the branch is an isometry when \(23\nmid(t-s)\).

For the higher digits, exact multiplication modulo \(23^2\) gives
\[
M^{506}=I+23C\pmod{23^2},\qquad C\equiv N\pmod{23}.
\]
For clarity, the displayed equality means \(M^{506}=I+23C_\ast\) over the integer matrices for some integral \(C_\ast\) whose reduction is \(N\); this follows because \(M^{506}\equiv I\pmod{23}\). We use \(C_\ast\) below.

**Prime-power matrix lemma.** If \(p\ge3\) is prime and \(B=I+pC\) for an integral square matrix \(C\), then for every integer \(h>0\), writing \(e=\nu_p(h)\) and \(a=h/p^e\),
\[
B^h\equiv I+p^{e+1}aC\pmod{p^{e+2}}.
\]
To verify this, induct on \(e\) using the binomial expansion of \((I+p^{e+1}C_e)^p\): all terms beyond the linear one are divisible by \(p^{e+3}\), and the coefficient of the linear term is \(p^{e+2}\). Raising the resulting congruence to the unit exponent \(a\) proves the formula. The lemma concerns powers of one matrix, so no noncommutativity issue arises.

Now suppose \(t\ne s\) and \(t\equiv s\pmod{23}\). Write \(t=t_0+23u\) and \(s=t_0+23v\), with \(0\le t_0\le22\) and \(u,v\ge0\). Interchange \(u,v\) if needed, so \(u>v\). Apply the lemma with \(B=M^{506}\) and \(h=u-v\), obtaining
\[
\frac{P_{r+22t}-P_{r+22s}}{23^{1+\nu_{23}(u-v)}}
\equiv\frac{u-v}{23^{\nu_{23}(u-v)}}eM^{r+22t_0}Nw\pmod{23}.
\]
This is well-defined because the numerator is divisible by the indicated power. The right-hand side is a unit modulo \(23\): since \(M^{22t_0}\equiv I+t_0N\) and \(N^2=0\), its matrix factor is \(5\cdot10^r\not\equiv0\). Hence
\[
\nu_{23}(P_{r+22t}-P_{r+22s})=1+\nu_{23}(u-v)=\nu_{23}(t-s).
\]
The case \(t\not\equiv s\pmod{23}\) was established by the affine reduction, completing the exact isometry theorem.

For fixed \(r\) and \(k\), the isometry implies that the map \(t\bmod23^k\mapsto P_{r+22t}\bmod23^k\) is injective. Since its finite domain and target each have size \(23^k\), it is bijective. As every index within \(0\le n<22\cdot23^k\) is uniquely \(n=r+22t\) with \(0\le r<22\), each residue occurs exactly once from each of the 22 branches, or 22 times in total.

To prove this block is a **least period**, note that the characteristic polynomial of \(M\) modulo 23 factors as
\[
X^3-X-1=(X-10)^2(X-3).
\]
The eigenvalue \(10\) has order \(22\) in \(\mathbb F_{23}^{\times}\), while \(M^{22}=I+N\ne I\) with \(N^2=0\). Thus \(M\) has exact order \(22\cdot23=506\) modulo \(23\): the order must be divisible by 22, and its remaining unipotent factor has exact order 23. The prime-power matrix lemma applied to \(M^{506}=I+23C_\ast\), with \(C_\ast\not\equiv0\pmod{23}\), then shows that \(M\) has order exactly \(506\cdot23^{k-1}=22\cdot23^k\) modulo \(23^k\). Finally, the columns \(w,Mw,M^2w\) form an integral matrix with determinant \(-1\). Therefore any period of the scalar Padovan sequence modulo \(23^k\) forces \(M^h=I\pmod{23^k}\) by its first three shifted values, so the scalar period equals the matrix order.

## Verification
The included `verify.py` independently implements exact matrix exponentiation and Padovan recurrence arithmetic. It checks the \(M^{22}\) and \(M^{506}\) certificates, the 22 slopes and finite-field affine identity, full frequency distributions for moduli \(23\), \(23^2\), and \(23^3\), least-period exclusions for those levels, and 2000 seeded random pairs for the exact branch-distance identity. It uses only Python's standard library. Run `python verify.py` alongside this document. The infinite statement is proved by the matrix-power lemma, not inferred from these finite tests.

## Relationship to prior work
Gil, Weiner and Zara (2006) study *complete* \(\Phi_3\)-sequences over a finite field, defined to have period \(p-1\) and to permute nonzero residues. Their special treatment of \(p=23\) establishes a primitive-root characterization for that different class of sequences, but it does not count residues in the classical Padovan sequence, whose exact period modulo 23 is 506 rather than 22. Yilmaz and Taskara (2015) study Padovan/Perrin matrix recurrences and iterated binomial transforms, without the exact 23-adic scalar distribution or isometry claim. The OEIS entry A000931 supplies the Padovan sequence and its shift conventions, but no theorem of this form. Bravo and Irmak (2024) study 2-adic valuations of *shifted* Padovan numbers, not 23-adic distribution.

The Perrin trace sequence obeys the same cubic recurrence but has different initial values. Its previously determined sparse 23-adic residue spectrum does not imply the uniform Padovan law; the derivative \(eM^rNw\) is nonzero for this Padovan initial vector, while the trace initial vector has a different lifting behavior.

## Limitations
The conclusion applies only to \(23\)-power moduli and the indicated Padovan normalization. It does not imply uniformity modulo arbitrary integers, or the absence of earlier equivalent results not located in the inspected sources. The proof and verifier have received only the documented self-review; independent mathematical audit has not been performed.

## References
1. J. B. Gil, M. D. Weiner and C. Zara, *Complete Padovan sequences in finite fields*, arXiv:math/0605348v1, publicly submitted 2006-05-12, https://arxiv.org/abs/math/0605348 .
2. N. Yilmaz and N. Taskara, *On the properties of iterated binomial transforms for the Padovan and Perrin matrix sequences*, arXiv:1502.07919, first publicly submitted 2015-02-27, https://arxiv.org/abs/1502.07919 .
3. OEIS Foundation, A000931, *Padovan sequence*, https://oeis.org/A000931 .
4. E. Bravo and N. Irmak, *The 2-adic valuation of shifted Padovan and Perrin numbers and applications*, Turkish Journal of Mathematics **48** (2024), 1183–1196, https://doi.org/10.55730/1300-0098.3568 .
