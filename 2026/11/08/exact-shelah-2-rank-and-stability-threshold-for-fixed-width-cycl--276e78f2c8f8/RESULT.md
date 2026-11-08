# Exact Shelah 2-rank and stability threshold for fixed-width cyclic windows

## Finding

For any integers \(n\ge 2\) and \(1\le \ell<n\), write \(G=\mathbb Z/n\mathbb Z\), and for each \(s\in G\) let
\[
I_s=\{s,s+1,\ldots,s+\ell-1\}\pmod n.
\]
The binary concept family is \(\mathcal C_{n,\ell}=\{I_s:s\in G\}\). Put \(w=\min\{\ell,n-\ell\}\). Its exact adaptive shattering rank is
\[
\boxed{\operatorname{Ldim}(\mathcal C_{n,\ell})=1+\lfloor\log_2 w\rfloor.}
\]
The value is the optimal worst-case deterministic online mistake bound in the realizable membership-prediction model, and, for the associated two-sorted incidence formula with window starts as object variables, the exact finite Shelah 2-rank.

There is also a precise **stability boundary**. For a sequence of such incidence structures \((n_j,\ell_j)\) and a nonprincipal ultrafilter \(\mathcal U\), their ultraproduct incidence formula is stable precisely if \(w_j=\min\{\ell_j,n_j-\ell_j\}\) is bounded on a \(\mathcal U\)-large index set. It is unstable if \(w_j\) tends to infinity along \(\mathcal U\). The second statement concerns the relation defining the windows, not stability of every formula of the entire ultraproduct theory.

For context, the complete static shattered-support polynomial is
\[
\Phi_{n,\ell}(z)=1+nz+n(w-1)z^2.
\]
Thus the VC dimension is one for \(w=1\), and two for \(w\ge2\). The static pair count follows from an earlier general translate-family identity, and the length-four online special case overlaps an existing four-point classification. Neither is proposed as independently novel here.

## Assumptions and scope

The cycle has \(n\ge2\) distinguishable positions. Every window contains exactly \(\ell\) consecutive positions in the indicated positive cyclic orientation, with \(1\le\ell<n\). No empty or full windows are included. The family contains exactly \(n\) distinct members, because a nonempty proper consecutive block has a unique boundary from an unselected to a selected position and hence no nontrivial period. The indexing parameters are the starts \(s\), and a membership query asks whether a chosen point \(x\in G\) lies in the unknown \(I_s\).

A complete binary tree of depth \(d\) is Littlestone-shattered if each internal vertex is labeled by a point of \(G\) and all \(2^d\) root-to-leaf binary answer sequences are realized by at least one window. Distinct leaves require distinct window hypotheses. The finite rank concerns deterministic realizable prediction; it is not an expression for randomized Littlestone dimension.

## Proof

**1. Upper bound.** Fix a query position \(x\). Exactly \(\ell\) start positions yield \(x\in I_s\); the other \(n-\ell\) yield \(x\notin I_s\). For a shattered tree of positive depth \(d\), both children of the root must support a shattered tree of depth \(d-1\). A shattered depth-\(r\) tree requires at least \(2^r\) distinct concepts, since incompatible binary paths need different witnesses. Hence \(2^{d-1}\le\min\{\ell,n-\ell\}=w\), giving \(d\le1+\lfloor\log_2 w\rfloor\).

**2. Consecutive-block splitting lemma.** Let \(B=(b,b+1,\ldots,b+k-1)\) be any cyclically ordered block of \(k\le w\) distinct possible start positions. For any cut after the first \(j\) starts, \(1\le j<k\), query the position \(x=b+j-1\pmod n\). If \(s=b+t\) with \(0\le t<j\), then \((x-s)\bmod n=j-1-t<k\le\ell\), so \(x\in I_s\). If \(j\le t<k\), then \((x-s)\bmod n=n-(t-j+1)\ge n-(k-1)>\ell-1\), because \(k\le n-\ell\). Thus \(x\notin I_s\). The query precisely separates the prefix of length \(j\) from the suffix. Repeating median cuts gives a complete depth-\(\lfloor\log_2 k\rfloor\) tree for any such block, with the optimal cardinality-limited depth.

**3. Lower bound.** Let \(m=2^{\lfloor\log_2w\rfloor}\). The first query \(x=\ell-1\) has positive starts \(0,1,\ldots,\ell-1\) and negative starts \(\ell,\ell+1,\ldots,n-1\). Retain the \(m\) starts \(0,\ldots,m-1\) on the positive branch and \(\ell,\ldots,\ell+m-1\) on the negative branch. Both are valid consecutive blocks, because \(m\le w\). By step 2, each branch admits a complete shattered tree of depth \(\log_2m\); attaching them to the first query yields depth \(1+\log_2m=1+\lfloor\log_2w\rfloor\). This meets the upper bound for every allowed \(n,\ell\), including \(w=1\).

**4. Static comparison.** Every position belongs to some but not all windows, giving \(s_1=n\). For distinct points at shortest circular separation \(d\), a window of length \(L\) contains both precisely when \(d+1\le L\). Thus both an included pair and an excluded pair can occur for the length-\(\ell\) window exactly when \(d<w\): exclusion of both means inclusion of both by the complementary consecutive window of length \(n-\ell\). The two single-positive patterns are available whenever the start-incidence sets of the distinct positions differ, which they do because proper consecutive blocks have no nontrivial period. Every circular distance \(d<w\le n/2\) contributes exactly \(n\) unordered pairs, giving \(s_2=n(w-1)\).

There are no shattered triples. For three distinct points, let \(g\) be the longest of their three cyclic gaps (measured in edges). A trace excluding all three requires the complementary \((n-\ell)\)-window to contain all three; the smallest arc containing all three has \(n-g+1\) vertices, so \(\ell\le g-1\). But a trace containing the two ends of that longest gap while excluding the third point must traverse that gap inside the selected window, requiring \(\ell\ge g+1\). The two conditions are incompatible. Heredity of shattering excludes all larger supports. Consequently \(\Phi_{n,\ell}(z)=1+nz+n(w-1)z^2\).

**5. Stability of ultraproduct windows.** Represent membership by a two-sorted first-order binary relation \(R_j(x,s)\), true exactly when \(x\in I_s\). For any fixed finite \(d\), existence of a complete shattered depth-\(d\) tree is expressible by one first-order sentence: existentially quantify the finitely many query points and one witnessing start parameter for every binary path, then assert their prescribed relation values. Łoś's theorem therefore transfers this property to the ultraproduct exactly when the corresponding set of indices lies in \(\mathcal U\). The established finite formula says that a depth-\(d\) tree exists exactly when \(w_j\ge2^{d-1}\) (for positive \(d\)). If \(w_j\) is bounded on a \(\mathcal U\)-large set, some finite depth is forbidden in the ultraproduct, so its Shelah 2-rank is finite and its window-incidence formula stable. Otherwise, for every fixed depth the required inequality holds on a \(\mathcal U\)-large set, so the ultraproduct has trees of all finite depths and the formula is unstable. We use the standard equivalence of finite Shelah 2-rank, finite Littlestone dimension, and stability of the fixed partitioned formula, not a new classification of general stable theories [1].

## Verification

The included standalone script `verify_cyclic_windows.py` uses exact recursive rank computation from independently constructed window-membership columns for every parameter pair \(2\le n\le17\) and \(1\le\ell<n\). It also checks explicit complete adaptive-tree witnesses, all one- and two-point static traces through the same range, and no shattered triple for \(n\le11\). Additional much larger cycles verify the explicit tree-construction procedure. The independent finite checks cover 136 parameter pairs and 15,786 nonempty candidate supports; they confirm examples and implementation of the constructive proof, not the general theorem by extrapolation. The verifier needs only Python 3 and its standard library; run `python verify_cyclic_windows.py`.

For example, when \(n=64\) and \(\ell=32\), the VC dimension is two and the Littlestone dimension is six. With \(n=1000\) and \(\ell=2\), the family still has one thousand distinct hypotheses, but its Littlestone dimension is only two. For any \(n=2^h\) with \(h\ge3\) and \(\ell=2^{h-1}\), the VC dimension remains two while the Littlestone dimension is \(h\).

## Relationship to prior work

Chase and Freitag [1] identify Littlestone/thicket dimension with the finite Shelah 2-rank and connect finite rank to stability of a formula; their general theorem is used in step 5, rather than claimed here. Filmus et al. [2] explain the optimal deterministic and randomized prediction ranks and characterize the deterministic online mistake bound generally; they do not give an exact all-width cyclic-window formula. Chase, Freitag and Reyzin [3] relate Littlestone dimension to query learning and compression and analyze a family of pairwise-disjoint real intervals, which differs from rotating overlapping cyclic windows.

Earlier translate-family work already handles the length-four special case of the exact online rank on sufficiently large cycles, and a general finite-group identity for shattered pairs subsumes the quadratic coefficient of the static polynomial. These overlaps are explicitly excluded from the originality claim. The new assessed contribution is the all-width formula for the adaptive rank together with its precise ultraproduct stability threshold, neither of which follows solely from those special-case and static formulas.

## Limitations

The model uses a fixed cardinality and a fixed cyclic orientation for each class. It does not cover unrestricted window lengths, unions of windows, arbitrary cyclic subsets, or randomized optimal mistake bounds. The ultraproduct result classifies stability of this particular incidence formula, not stability of the full ambient first-order theory. The outcome has been checked against relevant available literature and previous results, but an equivalent theorem under alternative circular-arc, two-rank, or online-prediction terminology cannot be categorically excluded. No independent scientific audit has been performed.

## References

[1] Hunter Chase and James Freitag, *Model Theory and Machine Learning*, arXiv:1801.06566v1, first publicly available 2018-01-19; see Section 4, in particular the definition of Shelah 2-rank and Theorem 4.6. https://arxiv.org/abs/1801.06566

[2] Yuval Filmus, Steve Hanneke, Idan Mehalel and Shay Moran, *Optimal Prediction Using Expert Advice and Randomized Littlestone Dimension*, arXiv:2302.13849, first public 2023-02-27; Proceedings of Machine Learning Research 195 (2023). https://proceedings.mlr.press/v195/filmus23a.html

[3] Hunter Chase, James Freitag and Lev Reyzin, *Applications of Littlestone Dimension to Query Learning and to Compression*, arXiv:2310.04812, first public 2023-10-07; MFCS 2024, DOI:10.4230/LIPIcs.MFCS.2024.42. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2024.42
