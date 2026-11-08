# Four-adic energy resonance of the dyadic quartic Fourier graph

## Finding
For each integer \(k\ge 1\), let \(N=2^k\), \(R=\mathbb Z/N\mathbb Z\), and let
\[
C_k=\{(x,x^4):x\in R\}\subset R^2.
\]
Its ordered additive energy is
\[
E_k=\#\{(x,y,u,v)\in R^4:x+y=u+v,\ x^4+y^4=u^4+v^4\}.
\]
Define \((B_1,B_2,B_3,B_4)=(17,19,23,30)\). Every \(k\ge1\) has a unique expression \(k=4m+r\), with integer \(m\ge0\) and \(1\le r\le4\). Then
\[
\boxed{E_k=N^2\bigl(B_r2^m-(k+14)\bigr).}
\]
In particular, the normalized energy has four distinct residue-class asymptotics
\[
\frac{E_k}{N^2}= B_r2^{-r/4}N^{1/4}-(k+14)\quad (k\equiv r\pmod4),
\]
where the residue \(r=4\) denotes zero modulo four. Equivalently, the initial values and exact four-step recursion are
\[
(E_1,E_2,E_3,E_4)=(8,48,384,3072),\qquad
E_k=(k+6)4^k+512E_{k-4}\quad(k\ge5).
\]
Let the unweighted Fourier sum be
\[
F_k(a,b)=\sum_{x\in R}\exp\left(\frac{2\pi i(ax+bx^4)}{N}\right).
\]
The complete constant-input fourth Fourier moment is exactly
\[
\boxed{\frac1{N^2}\sum_{a,b\in R}|F_k(a,b)|^4=E_k.}
\]
The result is about unweighted fourth moments, not the sharp \(\ell^2\)-to-\(\ell^4\) Fourier-extension operator norm for arbitrary coefficients.

## Assumptions and scope
All congruences below occur in the specified ring \(\mathbb Z/2^j\mathbb Z\). Additive energy counts ordered quadruples, including repeats. No smoothness, primality beyond the base prime two, or lower bound on \(k\) besides \(k\ge1\) is assumed. The input curve is injectively parametrized by its first coordinate. The Fourier transform uses unnormalized sums; its fourth moment is averaged over the \(N^2\) frequencies.

## Proof
Write \(h_s(x)=x^4+(s-x)^4\) and \(E_k=\sum_{s\in R}\#\{(x,y)\in R^2:h_s(x)=h_s(y)\}\). We first prove an elementary square-collision identity. If
\[
S_j=\#\{(u,v)\in(\mathbb Z/2^j\mathbb Z)^2:u^2=v^2\},
\]
then \(S_1=2\), \(S_2=8\), and \(S_j=j2^j\) for every \(j\ge1\). Indeed, for \(j\ge3\) odd squares comprise precisely the residues \(1\pmod8\), each having four odd square roots. Thus the odd--odd collisions number \(2^{j+1}\). In the even--even case write \(u=2u_0\), \(v=2v_0\), which contributes \(4S_{j-2}\). Opposite parities do not collide. The recurrence \(S_j=2^{j+1}+4S_{j-2}\), with the displayed initial values, proves the formula.

Fix \(k\ge5\). First suppose that \(s\) is odd. The map \(x\mapsto w=x(s-x)\) takes \(R\) onto the even residues, exactly twice onto each: modulo two both \(x=0\) and \(x=1\) solve \(x(s-x)=0\), and at either root the derivative \(s-2x\) is odd, so Hensel lifting is unique on each parity class. Write \(w=2z\), where \(z\) runs over \(\mathbb Z/2^{k-1}\mathbb Z\), each with multiplicity two. The identity
\[
h_s(x)=s^4-4s^2w+2w^2=2(2z-s^2)^2-s^4
\]
identifies \(t=2z-s^2\) with every odd residue modulo \(2^k\). Consequently the collision count for this fixed \(s\) equals \(16\) times the count of pairs of odd residues modulo \(2^{k-1}\) with equal squares. The latter count is \(2^k\) for \(k-1\ge3\). Each odd \(s\) therefore contributes \(16N\). Summing the \(N/2\) odd values gives \(8N^2\).

Now let \(s=2S\) be even. If \(x\) is odd, then both \(x\) and \(s-x\) are odd and \(h_s(x)\equiv2\pmod{16}\). If \(x\) is even, then \(h_s(x)\equiv0\pmod{16}\). Hence there are no cross-parity collisions.

For odd \(x\), put \(u=x-S\). A binomial expansion yields
\[
h_s(x)=2\bigl(u^4+6S^2u^2+S^4\bigr).
\]
If \(S\) is even, then \(u\) is odd. With \(z=u^2\), the difference of two such output values is
\[
2(z-z')(z+z'+6S^2).
\]
Here \(z,z'\equiv1\pmod8\), and \(6S^2\equiv0\pmod8\); the second factor has exact two-adic valuation one. Thus outputs agree modulo \(2^k\) exactly when \(z\equiv z'\pmod{2^{k-2}}\). For \(k\ge5\), the \(N/2\) odd choices of \(u\) fall into \(2^{k-5}\) square classes modulo \(2^{k-2}\), uniformly with sixteen preimages each. The collision count for each \(s\equiv0\pmod4\) among odd inputs is therefore \(2^{k-5}16^2=8N\).

If \(S\) is odd, then \(u\) is even. Set \(z=u^2\), so \(z,z'\equiv0\pmod4\). The same factored difference has second factor \(z+z'+6S^2\) of exact valuation one, hence output equality is equivalent to \(u^2\equiv u'^2\pmod{2^{k-2}}\). Writing \(u=2v\), with \(v\) modulo \(2^{k-1}\), reduces this condition to \(v^2\equiv v'^2\pmod{2^{k-4}}\). Every class modulo \(2^{k-4}\) has eight lifts to \(\mathbb Z/2^{k-1}\mathbb Z\). Consequently the odd-input collision contribution for each \(s\equiv2\pmod4\) is
\[
8^2 S_{k-4}=64(k-4)2^{k-4}=4(k-4)N.
\]
There are \(N/4\) values of each of the two even-residue types, so all even-\(s\), odd-\(x\) collisions contribute \(2N^2+(k-4)N^2=(k-2)N^2\).

Finally, for even \(s=2S\) and even \(x=2X\), one has \(h_s(x)=16h_S(X)\). The variables \(S,X,Y\) range independently modulo \(2^{k-1}\). The equality \(h_s(2X)=h_s(2Y)\pmod{2^k}\) is equivalent to \(h_S(X)=h_S(Y)\pmod{2^{k-4}}\). Each of the three coordinates has eight lifts from modulus \(2^{k-4}\) to \(2^{k-1}\); this part contributes \(8^3E_{k-4}=512E_{k-4}\). Thus
\[
E_k=8N^2+(k-2)N^2+512E_{k-4}=(k+6)4^k+512E_{k-4}.
\]
For \(2\le k\le4\), every odd fourth power is \(1\) modulo \(2^k\) and every even fourth power is \(0\). For odd \(s\), all \(N\) values of \(x\) give the same output; for even \(s\), the two input parity classes give different outputs, each with \(N/2\) preimages. Summing gives \(E_k=3N^3/4\), namely \(48,384,3072\). For \(k=1\), the fourth-power map is the identity, so \(E_1=8\).

Dividing the recurrence by \(4^k\) gives \(A_k=2A_{k-4}+k+6\), where \(A_k=E_k/4^k\) and \((A_1,A_2,A_3,A_4)=(2,3,6,12)\). Solving on the four residue classes yields \(A_{4m+r}=B_r2^m-(4m+r+14)\) with the four claimed coefficients. Finally, expand \(|F_k(a,b)|^4\) and average over all frequency pairs; orthogonality imposes the two additive-collision congruences exactly, proving the Fourier identity.

## Verification
The accompanying standalone `verify.py` uses only integer arithmetic and the Python standard library. It independently constructs each pair-sum histogram and sums squared multiplicities for every exponent \(1\le k\le11\), comparing against the closed form. It also checks all square-collision identities through modulus \(2^{11}\) and verifies each of the three parity/valuation contributions separately for \(5\le k\le11\). Execute `python3 verify.py`; success ends with `DYADIC_QUARTIC_GRAPH_ENERGY_CHECK_PASS`. These finite checks do not replace the proof for all exponents.

## Relationship to prior work
Mockenhaupt and Tao established the finite-field Fourier-restriction setting and the connection between even Fourier moments and additive representation counts. Their full moment curve uses consecutive powers and assumes odd characteristic, whereas the present object is the lacunary two-coordinate quartic graph over the non-field rings \(\mathbb Z/2^k\mathbb Z\).

Iosevich and Koh studied sums and Fourier extension for quadratic paraboloids over finite fields of odd characteristic. Hickman's 2015 thesis includes restriction over prime-power rings for full moment curves, a different coordinate set and a norm-inequality problem rather than this exact quartic energy. The published research record titled *Exact additive energy of the finite-field quartic graph* provides a particularly close polynomial comparison: its field theorem explicitly excludes characteristics two and three and uses an involution of pair products that is not valid after division by two in the present rings. None of these inspected results implies the stated four-residue dyadic recursion.

## Limitations
The theorem concerns only the unweighted fourth moment of the dyadic quartic graph, not arbitrary coefficient weights, the full twofold convolution histogram, other primes, or higher Fourier moments. A broader, possibly unindexed result on two-adic local representation densities could potentially imply this exact energy formula; historical priority is not established by the searches reported here. No independent mathematical validation has been performed.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1 (18 April 2002), §5, https://arxiv.org/abs/math/0204234.
2. A. Iosevich and D. Koh, *Extension Theorems for Paraboloids in the Finite Field Setting*, arXiv:0805.0814v1 (6 May 2008), https://arxiv.org/abs/0805.0814.
3. J. Hickman, *Topics in affine and discrete harmonic analysis*, University of Edinburgh thesis (1 July 2015), ch. 4, https://era.ed.ac.uk/items/29ea5d40-6678-4834-8ac0-2f2278ae7ffd.
4. *Exact additive energy of the finite-field quartic graph*, publicly available research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f.
