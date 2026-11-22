# Exact inverse-list spectrum of ternary adjacent-maximum reads on proper words

## Finding

Let \(m\ge1\), let \(\Sigma=\{0,1,2\}\) with its natural order, and define the **proper-word** source set
\[
\mathcal P_m=\{x_0x_1\cdots x_m\in\Sigma^{m+1}: x_i\ne x_{i+1}\text{ for every }0\le i<m\}.
\]
The indexed adjacent-maximum channel is
\[
T_m(x)_i=\max\{x_i,x_{i+1}\},\qquad 0\le i<m,
\]
with output alphabet \(\{1,2\}\). For an output \(y\in\{1,2\}^m\), write \(d_m(y)=|T_m^{-1}(y)|\). All words are linear and indexed, and the alphabet symbols are named; there is no rotation or symbol-permutation quotient.

**Theorem (complete inverse-list spectrum).** An output containing at least one \(1\) is attainable if and only if every maximal block of \(2\)'s strictly between successive \(1\)'s has **even** length. The all-\(2\) output is also attainable. For an attainable \(y\) containing \(1\), let \(r_0,\dots,r_s\) denote the lengths of its successive maximal blocks of \(2\)'s (including the possibly empty initial, final and intermediate blocks), so that \(s\ge1\) is the number of occurrences of \(1\). Then
\[
\boxed{d_m(y)=2^{1+\sum_{j=0}^{s}\lfloor r_j/2\rfloor}.}
\]
For the unique output consisting entirely of \(2\)'s,
\[
\boxed{d_m(2^m)=\begin{cases}
3\,2^{m/2},&m\text{ even},\\
2^{(m+3)/2},&m\text{ odd}.
\end{cases}}
\]
For any unattainable output the inverse list is empty.

In particular, there are exactly \(F_{m+3}-1\) attainable outputs, where \(F_0=0,F_1=1\) and \(F_{j+2}=F_{j+1}+F_j\). Thus the largest zero-error code for this deterministic indexed channel has size \(F_{m+3}-1\). The all-\(2\) output is the **unique** largest inverse list. The minimum nonzero inverse-list size is \(2\); the number of outputs realizing this minimum is \(1\), \(3\), or \(4\), respectively, when \(m=1\), \(m=2\), or \(m\ge3\).

The following rational generating function gives **the entire list-size distribution**, not just its extrema. Let \(c_{m,t}\) count outputs of length \(m\) containing \(1\) and having inverse-list size \(2^{t+1}\). Then
\[
\boxed{\sum_{m\ge1}\sum_{t\ge0}c_{m,t}z^m u^t
=\frac{z(1+z)^2}{(1-uz^2)(1-z-uz^2)}.}
\]
The exceptional all-\(2\) output at each positive length must be added separately with its list size above. Hence the count of attainable outputs and the full inverse-fiber histogram at every length are exact rational-series coefficients. The total source mass is \(\sum_y d_m(y)=3\cdot2^m\), and the average nonempty fiber is \(3\cdot2^m/(F_{m+3}-1)\).

## Assumptions and scope

The source length is exactly \(m+1\); the read length is exactly \(m\). No adjacent source symbols agree, but other repetitions are permitted. All consecutive two-site windows are observed **in positional order**, without noise or deletion. Maximum is taken in the fixed order \(0<1<2\). The result does not address circular inputs, larger alphabets, read losses, noisy outputs, or other pooling widths. A zero-error code here means a subset of \(\mathcal P_m\) on which the deterministic map \(T_m\) is injective; one representative per nonempty fiber attains the exact stated code size.

## Proof

**1. Edge-labeled walk representation.** Proper source words are walks on the three vertices \(0,1,2\), moving only between unequal vertices. A read \(1\) allows exactly edges \(0\!\leftrightarrow\!1\), whereas a read \(2\) allows exactly the four oriented edges between \(2\) and one of \(0,1\). Consequently, a read \(1\) leaves the walk at \(0\) or \(1\). Each subsequent read \(2\) switches between the singleton \(\{2\}\) and the pair \(\{0,1\}\). Two reads \(1\), separated by \(r\) consecutive reads \(2\), can coexist if and only if \(r\) is even. This proves necessity. For sufficiency choose one of the two orientations of the first edge \(0\!\leftrightarrow\!1\), route each even interior block through \(2\), and choose suitable endpoints for any initial and final blocks. If there is no \(1\), simply alternate \(2\) with an element of \(\{0,1\}\).

**2. Exact fiber multiplicities.** Let \(a\) count consistent source prefixes ending in each of \(0\) and \(1\) (the two counts agree by symmetry), and let \(b\) count those ending in \(2\). Initially \((a,b)=(1,1)\). Appending a read \(1\) transforms \((a,b)\mapsto(a,0)\), and appending \(2\) transforms \((a,b)\mapsto(b,2a)\). Therefore, with column-state convention,
\[
M_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
M_2=\begin{pmatrix}0&1\\2&0\end{pmatrix},\qquad M_2^2=2I,
\]
\[
d_m(y)=(2,1)M_{y_{m-1}}\cdots M_{y_0}(1,1)^{\mathsf T}.
\]
The identity \(M_2^2=2I\) shows that each disjoint pair of \(2\)'s multiplies the fiber by exactly two. After removing all such pairs from every run of \(2\)'s, a realizable output containing \(1\) reduces to one of the four forms \(1^s\), \(2\,1^s\), \(1^s\,2\), or \(2\,1^s\,2\), each having exactly two predecessors. This proves the stated formula. For \(y=2^m\), the matrix identity gives \(M_2^{2h}=2^h I\) and \(M_2^{2h+1}=2^h M_2\), yielding the two parity cases.

**3. The full distribution and output capacity.** An output containing \(s\ge1\) occurrences of \(1\) is uniquely expressible as
\[
2^{r_0}1\,2^{2k_1}1\cdots2^{2k_{s-1}}1\,2^{r_s},
\]
where \(r_0,r_s,k_j\) are nonnegative integers. Use \(z\) to mark the output length and \(u\) to mark each paired pair of \(2\)'s. An outer run has generating series
\[
A(z,u)=\sum_{r\ge0}z^r u^{\lfloor r/2\rfloor}=\frac{1+z}{1-uz^2},
\]
and each interior run has \(B(z,u)=\sum_{k\ge0}z^{2k}u^k=(1-uz^2)^{-1}\). Summing over \(s\ge1\) gives
\[
A(z,u)^2\sum_{s\ge1}z^s B(z,u)^{s-1}
=\frac{z(1+z)^2}{(1-uz^2)(1-z-uz^2)}.
\]
At \(u=1\), adding one all-\(2\) output at each length (including length zero only for the generating-series identity) produces
\[
\frac1{1-z}+\frac{z(1+z)^2}{(1-z^2)(1-z-z^2)}
=\frac1{(1-z)(1-z-z^2)}.
\]
The coefficient at \(z^m\) is \(F_{m+3}-1\). Since a deterministic map has one disjoint fiber per output, choosing one source per nonempty fiber is both necessary and sufficient for a largest injective code.

**4. Sharp extrema.** Every nonempty fiber containing \(1\) has size at least two; equality holds precisely when no block of \(2\)'s has length at least two, because every factor \(M_2^2\) doubles the count. Combining this restriction with the even-interior-block condition leaves \(1^m\), \(2\,1^{m-1}\), \(1^{m-1}\,2\), and \(2\,1^{m-2}\,2\) for \(m\ge3\), and the corresponding three or one valid forms at shorter lengths. For any realizable output containing \(1\), there are at most \(m-1\) symbols \(2\), so
\[
d_m(y)\le2^{1+\lfloor(m-1)/2\rfloor}<d_m(2^m).
\]
The all-\(2\) fiber is therefore the unique maximum, with the already computed value. This closes all lengths and boundary cases.

## Verification

The accompanying standalone Python checker uses only the standard library. It independently enumerates all \(98{,}298\) proper sources across read lengths \(1\) through \(14\) and compares direct preimage multiplicities against both the run formula and the two-state matrix recurrence. It separately expands the two-variable rational generating function through length \(100\) and verifies the full fiber-size histogram, total source mass, image cardinality, sharp minimum, and unique maximum. The enumerations are finite consistency tests; the all-length proof is given above.

Run from a directory containing this document and `verify.py` using `python3 verify.py`. No other files or software packages are needed.

## Relationship to prior work

MacDonald (2022) proves an infinite-subshift embedding theorem for sliding block codes under entropy and periodic-point conditions. Although the present local maximum operator is itself a sliding block code on a proper-word shift, that embedding theorem does not calculate finite-block inverse fiber sizes, the output language, or an exact finite-length zero-error code capacity. Wei, Schwartz and Ge (2023) study reconstruction and coding from ordered or unordered substring observations under errors; their channel outputs are substring traces, not symbolwise maxima of every two-symbol window. Weindel and colleagues (2023) study the merits of homopolymer-avoidance constraints and DNA-storage reliability, without this local ordered-maximum readout. Cahill and colleagues (public 2024) study group-invariant max filters on real inner-product spaces and orbit separation; their construction is not the indexed finite-alphabet two-site maximum map. The present classification requires the simultaneous inequality-adjacency constraint on sources and a lossy monotone local readout.

Standard transfer-matrix and Fibonacci techniques are used here and are not claimed as new in isolation. The proposed contribution is their **complete simultaneous resolution**, for this precisely specified channel, of the output language, all inverse-list multiplicities, their distribution, and sharp zero-error capacity and extremizers.

## Limitations

This is a mathematical idealization; neither a physical DNA sensor nor a validated performance improvement is claimed. No independent mathematical review has been performed. A prior equivalent formulation in less-indexed literature, or under an unexpected reduction to another labeled-walk channel, cannot be excluded. The proof does not imply comparable formulas for larger alphabets, longer windows, or circular boundary conditions.

## References

1. F. Weindel, A. L. Gimpel, R. N. Grass, R. Heckel, *Embracing Errors Is More Efficient Than Avoiding Them Through Constrained Coding for DNA Data Storage*, arXiv:2308.05952 (first posted 2023-08-11). https://arxiv.org/abs/2308.05952
2. H. Wei, M. Schwartz, G. Ge, *Reconstruction from Noisy Substrings*, arXiv:2312.04790 (first posted 2023-12-08). https://arxiv.org/abs/2312.04790
3. J. Cahill, J. W. Iverson, D. G. Mixon, D. Packer, *Group-Invariant Max Filtering*, *Foundations of Computational Mathematics* (online 2024-05-17). https://doi.org/10.1007/s10208-024-09656-9
4. S. MacDonald, *Encoding subshifts through sliding block codes*, arXiv:2210.08150 (first posted 2022-10-15; later published in *Ergodic Theory and Dynamical Systems*). https://arxiv.org/abs/2210.08150
