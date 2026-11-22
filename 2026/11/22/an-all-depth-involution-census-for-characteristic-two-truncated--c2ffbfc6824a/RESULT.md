# An all-depth involution census for characteristic-two truncated Nottingham groups

## Finding
Let \(q=2^e\) with \(e\ge1\), and let \(m\ge3\). The finite substitution group
\[
G_m(q)=\left\{f(t)=t+\sum_{j=2}^{m-1}a_jt^j\pmod{t^m}:a_j\in\mathbb F_q\right\}
\]
has order \(q^{m-2}\), with multiplication by truncated composition. For any nonidentity \(f\), define its depth \(r=\operatorname{ord}_t(f(t)-t)-1\in\{1,\ldots,m-2\}\). Let \(c_m(r)\) be the number of depth-\(r\) elements satisfying \(f\circ f=t\pmod{t^m}\), including those not lifting to formal involutions. Then
\[
c_m(r)=\begin{cases}
(q-1)q^{\min(\lfloor(m-2)/2\rfloor,m-r-2)},&r\text{ odd},\\
0,&r\text{ even and }2r+1<m,\\
(q-1)q^{m-r-2},&r\text{ even and }2r+1\ge m.
\end{cases}
\]
In particular, **every odd depth below the midpoint has the same number of involutions**. The total number \(I_m(q)\) of elements whose square is the identity, including the identity itself, is
\[
\boxed{I_{2h}(q)=q^{h-1}\bigl(1+(q-1)\lfloor h/2\rfloor\bigr),\quad h\ge2,}
\]
\[
\boxed{I_{2h+1}(q)=q^{h-1}\bigl(1+(q-1)(\lfloor h/2\rfloor+1)\bigr),\quad h\ge1.}
\]
For fixed \(q\), if a uniformly sampled nonidentity element satisfying \(f^2=1\) has depth \(R_m\), then \(R_m/m\) converges in distribution to the uniform law on \([0,1/2]\) as \(m\to\infty\).

## Assumptions and scope
The field has characteristic exactly two; \(q\) may be any power of two, with no bound on \(m\). The group uses polynomial representatives **modulo \(t^m\)**, so there are exactly \(m-2\) free coefficients. A formal series and its truncation are distinguished: \(f^2=1\) in a finite quotient does not guarantee it is a truncation of an involution in the infinite Nottingham group. The depth of the identity is excluded from \(c_m(r)\). The notation \(f^2\) means composition, not multiplication of power series.

## Proof
All composition identities in this proof take place in \(\mathbb F_q[[t]]\) until reduction modulo \(t^m\). Fix \(r\) and let \(f=t+a t^{r+1}+O(t^{r+2})\) with \(a\ne0\). Put \(H=f\circ f-t\). Cancellation of the direct copies of every coefficient shows \(\operatorname{ord}_t(H)\ge2r+1\). At degree \(2r+1\), the coefficient is \((r+1)a^2\). Therefore if \(r\) is even, an involution of this depth exists in \(G_m(q)\) exactly when \(2r+1\ge m\); in that case every coefficient after \(a\) is free, giving \((q-1)q^{m-r-2}\) choices.

Now let \(r\) be odd. The coefficient at degree \(2r+1\) vanishes. **Odd-degree obstruction lemma:** if \(H\ne0\) has least term \(b t^k\), then \(k\) must be even. Indeed, \(f\) commutes with \(f\circ f=t+H\). The first coefficient of their composition commutator, at degree \(r+k\), is \((k-r-1)ab\). When \(k\) and \(r\) are both odd this is \(ab\ne0\), a contradiction. Thus, after all preceding obstruction coefficients have been killed, any obstruction in an odd degree is automatically zero.

**Even-degree triangular lemma:** for each even \(k\ge2r+2\), the coefficient of \(t^k\) in \(H\) is affine in \(a_{k-r}\), with nonzero linear coefficient \(a\), and involves no later coefficients. To see this, replace \(f\) by \(f+u t^{k-r}\). Its direct two occurrences cancel in characteristic two. The first remaining mixed contribution is \((k-2r-1)au\,t^k=au\,t^k\); terms quadratic in \(u\) begin in degree at least \(2(k-r)-1>k\). Hence the equation at degree \(k\) uniquely determines the coefficient \(a_{k-r}\). Inductively choose all other coefficients freely, solve the even obstruction equations at \(k=2r+2,2r+4,\ldots<m\), and use the odd-degree lemma to remove the intervening equations. The number of determined coefficients is
\[
\max\bigl(0,\lfloor(m-1)/2\rfloor-r\bigr),
\]
so the number of freely chosen coefficients following \(a\) is
\[
m-r-2-\max\bigl(0,\lfloor(m-1)/2\rfloor-r\bigr)
=\min\bigl(\lfloor(m-2)/2\rfloor,m-r-2\bigr).
\]
This proves every depth count over every characteristic-two finite field.

For the total, if \(m=2h\), the shallow odd depths \(1\le r\le h-1\) contribute \(\lfloor h/2\rfloor(q-1)q^{h-1}\); every depth \(h\le r\le2h-2\) is unrestricted and contributes in aggregate \(q^{h-1}-1\). Adding the identity yields the even formula. If \(m=2h+1\), the shallow odd depths \(1\le r\le h\) contribute \(\lceil h/2\rceil(q-1)q^{h-1}\). The admissible even boundary depth \(r=h\) when \(h\) is even adds \((q-1)q^{h-1}\), and deeper depths contribute \(q^{h-1}-1\). Since \(\lceil h/2\rceil+\mathbf1_{2\mid h}=\lfloor h/2\rfloor+1\), the odd formula follows.

Finally, for fixed \(q\), the shallow odd depths carry \(1-O(1/m)\) of the mass among nonidentity involutions and each has identical weight. Those depths form a lattice of mesh \(2/m\) in \([0,1/2]\), proving the stated weak convergence.

## Verification
Run `python check.py` using Python 3 and its standard library. It exhaustively constructs truncated compositions and compares the actual **full depth histogram**, not only total counts, with the formulas for \(q=2\) and \(3\le m\le15\), \(q=4\) and \(3\le m\le9\), \(q=8\) and \(3\le m\le7\), and \(q=16\) and \(3\le m\le5\). `checked_output.txt` records the actual successful execution. These finite computations support, but do not replace, the proof for all \(m\) and \(q\).

## Relationship to prior work
Finite-order elements, ramification breaks, and conjugacy in the full Nottingham group are studied by Byszewski, Cornelissen and Tijsma (2020/2022), building on Klopsch and Lubin. Their results concern genuine formal torsion and its conjugacy, not the exact counts of square-one jets of **every** possible depth in all finite quotients. The publicly accessible 2026 result *Parity-obstructed lifting of depth-one involutions in truncated Nottingham groups* gives a precise affine description **only of depth one**, recovered by the \(r=1\) specialization here; the all-depth formula and limiting depth law are not contained in its stated scope. Pálfy's study counts conjugacy classes in bounded-degree quotients, a different invariant. The 2026 truncated-group presentation by Szechtman concerns power-commutator relations through degree fifteen; its complete text was not available for comparison, and a hidden implication at bounded degrees remains possible. No absolute priority claim is made.

## Limitations
Only order-dividing-two elements are counted, not elements of order four or higher, nor conjugacy classes among the involutions. The proof uses characteristic two essentially. The asymptotic law fixes \(q\) as \(m\to\infty\); it makes no assertion about a variable field order. Formula verification in finite small groups is not a substitute for the analytic and algebraic proof. Historical literature coverage and independent mathematical review remain incomplete.

## References
1. J. Byszewski, G. Cornelissen, D. Tijsma, *Automata and finite order elements in the Nottingham group*, arXiv:2008.04971 (first posted 2020-08-11); *J. Algebra* 602 (2022), 484–554. https://arxiv.org/abs/2008.04971 ; open final version https://research-portal.uu.nl/ws/files/149368215/1_s2.0_S002186932200134X_main.pdf
2. P. P. Pálfy, *The number of conjugacy classes in some quotients of the Nottingham group*, *Proc. Edinburgh Math. Soc.* 41 (1998), 369–384. https://doi.org/10.1017/S0013091500019714
3. *Parity-obstructed lifting of depth-one involutions in truncated Nottingham groups* (publicly posted 2026-11-08). https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-parity-obstructed-lifting-of-depth-one-involutions-in-truncated--e2982e387cf3/RESULT.md
4. *Trace-split conjugacy classes in the fourth finite Nottingham quotient over even fields* (publicly posted 2026-10-26). https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-trace-split-conjugacy-classes-in-the-fourth-finite-nottingham-qu--9e6f6037105a/RESULT.md
5. F. Szechtman, *A power-commutator presentation for the group of truncated polynomials under substitution*, arXiv:2610.01469 (first posted 2026-10-01). https://arxiv.org/abs/2610.01469
