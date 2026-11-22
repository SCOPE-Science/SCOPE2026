# Exact Fibonacci inverse fibers and singleton entropy for a constrained cyclic conjunction channel

## Finding
For every integer \(n\ge5\), let \(X_n\) consist of indexed cyclic binary words of length \(n\) avoiding the consecutive factor \(111\) at every cyclic position. Apply the deterministic indexed coincidence read \(\Phi_n(x)_i=x_i x_{i+1}\), with indices reduced modulo \(n\). The following gives a complete inverse-list classification.

An output \(y\) is attainable if and only if its one-positions have cyclic separations at least three (including the all-zero output). If \(y\ne0^n\) has \(k\ge1\) ones and successive cyclic distances \(d_1,\ldots,d_k\ge3\) summing to \(n\), then
\[
|\Phi_n^{-1}(y)|=\prod_{j=1}^{k}F_{d_j-2},
\]
where \(F_0=0,F_1=1\) and \(F_{t+2}=F_{t+1}+F_t\). For the all-zero output, \(|\Phi_n^{-1}(0^n)|=F_{n-1}+F_{n+1}\).

Writing \(T_n=|\Phi_n(X_n)|\) and \(U_n=|\{y\in\Phi_n(X_n):|\Phi_n^{-1}(y)|=1\}|\), one has
\[
T_n=1+\sum_{k=1}^{\lfloor n/3\rfloor}\frac nk\binom{n-2k-1}{k-1},\qquad
U_n=\sum_{\lceil n/4\rceil\le k\le\lfloor n/3\rfloor}\frac nk\binom{k}{n-3k}.
\]
Their rational generating functions, with the natural extension of these counts to positive lengths, are
\[
\sum_{n\ge1}T_nz^n=\frac{z+3z^3}{1-z-z^3},\qquad
\sum_{n\ge1}U_nz^n=\frac{3z^3+4z^4}{1-z^3-z^4}.
\]
The largest inverse fiber is uniquely \(0^n\), of cardinality \(F_{n-1}+F_{n+1}\). Among other outputs the maximum is \(F_{n-2}\), attained precisely by the \(n\) outputs with a single one. In particular, the largest zero-error codebook for the noiseless indexed read \(\Phi_n\) has size \(T_n\).

If \(\lambda\) denotes the positive root of \(\lambda^3=\lambda^2+1\) and \(\alpha\) the positive root of \(\alpha^4=\alpha+1\), then the proportion of *attainable outputs* with a unique input preimage satisfies
\[
\frac{U_n}{T_n}\sim\left(\frac{\alpha}{\lambda}\right)^n\longrightarrow0.
\]
Here \(\lambda\approx1.465571\) and \(\alpha\approx1.220744\).

## Assumptions and scope
All words are indexed, so cyclic rotations are different when their coordinate vectors differ; no quotient by rotation is taken. The binary source forbids only runs of at least three consecutive ones, including wraparound, and does not restrict zero runs. The read is noiseless, simultaneously reports all \(n\) adjacent products, and is not a histogram or a multiset. Each inverse fiber is counted among the constrained source \(X_n\), not among arbitrary binary words. The stated formulas are for all integers \(n\ge5\). The generating-function trace identities use formally extended positive-length sequences and need not define the intended channel at smaller ring lengths.

## Proof
**Reachability.** If \(y_i=1\), then \(x_i=x_{i+1}=1\). Hence \(y_{i+1}=1\) or \(y_{i+2}=1\) would force a cyclic occurrence of \(111\). Consequently distinct output-one coordinates have forward cyclic gap at least three. Conversely, given any nonzero \(y\) whose marked coordinates have this separation, put ones at each marked coordinate and its successor and zero everywhere else. This gives a source without \(111\) and with precisely the prescribed output. The all-zero output has the all-zero input.

**Inverse fibers.** For \(y=0^n\), the input can have no adjacent pair of ones. The number of cyclic independent sets on a labelled \(n\)-cycle is \(F_{n-1}+F_{n+1}\), obtained by splitting on the initial bit. For each pair of consecutive one-marks at distance \(d\), the two prescribed occupied input pairs force zeros immediately beyond the adjacent pairs. The remaining \(d-4\) free input coordinates (none when \(d=3\) or \(4\)) form a linear string with no adjacent ones. For \(d\ge4\), there are \(F_{d-2}\) such strings, and for \(d=3\) exactly one, again \(F_1=1\). All gaps are disjoint and independent, so multiplication yields the fiber formula. Every such input avoids \(111\) automatically.

**Image and singleton populations.** For exactly \(k\) output ones, each cyclic one-to-one distance is an integer at least three, and their sum is \(n\). Subtracting three from each distance shows that the number of ordered gap \(k\)-tuples is \(\binom{n-2k-1}{k-1}\). Choosing a starting marked site gives \(n\) choices; each indexed output is then counted exactly \(k\) times. Summing and adjoining the zero word proves \(T_n\). A positive output has a singleton fiber exactly when all factors \(F_{d-2}\) equal one, or equivalently all gaps are three or four. For a fixed \(k\), exactly \(n-3k\) gaps have size four, giving \(\binom{k}{n-3k}\) compositions. Counting marked starts as above proves \(U_n\). The zero output has more than one predecessor for every \(n\ge5\).

For any finite set of permitted gap lengths with generating polynomial \(W(z)\), the pointed cyclic composition enumerator is \(zW'(z)/(1-W(z))\): point a selected mark, record its following gap, and sum over the remaining ordered gaps. Here the image-nonzero gaps have \(W(z)=z^3/(1-z)\), and singleton gaps have \(W(z)=z^3+z^4\). Adding the zero output contributes \(z/(1-z)\) to the image count series. Simplifying yields the two displayed rational functions. Equivalently, these are the logarithmic derivatives of \(1-z-z^3\) and \(1-z^3-z^4\); their coefficients are the power sums of their respective inverse roots.

**Extrema.** A singleton-marker output has one gap \(n\), and hence \(F_{n-2}\) predecessors. If there are \(k\ge2\) marks, the elementary Fibonacci inequality \(F_aF_b\le F_{a+b-1}\) for all integers \(a,b\ge1\), applied repeatedly, gives
\[
\prod_{j=1}^k F_{d_j-2}\le F_{\sum_j(d_j-2)-(k-1)}=F_{n-3k+1}\le F_{n-5}<F_{n-2}.
\]
The pairwise inequality follows directly by concatenating independent-set strings on paths, or by the Fibonacci addition identity \(F_{a+b-1}=F_aF_b+F_{a-1}F_{b-1}\), with the second term nonnegative. (For \(k\ge2\), the domain guarantees \(n\ge6\).) Thus precisely the one-marker outputs maximize positive fibers. The zero fiber \(F_{n-1}+F_{n+1}\) strictly exceeds \(F_{n-2}\), establishing the unique global maximum.

**Asymptotics and code capacity.** The rational series for \(T_n\) and \(U_n\) are logarithmic derivatives of monic characteristic polynomials with unique positive dominant roots \(\lambda\) and \(\alpha\), respectively. Since all other roots have strictly smaller modulus (both polynomials are primitive companion-matrix characteristic polynomials), one has \(T_n\sim\lambda^n\) and \(U_n\sim\alpha^n\) with leading coefficient exactly one. As \(1<\alpha<\lambda\), their ratio tends to zero at the displayed exponential rate. Finally, any injective subset of \(X_n\) contains at most one member per output fiber; choosing one member from every nonempty fiber attains \(T_n\).

## Verification
The standalone Python 3 script `VERIFY.py` uses no external dependencies. It independently enumerates all input configurations and possible outputs at each length \(5\le n\le17\), checking every claimed inverse fiber, the image and singleton counts, and both extremal multiplicities. It separately tests the two rational generating-function recurrences against the finite-sum formulas through length \(122\). Run `python3 VERIFY.py` in the directory containing this file and `VERIFY.py`. Successful execution prints a PASS message. These computations are finite corroboration; the proof above supplies the all-length argument.

## Relationship to prior work
Stanovnik, Moškon and Mraz study cyclic run restrictions in non-overlapping codes and enumerate permitted cyclic words, but their objective is constructing and bounding *cross-bifix-free* codebooks, not the exact inverse fibers of a local deterministic observation. MacDonald proves an embedding theorem for general factor maps, not this indexed finite-length fiber spectrum. Fukś gives preimage-count sequences for iterates of elementary cellular automata on short target blocks, including rule 136, rather than the present all-target, one-step, cyclic, run-constrained distribution. Counting preimages by transfer matrices in unrestricted cellular automata is established background, not a new general principle claimed here. No general novelty claim is made for Fibonacci/Lucas or for the abstract cyclic-composition counting method.

## Limitations
The results are for one simultaneous adjacent-AND read and exactly the one-sided cyclic \(111\)-forbidden source; they do not cover nonindexed necklaces, noisy reads, longer windows, or multiple temporal iterations. The explicit fiber-count list does not specify an efficient ranked encoder, although the image count establishes combinatorial zero-error capacity. The finite checks are not independent mathematical certification. Earlier equivalent expressions under transfer-matrix or shift-of-finite-type terminology may exist beyond the inspected literature.

## References
- L. Stanovnik, M. Moškon and M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, arXiv:2410.18458v1 (first posted 24 October 2024); later in *Computational and Applied Mathematics* 44 (2025), article 109, doi:10.1007/s40314-024-03055-0. Primary MSC 94B25.
- S. MacDonald, *Encoding subshifts through sliding block codes*, arXiv:2210.08150 (first posted 15 October 2022), *Ergodic Theory and Dynamical Systems* 44 (2024), 1609–1628.
- H. Fukś, *Sequences of Preimages in Elementary Cellular Automata*, *Complex Systems* 14 (2003), 29–43, doi:10.25088/ComplexSystems.14.1.29.
