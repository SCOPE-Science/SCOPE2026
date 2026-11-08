# Complete inverse-list spectrum for a single deletion in ordered overlapping reads

## Finding
Let \(q\ge2\) and \(\ell\ge2\) be integers, and let \(n\ge\ell+1\). For a word \(x=x_1\cdots x_n\in\Sigma_q^n\), define its *ordered* overlapping read vector
\[
\mathcal R_\ell(x)=(x_{[1,\ell]},x_{[2,\ell+1]},\ldots,x_{[n-\ell+1,n]}).
\]
Here each read records the complete ordered \(\ell\)-symbol substring, not its Hamming weight or unordered composition. For a received vector \(y\) of \(n-\ell\) reads, let \(L(y)\) be the number of distinct words \(x\in\Sigma_q^n\) whose read vector becomes \(y\) after **exactly one** coordinate deletion.

Call two consecutive received reads *compatible* if their length-\((\ell-1)\) suffix and prefix, respectively, coincide. Call a pair *weakly compatible* when its corresponding length-\((\ell-2)\) suffix and prefix coincide (an empty overlap is always compatible). Then the complete inverse-list classification is:

1. If two or more consecutive pairs are incompatible, \(L(y)=0\).
2. If exactly one consecutive pair is incompatible, \(L(y)=1\) if that pair is weakly compatible and \(L(y)=0\) otherwise.
3. If all pairs are compatible, there is a unique word \(z\in\Sigma_q^{n-1}\) whose overlapping read vector is \(y\). If \(z\) is constant, then \(L(y)=2q-1\). Otherwise, partition \(z\) into its maximal constant runs and let \(k_\ell(z)\) count **strictly internal runs** (neither the first nor last) of length at least \(\ell-1\). Then
\[
L(y)=2q+k_\ell(z).
\]

Consequently, among all possible received vectors, exactly
\[
q^{n-1}+(n-\ell-1)(q^n-q^{n-\ell+1})
\]
have at least one parent, and the sharp maximum number of parents is
\[
\boxed{\max_y L(y)=2q+\left\lfloor\frac{n-3}{\ell-1}\right\rfloor.}
\]
This maximum is attainable over **every** alphabet size \(q\ge2\), by an alternating sequence of constant runs of lengths \(1,\ell-1,\ldots,\ell-1,1\), distributing any leftover symbols without reducing the number of long internal runs.

There is also an exact all-parameter enumerator. Set \(h=\ell-1\), \(F(z)=z/(1-z)\), \(S_h(z)=\sum_{j=1}^{h-1}z^j\), and \(H_h(z)=z^h/(1-z)\). Let \(A_{q,\ell,m}(u)\) count the length-\(m\) words \(z\) according to the inverse-list size in case 3. Then, as formal power series,
\[
\sum_{m\ge1}A_{q,\ell,m}(u)z^m
=qF(z)u^{2q-1}
+\frac{q(q-1)F(z)^2u^{2q}}{1-(q-1)(S_h(z)+uH_h(z))}.
\]
For \(n\ge\ell+1\), the complete positive-list spectrum is the coefficient polynomial
\[
P_{q,\ell,n}(u)=A_{q,\ell,n-1}(u)
+(n-\ell-1)(q^n-q^{n-\ell+1})u.
\]
In particular, the coefficient of \(u^j\) is exactly the number of received vectors with \(j\) distinct possible transmitted words, for each \(j\ge1\). The remaining \(q^{\ell(n-\ell)}-P_{q,\ell,n}(1)\) received vectors have no possible parent.

## Assumptions and scope
The alphabet is finite with \(q\ge2\), and read positions are ordered. The read length satisfies \(2\le\ell\le n-1\); the case \(n=\ell\) would yield the empty received read vector and is excluded. There is a single adversarial deletion of one entire read, not a symbol deletion in the underlying word. The receiver knows \(n\), \(q\), and \(\ell\), but not the deletion position. Parent counts are sets of distinct source words, so multiple deletion positions yielding the same parent count only once. No end markers, cyclic wraparound, read aggregation, or read-symbol corruption are assumed.

## Proof
Write \(r=n-\ell+1\), the number of original reads. The received vector has \(r-1\) reads. When the deleted read is the first or last, every consecutive received pair must be compatible. When an interior read at index \(i\) is deleted, all consecutive received pairs except possibly the pair straddling the missing read are compatible. Across this exceptional pair, the original two reads are separated by two starting positions and hence must overlap in their last and first \(\ell-2\) coordinates. Thus two incompatibilities are impossible. A single incompatible pair determines the deletion gap uniquely; at that gap, weak compatibility is necessary and sufficient to join the two read paths by inserting exactly one read. Such an insertion and the original word are unique because their union of coordinate intervals covers every source coordinate. This proves cases 1 and 2.

If every consecutive pair is compatible, their concatenated path uniquely spells a length-\((n-1)\) word \(z\), proving the existence and uniqueness asserted in case 3. Deleting the first read from a parent gives every possible prefix extension \(az\), with \(a\in\Sigma_q\). Deleting the last gives every suffix extension \(zb\), with \(b\in\Sigma_q\). Each family has \(q\) elements. The two families intersect if and only if \(z\) is constant; then their intersection consists of its one constant extension.

Now delete an interior read at position \(i\), with \(2\le i\le n-\ell\). The two retained reads across its gap already overlap in \(\ell-1\) coordinates because \(y=\mathcal R_\ell(z)\); to have originated two read positions apart, they must additionally overlap in \(\ell-2\) coordinates with the different alignment. Writing their symbols using \(z\), this extra condition is precisely
\[
z_i=z_{i+1}=\cdots=z_{i+\ell-2}.
\]
When it holds, the unique source parent is obtained by duplicating the symbol \(z_{i+\ell-2}\) immediately at that position in \(z\). Distinct duplication positions produce the same extended word exactly when they lie in the same maximal constant run: equality for two different positions forces the intervening word to be constant, and that condition also suffices.

A duplicated position in the first or last constant run produces an extension already counted among the prefix or suffix extensions. Each strictly internal constant run supplies one genuinely new parent if and only if its length is at least \(\ell-1\). This proves case 3, including the constant-word exception.

For case 2, the number of possible incompatible received read pairs is counted by their unique defective gap. There are \(r-2=n-\ell-1\) choices of this gap. For a fixed gap, the map from an underlying length-\(n\) source word to its received vector with that read deleted is injective: the two flanking read paths determine its entire source word. The sole incompatibility occurs exactly when a particular contiguous length-\(\ell\) source segment is not constant. There are \(q^n-q^{n-\ell+1}\) such source words. Distinct gap positions give disjoint received vectors, because the gap is detected by the unique incompatibility. There are separately exactly \(q^{n-1}\) fully compatible received vectors, one for each length-\((n-1)\) word. Adding these counts gives the displayed feasibility formula.

If \(z\) has \(k\) qualifying internal runs, it must have at least two nonempty endpoint runs, so \(n-1=|z|\ge 2+k(\ell-1)\), proving the maximum upper bound. Conversely, for \(k=\lfloor(n-3)/(\ell-1)\rfloor\), choose \(k+2\) alternating-color runs with endpoint lengths one and internal lengths at least \(\ell-1\), and append leftover length to any run without merging colors. Two symbols suffice, proving attainability for every \(q\ge2\).

Finally, consider the run-length generating function for fully compatible vectors. A single constant run of any positive length contributes \(qF(z)u^{2q-1}\). With two or more runs, choose the first symbol in \(q\) ways and each subsequent run symbol in \(q-1\) ways. The two boundary runs contribute \(F(z)^2\); each internal run contributes \(S_h(z)+uH_h(z)\), recording one factor of \(u\) when its length is at least \(h\). Summing the geometric series over the number of internal runs yields the rational function for \(A\). Each vector with one unique overlap defect contributes to \(u^1\); this supplies the second term in \(P\). Thus the complete enumerator follows.

## Verification
Run `python3 checker.py` using Python 3 with no third-party packages. The checker independently generates all sources and all distinct one-read-deletion outputs, compares each output's number of source parents against the overlap/run classification, compares the complete positive-list histogram against a separate enumeration of positive run-length compositions, and tests the feasible-output and worst-case formulas. Its executed self-test passed 49 \((q,n,\ell)\) combinations for \(q\in\{2,3,4,5\}\), \(\ell\in\{2,3,4\}\), and accessible small \(n\), totaling 343,337 feasible received vectors and 631,205 distinct source/output incidences. The checker performs finite corroboration only; the proof above establishes all parameter ranges.

## Relationship to prior work
Ye and Ge (arXiv:2606.26434v1, 24 June 2026) define precisely the ordered overlapping \(\ell\)-mer read channel followed by deletions and derive a structural interpretation used to construct correction codes. Their accessible abstract and introduction emphasize redundancy bounds and check patterns, rather than the complete inverse-list spectrum, sharp list size, or its generating function. The remaining body could not be compared exhaustively, so an implicit earlier formulation remains a priority risk.

Banerjee, Yehezkeally, Wachter-Zeh, and Yaakobi study a related nanopore deletion-readout model in which each read is a Hamming weight of a window, with additional boundary conventions. Their data are not full ordered \(\ell\)-mers, so their reconstruction theorem does not imply this inverse-list law. A separate published study titled *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph* concerns intersections of two ordinary symbol-deletion traces, not deletion of one member of an ordered window-read vector. A paper on list-decodability of symbol-pair codes concerns substitution/Hamming-radius list decoding, a different channel.

## Limitations
The theorem is for one deleted *complete ordered read* only, not for several deleted reads, cyclic read vectors, uncertain read ordering, or unlabeled/composition measurements. The coefficient formula is exact but does not supply an optimized closed coefficient expression for every list value. Neither historical priority nor the result's extension to multi-deletion channels has been independently established. Access to the main 2026 paper's full remaining body was incomplete during comparison; this is explicitly retained as a scientific priority risk, not treated as proof of novelty.

## References
1. Z. Ye and G. Ge, *Deletion-Correcting Codes for the \(\ell\)-Symbol Read Channel*, arXiv:2606.26434v1, first submitted 24 June 2026, https://arxiv.org/abs/2606.26434 .
2. A. Banerjee, Y. Yehezkeally, A. Wachter-Zeh, and E. Yaakobi, *Correcting a Single Deletion in Reads from a Nanopore Sequencer*, freely available manuscript, https://www.ce.cit.tum.de/fileadmin/w00cgn/lnt/staff/yehezkeally/YYconf12.pdf .
3. S. Liu, C. Xing, and C. Yuan, *List Decodability of Symbol-Pair Codes*, arXiv:1806.08992, https://arxiv.org/abs/1806.08992 .
