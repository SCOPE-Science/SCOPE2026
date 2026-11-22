# First post-range representation thresholds for three-term arithmetic progressions

## Finding

For each integer \(a\ge3\) and each integer \(d\ge3\) with \(\gcd(a,d)=1\), let \(R(N)\) be the number of triples \((x,y,z)\in\mathbb Z_{\ge0}^3\) satisfying
\[
a x+(a+d)y+(a+2d)z=N.
\]
Fix \(p=\lfloor a/2\rfloor+1\). The minimum nonnegative integer in each residue class modulo \(a\) having **more than** \(p\) representations is exactly one of the \(a\) integers
\[
M_t=\begin{cases}
a(a+d)+dt,&a\text{ odd},\\
a(a+d+(t\bmod2))+dt,&a\text{ even},
\end{cases}\qquad 0\le t<a.
\]
In particular, these integers form the complete \(p\)-Apéry set, with \(R(M_t)=p+1\) and \(R(M_t-a)=p\) for every \(t\). Thus the largest integer with at most \(p\) representations and the number of such nonnegative integers are, respectively,
\[
g_p=\begin{cases}
a(a-1)+(2a-1)d,&a\text{ odd},\\
a^2+(2a-1)d,&a\text{ even},
\end{cases}
\]
and
\[
n_p=a(a+d)+\frac{(a-1)(d-1)}2+\begin{cases}0,&a\text{ odd},\\a/2,&a\text{ even}.\end{cases}
\]
The displayed genus expression is integral because \(\gcd(a,d)=1\).

For example, the published triple \(\{11,15,19\}\) has \(p=6\) at the first level beyond the previously calculated \(p=5\) case: the new formulas give \(g_6=194\) and \(n_6=180\). For \(\{6,11,16\}\), the first post-range level \(p=4\) has \(g_4=91\) and \(n_4=79\).

## Assumptions and scope

All representations are ordered coefficient triples of **nonnegative** integers; the generators are distinguished and fixed. The multiplicity threshold \(p\) depends on \(a\). The parameter range \(a\ge3, d\ge3,\gcd(a,d)=1\) excludes the consecutive and consecutive-odd special cases, and includes infinitely many coprime arithmetic progressions. A residue class with representative \(dt\bmod a\) is indexed by the unique \(0\le t<a\). An integer with at most \(p\) representations is counted in \(n_p\), including zero. No statement is asserted for other thresholds or for noncoprime generators.

## Proof

1. Put \(u=x+y+z\) and \(v=y+2z\). Then the represented integer is \(N=au+dv\). For fixed nonnegative \(u,v\), the possible \(z\) satisfy \(\max(0,v-u)\le z\le\lfloor v/2\rfloor\). Hence their exact number is
\[
H(u,v)=\begin{cases}
1+\left\lfloor\min(v,2u-v)/2\right\rfloor,&u\ge0,\ 0\le v\le2u,\\
0,&\text{otherwise}.
\end{cases}
\]
2. Since \(\gcd(a,d)=1\), every integer in the residue class \(dt\pmod a\) has a unique description \(N=as+dt\), with \(s\in\mathbb Z\) and \(0\le t<a\). Each representation has \(v=t+a\ell\), \(u=s-d\ell\) for some \(\ell\ge0\). Consequently,
\[
R(as+dt)=\sum_{\ell\ge0}H(s-d\ell,t+a\ell).
\]
3. Evaluate at \(s=a+d+k\), where \(k=-1,0\) and, in the even-\(a\), odd-\(t\) case only, also \(k=1\). In every such case \(\ell\ge2\) cannot contribute: the necessary inequality \(2(s-d\ell)\ge t+a\ell\) would imply \(2a+2d+2\ge2a+4d+t\), impossible for \(d\ge3\). The \(\ell=0\) contribution is \(1+\lfloor t/2\rfloor\). For \(\ell=1\), direct substitution gives
\[
1+\left\lfloor\frac{a+2k-t}{2}\right\rfloor,
\]
where zero is allowed at the boundary. Thus, at these points,
\[
R(a(a+d+k)+dt)=2+\left\lfloor\frac t2\right\rfloor+\left\lfloor\frac{a+2k-t}{2}\right\rfloor.
\]
4. If \(a=2h+1\), taking \(k=0\) gives \(h+2=p+1\) at every \(t\), whereas \(k=-1\) gives \(h+1=p\). If \(a=2h\), taking \(k=0\) gives \(h+2=p+1\) for even \(t\) and \(h+1=p\) for odd \(t\). For even \(t\), \(k=-1\) gives \(h+1=p\). For odd \(t\), \(k=1\) gives \(h+2=p+1\). These are precisely the stated \(M_t\) and immediate predecessors modulo \(a\).
5. Adding one copy of generator \(a\) injects the representations of \(N\) into those of \(N+a\), so \(R(N+a)\ge R(N)\). Each \(M_t\) is therefore the **first** point in its residue class with more than \(p\) representations. Distinct \(t\) give distinct residues because \(d\) is invertible modulo \(a\).
6. The greatest exceptional number is \(\max_t(M_t-a)\). Both parity cases attain the maximum at \(t=a-1\); substitution gives the displayed \(g_p\). In a residue class whose first accepted value is \(M_t\), exactly \((M_t-r_t)/a\) nonnegative values are below it, where \(r_t\) is its least residue modulo \(a\). Summing, using \(\sum_t r_t=a(a-1)/2\), gives
\[
n_p=\frac1a\sum_{t=0}^{a-1}M_t-\frac{a-1}{2}.
\]
There are \(a/2\) odd indices \(t\) when \(a\) is even; evaluating this sum proves the displayed expression.

## Verification

The standalone `CHECKER.py` computes every denumerant exactly by unbounded-coin dynamic programming, independently of the proof's \((u,v)\) decomposition. It verifies all residue thresholds, representation counts on both sides, greatest excluded integers, and total excluded counts for all 1,260 coprime parameter pairs with \(3\le a\le121\) and \(3\le d\le19\): 78,178 distinct threshold residues, and 1,020 direct tests of the two-variable coefficient-count lemma. Execute `python3 CHECKER.py`. This is a finite regression test and not a substitute for the universal argument.

## Relationship to prior work

Komatsu and Ying's original preprint (27 June 2022; published in 2023) proves the general three-term arithmetic-progression formulas only for \(0\le p\le\lfloor a/2\rfloor\), and explicitly poses the higher-threshold problem. The present exact residue-by-residue result treats its **first excluded level** and supplies both the Frobenius and genus formulas for every coprime step \(d\ge3\). An independently indexed 2026 classification addresses the special step \(d=1\) at many thresholds; that specialization is not claimed as new. A 2026 paper on long consecutive-odd generator families studies a different, variable-length generating set and does not establish the present three-generator, all-step result. Standard generalized Apéry identities are used with credit; novelty is asserted only for the explicit first-post-range arithmetic classification.

## Limitations

No formula for thresholds larger than \(\lfloor a/2\rfloor+1\) is proved. This is a self-contained proof, not independent mathematical certification. Although inspected literature and semantically indexed claims did not establish equivalent or stronger coverage of the claimed parameter range, unindexed or implicit equivalents remain possible; full text of one related online classification was unavailable and only its indexed statement could be compared.

## References

1. T. Komatsu and H. Ying, *The \(p\)-Numerical Semigroup of the Triple of Arithmetic Progressions*, arXiv:2206.13052 (first posted 2022-06-27), *Symmetry* **15** (2023), 1328, doi:10.3390/sym15071328. Full open-access article: https://www.mdpi.com/2073-8994/15/7/1328.
2. D. Haji Mohammed, *Generalised Frobenius numbers: geometry of upper bounds, Frobenius graphs and exact formulas for arithmetic sequences*, Cardiff University PhD thesis (2017), https://orca.cardiff.ac.uk/id/eprint/98161/1/Final%20Thesis.pdf.
3. T. Komatsu, S. Hyun and K. Song, *\(p\)-numerical semigroup of the sequence of consecutive odd integers*, arXiv:2608.14053 (2026-08-14); comparison concerns its long consecutive-odd families, not the present three-term result.
4. *Three exact phases of generalized Frobenius numbers for three consecutive denominations* (2026), published indexed summary at https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-three-exact-phases-of-generalized-frobenius-numbers-for-three-co--6dc430dbb315; specializes to step \(d=1\), excluded from the present claim.
