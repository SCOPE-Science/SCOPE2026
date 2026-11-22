# Exact metameric-class census for ordered binary local histograms

## Finding
Fix integers \(n\ge h\ge2\). For each binary word \(x=(x_1,\ldots,x_n)\), observe the **ordered**, exact integer vector of all unit-stride length-\(h\) local weights
\[
\mathcal R_h(x)=(s_1,\ldots,s_{n-h+1}),\qquad s_i=\sum_{j=i}^{i+h-1}x_j.
\]
Two words are *metameric* when their read vectors coincide. Write \(n=qh+r\), with \(q\ge1\), \(0\le r<h\). For each residue-column index \(j\in\{1,\ldots,h\}\), put \(\ell_j=q+1\) if \(j\le r\) and \(\ell_j=q\) otherwise, and set \(a_j=2^{\ell_j}-1\), \(b_j=2^{\ell_j}-2\).

**Complete inverse fibers.** Split \(x\) into the \(h\) indexed subsequences \((x_j,x_{j+h},x_{j+2h},\ldots)\). Call a column *mixed* if it contains both symbols, and *pure* if all of its entries agree. The read vector determines every mixed column (including its individual bits), which columns are pure, and the **number** \(t\) of pure columns equal to one. These data conversely determine the read vector. If there are \(p\) pure columns, its inverse fiber has exactly \(\binom pt\) words: each assignment of exactly \(t\) all-one columns among the \(p\) pure columns is possible. In particular, the number of read vectors with exactly \(k\ge1\) preimages is
\[
F_{n,h}(k)=\sum_{P\subseteq\{1,\ldots,h\}}
\left(\prod_{j\notin P}b_j\right)
\sum_{t=0}^{|P|}\mathbf1_{\{\binom{|P|}{t}=k\}},
\]
where \(P\) is the set of pure columns and an empty product is one.

**Exact census.** The total number \(R_{n,h}\) of attainable read vectors, the number \(U_{n,h}\) of uniquely reconstructed source words, and the number \(K_{n,h}\) of non-singleton metameric classes satisfy
\[
\boxed{R_{n,h}=\prod_{j=1}^h a_j+\sum_{j=1}^h\prod_{i\ne j}a_i,}\qquad
\boxed{U_{n,h}=2\prod_{j=1}^h a_j-\prod_{j=1}^h b_j,}
\]
\[
\boxed{K_{n,h}=R_{n,h}-U_{n,h}.}
\]
Every formula is exact, including \(n=h\) and \(h=2\); for example \(K_{n,2}=1\), \(K_{h,h}=h-1\), and \(K_{h+1,h}=3h-5\) for \(h\ge2\). The largest fiber is exactly \(\binom h{\lfloor h/2\rfloor}\); it occurs for one read vector when \(h\) is even and two when \(h\) is odd. The maximum size of a zero-error code distinguished by this read vector is precisely \(R_{n,h}\).

## Assumptions and scope
The input alphabet is \(\{0,1\}\), the source length and window width are known, **every** one of the \(n-h+1\) overlapping linear windows is observed in its correct position, and weights are exact integer sums. There is no circular wrapping, truncation, noise, erasure or reordering. A *metameric class* here means one equivalence class containing at least two words, not the number of words in such a class. A singleton fiber contributes one uniquely reconstructed word. The source coordinates are indexed, not taken modulo reversal or rotation.

## Proof
**1. Kernel of the read map.** Let \(x,y\in\{0,1\}^n\), and define the integer differences \(d_i=y_i-x_i\). The successive read differences obey
\[
s_{i+1}(x)-s_i(x)=x_{i+h}-x_i\quad(1\le i\le n-h).
\]
Consequently \(\mathcal R_h(x)=\mathcal R_h(y)\) **if and only if**
\[
d_{i+h}=d_i\quad(1\le i\le n-h),\qquad\sum_{j=1}^h d_j=0.
\]
Necessity comes from subtraction; sufficiency follows because the first read sums coincide and their successive differences coincide. Thus \(d\) is constant on every indexed residue column modulo \(h\).

**2. Binary rigidity and fiber size.** If a column of \(x\) contains both zero and one, adding the same integer to all its positions and retaining binary entries forces this integer to be zero. If it is pure zero, the only allowed increments are zero and one; if it is pure one, they are zero and minus one. Therefore all mixed columns are fixed, whereas every pure column can be assigned all zeros or all ones. The sum constraint is exactly conservation of the number \(t\) of all-one pure columns. Hence there are \(\binom pt\) indistinguishable sources when \(p\) columns are pure.

For the converse statement about recovered data, the read differences specify each column's consecutive bit differences. A nonconstant binary column is uniquely determined by these differences, since two columns with the same differences differ by a constant and a nonconstant binary column admits no nonzero constant shift. A zero-difference column is pure. After recovering all mixed columns, the first window weight fixes the number \(t\) of pure all-one columns. Thus the data listed in the finding characterize the read vector without redundancy.

**3. Enumeration.** In column \(j\) there are exactly \(b_j=2^{\ell_j}-2\) mixed binary patterns. Fix the set \(P\) of pure columns. The mixed patterns admit \(\prod_{j\notin P}b_j\) choices, and each choice yields one different read vector for every integer \(0\le t\le|P|\). This proves the formula for \(F_{n,h}(k)\). Summing over fiber sizes gives
\[
R_{n,h}=\sum_{P\subseteq[h]}(|P|+1)\prod_{j\notin P}b_j.
\]
The generating polynomial identity
\[
\prod_{j=1}^h(b_j+z)=\sum_{P\subseteq[h]}z^{|P|}\prod_{j\notin P}b_j
\]
shows that evaluation at \(z=1\), plus its derivative at \(z=1\), gives \(R_{n,h}=\prod_j(b_j+1)+\sum_j\prod_{i\ne j}(b_i+1)\). A fiber is singleton when \(p=0\), or when \(p\ge1\) and \(t\) is zero or \(p\). Hence
\[
U_{n,h}=2\sum_{P\subseteq[h]}\prod_{j\notin P}b_j-\prod_{j=1}^h b_j
=2\prod_{j=1}^h(b_j+1)-\prod_{j=1}^h b_j,
\]
where the all-mixed case is counted only once. Subtracting gives \(K_{n,h}\). These expressions hold when some \(b_j=0\) as well.

**4. Sharp maximum and coding interpretation.** Since \(p\le h\), each fiber has size at most \(\binom h{\lfloor h/2\rfloor}\). Taking every column pure and choosing \(t\) central attains the bound; for \(h\ge2\) a strictly smaller number of pure columns cannot attain it. When every column is pure the read vector is constant with value \(t\), proving the one-or-two extremizer count. A zero-error code has at most one word in each fiber; choosing, for example, the lexicographically least word from every fiber attains exactly \(R_{n,h}\) codewords.

## Verification
The included `verify.py` independently groups all \(2^n\) binary words by the directly computed ordered local-weight vector for each \(1\le h\le n\le15\). It compares the **entire fiber-size histogram**, total output count, singleton count, non-singleton count and sharp maximum against two separate exact formulas. It also checks total source-mass conservation and five large integer parameter cases. Recorded command and output:

```text
python3 verify.py
VERIFY_OK parameter_pairs= 120 enumerated_input_instances= 917506 distinct_profiles= 409268 nonsingleton_fibers= 51436 range=1<=width<=n<=15
LARGE_PARAMETER_IDENTITY_OK 5
```

For \(n=6,h=3\) the formulas give \(R_{6,3}=54\), \(U_{6,3}=46\), \(K_{6,3}=8\), and the complete fiber census comprises 46 singleton fibers, 6 doubletons and 2 tripletons. These checks provide finite corroboration; the universal proof is the residue-column argument above.

## Relationship to prior work
Sporring and Darkner (2022), *Reconstructing Binary Signals from Local Histograms*, study exactly the ordered, densely overlapping binary local-histogram model. They prove the special counts \(K_{n,2}=1\), \(K_{h,h}=h-1\), and \(K_{h+1,h}=3h-5\), give a reconstruction algorithm and explicitly state in Section 4.4 that a closed form for general \(K_{n,h}\) remained unavailable. The formulas above resolve that exact finite counting question, sharpen it to the complete fiber distribution, and include their boundary formulas.

Sporring and Darkner (2022), *An algebra for local histograms*, develop a general partition and recursive reconstruction framework but do not state this closed all-parameter linear-window census. Yerushalmi, Etzion and Yaakobi (2024), *The Capacity of the Weighted Read Channel*, treat asymptotic capacity and shift-size variants; they do not give these finite length/unit-stride fiber laws.

A published theorem titled *Exact fiber and constant-weight capacity laws for cyclic binary weighted reads* has a closely related pure/mixed residue-class argument and a binomial fiber law for **all cyclic wraparound reads**. Its read operator and residue decomposition are different: it has \(\gcd(n,h)\) equal-length cyclic classes, while the present **nonwrapping linear** operator has \(h\) classes of lengths \(q\) or \(q+1\). When \(h\mid n\), the two exact output-count formulas agree; when \(h\nmid n\), its cyclic statement does not imply the mixed-length formula here. The shared underlying rigidity mechanism is acknowledged and is not claimed as independently new. Identical-looking parameters in the two read operators should not be confused.

## Limitations
The classification is binary and assumes complete **ordered** noiseless observations. Unordered composition multisets, cyclic wrapping, higher alphabets and missing or noisy local sums are outside its scope. Exact global novelty cannot be certified by a finite literature search; an unindexed equivalent characterization or a routine derivation from older histogram algebra may exist. The finite checker is not a substitute for a mathematical proof or independent audit. A broader finite-alphabet extension and error-tolerant decoding are not established here.

## References
1. J. Sporring and S. Darkner, *Reconstructing Binary Signals from Local Histograms*, Entropy 24(3), 433 (first verified public online date: 2022-03-21), DOI:10.3390/e24030433, https://www.mdpi.com/1099-4300/24/3/433.
2. J. Sporring and S. Darkner, *An algebra for local histograms*, Frontiers in Computer Science 4, 939563 (2022-11-17), DOI:10.3389/fcomp.2022.939563, https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2022.939563/full.
3. O. Yerushalmi, T. Etzion and E. Yaakobi, *The Capacity of the Weighted Read Channel*, arXiv:2401.15368v1 (first public 2024-01-27), https://arxiv.org/html/2401.15368v1.
4. *Exact fiber and constant-weight capacity laws for cyclic binary weighted reads*, published mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-fiber-and-constant-weight-capacity-laws-for-cyclic-binary--21136e4ec91c/RESULT.md.
