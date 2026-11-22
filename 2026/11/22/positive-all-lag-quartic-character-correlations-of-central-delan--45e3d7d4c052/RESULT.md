# Positive all-lag quartic-character correlations of central Delannoy numbers modulo five

## Finding

Let the central Delannoy numbers be \(D_n=\sum_{j=0}^{n}\binom{n}{j}^{2}2^j\), for every integer \(n\ge0\). Define the quartic character \(\chi:\mathbb F_5^\times\to\{1,i,-1,-i\}\) by \(\chi(3)=i\), and put \(u_n=\chi(D_n\bmod5)\). All terms are units modulo five. For every integer shift \(h\ge0\), the correlation
\[
 C(h)=\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}u_{n+h}\overline{u_n}
\]
exists, is real and rational, and is computable by the following complete recursion for every \(a\ge0\):
\[
\begin{aligned}
C(0)&=1,\qquad C(1)=\tfrac12,\\
C(5a)&=C(a),\\
C(5a+1)&=\frac{2C(a)+C(a+1)}5,\\
C(5a+2)&=\frac{C(a)}5,\\
C(5a+3)&=\frac{C(a+1)}5,\\
C(5a+4)&=\frac{C(a)+2C(a+1)}5.
\end{aligned}
\]
The formula for \(C(5a)\) at \(a=0\) is a consistent identity; the formula for \(C(5a+1)\) at \(a=0\) uniquely forces the displayed value of \(C(1)\). For all positive shifts \(h\),
\[
 0<C(h)\le\tfrac12,
 \qquad C(h)=\tfrac12\quad\Longleftrightarrow\quad h=5^j\text{ for an integer }j\ge0.
\]
The infimum of \(C(h)\) for positive \(h\) is zero and is not attained; in fact \(C((5^r-1)/2)=5^{-r}\) for every integer \(r\ge1\). All complete quintary lag sums are
\[
 \sum_{h=0}^{5^r-1}C(h)=\tfrac14+\tfrac34\left(\tfrac{13}{5}\right)^r\qquad(r\ge0).
\]
For fixed \(h\) and any \(N\ge1\), the defining finite sum is \(NC(h)+O_h(\log(2N))\). The four unit residue values of \(D_n\bmod5\) each have natural density \(1/4\). The stationary spectral measure determined by \(C\) has no atoms, although \(C(5^j)=1/2\) for all \(j\ge0\).

## Assumptions and scope

All indices and shifts are nonnegative integers; the modulus is the prime five; \(\overline{z}\) denotes complex conjugation. The Dirichlet character is normalized on the generator three, so \(\chi(3^j)=i^j\). Correlations are taken over ordinary increasing integer intervals, not cyclicly wrapped finite intervals. The term spectral measure denotes the unique finite positive measure on the circle whose Fourier coefficients are the positive-definite correlation sequence, as supplied by the Herglotz theorem. The theorem does not assert absolute continuity or determine the spectral measure's dimension.

## Proof

**1. Exact digit form.** Lucas' congruence applied termwise to \(D_n=\sum_j\binom nj^2 2^j\) yields \(D_n\equiv\prod_{t\ge0}D_{n_t}\pmod5\), where \(n_t\in\{0,1,2,3,4\}\) are the base-five digits. Direct calculation gives \((D_0,D_1,D_2,D_3,D_4)\equiv(1,3,3,3,1)\pmod5\). In particular no \(D_n\) vanishes modulo five. With \(w=(1,i,i,i,1)\), this becomes \(u_n=\prod_t w_{n_t}\). Define \(s(n)=\#\{t:n_t\in\{1,2,3\}\}\); then \(u_n=i^{s(n)}\), and \(u_{5m+d}=u_mw_d\) for \(0\le d\le4\).

**2. Existence and cutoff error.** Fix \(h\ge0\). Let \(A_r(h)=\sum_{0\le n<5^r}u_{n+h}\overline{u_n}\). For any aligned block \(I=[b5^r,(b+1)5^r)\), the summand at offset \(t\) equals the one in \(A_r(h)\) whenever \(0\le t<5^r-h\), because both indices share the same high digit block and the high-digit phases cancel. At most \(h\) terms can differ, each by complex magnitude at most two, so any aligned block sum differs from \(A_r(h)\) by at most \(2h\) (also valid if \(h\ge5^r\)). Partitioning \([0,5^s)\) into aligned blocks of length \(5^r\) for \(s\ge r\) proves \(|A_s(h)/5^s-A_r(h)/5^r|\le2h/5^r\). Thus \(C(h)=\lim_r A_r(h)/5^r\) exists and \(|A_r(h)-5^rC(h)|\le2h\). Every aligned block has discrepancy at most \(4h\) from its length times \(C(h)\). Greedy base-five decomposition of an arbitrary initial interval \([0,N)\) into at most four aligned blocks of each size \(5^r\) proves the claimed \(O_h(\log(2N))\) bound. This is an ordinary natural-density limit and not just a subsequence limit.

**3. Exact correlation recursion.** Split each index as \(n=5m+d\) and each shift as \(h=5a+r\). If \(d+r<5\), the factor of the summand depending on its final digit is \(w_{d+r}\overline{w_d}\), multiplying a quotient-level lag \(a\) term; otherwise it is \(w_{d+r-5}\overline{w_d}\), multiplying a lag \(a+1\) term. Asymptotic densities of each final digit are \(1/5\), by step 2. The corresponding sums of noncarry and carry digit factors for \(r=0,1,2,3,4\) are, respectively, \((5,0),(2,1),(1,0),(0,1),(1,2)\). These ordered pairs immediately give the five recursion branches. At \(h=1\), the self-reference \(C(1)=(2C(0)+C(1))/5\), with \(C(0)=1\), yields \(C(1)=1/2\). The recursion is therefore inductively evaluable: for \(h\ge2\), all nonzero arguments on the right are smaller than \(h\).

**4. Positivity and exact maxima.** The initial nonmultiples of five have \(C(1)=1/2\), \(C(2)=1/5\), \(C(3)=1/10\), and \(C(4)=2/5\). On removing factors of five, every remaining recursion branch is a strictly positive linear combination of earlier positive values. Thus \(C(h)>0\) for all positive \(h\). For any \(a\ge1\), every right-hand lag in a nonzero-remainder branch is positive; by induction they are at most \(1/2\). The branch coefficient sum is at most \(3/5\), hence \(C(5a+r)\le3/10<1/2\) for \(1\le r\le4\). The unique positive nonmultiple attaining \(1/2\) is therefore \(1\). The zero-remainder identity \(C(5a)=C(a)\) gives precisely the shifts \(5^j\). For \(h_r=(5^r-1)/2\), each of its \(r\) base-five digits equals two, whence the \(r\) applications of the third branch yield \(C(h_r)=5^{-r}\). No positive shift has zero correlation.

**5. Lag sums.** Write \(S_r=\sum_{h<5^r}C(h)\). The five branch coefficients sum to \((9/5)C(a)+(4/5)C(a+1)\). Because \(C(5^r)=C(1)=1/2\), summation over \(a<5^r\) gives \(S_{r+1}=(13/5)S_r-2/5\), with \(S_0=1\). Solving this first-order recurrence gives the claimed formula.

**6. Marginals and spectral consequence.** The mean of \(u_n^j\) over exactly \(5^r\) indices is \(((2+3i^j)/5)^r\) for each \(j=1,2,3\); these tend to zero because all three complex moduli are strictly less than one. More precisely, on any aligned block of length \(5^r\), the sum of \(u_n^j\) is the high-digit phase times \((2+3i^j)^r\). Decomposing arbitrary prefixes into at most four aligned blocks at each quintary scale bounds their total absolute sum by \(O(N^{\log_5\sqrt{13}})\) for \(j=1,3\) and by \(O(\log(2N))\) for \(j=2\). Hence the ordinary mean tends to zero. Fourier inversion on the four-element group proves frequency \(1/4\) for each of the four residues. Positive definiteness of the correlation sequence follows by taking limits of nonnegative finite quadratic forms, so it has a positive spectral measure. For \(0\le h<5^r\) we have \(|C(h)|^2\le C(h)\), and hence \(5^{-r}\sum_{0\le h<5^r}|C(h)|^2\le (1/4)5^{-r}+(3/4)(13/25)^r\to0\). The same conclusion for arbitrary cutoffs follows by comparison with the next power of five; negative Fourier indices are conjugate. The classical Wiener criterion therefore shows the spectral measure has no point masses. The fixed value \(C(5^j)=1/2\) shows its coefficients do not tend to zero.

## Verification

The self-contained standard-library Python program `check.py` evaluates both sides of the Delannoy congruence on 190 indices and checks the exact recurrence's positivity and equality characterization at 4,999 positive shifts. It verifies the lag-sum identity and the tiny-correlation shift family through seven powers, as well as full initial-block complex correlations at 5-adic sizes through \(5^5\). It reports **10,792 exact assertions passed**. These finite computations are checks on arithmetic implementation, not substitutes for the infinite proof in the preceding section. Reproduce using `python3 check.py`.

## Relationship to prior work

The scalar central-Delannoy Lucas congruence itself is classical and explicitly recorded in Pan's 2015 full-text paper, Equation (1.6), where it is credited to earlier congruence work. Eu, Liu and Yeh's 2005 publicly dated work studies Lucas-theorem congruences for combinatorial sequences including central Delannoy numbers. Rowland and Yassawi's 2013 full-text paper develops general finite-automata machinery for congruences of rational diagonals. The present claim is **not** the Lucas congruence or general automaticity, but the evaluated all-shift quartic-character correlation, its strictly positive rational recursion, sharp maximizers, complete lag-sum law, and continuous/nondecaying spectral behavior. A nearby indexed result on central *trinomial* residues modulo five has a different digit kernel and does not by itself imply the evaluated Delannoy formulas. Related general correlation machinery could subsume these formulas if a sufficiently strong explicitly applicable theorem is located; that historical-priority possibility is not ruled out.

## Limitations

The theorem is only for modulus five and the specified quartic character, not a universal statement about all Delannoy residues or prime moduli. Its correlations measure normalized complex character products, not the full sixteen-entry joint distribution of raw residues. The archival Eu–Liu–Yeh article was accessible by its abstract and bibliographic information but not by its full text; a possible stronger statement in inaccessible or unlocated historical literature remains a residual originality risk. The proof yields a continuous spectral measure but neither absolute continuity nor singular continuity is established. No external mathematical validation has been performed.

## References

1. S.-P. Eu, S.-C. Liu, and Y.-N. Yeh, *On the Congruences of Some Combinatorial Numbers*, Studies in Applied Mathematics **116** (2006), 135–144; first publicly available 20 December 2005. DOI: https://doi.org/10.1111/j.1467-9590.2006.00337.x (public abstract and bibliography inspected; full text unavailable).
2. H. Pan, *A Lucas-type congruence for \(q\)-Delannoy numbers*, arXiv:1508.02046, 9 August 2015, Sections 1–3; scalar Lucas congruence displayed as Equation (1.6). https://arxiv.org/html/1508.02046v1 (full text inspected).
3. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635, 31 October 2013, Sections 1 and 2 and later examples. https://arxiv.org/html/1310.8635v2 (full text inspected).
4. OEIS A001850, *Central Delannoy numbers*, https://oeis.org/A001850 (sequence definition and values).
