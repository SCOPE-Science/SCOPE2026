# Exact antisquare orders and starting densities in the Mephisto Waltz word

## Finding
Let \(w\) be the binary fixed point beginning in \(0\) of the substitution \(0\mapsto001\), \(1\mapsto110\). An *antisquare of order* \(k\ge1\) is a factor \(u\overline u\), where \(|u|=k\) and the bar interchanges \(0\) and \(1\). Then the following assertions hold.

1. **Complete order spectrum.** An antisquare of order \(k\) occurs in \(w\) if and only if \(k\in\{3^t,2\cdot3^t:t\ge0\}\).
2. **Exact starting-position criterion.** Define \(c(q)=w(q)\oplus w(q+1)\). Given \(t\ge0\), \(h\in\{1,2\}\), \(k=h3^t\), and a starting position \(i=q3^t+r\) with \(0\le r<3^t\), the factor beginning at \(i\) is an antisquare of order \(k\) precisely as follows:
   - If \(h=1,r=0\), exactly when \(c(q)=1\).
   - If \(h=1,r>0\), exactly when \(c(q)=c(q+1)=1\).
   - If \(h=2,r=0\), exactly when either \(q=3a\) with \(c(a)=1\), or \(q=3a+2\) with \(c(a)=0\), for some \(a\ge0\).
   - If \(h=2,r>0\), exactly when \(q\equiv2\pmod9\).
3. **Exact natural densities.** For \(k=h3^t\), the limit of the proportion of starting positions \(0\le i<N\) supporting an antisquare of order \(k\) exists, and is
\[
\delta_{3^t}=\frac16+\frac{1}{3^{t+1}},\qquad
\delta_{2\cdot3^t}=\frac19+\frac{2}{3^{t+2}}.
\]
For every other order the density is \(0\). In particular, arbitrarily long antisquares occur with positive starting-position densities, approaching \(1/6\) and \(1/9\) along the two allowed families.

## Assumptions and scope
Positions \(i,q,a\) are nonnegative integers, intervals have zero-based, end-exclusive indexing, and all densities are ordinary asymptotic natural densities over *starting positions* with a fixed antisquare order. Set \(w(n)=d_2(n)\bmod2\), where \(d_2(n)\) counts digits equal to \(2\) in the usual base-three expansion of \(n\); this is exactly the displayed fixed point. The symbol \(\oplus\) is addition modulo two. No statement concerns a simultaneous limit in which the order grows with the starting-position cutoff.

## Proof
**Digit structure.** The substitution gives, for every \(a\ge0\),
\[
w(3a)=w(3a+1)=w(a),\qquad w(3a+2)=1-w(a).
\tag{1}
\]
Consequently, whenever \(L=3^t\), \(q\ge0\), and \(0\le r<L\),
\[
w(Lq+r)=w(q)\oplus w(r).
\tag{2}
\]
Indeed, the ternary digits of \(Lq+r\) concatenate those of \(q\) and the \(t\)-digit representation of \(r\), with leading zeroes permitted.

**All possible orders.** Suppose \(w[i:i+2k]\) is an antisquare, so \(w(n+k)=1-w(n)\) for \(i\le n<i+k\). Complementation preserves the truth of equality between adjacent symbols. By (1), the pair at positions \(3a,3a+1\) is always equal and the pair at \(3a+1,3a+2\) always unequal. For \(k\ge4\) with \(k\equiv1\pmod3\), choose \(n\in[i,i+k-2]\) with \(n\equiv0\pmod3\): its adjacent pair is equal, whereas the shifted pair begins at residue \(1\) and is unequal, a contradiction. For \(k\ge4\) with \(k\equiv2\pmod3\), instead choose \(n\equiv1\pmod3\): its pair is unequal and the shifted pair begins at residue \(0\), giving the opposite contradiction. Such \(n\) exist because the interval contains at least three consecutive integers. Therefore every possible order \(k\ge4\) is divisible by three.

If \(k=3m\), then for each \(n\) in the first half, the equality \(w(n+3m)=1-w(n)\), together with (1), implies
\(w(\lfloor n/3\rfloor+m)=1-w(\lfloor n/3\rfloor)\).
As \(n\) ranges over \(3m\) consecutive positions, its quotients contain at least \(m\) consecutive integers, hence an antisquare of order \(m\) exists. Conversely, substitution of any antisquare \(u\overline u\) gives an antisquare \(\mu(u)\overline{\mu(u)}\) of order \(3m\) because \(\mu\) commutes with complementation. Thus order \(3m\) is possible exactly when order \(m\) is. The explicit factors \(01=w[1:3]\) and \(1001=w[2:6]\) witness orders \(1\) and \(2\). Induction and the preceding modulus-three obstruction prove assertion 1.

**Exact starts.** Write \(k=hL\), \(i=qL+r\) as in the theorem. Using (2), the antisquare condition is equivalent to
\[
w(Q+h)=1-w(Q)\quad\text{for every }Q=q,\ldots,q+h-1+\mathbf1_{r>0}.
\tag{3}
\]
For \(h=1\), this is \(c(q)=1\), with the additional condition \(c(q+1)=1\) when \(r>0\). For \(h=2\), examine the three possible residues of \(q\) in (3). By (1), when \(r=0\), residue \(0\) requires \(c(a)=1\), residue \(1\) is impossible, and residue \(2\) requires \(c(a)=0\), where \(q=3a+\text{residue}\). When \(r>0\), the additional comparison eliminates residues \(0\) and \(1\); residue \(2\) requires \(c(a)=0,c(a+1)=1\). The derivative identities
\[
c(3a)=0,\quad c(3a+1)=1,\quad c(3a+2)=1-c(a)
\tag{4}
\]
show that \(c(a)=0,c(a+1)=1\) holds exactly when \(a\equiv0\pmod3\), or equivalently \(q\equiv2\pmod9\). This proves assertion 2 without assuming any unverified recognizability theorem.

**Existence and values of densities.** Let \(C(N)=\sum_{a=0}^{N-1}c(a)\), \(D(N)=C(N)-N/2\). Summing (4) gives
\[
D(3m)=-D(m),\quad D(3m+1)=-D(m)-\tfrac12,\quad D(3m+2)=-D(m).
\tag{5}
\]
With \(D(0)=0\), repeated division by three yields \(|D(N)|\le (1+\lfloor\log_3 N\rfloor)/2\) for \(N\ge1\). Thus \(c\) has natural one-density \(1/2\). Equation (4) also shows that two successive ones of \(c\) occur precisely at positions \(3a+1\) with \(c(a)=0\), with natural density \(1/6\). Therefore the order-one tests in assertion 2 have respective densities \(1/2\) (when \(r=0\)) and \(1/6\) (when \(r>0\)). The two alternatives for \(h=2,r=0\) have combined density \((1/3)(1/2+1/2)=1/3\), while the congruence \(q\equiv2\pmod9\) has density \(1/9\). For fixed \(L=3^t\), each residue \(r\pmod L\) occupies \(1/L\) of positions \(i\), and \(q\) traverses consecutive integers. Hence
\[
\delta_L=L^{-1}(1/2)+(1-L^{-1})(1/6)=1/6+1/(3L)
\]
and
\[
\delta_{2L}=L^{-1}(1/3)+(1-L^{-1})(1/9)=1/9+2/(9L).
\]
For excluded orders there are no starts, by assertion 1. This completes the proof.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. The program constructs the fixed point and independently reconstructs its terms by ternary digit parity, then compares the exact starting-position criterion against direct factor comparisons at all \(4096\) starts and all orders \(1\) through \(512\) (\(2{,}097{,}152\) comparisons). It also checks the derivative recursion on \(2187\) ternary quotient values. All checks completed successfully. These are finite diagnostics, not a replacement for the unlimited-quantifier proof above.

## Relationship to prior work
Baranwal, Currie, Mol, Ochem, Rampersad, and Shallit [1] introduce antisquare order and analyze avoidance, critical exponents, and certain other binary words; they do not provide this exact order/occurrence/density classification for the Mephisto Waltz word. Meleshko, Ochem, Shallit, and Shan [2, §4.1] study this *same* fixed point but characterize pseudoperiodicity through the existence of one of several shifts matching each symbol, rather than complementary consecutive blocks at a single shift. Currie et al. [3] study avoidance of complementary factors appearing anywhere in a word, without requiring adjacency of those factors. OEIS A064990 [4] identifies the fixed point and its fourth-power avoidance, not its antisquare orders. In particular, the results from [2] and [3] do not directly imply the present starting-position formulas or densities.

## Limitations
The result concerns the specified binary fixed point and standard bitwise complementation, not arbitrary substitutions or more general antiperiodic words. The density limits fix \(k\) before sending \(N\) to infinity; no uniform two-parameter estimate is asserted. Independently checking literature not indexed by the consulted databases remains necessary before claiming universal priority. No independent scientific audit has been performed.

## References
[1] A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, and J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223, first public 2022-09-19. https://arxiv.org/abs/2209.09223

[2] J. Meleshko, P. Ochem, J. Shallit, and S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171, first public 2022-07-20. https://arxiv.org/abs/2207.10171

[3] J. Currie, Ľ. Dvořáková, P. Ochem, D. Opočenská, N. Rampersad, and J. Shallit, *Complement Avoidance in Binary Words*, arXiv:2209.09598, first public 2022-09-20. https://arxiv.org/abs/2209.09598

[4] The On-Line Encyclopedia of Integer Sequences, A064990, *Mephisto Waltz sequence*. https://oeis.org/A064990
