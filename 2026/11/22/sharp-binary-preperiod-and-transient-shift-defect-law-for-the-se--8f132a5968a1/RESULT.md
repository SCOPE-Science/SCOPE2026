# Sharp binary preperiod and transient shift-defect law for the seventh Stirling column

## Finding
Let \(S(n,7)\) be the number of partitions of an \(n\)-element set into seven nonempty blocks, with \(n\ge7\). For every integer \(k\ge1\), put
\[
P_k=2^{k+1},\qquad N_k=\max\{7,\,k+2+(k\bmod 2)\},\qquad \Delta_k(n)=S(n+P_k,7)-S(n,7).
\]
Then \(P_k\) is the **least eventual period** modulo \(2^k\), and \(N_k\) is the **least starting index** of a \(P_k\)-periodic tail: \(\Delta_k(n)\equiv0\pmod{2^k}\) for every \(n\ge N_k\), and when \(N_k>7\) the congruence fails at \(n=N_k-1\).

Moreover, all the dyadic shift-defect valuations outside two possible resonance indices are exact. For every \(n\ge7\),
\[
\nu_2(\Delta_k(n))=
\begin{cases}
\min\{k,n-3\},&n\text{ odd and }n\ne k+3,\\
\min\{k+2,n-2\},&n\text{ even and }n\ne k+4.
\end{cases}
\]
At the possible resonances, \(\nu_2(\Delta_k(k+3))\ge k+1\) if \(k+3\ge7\) is odd, and \(\nu_2(\Delta_k(k+4))\ge k+3\) if \(k+4\ge7\) is even. In particular, when \(k\) is odd the exact two-scale formula has no exceptions.

## Assumptions and scope
Only positive integers \(k\ge1\) and actual combinatorial indices \(n\ge7\) are included. The two-adic valuation of any nonzero integer is \(\nu_2(m)=\max\{e\ge0:2^e\mid m\}\). The differences in the theorem are nonzero because \(S(n,7)\) is strictly increasing for \(n\ge7\). The least starting index is relative to the natural domain \(n\ge7\). No claim is made that the exact valuations at the two exceptional resonance inputs equal their displayed lower bounds.

## Proof
Write the inclusion-exclusion identity
\[
5040S(n,7)=7^n-7\cdot6^n+21\cdot5^n-35\cdot4^n+35\cdot3^n-21\cdot2^n+7.
\]
Define the odd-base interpolation and the even-base remainder
\[
H(n)=\frac{7^n+21\cdot5^n+35\cdot3^n+7}{5040},\qquad
R(n)=-\frac{7\cdot2^n(3^n+3+5\cdot2^n)}{5040}.
\]
Thus \(S(n,7)=H(n)+R(n)\) for every integer \(n\ge7\). All expressions in the following argument are interpreted in \(\mathbb Q_2\).

**Parity-branch distance lemma.** For \(t\in\mathbb Z_2\) put \(E(t)=H(2t)\) and \(O(t)=H(2t+1)\). Their convergent Mahler expansions are
\[
E(t)=\frac4{315}+\sum_{j\ge1}a_j\binom tj,\quad
O(t)=\frac2{45}+\sum_{j\ge1}b_j\binom tj,
\]
where
\[
a_j=\frac{48^j+21\cdot24^j+35\cdot8^j}{5040},\quad
b_j=\frac{7\cdot48^j+105\cdot24^j+105\cdot8^j}{5040}.
\]
Here \(a_1=52/315\), \(b_1=11/15\), \(a_2=208/63\) and \(b_2=248/15\). Their valuations are respectively \(2,0,4,3\). For \(j\ge3\), all numerator summands are divisible by \(2^{3j}\), so \(\nu_2(a_j),\nu_2(b_j)\ge3j-4\).

For distinct nonnegative integers \(s,t\), set \(d=s-t\). Vandermonde's identity and \(\binom di=(d/i)\binom{d-1}{i-1}\) give
\[
\nu_2\!\left(\binom sj-\binom tj\right)\ge\nu_2(d)-\lfloor\log_2j\rfloor.
\]
The same holds for \(\mathbb Z_2\) inputs by continuity. For \(j\ge2\), the nonlinear terms of \(E(s)-E(t)\) have valuation at least \(\nu_2(d)+3\), while those of \(O(s)-O(t)\) have valuation at least \(\nu_2(d)+2\). The linear terms cannot cancel. Therefore
\[
\boxed{\nu_2(E(s)-E(t))=\nu_2(s-t)+2,\quad
\nu_2(O(s)-O(t))=\nu_2(s-t)}.
\]
The expansions also show \(E(t),O(t)\in\mathbb Z_2\). Consequently, \(O\) is a bijective isometry of \(\mathbb Z_2\), while \(E\) is a bijection from \(\mathbb Z_2\) onto \(4\mathbb Z_2\) with scale factor four. In particular, shifting the original input \(n\) by \(P_k=2^{k+1}\) shifts its parity-branch variable by \(2^k\), and
\[
\nu_2(H(n+P_k)-H(n))=\begin{cases}k,&n\text{ odd},\\k+2,&n\text{ even}.\end{cases}
\]

**Transient remainder.** For every odd integer \(n\ge7\), \(3^n+3+5\cdot2^n\) has valuation one, since \(3^{n-1}+1\equiv2\pmod8\). For every even integer \(n\ge8\), this parenthesis has valuation two, since \(\nu_2(3^{n-1}+1)=2\) for odd \(n-1\). As \(5040=16\cdot315\),
\[
\nu_2(R(n))=\begin{cases}n-3,&n\text{ odd},\\n-2,&n\text{ even}.\end{cases}
\]
The valuation of \(R(n+P_k)\) is strictly larger than each of the two competing valuations \(\nu_2(H(n+P_k)-H(n))\) and \(\nu_2(R(n))\). Hence ultrametric comparison gives the exact minimum whenever those two valuations differ. When they agree, cancellation guarantees at least one extra power of two, proving the stated resonance bounds and the complete nonresonant defect law.

**Sharp periodic tail.** Every \(n\ge N_k\) satisfies \(\nu_2(R(n))\ge k\). The parity-branch distance lemma gives \(H(n+P_k)\equiv H(n)\pmod{2^k}\), so the same congruence holds for \(S\). If \(N_k>7\), its predecessor \(N_k-1\) is odd and \(\nu_2(R(N_k-1))=N_k-4<k\); the odd-branch shift has valuation exactly \(k\), so the congruence fails there. Thus \(N_k\) is the sharp start.

Finally, the eventual period cannot be odd: the even-input odd-base interpolation lies entirely in \(4\mathbb Z_2\), whereas the odd-input interpolation is surjective modulo every \(2^k\). Any even period \(2d\) must preserve the odd parity branch; its distance law requires \(2^k\mid d\). Thus every eventual period is divisible by \(P_k\), establishing least period without extrapolating from finite experiments.

## Verification
A standalone Python 3 standard-library checker, `verify_stirling7.py`, verifies the inclusion-exclusion coefficients, the exact least periods and sharp starts for \(1\le k\le11\), the complete residue histograms in one full block, and the valuation law for finite sample indices including the resonances. It uses the independent Stirling recurrence and a separate modular inclusion-exclusion implementation of the differences. Its finite range is not an infinite proof. The proof above supplies the all-depth arguments.

## Relationship to prior work
Kwong (1989) proves the least eventual periods of fixed Stirling columns modulo prime powers; his binary formula yields \(2^{k+1}\) for the seventh column, but does not state its least tail onset. Bennett and Mosteig (2013), especially Section 6.2, identify the parity split of stable \(2\)-adic valuation classes for \(S(n,7)\) and prove the Amdeberhan–Manna–Moll conjecture in this case. Their even/odd class results imply corresponding stable branch regularity; the parity decomposition itself and eventual minimal period are not claimed as new. The present claim is the explicit complete transient **index-by-index shift-defect valuation law outside its stated resonance inputs** together with the sharp all-depth starting index. Zhao–Hong–Zhao (2014) give difference valuations for fixed-column indices not of Mersenne form; their stated general difference theorem excludes the seventh column. No source inspected established this sharp transient law as a previously stated or stronger implied result.

## Limitations
Two isolated resonance indices for even \(k\) have only strict lower bounds here. The proof does not classify their sometimes much larger valuations. A full historical priority check of all pre-electronic Stirling literature is not possible; in particular, the full publisher text of Zhao–Hong–Zhao could not be inspected, although its accessible theorem statement excludes the Mersenne case. The source comparison is a best-knowledge originality assessment, not a proof of historical uniqueness. The checker is finite and does not constitute independent mathematical validation.

## References
- C. Bennett and E. Mosteig, *Congruence Classes of 2-adic Valuations of Stirling Numbers of the Second Kind*, Journal of Integer Sequences **16** (2013), Article 13.3.6, publicly posted March 2, 2013. https://cs.uwaterloo.ca/journals/JIS/VOL16/Mosteig/mosteig4.pdf
- Y. H. Harris Kwong, *Minimum Periods of S(n,k) Modulo M*, Fibonacci Quarterly **27** (1989), 217–221. https://www.fq.math.ca/Scanned/27-3/kwong.pdf
- J. Zhao, S. Hong, W. Zhao, *Divisibility by 2 of Stirling numbers of the second kind and their differences*, Journal of Number Theory (2014), DOI:10.1016/j.jnt.2014.01.005. https://doi.org/10.1016/j.jnt.2014.01.005
