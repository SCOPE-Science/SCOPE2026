# All odd-modulus Newman digit sums satisfy the Shevelev–Moses identity

## Finding

For every odd integer \(n\geq3\), put \(b=n-1\), let \(s_b(r)\) be the sum of the base-\(b\) digits of the nonnegative integer \(r\), and define, for \(x\in\mathbb Z_{\geq0}\) and \(a\in\{0,\ldots,n-1\}\),
\[
S_{n,a}(x)=\sum_{\substack{0\leq r<x\\r\equiv a\pmod n}}(-1)^{s_b(r)}.
\]
Let
\[
P_n(t)=\sum_{j=0}^{(n-1)/2}(-1)^j\binom{n}{2j+1}t^j.
\]
Then, simultaneously for **all** residue classes \(a\) and all integer cutoffs \(x\geq0\),
\[
\boxed{\sum_{j=0}^{(n-1)/2}(-1)^j\binom{n}{2j+1}S_{n,a}(b^{2j}x)
=\sum_{c=0}^{n-1}S_{n,c}(x)
=\begin{cases}0,&x\text{ even},\\(-1)^{s_b(x-1)},&x\text{ odd}.\end{cases}}
\]
In particular, the \(a=0\) case establishes conjectural identity (15) of Shevelev and Moses, while the entire family of residue classes establishes their separately conjectured identity (74). They proved the former for \(n=3,5\) and tested further odd moduli; they explicitly posed the all-residue version as a separate generalization.

The stronger algebraic form is \(P_n(B_n^2)=J_n\) for the explicit integer matrix \(B_n\) defined below, where \(J_n\) is the all-ones matrix of size \(n\).

## Assumptions and scope

The modulus \(n\) is any odd integer at least three, **not necessarily prime**; \(b=n-1\) is even. The integer \(x\) is any nonnegative cutoff. The residue \(a\) ranges over all residue classes modulo \(n\), and \(s_b(0)=0\). The theorem makes no claim for even \(n\), for alternative bases, or for summands with weights other than base-digit parity.

Define \(f_n(d)=(-1)^d\) for \(0\leq d\leq n-2\), and \(f_n(n-1)=0\). Define the \(n\)-by-\(n\) matrix
\[
(B_n)_{ac}=f_n((a+c)\bmod n),\qquad 0\leq a,c<n.
\]
Here \((a+c)\bmod n\) is its representative in \(\{0,\ldots,n-1\}\). Define \(\mathbf S_n(x)=(S_{n,0}(x),\ldots,S_{n,n-1}(x))^\mathsf T\).

## Proof

**1. Exact digit transfer.** Write every \(0\leq r<bx\) uniquely as \(r=bu+d\), where \(0\leq u<x\) and \(0\leq d<b\). The digit concatenation gives \((-1)^{s_b(r)}=(-1)^{s_b(u)+d}\). Since \(b\equiv-1\pmod n\), the congruence \(r\equiv a\pmod n\) becomes \(d\equiv a+u\pmod n\). Therefore
\[
\mathbf S_n(bx)=B_n\mathbf S_n(x),
\qquad
\mathbf S_n(b^{2j}x)=B_n^{2j}\mathbf S_n(x)
\]
for every \(x\geq0\) and \(j\geq0\). This identity accounts for the interval endpoint exactly; no full-block restriction on \(x\) is needed.

**2. Diagonalize the square.** Fix \(\zeta=e^{2\pi i/n}\). The Fourier vectors \(v_r=(\zeta^{ra})_{a=0}^{n-1}\), for \(0\leq r<n\), form a complex basis, including for composite \(n\). From the displayed matrix definition,
\[
B_nv_r=w_rv_{-r},\qquad
w_r=\sum_{d=0}^{n-2}(-1)^d\zeta^{rd}
=\frac{1-\zeta^{-r}}{1+\zeta^r}.
\]
The finite geometric-sum formula uses that \(n-1\) is even. The denominator does not vanish: an odd-order root of unity cannot equal \(-1\). For \(r=0\), \(w_0=0\). For every \(1\leq r<n\), write
\[
u_r=\frac{\zeta^r-1}{\zeta^r+1}.
\]
Then direct multiplication yields
\[
B_n^2v_r=w_rw_{-r}v_r=-u_r^2v_r.
\]
Consequently, \(B_n^2\) is diagonal in the Fourier basis, with eigenvalue zero at \(r=0\) and eigenvalues \(-u_r^2\) at all nonzero frequencies.

**3. Annihilating polynomial.** The binomial identity
\[
P_n(-u^2)=\frac{(1+u)^n-(1-u)^n}{2u}
\]
holds for all nonzero complex \(u\). At \(u=u_r\),
\[
1+u_r=\frac{2\zeta^r}{1+\zeta^r},\qquad
1-u_r=\frac{2}{1+\zeta^r}.
\]
Since \(\zeta^{rn}=1\), the two numerators raised to the \(n\)-th power agree, so \(P_n(-u_r^2)=0\) for every \(r\ne0\). At \(r=0\), \(P_n(0)=\binom n1=n\). Thus \(P_n(B_n^2)\) has eigenvalue \(n\) on the constant Fourier vector and eigenvalue zero on every other Fourier vector. The matrix \(J_n\) has exactly the same action, hence
\[
\boxed{P_n(B_n^2)=J_n.}
\]
This is an exact integer-matrix identity for each odd \(n\geq3\), not merely a numerical eigenvalue calculation.

**4. Every cutoff and residue.** Apply the matrix identity to \(\mathbf S_n(x)\), use the digit transfer, and read coordinate \(a\):
\[
\sum_{j=0}^{(n-1)/2}(-1)^j\binom n{2j+1}S_{n,a}(b^{2j}x)
=\sum_{c=0}^{n-1}S_{n,c}(x)
=\sum_{0\leq r<x}(-1)^{s_b(r)}.
\]
To evaluate the final sum, pair consecutive integers \(2k,2k+1\). Because the base \(b\) is even, the least base-\(b\) digit of \(2k\) is even, so adding one produces no carry and changes the digit sum by exactly one. Each pair contributes zero. Thus the total sum is zero for even \(x\), and its one unpaired final term is \((-1)^{s_b(x-1)}\) for odd \(x\). This proves every asserted identity, including \(x=0\). \(\square\)

## Verification

The standalone standard-library script `verify.py` independently constructs \(B_n\), evaluates \(P_n(B_n^2)\) by exact integer-matrix Horner arithmetic for every odd \(n\) from \(3\) through \(41\), and checks that all matrix entries equal one. It independently enumerates digit parities and verifies the original arbitrary-cutoff formula for \(n=3\) and \(1\le x\le120\), \(n=5\) and \(1\le x\le40\), and \(n=7\) and \(1\le x\le12\); the largest direct enumeration endpoint is \(559872\). Run `python3 verify.py` in the directory containing this document. These finite checks supplement, but do not replace, the universal algebraic proof.

## Relationship to prior work

Shevelev and Moses, *A family of digit functions with large periods*, arXiv:1209.5705, equation (15), posed exactly the \(a=0\) arbitrary-cutoff identity for odd \(n\) and proved \(n=3,5\), with experimental checks for other odd \(n\). Their Section 10, equation (74), separately conjectures the simultaneous identity for all residue classes. The theorem above proves both conjectures for every odd modulus.

Their earlier *Tangent power sums and their applications*, arXiv:1207.0404, gives the tangent-root polynomial and the closely related endpoint identity at cutoffs of the form \(b^{2p}\) (especially its Section 6). Those results supply structural antecedents, but the previously established full-block statements do not entail the arbitrary-cutoff vector identity without the extra matrix argument here. OEIS A091042 records the tangent-power spectral polynomial rather than the complete arbitrary-cutoff Newman sum identity. Allouche's discussion of a resolved Shevelev conjecture concerns a distinct Thue–Morse translation problem, not this question.

## Limitations

The result is restricted to odd moduli and digit parity in the correlated even base \(n-1\). It establishes an exact linear identity, not a pointwise sign or asymptotic formula for each \(S_{n,a}(x)\). Existing work contains closely related spectral and digit-sum identities; an equivalent treatment in later or unlocated literature cannot be ruled out by the inspected sources. No independent mathematical audit has been conducted.

## References

1. V. Shevelev and P. J. C. Moses, *A family of digit functions with large periods*, arXiv:1209.5705 (first submitted 24 September 2012), especially equation (15) and the discussion of the \(n=3,5\) cases. https://arxiv.org/abs/1209.5705
2. V. Shevelev and P. J. C. Moses, *Tangent power sums and their applications*, arXiv:1207.0404 (first submitted 29 June 2012), Sections 2, 5 and 6. https://arxiv.org/abs/1207.0404
3. OEIS Foundation, A091042, tangent-power-sum characteristic polynomial and related identities. https://oeis.org/A091042
4. J.-P. Allouche, *Thue, Combinatorics on Words, and Conjectures Inspired by the Thue–Morse Sequence*, Journal de Théorie des Nombres de Bordeaux 27 (2015), 371–388, doi:10.5802/jtnb.906. https://doi.org/10.5802/jtnb.906
