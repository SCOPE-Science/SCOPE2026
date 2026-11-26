# Sharp worst-case multiplicity of linear binary bigram multispectra
## Finding
For a binary word \(w\) of length \(n\), record the four multiplicities \(c_{ab}(w)\) of its consecutive length-two factors \(ab\), \(a,b\in\{0,1\}\). Let \(L(n)\) be the largest number of length-\(n\) binary words with any single such profile.

For every integer \(m\ge2\),
\[
\begin{aligned}
L(4m)&=\frac{4m-1}{m}\binom{2m-2}{m-1}\binom{2m-1}{m-1},\\
L(4m+1)&=4\binom{2m-1}{m-1}^{2},\\
L(4m+2)&=\frac{4m+1}{m}\binom{2m-1}{m-1}\binom{2m}{m-1},\\
L(4m+3)&=\frac{4m+2}{m+1}\binom{2m}{m}^{2}.
\end{aligned}
\]
The exact maximizing profiles \((c_{00},c_{01},c_{10},c_{11})\) are respectively:

* \(n=4m\): \((m-1,m,m,m)\) and \((m,m,m,m-1)\).
* \(n=4m+1\): \((m,m,m,m)\).
* \(n=4m+2\): \((m,m,m,m+1)\), \((m+1,m,m,m)\), \((m-1,m+1,m+1,m)\), \((m,m+1,m+1,m-1)\).
* \(n=4m+3\): \((m,m+1,m+1,m)\).

For \(2\le n\le7\), the maxima are \(1,2,3,4,5,12\), respectively. Thus, in the stable range there are \(2,1,4,1\) maximum-achieving multispectra according to length modulo four, and all have equal cross-transition counts.

## Assumptions and scope
Observations are *linear* adjacent ordered pairs, with multiplicity and without a wraparound pair. The alphabet is exactly \(\{0,1\}\); words need not contain both symbols. Profiles count distinct words, not labeled Eulerian traversals. All formulas concern fixed length \(n\), not unrestricted k-mer sets or cyclic Markov types.

## Proof
Set \(N=n-1\). A nonconstant word with equal endpoint symbols and \(k\ge1\) transitions in each direction has profile \((p,k,k,q)\) with \(p+q+2k=N\). Its number of realizations is
\[
B(p,q,k)=\binom{p+k}{k}\binom{q+k-1}{k-1}+\binom{p+k-1}{k-1}\binom{q+k}{k}
=\frac{N}{k}\binom{p+k-1}{k-1}\binom{q+k-1}{k-1}.
\]
The first summand counts words beginning and ending in \(0\): there are \(k+1\) positive zero-runs and \(k\) positive one-runs. The second counts the opposite endpoint symbol. Here the same profile contains *both* endpoint orientations, so their counts must be added.

A word with unequal endpoints has one more transition in its starting-to-ending direction. Its profile is either \((p,k+1,k,q)\) or \((p,k,k+1,q)\), where \(p+q+2k+1=N\). Its class size is
\[
U(p,q,k)=\binom{p+k}{k}\binom{q+k}{k}.
\]
Constant words have class size one. These run-composition bijections give the complete class-size formulas.

To optimize \(B\), set \(t=k-1\), \(X=p+k-1\), and \(Y=q+k-1\). Then \(X+Y=n-3\) and
\[
B=\frac{n-1}{t+1}\binom Xt\binom Yt.
\]
For fixed \(t\ge1\), the binomial-product increases strictly whenever the two arguments are moved one unit toward equality: this follows from \(\binom{x+1}{t}/\binom xt=(x+1)/(x+1-t)\), decreasing with \(x\). For \(t=0\) the product is constant. Hence one may take \(X=\lfloor(n-3)/2\rfloor\) and \(Y=\lceil(n-3)/2\rceil\). The ratio between consecutive \(t\)-terms at these fixed arguments is
\[
\frac{B(t+1)}{B(t)}=\frac{(X-t)(Y-t)}{(t+1)(t+2)}.
\]
This ratio decreases strictly on its feasible interval. Its crossing of one gives \(t=m-1\) for \(n=4m\) and \(n=4m+1\); a tie \(t=m-1,m\) for \(n=4m+2\); and \(t=m\) for \(n=4m+3\). Substitution gives exactly the four displayed values. For \(m\ge2\), all these optimizers have \(t\ge1\), so the balance of \(X,Y\) is strict except for the two adjacent choices when their sum is odd. This proves the stated complete list of balanced maximizing profiles.

It remains to rule out endpoint-unequal classes. Put \(X=p+k\), \(Y=q+k\), and \(t=k\). Then \(X+Y=n-2\) and \(U=\binom Xt\binom Yt\). For fixed \(t\), balancing \(X,Y\) maximizes the product. With these balanced arguments, \(U(t+1)/U(t)=(X-t)(Y-t)/(t+1)^2\), again decreasing across the feasible range. Consequently the four residue-class maxima of \(U\), for \(n=4m+r\), are
\[
\binom{2m-1}{m-1}^{2},\qquad
\binom{2m}{m}\binom{2m-1}{m-1},\qquad
\binom{2m}{m}^{2},\qquad
\binom{2m+1}{m}\binom{2m}{m}.
\]
(The first case has a tie in the optimizing transition count.) Dividing the balanced maxima by these four values gives respectively
\[
\frac{4m-1}{2m-1},\qquad 2,\qquad\frac{4m+1}{2(m+1)},\qquad2,
\]
all strictly greater than one for \(m\ge1\). Thus every global maximum lies in the balanced class, and the earlier profile list is exhaustive for \(n\ge8\). Direct run counting covers \(2\le n\le7\).

## Verification
Run the standalone `verify.py` using Python 3; it independently enumerates all \(2^n\) binary words at each length \(2\le n\le16\), groups them by literal bigram multiplicities, checks both run-composition formulas, confirms the exact global maximum and the complete maximizing-profile set, and checks the four-case uniqueness counts from length eight. The finite check confirms the proof at small sizes; the all-length conclusion follows from the ratio inequalities above.

## Relationship to prior work
Karhumäki, Puzynina, Rao, and Whiteland (2016/2017) derive general cardinality expressions for individual \(k\)-abelian classes, including the setting underlying binary bigram counts; the present theorem does **not** claim the per-class composition identities as new. It instead optimizes across *all* realizable linear spectra and classifies *every* maximizing profile. The published binary read-two multispectrum census determines the number of spectra and singleton classes but does not state this sharp largest-class law. Jacquet, Knessl, and Szpankowski (2010) enumerate **cyclic** Markov types rather than the maximum size of a **linear** fiber. Schmidt and Alanko (2023) study minimum representation of \(k\)-mer *sets* without repeats, rather than worst-case ambiguity under multisets retaining repeated 2-mers.

## Limitations
The theorem is binary and has read length exactly two. It does not address larger alphabets, longer reads, cyclic observations, or decoding with errors. The source comparison found no statement of this exact global optimization; unindexed work or a special case of a stronger published theorem remains an originality risk. Independent audit has not been performed.

## References
1. S. Schmidt and J. N. Alanko, *Eulertigs: minimum plain text representation of k-mer sets without repetitions in linear time*, Research Square preprint, posted 2023-02-16, DOI:10.21203/rs.3.rs-2581995/v1; Algorithms for Molecular Biology 18, 5 (2023), DOI:10.1186/s13015-023-00227-1.
2. J. Karhumäki, S. Puzynina, M. Rao, and M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, arXiv:1605.03319 (2016); Theoretical Computer Science 658, 190–204 (2017), DOI:10.1016/j.tcs.2016.06.010.
3. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548 (2018), IEEE Transactions on Information Theory 65, 7682–7696 (2019).
4. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768.
