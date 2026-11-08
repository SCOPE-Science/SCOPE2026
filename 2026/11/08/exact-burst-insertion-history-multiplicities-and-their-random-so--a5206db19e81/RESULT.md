# Exact burst-insertion history multiplicities and their random-source law

## Finding

Fix an alphabet of size \(q\ge2\), a burst length \(b\ge1\), an integer \(m\ge0\), and a word \(y\) of length \(m\). Write \(I_b(y)\) for the distinct words \(x\) of length \(m+b\) obtained by inserting one contiguous block of length \(b\) into \(y\). For each \(x\in I_b(y)\), let \(h_y(x)\) be the number of start positions whose length-\(b\) deletion from \(x\) produces \(y\). Define \(N_s(y)=|\{x\in I_b(y):h_y(x)=s\}|\).

The entire *history multiplicity spectrum* has a direct finite formula. Put \(T_{m+2}=T_{m+3}=0\), and for \(1\le s\le m+1\) set
\[
T_s(y)=\begin{cases}
(m-s+2)q^{b-s+1},&s\le b+1,\\
\displaystyle\sum_{i=0}^{m-s+1}\mathbf 1\{y_i\cdots y_{i+s-2}\text{ has period }b\},&s\ge b+2.
\end{cases}
\]
Here a finite word has period \(b\) when symbols spaced \(b\) places apart coincide wherever both exist; the sum is zero when its index set is empty. Then for every \(1\le s\le m+1\),
\[
\boxed{N_s(y)=T_s(y)-2T_{s+1}(y)+T_{s+2}(y).}
\]
In particular, the low multiplicities are rigid: whenever \(1\le s\le\min(b-1,m-1)\),
\[
N_s(y)=q^{b-s-1}(q-1)\big((m-s+2)(q-1)+2\big),
\]
independently of the word \(y\). Summing the spectrum recovers the *previously known* burst-insertion ball size \(\lvert I_b(y)\rvert=q^b+m(q-1)q^{b-1}\); that cardinality is not claimed as a new result.

For an independently uniform random center \(Y\in\Sigma_q^m\), the full expected spectrum is
\[
\boxed{\mathbb E N_s(Y)=
\begin{cases}
(q-1)q^{b-s-1}\big((m-s+2)(q-1)+2\big),&1\le s\le m,\\
q^{b-m},&s=m+1.
\end{cases}}
\]
This formula includes the empty center, with its first case void. The maximum multiplicity \(H(Y)=\max_x h_Y(x)\) obeys the following *exact distributional identity*. Let \(L_N\) be the longest consecutive run of successes among \(N=\max(0,m-b)\) independent Bernoulli variables of success probability \(1/q\), with \(L_0=0\). Then
\[
\boxed{H(Y)\stackrel{d}=\min(m+1,b+1)+L_N.}
\]
Indeed the stronger deterministic identity holds with the success indicators \(\mathbf1\{y_i=y_{i+b}\}\). For fixed \(q,b\), this implies \(H(Y)/\log_q m\to1\) in probability as \(m\to\infty\).

Under a uniform random insertion location and an independent uniform length-\(b\) inserted block, \(\Pr(X=x\mid Y=y)=h_y(x)/((m+1)q^b)\). Thus the spectrum specifies **the entire finite output probability distribution**, including its maximum atom \(H(y)/((m+1)q^b)\), and not just the number of possible outputs.

## Assumptions and scope

All parameters are finite integers in the ranges above; symbol equality is literal equality in an alphabet of cardinality \(q\). Positions are indexed from zero: inserting at index \(i\) places the block before \(y_i\), with \(i=m\) meaning append. A deletion at index \(i\) removes coordinates \(i,\ldots,i+b-1\) of the longer word. Different inserted block strings at a fixed index always produce different outputs. A single longer word may correspond to multiple indices, counted by \(h_y\). This does not count multiple edit *sequences* of more than one burst.

## Proof

**1. Equality of two deletion histories.** Let \(x\) have length \(m+b\), and \(0\le i<j\le m\). Deleting the length-\(b\) segments starting at \(i\) and \(j\) yields the same shorter word if and only if
\[
 x_t=x_{t+b}\quad\text{for all } i\le t<j.
\]
This follows by comparing the two deletion outputs: outside the interval from \(i\) to \(j-1\) they agree automatically, while in that interval one contains \(x_{t+b}\) and the other contains \(x_t\). Consequently, whenever two indices are valid for the same output \(y\), every index between them is valid: the valid starts form a single integer interval. (This is the familiar period-\(b\) deletion equivalence; the new analysis below counts its complete fiber distribution.)

**2. Pairwise intersections of insertion-location images.** Let \(S_i(y)\) be the set of words produced by inserting a length-\(b\) block at index \(i\) of \(y\). For \(d=j-i\ge0\), the equality in step 1 applied to \(x=y_0\cdots y_{i-1}zy_i\cdots y_{m-1}\) yields
\[
|S_i(y)\cap S_j(y)|=\begin{cases}
q^{b-d},&0\le d\le b,\\
\mathbf1\{y_i\cdots y_{j-1}\text{ has period }b\},&d>b.
\end{cases}
\]
For \(d\le b\), exactly the first \(d\) symbols of the inserted block are forced and its other \(b-d\) symbols are free. For \(d>b\), the entire block is forced; consistency of the remaining \(d-b\) comparisons is exactly period \(b\) of the displayed factor. The factor has length \(d\), and all its period comparisons are included. Both directions explicitly construct the unique compatible block when \(d>b\).

**3. Convert overlaps to multiplicities.** Since the valid starts for each output form an interval of size \(h_y(x)\), the number of contiguous groups of \(s\) valid starts is \((h_y(x)-s+1)_+\), where \((u)_+=\max(u,0)\). Count these groups first by the output and then by the first start:
\[
T_s(y)=\sum_{x\in I_b(y)}(h_y(x)-s+1)_+
=\sum_{i=0}^{m-s+1}|S_i(y)\cap S_{i+s-1}(y)|.
\]
The equality of the two endpoints forces all intermediate starts to be valid, so the second sum counts exactly the required groups. Inserting step 2 gives the stated \(T_s\) formula. Because \(T_s-T_{s+1}\) counts outputs with multiplicity at least \(s\), taking another difference proves \(N_s=T_s-2T_{s+1}+T_{s+2}\). The boundary conventions \(T_{m+2}=T_{m+3}=0\) are essential for the largest multiplicity \(s=m+1\). For \(s\le\min(b-1,m-1)\), all three terms are in the geometric branch, giving the rigid formula by algebra. The total ball size follows separately from \(\sum_sN_s=T_1-T_2\) for \(m\ge1\), with \(m=0\) checked directly, and agrees with the established insertion-ball formula.

**4. Uniform random centers.** For \(i=0,\ldots,m-b-1\), put \(E_i=\mathbf1\{Y_i=Y_{i+b}\}\). The graph of these comparisons decomposes into \(b\) disjoint paths indexed by residues modulo \(b\). Along each path, independently uniform vertex labels make successive equality indicators independent Bernoulli variables of probability \(1/q\): fix the first label, and at each edge exactly one of the \(q\) next labels yields equality. This also proves independence jointly across the paths. For \(s\ge b+2\), the period indicator for the factor in \(T_s\) requires \(s-b-1\) consecutive successes, hence has expectation \(q^{-(s-b-1)}\). This is exactly the expectation of the first branch, \((m-s+2)q^{b-s+1}\), which therefore holds for \(\mathbb E T_s\) at every \(1\le s\le m+1\). Two differences give the expected formula for \(s\le m\); at \(s=m+1\) use the boundary zero terms separately to obtain \(q^{b-m}\), avoiding an invalid extrapolation past the endpoint.

By step 3, \(h_y(x)\ge s\) is attainable exactly when a consecutive group of \(s\) valid starts exists, i.e. \(T_s>0\). Groups up through \(\min(b+1,m+1)\) always exist. For larger \(s\), existence is equivalent to \(s-b-1\) consecutive successes in the string of \(E_i\)'s. The deterministic and distributional identities for \(H\) follow. For an explicit finite distribution, fix \(r\ge1\), set \(a_t^{(r)}=1\) for \(0\le t<r\), and recursively define
\[
 a_t^{(r)}=(1-q^{-1})\sum_{j=0}^{r-1}q^{-j}a_{t-j-1}^{(r)}\quad(t\ge r).
\]
Condition on the last failure followed by fewer than \(r\) successes to see that \(a_N^{(r)}=\Pr(L_N<r)\); hence \(\Pr(H<\min(m+1,b+1)+r)=a_N^{(r)}\). For \(N\to\infty\), the union bound gives \(\Pr(L_N\ge\lceil(1+\varepsilon)\log_qN\rceil)\le Nq^{-\lceil(1+\varepsilon)\log_qN\rceil}\to0\). Splitting the trials into disjoint blocks of \(r=\lfloor(1-\varepsilon)\log_qN\rfloor\) sites gives \(\Pr(L_N<r)\le(1-q^{-r})^{\lfloor N/r\rfloor}\to0\), for every fixed \(0<\varepsilon<1\). Therefore \(L_N/\log_qN\to1\) in probability and the same holds for \(H(Y)/\log_qm\) at fixed \(b\).

**5. Induced output likelihood.** There are exactly \((m+1)q^b\) equally likely histories \((i,z)\), and exactly \(h_y(x)\) of them output a given \(x\). Division gives the stated probability and its maximum. No independence or decoding claim about an unknown source word is inferred from this conditional generation model.

## Verification

The accompanying standalone `checker.py` enumerates the insertion histories independently of the formulas. It checks 736 distinct fixed-center parameter instances, including 54,360 distinct output words, for the complete multiplicity profile, interval property, total ball size, exact maximum and conservation of histories. A separate exhaustive averaging pass verifies the expected profiles and longest-run distribution recursion for small alphabets and parameters. The checker uses Python 3 standard library and exact integer/rational arithmetic; run `python3 checker.py`. These finite tests check implementation and boundary cases, while the preceding proof establishes the infinite parameter statement.

## Relationship to prior work

Lan, Sun, Yu and Ge (arXiv:2504.20460, initially available 29 April 2025), Sections III–IV, determine burst-insertion ball sizes, intersections between error balls with *different* centers, and reconstruction thresholds. Xi, Sun and Ge (arXiv:2506.07817, 9 June 2025), Sections 2–3, explicitly use the period-\(b\) deletion-equivalence observation and study cardinalities of fixed-length burst Levenshtein balls. Their known lemmas are used here as background rather than presented as discoveries. The present result concerns the complete **within-one-center insertion-history fiber-size distribution**, its random-center expectation, and its extreme-value law, which are not implied numerically by ball sizes or distinct-center intersection maxima alone. Sun, Xi and Ge (IEEE TIT 2023, DOI below) is a relevant earlier single-burst reconstruction source; its full text was not available in the consulted open-access material, leaving a priority risk for implicit related statements. No claim of definitive historical uniqueness is made.

## Limitations

The results concern one *contiguous* inserted block of a fixed length, with distinguishable insertion locations and literal symbol equality. The random-center law assumes independently uniform symbols, and the limiting statement fixes the alphabet size and burst length while center length tends to infinity. General nonuniform or dependent sources, multiple bursts, and code-capacity consequences are not covered. Closely related period-\(b\) equivalence and total sphere cardinality are established in prior work; independent verification and complete priority certification are outstanding.

## References

1. Z. Lan, Y. Sun, W. Yu and G. Ge, "Sequence Reconstruction under Channels with Multiple Bursts of Insertions or Deletions," arXiv:2504.20460v1 (29 April 2025), https://arxiv.org/html/2504.20460v1.
2. Y. Xi, Y. Sun and G. Ge, "On the Fixed-Length-Burst Levenshtein Ball with Unit Radius," arXiv:2506.07817v1 (9 June 2025), https://arxiv.org/html/2506.07817.
3. Y. Sun, Y. Xi and G. Ge, "Sequence Reconstruction Under Single-Burst-Insertion/Deletion/Edit Channel," IEEE Transactions on Information Theory 69 (2023), 4466–4483, https://doi.org/10.1109/TIT.2023.3250459.
4. Y. Sun, Z. Lu, Y. Zhang and G. Ge, "Asymptotically Optimal Codes for (t,s)-Burst Error," arXiv:2403.11750 (first posted 18 March 2024), https://arxiv.org/abs/2403.11750.
